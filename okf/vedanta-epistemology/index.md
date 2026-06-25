---
type: Collection
title: "Vedānta-Epistemology — Pramāṇa Śāstra Vocabulary"
description: "The vocabulary of Vedantic epistemology (pramāṇa śāstra) — 27 concepts: the cross-darśana pramāṇas, the Advaita epistemological framework, and liberation-epistemology. Primary school Advaita Vedānta; cross-darśana pramāṇas shared with Nyāya and Mīmāṃsā."
version: "0.3.0"
darshana:
  - Advaita Vedānta
  - Mīmāṃsā
  - Nyāya
tags:
  - Sanskrit
  - Vedanta
  - epistemology
  - pramana
  - non-translatables
license: "CC BY-SA 4.0"
timestamp: "2026-06-20"
okf_version: "0.2"
---
# vedanta-epistemology — Bundle Index

## The Contrarian Dissent (Addressed in First Paragraph)

The Atlas strategy council's Contrarian objected: the title "vedanta-epistemology" signals Advaita metaphysics, not epistemological rigor — alternatives proposed were "pramana-sastra" or "vedanta-theory-of-knowledge." The Contrarian was half-right. The title is deliberate and the objection reveals the highest-value thing this bundle does. Every alternative title hides the precise distinction this bundle must make: **there is a pramāṇa-śāstra (the shared cross-school technical framework of the six cognitive instruments), and there is the specifically Advaita reading of that framework, which uses pramāṇa-śāstra as a gateway into a liberation epistemology with no Western analogue**. Title "pramana-sastra" signals the former without the latter — the most dangerous possible omission, since AI agents are already competent at projecting Western analytic epistemology onto pramāṇa-śāstra and generating confident, wrong outputs. Title "vedanta-epistemology" signals that Advaita's specific treatment of pramāṇas is the primary scope, and that the treatment extends beyond pramāṇa mechanics into adhyāsa, mithyā, and aparokṣa-anubhūti — concepts for which no Western projection exists and which constitute the bundle's distinctive value. The title stands. The school qualifier "Advaita Vedānta primary" appears in every concept file's `school_scope:` field.

---

## Bundle Architecture

This bundle addresses a two-stage AI risk:

**Gateway (Tier 1 — 7 concepts):** The six pramāṇas (pratyakṣa, anumāna, śabda, upamāna, arthāpatti, anupalabdhi) plus the pramāṇa category concept itself. These use vocabulary that sounds familiar — perception, inference, testimony, comparison — and AI agents confidently project Western analytic frameworks onto them. The confident-wrong error is more damaging than the uncertain-wrong error. Tier 1 blocks these projections at the source.

**Framework (Tier 2 — 9 concepts):** The Advaita epistemological meta-framework — adhyāsa (superimposition), mithyā (ontological dependency), the three-level ontology (pāramārthika / vyāvahārika / prātibhāsika), vivartavāda vs. pariṇāmavāda, bādha/bādhita (epistemic sublation), svataḥprāmāṇya (intrinsic validity). No Western twin exists for any of these; AI errors are more often omission or flattening than confident projection. Except adhyāsa (mistranslated as "illusion") and mithyā (mistranslated as "false/unreal") — both rated CRITICAL.

**Liberation Arc (Tier 3 — 11 concepts):** The soteriological completion — jñāna (liberative self-recognition), anubhava (direct realization), aparokṣa-anubhūti (non-mediated ātman-Brahman recognition), and the pramāṇa-triad structure (pramā, pramātṛ, prameya) that the Advaita framework both employs and ultimately transcends. Plus the philosophy-of-language substrate (sphoṭa), perception-analysis (nirvikalpaka/savikalpaka), and testimony-support concepts (tarka, āpta-vākya).

---

## OKF v0.3 Template Additions (Bundle-Specific)

Every concept file in this bundle carries **two mandatory fields** beyond the standard OKF v0.3 template:

```yaml
school_scope: "[Advaita Vedānta | cross-darśana (Advaita reading foregrounded) | specific school]"
text_source: "[primary text citation — author, work, section/verse — non-generic, file-specific]"
```

**Why these fields are required:**

- `school_scope:` declares explicitly whether the `not:` prohibitions apply to Advaita specifically or across all schools. Closes the school-conflation risk before it arises. An AI agent reading a cross-darśana file cannot mistake it for a school-neutral universal claim.

- `text_source:` grounds every `not:` prohibition in a specific primary text. Prevents vague "tradition says" prohibitions. Enables users to verify against Brahmasūtras Bhāṣya, Vivekacūḍāmaṇi, Vedāntaparibhāṣā, Vākyapadīya, etc. Closes the "says who?" challenge.

