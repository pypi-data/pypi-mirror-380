from __future__ import annotations

import copy
import platform
from asyncio.exceptions import TimeoutError
from functools import cached_property
from typing import TYPE_CHECKING, Any
from urllib.parse import urlsplit

import aiohttp
import requests
from aiohttp.client_exceptions import ClientConnectorError
from airflow.exceptions import AirflowException
from airflow.providers_manager import ProvidersManager
from requests import PreparedRequest, exceptions as requests_exceptions
from requests.auth import AuthBase, HTTPBasicAuth
from requests.exceptions import JSONDecodeError
from tenacity import (
    AsyncRetrying,
    RetryError,
    Retrying,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential,
)

from airflow import __version__

try:
    from airflow.sdk import BaseHook
except ImportError:
    from airflow.hooks.base import BaseHook as BaseHook  # type: ignore

if TYPE_CHECKING:
    from airflow.models import Connection


class BaseTasketteHook(BaseHook):
    """
    Base for interaction with Taskette.

    :param taskette_conn_id: Taskette connection id
    :param timeout_seconds: The amount of time in seconds the requests library
        will wait before timing-out.
    :param retry_limit: The number of times to retry the connection in case of
        service outages.
    :param retry_delay: The number of seconds to wait between retries (it
        might be a floating point number).
    :param retry_args: An optional dictionary with arguments passed to ``tenacity.Retrying`` class.
    :param caller: The name of the operator that is calling the hook.
    """

    conn_name_attr: str = "taskette_conn_id"
    default_conn_name = "taskette_default"
    conn_type = "taskette"

    extra_parameters = [
        "token",
        "host",
    ]

    def __init__(
        self,
        taskette_conn_id: str = default_conn_name,
        timeout_seconds: int = 180,
        retry_limit: int = 3,
        retry_delay: float = 1.0,
        retry_args: dict[Any, Any] | None = None,
        caller: str = "Unknown",
    ) -> None:
        super().__init__()
        self.taskette_conn_id = taskette_conn_id
        self.timeout_seconds = timeout_seconds
        if retry_limit < 1:
            raise ValueError("Retry limit must be greater than or equal to 1")
        self.retry_limit = retry_limit
        self.retry_delay = retry_delay
        self.token_timeout_seconds = 10
        self.caller = caller
        self._metadata_cache: dict[str, Any] = {}
        self._metadata_expiry: float = 0
        self._metadata_ttl: int = 300

        def my_after_func(retry_state):
            self._log_request_error(retry_state.attempt_number, retry_state.outcome)

        if retry_args:
            self.retry_args = copy.copy(retry_args)
            self.retry_args["retry"] = retry_if_exception(self._retryable_error)
            self.retry_args["after"] = my_after_func
        else:
            self.retry_args = {
                "stop": stop_after_attempt(self.retry_limit),
                "wait": wait_exponential(min=self.retry_delay, max=(2**retry_limit)),
                "retry": retry_if_exception(self._retryable_error),
                "after": my_after_func,
            }

    @cached_property
    def taskette_conn(self) -> Connection:
        return self.get_connection(self.taskette_conn_id)  # type: ignore[return-value]

    def get_conn(self) -> Connection:
        return self.taskette_conn

    @cached_property
    def user_agent_header(self) -> dict[str, str]:
        return {"user-agent": self.user_agent_value}

    @cached_property
    def user_agent_value(self) -> str:
        manager = ProvidersManager()
        package_name = manager.hooks[BaseTasketteHook.conn_type].package_name  # type: ignore[union-attr]
        provider = manager.providers[package_name]
        version = provider.version
        python_version = platform.python_version()
        system = platform.system().lower()
        ua_string = f"taskette-airflow/{version} _/0.0.0 python/{python_version} os/{system} " f"airflow/{__version__} operator/{self.caller}"
        return ua_string

    @classmethod
    def get_ui_field_behaviour(cls) -> dict[str, Any]:
        """Get custom field behaviour."""
        return {
            "hidden_fields": ["port", "schema"],
            "relabeling": {"host": "Connection URL"},
        }

    @cached_property
    def host(self) -> str:
        if "host" in self.taskette_conn.extra_dejson:
            host = self._parse_host(self.taskette_conn.extra_dejson["host"])
        else:
            host = self._parse_host(self.taskette_conn.host)

        return host

    async def __aenter__(self):
        self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, *err):
        await self._session.close()
        self._session = None

    @staticmethod
    def _parse_host(host: str) -> str:
        """
        Parse host field data; this function is resistant to incorrect connection settings provided by users.

        For example -- when users supply ``https://xx.taskette.com`` as the
        host, we must strip out the protocol to get the host.::

            h = TasketteHook()
            assert h._parse_host('https://xx.taskette.com') == \
                'xx.taskette.com'

        In the case where users supply the correct ``xx.taskette.com`` as the
        host, this function is a no-op.::

            assert h._parse_host('xx.taskette.com') == 'xx.taskette.com'

        """
        urlparse_host = urlsplit(host).hostname
        if urlparse_host:
            # In this case, host = https://xx.taskette.com
            return urlparse_host
        # In this case, host = xx.taskette.com
        return host

    def _get_retry_object(self) -> Retrying:
        """
        Instantiate a retry object.

        :return: instance of Retrying class
        """
        return Retrying(**self.retry_args)

    def _a_get_retry_object(self) -> AsyncRetrying:
        """
        Instantiate an async retry object.

        :return: instance of AsyncRetrying class
        """
        return AsyncRetrying(**self.retry_args)

    def _get_token(self, raise_error: bool = False) -> str | None:
        if "token" in self.taskette_conn.extra_dejson:
            self.log.info("Using token auth. For security reasons, please set token in Password field instead of extra")
            return self.taskette_conn.extra_dejson["token"]
        raise AirflowException("Token authentication isn't configured")
        return None

    async def _a_get_token(self, raise_error: bool = False) -> str | None:
        if "token" in self.taskette_conn.extra_dejson:
            self.log.info("Using token auth. For security reasons, please set token in Password field instead of extra")
            return self.taskette_conn.extra_dejson["token"]
        raise AirflowException("Token authentication isn't configured")
        return None

    def _log_request_error(self, attempt_num: int, error: str) -> None:
        self.log.error("Attempt %s API Request to Taskette failed with reason: %s", attempt_num, error)

    def _endpoint_url(self, endpoint):
        port = f":{self.taskette_conn.port}" if self.taskette_conn.port else ""
        schema = self.taskette_conn.schema or "https"
        return f"{schema}://{self.host}{port}/{endpoint}"

    def _do_api_call(
        self,
        endpoint_info: tuple[str, str],
        json: dict[str, Any] | None = None,
        wrap_http_errors: bool = True,
    ):
        """
        Perform an API call with retries.

        :param endpoint_info: Tuple of method and endpoint
        :param json: Parameters for this API call.
        :return: If the api call returns a OK status code,
            this function returns the response in JSON. Otherwise,
            we throw an AirflowException.
        """
        method, endpoint = endpoint_info

        # Automatically prepend 'api/' prefix to all endpoint paths
        full_endpoint = f"api/{endpoint}"
        url = self._endpoint_url(full_endpoint)

        headers = {**self.user_agent_header}

        auth: AuthBase
        token = self._get_token()
        if token:
            auth = _TokenAuth(token)
        else:
            self.log.info("Using basic auth.")
            auth = HTTPBasicAuth(self.taskette_conn.login, self.taskette_conn.password)

        request_func: Any
        if method == "GET":
            request_func = requests.get
        elif method == "POST":
            request_func = requests.post
        elif method == "PATCH":
            request_func = requests.patch
        elif method == "DELETE":
            request_func = requests.delete
        else:
            raise AirflowException("Unexpected HTTP Method: " + method)

        try:
            for attempt in self._get_retry_object():
                with attempt:
                    self.log.debug(
                        "Initiating %s request to %s with payload: %s, headers: %s",
                        method,
                        url,
                        json,
                        headers,
                    )
                    response = request_func(
                        url,
                        json=json if method in ("POST", "PATCH") else None,
                        params=json if method == "GET" else None,
                        auth=auth,
                        headers=headers,
                        timeout=self.timeout_seconds,
                    )
                    self.log.debug("Response Status Code: %s", response.status_code)
                    self.log.debug("Response text: %s", response.text)
                    response.raise_for_status()
                    return response.json()
        except RetryError:
            raise AirflowException(f"API requests to Taskette failed {self.retry_limit} times. Giving up.")
        except requests_exceptions.HTTPError as e:
            if wrap_http_errors:
                msg = f"Response: {e.response.content.decode()}, Status Code: {e.response.status_code}"
                raise AirflowException(msg)
            raise

    async def _a_do_api_call(self, endpoint_info: tuple[str, str], json: dict[str, Any] | None = None):
        """
        Async version of `_do_api_call()`.

        :param endpoint_info: Tuple of method and endpoint
        :param json: Parameters for this API call.
        :return: If the api call returns a OK status code,
            this function returns the response in JSON. Otherwise, throw an AirflowException.
        """
        method, endpoint = endpoint_info

        full_endpoint = f"api/{endpoint}"
        url = self._endpoint_url(full_endpoint)

        headers = {**self.user_agent_header}

        auth: aiohttp.BasicAuth
        token = await self._a_get_token()
        if token:
            auth = BearerAuth(token)
        else:
            self.log.info("Using basic auth.")
            auth = aiohttp.BasicAuth(self.taskette_conn.login, self.taskette_conn.password)

        request_func: Any
        if method == "GET":
            request_func = self._session.get
        elif method == "POST":
            request_func = self._session.post
        elif method == "PATCH":
            request_func = self._session.patch
        else:
            raise AirflowException("Unexpected HTTP Method: " + method)
        try:
            async for attempt in self._a_get_retry_object():
                with attempt:
                    self.log.debug(
                        "Initiating %s request to %s with payload: %s, headers: %s",
                        method,
                        url,
                        json,
                        headers,
                    )
                    async with request_func(
                        url,
                        json=json,
                        auth=auth,
                        headers={**headers, **self.user_agent_header},
                        timeout=self.timeout_seconds,
                    ) as response:
                        self.log.debug("Response Status Code: %s", response.status)
                        self.log.debug("Response text: %s", response.text)
                        response.raise_for_status()
                        return await response.json()
        except RetryError:
            raise AirflowException(f"API requests to Taskette failed {self.retry_limit} times. Giving up.")
        except aiohttp.ClientResponseError as err:
            raise AirflowException(f"Response: {err.message}, Status Code: {err.status}")

    @staticmethod
    def _get_error_code(exception: BaseException) -> str:
        if isinstance(exception, requests_exceptions.HTTPError):
            try:
                jsn = exception.response.json()
                return jsn.get("error_code", "")
            except JSONDecodeError:
                pass

        return ""

    @staticmethod
    def _retryable_error(exception: BaseException) -> bool:
        if isinstance(exception, requests_exceptions.RequestException):
            if isinstance(exception, (requests_exceptions.ConnectionError, requests_exceptions.Timeout)) or (
                exception.response is not None
                and (
                    exception.response.status_code >= 500
                    or exception.response.status_code == 429
                    or (exception.response.status_code == 400 and BaseTasketteHook._get_error_code(exception) == "COULD_NOT_ACQUIRE_LOCK")
                )
            ):
                return True

        if isinstance(exception, aiohttp.ClientResponseError):
            if exception.status >= 500 or exception.status == 429:
                return True

        if isinstance(exception, (ClientConnectorError, TimeoutError)):
            return True

        return False


class _TokenAuth(AuthBase):
    """
    Helper class for requests Auth field.

    AuthBase requires you to implement the ``__call__``
    magic function.
    """

    def __init__(self, token: str) -> None:
        self.token = token

    def __call__(self, r: PreparedRequest) -> PreparedRequest:
        r.headers["Authorization"] = "Bearer " + self.token
        return r


class BearerAuth(aiohttp.BasicAuth):
    """aiohttp only ships BasicAuth, for Bearer auth we need a subclass of BasicAuth."""

    def __new__(cls, token: str) -> BearerAuth:
        return super().__new__(cls, token)  # type: ignore

    def __init__(self, token: str) -> None:
        self.token = token

    def encode(self) -> str:
        return f"Bearer {self.token}"
