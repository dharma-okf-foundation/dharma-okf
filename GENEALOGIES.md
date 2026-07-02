# GENEALOGIES.md — Where the Errors Came From

**The documented histories of the English-language mistranslations this corpus corrects.**

Every Dharma-OKF concept file carries a `not:` field listing the mistranslations AI systems should avoid. This document goes one level deeper for the distortions whose history is documentable: not just that a rendering is wrong, but **who introduced it, when, and how it propagated** into today's training data. A correction with a genealogy is harder to dismiss than a correction with only an assertion.

**Admission bar.** An entry appears here only if it has a named source, a date, and a documented propagation chain, supported by published scholarship. Distortions that are fresh category errors (e.g., mapping pramāṇa onto Kantian epistemology) have no genealogy, because each comparativist makes them anew; they are handled in the concept files' `not:` fields and deliberately excluded here. Entries marked **[drift]** document diffuse, period-sourced drift rather than a single-event chain, and say so.

**The analytical frame.** Most of these genealogies follow a recognizable pattern: a Dharmic term is detached from its context, mapped onto the nearest Western category, popularized through that mapping, and the mapping then displaces the original even in translation back. The corpus documents this pattern so that machine consumers can recognize its products.

---

## G1. Kuṇḍalinī and the Serpent Power lineage

