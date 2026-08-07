# CHANGELOG — Dharma-OKF

In-place change waves on `main`, newest first, per the contract in [VERSIONING.md](VERSIONING.md). Release tags remain immutable snapshots; this log covers what changes between them.

## 2026-08-06 — Licensing scope and repository hygiene (docs wave)

No concept document touched; no release tag.

**Licensing stated by scope, not by inheritance.** `README.md` described the Apache licence as *"inherited from the upstream GoogleCloudPlatform fork."* That was inaccurate. `okf/tools/` has no counterpart in the upstream repository, and the validator imports the upstream parser *optionally* rather than embedding it — the code is this project's own work. The README now states both licences by scope: **CC BY-SA 4.0** for the corpus and the repository prose (`LICENSE-CONTENT`), **Apache 2.0 © Dharma OKF Foundation** for `okf/tools/` and `okf/tests/` (`LICENSE.md`, scope in the new `NOTICE`).

**Added [NOTICE](NOTICE):** the copyright line and the licence-scope boundary, in the conventional place. `LICENSE.md` itself is unchanged — the Apache 2.0 text is reproduced verbatim, as it must be.

**Removed committed bytecode.** `okf/tools/__pycache__/okf_validate.cpython-310.pyc` was tracked. `okf/.gitignore` already listed `__pycache__/`, but an ignore rule does not untrack an existing file. Deleted, and the **root `.gitignore`** now mirrors the Python ignores so bytecode cannot be committed from outside `okf/`.

## 2026-08-06 — Bundle-root index reconciliation (metadata wave)

No concept document touched; no release tag. Closes the `bundle_version` half of the known gap that the versioning correction (below) had disclosed hours earlier.

**Seven bundle-root `index.md` files carried a content revision older than their bundle's newest release tag.** Each is now reconciled:

| Bundle | Was | Now |
|---|---|---|
| `dharma-foundation` | `version: "0.1.1"` | **`"0.1.3"`** |
| `yoga-darshana` | `version: "0.2.0"` | **`"0.2.1"`** |
| `vedanta-epistemology` | `version: "0.3.0"` | **`"0.3.2"`** |
| `bhakti-marga` | `version: "0.4.0"` | **`"0.4.2"`** |
| `dharmic-ethics` | `version: "0.5.0"` | **`"0.5.2"`** |
| `shakta-darshana` | `version: "0.8.0"` | **`"0.8.1"`** |
| `sankhya-darshana` | `bundle_version: 0.13.0` *(unquoted)* | **`"0.13.2"`** |

`upanishadic-core` (0.6.1) and `cosmology-creation` (0.7.2) already matched; the four newest bundles have never had a patch bump. Every target was read from `git ls-remote --tags`, per the standing rule that versions are read from the remote and never from a planning document.

**Each target was checked against post-tag history, not merely matched to the tag.** Where commits landed after a bundle's newest tag they were `viz.html` regenerations (a generated artifact) or the Wave 0 `sources:`-shape fix — corrections under `VERSIONING.md` rule 1, which owe no bump. No bundle was owed a *higher* number than its newest tag.

> **`dharma-foundation` is `0.1.3`, deliberately not `0.1.4`.** `v0.1.4` is reserved for the forthcoming Level 3 retrofit of this bundle. Bumping the index into that number now would consume a planned tag and recreate the collision this project has already hit once.

**Key names left as found.** Six bundles use `version:` and one uses `bundle_version:`. `PROFILE.md` §1.1 discloses the bundle-root frontmatter block by name and `version` appears in that published list, so renaming would falsify a disclosure to gain nothing — no tooling reads either key. Unifying the key name is deferred to the normalization pass, where §1.1 can be updated in the same wave.

**Also fixed in `okf/dharma-foundation/index.md`,** two stale links open since Wave 0:

- the OKF reference pointed at `github.com/google/open-knowledge-format`, which does not resolve. It now points at the **pinned-SHA specification URL already used by `PROFILE.md` and `README.md`**, so all three cite the base identically, at the pin and never at `main`.
- the contributor line pointed at `github.com/kdschampions/dharma-okf-toolkit`, a different repository, contradicting the root `CONTRIBUTING.md` that Wave 0 added. It now points at `CONTRIBUTING.md`, `PROFILE.md`, and `okf/tools/`, in the relative form §3.1 requires.

