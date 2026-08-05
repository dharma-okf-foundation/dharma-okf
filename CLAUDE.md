# dharma-okf — agent working rules

This repository publishes **Dharma-OKF**, a profile of the Open Knowledge Format. Read `PROFILE.md` before changing anything; it is normative and this file is its operational summary. Where the two disagree, `PROFILE.md` wins and this file is the bug.

**Base spec:** OKF v0.2 at `GoogleCloudPlatform/knowledge-catalog@3fcbb9f`. **Profile:** `dharma-okf/1.0`.
**Corpus:** 442 concept documents in 13 bundles — 310 `type: Concept`, 132 `type: Reference`.

---

## The one thing to understand first

**On OKF v0.2, the specification and the reference implementation disagree.** Reading `SPEC.md` alone will lead you to author bundles that upstream's own tooling silently mishandles. Every rule below marked ⚠️ exists because of a specific divergence that was verified by reading upstream source, not upstream prose. Do not "correct" them back toward the spec text.

---

## Never

These are refusals. If a task appears to require one, stop and ask.

1. **Never write `verified:`.** It records a human review event by a tradition-bearer. Automated tooling writes `generated:` and nothing else. Stamping `verified:` during a mechanical edit asserts that a person checked a document no person checked — it converts the corpus's central trust claim into noise. (`PROFILE.md` §3.3)
2. **Never flatten `not:` to a list of strings.** The `term` / `why` / `instead` triple is the payload, not decoration. `why` is the argument; `instead` is what a consuming agent actually executes as a prompt or filter constraint. A bare `["Fate", "Destiny"]` is the abandoned v0.1 shape and destroys the field's function across 310 files. (§2.1)
3. **Never delete `## Citations` body sections or their links** when adding `sources:` frontmatter. Body links are the **only** source of graph edges — `related:` frontmatter is not traversed by link-graph consumers. Removing them silently deletes the bundle's relationship graph. Frontmatter `sources` is *added alongside*, never *migrated from*. (§2.5, §3.1)
4. **Never claim another producer's identity in `generated.by`.** `reference_agent/...` is Google's. Use your own namespace: `claude-opus-5/<version>`, `gemini-spark/<version>`. (§2.3, base §7)
5. **Never change a document's `type:` value.** It is `Concept` or `Reference`. Both are load-bearing: `Reference` is colour-matched by upstream's viewer, and the split is what makes `not:`-applicability checkable. (§1)
6. **Never edit files under a release tag's assumptions.** `main` is the living vocabulary; tags are immutable snapshots. Content revisions patch-bump `bundle_version` and append to `CHANGELOG.md`. See `VERSIONING.md`.

---

## Authoring a concept

```yaml
---
type: Concept                      # or Reference. Never anything else.
title: "Dharma"
description: "One line, including the key 'not' contrasts."
id: dharma
iast: "Dharma"
devanagari: "धर्म"
bundle: dharma-foundation
bundle_version: "0.1.3"
darshana:                          # REQUIRED on Concept. A list. Doctrinal claim, not a tag.
  - Pan-dharmic
school_scope: "…"                  # optional prose nuance
text_source: "…"                   # optional primary anchor
tags: [ … ]
not:                               # REQUIRED on Concept. Structured. Never strings.
  - term: "Religion"
    why: "Implies a belief system with founder, book, and creed; Dharma has no founder…"
    instead: "Keep Dharma untranslated; gloss per context."
  - term: "Duty"
    why: "Strips the cosmic dimension, reducing Dharma to social obligation."
related:
  - ../concepts/karma.md
generated: { by: "<producer>/<version>", at: "<ISO 8601>" }
okf_version: "0.2"                 # UPSTREAM spec version. Not ours.
okf_profile: "dharma-okf/1.0"      # Ours.
license: "CC BY-SA 4.0"
---
```

Body order: `# Title — देवनागरी` → `**Not:** term, term, …` (human echo of the frontmatter) → teaching sections → `## Audience Metaphor` → `## Citations`.

`not:` and `darshana:` are required on every `Concept` and are currently at 310/310. Do not be the commit that breaks that.

---

## ⚠️ Link form: relative, never absolute

```markdown
✅  [karma](../concepts/karma.md)      ✅  [karma](./karma.md)
❌  [karma](/concepts/karma.md)
```

Base §6.1 *recommends* the absolute form. Upstream's reference viewer discards it:

```python
# okf/src/reference_agent/viewer/generator.py :: _extract_links
if "://" in target or target.startswith("/"):
    continue
```

Absolute links produce **no graph edge**. Eight of thirteen bundles are already clean; five legacy bundles carry 400 absolute links pending normalization. Author relative. If you see absolute links in a file you are editing for another reason, leave them — normalization is a scheduled wave with its own validation, not a drive-by fix.

---

## ⚠️ Index files

Every directory holding concepts needs an `index.md` in base §8 form — **no frontmatter**, sections of `* [Title](file) - description.` bullets. Currently 18 of 39 directories have one; all 13 `concepts/` directories are missing theirs.

The **bundle-root** `index.md` is the sole exception permitted to carry frontmatter. Do not add frontmatter to any other index.

---

## Version axes — keep them distinct

| Key | Means |
|---|---|
| `okf_version: "0.2"` | **Upstream's** spec version, at the pinned commit. Never ours. |
| `okf_profile: "dharma-okf/1.0"` | This profile. |
| `bundle_version` | A bundle's content revision. Patch-bump on enrichment. |
| git tag `v0.13.0` | Per-bundle immutable release snapshot. |

Conflating these has caused real confusion in this project's history. `okf_version` is **not** a release number.

---

## Declined base features — do not add them

- **`stale_after`** — a non-translatable has no review cadence. Absence is the honest signal and `is_stale()` correctly returns `False`. Adding a date asserts a freshness claim this project cannot honour. (§4.1)
- **Attested Computation** (`runtime`, `parameters`, `executor`, `attester`) — nothing here is computed. (§4.2)

If a task asks for either, it is working from the base spec without the profile. Point at `PROFILE.md` §4.

---

## Before any push

1. `python3 okf/tools/okf_validate.py --strict` → expect **0 fail / 0 warn**.
2. `python3 -m pytest okf/tests/` for the touched bundle.
3. Confirm every body link resolves and none begin with `/`.
4. Patch-bump `bundle_version` on **touched files only**; append to `CHANGELOG.md`.
5. Clone-diff verify after upload: `git clone` to a temp dir, `diff -rq` against the local mirror → empty.

The mirror is the source of truth for what is published. Never push from a local tree that has drifted from it — reconcile local ← remote first, or an upload will silently strip work done directly on `main`.

---

## Reading upstream

Always read the base spec and its source **at the pinned commit `3fcbb9f`**, never at `main`.

> **Never press GitHub's "Sync fork" button on this repository.** Upstream has modified files this repo deleted (`okf/SPEC.md`, `toolbox/mdcode/*`), so a sync hits delete-vs-modify conflicts and GitHub's fallback offer is "Discard commits" — which discards *ours*, not theirs. Detaching the fork is an open follow-up; until then, the button is one click from losing the corpus.

`raw.githubusercontent.com` has been observed serving a mixed pre-/post-v0.2 state on upstream's `main`: `document.py` returning the v0.1 file while `generator.py` returns the v0.2 file that imports symbols from it. Those cannot coexist in a working tree. If a conformance question matters, clone at the SHA rather than fetching raw.
