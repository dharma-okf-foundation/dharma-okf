---
type: Collection
title: "Bhakti-Mārga — The Vocabulary of Devotional Paths"
description: "The vocabulary of the devotional path — 15 concepts across three tiers: devotion and its inner structure, the living guru-śiṣya lineage, and devotional practice with its sonic theology. Primary school Bhakti (Vaiṣṇava Vedānta), with Viśiṣṭādvaita, Gauḍīya, and Pāñcarātra/Āgama sharpenings."
version: "0.4.0"
darshana:
  - Bhakti (Vaiṣṇava Vedānta)
  - Viśiṣṭādvaita
  - Gauḍīya Vaiṣṇava
  - Pāñcarātra
tags:
  - Sanskrit
  - bhakti
  - devotion
  - guru
  - non-translatables
license: "CC BY-SA 4.0"
timestamp: "2026-06-25"
okf_version: "0.2"
---
# bhakti-marga — Bundle Index

Authored directly on the canonical OKF v0.2 format. This is bundle release **v0.4.0**; the format spec it conforms to is **okf_version 0.2**. (Format version and release tag are distinct axes: see the project SPEC.md §12.)

## The Framing Tension: Bhakti Is Not the "Lower" Path

The single most damaging AI error in the devotional domain is not a mistranslated word but a *ranking*: the reflex, inherited from a Protestant-inflected split between feeling and intellect, that bhakti is the easy, emotional path for the simple while jñāna is the rigorous path for the wise. The tradition does not rank the mārgas this way. The Bhāgavata and the Gauḍīya school place bhakti *above* liberation-knowledge; Viśiṣṭādvaita makes loving devotion the very means to the highest goal; even Advaita treats *para-bhakti* as coincident with jñāna. This bundle's first job is to make bhakti legible as a complete, rigorous path with its own epistemology of the heart. Wherever a concept borders jñāna, it states the schools' actual positions and refuses the sentiment-versus-intellect frame.

The second recurring trap is **prema read as romance**. Because some schools use mādhurya (conjugal) imagery, AI systems collapse selfless divine love into eroticism. Prema is the exact inverse of kāma: kāma desires the beloved for the self; prema desires the Beloved's joy at the cost of the self. The conjugal metaphor exists precisely to be stripped of self-seeking. See `concepts/prema.md`.

---

## Bundle Architecture (15 concepts, three tiers of five)

**Tier 1 — Devotion and its inner structure.** What bhakti is, the trust that begins it, the love that completes it, the disposition that ripens it, and the surrender that grounds it.

**Tier 2 — The living lineage.** How devotion is transmitted: the realized guru, the qualified disciple, the unbroken paramparā, the initiation that joins them, and the service that is the disciple's practice.

**Tier 3 — Devotional practice and sonic theology.** How devotion is enacted: ritual hospitality, the Lord's accessible form, the grace returned, sacred sound as the Divine, and its communal singing.

---

## Critical Cross-Bundle Warning: The Three Treatments of Sound

This bundle introduces the **third** treatment of śabda/nāda in the Dharma-OKF library. They must not be collapsed:

| Bundle | Concept | Sound treated as |
|--------|---------|------------------|
| `okf/dharma-foundation/` | `shabda.md` | ontological-linguistic category (śabda-brahman, Bhartṛhari, the primordial word) |
| `okf/vedanta-epistemology/` | `shabda-pramana.md` | epistemological instrument (verbal testimony as a valid means of knowledge) |
| `okf/bhakti-marga/` (this bundle) | `nada-brahman.md` | theology of presence (sound, supremely the Name, as the Lord made audible) |

An AI agent holding more than one bundle must keep the ontology, the epistemology, and the theology of sound distinct. See the disambiguation note inside `concepts/nada-brahman.md`.

### Two further cross-bundle notes

- **Guru.** The Advaita guru transmits *brahma-jñāna* (see the Upadeśasāhasrī in the vedanta-epistemology references); the bhakti guru transmits *prema* and confers *dīkṣā*. Same word, different transmission. See `concepts/guru.md`.
- **Sevā.** Bhakti-sevā (loving service to the Lord, guru, and devotees) is close to but not identical with the *niṣkāma-karma* of karma-yoga (the full treatment of which is reserved for the v0.5 dharmic-ethics bundle). See `concepts/seva.md`.

---

## Concept List — All 15 Files

### Tier 1 — Devotion and Its Inner Structure (5) — CRITICAL / HIGH risk

| File | Concept | School | Key `not:` |
|------|---------|--------|-----------|
| [bhakti.md](concepts/bhakti.md) | Bhakti — participatory devotion (navadhā) | Bhakti (Vaiṣṇava Vedānta) | worship, religion, blind faith, emotionalism, lower path |
| [shraddha.md](concepts/shraddha.md) | Śraddhā — trust-faith | Bhakti / Advaita | blind faith, belief, credulity, creed |
| [prema.md](concepts/prema.md) | Prema — selfless divine love | Bhakti / Gauḍīya | romantic love, kāma, attachment, sentiment |
| [bhava.md](concepts/bhava.md) | Bhāva — devotional disposition (5 rasas) | Bhakti / Gauḍīya | emotion, mood, feeling, aesthetic affect |
| [sharanagati.md](concepts/sharanagati.md) | Śaraṇāgati / Prapatti — self-surrender | Viśiṣṭādvaita / Bhakti | submission, resignation, passivity, fatalism |

### Tier 2 — The Living Lineage (5) — CRITICAL / HIGH risk