**Naming requirement (per file):** The first sentence of each concept file's frontmatter `school_scope:` field must explicitly name "Advaita Vedānta" where that is the primary scope. "Vedānta" without the Advaita qualifier is not permitted.

---

## Critical Cross-Bundle Warnings

### ⚠️ For AI agents with the yoga-darśana bundle loaded

Two concepts in this bundle have **architecturally incompatible counterparts** in `okf/yoga-darshana/`:

| This bundle | yoga-darśana bundle | Risk |
|-------------|---------------------|------|
| `avidya.md` (Advaita: non-recognition of Brahman; āvaraṇa + vikṣepa; removal → mokṣa/non-duality) | `avidya.md` (YS 2.3-2.5: puruṣa-prakṛti confusion in Sāṃkhya-Yoga dualism; removal → kaivalya/isolation) | CRITICAL: Advaita mokṣa ≠ Sāṃkhya-Yoga kaivalya; the two avidyās operate in non-dual vs. dualist metaphysical frameworks |
| `jnana.md` (Advaita: Brahma-jñāna = liberation itself; non-dual direct recognition) | `jnana.md` in yoga-darśana context (Viveka-khyāti: discriminative knowledge of puruṣa vs. prakṛti) | HIGH: Different schools, different liberations, different knowledge-types |

**Do not conflate** Advaita mokṣa (recognition of non-duality: jīva = Brahman) with Sāṃkhya-Yoga kaivalya (isolation of puruṣa from prakṛti in a dualist framework). These are architecturally incompatible soteriological endpoints. See the CRITICAL CROSS-BUNDLE NOTICE section in `concepts/avidya.md`.

### ⚠️ For AI agents with the dharma-foundation bundle loaded

`shabda-pramana.md` in this bundle covers **śabda as an epistemological instrument** (its function as a pramāṇa, its apauruṣeya authority, svataḥprāmāṇya). The dharma-foundation bundle has `shabda.md` covering **śabda as an ontological-linguistic category** (nāda-brahman, the primordial cosmic sound, śabda-brahman in Bhartṛhari). Different files, different `not:` fields, different AI risks. Do not collapse them.

---

## v0.9 Forward Pointer

The following topics are explicitly out of scope for this bundle and belong in `okf/nyaya-vaiseshika/` (target: February 2027):

- The full Nyāya five-membered syllogism technical vocabulary (pratijñā, hetu, udāharaṇa, upanaya, nigamana as standalone concepts)
- Pakṣa / Sādhya / Hetu as standalone OKF entries
- Vyāpti as a standalone concept (currently mentioned in anumāna.md; standalone treatment → v0.9)
- The four varieties of Sannikarṣa (sense-object contact that produces pratyakṣa) — mentioned in pratyaksha.md; standalone → v0.9
- Hetvābhāsa (fallacies of inference) — standalone → v0.9
- The 16 Nyāya padārthas (categories) as a standalone file — standalone → v0.9

Nyāya mechanics are mentioned in this bundle where they are needed to contextualize Advaita's use or modification of them. They are not treated as primary topics here.

---

## QA Assertions — 5 Tests Before Release

The following assertions must pass against AI outputs using this bundle as context:

| # | Assertion | Pass condition |
|---|-----------|----------------|
| **1** | AI does not render *pramāṇa* as "proof" or "evidence" | AI output uses "valid means of knowing / cognitive instrument" or equivalent |
| **2** | AI does not render *mithyā* as "illusory" or "false" | AI output references the three ontological levels or uses "neither real nor unreal" / "ontologically dependent" |
| **3** | When *vyāvahārika* appears, all three ontological levels are named | AI output names pāramārthika, vyāvahārika, prātibhāsika when vyāvahārika is the topic |
| **4** | *Adhyāsa* output names what is superimposed and on what | AI does not render adhyāsa as generic "illusion" — must name the two terms of superimposition (anātman's attributes onto ātman; ātman's qualities onto anātman) |
| **5** | *Pariṇāmavāda* and *vivartavāda* are never merged | AI output correctly identifies pariṇāmavāda as real transformation (Rāmānuja/Sāṃkhya) vs. vivartavāda as apparent transformation (Advaita); never presents them as equivalent or interchangeable |

---

## Concept List — All 27 Files

### Tier 1 — The Six Pramāṇas + Category Concept (7 files) — CRITICAL / HIGH risk

