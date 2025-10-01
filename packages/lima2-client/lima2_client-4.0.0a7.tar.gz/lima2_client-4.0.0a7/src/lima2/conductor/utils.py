# This file is part of the Lima2 project
#
# Copyright (c) 2020-2024 Beamline Control Unit, ESRF
# Distributed under the MIT license. See LICENSE for more info.

"""Utility functions"""

import asyncio
import contextlib
import logging
import time
import traceback
from collections.abc import Awaitable, Callable, Coroutine, Generator
from typing import Any, TypeVar

import jsonschema
import numpy as np
import numpy.typing as npt
from jsonschema import validators
from jsonschema.protocols import Validator

from lima2.common.types import pixel_type_to_np_dtype

logger = logging.getLogger(__name__)

DecoratedFunc = TypeVar("DecoratedFunc", bound=Callable[..., Any])


def validate(instance: dict[str, Any], schema: dict[str, Any]) -> None:
    """Lima2 param validation.

    Raises a ValidationError if `instance` fails the schema validation.

    Since JSON schema draft 6, a value is considered an "integer" if its
    fractional part is zero [1]. This means for example that 2.0 is considered
    an integer. Since we don't want floats to pass the validation where ints are
    expected, this function overrides this flexibility with a stricter type check.

    [1] https://json-schema.org/draft-06/json-schema-release-notes
    """

    def is_strict_int(_: Validator, value: Any) -> bool:
        return type(value) is int

    base_validator: type[Validator] = validators.validator_for(schema)
    strict_checker = base_validator.TYPE_CHECKER.redefine("integer", is_strict_int)
    strict_validator = validators.extend(base_validator, type_checker=strict_checker)  # type: ignore

    jsonschema.validate(instance, schema, cls=strict_validator)


def frame_info_to_shape_dtype(frame_info: dict[str, Any]) -> dict[str, Any]:
    return dict(
        shape=(
            frame_info["nb_channels"],
            frame_info["dimensions"]["y"],
            frame_info["dimensions"]["x"],
        ),
        dtype=pixel_type_to_np_dtype[frame_info["pixel_type"]],
    )


def naturalsize(size: int, decimal_places: int = 2) -> str:
    """Format a size."""
    size = float(size)
    for unit in ["B", "KiB", "MiB", "GiB", "TiB", "PiB"]:
        if size < 1024 or unit == "PiB":
            break
        size /= 1024
    return f"{size:.{decimal_places}f} {unit}"


class Ticker:
    """Execute an async callback at regular intervals."""

    def __init__(
        self,
        interval_s: float,
        callback: Callable[..., Awaitable[bool | None]],
        kwargs: dict[str, Any] = {},
        descr: str = "",
        skip_one: bool = False,
    ) -> None:
        self.task: asyncio.Task[None] | None = None
        self.interval_s = interval_s
        self.callback = callback
        self.kwargs = kwargs
        self.skip_one = skip_one
        if descr == "":
            self.descr = self.callback.__name__
        else:
            self.descr = descr

    async def _loop(self) -> None:
        if self.skip_one:
            await asyncio.sleep(self.interval_s)
        while True:
            start = time.perf_counter()
            try:
                stop = await self.callback(**self.kwargs)
                if stop:
                    break
            except Exception:
                logger.error(
                    f"Exception in ticker callback '{self.descr}': "
                    f"{traceback.format_exc()}"
                )
            delta = time.perf_counter() - start
            if delta >= self.interval_s:
                logger.warning(
                    f"Ticker callback '{self.descr}' took "
                    f"{(delta - self.interval_s)*1e3:.1f}ms "
                    f"longer than interval ({self.interval_s}s)"
                )
            await asyncio.sleep(max(0, self.interval_s - delta))

    @contextlib.contextmanager
    def context(self) -> Generator[None, None, None]:
        self.start()
        yield
        self.cancel()

    def start(self) -> None:
        self.task = asyncio.create_task(
            self._loop(), name=f"ticker({self.descr}, {self.interval_s})"
        )

    def cancel(self) -> None:
        if self.task:
            self.task.cancel()

    def done(self) -> bool:
        if self.task:
            return self.task.done()
        else:
            return False


def expand(array: npt.NDArray[Any], fill_value: Any = None) -> npt.NDArray[Any]:
    """Expands an array by a factor 2 along its first dimension."""

    if fill_value:
        ret = np.full(
            fill_value=fill_value,
            shape=(array.shape[0] * 2, *array.shape[1:]),
            dtype=array.dtype,
        )
    else:
        ret = np.empty(
            shape=(array.shape[0] * 2, *array.shape[1:]),
            dtype=array.dtype,
        )
    ret[: array.shape[0]] = array
    return ret


T = TypeVar("T")


async def gather_or(
    futures: list[Awaitable[T]], on_exception: Callable[[], T]
) -> list[T]:
    """Await a list of coroutines, replacing exceptions by on_exception()."""
    results: list[T | BaseException] = await asyncio.gather(
        *futures, return_exceptions=True
    )
    ret: list[T] = []
    for i, r in enumerate(results):
        if isinstance(r, BaseException):
            logger.error(
                f"Error awaiting future #{i} in gather_or: {r}\n"
                f"{''.join(traceback.format_exception(r))}"
            )
            ret.append(on_exception())
        else:
            ret.append(r)

    return ret


async def warn_if_hanging(coroutine: Coroutine[Any, Any, T], warn_every_s: float) -> T:
    """Await a coroutine forever, but log a warning periodically if it takes too long."""

    async def notify() -> None:
        logger.warning(
            f"{coroutine.__qualname__} has been working for {warn_every_s}s..."
        )

    with Ticker(interval_s=warn_every_s, callback=notify, skip_one=True).context():
        return await coroutine
