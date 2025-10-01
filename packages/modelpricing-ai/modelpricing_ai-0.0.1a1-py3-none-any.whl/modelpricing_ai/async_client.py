import os
from typing import Any, Dict, Optional, Union

import aiohttp
from tenacity import (
    AsyncRetrying,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential_jitter,
)

from .errors import ModelPricingError, NotFound, ServerError, Unauthorized, ValidationError
from .models import EstimateResponse


class AsyncModelPricingClient:
    """Asynchronous client for the ModelPricing.ai API using aiohttp."""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
        session: Optional[aiohttp.ClientSession] = None,
        max_retries: int = 3,
    ) -> None:
        if not api_key or not isinstance(api_key, str):
            raise ValueError("api_key is required")
        self.api_key = api_key
        configured_base = base_url or os.environ.get(
            "MODELPRICING_BASE_URL", "https://api.modelpricing.ai"
        )
        self.base_url = configured_base.rstrip("/")
        self.timeout = timeout
        self._session = session
        self.max_retries = max_retries

    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    async def _ensure_session(self) -> aiohttp.ClientSession:
        if self._session is None:
            timeout = aiohttp.ClientTimeout(total=self.timeout)
            self._session = aiohttp.ClientSession(timeout=timeout)
        return self._session

    async def aclose(self) -> None:
        if self._session is not None and not self._session.closed:
            await self._session.close()

    def _get_retry_handler(self):
        """Get retry configuration for async operations."""
        return AsyncRetrying(
            retry=retry_if_exception_type((ServerError, aiohttp.ClientError)),
            stop=stop_after_attempt(self.max_retries),
            wait=wait_exponential_jitter(initial=1, max=10, jitter=2),
            reraise=True,
        )

    async def _handle_response(self, resp: aiohttp.ClientResponse) -> Union[Dict[str, Any], EstimateResponse]:
        """Process HTTP response and raise appropriate exceptions."""
        status = resp.status
        if status == 200:
            data = await resp.json()
            try:
                return EstimateResponse.model_validate(data)
            except Exception:
                return data
        if status == 401:
            raise Unauthorized("Unauthorized", status_code=401)
        if status == 404:
            raise NotFound("Not found", status_code=404)
        if status == 422:
            try:
                data = await resp.json()
                message = data.get("error") or "Unprocessable Entity"
                details = data.get("details")
                if details:
                    message = f"{message}: {details}"
            except Exception:
                message = "Unprocessable Entity"
            raise ValidationError(message, status_code=422)

        try:
            data = await resp.json()
            message = data.get("error") or await resp.text()
        except Exception:
            message = await resp.text()
        if 500 <= status <= 599:
            raise ServerError(message, status_code=status)
        raise ModelPricingError(message, status_code=status)

    async def estimate(
        self,
        *,
        model: str,
        tokens_in: int,
        tokens_out: int,
        trace_id: Optional[Dict[str, Any]] = None,
    ) -> Union[Dict[str, Any], EstimateResponse]:
        """
        Call POST /v1/estimate and return the response JSON.

        Retries on ServerError (5xx) and connection errors with exponential backoff.
        """
        if not model:
            raise ValueError("model is required")
        if tokens_in is None or tokens_out is None:
            raise ValueError("tokens_in and tokens_out are required")

        async for attempt in self._get_retry_handler():
            with attempt:
                url = f"{self.base_url}/v1/estimate"
                payload: Dict[str, Any] = {
                    "model": model,
                    "metrics": {"tokensIn": int(tokens_in), "tokensOut": int(tokens_out)},
                }
                if trace_id is not None:
                    payload["traceId"] = trace_id

                session = await self._ensure_session()
                async with session.post(url, json=payload, headers=self._headers()) as resp:
                    return await self._handle_response(resp)