**Still open on this axis:** `dharma-foundation`'s 25 concept documents carry no `bundle_version` at all — the bundle predates the key. That backfill is scheduled with the normalization pass.

## 2026-08-06 — Versioning contract correction (docs wave)

No concept file touched; no release tag. Corrections to `PROFILE.md`, `VERSIONING.md` and `README.md` after an audit measured the tag namespace against the remote.

**Withdrawn: "per-bundle immutable snapshot."** `PROFILE.md` §7 described a release tag that way. It is not accurate. Tags mark repository-wide publication events, and where one commit published or enriched several bundles, several tags were applied to that commit. **29 tags resolve to 18 distinct commits; 16 of the 29 share just 5.** `v0.5.2`, `v0.4.2` and `v0.6.1` are one git object; so are `v0.6.0`, `v0.7.0` and `v0.8.0`.

**Corrected in `VERSIONING.md`:**

- The worked example for comparing releases was `git diff v0.7.0 v0.8.0 -- okf/`. Those tags are the same commit, so the command returns **nothing**. Replaced with a SHA-scoped, per-bundle diff and a warning to resolve tags with `git rev-parse` first.
- **Academic citation guidance now leads with the bundle name and commit SHA.** A tag may be cited in addition, never instead — a tag alone does not identify a bundle.
- The axes table goes from three to four, adding `okf_profile` to match `PROFILE.md` §7.
- `bundle_version` is redefined as what it has always actually been: **the bundle revision current when that document was last edited** — a per-document marker, not a bundle-wide constant. A wave touches a subset of files, so one bundle legitimately carries several values (`sankhya-darshana` spans 0.13.0–0.13.2). The bundle-wide value is the one in the bundle's root `index.md`.
- Rule 2 now carries a **known-gap notice**: the patch-bump rule has not been applied consistently. Seven bundle-root indexes trail their newest tag, and `dharma-foundation`'s 25 concept documents carry no `bundle_version` at all. Reconciliation and backfill are scheduled.

**Also corrected in `PROFILE.md` §2.3:** `related:` was described as carrying "bundle-relative paths." At this revision **1,074 of 1,075 entries use the bundle-absolute form** — the form §3.1 requires bodies not to use. Inert, because `related:` is not traversed, but disclosed rather than left misdescribed.

**Corrected in `README.md`:** three rows of the bundle table listed a release older than that bundle's newest tag — `cosmology-creation` v0.7.1 → **v0.7.2**, `shakta-darshana` v0.8.0 → **v0.8.1**, `sankhya-darshana` v0.13.1 → **v0.13.2**. Banner figures (13 bundles · 310 concepts · 132 references) were re-measured and are correct.

**Not repaired: the tags themselves.** `VERSIONING.md` rule 4 states tags never move. Rewriting sixteen published tags to fix a naming defect would break the contract's only real guarantee in order to tidy a cosmetic one. **Forward scheme from the next release:** per-bundle tags are namespaced `bundle/<name>/vX.Y.Z`; repository-wide milestones keep the bare `vX.Y.Z`. Legacy tags remain valid citations when paired with a bundle name.

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

The files named in [GENEALOGIES.md](GENEALOGIES.md)'s Reverse Index received an **Error Genealogy** section — a documented summary (named source, date, propagation chain) plus a link to the canonical genealogy — back-porting v0.8 `shakta-darshana`'s genealogy-native standard to the older bundles.

**Retrofitted: 17 files across 5 bundles.**

| Bundle | Files | Genealogies |
|---|---|---|
| `dharma-foundation` (v0.1) | chakra, karma, samsara *(partial)*, yoga, dharma, moksha, maya | G1, G2, G4, G5, G6, G7, G8 |
| `bhakti-marga` (v0.4) | murti, puja *(partial)*, guru, nada-brahman *(partial)* | G9, G11, G13 |
| `cosmology-creation` (v0.7) | maya-cosmological, purusha-sukta, trimurti | G8, G10, G12 |
| `dharmic-ethics` (v0.5) | rta *(partial)*, svadharma *(partial)* | G6, G10 |
| `vedanta-epistemology` (v0.3) | mithya *(partial)* | G8 |

`shakta-darshana` (v0.8) was authored genealogy-native and needed no retrofit; its 7 genealogy-bearing files bring the corpus total carrying an Error Genealogy section to **24**.

