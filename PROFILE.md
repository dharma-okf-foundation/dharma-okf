# Dharma-OKF Profile of the Open Knowledge Format

**Profile version:** `dharma-okf/1.0`
**Base specification:** Open Knowledge Format **v0.2**, as specified at
[`GoogleCloudPlatform/knowledge-catalog@3fcbb9f`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/3fcbb9f828c2f23d109c855ee403c3a4c81f3a96/okf/SPEC.md) (`okf/SPEC.md`)
**Status:** Draft · **Date:** 2026-08-05 · **Maintainer:** Dharma OKF Foundation
**Content licence:** CC BY-SA 4.0 (see `LICENSE-CONTENT`)

---

## 0. What this document is

Dharma-OKF is a **profile** of the Open Knowledge Format: it conforms to the base specification without modification, adds a small set of documented extensions, and applies rules stricter than the base in a few places. It does not fork OKF, does not redefine any base field, and does not require changes to OKF to be consumable.

This is the same relationship DCAT-AP holds to W3C DCAT — a domain profile that constrains and extends a general base vocabulary while remaining readable by unmodified base consumers.

**We do not maintain a copy of the base specification.** Earlier revisions of this repository vendored and locally edited upstream's `okf/SPEC.md`, which produced a version-number collision (two different documents both declaring "v0.2") and a recurring merge conflict on a file this project does not own. That practice is retired. The base is cited, never copied.

### Why the base is pinned to a commit, not to `main`

The base specification's own §12 defers the runtime protocol, attester ABI, portability, sandboxing, and attestation caching to future revisions. A profile that tracked `main` would let upstream drift silently change what our bundles claim to be. Re-pinning is therefore a deliberate, dated act, recorded in §7 — not something that happens by itself.

The value of that discipline was demonstrated within two weeks of adopting it. This profile originally pinned `780fe9d`, the commit that introduced OKF v0.2. Two hours later upstream published `3fcbb9f`, which removed the word "(Draft)" from the version line — the same specification, now final rather than provisional. Under a `main`-tracking policy that reclassification would have altered what this profile claimed without anyone deciding anything. Instead it is §7 re-pinning decision **RP-001**, dated and recorded.

> **Reader note (2026-07-28).** `raw.githubusercontent.com` is currently serving a mixed pre-/post-v0.2 state on upstream's `main` branch: `okf/src/reference_agent/bundle/document.py` returns the v0.1 file, while `okf/src/reference_agent/viewer/generator.py` returns the v0.2 file that imports symbols from it. Read the base at the pinned commit, not at `main`.

---

## 1. Conformance to the base

Base §11 defines a conformant bundle as one where every non-reserved `.md` file has a parseable YAML frontmatter block, every frontmatter block has a non-empty `type`, and reserved filenames (`index.md`, `log.md`) follow §8/§9 when present.

**Every Dharma-OKF bundle satisfies base conformance.** Measured across the corpus at this revision: **442 concept documents in 13 bundles** — 310 of `type: Concept` and 132 of `type: Reference` — each carrying parseable frontmatter with a non-empty `type`. Sub-directory `index.md` files are frontmatter-free and use the base §8 bullet form.

Base §4.1 states that producers MAY include additional keys and that consumers MUST NOT reject documents carrying unrecognized fields. Every extension in §2 relies on that guarantee and on nothing else.

### 1.1 A known deviation, disclosed

Bundle-root `index.md` files in this corpus carry a frontmatter block richer than the single `okf_version` key base §8 contemplates (they also carry `type`, `title`, `description`, `version`, `tags`, `resource`, `authors`, `license`). Base §11 does not reject this, and upstream's own reference viewer skips `index.md` entirely when walking a bundle, so it is inert in practice. It is disclosed here rather than quietly relied upon, and is a candidate for simplification in a future profile revision.

---

## 2. Profile extensions

These keys are additions permitted by base §4.1. A base consumer that ignores every one of them still reads a valid, useful bundle; the body prose carries the same content in human-readable form. **None of them redefines or shadows a base field.**

### 2.1 The `not:` field — the profile's reason for existing

```yaml
not:
  - term: "Religion"
    why: "Implies a belief system with founder, book, and creed; Dharma has no founder, predates any text, and is discovered, not converted to."
    instead: "Keep Dharma untranslated; gloss per context (cosmic order, svadharma, inherent nature)."
  - term: "Duty"
    why: "Strips the cosmic and metaphysical dimensions, reducing Dharma to social obligation; duty is imposed, Dharma is inherent."
```

A list of mappings, each naming a specific mistranslation of the concept.

