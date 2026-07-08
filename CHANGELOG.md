# CHANGELOG — Dharma-OKF

In-place change waves on `main`, newest first, per the contract in [VERSIONING.md](VERSIONING.md). Release tags remain immutable snapshots; this log covers what changes between them.

## 2026-07 — The Genealogy Update, Phase 1 (docs wave)

- **Added [VERSIONING.md](VERSIONING.md):** the repository's declared update contract (living vocabulary on main; immutable release tags; patch-bump enrichment semantics). Declared before any known external consumer existed.
- **Added [GENEALOGIES.md](GENEALOGIES.md):** "Where the Errors Came From": 13 documented mistranslation genealogies (10 chain-sourced, 3 labeled drift), each with named sources, dates, propagation chains, and a reverse-index of affected concept files. Admission bar: named source + date + documented propagation, or excluded.
- **Added this CHANGELOG.md.**
- No concept files were modified in this wave.

## 2026-07 — The Genealogy Update, Phase 2 (retrofit wave)

The reverse-index files in [GENEALOGIES.md](GENEALOGIES.md) received an **Error Genealogy** section (a documented summary — named source, date, propagation chain — plus a link to the canonical genealogy), back-porting v0.8 shakta-darshana's genealogy-native standard to the older bundles. 18 files across 5 bundles.

- **dharma-foundation (v0.1):** chakra (G1, G2), karma (G4), samsara (G4, partial), yoga (G5), dharma (G6), moksha (G7), maya (G8). This bundle predates the per-file `bundle
-  Tooling: extended okf_validate.py (link/slug checks) + per-bundle pytest suite added.
