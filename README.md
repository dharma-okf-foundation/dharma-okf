# Dharma OKF — Open Knowledge Format for Sanskrit Non-Translatables

A structured, machine-readable knowledge base of Sanskrit concepts that

resist accurate translation into English — built for AI agents, educators,

researchers, and technologists working with dharmic knowledge systems.

## What Is OKF?

The Open Knowledge Format (OKF) uses YAML-frontmatter Markdown files with

a critical `not:` field listing English mistranslations AI agents must avoid.

This prevents AI systems from confidently substituting inaccurate equivalents:

- "Karma = Fate" → **Wrong.** See `concepts/karma.md`

- "Dharma = Religion" → **Wrong.** See `concepts/dharma.md`

- "Samadhi = Trance" → **Wrong.** See `concepts/samadhi.md`

- "Yoga = Exercise" → **Wrong.** See `concepts/yoga.md`

## The `not:` Field — Why It Matters

When AI agents encounter Sanskrit terms, they default to common English

translations. These translations are often structurally incorrect — they

carry different metaphysical assumptions, different philosophical contexts,

and different cultural baggage. The `not:` field in each concept file is a

machine-readable instruction: *do not substitute these terms.*

## Bundle: dharma-foundation

25 Sanskrit concept files covering:

- **Vedanta metaphysics:** Brahman, Ātman, Jīva, Māyā, Mokṣa, Saṃsāra

- **Vedic psychology:** Buddhi, Manas, Chitta, Ahankāra, Viveka, Vairāgya

- **Yoga philosophy:** Yoga, Dhyāna, Samādhi, Prāṇa, Karma, Dharma

- **Sound and language:** Śabda, Mantra, Akṣara, Om

- **Cosmology:** Chakra, Loka, Prakṛti

Located at: `okf/dharma-foundation/concepts/`

## File Format

Each concept file contains:

- **YAML frontmatter:** type, title, description, tags, `not:`, `related:`, timestamp, okf_version

- **What It Actually Means** — precise dharmic definition

- **Why the Substitutes Fail** — why common English terms are wrong

- **Audience Metaphor** — accessible analogy for AI or general audiences

- **Key Sources** — primary śāstra references

## Content License

The concept files in `/okf/` are licensed under **CC BY-SA 4.0** (ShareAlike).

See [LICENSE-CONTENT](./LICENSE-CONTENT) for details.

Repository tooling is under Apache 2.0 (inherited from upstream GoogleCloudPlatform fork).

## Contributing

This is a standalone publication home for the Dharma OKF Foundation.

Contributions, corrections, and additions that deepen accuracy are welcome

via Pull Request.
