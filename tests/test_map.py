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


import copy
import json

from map.engine import main, report


def _mutated():
    return copy.deepcopy(IDENTITIES), copy.deepcopy(CENSUS_PRESENCE)


def test_rejects_merge_of_sovereign_names() -> None:
    idents, presence = _mutated()
    idents["SovereignOS"]["status"] = "CANONICAL_CANDIDATE"
    assert any("AMBIGUOUS_DUPLICATE" in e for e in validate(idents, presence))


def test_rejects_missing_identity() -> None:
    idents, presence = _mutated()
    del idents["LegionOS"]
    errors = validate(idents, presence)
    assert "expected exactly four OS-family identities" in errors
    assert "census presence keys must match identities" in errors


def test_rejects_kernel_claim_cap_and_unknown_keys() -> None:
    idents, presence = _mutated()
    idents["RealityOS"]["claim_cap"] = "KERNEL_SHIPPED"
    idents["RealityOS"]["kernel"] = True
    errors = validate(idents, presence)
    assert "RealityOS: bad claim_cap" in errors
    assert any("unknown keys" in e for e in errors)


def test_rejects_wrong_url_and_archived_flip() -> None:
    idents, presence = _mutated()
    idents["LegionOS"]["url"] = "https://github.com/someone-else/LegionOS"
    presence["LegionOS"]["archived"] = True
    errors = validate(idents, presence)
    assert "LegionOS: url must point at beyond-repair/LegionOS" in errors
    assert any("archived flag" in e for e in errors)


def test_cli_text_and_json(capsys) -> None:
    assert main([]) == 0
    out = capsys.readouterr().out
    assert "identities=4" in out
    assert out.strip().endswith("PASS: os-family-constitution-map valid")
    assert main(["--json"]) == 0
    data = json.loads(capsys.readouterr().out)
    assert data == report()
    assert data["identities"]["SovereignOS"]["possible_duplicate_of"] == "Sovereign-OS"
