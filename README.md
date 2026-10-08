<div align="center">

[![Lifecycle](https://img.shields.io/badge/●_RESEARCH-a855f7?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)
[![Claim](https://img.shields.io/badge/Claim_≤1-22c55e?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)
[![Governance](https://img.shields.io/badge/ADL--Governance-7c3aed?style=for-the-badge&labelColor=0f0f23)](https://github.com/beyond-repair/ADL-Governance)

```
LIFECYCLE   RESEARCH
CLAIM       ≤1
NOT CLAIMED thrust · energy extraction · AGI · production autonomy
```

</div>

---

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
- Sweep-259 census recheck (2026-10-06, search total 83): all four names were present. `SovereignOS` remained private. None were archived. Snapshot date stays `2026-09-05`. Presence is not a tree audit and not a merge.

## Not claimed

- Running operating systems
- Equivalence of trees
- Merge of source
- Governance of agents by any OS repo
- Census presence as a SUPERSEDES proof

## Run

Needs Python 3.10 or newer. Nothing here touches the network.

```bash
git clone https://github.com/beyond-repair/os-family-constitution-map.git
cd os-family-constitution-map
python3 -m venv .venv && . .venv/bin/activate
python -m pip install -e ".[dev]"
python -m map            # same as python -m map.engine or the os-family-map command
python -m map --json     # the locked map as JSON
python -m pytest -q
```

Expected `python -m map` output (exit 0):

```
identities=4 snapshot=2026-09-05 recheck=2026-10-06 census_total=83
  Sovereign-OS   cap=SURFACE_API_UNVERIFIED           status=CANONICAL_CANDIDATE
  SovereignOS    cap=METADATA_ONLY                    status=AMBIGUOUS_DUPLICATE possible_duplicate_of=Sovereign-OS
  LegionOS       cap=METADATA_ONLY                    status=STUB
  RealityOS      cap=SURFACE_API_UNVERIFIED           status=DISTINCT_NAME_UNAUDITED
PASS: os-family-constitution-map valid
```

If the locked data drifts (a fifth identity, a kernel claim cap, `SovereignOS` promoted out of `AMBIGUOUS_DUPLICATE`, a URL outside `beyond-repair`, a missing forbidden claim), the command prints `FAIL:` lines and exits 1.

Without installing, `pip install -r requirements.txt` then `python -m map.engine` and `python -m pytest -q` from the repository root also work (this is what CI runs).


---

<div align="center">

**REWRITE · BUILD · TRANSCEND**

Governing source: [ADL-Governance](https://github.com/beyond-repair/ADL-Governance) · [Claim levels 0–5](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)

</div>
