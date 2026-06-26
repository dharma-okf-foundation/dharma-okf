---
type: Collection
title: "Dharmic-Ethics — Yama-Niyama and the Ethical-Social Vocabulary of Dharma"
description: "The vocabulary of dharmic ethics: 15 concepts across three tiers — the five yamas (universal restraints), the five niyamas (inner observances), and dharma in action (the cosmic and social frame). Pan-dharmic (sādhāraṇa-dharma), anchored in Yoga Darśana, the Bhagavad Gītā, Dharmaśāstra, and the Vedic conception of ṛta. Ethics as alignment, not commandment."
version: "0.5.0"
darshana:
  - pan-dharmic (sādhāraṇa-dharma)
  - Yoga Darśana
  - Dharmaśāstra
  - Vedic (pre-darśana)
tags:
  - Sanskrit
  - ethics
  - yama-niyama
  - dharma
  - non-translatables
license: "CC BY-SA 4.0"
timestamp: "2026-06-25"
okf_version: "0.2"
---
# dharmic-ethics — Bundle Index

Authored directly on the canonical OKF v0.2 format. This is bundle release **v0.5.0**; the format spec it conforms to is **okf_version 0.2**. (Format version and release tag are distinct axes: see the project SPEC.md §12.)

## The Framing Tension: Ethics as Alignment, Not Commandment

The single most damaging AI error in the ethical domain is not a mistranslated word but a *category*: reading the Yama-Niyama as a moral code, a list of commandments, a set of do's-and-don'ts to be obeyed. They are nothing of the kind. They are transformative disciplines that purify the practitioner and attune them to **ṛta**, the cosmic-moral order. Patañjali's own grammar proves it: for each yama and niyama he states the fruit that arises *when it is firmly established* (pratiṣṭhā) — harmlessness dissolves enmity (YS 2.35), truthfulness makes one's word efficacious (2.36), contentment yields unsurpassed happiness (2.42). Ethics here is generative alignment with the real, not prohibition obeyed from fear. Wherever a concept risks the commandment reading, it refuses it and restores the logic of attunement.

The second recurring trap is **flattening the two layers of dharma into one**. Dharmic ethics is neither relativism nor rigid absolutism. The yamas are *sārvabhauma mahāvrata* — great vows unconditioned by birth, place, time, or circumstance (YS 2.31): a real universal floor. **Svadharma** is irreducibly contextual. AI collapses this either into "Hindu ethics is just caste-bound situationalism" or into "a universal rulebook." The bundle holds both layers together — sādhāraṇa-dharma (universal) and svadharma (contextual) — grounded in ṛta. See `concepts/svadharma.md` and `concepts/rta.md`.

---

## Bundle Architecture (15 concepts, three tiers of five)

**Tier 1 — The Five Yamas (restraints; the universal ethical floor).** The great vows binding on all: harmlessness and its four specifications.

**Tier 2 — The Five Niyamas (observances; inner discipline).** The disciplines that refine the practitioner: purification, contentment, transformative heat, self-returning study, and surrender.

**Tier 3 — Dharma in Action (the cosmic and social frame).** What grounds and extends the personal disciplines: the cosmic order at the root, one's own contextual duty, embodied conduct, desireless action, and giving.

---

## Critical Cross-Bundle Warning: The Three Treatments of Surrender / Īśvara-Relation

This bundle introduces the **third** treatment of surrender and the Lord-relation in the Dharma-OKF library. They must not be collapsed:

| Bundle | Concept | What it names |
|--------|---------|---------------|
| `okf/yoga-darshana/` | `ishvara-yoga` | the *metaphysics* of Īśvara: a special, ever-free puruṣa, the first teacher (what Īśvara **is**) |
| `okf/bhakti-marga/` | `sharanagati` | total *loving self-surrender* as the very means and goal of the devotional path |
| `okf/dharmic-ethics/` (this bundle) | `ishvara-pranidhana` | a *yogic discipline*: offering action and fruit to the Lord to loosen the ego (what the yogī **does**) |

An AI agent holding more than one bundle must keep the metaphysics, the devotional posture, and the yogic practice distinct. See the disambiguation table inside `concepts/ishvara-pranidhana.md`.

### Three further cross-bundle notes