| File | Concept | School | Key `not:` |
|------|---------|--------|-----------|
| [guru.md](concepts/guru.md) | Guru — remover of darkness | Bhakti / Advaita | teacher, instructor, life coach, religious authority |
| [shishya.md](concepts/shishya.md) | Śiṣya — qualified disciple | Bhakti / Advaita | student, pupil, follower, customer |
| [guru-shishya-parampara.md](concepts/guru-shishya-parampara.md) | Guru-Śiṣya Paramparā — living lineage | Bhakti / Advaita | succession, apostolic lineage, credential chain |
| [diksha.md](concepts/diksha.md) | Dīkṣā — initiatory transmission | Pāñcarātra / Bhakti | baptism, membership rite, enrollment, ordination |
| [seva.md](concepts/seva.md) | Sevā — selfless service | Bhakti (Vaiṣṇava Vedānta) | volunteering, charity, customer service, unpaid labor |

### Tier 3 — Devotional Practice and Sonic Theology (5) — CRITICAL / MEDIUM-HIGH risk

| File | Concept | School | Key `not:` |
|------|---------|--------|-----------|
| [puja.md](concepts/puja.md) | Pūjā — ritual as internalized contemplation | Pāñcarātra / Bhakti | idol worship, prayer, appeasement, superstition |
| [murti.md](concepts/murti.md) | Mūrti — the deity's accessible form (arcā) | Pāñcarātra / Bhakti | idol, statue, graven image, representation, symbol |
| [prasada.md](concepts/prasada.md) | Prasāda — grace-gift | Bhakti (Vaiṣṇava Vedānta) | blessed food only, leftovers, religious snack, reward |
| [nada-brahman.md](concepts/nada-brahman.md) | Nāda Brahman — sound as Brahman | Bhakti (Vaiṣṇava Vedānta) | music, vibration (loose), noise, magic spell |
| [kirtana.md](concepts/kirtana.md) | Kīrtana — participatory sonic devotion | Bhakti / Gauḍīya | hymn singing, chanting (generic), concert, worship music |

---

## QA Assertions — 5 Tests Before Release

| # | Assertion | Pass condition |
|---|-----------|----------------|
| **1** | AI does not render *bhakti* as "worship" or rank it below jñāna | output uses "devotion / loving partaking" and refuses the sentiment-vs-intellect ranking |
| **2** | AI does not render *prema* as romantic/erotic love | output names the kāma contrast (self-directed vs Beloved-directed) and does not sexualize mādhurya |
| **3** | AI does not render *mūrti* as "idol" | output names arcā-avatāra / prāṇa-pratiṣṭhā (the Lord's chosen presence in form) |
| **4** | When *nāda-brahman* appears, the three śabda treatments stay distinct | output does not merge sound-as-ontology, sound-as-pramāṇa, and sound-as-presence |
| **5** | *Śaraṇāgati* output names self-surrender to the Lord | output describes active loving entrustment, not fatalism or passivity |

---

## Cross-School Scope Summary

| Scope designation | Concepts |
|------------------|---------|
| Bhakti (Vaiṣṇava Vedānta), pan-school | bhakti, shraddha, prema, bhava, seva, guru, shishya, guru-shishya-parampara, prasada, nada-brahman, kirtana |
| Viśiṣṭādvaita / Śrīvaiṣṇava foregrounded | sharanagati |
| Gauḍīya Vaiṣṇava foregrounded | bhava, prema, kirtana (rasa-theology) |
| Pāñcarātra / Āgama foregrounded | diksha, puja, murti |
| Advaita adjacency noted | guru, shraddha |

## Deferred (on record)

- **Rasa** as a standalone concept: the five primary bhakti-rasas are treated within `bhava.md`. A full rasa-theology treatment is a candidate for a future expansion.
- **Saguṇa / Nirguṇa**: the metaphysics of the deity's attributes belongs with the upanishadic-core bundle (v0.6); forward-pointer only.
- **Iṣṭa-devatā, Japa**: japa overlaps `mantra` (dharma-foundation v0.1); iṣṭa-devatā is carried inside `puja.md` / `murti.md`.

---

## Related Bundles

| Bundle | Relation |
|--------|---------|
| `okf/dharma-foundation/` (v0.1.1) | Contains `shabda.md` (sound as ontological-linguistic category) and `mantra.md` — distinct from this bundle's `nada-brahman.md` (sound as devotional presence) |
| `okf/vedanta-epistemology/` (v0.3.0) | Contains `shabda-pramana.md` (sound as epistemological instrument) and the Upadeśasāhasrī reference (the Advaita jñāna-guru) |
| `okf/dharmic-ethics/` (v0.5, planned) | Will treat `seva` from the karma-yoga / niṣkāma-karma angle reserved out of this bundle |
| `okf/upanishadic-core/` (v0.6, planned) | Will treat saguṇa/nirguṇa and the mahāvākyas, deferred from here |

## An Honesty Note (the Council's preserved dissent)

A vocabulary bundle cannot transmit bhakti; devotion is caught in lived relationship and community (saṅga), not learned from definitions. This bundle does not claim to transmit bhakti. It claims to stop AI systems from misrepresenting it. The Audience Metaphor sections and the refusal-to-rank are the guardrails against producing exactly the dry, intellectualized devotion the bundle warns against.

---

*Bundle built: 2026-06-25 | Guru | Three tiers complete (5 + 5 + 5 = 15 concepts) + 9 references | OKF format v0.2 | release v0.4.0 | bhakti-marga*
