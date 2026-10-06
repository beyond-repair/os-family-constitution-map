from __future__ import annotations

from map.identities import (
    CENSUS_PRESENCE,
    CENSUS_RECHECK_DATE,
    CENSUS_TOTAL,
    CLAIM_CAPS,
    FORBIDDEN_CLAIMS,
    IDENTITIES,
    SNAPSHOT_DATE,
    STATUSES,
)


def validate() -> list[str]:
    errors: list[str] = []
    ids = [row["artifact_id"] for row in IDENTITIES.values()]
    if len(ids) != len(set(ids)):
        errors.append("artifact_id not unique")
    if len(IDENTITIES) != 4:
        errors.append("expected exactly four OS-family identities")
    if SNAPSHOT_DATE != "2026-09-05":
        errors.append("snapshot date must stay 2026-09-05")
    if CENSUS_RECHECK_DATE != "2026-10-06":
        errors.append("census recheck date drifted")
    if CENSUS_TOTAL != 83:
        errors.append("census total drifted from locked recheck")
    if set(CENSUS_PRESENCE) != set(IDENTITIES):
        errors.append("census presence keys must match identities")
    for name, row in IDENTITIES.items():
        if row["claim_cap"] not in CLAIM_CAPS:
            errors.append(f"{name}: bad claim_cap")
        if row["status"] not in STATUSES:
            errors.append(f"{name}: bad status")
        if not row["artifact_id"].startswith("repo:"):
            errors.append(f"{name}: artifact_id must be repo:<name>")
        if row["artifact_id"] != f"repo:{name}":
            errors.append(f"{name}: artifact_id must match name")
        presence = CENSUS_PRESENCE[name]
        if presence.get("present") is not True:
            errors.append(f"{name}: census presence must stay true for this recheck")
        if presence.get("archived") is not False:
            errors.append(f"{name}: archived flag must stay false for this recheck")
    if CENSUS_PRESENCE["SovereignOS"]["private"] is not True:
        errors.append("SovereignOS private flag must stay true for this recheck")
    if IDENTITIES["SovereignOS"].get("possible_duplicate_of") != "Sovereign-OS":
        errors.append("SovereignOS must declare possible_duplicate_of Sovereign-OS")
    if IDENTITIES["SovereignOS"]["status"] != "AMBIGUOUS_DUPLICATE":
        errors.append("SovereignOS must remain AMBIGUOUS_DUPLICATE until SUPERSEDES proof")
    if "shipped OS kernels" not in FORBIDDEN_CLAIMS:
        errors.append("forbidden claim list drifted")
    if "census presence is a tree merge" not in FORBIDDEN_CLAIMS:
        errors.append("census-merge forbidden claim missing")
    return errors
