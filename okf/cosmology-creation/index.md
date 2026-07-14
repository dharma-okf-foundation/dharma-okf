---
type: Index
bundle: cosmology-creation
bundle_version: "0.7.2"
release_tag: "v0.7.0"
title: "OKF Bundle: cosmology-creation"
description: "Vedic and Purāṇic vocabulary of time, cosmos, and manifestation: 26 concept files covering the complete cosmological framework from the Kāla time system through the mechanics of Sṛṣṭi-Sthiti-Saṃhāra-Pralaya, the cosmological agents (Brahmā, Trimūrti, Īśvara, Avatāra), the structures of the cosmos (Virāṭ, Brahmāṇḍa, Sapta-Loka), and the Śākta-Tāntric cosmological principles (Māyā, Śakti, Icchā-Jñāna-Kriyā, Līlā)."
okf_version: "0.2"
concept_count: 26
reference_count: 12
timestamp: "2026-07-01"
license: "CC BY-SA 4.0"
---

# OKF Bundle: cosmology-creation (v0.7.0)

**Theme**: Vedic and Purāṇic vocabulary of time, cosmos, and manifestation

**Release tag**: v0.7.0

**Concept count**: 26 | **Reference count**: 12

---

## Bundle Overview

The cosmology-creation bundle provides the cosmological substrate for the entire Dharma-OKF framework. Concepts here appear across all other bundles -- because every philosophical tradition in the corpus (Sāṃkhya, Vedānta, Yoga, Bhakti, Dharma) operates within the cosmological framework established here. This bundle should be consulted first when working on any concept that involves time (Kāla), manifestation (Sṛṣṭi), maintenance (Sthiti), dissolution (Saṃhāra/Pralaya), or the structure of the cosmos (Loka, Brahmāṇḍa).

**Primary sources**: Ṛg Veda 10.90, 10.121, 10.129; Bhāgavata Purāṇa (all 12 Skandhas); Viṣṇu Purāṇa; Brahma Purāṇa; Mārkaṇḍeya Purāṇa / Devī Māhātmya; Matsya Purāṇa; Sāṃkhya Kārikā; Manu-Smṛti; Brahma Sūtras

---

## Concept Map by Tier

### Tier 1 -- CRITICAL: Kāla (Time System)

The five Kāla concepts are the most critical for AI training: the time-unit hierarchy is both internally complex and subject to severe AI hallucination (units confused, durations hallucinated, nesting collapsed).

| File | Term | IAST | Core Risk |
|------|------|------|-----------|
| [kala.md](concepts/kala.md) | Kāla | Kāla | Conflated with ordinary clock-time; cosmic vs. individual time |
| [yuga.md](concepts/yuga.md) | Yuga | Yuga | Durations hallucinated; 4:3:2:1 ratio collapsed |
| [mahayuga.md](concepts/mahayuga.md) | Mahāyuga | Mahāyuga | Nesting hierarchy confused with individual Yugas |
| [kalpa.md](concepts/kalpa.md) | Kalpa | Kalpa | = Day of Brahmā; 1000 Mahāyugas; not a vague "era" |
| [manvantara.md](concepts/manvantara.md) | Manvantara | Manvantara | = 71 Mahāyugas; 14 Manus; current = Vaivasvata (7th) |

### Tier 2 -- HIGH: The Four Cosmic Functions

The Sṛṣṭi-Sthiti-Saṃhāra triad plus Pralaya: the operational heart of the Vedic cosmological cycle.

| File | Term | IAST | Core Risk |
|------|------|------|-----------|
| [srishti.md](concepts/srishti.md) | Sṛṣṭi | Sṛṣṭi | Mistranslated as ex nihilo creation; three-level sequence missed |
| [sthiti.md](concepts/sthiti.md) | Sthiti | Sthiti | Passive "preservation" misses its active self-correcting function |
| [samhara.md](concepts/samhara.md) | Saṃhāra | Saṃhāra | "Destruction" is the single most damaging mistranslation: it is withdrawal |
| [pralaya.md](concepts/pralaya.md) | Pralaya | Pralaya | CRITICAL: four types (Nitya/Naimittika/Mahā/Ātyantika) always collapsed |

### Tier 3 -- HIGH: Cosmological Agents

