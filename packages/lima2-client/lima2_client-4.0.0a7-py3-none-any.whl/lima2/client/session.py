# This file is part of the Lima2 project
#
# Copyright (c) 2020-2024 Beamline Control Unit, ESRF
# Distributed under the MIT licence. See LICENSE for more info.

"""Conductor client session."""

import logging
from typing import Any

import requests

from lima2.client.exceptions import ConductorConnectionError, MalformedConductorResponse
from lima2.common.exceptions import deserialize

logger = logging.getLogger(__name__)


def decode_error(response: requests.Response) -> Exception:
    """Decode an error contained in the conductor's HTTP response.

    Returns an exception instance.

    Raises:
      MalformedConductorResponse: The response contains an invalid JSON
        payload, or has missing keys, or cannot be deserialized into an
        exception.
    """

    try:
        ser_exc = response.json()
    except requests.JSONDecodeError as e:
        raise MalformedConductorResponse(
            f"Conductor returned a {response.status_code} "
            f"error, but the payload isn't valid json.\nContent: {repr(response.content)}\n"
            f"See decoding error above.",
        ) from e

    try:
        exc = deserialize(ser_exc=ser_exc)
    except KeyError as e:
        raise MalformedConductorResponse(
            f"Conductor returned a {response.status_code} "
            f"error with a valid json payload, but key {e} is missing.\n"
            f"Payload: {repr(ser_exc)}",
        ) from None
    except Exception as e:
        raise MalformedConductorResponse(
            f"Could not deserialize exception received from conductor:\n"
            f"Payload: {repr(ser_exc)}"
        ) from e

    logger.debug("".join(ser_exc["trace"]))

    return exc


class ConductorSession:
    def __init__(self, hostname: str, port: int) -> None:
        self.hostname = hostname
        self.port = port
        self.session = requests.Session()

    @property
    def base_url(self) -> str:
        return f"http://{self.hostname}:{self.port}"

    def get(self, endpoint: str, *args: Any, **kwargs: Any) -> requests.Response:
        """Make a GET request at /{endpoint}.

        If an error occurred on the conductor side, try to deserialize the
        payload into an appropriate exception. See lima2.common.exceptions.

        Raises:
          ConductorConnectionError: The conductor failed to respond.
          MalformedConductorResponse: The status code is 400, but the
            contained payload cannot be interpreted.
          NotImplementedError: The status code is neither 200 nor 400.
        """
        try:
            res = self.session.get(f"{self.base_url}{endpoint}", *args, **kwargs)
        except requests.ConnectionError as e:
            raise ConductorConnectionError(
                f"Conductor server at {self.base_url} is unreachable"
            ) from e

        if res.status_code == 200:
            return res
        elif res.status_code == 400:
            raise decode_error(response=res)
        else:
            raise NotImplementedError(
                f"Unexpected error code {res.status_code}. Payload: {res.content!r}"
            )

    def post(self, endpoint: str, *args: Any, **kwargs: Any) -> requests.Response:
        """Make a POST request at /{endpoint}.

        If an error occurred on the conductor side, try to deserialize the
        payload into an appropriate exception. See lima2.common.exceptions.

        Raises:
          ConductorConnectionError: The conductor failed to respond.
          MalformedConductorResponse: The status code is 400, but the
            contained payload cannot be interpreted.
          NotImplementedError: The status code is neither 202 nor 400.
        """
        try:
            res = self.session.post(f"{self.base_url}{endpoint}", *args, **kwargs)
        except requests.ConnectionError as e:
            raise ConductorConnectionError(
                f"Conductor server at {self.base_url} is unreachable"
            ) from e

        if res.status_code == 202:
            return res
        elif res.status_code == 400:
            raise decode_error(response=res)
        else:
            raise NotImplementedError(
                f"Unexpected error code {res.status_code}. Payload: {res.content!r}"
            )
