# Contributing to Dharma-OKF

This repository publishes the Dharma-OKF knowledge bundles and the `dharma-okf/1.0`
profile of the Open Knowledge Format. Content is licensed CC BY-SA 4.0 — see
`LICENSE-CONTENT`.

Before proposing a change, read `PROFILE.md` (normative) and `CLAUDE.md` (working
rules for AI agents operating in this repository).

## Corrections to a concept

Doctrinal corrections are the most valuable contribution here and are welcome.

Open an issue naming:

1. the concept file,
2. the claim you believe is wrong,
3. the primary-source citation supporting the correction.

Corrections are reviewed by a human before publication (`PROFILE.md` §3.3). We are
particularly interested in cases where a `not:` field names a mistranslation
inaccurately, or misses one that is doing real damage in circulation.

## Scope and affiliation

This repository is **not affiliated with GoogleCloudPlatform/knowledge-catalog**.
Dharma-OKF is an independent profile of the Open Knowledge Format; contributing here
involves no agreement with any third party. Contributions to the *base specification*
belong in that project, under its own terms.

## If you open a pull request

- `python3 okf/tools/okf_validate.py --strict` → 0 fail / 0 warn
- `python3 -m pytest okf/tests/`
- Body links must be **relative**, never absolute (`PROFILE.md` §3.1) — the reference
  viewer discards absolute links, so they render as missing relationships
- Never add or edit a `verified:` field. It records a human review event and is not
  written by tooling or contributors (`PROFILE.md` §3.3)
- Leave `not:` structure intact: `term` / `why` / `instead`, never a bare list of
  strings (`PROFILE.md` §2.1)

## Questions

Open a discussion. Questions about what a term means, and challenges to how we have
drawn a distinction, are both in scope.
