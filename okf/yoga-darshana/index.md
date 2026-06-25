---
type: Collection
title: "Yoga Darśana — Pātañjala Yoga Vocabulary"
description: "The technical lexicon of Patañjali Yoga Sūtras as a distinct darśana — 26 Sanskrit non-translatable concepts. Enforces the cross-darśana distinction: Kaivalya is not Mokṣa; Puruṣa is not Ātman/Brahman."
version: "0.2.0"
darshana:
  - Pātañjala Yoga
  - Sāṃkhya
tags:
  - Sanskrit
  - Yoga
  - Patanjali
  - Samkhya
  - non-translatables
license: "CC BY-SA 4.0"
timestamp: "2026-06-20"
okf_version: "0.2"
---
# Yoga Darśana OKF Bundle — Index

**Bundle:** `yoga-darshana`  
**Version:** `0.2.0`  
**License:** CC BY-SA 4.0  
**Darśana:** Yoga (Patañjali's Yoga Sūtras)  
**Related Darśana:** Sāṃkhya  
**Concept Count:** 26  
**Status:** Complete  

---

## Purpose

This bundle provides AI-ready Open Knowledge Format (OKF) concept files for the vocabulary of Patañjali's Yoga Sūtras as a distinct philosophical school (*darśana*). Each file includes:

- YAML frontmatter with `not:` fields — English mistranslations the AI must avoid
- Full IAST transliterations and Devanāgarī
- Sūtra references with IAST originals and translations
- Audience metaphors for non-specialist explanation
- Cross-references to other bundle concepts

**Critical design principle:** Yoga Darśana is a *dual ontology*. Liberation in Yoga is *kaivalya* (permanent isolation of Puruṣa from Prakṛti) — not Advaita Vedānta's *mokṣa* (Ātman recognized as Brahman). These two frameworks cannot be mixed. Every file in this bundle has been designed to prevent that cross-darśana conflation.

---

## Group 1 — Sāṃkhya Ontological Frame (6 concepts)

The foundational dual ontology that Yoga shares with and builds upon Sāṃkhya.

| File | Concept | Sūtra | Brief Description |
|------|---------|-------|-------------------|
| [purusha.md](concepts/purusha.md) | Puruṣa | YS 1.3, 2.20, 4.34 | Pure witness-consciousness; unchanging; many; not Ātman |
| [prakriti-yoga.md](concepts/prakriti-yoga.md) | Prakṛti (Yoga) | YS 2.18-2.19, 4.13-14 | All that is not Puruṣa; the Guṇa-triad in dynamic play; site of liberation-path |
| [guna.md](concepts/guna.md) | Guṇa-s | YS 2.18-2.19 | Three constitutive strands of Prakṛti: Sattva, Rajas, Tamas |
| [sattva.md](concepts/sattva.md) | Sattva | YS 2.41, 3.35-3.36, 3.49 | Guṇa of luminosity and clarity; medium of viveka-khyāti |
| [rajas.md](concepts/rajas.md) | Rajas | YS 2.18, 4.13-14 | Guṇa of activity and motion; driver of vṛtti-generation |
| [tamas.md](concepts/tamas.md) | Tamas | YS 2.18, 4.13-14 | Guṇa of inertia; obscures clarity AND stores saṃskāras |

---

## Group 2 — Kleśa-s and Obstacles (6 concepts)

The five affliction-roots and the taxonomy of suffering in Yoga Darśana.

| File | Concept | Sūtra | Brief Description |
|------|---------|-------|-------------------|
| [klesha.md](concepts/klesha.md) | Kleśa-s | YS 2.2-2.9 | Five affliction-roots: the structure of suffering in Prakṛti |
| [avidya-yoga.md](concepts/avidya-yoga.md) | Avidyā (Yoga) | YS 2.4-2.5 | Root misidentification of Puruṣa with Prakṛti; mother kleśa |
| [asmita.md](concepts/asmita.md) | Asmitā | YS 2.6 | Misidentification of Puruṣa with buddhi (*draṣṭṛ-darśanaśaktyor ekatāmiva*) |
| [raga.md](concepts/raga.md) | Rāga | YS 2.7 | Attraction-pattern flowing from past pleasure; Sāttvic trap included |
| [dvesha.md](concepts/dvesha.md) | Dveṣa | YS 2.8 | Aversion-pattern flowing from past pain; structural pair with rāga |
| [abhinivesha.md](concepts/abhinivesha.md) | Abhiniveśa | YS 2.9 | The drive to persist (*abhi* = toward, *ni* = down, *viś* = to enter); last kleśa dissolved at kaivalya |

---

## Group 3 — Citta Dynamics (5 concepts)

How the mind-complex works, accumulates patterns, and can be transformed.

| File | Concept | Sūtra | Brief Description |
|------|---------|-------|-------------------|
| [chitta-vritti.md](concepts/chitta-vritti.md) | Citta-Vṛtti | YS 1.2 | The definitional term: *yogaś citta-vṛtti-nirodhaḥ* |
| [vritti.md](concepts/vritti.md) | Vṛtti | YS 1.5-1.11 | Five types of citta-modification; kliṣṭa/akliṣṭa distinction |
| [samskara.md](concepts/samskara.md) | Saṃskāra | YS 1.18, 3.9-3.10, 4.8-4.9 | Cognitive ruts; formation mechanism; nirodha-saṃskāra paradox; dagdhabīja |
| [vasana.md](concepts/vasana.md) | Vāsanā | YS 4.8-4.9, 4.24 | Perfume-like residue; cross-life persistence; saṃskāra-vāsanā-kleśa chain |
| [nirodha.md](concepts/nirodha.md) | Nirodha | YS 1.2, 1.51, 3.9 | Cessation (not suppression); abhyāsa + vairāgya; five levels; final nirodha = kaivalya |

---

## Group 4 — Absorption States (5 concepts)

Samādhi, its stages, cognitive mechanics, and the transformation theory underlying them.

| File | Concept | Sūtra | Brief Description |
|------|---------|-------|-------------------|
| [samprajnata-samadhi.md](concepts/samprajnata-samadhi.md) | Samprajñāta Samādhi | YS 1.17-1.18, 1.41-1.46 | Seeded absorption; four stages: savitarka/savicāra/sānanda/sāsmitā |
| [asamprajnata-samadhi.md](concepts/asamprajnata-samadhi.md) | Asamprajñāta Samādhi | YS 1.18, 1.51, 3.8 | Seedless absorption; virāma-pratyaya; burns all saṃskāras; nirbīja |
| [samapatti.md](concepts/samapatti.md) | Samāpatti | YS 1.41-1.46 | Cognitive coincidence — the *mechanism* by which samādhi works; abhijāta maṇi |
| [parinama.md](concepts/parinama.md) | Pariṇāma | YS 3.9-3.16 | Transformation within satkāryavāda; three citta-pariṇāma-s (nirodha/samādhi/ekāgratā) |
| [kaivalya.md](concepts/kaivalya.md) | Kaivalya | YS 4.34, 2.25, 3.55 | Liberation — Puruṣa's permanent isolation from Prakṛti; NOT mokṣa |

---

## Group 5 — Eight-Limb Deep Dives (4 concepts)

Selected limbs and advanced topics requiring the most careful terminological precision.

| File | Concept | Sūtra | Brief Description |
|------|---------|-------|-------------------|
| [pratyahara.md](concepts/pratyahara.md) | Pratyāhāra | YS 2.54-2.55 | Bridge limb; senses following citta inward; consequence not technique |
| [dharana.md](concepts/dharana.md) | Dhāraṇā | YS 3.1 | Sixth limb; *deśa-bandha* — deliberate binding of citta to one point |
| [viveka-khyati.md](concepts/viveka-khyati.md) | Viveka-Khyāti | YS 2.26-2.28, 3.55 | Discriminative recognition of Puruṣa/Prakṛti distinction; remedy for avidyā; must be transcended |
| [ishvara-yoga.md](concepts/ishvara-yoga.md) | Īśvara (Yoga) | YS 1.23-1.29 | Special Puruṣa untouched by kleśas; Praṇava (OṂ) as designator; not a creator God |

---

## Critical Cross-Darśana Warnings

AI systems processing this bundle must maintain the following distinctions:

### Kaivalya ≠ Mokṣa
- **Kaivalya** (Yoga): Puruṣa permanently isolated from Prakṛti; dual ontology remains; Prakṛti continues to exist
- **Mokṣa** (Advaita): Ātman recognized as identical with Brahman; non-dual; world dissolves as Māyā

### Puruṣa ≠ Ātman/Brahman
- **Puruṣa** (Sāṃkhya-Yoga): pure witness-consciousness; eternally many; never identical with Prakṛti; distinct from all evolutes of Prakṛti including buddhi
- **Ātman** (Advaita): pure witness-consciousness, ultimately identical with Brahman — not an individual self at all; not a concept in Sāṃkhya-Yoga

### Īśvara (Yoga) ≠ Brahman (Advaita)
- **Īśvara** (Yoga): a special Puruṣa (*puruṣa-viśeṣa*) untouched by kleśas; not a creator; one of many eternal Puruṣa-s
- **Brahman** (Advaita): the sole non-dual reality; all plurality is Māyā

### Viveka-Khyāti ≠ Enlightenment / Self-Realization
- **Viveka-khyāti**: sustained discriminative awareness of Puruṣa/Prakṛti distinction; a Sattvic vṛtti that must itself be transcended
- Not to be equated with Vedāntic self-realization, Buddhist enlightenment, or any non-dual recognition-event

---

## Bundle Metadata

```yaml
bundle: yoga-darshana
version: 0.2.0
created: 2026-06-20
okf_schema: 0.1
license: CC BY-SA 4.0
primary_sources:
  - Yoga Sūtras of Patañjali (with IAST)
  - Yoga Bhāṣya of Vyāsa
  - Tattvavaiśāradī of Vācaspatimiśra
  - Sāṃkhya Kārikā of Īśvarakṛṣṇa (for Sāṃkhya frame)
related_bundles:
  - dharma-foundation v0.1 (shared terms: avidya, ishvara, prakriti with -yoga suffix)
github_target: okf/yoga-darshana/
```