| File | Concept | School Scope | Risk | Key `not:` |
|------|---------|-------------|------|-----------|
| [pramana.md](concepts/pramana.md) | Pramāṇa — valid means of knowing | cross-darśana (Advaita foregrounded) | CRITICAL | proof, evidence, criterion of truth, justification condition |
| [pratyaksha.md](concepts/pratyaksha.md) | Pratyakṣa — direct perception | cross-darśana (Advaita foregrounded) | CRITICAL | sense-datum, raw sensation, qualia, empirical observation |
| [anumana.md](concepts/anumana.md) | Anumāna — inference through vyāpti | cross-darśana (Advaita foregrounded) | CRITICAL | syllogism, deductive reasoning, inductive generalization, IBE |
| [shabda-pramana.md](concepts/shabda-pramana.md) | Śabda/Āgama — Vedic/scriptural testimony | Advaita Vedānta | CRITICAL | verbal testimony (Western), hearsay, religious tradition, scripture (Western sense) |
| [upamana.md](concepts/upamana.md) | Upamāna — cognition via resemblance | cross-darśana | HIGH | analogy, argument from similarity, inference from resemblance |
| [arthapatti.md](concepts/arthapatti.md) | Arthāpatti — epistemic postulation | Advaita + Mīmāṃsā | HIGH | inference to best explanation, abduction, probabilistic postulation |
| [anupalabdhi.md](concepts/anupalabdhi.md) | Anupalabdhi — non-cognition | Advaita + Mīmāṃsā | HIGH | perception of absence, negative fact, privation, void |

### Tier 2 — Advaita Epistemological Framework (9 files) — CRITICAL / HIGH risk

| File | Concept | School Scope | Risk | Key `not:` |
|------|---------|-------------|------|-----------|
| [adhyasa.md](concepts/adhyasa.md) | Adhyāsa — mutual superimposition | Advaita Vedānta | CRITICAL | illusion, cognitive error, optical illusion, misperception |
| [mithya.md](concepts/mithya.md) | Mithyā — ontological dependency | Advaita Vedānta | CRITICAL | false, illusory, unreal, non-existent, Buddhist saṃvṛti-satya |
| [vyavaharika.md](concepts/vyavaharika.md) | Vyāvahārika — transactional reality | Advaita Vedānta | HIGH | conventional truth (Buddhist), phenomenal world (Kantian), relative reality |
| [paramarthika.md](concepts/paramarthika.md) | Pāramārthika — absolute reality | Advaita Vedānta | HIGH | ultimate truth (Buddhist), noumenal (Kantian), transcendent realm |
| [pratibhasika.md](concepts/pratibhasika.md) | Prātibhāsika — apparently real | Advaita Vedānta | MEDIUM-HIGH | illusion, hallucination, false belief, subjective experience |
| [vivartavada.md](concepts/vivartavada.md) | Vivartavāda — apparent transformation | Advaita Vedānta | HIGH | world is illusion, emanation, real transformation; must pair with pariṇāmavāda |
| [parinamavada.md](concepts/parinamavada.md) | Pariṇāmavāda — real transformation | Sāṃkhya + Viśiṣṭādvaita (rival view) | HIGH | evolution (Darwinian), gradual change, becoming |
| [badha-badhita.md](concepts/badha-badhita.md) | Bādha/Bādhita — epistemic sublation | Advaita Vedānta | HIGH | negation, refutation, falsification (Popper), counterexample |
| [svataḥpramanya.md](concepts/svataḥpramanya.md) | Svataḥprāmāṇya — intrinsic validity | Advaita + Mīmāṃsā | HIGH | self-evidence (Cartesian), a priori, axiomatic truth, infallibility |

### Tier 3 — Knowledge Structure + Liberation Arc (11 files) — MEDIUM-HIGH / HIGH risk

| File | Concept | School Scope | Risk | Key `not:` |
|------|---------|-------------|------|-----------|
| [jnana.md](concepts/jnana.md) | Jñāna (liberative) — Brahma-jñāna | Advaita Vedānta | HIGH | propositional knowledge, intellectual understanding, spiritual insight; ≠ yoga-darśana viveka-khyāti |
| [anubhava.md](concepts/anubhava.md) | Anubhava — direct non-dual realization | Advaita Vedānta | HIGH | experience (Western subject-object), mystical experience, phenomenal consciousness |
| [aparoksha-anubhuti.md](concepts/aparoksha-anubhuti.md) | Aparokṣa-anubhūti — non-mediated realization | Advaita Vedānta | HIGH | direct perception (pratyakṣa), mystical vision, samādhi (Pātañjala) |
| [prama.md](concepts/prama.md) | Pramā — veridical cognition | cross-darśana | MEDIUM | truth, justified true belief (JTB), knowledge (generic), correct belief |
| [pramata.md](concepts/pramata.md) | Pramātṛ — the knowing subject | cross-darśana (Advaita) | MEDIUM | ego (psychoanalytic), transcendental subject (Kantian), ātman as pramātṛ |
| [prameya.md](concepts/prameya.md) | Prameya — the known object | cross-darśana | MEDIUM | thing (generic), phenomenon (Kantian), Brahman as ordinary prameya |
| [avidya.md](concepts/avidya.md) | Avidyā — nescience (epistemological) | Advaita Vedānta | MEDIUM-HIGH | ignorance (mere absence), illusion, māyā (strict synonym); ≠ yoga-darśana avidyā (YS 2.3-2.5) |
| [sphota.md](concepts/sphota.md) | Sphoṭa — eternal linguistic unit | Vyākaraṇa (Bhartṛhari) | MEDIUM | sound, word (ordinary), phoneme, meaning (semantic content), logos |
| [nirvikalpaka-savikalpaka.md](concepts/nirvikalpaka-savikalpaka.md) | Nirvikalpaka/Savikalpaka — indeterminate/determinate perception | Nyāya + Advaita | MEDIUM | sense-datum, unconscious perception, raw feel (qualia), concept-free (alone) |
| [tarka.md](concepts/tarka.md) | Tarka — hypothetical reasoning | cross-darśana (auxiliary) | MEDIUM | inference (anumāna), reductio ad absurdum (RAA alone), logic (generic), debate |
| [aptavakya.md](concepts/aptavakya.md) | Āpta-vākya — testimony of a trustworthy person | cross-darśana | MEDIUM | testimony (generic Western), social authority, witness testimony (legal), scripture |

