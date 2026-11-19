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
