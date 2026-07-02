# CHANGELOG — Dharma-OKF

In-place change waves on `main`, newest first, per the contract in [VERSIONING.md](VERSIONING.md). Release tags remain immutable snapshots; this log covers what changes between them.

## 2026-07 — The Genealogy Update, Phase 1 (docs wave)

- **Added [VERSIONING.md](VERSIONING.md):** the repository's declared update contract (living vocabulary on main; immutable release tags; patch-bump enrichment semantics). Declared before any known external consumer existed.
- **Added [GENEALOGIES.md](GENEALOGIES.md):** "Where the Errors Came From": 13 documented mistranslation genealogies (10 chain-sourced, 3 labeled drift), each with named sources, dates, propagation chains, and a reverse-index of affected concept files. Admission bar: named source + date + documented propagation, or excluded.
- **Added this CHANGELOG.md.**
- No concept files were modified in this wave.

## Planned — The Genealogy Update, Phase 2 (retrofit wave, after the v0.9 concept-lock)

- The files in GENEALOGIES.md's reverse index receive genealogy summaries and links in their `not:` fields.
- Every touched bundle gets a `bundle_version` patch bump (e.g., dharma-foundation 0.1.1 → 0.1.2) and an entry here.

## Prior history (pre-contract)

Bundle releases v0.1.0 through v0.8.0 (2026-06-18 to 2026-07-02) and the adoption layer (INTEGRATION.md, demos; 2026-06-26) predate this changelog; their history lives in the release notes and git log.
