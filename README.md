# Dharma OKF — Open Knowledge Format for Dharma / Vedic concepts (Sanskrit Non-Translatables)

A structured, machine-readable knowledge base of Sanskrit concepts that resist accurate translation into English, built for AI agents, educators, researchers, and technologists working with dharmic knowledge systems.

## What Is OKF?

The Open Knowledge Format (OKF) uses YAML-frontmatter Markdown files. Each concept file does **two** jobs at once, a dual-action design:

1. **A boundary** — a `not:` field listing the English mistranslations an AI must avoid, each paired with *why* it fails and what to use *instead*.
2. **A scaffold** — positive fields that install the correct understanding: *What It Actually Means*, *Audience Metaphor*, *Etymology*, and *Citations*.

So OKF does not merely tell a model what a term is **not**. It clears out the wrong definition and immediately installs the right one, leaving the model with a complete semantic package rather than a severed, "floating" term.

- "Karma = Fate" → **Wrong.** It is action and consequence. See `okf/dharma-foundation/concepts/karma.md`
- "Dharma = Religion" → **Wrong.** It is the natural sustaining order / right conduct. See `okf/dharma-foundation/concepts/dharma.md`
- "Samadhi = Trance" → **Wrong.** It is absorption / unified awareness. See `okf/dharma-foundation/concepts/samadhi.md`
- "Yoga = Exercise" → **Wrong.** It is the discipline of stilling the mind. See `okf/dharma-foundation/concepts/yoga.md`

## Why this is an engineering problem, not only a cultural one

A mistranslation changes the **category** a model reasons in, which changes its action space and therefore its output. A wellness bot that reads `yoga` as exercise recommends the squat rack; an advisor that reads `karma` as fate gives fatalistic, agency-removing advice. The metaphysical error *is* a logic bug.

See [`demos/failure-vs-success.md`](demos/failure-vs-success.md) for side-by-side failure-mode vs success-mode transcripts.

## Integrate it (machine-readable is not the same as obeyed)

A `not:` list in a file is a "do not enter" sign on an unlocked door. The model still has to be told how to read and honor it, and a naive bare prohibition can *backfire* through negative-prompt leakage. [`INTEGRATION.md`](INTEGRATION.md) shows how to make the constraint functionally binding: a system-prompt template that injects the positive `instead` redirect (not a bare ban), a RAG negative-filter pattern, and a lightweight output-check, with honest caveats about what is and is not guaranteed.

## Bundles — five live, all on canonical OKF v0.2

| Bundle | Release | Concepts | Theme |
|---|---|---|---|
| `okf/dharma-foundation/` | v0.1.1 | 25 | Foundational Sanskrit non-translatable vocabulary |
| `okf/yoga-darshana/` | v0.2.0 | 26 | Patañjali's Yoga Sūtra technical lexicon |
| `okf/vedanta-epistemology/` | v0.3.0 | 27 | Pramāṇa-śāstra — Vedantic epistemology |
| `okf/bhakti-marga/` | v0.4.0 | 15 (+9 refs) | The vocabulary of the devotional path |
| `okf/dharmic-ethics/` | v0.5.0 | 15 (+6 refs) | Yama-Niyama and the ethical-social vocabulary |

## Concept file format (OKF v0.2)

Each concept file contains:

- **YAML frontmatter:** `type`, `title`, `iast`, `devanagari`, `description`, `darshana`, a structured `not:` (each entry `term` / `why` / `instead`), `related:`, `tags`, `okf_version`, `license`
- **## What It Actually Means** (and **## Etymology**) — the precise positive definition
- **## Audience Metaphor** — an accessible analogy engineered for AI and general comprehension
- **## Citations** — primary śāstra references, linked into a `references/` sub-bundle of first-class `type: Reference` concepts

Full specification: [`okf/SPEC.md`](okf/SPEC.md) (Section 12 covers the v0.2 additions: `darshana`, the structured `not:` with `instead`, the bundle-root manifest, and `Citations` / `references/`).

## Content License

The concept files in `/okf/` are licensed under **CC BY-SA 4.0** (ShareAlike). See [LICENSE-CONTENT](./LICENSE-CONTENT) for details.

Repository tooling is under Apache 2.0 (inherited from the upstream GoogleCloudPlatform fork).

## Contributing

This is the standalone publication home for the Dharma OKF Foundation. Contributions, corrections, and additions that deepen accuracy are welcome via Pull Request. See [CONTRIBUTING.md](./CONTRIBUTING.md).
