# Dharma OKF — Open Knowledge Format for Dharma / Vedic concepts (Sanskrit Non-Translatables)

A structured, machine-readable knowledge base of Sanskrit concepts that resist accurate translation into English, built for AI agents, educators, researchers, and technologists working with dharmic knowledge systems.

**11 bundles · 264 concept files · 122 primary-source references — every file on canonical OKF v0.2, validated 0-fail.**

## What Is OKF?

The Open Knowledge Format (OKF) uses YAML-frontmatter Markdown files. Each concept file does **two** jobs at once, a dual-action design:

1. **A boundary** — a `not:` field listing the English mistranslations an AI must avoid, each paired with *why* it fails and what to use *instead*.
2. **A scaffold** — positive fields that install the correct understanding: *What It Actually Means*, *Audience Metaphor*, *Etymology*, and *Citations*.

So OKF does not merely tell a model what a term is **not**. It clears out the wrong definition and immediately installs the right one, leaving the model with a complete semantic package rather than a severed, "floating" term.

- "Karma = Fate" → **Wrong.** It is action and consequence. See `okf/dharma-foundation/concepts/karma.md`
- "Dharma = Religion" → **Wrong.** It is the natural sustaining order / right conduct. See `okf/dharma-foundation/concepts/dharma.md`
- "Samadhi = Trance" → **Wrong.** It is absorption / unified awareness. See `okf/dharma-foundation/concepts/samadhi.md`
- "Yoga = Exercise" → **Wrong.** It is the discipline of stilling the mind. See `okf/dharma-foundation/concepts/yoga.md`

**A non-translatable is school-relative.** The same Sanskrit word can be a *different technical object* in a different darśana, and the corpus preserves the distinction rather than flattening it: `karma` is moral action-and-consequence in dharma-foundation but the padārtha of **motion** in Nyāya-Vaiśeṣika; `anumāna` is a full pramāṇa yielding certainty in Nyāya but auxiliary-to-śabda in Advaita. Shared terms carry a `school_scope:` field, an index contrast note, and reciprocal cross-links — never a single "canonical" definition.

## Why this is an engineering problem, not only a cultural one

A mistranslation changes the **category** a model reasons in, which changes its action space and therefore its output. A wellness bot that reads `yoga` as exercise recommends the squat rack; an advisor that reads `karma` as fate gives fatalistic, agency-removing advice. The metaphysical error *is* a logic bug.

See [`demos/failure-vs-success.md`](demos/failure-vs-success.md) for side-by-side failure-mode vs success-mode transcripts.

## Integrate it (machine-readable is not the same as obeyed)

A `not:` list in a file is a "do not enter" sign on an unlocked door. The model still has to be told how to read and honor it, and a naive bare prohibition can *backfire* through negative-prompt leakage. [`INTEGRATION.md`](INTEGRATION.md) shows how to make the constraint functionally binding: a system-prompt template that injects the positive `instead` redirect (not a bare ban), a RAG negative-filter pattern, and a lightweight output-check, with honest caveats about what is and is not guaranteed.

## Bundles — nine live, all on canonical OKF v0.2

| Bundle | Release | Concepts | Refs | Theme |
|---|---|---|---|---|
| `okf/dharma-foundation/` | v0.1.2 | 25 | 13 | Foundational Sanskrit non-translatable vocabulary |
| `okf/yoga-darshana/` | v0.2.0 | 26 | 7 | Patañjali's Yoga Sūtra technical lexicon |
| `okf/vedanta-epistemology/` | v0.3.1 | 27 | 20 | Pramāṇa-śāstra — Vedantic epistemology |
| `okf/bhakti-marga/` | v0.4.1 | 15 | 10 | The vocabulary of the devotional path |
| `okf/dharmic-ethics/` | v0.5.1 | 15 | 7 | Yama–Niyama and the ethical-social vocabulary of dharma |
| `okf/upanishadic-core/` | v0.6.0 | 26 | 16 | Core Upaniṣadic vocabulary across the Vedānta schools — mahāvākyas, Ātman–Brahman, self-knowledge |
| `okf/cosmology-creation/` | v0.7.1 | 26 | 12 | Vedic & Purāṇic vocabulary of time, cosmos, and manifestation |
| `okf/shakta-darshana/` | v0.8.0 | 26 | 12 | Śākta-Tāntric metaphysics of Śakti, Devī, and consciousness-power |
| `okf/nyaya-vaisheshika/` | v0.9.0 | 27 | 10 | The science of inference and debate — Nyāya apparatus + Vaiśeṣika realist ontology |
| `okf/mimamsa-dharma/` | v0.10.0 | 25 | 7 | Mimamsa is one of the world's earliest systematic theories of language-as-action and self-validating knowledge |
| `okf/ayurveda-consciousness/` | v0.11.0 | 26 | 8 | school_scope: ayurveda on prakriti, guna, rasa |
| **Total** | | **264** | **122** | **11 bundles spanning the six āstika darśanas + the devotional, ethical, and cosmological corpora** |

## Update contract & documented error genealogies

Two consumption surfaces, both first-class, are declared in [`VERSIONING.md`](VERSIONING.md): **`main` is a living vocabulary** (concept files are enriched in place — sharper `not:` fields, added citations, documented genealogies — with `bundle_version` patch bumps), and **release tags are immutable archival snapshots** (`v0.1.0` … `v0.9.0`; pin a tag or SHA for citation stability). In-place enrichment waves are logged newest-first in [`CHANGELOG.md`](CHANGELOG.md).

[`GENEALOGIES.md`](GENEALOGIES.md) — *"Where the Errors Came From"* — documents the histories of the English mistranslations this corpus corrects: not just that a rendering is wrong, but **who introduced it, when, and how it propagated** into today's training data (e.g., karma-as-fate from Blavatsky 1889; yoga-as-posture via Vivekananda → Krishnamacharya → Singleton 2010; māyā-as-illusion via Schopenhauer 1818). A correction with a genealogy is harder to dismiss than one with only an assertion. The admission bar is strict: a named source, a date, and a documented propagation chain, or it is excluded. The affected concept files carry a matching **Error Genealogy** section linking back to the canonical entry.

## Concept file format (OKF v0.2)

Each concept file contains:

- **YAML frontmatter:** `type`, `title`, `iast`, `devanagari`, `description`, `darshana`, a structured `not:` (each entry `term` / `why` / `instead`), `related:`, `tags`, `okf_version`, `license` (and, where a term recurs across darśanas, `school_scope:`)
- **## What It Actually Means** (and **## Etymology**) — the precise positive definition
- **## Audience Metaphor** — an accessible analogy engineered for AI and general comprehension
- **## Citations** — primary śāstra references, linked into a `references/` sub-bundle of first-class `type: Reference` concepts

Full specification: [`okf/SPEC.md`](okf/SPEC.md) (Section 12 covers the v0.2 additions: `darshana`, the structured `not:` with `instead`, the bundle-root manifest, and `Citations` / `references/`).

## Content License

The concept files in `/okf/` are licensed under **CC BY-SA 4.0** (ShareAlike). See [LICENSE-CONTENT](./LICENSE-CONTENT) for details.

Repository tooling is under Apache 2.0 (inherited from the upstream GoogleCloudPlatform fork).

## Contributing

This is the standalone publication home for the Dharma OKF Foundation. Contributions, corrections, and additions that deepen accuracy are welcome via Pull Request. See [CONTRIBUTING.md](./CONTRIBUTING.md).