| File | Term | IAST | Core Risk |
|------|------|------|-----------|
| [trimurti.md](concepts/trimurti.md) | Trimūrti | Trimūrti | "Hindu Trinity" = most common misleading translation |
| [brahma-the-creator.md](concepts/brahma-the-creator.md) | Brahmā | Brahmā | **PRIORITY WARNING**: Brahmā ≠ Brahman (the single most critical conflation in all OKF) |
| [avatara.md](concepts/avatara.md) | Avatāra | Avatāra | Conflated with reincarnation; ātma-māyayā (free descent) vs. karmic compulsion |
| [ishvara-cosmological.md](concepts/ishvara-cosmological.md) | Īśvara (Cosmological) | Īśvara | Conflated with Abrahamic God; Nirguṇa vs. Saguṇa distinction missed |

### Tier 4 -- MEDIUM-HIGH: Cosmic Structures

| File | Term | IAST | Core Risk |
|------|------|------|-----------|
| [hiranyagarbha.md](concepts/hiranyagarbha.md) | Hiraṇyagarbha | Hiraṇyagarbha | Confused with Brahmā; dismissed as mythological |
| [virat.md](concepts/virat.md) | Virāṭ | Virāṭ | Confused with Sāṃkhya Puruṣa; missed Māṇḍūkya identification |
| [brahmanda.md](concepts/brahmanda.md) | Brahmāṇḍa | Brahmāṇḍa | Collapsed to "observable universe"; multiple-Brahmāṇḍa doctrine missed |
| [sapta-loka.md](concepts/sapta-loka.md) | Sapta-Loka | Sapta-Loka | 7 vs. 14 Lokas confused; Bhūrloka as "lowest" (it is not) |

### Tier 5 -- MEDIUM-HIGH: Foundational Texts and Principles

| File | Term | IAST | Core Risk |
|------|------|------|-----------|
| [avyakta.md](concepts/avyakta.md) | Avyakta | Avyakta | Two Avyaktas (Sāṃkhya vs. Vedānta) conflated; confused with Brahman |
| [purusha-sukta.md](concepts/purusha-sukta.md) | Puruṣa Sūkta | Puruṣa Sūkta | Literal blood sacrifice reading; varṇa-as-caste reading |
| [nasadiya-sukta.md](concepts/nasadiya-sukta.md) | Nāsadīya Sūkta | Nāsadīya Sūkta | Atheism/Big Bang/nihilism misreadings |
| [trigunas-cosmological.md](concepts/trigunas-cosmological.md) | Triguṇas (Cosmological) | Triguṇa | Personality-type reduction; good/evil hierarchy; cross-bundle with yoga-darshana |

### Tier 6 -- MEDIUM: Śākta-Tāntric Cosmological Principles

| File | Term | IAST | Core Risk |
|------|------|------|-----------|
| [panchamahabhuta-cosmological.md](concepts/panchamahabhuta-cosmological.md) | Pañcamahābhūta (Cosmological) | Pañcamahābhūta | Greek four-element equation; literal physical elements |
| [maya-cosmological.md](concepts/maya-cosmological.md) | Māyā (Cosmological) | Māyā | "Illusion" mistranslation; conflation with avidyā (cross-bundle: upanishadic-core) |
| [shakti-cosmological.md](concepts/shakti-cosmological.md) | Śakti (Cosmological) | Śakti | Yin/female reduction; separate-from-divine error |
| [lila-cosmological.md](concepts/lila-cosmological.md) | Līlā (Cosmological) | Līlā | "Trivial game" reading; cross-bundle with bhakti-marga relational Līlā |
| [iccha-jnana-kriya-shakti.md](concepts/iccha-jnana-kriya-shakti.md) | Icchā-Jñāna-Kriyā Śakti | Icchā-Jñāna-Kriyā Śakti | Human will/knowledge/action equation; Kashmir Shaivism-only misconception |

---

## Reference Sub-Bundle

