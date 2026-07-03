# Upload Guide -- nyaya-vaisheshika v0.9.0

**Bundle:** nyaya-vaisheshika (OKF v0.9) | **Release tag:** v0.9.0 | **okf_version:** 0.2 (canonical)
**Validated:** 0 fail / 0 warn (okf_validate.py), 2026-07-03
**Local source:** `outputs/2026-07/okf-bundles/nyaya-vaisheshika/`

## What's in the bundle (38 files)

- `index.md` (bundle index: does-not-claim block, v0.3 boundary note, 5 tier tables, 8 cross-bundle warnings, Navya-Nyaya deferral, reference list)
- `concepts/` -- 27 concept files, 5 tiers
- `references/` -- 10 primary-text reference files

**Tiers:** T1 Inference Engine (6: anumana, vyapti, panchavayava, hetu, tarka, hetvabhasa) - T2 Pramanas from the source school (5: pramana, pratyaksha, upamana, shabda, pramanya) - T3 Debate and inquiry (5: shodasha-padartha, vada, jalpa, vitanda, nigrahasthana) - T4 Vaisesika ontology (6: saptapadartha, dravya, guna, karma, samanya-vishesha, samavaya) - T5 Atomism and realist theism (5: paramanu, dvyanuka-tryanuka, atman, ishvara, anyatha-khyati).

## Upload steps (GitHub web UI, Option B)

1. Create folder `okf/nyaya-vaisheshika/` in the dharma-okf repo.
2. Upload `index.md`, then the `concepts/` folder (27 files), then the `references/` folder (10 files). Preserve the subfolder structure.
3. Spot-check the index.md blob render: all tier-table links and the reference links should be clickable and resolve.
4. Create **Release v0.9.0** tagged at the upload commit, title "nyaya-vaisheshika bundle: the science of inference and debate."

## Post-upload verification (okf-release-verify)

- Clone-diff at the release SHA (`git clone --filter=blob:none` + sparse checkout, or full shallow clone), byte-diff against the local source. This is the authoritative method (immune to API throttling / raw-URL provenance blocks).
- Confirm `ls-remote` shows the `v0.9.0` tag on the remote (not a draft).
- Confirm all `okf_version: "0.2"` and `bundle_version: 0.9.0` throughout; all citation/related links resolve; ASCII slugs throughout.

## Doctrinal notes for the release

- Framing is "the science of inference and debate," NOT "formal logic" (Contrarian reframe; see the does-not-claim block in index.md).
- The v0.3 pramana overlap is school-contrast, not duplication: shared terms carry `school_scope: nyaya` and are reciprocally cross-linked. The reciprocal `related:` back-link INTO v0.3's anumana is the first Genealogy Phase 2 action (patch bump v0.3.1 + changelog), staged, not yet applied.
- Navya-Nyaya is named-and-deferred (Tattvacintamani reference only); it is reserved for a dedicated future bundle.
- **karma (Vaisesika, motion) is the flagship cross-bundle collision:** it is one of five kinds of physical motion, NOT the moral law of karma in dharma-foundation v0.1. Vaisesika files moral desert under adrsta, not under the karma category. See concepts/karma.md `not:` field and cross-bundle warning #8.

## 27th concept added: karma (owner-approved 2026-07-03)

`karma (Vaisesika, motion)` was drafted during the sprint and held back to keep the bundle at the approved 26. On owner go ("add karma to v0.9"), it is now **included as the 27th concept** in Tier 4 (Vaisesika ontology), between guna and samanya-vishesha. This is a deliberate change to the "approved as proposed" 26-concept lock; the lock now stands at 27. Genealogy Phase 2 (gated on this concept-lock) proceeds from the 27-concept lock.

## Companion re-upload: dharma-foundation v0.1 (reciprocal cross-link)

The reciprocal cross-reference back into v0.1 was applied **now** (owner directed), not deferred to the Phase 2 wave. `okf/dharma-foundation/concepts/karma.md` gained a sixth `not:` entry ("Karma as physical motion (the Vaisesika padartha)") and its body `**Not:**` line was updated to match. This is a one-file patch to the already-published v0.1 bundle and **must be re-uploaded** (commit to `okf/dharma-foundation/concepts/karma.md`; no new release tag required, or a v0.1.x patch tag if you prefer). Local source of truth: `dharma-okf-main/okf/dharma-foundation/concepts/karma.md`. Re-verify via clone-diff after push.