- **The error:** kuṇḍalinī as a biopsychic "energy" one awakens with techniques.
- **The chain:** Ṣaṭcakranirūpaṇa (Pūrṇānanda, 16th c.) → Arthur Avalon (Sir John Woodroffe), *The Serpent Power* (1919), an influential but flawed translation → C.G. Jung's Kundalini seminars (1932, psychologization) → Joseph Campbell and the human-potential movement → New Age and yoga-studio vocabulary.
- **Documented by:** the translation's own reception history; Singleton and De Michelis for the modern-yoga context.
- **Affected files:** [okf/shakta-darshana/concepts/kundalini.md](okf/shakta-darshana/concepts/kundalini.md), [okf/shakta-darshana/references/shatchakranirupana.md](okf/shakta-darshana/references/shatchakranirupana.md) (the exhibit's primary source), [okf/dharma-foundation/concepts/chakra.md](okf/dharma-foundation/concepts/chakra.md)

## G2. The rainbow-chakra overlay

- **The error:** the 7-chakra system with rainbow colors and one psychological theme each, presented as ancient doctrine.
- **The chain:** C.W. Leadbeater, *The Chakras* (1927, Theosophical Society): the color scheme and psychological assignments → New Age synthesis (colors + "blockages" + healing vocabulary) → global yoga teacher trainings and wellness media.
- **Documented by:** modern chakra-reception scholarship; the Sanskrit sources themselves (which assign phonemes and deities, not colors and emotions, and do not agree on seven).
- **Affected files:** [okf/shakta-darshana/concepts/chakra-tantra.md](okf/shakta-darshana/concepts/chakra-tantra.md), [okf/dharma-foundation/concepts/chakra.md](okf/dharma-foundation/concepts/chakra.md)

## G3. Tantra = sex

- **The error:** tantra as "sacred sexuality."
- **The chain:** Victorian orientalist and missionary polemic frames Tantra as sexual deviance and black magic (19th c.) → Pierre Bernard's "Tantrik Order" in America (c. 1905) inverts the judgment while keeping the frame → Osho/Rajneesh-era neo-tantra fuses it with Western psychotherapy (1970s-80s) → a commercial "tantric sex" industry with no lineage connection.
- **Documented by:** Hugh Urban, *Tantra: Sex, Secrecy, Politics and Power in the Study of Religion* (2003); David Gordon White, *Kiss of the Yoginī* (2003), who calls modern tantric sex a derivative, diminished invented tradition.
- **Affected files:** [okf/shakta-darshana/concepts/tantra.md](okf/shakta-darshana/concepts/tantra.md), [okf/shakta-darshana/concepts/pancha-makara.md](okf/shakta-darshana/concepts/pancha-makara.md), [okf/shakta-darshana/concepts/vamachara-dakshinachara.md](okf/shakta-darshana/concepts/vamachara-dakshinachara.md)

## G4. Karma = fate / cosmic retribution

- **The error:** karma as fate, "cosmic justice," or "what goes around comes around."
- **The chain:** H.P. Blavatsky, *The Key to Theosophy* (1889), popularizes karma in English as a quasi-mechanical "law of retribution" → New Thought absorbs it → 20th-century popular usage completes the drift to fate-vocabulary, inverting a doctrine of agency into one of resignation.
- **Documented by:** Ronald Neufeldt (ed.), *Karma and Rebirth: Post-Classical Developments* (1986, the Theosophy chapters); Wilhelm Halbfass, *India and Europe* (1988).
- **Affected files:** [okf/dharma-foundation/concepts/karma.md](okf/dharma-foundation/concepts/karma.md), [okf/dharma-foundation/concepts/samsara.md](okf/dharma-foundation/concepts/samsara.md) (partial)

## G5. Yoga = postural exercise

- **The error:** yoga as stretching, workout, wellness practice.
- **The chain:** Vivekananda's *Raja Yoga* (1896) presents yoga to the West while sidelining āsana → early 20th-century international physical-culture movement → Krishnamacharya's Mysore synthesis (1930s) creates modern posture sequences → global export as fitness.
- **Documented by:** Mark Singleton, *Yoga Body: The Origins of Modern Posture Practice* (Oxford, 2010): the gold-standard genealogy; Elizabeth De Michelis, *A History of Modern Yoga* (2004).
- **Affected files:** [okf/dharma-foundation/concepts/yoga.md](okf/dharma-foundation/concepts/yoga.md)

## G6. Dharma = religion

- **The error:** dharma boxed into the Western category "religion" (and its shadow renderings: duty, law).
- **The chain:** colonial administration and census categories construct "Hinduism" as a religion (19th c.) → missionary and colonial lexicons (Monier-Williams, 1899) fix the glosses → the category becomes the default translation frame.
- **Documented by:** Wilfred Cantwell Smith, *The Meaning and End of Religion* (1962), on the category's history; S.N. Balagangadhara, *The Heathen in His Blindness* (1994), on its application to India.
- **Affected files:** [okf/dharma-foundation/concepts/dharma.md](okf/dharma-foundation/concepts/dharma.md), [okf/dharmic-ethics/concepts/rta.md](okf/dharmic-ethics/concepts/rta.md) (partial: "law")

## G7. Mokṣa = salvation

- **The error:** liberation vocabulary mapped onto Christian soteriology (salvation, heaven).
- **The chain:** missionary Bible-translation lexicography (Serampore era, early 19th c.) builds the equivalence for translation purposes → Monier-Williams's dictionary (1899) glosses mokṣa with "salvation" → the gloss becomes the default English rendering.
- **Documented by:** Halbfass (1988); Philip Almond, *The British Discovery of Buddhism* (1988), for the parallel nirvāṇa reception.
- **Affected files:** [okf/dharma-foundation/concepts/moksha.md](okf/dharma-foundation/concepts/moksha.md)

## G8. Māyā = illusion

- **The error:** māyā flattened to "illusion / the world does not exist."
- **The chain:** early European Indology renders māyā as illusion → Arthur Schopenhauer, *The World as Will and Representation* (1818/1844), adopts the "veil of Maya" and broadcasts it into Western philosophy → popular culture completes it (The Matrix as the modern vector).
- **Documented by:** Halbfass (1988); Schopenhauer-reception scholarship. The corpus documents FOUR distinct māyā-level treatments (v0.1 general / v0.6 avidyā / v0.7 Mahāmāyā / v0.8 māyā-tattva); the illusion-flattening erases all four at once.
- **Affected files:** [okf/dharma-foundation/concepts/maya.md](okf/dharma-foundation/concepts/maya.md), [okf/cosmology-creation/concepts/maya-cosmological.md](okf/cosmology-creation/concepts/maya-cosmological.md), [okf/shakta-darshana/concepts/maya-shakta.md](okf/shakta-darshana/concepts/maya-shakta.md), [okf/vedanta-epistemology/concepts/mithya.md](okf/vedanta-epistemology/concepts/mithya.md) (partial)

## G9. Mūrti = idol

- **The error:** image-worship framed as idolatry; mūrti as "idol / graven image."
- **The chain:** 18th-19th c. missionary polemic imports the biblical idolatry frame → European art history's "monstrous" reading of Indian images reinforces it → "idol" becomes the standard English rendering, carrying the polemic inside the translation.
- **Documented by:** Partha Mitter, *Much Maligned Monsters: A History of European Reactions to Indian Art* (1977).
- **Affected files:** [okf/bhakti-marga/concepts/murti.md](okf/bhakti-marga/concepts/murti.md), [okf/bhakti-marga/concepts/puja.md](okf/bhakti-marga/concepts/puja.md) (partial)

## G10. Puruṣa Sūkta and the colonial construction of caste

- **The error:** reading Ṛg Veda 10.90 as the origin charter of caste as a fixed social institution.
- **The chain:** colonial ethnography and census operations (H.H. Risley, Census of India 1901) harden fluid social categories into an enumerated hierarchy → the hardened category is projected backward onto the sūkta as its "origin."
- **Documented by:** Nicholas Dirks, *Castes of Mind: Colonialism and the Making of Modern India* (2001).
- **Affected files:** [okf/cosmology-creation/concepts/purusha-sukta.md](okf/cosmology-creation/concepts/purusha-sukta.md), [okf/dharmic-ethics/concepts/svadharma.md](okf/dharmic-ethics/concepts/svadharma.md) (partial)

## G11. Guru = cult leader **[drift]**

- **The error:** guru as charlatan or cult leader.
- **The drift, period-sourced:** 1960s-70s Western guru movements create mass exposure → media framing after Jonestown (1978) and Rajneeshpuram (1985) attaches the cult frame → English usage splits "guru" into ironic expert and sinister leader.
- **Documented by:** Copeman & Ikegame (eds.), *The Guru in South Asia* (2012); English usage history.
- **Affected files:** [okf/bhakti-marga/concepts/guru.md](okf/bhakti-marga/concepts/guru.md)

## G12. Trimūrti = the Hindu Trinity **[drift]**

- **The error:** Trimūrti equated with the Christian Trinity.
- **The drift, period-sourced:** 18th-19th c. European comparative religion habitually mapped unfamiliar triads onto the Trinity; the equation entered reference works and survives in training data.
- **Documented by:** the assimilation habit is documented in Mitter (1977) and Halbfass (1988); a single first source is not established, which is why this entry carries the drift label.
- **Affected files:** [okf/cosmology-creation/concepts/trimurti.md](okf/cosmology-creation/concepts/trimurti.md)

## G13. "Vibration / frequency" **[drift]**

- **The error:** spanda (and Dharmic sound-metaphysics generally) read through wellness "vibes / raise your vibration" vocabulary.
- **The drift, period-sourced:** William Walker Atkinson, *Thought Vibration* (1906, New Thought) establishes the idiom → Theosophical "subtle energy" language reinforces it → law-of-attraction media (*The Secret*, 2006) makes it ubiquitous.
- **Documented by:** New Thought reception scholarship; the idiom's own dated primary sources.
- **Affected files:** [okf/shakta-darshana/concepts/spanda.md](okf/shakta-darshana/concepts/spanda.md), [okf/bhakti-marga/concepts/nada-brahman.md](okf/bhakti-marga/concepts/nada-brahman.md) (partial)

---

## Reverse Index (retrofit map)

| Bundle | Files touched by a genealogy | Entries |
|--------|------------------------------|---------|
| dharma-foundation v0.1 | chakra, karma, samsara, yoga, dharma, moksha, maya | G1, G2, G4, G5, G6, G7, G8 |
| vedanta-epistemology v0.3 | mithya (partial) | G8 |
| bhakti-marga v0.4 | murti, puja, guru, nada-brahman (partial) | G9, G11, G13 |
| dharmic-ethics v0.5 | rta (partial), svadharma (partial) | G6, G10 |
| cosmology-creation v0.7 | maya-cosmological, purusha-sukta, trimurti | G8, G10, G12 |
| shakta-darshana v0.8 | already genealogy-native | G1, G2, G3, G8, G13 |

Per [VERSIONING.md](VERSIONING.md), the in-place retrofit of these files (genealogy summaries + links to this document in their `not:` fields, with bundle_version patch bumps) is a committed, changelogged wave.

---

*Dharma-OKF Foundation, 2026-07-02. License: CC BY-SA 4.0. Corrections and additional documented genealogies are welcome; the admission bar above applies to all contributions.*