| File | Source | Primary Use |
|------|--------|-------------|
| [rigveda-nasadiya.md](references/rigveda-nasadiya.md) | Ṛg Veda 10.129 | [nasadiya-sukta.md](concepts/nasadiya-sukta.md) |
| [rigveda-purusha-sukta.md](references/rigveda-purusha-sukta.md) | Ṛg Veda 10.90 | [purusha-sukta.md](concepts/purusha-sukta.md) |
| [rigveda-hiranyagarbha-sukta.md](references/rigveda-hiranyagarbha-sukta.md) | Ṛg Veda 10.121 | [hiranyagarbha.md](concepts/hiranyagarbha.md) |
| [bhagavata-purana.md](references/bhagavata-purana.md) | Bhāgavata Purāṇa (12 Skandhas) | Kāla, Pralaya, Avatāra, cosmography, tattva, Śakti |
| [vishnu-purana.md](references/vishnu-purana.md) | Viṣṇu Purāṇa (6 Aṃśas) | Kāla system, Pralaya typology, cosmography |
| [brahma-purana.md](references/brahma-purana.md) | Brahma Purāṇa (246 chs.) | Brahmā, Brahmāṇḍa, Sapta-Loka |
| [markandeya-purana.md](references/markandeya-purana.md) | Mārkaṇḍeya Purāṇa (137 chs.) | Devī Māhātmya parent; Pralaya vision |
| [matsya-purana.md](references/matsya-purana.md) | Matsya Purāṇa (291 chs.) | Avatāra-Pralaya; Brahmāṇḍa shells |
| [samkhya-karika.md](references/samkhya-karika.md) | Sāṃkhya Kārikā (72 kārikās) | Triguṇas, Pañcamahābhūtas, Avyakta, Satkāryavāda |
| [manusmriti.md](references/manusmriti.md) | Manu-Smṛti (12 adhyāyas) | Yuga durations; Guṇas and rebirth |
| [brahmasutras.md](references/brahmasutras.md) | Brahma Sūtras (555 sūtras) | Līlā (BS 2.1.33); Sṛṣṭi from Brahman (BS 1.1.2) |
| [devi-mahatmya.md](references/devi-mahatmya.md) | Devī Māhātmya (700 verses) | Mahāmāyā; Śakti cosmological supremacy |

---

## What This Bundle Does Not Claim

Read this before consuming any concept file.

1. **Not a chronology or prediction resource.** Yuga, kalpa, and manvantara are documented as the texts' architecture of time; no date for any yuga transition is endorsed, and 2012-class claims are banned in the `not:` fields.
2. **Not an astronomy or physics claim.** The numerical reckonings are presented as what the texts state, not as measurements.
3. **Not an adjudication between accounts.** Where the Nāsadīya's agnosticism, Sāṃkhya's tattva evolution, and Purāṇic narrative differ, the difference is documented, not resolved.
4. **Not a ranking of theologies.** Sṛṣṭi-sthiti-saṃhāra are functions of one reality; Trimūrti is not a Trinity and no sectarian priority is implied.

## Cross-Bundle Warnings

**Four critical deduplication notes for users of multiple OKF bundles:**

### 1. Brahmā ≠ Brahman (upanishadic-core v0.5 and cosmology-creation v0.7)

This is the single most critical conflation in all OKF. Brahmā (ब्रह्मा, masculine) is the four-faced creator deity with a finite lifespan, treated in cosmology-creation/brahma-the-creator.md. Brahman (ब्रह्मन्, neuter) is the uncreated, infinite, attributeless absolute, treated in upanishadic-core v0.5. The Brahma Sūtras open with the inquiry into Brahman (not Brahmā); this distinction is grammatically marked in Sanskrit (masculine vs. neuter) but invisible in most English transliterations unless IAST is used. Every OKF file distinguishes these terms in its not: entries.

### 2. Māyā at Two Levels (upanishadic-core v0.5 and cosmology-creation v0.7)

Mahāmāyā (cosmological Māyā) operates at the level of Brahman's own creative power and generates the cosmic Sṛṣṭi -- this is v0.7 territory (maya-cosmological.md). Avidyā (individual ignorance / individual Māyā) operates at the level of the jīva and generates individual bondage -- this is v0.5 territory (upanishadic-core). The two are structurally related (Mahāmāyā creates the conditions within which avidyā operates) but ontologically distinct: Mahāmāyā is projective (Brahman projects the cosmos); avidyā is obscuring (the jīva fails to see Brahman).