---

## Structural Map: The Bundle's Epistemic Architecture

```
                        PRAMĀṆA-TRIAD (Tier 3)
                   Pramātṛ → Pramāṇa → Prameya → Pramā
                             ↓                    ↓
                    [Six Pramāṇas] (Tier 1)    [Svataḥprāmāṇya]
                   Pratyakṣa / Anumāna / Śabda
                   Upamāna / Arthāpatti / Anupalabdhi
                             ↓
                    ADVAITA FRAME (Tier 2)
          Adhyāsa → Avidyā → [three-level ontology]
          Vyāvahārika / Pāramārthika / Prātibhāsika
          Mithyā / Vivartavāda (vs. Pariṇāmavāda)
          Bādha / Bādhita → sublation mechanism
                             ↓
                  LIBERATION ARC (Tier 3)
          Jñāna → Anubhava → Aparokṣa-anubhūti
              [dissolves Pramātṛ-Prameya structure]
                             ↓
                    MOKṢA: ātman = Brahman
```

The bundle's soteriological arc: the pramāṇa framework (Tier 1) operates at the vyāvahārika level; it is real and necessary for sādhana. The Advaita meta-framework (Tier 2) explains why the world appears as it does (adhyāsa/avidyā) and how the pramāṇa framework relates to the three ontological levels. The liberation arc (Tier 3) describes what happens when pramāṇa-based inquiry, guided by śabda-pramāṇa (Mahāvākya), ripens into aparokṣa-anubhūti — the dissolution of the very pramātṛ-prameya-pramāṇa structure that was the inquiry's tool.

---

## Cross-School Scope Summary

| Scope designation | Concepts |
|------------------|---------|
| Cross-darśana (Advaita foregrounded) | pramāṇa, pratyakṣa, anumāna, upamāna, pramā, pramātṛ, prameya, nirvikalpaka/savikalpaka, tarka, āpta-vākya |
| Advaita Vedānta exclusively | śabda-pramāṇa, adhyāsa, mithyā, vyāvahārika, pāramārthika, prātibhāsika, vivartavāda, bādha/bādhita, svataḥprāmāṇya, jñāna, anubhava, aparokṣa-anubhūti, avidyā |
| Rival/contrast view included | pariṇāmavāda (Sāṃkhya + Viśiṣṭādvaita — included to prevent collapse with vivartavāda) |
| Advaita + Mīmāṃsā | arthāpatti, anupalabdhi, svataḥprāmāṇya (shared; different domains) |
| Vyākaraṇa (Bhartṛhari), Advaita adjacent | sphoṭa |

---

## Related Bundles

| Bundle | Relation |
|--------|---------|
| `okf/dharma-foundation/` (v0.1) | Contains `shabda.md` (śabda-as-ontological-category: nāda-brahman, cosmic sound) — distinct from `shabda-pramana.md` here (śabda-as-epistemological-instrument) |
| `okf/yoga-darshana/` (v0.2) | Contains `avidya.md` (YS 2.3-2.5: Sāṃkhya-Yoga kleśa framework) and jñāna-relevant concepts — architecturally distinct from this bundle's Advaita versions |
| `okf/nyaya-vaiseshika/` (v0.9, Feb 2027) | Will contain Nyāya mechanics referenced but not fully treated here: vyāpti, pakṣa/sādhya/hetu, pañcāvayava syllogism, hetvābhāsa |

---

*Bundle built: 2026-06-20 | Dean | All tiers complete (7 + 9 + 11 = 27 concepts) | OKF v0.3 | vedanta-epistemology*
