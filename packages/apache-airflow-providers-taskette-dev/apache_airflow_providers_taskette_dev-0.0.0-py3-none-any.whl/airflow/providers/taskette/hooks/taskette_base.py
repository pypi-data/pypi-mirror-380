from __future__ import annotations

import copy
from functools import cached_property
from typing import TYPE_CHECKING, Any

from tenacity import (  # AsyncRetrying,; RetryError,; Retrying,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential,
)

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
        self.oauth_tokens: dict[str, dict] = {}
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
