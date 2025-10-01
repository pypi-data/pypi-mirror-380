import os
from typing import Any, Dict, Optional, Union

import requests
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential_jitter,
)

from .errors import ModelPricingError, NotFound, ServerError, Unauthorized, ValidationError
from .models import EstimateResponse


class ModelPricingClient:
    """Synchronous client for the ModelPricing.ai API."""

    def __init__(
        self,
        api_key: str,
        *,
        base_url: Optional[str] = None,
        timeout: float = 30.0,
        session: Optional[requests.Session] = None,
        max_retries: int = 3,
    ) -> None:
        if not api_key or not isinstance(api_key, str):
            raise ValueError("api_key is required")
        self.api_key = api_key
        configured_base = base_url or os.environ.get(
            "MODELPRICING_BASE_URL", "https://api.modelpricing.ai"
        )
        # Normalize base URL (no trailing slash)
        self.base_url = configured_base.rstrip("/")
        self.timeout = timeout
        self._session = session or requests.Session()
        self.max_retries = max_retries

    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def _retry_on_server_error(self, func):
        """Decorator to retry a function on server errors and connection issues."""
        return retry(
            retry=retry_if_exception_type((ServerError, requests.exceptions.RequestException)),
            stop=stop_after_attempt(self.max_retries),
            wait=wait_exponential_jitter(initial=1, max=10, jitter=2),
            reraise=True,
        )(func)

    def _handle_response(
        self, response: requests.Response
    ) -> Union[Dict[str, Any], EstimateResponse]:
        """Process HTTP response and raise appropriate exceptions."""
        if response.status_code == 200:
            data = response.json()
            try:
                return EstimateResponse.model_validate(data)
            except Exception:
                return data
        if response.status_code == 401:
            raise Unauthorized("Unauthorized", status_code=401)
        if response.status_code == 404:
            raise NotFound("Not found", status_code=404)
        if response.status_code == 422:
            try:
                data = response.json()
                message = data.get("error") or "Unprocessable Entity"
                details = data.get("details")
                if details:
                    message = f"{message}: {details}"
            except Exception:
                message = "Unprocessable Entity"
            raise ValidationError(message, status_code=422)

        # Other 4xx/5xx
        try:
            data = response.json()
            message = data.get("error") or response.text or "HTTP error"
        except Exception:
            message = response.text or "HTTP error"

        if 500 <= response.status_code <= 599:
            raise ServerError(message, status_code=response.status_code)
        raise ModelPricingError(message, status_code=response.status_code)

    def estimate(
        self,
        *,
        model: str,
        tokens_in: int,
        tokens_out: int,
        trace_id: Optional[Dict[str, Any]] = None,
    ) -> Union[Dict[str, Any], EstimateResponse]:
        """
        Call POST /v1/estimate and return the response JSON.

        Returns dict with keys: total, breakdown, model, traceId.

        Retries on ServerError (5xx) and connection errors with exponential backoff.
        """
        if not model:
            raise ValueError("model is required")
        if tokens_in is None or tokens_out is None:
            raise ValueError("tokens_in and tokens_out are required")

        def _make_request() -> Union[Dict[str, Any], EstimateResponse]:
            url = f"{self.base_url}/v1/estimate"
            payload: Dict[str, Any] = {
                "model": model,
                "metrics": {"tokensIn": int(tokens_in), "tokensOut": int(tokens_out)},
            }
            if trace_id is not None:
                payload["traceId"] = trace_id

            response = self._session.post(
                url, json=payload, headers=self._headers(), timeout=self.timeout
            )
            return self._handle_response(response)

        return self._retry_on_server_error(_make_request)()


