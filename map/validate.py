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


REQUIRED_KEYS = {"artifact_id", "claim_cap", "status", "note", "url"}
OPTIONAL_KEYS = {"possible_duplicate_of"}
REQUIRED_FORBIDDEN = {
    "shipped OS kernels",
    "SovereignOS == Sovereign-OS",
    "census presence is a tree merge",
}


def validate(identities: dict | None = None, presence: dict | None = None) -> list[str]:
    """Return a list of problems with the locked map. Empty list means valid.

    ``identities`` and ``presence`` default to the locked snapshot; tests pass
    mutated copies to prove the checker rejects drift.
    """
    idents = IDENTITIES if identities is None else identities
    presence_map = CENSUS_PRESENCE if presence is None else presence
    errors: list[str] = []
    ids = [row.get("artifact_id") for row in idents.values()]
    if len(ids) != len(set(ids)):
        errors.append("artifact_id not unique")
    if len(idents) != 4:
        errors.append("expected exactly four OS-family identities")
    if SNAPSHOT_DATE != "2026-09-05":
        errors.append("snapshot date must stay 2026-09-05")
    if CENSUS_RECHECK_DATE != "2026-10-06":
        errors.append("census recheck date drifted")
    if CENSUS_TOTAL != 83:
        errors.append("census total drifted from locked recheck")
    if set(presence_map) != set(idents):
        errors.append("census presence keys must match identities")
    for name, row in idents.items():
        keys = set(row)
        missing = REQUIRED_KEYS - keys
        if missing:
            errors.append(f"{name}: missing keys {sorted(missing)}")
            continue
        extra = keys - REQUIRED_KEYS - OPTIONAL_KEYS
        if extra:
            errors.append(f"{name}: unknown keys {sorted(extra)}")
        if row["url"] != f"https://github.com/beyond-repair/{name}":
            errors.append(f"{name}: url must point at beyond-repair/{name}")
        if row["claim_cap"] not in CLAIM_CAPS:
            errors.append(f"{name}: bad claim_cap")
        if row["status"] not in STATUSES:
            errors.append(f"{name}: bad status")
        if not row["artifact_id"].startswith("repo:"):
            errors.append(f"{name}: artifact_id must be repo:<name>")
        if row["artifact_id"] != f"repo:{name}":
            errors.append(f"{name}: artifact_id must match name")
        seen = presence_map.get(name, {})
        if seen.get("present") is not True:
            errors.append(f"{name}: census presence must stay true for this recheck")
        if seen.get("archived") is not False:
            errors.append(f"{name}: archived flag must stay false for this recheck")
    if presence_map.get("SovereignOS", {}).get("private") is not True:
        errors.append("SovereignOS private flag must stay true for this recheck")
    sov = idents.get("SovereignOS", {})
    if sov.get("possible_duplicate_of") != "Sovereign-OS":
        errors.append("SovereignOS must declare possible_duplicate_of Sovereign-OS")
    if sov.get("status") != "AMBIGUOUS_DUPLICATE":
        errors.append("SovereignOS must remain AMBIGUOUS_DUPLICATE until SUPERSEDES proof")
    for claim in sorted(REQUIRED_FORBIDDEN - set(FORBIDDEN_CLAIMS)):
        errors.append(f"forbidden claim missing: {claim}")
    return errors
