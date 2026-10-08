from __future__ import annotations

import argparse
import json

from map import __version__
from map.identities import (
    CENSUS_RECHECK_DATE,
    CENSUS_TOTAL,
    IDENTITIES,
    SNAPSHOT_DATE,
)
from map.validate import validate


def report() -> dict:
    """Return the locked map as plain data (no network, no crawl)."""
    return {
        "version": __version__,
        "snapshot_date": SNAPSHOT_DATE,
        "census_recheck_date": CENSUS_RECHECK_DATE,
        "census_total": CENSUS_TOTAL,
        "identities": {
            name: {
                "artifact_id": row["artifact_id"],
                "claim_cap": row["claim_cap"],
                "status": row["status"],
                "possible_duplicate_of": row.get("possible_duplicate_of"),
            }
            for name, row in IDENTITIES.items()
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m map",
        description="Validate and print the locked OS-family identity map. Not a live crawler.",
    )
    parser.add_argument("--json", action="store_true", help="print the map as JSON")
    args = parser.parse_args(argv)

    errors = validate()
    if errors:
        for e in errors:
            print("FAIL:", e)
        return 1

    data = report()
    if args.json:
        print(json.dumps(data, indent=2, sort_keys=True))
        return 0

    print(
        f"identities={len(IDENTITIES)} snapshot={SNAPSHOT_DATE} "
        f"recheck={CENSUS_RECHECK_DATE} census_total={CENSUS_TOTAL}"
    )
    for name, row in data["identities"].items():
        dup = f" possible_duplicate_of={row['possible_duplicate_of']}" if row["possible_duplicate_of"] else ""
        print(f"  {name:<14} cap={row['claim_cap']:<32} status={row['status']}{dup}")
    print("PASS: os-family-constitution-map valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
