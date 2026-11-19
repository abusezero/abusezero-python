# AbuseZero Python SDK

Use the AbuseZero Python SDK to evaluate claims and manage your workspace from your server. AbuseZero is an abuse prevention API for SaaS.

## Install

```bash
python -m pip install abusezero
```

The SDK supports Python 3.11 to 3.15. It requires HTTPX, which pip installs with it.

The package includes its SDK license as `LICENSE`. HTTPX and its dependencies are installed separately and keep their own licenses. [`API.md`](https://github.com/abusezero/abusezero-python/blob/main/API.md), the Django and FastAPI examples and an example script are in the [GitHub repository](https://github.com/abusezero/abusezero-python).

## Evaluate and report a grant

Store your SECRET KEY or RESTRICTED KEY in `ABUSEZERO_SECRET_KEY` on the server. Use a stable claim ID and keep the same idempotency key when retrying the same action.

```python
import os
from collections.abc import Callable
from abusezero import AbuseZero


def create_client() -> AbuseZero:
    return AbuseZero(key=os.environ["ABUSEZERO_SECRET_KEY"], outage="throw")


def evaluate_and_grant(client: AbuseZero, claim_id: str, email: str,
                       grant: Callable[[str], None]):
    result = client.evaluate({
        "benefit": "pro_trial", "claim_id": claim_id,
        "subject": {"email": email},
    }, idempotency_key="evaluate:" + claim_id)
    if "status" in result:
        return result  # No decision was made.
    if result["source"] == "local_outage" or result["result"] != "allow":
        return result
    grant(claim_id)  # Your transaction must finish successfully before returning.
    client.outcome({"outcome": "granted"}, path={"id": result["id"]},
                   idempotency_key="grant:" + claim_id)
    return result
```

Create the client once at worker startup, reuse it across requests and close it at shutdown. Call this helper from your authenticated handler with your own stored claim ID, authenticated user email and transactional grant function. The grant function must be idempotent for that claim ID. The helper reports `granted` only after the grant function succeeds; if reporting fails afterward, retry with the same claim ID and keys. On `deny`, don't grant the benefit. A skipped result is neither allow nor deny, including when its reason is new to your application.

## Clients and credentials

```python
import os
from abusezero import AbuseZero, AbuseZeroPublic, AsyncAbuseZero

# An OAuth access token, from a sign-in or a machine client, acts in the selected workspace.
oauth = AbuseZero(access_token=os.environ["ABUSEZERO_ACCESS_TOKEN"],
                  workspace=os.environ["ABUSEZERO_WORKSPACE"], outage="throw")
keys = oauth.api_keys({"limit": 20})

# The public client reads public information and sends no credentials.
with AbuseZeroPublic() as public:
    pricing = public.pricing()


async def list_benefits(client: AsyncAbuseZero):
    # Create the async client once for your event loop and reuse it, like the synchronous client.
    return await client.benefits({"limit": 20})
```

Management operations need an OAuth access token, from a sign-in or a machine client. An API key alone can't perform them. The selected workspace and the approving member's permissions still apply. Some actions act for one member or follow what that member may do, such as notifications, support tickets and changes to members, and need that member's own sign-in; API keys and machine clients get `MEMBER_SIGN_IN_REQUIRED` for them. See [Actions that need a member's own sign-in](https://docs.abusezero.com/docs/api-reference/authentication#actions-that-need-a-members-own-sign-in).

Async methods support task cancellation. The synchronous client also works inside an async application, but use `AsyncAbuseZero` to avoid blocking its event loop. Pass an HTTPX transport with `transport=` to configure a proxy or a test service. The client owns and closes it. Custom synchronous transports must honor the request timeout; the built-in transport cancels requests when the total budget ends.

## Webhooks

```python
from abusezero import WebhookVerificationError, verify_webhook


def receive(raw_body: bytes, headers: dict[str, str], current_secret: str, previous_secret: str | None):
    try:
        # Use the original request bytes. Keep both secrets during rotation.
        event = verify_webhook(payload=raw_body, headers=headers,
                               secret=[current_secret, previous_secret])
    except WebhookVerificationError:
        return 400
    ...  # Deduplicate by event["id"], then handle the event.
    return 200
```

`verify_webhook(payload=, headers=, secret=, tolerance_seconds=300)` checks the signature over the original request bytes and the timestamp within `tolerance_seconds`, accepts rotating secrets and rejects a modified body. It returns the event, or raises `WebhookVerificationError` when the signature or event body can't be verified. Deduplicate accepted events by their event ID in your application.

## Errors, retries and results

Catch `AbuseZeroError`. Its fields are `code`, `status`, `request_id`, `retryable` and `docs_url`. `status` is the HTTP status, or `0` for `TRANSPORT_ERROR` and `DEADLINE_EXCEEDED`, which have no response. The SDK raises these before sending a request, each with a 4xx status: `CREDENTIAL_REQUIRED`, `INVALID_KEY`, `INVALID_TOKEN`, `WORKSPACE_REQUIRED`, `INVALID_WORKSPACE`, `OAUTH_REQUIRED`, `INVALID_IDEMPOTENCY_KEY` and `INVALID_REQUEST`. `INVALID_RESPONSE` means a response couldn't be read.

Set `outage` to `throw`, `allow` or `deny`. The default is `throw`. Only evaluation calls can return `source: local_outage`; other operations raise an error. Rate limits always remain errors. Skipped responses remain skips, including unknown skip reasons.

Within `v1`, responses can gain new fields and new values for codes and enums. The SDK returns them unchanged, so handle a value your code doesn't recognize as a generic case.

Calls make at most three attempts. Network errors, retryable API errors and HTTP 429, 502, 503 and 504 are retried. `Retry-After` sets the minimum wait. Every attempt uses identical serialized input and the same idempotency key. The entire call, including waits, has one budget: 1.8 seconds for `evaluate` and 5 seconds for other calls, dry runs included. An events long poll adds 5 seconds to its requested wait. The server's own operation deadline can be shorter.

## Methods and pagination

Every public server operation has a method. Pass input fields in the method's input and path fields separately in `path`. Mutation methods require an idempotency key. [`API.md`](https://github.com/abusezero/abusezero-python/blob/main/API.md) lists every method; see the [AbuseZero REST API reference](https://docs.abusezero.com/docs/api-reference) for each operation's fields.

List methods accept `cursor` and `limit` where documented. Process the returned `data`, then pass the returned `next_cursor` to the same method until it is null. Keep IDs and cursors as strings. Send null only when the field allows it; omitting a field leaves it absent.

## Incoming requests and identifiers

```python
import os
from abusezero import AbuseZero, create_custom_identifier, create_phone_hash, incoming_request


def evaluate_with_identifiers(client: AbuseZero, claim_id: str, email: str,
                              method: str, url: str, headers: dict[str, str]):
    secret = os.environ["IDENTIFIER_HASH_SECRET"]
    phone_hash = create_phone_hash(secret=secret, key_version="v1", e164="+14155550123")
    team = create_custom_identifier(secret=secret, key_version="v1", key="team_id", value="team_8812")
    return client.evaluate({
        "benefit": "pro_trial", "claim_id": claim_id, "subject": {"email": email},
        "identifiers": {"phone_hash": phone_hash, "phone_verified": True, "custom": [team]},
        "request": incoming_request(method, url, headers),
    }, idempotency_key="evaluate:" + claim_id)
```

`incoming_request(method, url, headers)` takes the incoming HTTP method, absolute URL and headers, and removes credential headers before you include the request in an evaluation. It doesn't infer a trusted client IP; use your application's trusted proxy configuration for that.

`create_phone_hash(secret=, key_version=, e164=)` needs a number in E.164 format. `create_custom_identifier(secret=, key_version=, key=, value=)` needs a [registered](https://docs.abusezero.com/docs/api-reference/custom-identifiers#register-a-custom-identifier) identifier key. Both return the public API's hash objects. Use the same secret and `key_version` everywhere the same value should match. See [Send identifiers](https://docs.abusezero.com/docs/guides/send-identifiers).

## Frameworks and browser protection

The Django and FastAPI examples are in [`examples/frameworks.md`](https://github.com/abusezero/abusezero-python/blob/main/examples/frameworks.md); no framework dependency is required.

For browser protection, add the [standalone browser script](https://docs.abusezero.com/docs/tools/browser-sdk#standalone-browser-script) to your page and pass its device token to your server. Send the token unchanged in the evaluation input as `identifiers.device_token`. This SDK is the only package to install. See [Set up browser protection](https://docs.abusezero.com/docs/guides/set-up-browser-protection).

## API origin and TLS

The default API origin is `https://api.abusezero.com`. Custom origins require HTTPS; HTTP is accepted only for explicit loopback testing. Built-in transports verify TLS and refuse redirects. Custom transports are responsible for equivalent behavior. Never log credentials or raw authenticated requests.

## More documentation

See [authentication](https://docs.abusezero.com/docs/api-reference/authentication), [evaluation results](https://docs.abusezero.com/docs/concepts/evaluations) and [webhooks](https://docs.abusezero.com/docs/guides/receive-webhooks).
