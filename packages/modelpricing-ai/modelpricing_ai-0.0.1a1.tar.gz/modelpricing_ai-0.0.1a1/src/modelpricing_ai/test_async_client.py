import asyncio
from typing import Any

import pytest

from .async_client import AsyncModelPricingClient
from .models import EstimateResponse
from .errors import Unauthorized, ValidationError, ServerError


class DummyAiohttpResponse:
    def __init__(self, status: int, json_data: Any = None, text: str = "") -> None:
        self.status = status
        self._json_data = json_data
        self._text = text

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        return False

    async def json(self):
        if self._json_data is None:
            raise ValueError("No JSON")
        return self._json_data

    async def text(self):
        return self._text


class DummyAiohttpSession:
    def __init__(self, response: DummyAiohttpResponse) -> None:
        self._response = response
        self.closed = False
        self.last_request = None
        self.call_count = 0

    async def close(self):
        self.closed = True

    def post(self, url, json=None, headers=None):
        self.call_count += 1
        self.last_request = {"url": url, "json": json, "headers": headers}
        return self._response


class FailThenSucceedAiohttpSession:
    """Session that fails N times before succeeding"""

    def __init__(self, fail_count: int, final_response: DummyAiohttpResponse) -> None:
        self._fail_count = fail_count
        self._final_response = final_response
        self.call_count = 0
        self.closed = False

    async def close(self):
        self.closed = True

    def post(self, url, json=None, headers=None):
        self.call_count += 1
        if self.call_count <= self._fail_count:
            return DummyAiohttpResponse(503, {"error": "Service Unavailable"}, "Service Unavailable")
        return self._final_response


@pytest.mark.asyncio
async def test_async_estimate_success():
    response = DummyAiohttpResponse(
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
    session = DummyAiohttpSession(response)
    client = AsyncModelPricingClient(api_key="test", session=session)
    result = await client.estimate(model="gpt-4o-mini", tokens_in=10, tokens_out=20)
    assert isinstance(result, EstimateResponse)
    assert result.total == 0.001
    assert session.last_request["url"].endswith("/v1/estimate")
    assert session.last_request["headers"]["Authorization"] == "Bearer test"


@pytest.mark.asyncio
async def test_async_estimate_unauthorized():
    session = DummyAiohttpSession(DummyAiohttpResponse(401, {"error": "Unauthorized"}))
    client = AsyncModelPricingClient(api_key="bad", session=session)
    with pytest.raises(Unauthorized):
        await client.estimate(model="m", tokens_in=1, tokens_out=1)


@pytest.mark.asyncio
async def test_async_estimate_validation_error():
    session = DummyAiohttpSession(DummyAiohttpResponse(422, {"error": "Invalid request", "details": "model not found"}))
    client = AsyncModelPricingClient(api_key="test", session=session)
    with pytest.raises(ValidationError) as exc:
        await client.estimate(model="bad-model", tokens_in=1, tokens_out=1)
    assert "model not found" in str(exc.value)


@pytest.mark.asyncio
async def test_async_retry_on_server_error():
    """Test that async client retries on 5xx errors"""
    success_response = DummyAiohttpResponse(
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
    session = FailThenSucceedAiohttpSession(fail_count=2, final_response=success_response)
    client = AsyncModelPricingClient(api_key="test", session=session, max_retries=3)
    result = await client.estimate(model="gpt-4o-mini", tokens_in=10, tokens_out=20)
    assert isinstance(result, EstimateResponse)
    assert result.total == 0.001
    # Should have been called 3 times (2 failures + 1 success)
    assert session.call_count == 3


@pytest.mark.asyncio
async def test_async_retry_exhausted():
    """Test that async client raises error after max retries"""
    session = DummyAiohttpSession(DummyAiohttpResponse(503, {"error": "Service Unavailable"}, "Service Unavailable"))
    client = AsyncModelPricingClient(api_key="test", session=session, max_retries=2)
    with pytest.raises(ServerError):
        await client.estimate(model="m", tokens_in=1, tokens_out=1)
    # Should have been called 2 times (max_retries)
    assert session.call_count == 2


@pytest.mark.asyncio
async def test_async_no_retry_on_4xx():
    """Test that 4xx errors are not retried"""
    session = DummyAiohttpSession(DummyAiohttpResponse(404, {"error": "Not found"}))
    client = AsyncModelPricingClient(api_key="test", session=session, max_retries=3)
    with pytest.raises(Exception):  # NotFound or ValidationError
        await client.estimate(model="m", tokens_in=1, tokens_out=1)
    # Should only be called once (no retry on 4xx)
    assert session.call_count == 1


@pytest.mark.asyncio
async def test_async_max_retries_config():
    """Test that max_retries can be configured"""
    client = AsyncModelPricingClient(api_key="test", max_retries=5)
    assert client.max_retries == 5

    client_default = AsyncModelPricingClient(api_key="test")
    assert client_default.max_retries == 3
