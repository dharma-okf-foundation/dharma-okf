# CHANGELOG — Dharma-OKF

In-place change waves on `main`, newest first, per the contract in [VERSIONING.md](VERSIONING.md). Release tags remain immutable snapshots; this log covers what changes between them.

## 2026-08 — Wave 0: de-fork and the `dharma-okf/1.0` profile (structural wave)

Merge [`22b9701`](https://github.com/dharma-okf-foundation/dharma-okf/commit/22b9701) (PR #2, branch `bf5a9ed`) — **449 deletions, 5 additions/edits.** No release tag; no concept content changed.

**Why.** This repository began as a fork of [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) and had vendored that project's code at two levels while locally editing its `okf/SPEC.md` to declare a rival "v0.2". When upstream published its own OKF v0.2 on 2026-07-24, that became a standing merge conflict on a file this project does not own — and `okf/README.md` was still advertising v0.1 directly above it.

**Removed** — the vendored upstream, retrievable from that project at any time:

- `agents/`, `toolbox/`, `samples/`, `demos/`-adjacent trees at the repository root
- `okf/bundles/` (the `ga4`, `stackoverflow` and `crypto_bitcoin` sample bundles), `okf/src/` (the reference enrichment agent), `okf/samples/`
- `okf/README.md`, `okf/SPEC.md`, `okf/LICENSE.md`, `okf/pyproject.toml`
- seven upstream test modules from `okf/tests/`

Retained: `okf/tools/okf_validate.py`, the seven Dharma-OKF regression tests, `demos/failure-vs-success.md`, and all thirteen bundles.

**Added:**

- **[PROFILE.md](PROFILE.md)** — Dharma-OKF declared as a *profile* of the Open Knowledge Format rather than a fork of it: base conformance claim, documented extensions (`not:`, `darshana:`, `reception_note:`, and others), rules stricter than the base, and explicit declinations with reasons. The base is **cited at a pinned commit, never tracked from `main`**, so upstream drift cannot silently change what these bundles claim. Replaces the locally-edited `okf/SPEC.md`; that practice is retired.
- **[CLAUDE.md](CLAUDE.md)** — operational working rules for AI agents editing this repository, derived from `PROFILE.md`.
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — rewritten. The previous file was upstream's and directed contributors to sign a *Google* Contributor License Agreement in order to contribute here.

**Fixed:** `okf/dharma-foundation/index.md` carried `sources:` as a list of plain strings, colliding with the base specification's requirement that each entry be a mapping with a `resource:`. The only such collision in 442 documents; corrected to the conformant shape.

**Corrected in the README:** the primary-source reference count was 137, which counted the five `references/index.md` files as sources. The true count of `type: Reference` documents is **132**.

**Verified:** mirror byte-clean against the remote in both directions; 442 concept documents (310 `type: Concept`, 132 `type: Reference`); validator 0 fail / 0 warn.

### Re-pinning RP-001 — 2026-08-05

Base specification re-pinned `780fe9d` → [`3fcbb9f`](https://github.com/GoogleCloudPlatform/knowledge-catalog/commit/3fcbb9f828c2f23d109c855ee403c3a4c81f3a96). Upstream removed "(Draft)" from the OKF v0.2 version line two hours after publishing it; the specification text is otherwise unchanged. Recorded as a dated decision rather than absorbed silently — which is the point of pinning. See `PROFILE.md` §7.
## 2026-07 — The Genealogy Update, Phase 1 (docs wave)

- **Added [VERSIONING.md](VERSIONING.md):** the repository's declared update contract (living vocabulary on main; immutable release tags; patch-bump enrichment semantics). Declared before any known external consumer existed.
- **Added [GENEALOGIES.md](GENEALOGIES.md):** "Where the Errors Came From": 13 documented mistranslation genealogies (10 chain-sourced, 3 labeled drift), each with named sources, dates, propagation chains, and a reverse-index of affected concept files. Admission bar: named source + date + documented propagation, or excluded.
- **Added this CHANGELOG.md.**
- No concept files were modified in this wave.

## 2026-07 — The Genealogy Update, Phase 2 (retrofit wave)

The reverse-index files in [GENEALOGIES.md](GENEALOGIES.md) received an **Error Genealogy** section (a documented summary — named source, date, propagation chain — plus a link to the canonical genealogy), back-porting v0.8 shakta-darshana's genealogy-native standard to the older bundles. 18 files across 5 bundles.

- **dharma-foundation (v0.1):** chakra (G1, G2), karma (G4), samsara (G4, partial), yoga (G5), dharma (G6), moksha (G7), maya (G8). This bundle predates the per-file `bundle
-  Tooling: extended okf_validate.py (link/slug checks) + per-bundle pytest suite added.
