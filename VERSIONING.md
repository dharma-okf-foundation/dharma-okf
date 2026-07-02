# VERSIONING.md — The Dharma-OKF Update Contract

**Status: declared 2026-07-02, before any known external consumer existed. This document states the repository's standing policy so that no future consumer can be surprised by it.**

## The Two Surfaces

This repository deliberately offers two consumption surfaces, and both are first-class:

1. **`main` is a living vocabulary.** Concept files on main are enriched over time: sharper `not:` fields, added citations, documented error genealogies, new cross-bundle warnings. If you want the best current state of the vocabulary, consume main. (This is the Schema.org model: published terms improve in place.)
2. **Release tags are immutable archival snapshots.** `v0.1.0`, `v0.2.0`, ... mark the repository state at each bundle release. Tags are never moved, deleted, or rewritten after publication. If you need citation stability (academic reference, reproducible pipelines, dataset provenance), pin a tag or a commit SHA.

Nothing about in-place enrichment on main affects the meaning of a citation to a tag. That is the whole contract in one sentence.

## Version Axes (three, kept distinct)

| Axis | Where | Means |
|------|-------|-------|
| **Release tag** | git tags (`v0.8.0`) | A snapshot event: a bundle's publication or a major corpus milestone |
| **`bundle_version`** | each file's frontmatter (`"0.8.0"`) | That bundle's CONTENT revision. Patch bumps (`0.1.1` → `0.1.2`) signal in-place enrichment under this contract |
| **`okf_version`** | each file's frontmatter (`"0.2"`) | The OKF FORMAT specification version. Changes only when the file format itself changes |

## Rules of Change

1. **Corrections** (typos, broken links, factual errors): committed to main any time; noted in CHANGELOG.md if substantive.
2. **Enrichments** (added genealogies, strengthened `not:` fields, new citations): committed to main in documented waves; every touched bundle gets a `bundle_version` patch bump; every wave gets a CHANGELOG.md entry naming the files and the nature of the change.
3. **New concepts or removals** within a live bundle: minor bump (`0.1.x` → `0.2.0` content version) + changelog + release note.
4. **Tags never move.** A post-release fix means main advances; if the release must reference the fixed state, a new patch tag is created (`v0.8.1`); the old tag stays.
5. **Slugs are permanent.** Concept filenames/IDs never change after publication (the bridge contract of the two-stack architecture). Disambiguation is done by suffix at creation time (`chakra-tantra`, `maya-shakta`), never by rename.

## Guidance for Consumers

- **RAG / training pipelines:** consume main for the best vocabulary; record the commit SHA you ingested for provenance.
- **Academic citation:** cite a tag (e.g., `v0.8.0`) or SHA; the format is: Dharma-OKF Foundation, bundle name, version, year, URL.
- **Diffing releases:** `git diff v0.7.0 v0.8.0 -- okf/` shows exactly what changed between snapshots.

## Changelog

In-place change waves are logged in [CHANGELOG.md](CHANGELOG.md), newest first. The first entry under this contract is the Genealogy Update (see [GENEALOGIES.md](GENEALOGIES.md)).

---

*Declared by the Dharma-OKF Foundation, 2026-07-02. License: CC BY-SA 4.0, matching the corpus.*