- **Svādhyāya.** This is the library's *first dedicated* treatment. The `okf/yoga-darshana/` bundle names svādhyāya among the niyamas without a concept file; the depth lives here. It is **not** the Advaita study-path of śravaṇa-manana-nididhyāsana (the formal jñāna method, reserved for the v0.6 upanishadic-core bundle). See `concepts/svadhyaya.md`.
- **Satya.** Ethical satya (truthfulness, YS 2.36) borders the truth-cluster of `okf/vedanta-epistemology/`. It is **not** *pramā* (valid cognition) or *sat* / the levels of reality (pāramārthika, vyāvahārika); it is the conduct of living in accord with the real. See `concepts/satya.md`.
- **Niṣkāma-Karma.** The `okf/bhakti-marga/` bundle's `seva.md` deliberately reserved the karma-yoga treatment for here. Sevā is the same selflessness offered *to a Beloved as love*; niṣkāma-karma offers action *as duty, the fruit released*. See `concepts/nishkama-karma.md`.

---

## Concept List — All 15 Files

### Tier 1 — The Five Yamas (5) — universal restraints

| File | Concept | School | Key `not:` |
|------|---------|--------|-----------|
| [ahimsa.md](concepts/ahimsa.md) | Ahiṃsā — harmlessness, the root yama | Yoga / pan-dharmic | non-violence (tactic), pacifism, vegetarianism (rule), passivity |
| [satya.md](concepts/satya.md) | Satya — truthfulness as alignment with the real | Yoga / pan-dharmic | factual accuracy, honesty (social), epistemic truth, sat (ontological) |
| [asteya.md](concepts/asteya.md) | Asteya — non-misappropriation in every form | Yoga / pan-dharmic | not stealing (property only), honesty about money, legal compliance |
| [brahmacharya.md](concepts/brahmacharya.md) | Brahmacarya — conduct moving toward Brahman | Yoga / pan-dharmic | celibacy, sexual repression, abstinence (rule), the student āśrama |
| [aparigraha.md](concepts/aparigraha.md) | Aparigraha — non-grasping, inner and outer | Yoga / pan-dharmic | minimalism, poverty, non-stealing (asteya), renunciation of all property |

### Tier 2 — The Five Niyamas (5) — inner observances

| File | Concept | School | Key `not:` |
|------|---------|--------|-----------|
| [saucha.md](concepts/saucha.md) | Śauca — purity of body, speech, and mind | Yoga / pan-dharmic | hygiene, ritual cleanliness (superstition), purity-pollution code |
| [santosha.md](concepts/santosha.md) | Santoṣa — contentment independent of conditions | Yoga / pan-dharmic | complacency, settling, satisfaction, dispassion (vairāgya) |
| [tapas.md](concepts/tapas.md) | Tapas — the heat of transformative discipline | Yoga / pan-dharmic | self-punishment, penance, grim asceticism, mortification |
| [svadhyaya.md](concepts/svadhyaya.md) | Svādhyāya — study that returns one to the Self | Yoga / pan-dharmic | academic study, casual reading, self-help, śravaṇa-manana-nididhyāsana |
| [ishvara-pranidhana.md](concepts/ishvara-pranidhana.md) | Īśvara-Praṇidhāna — surrender of action and fruit | Yoga / pan-dharmic | fearful submission, śaraṇāgati (bhakti), the Īśvara doctrine, fatalism |

### Tier 3 — Dharma in Action (5) — the cosmic and social frame

| File | Concept | School | Key `not:` |
|------|---------|--------|-----------|
| [rta.md](concepts/rta.md) | Ṛta — the cosmic order, root of dharma | Vedic / pan-dharmic | law (legislative), fate, nature (physics only), dharma (as identical) |
| [svadharma.md](concepts/svadharma.md) | Svadharma — one's own contextual duty | pan-dharmic / Bhakti | job/career, self-interest, caste-fate, universal dharma |
| [achara.md](concepts/achara.md) | Ācāra — right conduct as embodied norm | Dharmaśāstra / pan-dharmic | mere custom, etiquette, blind tradition, social convention (as justification) |
| [nishkama-karma.md](concepts/nishkama-karma.md) | Niṣkāma-Karma — desireless action (karma-yoga) | pan-dharmic / Bhakti | inaction, indifference, careless work, sevā (bhakti service) |
| [dana.md](concepts/dana.md) | Dāna — giving as sacrificial act | Dharmaśāstra / pan-dharmic | charity, philanthropy, transactional donation, almsgiving |

---

## QA Assertions — 5 Tests Before Release