| Key | Requirement | Meaning |
|---|---|---|
| `term` | mandatory | The rejected rendering, quoted as it circulates in the wild. |
| `why` | mandatory | One or two sentences on how the substitution fails — what it imports or strips. |
| `instead` | recommended (mandatory on the first entry) | The positive instruction: what to do in place of the rejected term. |

**Purpose.** These bundles exist because certain Sanskrit terms have no English equivalent, and the substitutes in general circulation carry doctrinal cargo that inverts the source meaning. `not:` is a machine-readable negative constraint: a consuming agent can use it as a prompt-injection guard (via `instead`), a RAG negative filter, or an output check. See `INTEGRATION.md`.

**Body echo.** Every document carrying `not:` also opens its body with a human-readable `**Not:** <term>, <term>, …` line. The frontmatter is the machine surface; the echo keeps the constraint visible to a reader who never parses YAML.

**Applicability.** `not:` is carried by every `type: Concept` document (310 of 310). It is not required on `type: Reference` documents, which describe source texts rather than concepts, and none carry it.

**Provenance.** See §6.

### 2.2 School attribution

| Key | Requirement | Meaning |
|---|---|---|
| `darshana` | mandatory on `Concept` | YAML list. The philosophical school(s) the treatment is drawn from. A term's meaning is school-relative; this records which school's meaning is being given. Carried by 310 of 310 Concepts. |
| `school_scope` | optional | Prose nuance where a list is too blunt — e.g. that a term is cross-darśana in some senses and school-specific in others. |
| `text_source` | optional | Primary textual anchor grounding the `not:` claims (e.g. `YS 2.9`, `Cha. Sha. 1.102`). |

**Why this is not `tags`.** `darshana` is a doctrinal claim with truth conditions, not a categorization convenience. The same term (`karma`, `guṇa`, `kaivalya`, `yoga`) appears in multiple bundles under different schools with genuinely different referents; flattening that into `tags` would erase the distinction these bundles exist to preserve.

### 2.3 Identity and display

| Key | Requirement | Meaning |
|---|---|---|
| `id` | recommended | ASCII slug, stable across renames. |
| `iast` | recommended on `Concept` | IAST transliteration. |
| `devanagari` | recommended on `Concept` | Devanāgarī script form. |
| `bundle`, `bundle_version` | recommended | Owning bundle and its content revision. Distinct from the base `okf_version` and from the git release tag — see §7. |
| `related` | recommended | Bundle-relative paths to sibling concepts. **Advisory only** — see the traversal note in §3.1. |
| `reception_note` | optional | How a term is distorted in contemporary reception, where that distortion is a documented historical construction rather than a simple mistranslation. Used in bundles covering commercially or politically captured vocabulary. |

### 2.4 Reference-document extensions

Carried by `type: Reference` documents describing primary source texts. All optional, applied where meaningful: `language`, `approximate_date`, `period`, `tradition`, `text`, `text_type`, `text_division`, `author`, `key_concepts_in_bundle`.

> `author` here is a top-level key on a Reference document and is unrelated to the base `sources[].author` credibility signal (base §5.1), which appears only inside a `sources` entry.

### 2.5 Per-claim attribution — footnotes keyed to `sources[].id`

Where a body claim rests on a specific source, the profile attributes it with a markdown footnote whose label **is** the `id` of a `sources` entry:

```markdown
Kaivalya is reached through viveka-khyāti, not through nirodha.[^sk-64]

[^sk-64]: Sāṃkhya Kārikā 64
```

```yaml
sources:
  - id: sk-64
    resource: references/samkhya-karika.md
    title: "Sāṃkhya Kārikā"
```

This is base §5.1's mechanism, adopted unchanged. The footnote label is the join key into `sources`; a consumer resolves attribution through the matching entry rather than by parsing the footnote prose.

**Why keyed and not positional.** The base specification gives the reason directly, and it applies with unusual force here: agents rewrite these documents, and *"a positional index misattributes silently the moment the list is reordered, whereas a stable `id` survives reordering."* A corpus whose entire purpose is preventing silent misattribution cannot afford an attribution mechanism that fails silently.

**This is additive, never a replacement.** Adopting `sources` and footnotes does **not** remove the `## Citations` body sections or their links into `references/`. Those body links are the sole source of graph edges for link-graph consumers — `related:` frontmatter is not traversed (§3.1) — so removing them would silently delete the bundle's relationship graph. Base §13.1 explicitly permits a consumer to keep parsing a legacy `# Citations` list, so nothing requires the deletion. **Frontmatter `sources` and body citation links coexist; the footnote is a third layer over both.**

