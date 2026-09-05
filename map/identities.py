"""Locked snapshot of OS-family identities. Dated 2026-09-04/05. Not a live crawler."""

from __future__ import annotations

SNAPSHOT_DATE = "2026-09-05"
FAMILY = "OS_CONSTITUTION"

CLAIM_CAPS = (
    "NAME_ONLY",
    "METADATA_ONLY",
    "SURFACE_API_UNVERIFIED",
    "TREE_PRESENT_FUNCTIONS_UNAUDITED",
)

STATUSES = (
    "CANONICAL_CANDIDATE",
    "AMBIGUOUS_DUPLICATE",
    "DISTINCT_NAME_UNAUDITED",
    "STUB",
)

# Identities are distinct even when names collide after punctuation strip.
IDENTITIES: dict[str, dict] = {
    "Sovereign-OS": {
        "artifact_id": "repo:Sovereign-OS",
        "claim_cap": "SURFACE_API_UNVERIFIED",
        "status": "CANONICAL_CANDIDATE",
        "note": "Public v0.2 constitutional OS description; tree not function-audited.",
        "url": "https://github.com/beyond-repair/Sovereign-OS",
    },
    "SovereignOS": {
        "artifact_id": "repo:SovereignOS",
        "claim_cap": "METADATA_ONLY",
        "status": "AMBIGUOUS_DUPLICATE",
        "note": "Distinct GitHub identity (no hyphen). Connector listing marked private. No SUPERSEDES proof.",
        "url": "https://github.com/beyond-repair/SovereignOS",
        "possible_duplicate_of": "Sovereign-OS",
    },
    "LegionOS": {
        "artifact_id": "repo:LegionOS",
        "claim_cap": "METADATA_ONLY",
        "status": "STUB",
        "note": "Company/agent OS name; scaffold-level.",
        "url": "https://github.com/beyond-repair/LegionOS",
    },
    "RealityOS": {
        "artifact_id": "repo:RealityOS",
        "claim_cap": "SURFACE_API_UNVERIFIED",
        "status": "DISTINCT_NAME_UNAUDITED",
        "note": "Decision-infrastructure naming; not proven equivalent to Sovereign-OS.",
        "url": "https://github.com/beyond-repair/RealityOS",
    },
}

FORBIDDEN_CLAIMS = (
    "shipped OS kernels",
    "SovereignOS == Sovereign-OS",
    "LegionOS governs sunder agents",
    "RealityOS is a runtime for SEEM",
)