**Note on `dharma-foundation`.** This bundle predates the per-file `bundle_version` key and none of its 25 concept documents carry one, so its Phase 2 edits are recorded here rather than by a version bump. Backfilling `bundle_version` across the bundle is scheduled with the normalization pass; until then this log is the only revision record for those files.

**Tooling in the same wave:** `okf/tools/okf_validate.py` extended with link-resolution and slug checks, and a per-bundle `pytest` suite added under `okf/tests/`.

## 2026-06 — OKF v0.2: the structured `not:` field (format wave)

The wave that gave the corpus its present shape. Recorded here because it is the dated provenance for `PROFILE.md` §2.1 and §6, and because it predates this CHANGELOG's first entry.

### PR #1 — the structured-`not:` exemplar

Merge [`dc137e5`](https://github.com/dharma-okf-foundation/dharma-okf/commit/dc137e5) (PR #1, branch `okf-0.2-audit`), **2026-06-24** — *"OKF v0.2: darshana, structured not, citations + references, validator"*.

One file, **+15 / −8**: `okf/dharma-foundation/concepts/ahankara.md`. Small, and load-bearing — it is the first appearance in this repository of the conventions the profile is now built on:

- **`not:` converted from a flat list of strings to the structured three-key form.** Before: `- Ego (Freudian)`, `- Self-identity`, `- Pride`, `- Narcissism`. After: each rejected rendering paired with a `why` explaining what the substitution imports or strips, and an `instead` giving the positive redirect. This is the `term` / `why` / `instead` structure specified in `PROFILE.md` §2.1.
- **`darshana:` introduced** — `Sāṃkhya` on this document, the first school attribution in the corpus (§2.2).
- **`## Key Sources` renamed `## Citations`**, with bare source names converted to links into `references/` — the body-link citation form that §2.5 records as the corpus's only source of graph edges.

**Why this commit matters as provenance.** `PROFILE.md` §6 dates the structured form to 2026-06-24. `dc137e5` is that date as a git-timestamped, publicly verifiable artifact, and its diff shows both the before and the after state — evidence a reader can check without trusting this repository's own account. It is also the only change in the project's history merged through a pull request rather than committed directly to `main`, which is why a PR number exists to cite.

**Scope, stated plainly:** this commit changed one document. It set the pattern; it did not roll it out.

### Corpus-wide rollout, 2026-06-25 (direct to `main`)

The pattern from PR #1 applied across the then-published bundles, in a sequence of direct commits: `70109d7` (bump concept `okf_version`), `181ab20` (13 reference documents; 12 receive `okf_version: 0.2`), [`f6f0f0c`](https://github.com/dharma-okf-foundation/dharma-okf/commit/f6f0f0c) (format ratification), `0420e0e` (index `okf_version` + bundle index at `0.1.1`). `yoga-darshana` and `vedanta-epistemology` were published in the same window, authored to the new form.

Two disclosures about this rollout, both since acted on:

- **It recorded the ratification by editing `okf/SPEC.md`** — upstream's file, vendored in this repository. That practice is what Wave 0 retired in favour of `PROFILE.md`; the edits no longer exist on `main`.
- **The citation links it introduced use the bundle-relative absolute form** (`/references/samkhya-karika.md`), following base §6.1's recommendation. Upstream's reference viewer discards that form, so those links produce no graph edges — see `PROFILE.md` §3.1 and upstream issue [#201](https://github.com/GoogleCloudPlatform/knowledge-catalog/issues/201). This wave is the origin of the 400-link Level 2 gap, and normalising it is scheduled.

### Adoption layer, 2026-06-26

- **Added [INTEGRATION.md](INTEGRATION.md)** — how to make the `not:` constraint functionally binding rather than merely present: a system-prompt template injecting the positive `instead` redirect rather than a bare prohibition, a RAG negative-filter pattern, and an output check, with stated caveats about negative-prompt leakage.
- **Added [demos/failure-vs-success.md](demos/failure-vs-success.md)** — side-by-side transcripts of downstream reasoning failures with and without the constraint applied.
- **README reframed** around the dual-action design (boundary plus scaffold) and the v0.2 format.

**Not recorded here:** the per-bundle publication history for v0.1 through v0.5. Those are the release tags' job, and duplicating them in this log would create a second record to keep in sync. See the tag list and `VERSIONING.md`.