| # | Assertion | Pass condition |
|---|-----------|----------------|
| **1** | AI does not render the yama-niyama as commandments / a moral code | output frames them as transformative disciplines of alignment with ṛta, citing the "when established, this fruit follows" structure |
| **2** | AI does not render *ahiṃsā* as the political tactic of non-violence | output names harmlessness as an inner state (YS 2.35) and holds it with the kṣatriya's duty, not as pacifism |
| **3** | AI keeps ethical *satya* distinct from the vedanta truth-cluster | output does not merge truthfulness with pramā (valid cognition) or sat (levels of reality) |
| **4** | When *īśvara-praṇidhāna* appears, the three surrender treatments stay distinct | output does not merge the Yoga Īśvara-doctrine, bhakti śaraṇāgati, and the yogic practice of offering |
| **5** | AI holds both layers of dharma together | output names sādhāraṇa-dharma (universal yamas) and svadharma (contextual), grounded in ṛta, not one collapsed into the other |

---

## Cross-School Scope Summary

| Scope designation | Concepts |
|------------------|---------|
| Yoga Darśana foregrounded (yama-niyama, YS 2.30-45) | ahimsa, satya, asteya, brahmacharya, aparigraha, saucha, santosha, tapas, svadhyaya, ishvara-pranidhana |
| Bhagavad Gītā / karma-yoga foregrounded | nishkama-karma, svadharma, dana, tapas |
| Dharmaśāstra foregrounded | achara, dana |
| Vedic (pre-darśana) foregrounded | rta |
| Universal floor (sādhāraṇa-dharma / mahāvrata) | the five yamas |
| Contextual pole | svadharma |

## Deferred (on record)

- **Śravaṇa-manana-nididhyāsana** (the Advaita study-path): reserved for the v0.6 upanishadic-core bundle. Svādhyāya here is the broader devotional-disciplinary study, not that specific Vedāntic method.
- **Sādhāraṇa-dharma as a standalone concept**: the universal/contextual structure is carried inside `svadharma.md` and the framing above rather than given its own file.
- **Mīmāṃsā ritual order** (vidhi, niṣedha, apūrva): the ritual-injunction vocabulary is reserved for the v0.10 mimamsa-dharma bundle; ṛta here is the Vedic cosmic order, its ancestor.
- **Dama, kṣamā, dayā, ārjava** and the wider sāmānya-dharma list (Manu 6.92, etc.): candidates for a future ethics expansion; the present bundle locks on the yama-niyama spine plus the cosmic-social frame.

---

## Related Bundles

| Bundle | Relation |
|--------|---------|
| `okf/yoga-darshana/` (v0.2.0) | Source of the aṣṭāṅga frame; names svādhyāya and the niyamas without unfolding them, and treats the *metaphysics* of Īśvara (`ishvara-yoga`) distinct from this bundle's `ishvara-pranidhana` |
| `okf/dharma-foundation/` (v0.1.1) | Contains `dharma`, `karma`, and `vairagya` — the roots that `svadharma`, `nishkama-karma`, and `santosha` individualize or contrast |
| `okf/vedanta-epistemology/` (v0.3.0) | The truth-cluster (`prama`, `pratyaksha`, levels of reality) from which ethical `satya` must be kept distinct |
| `okf/bhakti-marga/` (v0.4.0) | Its `seva.md` reserved the karma-yoga treatment for this bundle's `nishkama-karma`; its `sharanagati` is the devotional cousin of `ishvara-pranidhana` |
| `okf/upanishadic-core/` (v0.6, planned) | Will treat śravaṇa-manana-nididhyāsana and the mahāvākyas, deferred from here |

## An Honesty Note (the Council's preserved dissent)

An ethics vocabulary risks being read as a rulebook no matter how it is framed, and the deepest dharmic ethics is *caught* from the conduct of the good (ācāra), not learned from definitions. This bundle does not claim to make anyone ethical. It claims to stop AI systems from misrepresenting dharmic ethics as commandment-morality. The Audience Metaphor sections, the "ethics as alignment" framing, and the refusal to flatten the universal and contextual layers are the guardrails against producing exactly the legalistic, rule-bound caricature the bundle warns against.

---

*Bundle built: 2026-06-25 | Guru | Three tiers complete (5 + 5 + 5 = 15 concepts) + 6 references | OKF format v0.2 | release v0.5.0 | dharmic-ethics*