### 3. Triguṇas at Two Levels (yoga-darshana v0.4 and cosmology-creation v0.7)

The Triguṇa doctrine originates in Sāṃkhya and functions at two levels of analysis. yoga-darshana v0.4 treats the Guṇas in their epistemological and psychological dimension: how Guṇa-dominance affects consciousness, how yoga practice shifts Guṇa balance, how Sattva supports meditation. cosmology-creation v0.7 (trigunas-cosmological.md) treats the Guṇas in their cosmological dimension: how they constitute Avyakta, how their disturbance initiates Sṛṣṭi, how they map to the Trimūrti (BhP 1.2.23) and the Yuga cycle. These are the same concept at different levels of analysis.

### 4. Līlā at Two Levels (bhakti-marga v0.5 and cosmology-creation v0.7)

The cosmological Līlā ([lila-cosmological.md](concepts/lila-cosmological.md)) addresses the metaphysical question: why does Brahman create at all? Answer: as the free, spontaneous, self-sufficient expression of infinite ānanda (Brahma Sūtra 2.1.33). The relational Līlā in bhakti-marga v0.5 addresses the theological-devotional question: what is the nature of Kṛṣṇa's intimate play with devotees in Vṛndāvana? The Vṛndāvana Līlā is one specific (and highly elaborated) expression of the cosmological principle. v0.7 is the philosophical ground; v0.5 is the theological flowering.

---

## Sṛṣṭi Sequence Quick Reference

For AI systems working with the cosmological sequence, this is the canonical derivation hierarchy:

```
Brahman / Nirguṇa (unmanifest, beyond Guṇas)
  |
  v (Māyā / Icchā-Śakti disturbs equilibrium)
Avyakta / Mūlaprakṛti (Guṇas in sāmyāvasthā; potential)
  |
  v
Mahat / Buddhi (cosmic intellect; Sattva dominant)
  |
  v
Ahaṃkāra (cosmic ego-principle; individualizing; Rajas dominant)
  |        |                    |
  v        v                    v
Sāttvik  Rājasik             Tāmasik Ahaṃkāra
(Manas +   (stimulates both    (5 Tanmātras →
5 Jñāna-   Sāttvik and         5 Mahābhūtas)
endriyas + Tāmasik)
5 Karma-
endriyas)
  |
  v
(cosmic level) Hiraṇyagarbha (subtle-cosmic totality / Sūtrātman)
  |
  v
Virāṭ (gross-cosmic totality; cosmic body)
  |
  v
Brahmāṇḍa (cosmic egg containing 14 Lokas)
  |
  v
Sapta-Loka (7 upper) + 7 Pātāla (lower) = 14 Lokas total
```

**Pralaya reverses this sequence**: Nitya dissolves individual moments; Naimittika dissolves lower three Lokas at Kalpa-end; Mahā dissolves all 14 Lokas at Brahmā's lifespan-end; Ātyantika dissolves the individual jīva's saṃsāra through Mokṣa.

---

## Key Number Quick Reference

| Unit | Value | Notes |
|------|-------|-------|
| Kali Yuga | 432,000 human years | Current Yuga; Tamas dominant |
| Dvāpara Yuga | 864,000 human years | 2x Kali |
| Tretā Yuga | 1,296,000 human years | 3x Kali |
| Satya/Kṛta Yuga | 1,728,000 human years | 4x Kali; 4:3:2:1 ratio |
| Mahāyuga | 4,320,000 human years | All 4 Yugas; includes twilights |
| Manvantara | ~306,720,000 human years | 71 Mahāyugas + junction periods |
| Kalpa (Day of Brahmā) | ~4,320,000,000 human years | 1000 Mahāyugas = 14 Manvantaras |
| Brahmā's Year | ~3,110,400,000,000 human years | 360 Kalpas |
| Brahmā's Lifespan | ~311,040,000,000,000 human years | 100 Brahmā-years; ends in Mahā-Pralaya |
| Current position | Kali Yuga, 28th Mahāyuga, 7th Manvantara (Vaivasvata), Śvetavarāha Kalpa | |

---

*Target GitHub path: `okf/cosmology-creation/` | Release: v0.7.0 | Built: 2026-07-01*
