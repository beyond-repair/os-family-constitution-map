# os-family-constitution-map

Claim-capped **identity map** for the Sovereign / Legion / Reality OS name family.

Closes queue items:

- `adl-capability-matrix` Q-005 (`os-family-constitution-map`)
- `adl-function-census` Q-FUNC-004 (`os-constitution-merge`) — **map only**, not a merge of trees

## Claimed

- Four repository identities exist and are not equivalent by name:
  - `Sovereign-OS` (hyphen)
  - `SovereignOS` (no hyphen; private in connector listing)
  - `LegionOS`
  - `RealityOS`
- Each identity has a claim cap. None is a shipped kernel.
- `SovereignOS` is marked `AMBIGUOUS_DUPLICATE` of `Sovereign-OS` until a SUPERSEDES proof exists.
- This repository is a deterministic JSON + validator, not a live crawler.

## Not claimed

- Running operating systems
- Equivalence of trees
- Merge of source
- Governance of agents by any OS repo

## Run

```bash
pip install -r requirements.txt
python -m map.engine
python -m pytest -q
```
