from map.identities import (
    CENSUS_PRESENCE,
    CENSUS_RECHECK_DATE,
    FORBIDDEN_CLAIMS,
    IDENTITIES,
    SNAPSHOT_DATE,
)
from map.validate import validate


def test_no_errors() -> None:
    assert validate() == []


def test_four_distinct_identities() -> None:
    assert set(IDENTITIES) == {"Sovereign-OS", "SovereignOS", "LegionOS", "RealityOS"}


def test_hyphen_collision_not_equivalence() -> None:
    assert IDENTITIES["Sovereign-OS"]["artifact_id"] != IDENTITIES["SovereignOS"]["artifact_id"]
    assert IDENTITIES["SovereignOS"]["status"] == "AMBIGUOUS_DUPLICATE"


def test_no_kernel_claim() -> None:
    assert "shipped OS kernels" in FORBIDDEN_CLAIMS
    for row in IDENTITIES.values():
        assert row["claim_cap"] != "KERNEL_SHIPPED"


def test_census_recheck_does_not_replace_snapshot() -> None:
    assert SNAPSHOT_DATE == "2026-09-05"
    assert CENSUS_RECHECK_DATE == "2026-10-06"
    assert CENSUS_PRESENCE["SovereignOS"]["private"] is True
    assert "census presence is a tree merge" in FORBIDDEN_CLAIMS
