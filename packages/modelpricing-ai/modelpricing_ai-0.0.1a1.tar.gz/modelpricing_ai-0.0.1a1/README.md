# modelpricing-ai

Python client for the ModelPricing.ai API.

## Installation

```bash
pip install modelpricing-ai
```

## Usage (sync, typed)

```python
from modelpricing_ai import ModelPricingClient

client = ModelPricingClient(api_key="YOUR_API_KEY")

estimate = client.estimate(
    model="gpt-4o-mini",
    tokens_in=125000,
    tokens_out=42000,
    trace_id={"requestId": "abc-123"},
)
print(estimate.total)  # total USD cost
```

- Base URL: `https://api.modelpricing.ai`
- Auth: `Authorization: Bearer <API_KEY>`
- Endpoint: `POST /v1/estimate`
- Request body:

```json
{
    "metrics": { "tokensIn": 1000, "tokensOut": 2000 },
    "model": "<model-name>",
    "traceId": { "...": "..." }
}
```

### Error handling

- 401 Unauthorized: invalid or missing API key
- 422 Unprocessable Entity: validation error (e.g., invalid model or metrics)
- Other 4xx/5xx: raised as a generic server error

### Retry behavior

The client automatically retries on transient errors with exponential backoff:

- **Retries**: 5xx server errors and network/connection errors
- **No retry**: 4xx client errors (401, 404, 422)
- **Default**: 3 attempts with exponential backoff (1s, 2s, 4s, up to 10s max)

Configure retry behavior:

```python
# Customize max retries (default is 3)
client = ModelPricingClient(api_key="YOUR_API_KEY", max_retries=5)

# Disable retries
client = ModelPricingClient(api_key="YOUR_API_KEY", max_retries=1)
```

This handles transient infrastructure issues like Cloudflare errors, DNS failures, and temporary service disruptions.

## License

MIT

## Async usage (typed)

```python
import asyncio
from modelpricing_ai import AsyncModelPricingClient

async def main():
    client = AsyncModelPricingClient(api_key="YOUR_API_KEY")
    estimate = await client.estimate(
        model="gpt-4o-mini",
        tokens_in=125000,
        tokens_out=42000,
        trace_id={"requestId": "abc-123"},
    )
    print(estimate.total)  # total USD cost

asyncio.run(main())
```
