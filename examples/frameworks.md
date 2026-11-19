# Django and FastAPI

Reuse the client for the application's lifetime. Pass the incoming request helper's result as `request` in the evaluation input. The application still decides when to grant the benefit.

## Django

```python
import os
from abusezero import AbuseZero, incoming_request

client = AbuseZero(key=os.environ["ABUSEZERO_SECRET_KEY"], outage="throw")  # Once per worker.


def evaluate_claim(request, claim_id: str):
    incoming = incoming_request(request.method, request.build_absolute_uri(), dict(request.headers))
    return client.evaluate({
        "benefit": "pro_trial", "claim_id": claim_id,
        "subject": {"email": request.user.email}, "request": incoming,
    }, idempotency_key="evaluate:" + claim_id)
```

Create `AbuseZero` once for your worker and close it when the worker stops. Call `evaluate_claim` from an authenticated view with your own stored claim ID.

## FastAPI

```python
from contextlib import asynccontextmanager
import os
from fastapi import FastAPI, Request
from abusezero import AsyncAbuseZero, incoming_request

@asynccontextmanager
async def lifespan(app):
    async with AsyncAbuseZero(key=os.environ["ABUSEZERO_SECRET_KEY"], outage="throw") as client:
        app.state.abusezero = client
        yield

app = FastAPI(lifespan=lifespan)

async def evaluate_claim(request: Request, claim_id: str, verified_email: str):
    return await request.app.state.abusezero.evaluate({
        "benefit": "pro_trial", "claim_id": claim_id,
        "subject": {"email": verified_email},
        "request": incoming_request(request.method, str(request.url), dict(request.headers)),
    }, idempotency_key="evaluate:" + claim_id)
```

Call `evaluate_claim` from your authenticated route. Follow the README's skipped, outage, allow and deny branches before granting anything. For webhooks, pass `await request.body()` to `verify_webhook` before parsing JSON. In Django, use `request.body`.
