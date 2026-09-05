from __future__ import annotations

from map.validate import validate


def main() -> int:
    errors = validate()
    if errors:
        for e in errors:
            print("FAIL:", e)
        return 1
    print("PASS: os-family-constitution-map valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
