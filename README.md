# Dharma OKF — Open Knowledge Format for Dharma / Vedic concepts (Sanskrit Non-Translatables)

A structured, machine-readable knowledge base of Sanskrit concepts that resist accurate translation into English, built for AI agents, educators, researchers, and technologists working with dharmic knowledge systems.

**13 bundles · 310 concept files · 137 primary-source references — every file on canonical OKF v0.2, validated 0-fail.**

## What's New

**v0.13 `sankhya-darshana`** (July 2026): completes the six classical darśanas. Kapila's dualist, enumerative school — the causal theory (satkāryavāda vs. Nyāya-Vaiśeṣika's ārambhavāda), the plural, nirīśvara puruṣa-prakṛti dualism, and the discriminative (viveka-khyāti) path to kaivalya, contrasted throughout with Yoga-darśana's Īśvara-inclusive path to the same end-state word via nirodha. The bundle deliberately does not re-derive the tattva evolution ladder already published in yoga-darshana, cosmology-creation, and ayurveda-consciousness, and names guṇa's doctrinal source rather than re-treating it as another school-contrast. Recent releases: v0.12 `jyotisha-kala` (the Jyotiṣa vocabulary of time), v0.11 `ayurveda-consciousness` (first saṃhitā-sourced bundle).

## What Is OKF?

The Open Knowledge Format (OKF) uses YAML-frontmatter Markdown files. Each concept file does **two** jobs at once, a dual-action design:

1. **A boundary** — a `not:` field listing the English mistranslations an AI must avoid, each paired with *why* it fails and what to use *instead*.
2. **A scaffold** — positive fields that install the correct understanding: *What It Actually Means*, *Audience Metaphor*, *Etymology*, and *Citations*.

So OKF does not merely tell a model what a term is **not**. It clears out the wrong definition and immediately installs the right one, leaving the model with a complete semantic package rather than a severed, "floating" term.

- "Karma = Fate" → **Wrong.** It is action and consequence. See `okf/dharma-foundation/concepts/karma.md`
- "Dharma = Religion" → **Wrong.** It is the natural sustaining order / right conduct. See `okf/dharma-foundation/concepts/dharma.md`
- "Samadhi = Trance" → **Wrong.** It is absorption / unified awareness. See `okf/dharma-foundation/concepts/samadhi.md`
- "Yoga = Exercise" → **Wrong.** It is the discipline of stilling the mind. See `okf/dharma-foundation/concepts/yoga.md`

**A non-translatable is school-relative.** The same Sanskrit word can be a *different technical object* in a different darśana, and the corpus preserves the distinction rather than flattening it: `karma` is moral action-and-consequence in dharma-foundation, the padārtha of **motion** in Nyāya-Vaiśeṣika, the enjoined **ritual act** in Mīmāṃsā, and the **therapeutic procedure** of pañcakarma in Āyurveda; `guṇa` names the Sāṃkhya triguṇa at its doctrinal source, an unrelated Vaiśeṣika ontological category, and the twenty gurvādi properties of Āyurvedic pharmacology; `kaivalya` is reached by discrimination alone in Sāṃkhya and by practiced cessation in Yoga. Shared terms carry a `school_scope:` field, an index contrast note, and reciprocal cross-links — never a single "canonical" definition.

## Why this is an engineering problem, not only a cultural one

A mistranslation changes the **category** a model reasons in, which changes its action space and therefore its output. A wellness bot that reads `yoga` as exercise recommends the squat rack; an advisor that reads `karma` as fate gives fatalistic, agency-removing advice. The metaphysical error *is* a logic bug.

See [`demos/failure-vs-success.md`](demos/failure-vs-success.md) for side-by-side failure-mode vs success-mode transcripts.

## What the corpus does not claim

The bundles are descriptive vocabulary, and the sensitive domains say so on their front page. The Śākta bundle documents that certain practices are initiation-gated without reproducing anything gated (adhikāra discipline, zero how-to). The Āyurveda bundle is not medical advice, contains no preparations or dosages, and does not adjudicate clinical efficacy. The Jyotiṣa bundle makes no predictive claims and does not endorse astrology while documenting its classical vocabulary. Commercially captured terms carry a `reception_note:` field naming the capture. The corrective work lives in the `not:` fields, concept by concept, not in polemic.