Adoption is staged with the trust and provenance families (§5, Level 3), since `sources[].id` is what a footnote binds to.

---

## 3. Rules stricter than the base

A profile may constrain what the base permits. These are the constraints.

### 3.1 Link form: relative, not absolute

**Base §6.1 recommends** the bundle-relative absolute form (`/concepts/karma.md`) "because it is stable when documents are moved within their subdirectory."

**This profile requires the relative form** (`../concepts/karma.md`, `./karma.md`) in document bodies.

This is a deliberate divergence from the base's recommendation, and it is a **workaround, not a preference**. Upstream's reference viewer discards absolute-form links when building its graph:

```python
# okf/src/reference_agent/viewer/generator.py :: _extract_links
if "://" in target or target.startswith("/"):
    continue
```

A bundle authored exactly as base §6.1 advises therefore renders with no edges between its concepts. Since the profile's value depends on the relationship graph being visible to consumers, the profile follows the implementation rather than the recommendation, and discloses that it is doing so. This rule will be revisited if upstream resolves the discrepancy in either direction.

**Traversal note for consumers.** The `related:` key (§2.3) is frontmatter and is **not** traversed by link-graph consumers, which read bodies only. Every relationship asserted in `related:` is also expressed as a body link. Consumers building a graph should read bodies; `related:` is a convenience for readers and profile-aware tools.

### 3.2 A `references/` sub-bundle is required

Base §6.3 makes `references/` a convention. This profile makes it a requirement: every bundle carries a `references/` sub-bundle in which each cited primary text is a first-class `type: Reference` document, so citations are traversable inside the bundle rather than being dead prose. Present in 13 of 13 bundles (132 Reference documents).

### 3.3 Human verification is required for published concepts

See §5, Level 3. A Dharma-OKF concept asserts doctrinal content; the profile requires that a human tradition-bearer has confirmed it, recorded as `verified: { by: human:<id>, at: <date> }` (base §5.2). Machine-only verification does not satisfy this profile, though it satisfies the base.

This is the profile's strictest rule and the one it most cares about. Base §5.3 derives a trust tier from `verified`, and a `human:` actor yields the `human-reviewed` tier. Rendered in frontmatter, that field carries the claim a transmitted tradition has always made: a person who holds the teaching has checked it.

**Corollary, binding on tooling.** Automated tooling operating on this corpus MAY write `generated:`. It MUST NOT write `verified:`. That field records a human review event and is produced by nothing else. A rewriter that stamps `verified:` while reformatting YAML does not merely misuse a field — it converts the profile's central trust claim into noise, asserting that a person checked documents no person checked.

### 3.4 Progressive disclosure — an `index.md` in every directory

Base §8 says an `index.md` **MAY** appear in any directory. This profile requires one in **every** directory containing concept documents, using the base §8 form: no frontmatter, sections of `* [Title](file) - description.` bullets.

The reason is the corpus's primary consumer. An agent traversing a bundle one level at a time cannot see what a directory holds without an index; it must either load every file or guess. For a 442-document corpus intended for context-window-bounded consumption, progressive disclosure is not a nicety.

**Measured state at this revision: 18 of 39 directories carry an `index.md`; 21 do not.** Every `concepts/` directory in all thirteen bundles is missing one, as are the `references/` directories in the eight bundles from `upanishadic-core` forward. The five earliest bundles carry `references/index.md` but not `concepts/index.md`.

Bundle-root `index.md` files exist in all thirteen bundles and enumerate their concepts, so the corpus is navigable — but only from the root, in one hop, with no intermediate listing. Scheduled with the normalization work in §5.

> Verified clean: **no sub-directory `index.md` carries frontmatter.** The frontmatter deviation disclosed in §1.1 is confined to the thirteen bundle-root indexes.

---

## 4. Base features declined, with reasons

A profile is as much what it refuses as what it adds. These base features are deliberately unused. Their absence is meaningful and should not be read as incompleteness.

### 4.1 `stale_after` — declined

Base §5.5 marks a concept stale on a given date. Upstream's own worked example ties it to a review cadence: `acme_retail` sets `stale_after: 2026-12-31` because "the cost-allocation standard is reviewed annually."

**A non-translatable has no review cadence.** The meaning of *ṛta* is not scheduled for revision in Q4. Setting a date would assert a freshness claim this project cannot honour; setting a far-future date would be theatre. Base behaviour makes the omission correct rather than merely acceptable — `is_stale()` returns `False` when the key is absent, so Dharma-OKF concepts report as never-stale, which is the accurate answer.

