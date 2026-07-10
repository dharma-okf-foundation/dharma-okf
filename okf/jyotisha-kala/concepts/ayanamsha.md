---
type: Concept
bundle: jyotisha-kala
bundle_version: 0.12.0
id: ayanamsha
title: Ayanāṃśa
iast: Ayanāṃśa
devanagari: अयनांश
description: 'The accumulating angular difference between sidereal and tropical zodiacs caused by the precession of the equinoxes, near 24° today; the hinge on which every sidereal computation turns; NOT a fudge factor, NOT a single agreed number, NOT irrelevant trivia.'
darshana:
- Jyotiṣa
text_source: Sūrya Siddhānta 3; Siddhānta Śiromaṇi
tags:
- ayanamsha
- precession
- sidereal
- ganita
- jyotisha
not:
- term: 'a fudge factor'
  why: 'The ayanāṃśa measures a real astronomical phenomenon: the equinoxes precess along the ecliptic about 50.3 arcseconds a year, so the season-anchored and star-anchored reference frames drift apart continuously. The siddhāntas modeled the motion (Sūrya Siddhānta as an oscillating trepidation); the modern almanac states the accumulated value.'
  instead: 'Render ayanāṃśa as the sidereal-tropical offset from precession and keep the Sanskrit term.'
- term: 'a single agreed number'
  why: 'Ayanāṃśas differ by their chosen zero-date and anchor star. Lahiri (Citrapakṣa, anchored on Citrā/Spica) is the Indian official standard; Raman, Kṛṣṇamūrti, and others differ by fractions of a degree that move chart boundaries. Serious almanacs state which ayanāṃśa they use.'
- term: 'irrelevant trivia'
  why: 'About 24 degrees is most of a sign: it is the entire difference between the tropical and sidereal answer to “where is the Sun.” Nothing sidereal is computable without declaring it.'
related:
- /concepts/rashi.md
- /concepts/ayana.md
- /concepts/nakshatra.md
timestamp: '2026-07-09'
okf_version: '0.2'
license: CC BY-SA 4.0
---

# Ayanāṃśa -- अयनांश

**Not:** a fudge factor, a single agreed number, irrelevant trivia

## What It Actually Means

Precession swings the equinox slowly backward along the ecliptic, about 50.3 arcseconds a year, so a zodiac anchored to the seasons (tropical) and one anchored to the stars (sidereal) drift apart roughly a degree every 72 years. The ayanāṃśa is the accumulated gap, near 24 degrees today, and it is the declared constant that converts tropical positions into sidereal ones. Classical siddhāntas modeled the motion as trepidation; the modern Indian ephemeris fixes the Lahiri (Citrapakṣa) ayanāṃśa, anchored on the star Citrā, as the official standard, with rival ayanāṃśas in use across the horā tradition. It is the single most consequential technical parameter in sidereal astronomy’s toolkit.

## Audience Metaphor

Two rulers laid along the same sky, one nailed to the stars and one to the seasons, drifting apart a hair each year for two thousand years: the gap is now almost a full sign wide. Every sidereal computation begins by declaring how wide it takes the gap to be, and that declaration has a name.

## Citations

1. Sūrya Siddhānta 3 on the motion of the equinoxes (trepidation) -- see [references/surya-siddhanta.md](../references/surya-siddhanta.md)
2. Siddhānta Śiromaṇi on precession in the later gaṇita tradition -- see [references/siddhanta-shiromani.md](../references/siddhanta-shiromani.md)
