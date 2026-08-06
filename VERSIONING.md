# VERSIONING.md — The Dharma-OKF Update Contract

**Status: declared 2026-07-02, before any known external consumer existed. This document states the repository's standing policy so that no future consumer can be surprised by it.**

## The Two Surfaces

This repository deliberately offers two consumption surfaces, and both are first-class:

1. **`main` is a living vocabulary.** Concept files on main are enriched over time: sharper `not:` fields, added citations, documented error genealogies, new cross-bundle warnings. If you want the best current state of the vocabulary, consume main. (This is the Schema.org model: published terms improve in place.)
2. **Release tags are immutable archival snapshots.** `v0.1.0`, `v0.2.0`, ... mark the repository state at each bundle release. Tags are never moved, deleted, or rewritten after publication. If you need citation stability (academic reference, reproducible pipelines, dataset provenance), pin a tag or a commit SHA.

Nothing about in-place enrichment on main affects the meaning of a citation to a tag. That is the whole contract in one sentence.

## Version Axes (four, kept distinct)

| Axis | Where | Means |
|------|-------|-------|
| **Release tag** | git tags (`v0.8.0`) | A snapshot of the **whole repository** at a publication event, named after the bundle that occasioned it. **It does not isolate one bundle** — see Tag History below |
| **`okf_profile`** | each file's frontmatter (`"dharma-okf/1.0"`) | The Dharma-OKF PROFILE version. See `PROFILE.md` §7 |
| **`bundle_version`** | each file's frontmatter (`"0.8.0"`) | The bundle revision current **when that document was last edited**. Patch bumps (`0.1.1` → `0.1.2`) signal in-place enrichment. Because a wave touches a subset of files, one bundle may carry several values at once; the bundle-wide value is the one in its root `index.md` |
| **`okf_version`** | each file's frontmatter (`"0.2"`) | The OKF FORMAT specification version. Changes only when the file format itself changes |

## Rules of Change

1. **Corrections** (typos, broken links, factual errors): committed to main any time; noted in CHANGELOG.md if substantive.
2. **Enrichments** (added genealogies, strengthened `not:` fields, new citations): committed to main in documented waves; every **file touched** gets a `bundle_version` patch bump and the bundle's root `index.md` is bumped to match; every wave gets a CHANGELOG.md entry naming the files and the nature of the change.

   > **Known gap — half closed, half open.** This rule was not applied consistently for much of the corpus's history.
   >
   > **Closed 2026-08-06:** seven bundle-root indexes trailed their newest tag and have been reconciled — `dharma-foundation`, `yoga-darshana`, `vedanta-epistemology`, `bhakti-marga`, `dharmic-ethics`, `shakta-darshana`, `sankhya-darshana`. **All thirteen bundle-root indexes now match their bundle's newest release tag.** See `CHANGELOG.md`, *Bundle-root index reconciliation*.
   >
   > **Still open:** **`dharma-foundation`'s 25 concept documents carry no `bundle_version` at all** — the bundle predates the key. That backfill is scheduled with the normalization pass. Bundle-root indexes also remain split between the `version:` and `bundle_version:` key names (twelve and one); unifying them is scheduled with the same pass, since `PROFILE.md` §1.1 discloses `version` by name and both must move together.
3. **New concepts or removals** within a live bundle: minor bump (`0.1.x` → `0.2.0` content version) + changelog + release note.
4. **Tags never move.** A post-release fix means main advances; if the release must reference the fixed state, a new patch tag is created (`v0.8.1`); the old tag stays.
5. **Slugs are permanent.** Concept filenames/IDs never change after publication (the bridge contract of the two-stack architecture). Disambiguation is done by suffix at creation time (`chakra-tantra`, `maya-shakta`), never by rename.

## Guidance for Consumers

- **RAG / training pipelines:** consume main for the best vocabulary; record the commit SHA you ingested for provenance.
- **Academic citation — cite the bundle name and the commit SHA.** Format: *Dharma-OKF Foundation, `<bundle>`, `<bundle_version>`, commit `<sha>`, year, URL.* A tag may be cited **in addition**, never instead: tags do not uniquely identify a bundle (see Tag History below). Example: *Dharma-OKF Foundation, `yoga-darshana`, 0.2.1, commit `e5cc501`, 2026, https://github.com/dharma-okf-foundation/dharma-okf*.
- **Diffing releases:** scope the diff to the bundle you care about — `git diff <sha-a> <sha-b> -- okf/<bundle>/`. **Do not diff two tags blind:** several tags share a commit, so `git diff v0.7.0 v0.8.0` returns empty. Resolve first with `git rev-parse v0.7.0^{commit}`.

## Tag History — a disclosed defect, not repaired

Tags mark repository-wide publication events. Where one commit published or enriched several bundles, several tags were applied to that one commit. **29 tags resolve to 18 distinct commits; 16 of the 29 share just 5:**

| Commit | Tags |
|---|---|
| `fd71535` | `v0.1.2` · `v0.3.1` · `v0.4.1` · `v0.5.1` · `v0.7.1` |
| `e5cc501` | `v0.1.3` · `v0.2.1` · `v0.3.2` |
| `183effd` | `v0.4.2` · `v0.5.2` · `v0.6.1` |
| `e90f60c` | `v0.6.0` · `v0.7.0` · `v0.8.0` |
| `3a6d595` | `v0.7.2` · `v0.8.1` |

**Why they are not being fixed.** Rule 4 says tags never move. Rewriting sixteen published tags to correct a naming defect would break the only guarantee this contract makes, in order to tidy a cosmetic one. The defect is disclosed instead.

**Forward scheme, from the next release.** Per-bundle tags are namespaced `bundle/<name>/vX.Y.Z`, so a tag names exactly one bundle and cannot collide. Repository-wide milestones keep the bare `vX.Y.Z` form. Legacy tags remain valid citations when paired with a bundle name.

## Changelog

In-place change waves are logged in [CHANGELOG.md](CHANGELOG.md), newest first. The first entry under this contract is the Genealogy Update (see [GENEALOGIES.md](GENEALOGIES.md)).

---

*Declared by the Dharma-OKF Foundation, 2026-07-02. License: CC BY-SA 4.0, matching the corpus.*
