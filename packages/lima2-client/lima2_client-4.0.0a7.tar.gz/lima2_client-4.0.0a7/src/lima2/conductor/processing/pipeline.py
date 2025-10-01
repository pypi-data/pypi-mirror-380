# This file is part of the Lima2 project
#
# Copyright (c) 2020-2024 Beamline Control Unit, ESRF
# Distributed under the MIT licence. See LICENSE for more info.

"""Lima2 pipeline base class.

An instance of Pipeline represents one processing pipeline, possibly distributed across multiple
Lima2 receivers. The processing is assumed to be the same across all receivers.

It has knowledge of the topology, and therefore can fetch a frame given a global
frame index, and provide aggregated progress counters during/after an acquisition.
"""

import asyncio
import logging
import traceback
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, AsyncIterator, Awaitable
from uuid import UUID

import numpy as np
import numpy.typing as npt

from lima2.common import progress_counter
from lima2.common.exceptions import Lima2LookupError
from lima2.common.progress_counter import ProgressCounter, SingleCounter
from lima2.common.types import (
    FrameChannel,
    FrameInfo,
    FrameSource,
    ReducedDataSource,
    SavingParams,
)
from lima2.conductor.processing.master_file import (
    MasterFileGenerator,
    MasterFileMetadata,
)
from lima2.conductor.processing.reduced_data import ReducedData
from lima2.conductor.tango.processing import ProcessingErrorEvent, TangoProcessing
from lima2.conductor.topology import (
    DynamicDispatch,
    FrameMapping,
    GlobalIdx,
    LocalIdx,
    LookupTable,
    ReceiverIdx,
    RoundRobin,
    SingleReceiver,
    Topology,
)

logger = logging.getLogger(__name__)


async def single_receiver_frame_iterator(
    device: TangoProcessing,
    fetch_interval_s: float,
    stop_evt: asyncio.Event,
) -> AsyncIterator[FrameMapping]:
    num_frames = np.uint32(0)

    while True:
        # NOTE(mdu) nb_frames_source is present on all pipelines (cuda,
        # failing, legacy, smx, xpcs).
        nfs = (await device.progress_counters())["nb_frames_source"]

        if stop_evt.is_set() and num_frames >= nfs:
            logger.info(f"Breaking frame_idx_iterator at {num_frames}")
            break

        while num_frames < nfs:
            yield FrameMapping(
                receiver_idx=ReceiverIdx(np.uint32(0)),
                local_idx=LocalIdx(num_frames),
                frame_idx=GlobalIdx(num_frames),
            )
            num_frames += 1

        await asyncio.sleep(fetch_interval_s)


async def round_robin_frame_iterator(
    devices: list[TangoProcessing],
    ordering: list[int],
    fetch_interval_s: float,
    stop_evt: asyncio.Event,
) -> AsyncIterator[FrameMapping]:
    local_idx: npt.NDArray[LocalIdx] = np.array([0 for _ in devices])

    while True:
        # NOTE(mdu) nb_frames_source is present on all pipelines (cuda,
        # failing, legacy, smx, xpcs).
        pcs = await asyncio.gather(*[dev.progress_counters() for dev in devices])
        nfs = [pc["nb_frames_source"] for pc in pcs]

        if stop_evt.is_set() and np.all(local_idx >= nfs):
            logger.info(
                f"Breaking frame_idx_iterator at {local_idx}, {nfs=}, "
                f"total={sum(local_idx)}"
            )
            break

        while np.any(local_idx < nfs):
            frame_idx = local_idx.sum()
            rcv_idx = ordering[frame_idx % len(devices)]

            yield FrameMapping(
                receiver_idx=rcv_idx,
                local_idx=local_idx[rcv_idx],
                frame_idx=frame_idx,
            )

            local_idx[rcv_idx] += 1

        await asyncio.sleep(fetch_interval_s)


@dataclass
class PipelineErrorEvent:
    """Structure passed to the registered callback upon error in the pipeline."""

    uuid: UUID
    device_name: str
    error_msg: str


