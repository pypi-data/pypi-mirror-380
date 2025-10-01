import json
from typing import Any

import pytest

from .client import ModelPricingClient
from .models import EstimateResponse
from .errors import Unauthorized, ValidationError, ServerError


class DummyResponse:
    def __init__(self, status_code: int, json_data: Any = None, text: str = "") -> None:
        self.status_code = status_code
        self._json_data = json_data
        self.text = text

    def json(self) -> Any:
        if self._json_data is None:
            raise ValueError("No JSON")
        return self._json_data


class DummySession:
    def __init__(self, response: DummyResponse) -> None:
        self._response = response
        self.last_request = None
        self.call_count = 0

    def post(self, url, json=None, headers=None, timeout=None):
        self.call_count += 1
        self.last_request = {"url": url, "json": json, "headers": headers, "timeout": timeout}
        return self._response


class FailThenSucceedSession:
    """Session that fails N times before succeeding"""

    def __init__(self, fail_count: int, final_response: DummyResponse) -> None:
        self._fail_count = fail_count
        self._final_response = final_response
        self.call_count = 0

    def post(self, url, json=None, headers=None, timeout=None):
        self.call_count += 1
        if self.call_count <= self._fail_count:
            # Return 5xx error to trigger retry
            return DummyResponse(503, {"error": "Service Unavailable"}, "Service Unavailable")
        return self._final_response


def test_estimate_success():
    response = DummyResponse(
        200,
        {
            "total": 0.01234,
            "breakdown": {
                "input": {"unit": "per-1M-input", "branch": "gpt-4o-mini", "qty": 10, "rate": 1, "subtotal": 0.00001},
                "output": {"unit": "per-1M-output", "branch": "gpt-4o-mini", "qty": 20, "rate": 2, "subtotal": 0.00002},
            },
            "model": "gpt-4o-mini",
            "traceId": None,
        },
    )
    session = DummySession(response)
    client = ModelPricingClient(api_key="test", base_url="https://api.modelpricing.ai", session=session)
    result = client.estimate(model="gpt-4o-mini", tokens_in=10, tokens_out=20)
    assert isinstance(result, EstimateResponse)
    assert result.total == 0.01234
    assert session.last_request["url"].endswith("/v1/estimate")
    assert session.last_request["headers"]["Authorization"] == "Bearer test"
    assert session.last_request["json"]["metrics"] == {"tokensIn": 10, "tokensOut": 20}


def test_estimate_unauthorized():
    session = DummySession(DummyResponse(401, {"error": "Unauthorized"}))
    client = ModelPricingClient(api_key="bad", session=session)
    with pytest.raises(Unauthorized):
        client.estimate(model="m", tokens_in=1, tokens_out=1)


def test_estimate_validation_error():
    session = DummySession(DummyResponse(422, {"error": "Invalid request", "details": "model not found"}))
    client = ModelPricingClient(api_key="test", session=session)
    with pytest.raises(ValidationError) as exc:
        client.estimate(model="bad-model", tokens_in=1, tokens_out=1)
    assert "model not found" in str(exc.value)


def test_retry_on_server_error():
    """Test that client retries on 5xx errors"""
    success_response = DummyResponse(
        200,
        {
            "total": 0.001,
            "breakdown": {
                "input": {"unit": "per-1M-input", "branch": "gpt-4o-mini", "qty": 10, "rate": 1, "subtotal": 0.00001},
                "output": {"unit": "per-1M-output", "branch": "gpt-4o-mini", "qty": 20, "rate": 2, "subtotal": 0.00002},
            },
            "model": "gpt-4o-mini",
            "traceId": None,
        },
    )
    # Fail twice, then succeed on third attempt
    session = FailThenSucceedSession(fail_count=2, final_response=success_response)
    client = ModelPricingClient(api_key="test", session=session, max_retries=3)
    result = client.estimate(model="gpt-4o-mini", tokens_in=10, tokens_out=20)
    assert isinstance(result, EstimateResponse)
    assert result.total == 0.001
    # Should have been called 3 times (2 failures + 1 success)
    assert session.call_count == 3


def test_retry_exhausted():
    """Test that client raises error after max retries"""
    session = DummySession(DummyResponse(503, {"error": "Service Unavailable"}, "Service Unavailable"))
    client = ModelPricingClient(api_key="test", session=session, max_retries=2)
    with pytest.raises(ServerError):
        client.estimate(model="m", tokens_in=1, tokens_out=1)
    # Should have been called 2 times (max_retries)
    assert session.call_count == 2


def test_no_retry_on_4xx():
    """Test that 4xx errors are not retried"""
    session = DummySession(DummyResponse(404, {"error": "Not found"}))
    client = ModelPricingClient(api_key="test", session=session, max_retries=3)
    with pytest.raises(Exception):  # NotFound or ValidationError
        client.estimate(model="m", tokens_in=1, tokens_out=1)
    # Should only be called once (no retry on 4xx)
    assert session.call_count == 1


def test_max_retries_config():
    """Test that max_retries can be configured"""
    client = ModelPricingClient(api_key="test", max_retries=5)
    assert client.max_retries == 5

    client_default = ModelPricingClient(api_key="test")
    assert client_default.max_retries == 3