## Integrate it (machine-readable is not the same as obeyed)

A `not:` list in a file is a "do not enter" sign on an unlocked door. The model still has to be told how to read and honor it, and a naive bare prohibition can *backfire* through negative-prompt leakage. [`INTEGRATION.md`](INTEGRATION.md) shows how to make the constraint functionally binding: a system-prompt template that injects the positive `instead` redirect (not a bare ban), a RAG negative-filter pattern, and a lightweight output-check, with honest caveats about what is and is not guaranteed.

## Bundles — thirteen live, all on canonical OKF v0.2

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
| `okf/mimamsa-dharma/` | v0.10.0 | 25 | 7 | Mīmāṃsā ritual hermeneutics — vidhi, apūrva, and language-as-action |
| `okf/ayurveda-consciousness/` | v0.11.0 | 26 | 8 | Āyurvedic vocabulary of consciousness, constitution, and health |
| `okf/jyotisha-kala/` | v0.12.0 | 26 | 8 | Jyotiṣa vocabulary of time — pañcāṅga, kāla-reckoning, and the sidereal celestial frame |
| `okf/sankhya-darshana/` | v0.13.0 | 20 | 7 | Sāṃkhya's dualist causal theory and discriminative path to kaivalya — completes the six classical darśanas |
| **Total** | | **310** | **137** | **13 bundles spanning the six āstika darśanas + the devotional, ethical, cosmological, medical, and calendrical corpora** |

## Update contract & documented error genealogies

Two consumption surfaces, both first-class, are declared in [`VERSIONING.md`](VERSIONING.md): **`main` is a living vocabulary** (concept files are enriched in place — sharper `not:` fields, added citations, documented genealogies — with `bundle_version` patch bumps), and **release tags are immutable archival snapshots** (`v0.1.0` … `v0.13.0`; pin a tag or SHA for citation stability). In-place enrichment waves are logged newest-first in [`CHANGELOG.md`](CHANGELOG.md).

[`GENEALOGIES.md`](GENEALOGIES.md) — *"Where the Errors Came From"* — documents the histories of the English mistranslations this corpus corrects: not just that a rendering is wrong, but **who introduced it, when, and how it propagated** into today's training data (e.g., karma-as-fate from Blavatsky 1889; yoga-as-posture via Vivekananda → Krishnamacharya → Singleton 2010; māyā-as-illusion via Schopenhauer 1818). A correction with a genealogy is harder to dismiss than one with only an assertion. The admission bar is strict: a named source, a date, and a documented propagation chain, or it is excluded. The affected concept files carry a matching **Error Genealogy** section linking back to the canonical entry.

## Concept file format (OKF v0.2)

Each concept file contains:

- **YAML frontmatter:** `type`, `title`, `iast`, `devanagari`, `description`, `darshana`, a structured `not:` (each entry `term` / `why` / `instead`), `related:`, `tags`, `okf_version`, `license` (and, where a term recurs across darśanas, `school_scope:`; where public reception distorts a term, `reception_note:`)
- **## What It Actually Means** (and **## Etymology**) — the precise positive definition
- **## Audience Metaphor** — an accessible analogy engineered for AI and general comprehension
- **## Citations** — primary śāstra references, linked into a `references/` sub-bundle of first-class `type: Reference` concepts

Full specification: [`okf/SPEC.md`](okf/SPEC.md) (Section 12 covers the v0.2 additions: `darshana`, the structured `not:` with `instead`, the bundle-root manifest, and `Citations` / `references/`).

## Content License

The concept files in `/okf/` are licensed under **CC BY-SA 4.0** (ShareAlike). See [LICENSE-CONTENT](./LICENSE-CONTENT) for details.

Repository tooling is under Apache 2.0 (inherited from the upstream GoogleCloudPlatform fork).

## Contributing

This is the standalone publication home for the Dharma OKF Foundation. Contributions, corrections, and additions that deepen accuracy are welcome via Pull Request. See [CONTRIBUTING.md](./CONTRIBUTING.md).