class Pipeline:
    """A base class for all processing pipelines.

    Implements logic common to all processing pipelines.
    """

    FRAME_SOURCES: dict[str, FrameSource]
    """Map of available frame source names to a corresponding FrameSource descriptor.

    Definition in child classes is enforced by __init_subclass__().
    """

    REDUCED_DATA_SOURCES: dict[str, ReducedDataSource]
    """Map of available reduced data names to a corresponding ReducedDataSource descriptor.

    Definition in child classes is enforced by __init_subclass__().
    """

    TANGO_CLASS: str
    """Class name as defined on server side.

    Definition in child classes is enforced by __init_subclass__().
    """

    PROGRESS_INDICATOR: str
    """Name of the main progress counter.

    Definition in child classes is enforced by __init_subclass__().
    """

    @classmethod
    def __init_subclass__(cls) -> None:
        """Initialize a pipeline subclass."""
        if not hasattr(cls, "TANGO_CLASS"):
            raise ValueError(
                f"Pipeline subclass {cls} must define a TANGO_CLASS class member"
            )

        if not hasattr(cls, "FRAME_SOURCES"):
            raise ValueError(
                f"Pipeline subclass {cls} must define a FRAME_SOURCES class member"
            )

        if not hasattr(cls, "REDUCED_DATA_SOURCES"):
            raise ValueError(
                f"Pipeline subclass {cls} must define a REDUCED_DATA_SOURCES class member"
            )

        if not hasattr(cls, "PROGRESS_INDICATOR"):
            raise ValueError(
                f"Pipeline subclass {cls} must define a PROGRESS_INDICATOR class member"
            )

    def __init__(
        self,
        uuid: UUID,
        devices: list[TangoProcessing],
        topology: Topology,
        on_finished: Callable[[list[str]], Awaitable[None]],
        on_error: Callable[[PipelineErrorEvent], Awaitable[None]],
    ):
        """Construct a Pipeline object.

        Args:
            uuid: Unique identifer of the acquisition
            devices: Variable length processing device instances
            topology: Receiver topology
            on_finished: Async callback called when all devices are done processing
            on_error: Async callback called when an error event is received from
                one of the processing devices.
        """

        self.uuid = uuid
        self.devices: list[TangoProcessing] = devices
        self.topology = topology

        self.on_finished_callback = on_finished
        self.on_error_callback = on_error

        self.errors: list[str] = []
        """Holds processing error messages that occurred during the run, if any."""

        self.finished_devices: set[str] = set()
        """Set of names of processing devices which are done processing.

        Used to call the on_finished_callback when all devices are finished.
        """

        self.frame_infos: dict[str, FrameInfo] = {}
        """Dynamic frame info (shape, pixel type). Populated in connect()."""

        self.reduced_data = ReducedData(devices=self.devices)

        self.lut: LookupTable | None = None
        self.lut_task: asyncio.Task[None] | None = None

        self.master_file_generator = MasterFileGenerator()
        self.master_file_task: asyncio.Task[None] | None = None

        self.close_event = asyncio.Event()
        """
        Set in close(), used to stop the frame index iteration in single and
        round robin topologies.

        In dynamic dispatch, frame indices are fetched from each receiver to
        build the lookup table instead.
        """

        self.started = False
        """Set to True on start()."""

        self.closed = False
        """Set to True on close()."""

    async def connect(self) -> None:
        """Ping the devices, then subscribe to error/finished events.

        Should be called just after instantiating the Pipeline instance.
        """

        async def on_finished(device_name: str) -> None:
            """Adds a processing device to the finished_devices set.

            When the set is complete, call the on_finished callback registered to
            this pipeline instance (see constructor).
            """
            logger.info(f"Processing device {device_name} is done")
            self.finished_devices.add(device_name)

            if self.finished_devices == set([dev.name for dev in self.devices]):
                try:
                    await self.on_finished_callback(self.errors)
                except Exception:
                    logger.error(
                        f"Exception raised in pipeline {self.uuid} "
                        "on_finished callback:\n"
                        f"{traceback.format_exc()}"
                    )

        async def on_processing_error(evt: ProcessingErrorEvent) -> None:
            """Reports a processing error to the registered callback."""
            logger.warning(
                f"Error from processing device {evt.device_name}. "
                f"Reason: '{evt.error_msg}'"
            )
            self.errors.append(f"{evt.device_name}: {evt.error_msg}")

            pipeline_err_evt = PipelineErrorEvent(
                uuid=self.uuid, error_msg=evt.error_msg, device_name=evt.device_name
            )

            try:
                await self.on_error_callback(pipeline_err_evt)
            except Exception:
                logger.error(
                    f"Exception raised in pipeline {self.uuid} "
                    "on_error callback:\n"
                    f"{traceback.format_exc()}"
                )

        for device in self.devices:
            ping_us = await device.ping()
            logger.debug(f"Ping {device.name}: {ping_us}µs")
            await device.on_finished(on_finished)
            await device.on_error(on_processing_error)

        for name in self.FRAME_SOURCES.keys():
            # TODO(mdu) We should come up with a better mechanism for getting
            # the frame info for a specific frame source.
            if name == "input_frame":
                self.frame_infos[name] = await self.devices[0].input_frame_info()
            else:
                self.frame_infos[name] = await self.devices[0].processed_frame_info()

    @staticmethod
    def distribute_acq(
        cls: type["Pipeline"],
        ctl_params: dict[str, Any],
        acq_params: list[dict[str, Any]],
        proc_params: list[dict[str, Any]],
    ) -> tuple[dict[str, Any], list[dict[str, Any]], list[dict[str, Any]]]:
        """Initialize pipeline-specific parameters for distributed acquisition.

        It is implemented as static method so derived classes can access to the
        base class implemtation.
        """
        for i, proc in enumerate(proc_params):
            # Assign unique filename rank per receiver
            for source in cls.FRAME_SOURCES.values():
                if source.saving_channel is not None:
                    proc[source.saving_channel]["filename_rank"] = i

        return ctl_params, acq_params, proc_params

    async def frame_idx_iterator(
        self,
        fetch_interval_s: float,
        stop_evt: asyncio.Event,
    ) -> AsyncIterator[FrameMapping]:
        num_frames = 0

        iterator: AsyncIterator[FrameMapping]

        if type(self.topology) is SingleReceiver:
            iterator = single_receiver_frame_iterator(
                device=self.devices[0],
                fetch_interval_s=fetch_interval_s,
                stop_evt=stop_evt,
            )

        elif type(self.topology) is RoundRobin:
            iterator = round_robin_frame_iterator(
                devices=self.devices,
                ordering=self.topology.ordering,
                fetch_interval_s=fetch_interval_s,
                stop_evt=stop_evt,
            )

        elif type(self.topology) is DynamicDispatch:
            iterator = self.reduced_data.dynamic_index(
                fetch_interval_s=fetch_interval_s
            )

        async for mapping in iterator:
            yield mapping
            num_frames += 1

        logger.info(f"Frame index iterator done after {num_frames} frames")

    def prepare(
        self,
        acq_params: dict[str, Any],
        proc_params: dict[str, Any],
        det_info: dict[str, Any],
    ) -> None:
        """Prepare the reduced-data system and master file generator.

        Raises:
          RuntimeError: The reduced data system or master file
            generation failed to prepare.
        """

        num_frames = acq_params["acq"]["nb_frames"]

        if num_frames < 0:
            raise ValueError("Need either nb_frames > 0, or nb_frames == 0 (endless)")

        if num_frames == 0:
            # Pick a reasonably large initial buffer size for endless acquisition.
            size_hint = 32_768
        else:
            # Evenized num_frames
            size_hint = num_frames + num_frames % 2

        self.lut = LookupTable(size_hint=size_hint, num_receivers=len(self.devices))

        self.reduced_data.prepare(
            size_hint=size_hint,
            lookup=self.lut,
            roi_stats_params=proc_params.get("statistics"),
            profile_params=proc_params.get("profiles"),
            static_sources=self.REDUCED_DATA_SOURCES,
            fetch_interval_s=0.05,
        )

        frame_channels: dict[str, FrameChannel] = {}
        for name, source in self.FRAME_SOURCES.items():
            if source.saving_channel is not None:
                try:
                    sdict = proc_params[source.saving_channel]
                    sav_params = SavingParams(
                        base_path=sdict["base_path"],
                        filename_prefix=sdict["filename_prefix"],
                        file_exists_policy=sdict["file_exists_policy"],
                        nb_frames_per_file=sdict["nb_frames_per_file"],
                        nx_entry_name=sdict["nx_entry_name"],
                        nx_instrument_name=sdict["nx_instrument_name"],
                        nx_detector_name=sdict["nx_detector_name"],
                        enabled=sdict["enabled"],
                    )
                except KeyError as e:
                    raise RuntimeError(
                        f"Missing key {e} in proc_params['{source.saving_channel}'] "
                        "dictionary."
                    ) from None
            else:
                sav_params = None
            frame_channels[name] = (source, self.frame_infos[name], sav_params)

        self.master_file_generator.prepare(
            frame_channels=frame_channels,
            metadata=MasterFileMetadata(
                acq_params=acq_params, proc_params=proc_params, det_info=det_info
            ),
        )

    def start(self) -> None:
        """Start the reduced data fetching and master file generation tasks."""
        if not self.lut:
            raise RuntimeError("No LUT")

        frame_idx_it = self.frame_idx_iterator(
            fetch_interval_s=0.05,
            stop_evt=self.close_event,
        )
        self.lut_task = asyncio.create_task(
            self.lut.build(frame_idx_it), name="lut task"
        )

        self.reduced_data.start()

        self.master_file_task = asyncio.create_task(
            self.master_file_generator.write_master_files(
                num_receivers=len(self.devices), lut=self.lut
            ),
            name="master file task",
        )

        self.started = True

    async def close(self) -> None:
        """Wait for the reduced data subtasks to finish."""

        # Signal end to frame index iteration (single, round robin)
        self.close_event.set()

        await self.reduced_data.close()
        logger.info("Reduced data system closed")

        if self.lut_task:
            try:
                await self.lut_task
                logger.info("LUT task closed")
            except Exception:
                logger.error("LUT task failed: reduced data will be truncated")

        if self.master_file_task:
            await self.master_file_task
            logger.info("Master file task closed")

        self.closed = True

    def reduced_data_channels(
        self,
    ) -> dict[str, list[tuple[np.dtype[Any], tuple[int, ...]]]]:
        """Get the description of available reduced data streams."""
        return self.reduced_data.channel_info()

    def master_files(self) -> dict[str, str]:
        return {
            key: desc.master_file_path
            for key, desc in self.master_file_generator.mfd.items()
        }

    def is_running(self) -> bool:
        return self.started and not self.closed

    async def progress_counters(self) -> dict[str, ProgressCounter]:
        """Get the list of aggregated progress counters"""
        pcs_by_rcv = [await dev.progress_counters() for dev in self.devices]

        # Set of unique progress counter names
        pc_keys = set()
        for rcv_pcs in pcs_by_rcv:
            for k in rcv_pcs.keys():
                pc_keys.add(k)

        # Sanity check: all receivers have the same progress counters (assume homogeneous)
        # Perhaps not true in all future topologies
        for rcv in pcs_by_rcv:
            for key in pc_keys:
                assert key in rcv.keys()

        aggregated_pcs: dict[str, ProgressCounter] = {}
        for pc_key in pc_keys:
            single_counters = []
            for dev, pcs in zip(self.devices, pcs_by_rcv, strict=True):
                single_counters.append(
                    SingleCounter(name=pc_key, value=pcs[pc_key], source=dev.name)
                )

            aggregated_pcs[pc_key] = progress_counter.aggregate(
                single_counters=single_counters
            )

        return aggregated_pcs

    async def lookup_last(self) -> str:
        """Returns the url of the receiver who has processed the latest frame.

        Raises: Lima2LookupError if the frame cannot be looked up.
        """
        match self.topology:
            case SingleReceiver():
                return self.devices[0].name
            case RoundRobin() | DynamicDispatch():
                # Last processed frame index
                values = [
                    (await device.last_frames())["processed_idx"]
                    for device in self.devices
                ]

                if all([value < 0 for value in values]):
                    raise Lima2LookupError(
                        "Cannot lookup last frame: no frames processed yet."
                    )
                else:
                    # Take the receiver with most frames processed and ask it for the
                    # latest one
                    # Reverse the list so that rightmost receivers are favored.
                    values.reverse()
                    rcv_idx = len(values) - values.index(max(values)) - 1
                    return self.devices[rcv_idx].name
            case _:
                raise NotImplementedError

    def lookup(self, frame_idx: GlobalIdx) -> str:
        """Returns the url of the receiver that processed a given frame.

        Raises:
          Lima2LookupError (dynamic dispatch only): Frame not found.
        """
        if not self.lut:
            raise RuntimeError("No LUT")

        return self.devices[self.lut.lookup(frame_idx=frame_idx)].name

    def reduced_data_stream(
        self, name: str, channel_idx: int
    ) -> AsyncIterator[npt.NDArray[Any]]:
        """Get a reduced data stream as an async iterator of chunks."""
        return self.reduced_data.stream(name=name, channel_idx=channel_idx)
