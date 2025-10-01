from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Protocol

import requests
from pydantic import TypeAdapter

from xq_cloud.schemas import BackendInfo


class XQCloudApiError(Exception):
    """Generic API error raised for non-success HTTP responses."""

    def __init__(self, message: str, *, status_code: int, response_body: Any | None = None) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body


class XQCloudNotFoundError(XQCloudApiError):
    """Raised when a resource is not found (404)."""

    pass


@dataclass
class ResultStatus:
    """Represents the status of a job execution."""

    status: str  # "running" or "completed" # TODO(agent): Use an Enum here
    result: Optional[Dict[str, float]] = None
    error: Optional[str] = None


class HttpSession(Protocol):
    """
    Abstraction over an HTTP session, compatible with requests.Session and FastAPI's TestClient.
    """

    def get(self, url: str, *, headers: Optional[Dict[str, str]] = None, timeout: Optional[float] = None) -> Any: ...
    def post(
        self,
        url: str,
        *,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[float] = None,
    ) -> Any: ...


class XQCloudClient:
    """Synchronous client for the XQ Cloud API.

    This client is designed to work with both real servers (via requests.Session)
    and FastAPI's TestClient (which subclasses requests.Session). For tests,
    pass the TestClient instance as the ``session`` parameter.
    """

    def __init__(
        self,
        base_url: str,
        *,
        api_key: str,
        session: Optional[HttpSession] = None,
        timeout_seconds: float = 30.0,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.session = session or requests.Session()
        self.timeout_seconds = timeout_seconds

    def list_backends(self) -> List[BackendInfo]:
        """Return available backends."""
        url = f"{self.base_url}/backends"
        response = self.session.get(
            url,
            headers=self.auth_headers(),
            timeout=self.timeout_seconds,
        )
        if response.status_code != 200:
            self.raise_for_status(response)
        data = response.json()
        return TypeAdapter(list[BackendInfo]).validate_python(data)

    def queue_circuit(self, qasm: str, *, backend: str) -> int:
        """Submit a job to ``backend``'s execution queue and return its job id."""
        url = f"{self.base_url}/queue"
        response = self.session.post(
            url,
            json={"qasm": qasm, "backend": backend},
            headers=self.auth_headers(),
            timeout=self.timeout_seconds,
        )
        if response.status_code != 200:
            self.raise_for_status(response)
        body = response.json()
        return int(body["job_id"])

    def get_queue_position(self, job_id: int) -> int:
        """Get the current position in the queue for a job (0 if not queued)."""
        url = f"{self.base_url}/queue/{job_id}"
        response = self.session.get(
            url,
            headers=self.auth_headers(),
            timeout=self.timeout_seconds,
        )
        if response.status_code == 404:
            raise XQCloudNotFoundError("Job not found", status_code=404, response_body=response.text)
        if response.status_code != 200:
            self.raise_for_status(response)
        body = response.json()
        return int(body.get("position", 0))

    def get_result(self, job_id: int) -> ResultStatus:
        """Check the result of a job execution.

        Returns ResultStatus where ``status`` is:
        - "running" while the circuit is still executing
        - "completed" once finished, with ``result`` and optional ``error`` fields
        """
        url = f"{self.base_url}/result/{job_id}"
        response = self.session.get(
            url,
            headers=self.auth_headers(),
            timeout=self.timeout_seconds,
        )
        if response.status_code == 404:
            raise XQCloudNotFoundError("Job not found", status_code=404, response_body=response.text)
        if response.status_code == 202:
            return ResultStatus(status="running")
        if response.status_code != 200:
            self.raise_for_status(response)
        body = response.json()
        return ResultStatus(status="completed", result=body.get("result"), error=body.get("error"))

    def wait_for_result(
        self,
        job_id: int,
        *,
        poll_interval_seconds: float = 0.1,
        timeout_seconds: float = 30.0,
    ) -> Dict[str, float]:
        """Poll until the job is completed or timeout is reached.

        Raises TimeoutError if the timeout elapses before completion.
        Raises XQCloudApiError if the API returns a non-success status.
        Raises XQCloudApiError if the job finished with an error.
        Returns the result probabilities dictionary on success.
        """
        start = time.monotonic()
        while True:
            status = self.get_result(job_id)
            if status.status == "completed":
                if status.error:
                    raise XQCloudApiError(
                        f"Job {job_id} failed: {status.error}", status_code=200, response_body=status.error
                    )
                return status.result or {}

            if time.monotonic() - start > timeout_seconds:
                raise TimeoutError(f"Timed out waiting for result of job {job_id}")
            time.sleep(poll_interval_seconds)

    def auth_headers(self) -> Dict[str, str]:
        return {"x-key": self.api_key}

    def raise_for_status(self, response: requests.Response) -> None:
        try:
            detail = response.json()
        except Exception:
            detail = response.text
        raise XQCloudApiError(
            f"HTTP {response.status_code} error for {response.request.method} {response.request.url}",
            status_code=response.status_code,
            response_body=detail,
        )