Corrections to a concept are handled as content revisions (`bundle_version` patch bump + `CHANGELOG.md`), not as expiry. See `VERSIONING.md`.

### 4.2 Attested Computation — not applicable

Base §10 defines `type: Attested Computation` with `runtime`, `parameters`, `computation`, `executor`, and `attester`, so a consumer can confirm a number was produced by a sanctioned computation. Dharma-OKF publishes vocabulary, not computed values. Nothing in this corpus is executable and no concept resolves to a figure. The family is unused in full.

### 4.3 `resource` — largely unused

Base §4.1 recommends `resource` as a URI for the underlying asset a concept describes. Dharma-OKF concepts describe ideas rather than resolvable assets; base §4.1 explicitly contemplates this ("absent for concepts that describe abstract ideas"). `Reference` documents describing published texts are the natural place for it and may adopt it in a future revision.

---

## 5. Conformance levels and current coverage

Conformance is stated as levels, each independently checkable, with the corpus's actual position at this revision. **This table is the honest state of the corpus, not an aspiration.** It is updated with each wave and is machine-checkable (§8).

| Level | Requirement | Bundles conformant |
|---|---|---|
| **0 — Base** | Satisfies base §11 (parseable frontmatter, non-empty `type`, §8/§9 reserved files) | **13 / 13** |
| **1 — Profile core** | Every `Concept` carries `not:` and `darshana:`; a `references/` sub-bundle is present (§2.1, §2.2, §3.2) | **13 / 13** |
| **2 — Graph interoperable** | Body links use the relative form only (§3.1) | **8 / 13** |
| **2b — Progressive disclosure** | Every directory holding concepts carries a base §8 `index.md` (§3.4) | **0 / 13** |
| **3 — Trust and provenance** | `generated:`, `verified: { by: human:… }`, `sources:` with footnote attribution, and `okf_profile:` present on every document (§2.5, §3.3) | **0 / 13** |

**Level 2 gap (5 bundles, 400 links).** `dharma-foundation` (136 absolute links of 183), `vedanta-epistemology` (89), `yoga-darshana` (84), `bhakti-marga` (46), `dharmic-ethics` (45). All five predate the convention change at `upanishadic-core`; every bundle from that point on is already Level 2. Scheduled for a dedicated normalization wave.

**Level 2b gap (13 bundles, 21 directories).** No bundle is yet complete. The two gaps are inversely distributed — the five oldest bundles have `references/index.md` but absolute links; the eight newest have relative links but no sub-directory indexes. Both are mechanical and are scheduled together in the normalization wave, since they touch the same five-versus-eight split from opposite directions.

**Level 3 gap (all 13).** The trust and provenance families are adopted by this profile revision and applied bundle-by-bundle on the publication cadence, beginning with a single pilot bundle gated on a rendering and round-trip acceptance test. Until a bundle reaches Level 3, its documents carry the legacy `timestamp` key, which base §13.1 permits consumers to fall back to.

**Verifier identity.** This profile's human verifier actor is `human:sanjay@dharmaokf.foundation`. The domain-qualified form is used deliberately: these documents are intended for third-party ingestion and citation, and a bare local identifier would be permanently ambiguous outside this repository.

---

## 6. Provenance of the `not:` field

Recorded to the standard this project applies to error genealogies elsewhere (`GENEALOGIES.md`): named source, date, chain, and evidence a reader can verify without trusting this document.

### The sequence

The `not:` field with its `term` / `why` / `instead` structure, and the accompanying `**Not:**` body-echo convention, were defined in this project's canonical concept template on **2026-06-24** and published in the `dharma-foundation` bundle on **2026-06-18** (structured form ratified 2026-06-24).

### The evidence upstream

`not:` is **not part of the base specification** and appears nowhere in `SPEC.md`. It appears in upstream's sample bundle, in two independent places.

