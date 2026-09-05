from __future__ import annotations

from map.identities import CLAIM_CAPS, FORBIDDEN_CLAIMS, IDENTITIES, STATUSES


def validate() -> list[str]:
    errors: list[str] = []
    ids = [row["artifact_id"] for row in IDENTITIES.values()]
    if len(ids) != len(set(ids)):
        errors.append("artifact_id not unique")
    if len(IDENTITIES) != 4:
        errors.append("expected exactly four OS-family identities")
    for name, row in IDENTITIES.items():
        if row["claim_cap"] not in CLAIM_CAPS:
            errors.append(f"{name}: bad claim_cap")
        if row["status"] not in STATUSES:
            errors.append(f"{name}: bad status")
        if not row["artifact_id"].startswith("repo:"):
            errors.append(f"{name}: artifact_id must be repo:<name>")
        if row["artifact_id"] != f"repo:{name}":
            errors.append(f"{name}: artifact_id must match name")
    if IDENTITIES["SovereignOS"].get("possible_duplicate_of") != "Sovereign-OS":
        errors.append("SovereignOS must declare possible_duplicate_of Sovereign-OS")
    if IDENTITIES["SovereignOS"]["status"] != "AMBIGUOUS_DUPLICATE":
        errors.append("SovereignOS must remain AMBIGUOUS_DUPLICATE until SUPERSEDES proof")
    if "shipped OS kernels" not in FORBIDDEN_CLAIMS:
        errors.append("forbidden claim list drifted")
    return errors