**1. The commit message.** Commit [`780fe9d30b5bbca8931256edf1d0290d6bda5462`](https://github.com/GoogleCloudPlatform/knowledge-catalog/commit/780fe9d30b5bbca8931256edf1d0290d6bda5462), 2026-07-24, describes the new `acme_retail` bundle verbatim as:

> Structured to match conventions observed in public OKF bundles (kebab-case markdown filenames, top-level domain dirs, **dharma-style not: field on gross-margin**, saschb2b-style # Cited by on policy references).

**2. The file itself.** `okf/bundles/acme_retail/metrics/gross-margin.md` carries the full three-key structure and the body echo:

    not:
      - term: "revenue minus product cost only"
        why: "that is the pre-FY2026 definition (see gross-margin-legacy)…"
        instead: "revenue minus full COGS (product cost + inbound fulfillment + …)"

### Why this cites a commit hash rather than a pull request

**Verified 2026-08-05:** commit `780fe9d` is served by multiple independent repositories — confirmed at `GoogleCloudPlatform/knowledge-catalog`, `inematds/okf`, and `Kosaki-1AE/KQI`. Repositories in a GitHub fork network share a git object store, so a content-addressed hash resolves at any member. If the origin repository were renamed, relocated or deleted, the object would persist.

A pull-request URL does not. Upstream's own `toolbox/mdcode/demo/README.md` already references the format as `github.com/google/okf`, a repository that does not presently resolve — so a relocation appears to be contemplated. Were it to happen, a `/pull/227` link would break while the hash would not. **Cite the hash.**

### What this note does and does not claim

It records a sequence and points at verifiable artifacts. It asserts **no ownership of the field, no priority claim requiring anyone's acknowledgement, and no obligation on any party.** `not:` is offered as a profile extension that any producer may adopt freely, and this project would welcome its standardization in a future base revision.

---

## 7. Versioning

Four independent axes. Conflating them has caused real confusion in this project's history and the distinction is load-bearing.

| Axis | Key | Meaning |
|---|---|---|
| Base format | `okf_version: "0.2"` | The **upstream** specification version this document targets, at the commit pinned above. Not a Dharma-OKF version. |
| Profile | `okf_profile: "dharma-okf/1.0"` | This profile's version. |
| Bundle content | `bundle_version` | A bundle's content revision. Patch-bumped on enrichment; see `VERSIONING.md`. |
| Release | git tag (`v0.13.0`) | Per-bundle immutable snapshot. `main` is the living vocabulary; tags are frozen. |

**Re-pinning the base.** Moving to a newer base revision is a deliberate, dated decision recorded in `CHANGELOG.md` — never automatic, and never a silent follow of `main`. A base minor bump does not oblige a profile revision; a profile revision does not oblige a base re-pin.

### Re-pinning log

| ID | Date | From → To | Reason |
|---|---|---|---|
| **RP-001** | 2026-08-05 | `780fe9d` → [`3fcbb9f`](https://github.com/GoogleCloudPlatform/knowledge-catalog/commit/3fcbb9f828c2f23d109c855ee403c3a4c81f3a96) | Upstream removed "(Draft)" from the OKF v0.2 version line. Specification text otherwise unchanged — a one-line reclassification from provisional to final. Verified: `git diff 780fe9d..3fcbb9f -- okf/SPEC.md` is that single line. No profile rule is affected; no bundle requires revision. |

**Upstream state at RP-001.** Two further commits exist on upstream `main` (`599a240`, `930b65f`, both 2026-08-04), confined to `toolbox/mdcode` — Semantic Model IR and BigQuery property-graph DDL. Neither touches `okf/SPEC.md` nor the reference viewer, so the §3.1 link-handling divergence stands unresolved as of this pin.

**Watch item.** Upstream's `toolbox/mdcode/demo/README.md` references the format as `github.com/google/okf`, a repository that does not presently resolve. If the base specification relocates, the citation in this document is updated as a §7 re-pinning decision.

---

## 8. Validation

Profile conformance is machine-checkable, not merely asserted. A profile whose rules cannot be tested is a preference.

`okf/tools/okf_validate.py` checks bundle integrity and link resolution today. It is being extended into a two-layer checker that reports **base conformance** (§1) and **profile conformance** (§5 levels 1–3) separately, so a consumer can tell "this is not OKF" from "this is OKF but not this profile."

Base consumers need none of this. A bundle that fails every profile rule in §3 is still a conformant OKF bundle under base §11, and will still load, render, and be useful. That is the point of profiling rather than forking.

---

## 9. For consumers

- **If you consume plain OKF:** ignore this document. The bundles are base-conformant; unknown keys are safe to skip per base §4.1, and the body prose carries the same content.
- **If you want the anti-mistranslation constraints:** read `not:` from frontmatter and apply it as a negative filter or prompt constraint. `INTEGRATION.md` has worked patterns.
- **If you are building a profile of your own:** this document's shape — conformance claim, extensions, stricter rules, declinations, coverage table — is freely reusable. The corpus is CC BY-SA 4.0.

---

*Dharma OKF Foundation · profile `dharma-okf/1.0` · base OKF v0.2 @ `3fcbb9f` · re-pinned 2026-08-05 (RP-001)*
