#!/usr/bin/env python3
"""OKF bundle validator.

Validates an OKF bundle (a directory tree of markdown-with-frontmatter files)
against OKF v0.1 conformance plus the optional v0.2 conventions proposed for the
Dharma-OKF bundle (`darshana:` attribution and the structured `not:` field).

Design goals:
  * Zero hard dependencies beyond PyYAML.
  * Reuses the canonical parser (`enrichment_agent.bundle.document.OKFDocument`)
    when it is importable; otherwise falls back to an equivalent local parser.
  * Three severity levels — FAIL (breaks conformance), WARN (bundle guidance),
    INFO (nice-to-have) — and a non-zero exit code only when a FAIL is found.

Usage:
    python okf_validate.py [BUNDLE_DIR]
        [--require-section "What It Actually Means" ...]
        [--require-darshana] [--require-structured-not]
        [--strict]      # treat WARN as failing too
        [--fix]         # rewrite each body "**Not:**" line from frontmatter
        [--quiet]

Defaults to validating ../dharma-foundation relative to this file, with the
dharma bundle's conventional sections and v0.2 rules enabled.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json as _json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.stderr.write("PyYAML is required: pip install pyyaml\n")
    raise

# --- canonical parser, with a local fallback -------------------------------
try:  # reuse the repo's parser if the package is importable
    _here = Path(__file__).resolve()
    _src = _here.parent.parent / "src"
    if str(_src) not in sys.path:
        sys.path.insert(0, str(_src))
    from enrichment_agent.bundle.document import OKFDocument  # type: ignore
except Exception:  # pragma: no cover - fallback keeps the tool standalone
    @dataclass
    class OKFDocument:  # type: ignore[no-redef]
        frontmatter: dict[str, Any] = field(default_factory=dict)
        body: str = ""

        @classmethod
        def parse(cls, text: str) -> "OKFDocument":
            lines = text.splitlines()
            if not lines or lines[0].strip() != "---":
                return cls({}, text)
            end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
            if end is None:
                raise ValueError("Unterminated YAML frontmatter block")
            fm = yaml.safe_load("\n".join(lines[1:end])) or {}
            if not isinstance(fm, dict):
                raise ValueError("Frontmatter must be a YAML mapping")
            body = "\n".join(lines[end + 1:])
            return cls(fm, body[1:] if body.startswith("\n") else body)


RESERVED = {"index.md", "log.md"}
DEFAULT_SECTIONS = ["What It Actually Means", "Audience Metaphor", "Citations"]
# Legacy scholarly body format (decision 2026-07-14, Traceable-Guardrail
# Enrichment Pass wave 1, zero-content-churn ruling): these five bundles
# predate the canonical body template. Their definitional content lives in
# named scholarly sections (Etymology, per-text Definition headings, source
# analyses) rather than under the literal 'What It Actually Means' heading.
# For files in these bundles that one heading requirement is waived;
# 'Audience Metaphor' and 'Citations' remain required. Bundles authored after
# the canonical template (v0.8+) and all future bundles MUST carry the
# canonical heading and are NOT in this set.
LEGACY_BODY_FORMAT_BUNDLES = frozenset({
    "yoga-darshana", "vedanta-epistemology", "bhakti-marga",
    "upanishadic-core", "cosmology-creation",
})
LEGACY_WAIVED_SECTION = "What It Actually Means"
RECOMMENDED_KEYS = ("title", "description", "timestamp")
_ISO_DT = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")
_BODY_NOT = re.compile(r"^\*\*Not:\*\*\s*(.+)$", re.M)
_INLINE_LINK = re.compile(r"\]\((/[^)]+\.md|\.{1,2}/[^)]+\.md)\)")
# Bare-relative body links like `](foo.md)` or `](concepts/foo.md)` — first char
# is not `/`, `.`, whitespace or `)`. The validator previously ignored these, so
# draft id-typos in cross-reference prose slipped through (the vedanta defect).
_BARE_LINK = re.compile(r"\]\(([^/.\s)][^)\s]*\.md)\)")
# Any non-ASCII codepoint — slugs/filenames/link paths must stay ASCII for URL
# portability (a non-ASCII filename broke the fetch tooling on vedanta).
_NONASCII = re.compile(r"[^\x00-\x7f]")
PROFILE_CHECKER_VERSION = "2.2"
PROFILE_ID = "dharma-okf/1.0"


# --- severity bookkeeping --------------------------------------------------
@dataclass
class Report:
    fails: list[str] = field(default_factory=list)
    warns: list[str] = field(default_factory=list)
    infos: list[str] = field(default_factory=list)

    def fail(self, where: str, msg: str) -> None: self.fails.append(f"{where}: {msg}")
    def warn(self, where: str, msg: str) -> None: self.warns.append(f"{where}: {msg}")
    def info(self, where: str, msg: str) -> None: self.infos.append(f"{where}: {msg}")


def split_top_level_commas(s: str) -> list[str]:
    """Split on commas that are NOT inside parentheses or quotes.

    This is the fix for the false positive seen during the audit, where a comma
    inside a parenthetical ('... mokṣa, not a synonym') was wrongly counted as a
    list separator.
    """
    out, buf, depth = [], [], 0
    quote = None
    for i, ch in enumerate(s):
        if quote:
            # An apostrophe followed by a letter (Brahman's) is possessive, not
            # a closing quote (wave-2 tokenizer fix, 2026-07-14).
            if ch == quote and not (ch == "'" and i + 1 < len(s) and s[i + 1].isalpha()):
                quote = None
            buf.append(ch)
        elif ch in "\"'":
            # An apostrophe attached to a preceding letter is part of the word
            # (possessive/elision), never an opening quote.
            if ch == "'" and i > 0 and s[i - 1].isalpha():
                buf.append(ch)
            else:
                quote = ch; buf.append(ch)
        elif ch in "([{":
            depth += 1; buf.append(ch)
        elif ch in ")]}":
            depth = max(0, depth - 1); buf.append(ch)
        elif ch == "," and depth == 0:
            out.append("".join(buf).strip()); buf = []
        else:
            buf.append(ch)
    if buf:
        out.append("".join(buf).strip())
    return [x for x in out if x]


def not_terms(fm_not: Any) -> list[str]:
    """Extract the term list from a v0.1 (strings) or v0.2 (mappings) `not:`."""
    terms = []
    for item in fm_not or []:
        if isinstance(item, str):
            terms.append(item)
        elif isinstance(item, dict) and "term" in item:
            terms.append(str(item["term"]))
    return terms


def render_not_line(terms: list[str]) -> str:
    return "**Not:** " + ", ".join(terms)


def concept_ids(bundle: Path) -> set[str]:
    ids = set()
    for p in bundle.rglob("*.md"):
        if p.name in RESERVED:
            continue
        ids.add("/".join(p.relative_to(bundle).with_suffix("").parts))
    return ids


def resolve_link(link: str, concept_path: Path, bundle: Path) -> bool:
    raw = link.split("#", 1)[0]
    if raw.startswith("/"):
        target = (bundle / raw.lstrip("/")).resolve()
    else:
        target = (concept_path.parent / raw).resolve()
    return target.exists()


def _escapes_bundle(link: str, concept_path: Path, bundle: Path) -> bool:
    """True if a resolvable link lands OUTSIDE the bundle root.

    resolve_link() asks only whether the target exists on disk. Upstream's
    fixed `_extract_links` takes a `bundle_root` and rejects paths that escape
    it (open-knowledge-format#14, acceptance criterion 5), so a link this
    checker passes can still be dropped by a base-conformant resolver.
    Reported, never scored: the profile permits these and discloses them
    (PROFILE.md §3.1). Counting them is how the disclosure stays true.
    """
    raw = link.split("#", 1)[0]
    if raw.startswith("/"):
        return False
    try:
        target = (concept_path.parent / raw).resolve()
        target.relative_to(bundle.resolve())
    except ValueError:
        return True
    except OSError:
        return False
    return False


def validate(bundle: Path, *, sections: list[str], require_darshana: bool,
             require_structured_not: bool, fix: bool) -> Report:
    rep = Report()
    _ = concept_ids(bundle)

    for path in sorted(bundle.rglob("*.md")):
        where = str(path.relative_to(bundle))
        if path.name in RESERVED:
            continue
        # --- WARN: ASCII slug (filename) -------------------------------
        if _NONASCII.search(path.name):
            rep.warn(where, f"non-ASCII filename (slug must be ASCII): {path.name}")
        text = path.read_text(encoding="utf-8")

        # --- FAIL: parseable frontmatter --------------------------------
        try:
            doc = OKFDocument.parse(text)
        except Exception as e:
            rep.fail(where, f"unparseable frontmatter ({e})")
            continue
        fm, body = doc.frontmatter, doc.body
        if not fm:
            rep.fail(where, "no frontmatter block")
            continue

        # --- FAIL: type present (SPEC §9) -------------------------------
        if not fm.get("type"):
            rep.fail(where, "missing/empty required field: type")

        # --- FAIL: structured not entries must carry a term ------------
        nf = fm.get("not")
        if isinstance(nf, list):
            for i, item in enumerate(nf):
                if isinstance(item, dict) and not item.get("term"):
                    rep.fail(where, f"not[{i}] mapping missing 'term'")
        elif nf is not None:
            rep.fail(where, "'not' must be a list")

        # --- WARN: recommended frontmatter keys ------------------------
        for k in RECOMMENDED_KEYS:
            if not fm.get(k):
                rep.warn(where, f"missing recommended field: {k}")

        # --- WARN: darshana presence (v0.2) — concepts only ------------
        if require_darshana and fm.get("type") == "Concept" and not fm.get("darshana"):
            rep.warn(where, "missing 'darshana' (school attribution)")

        # --- WARN: structured not + why (v0.2) -------------------------
        if isinstance(nf, list):
            for i, item in enumerate(nf):
                if require_structured_not and not isinstance(item, dict):
                    rep.warn(where, f"not[{i}] is a bare string; expected term/why mapping")
                elif isinstance(item, dict) and not item.get("why"):
                    rep.warn(where, f"not[{i}] ('{item.get('term')}') has no 'why'")

        # --- WARN/FIX: body **Not:** line parity -----------------------
        fm_terms = not_terms(nf)
        m = _BODY_NOT.search(body)
        if fm_terms:
            if not m:
                rep.warn(where, "no '**Not:**' summary line in body")
                if fix:
                    body = _inject_not_line(body, render_not_line(fm_terms))
            else:
                body_terms = split_top_level_commas(m.group(1))
                # Count-based parity: the body line is a human-readable echo, so we
                # check coverage (same number of terms) rather than exact wording.
                if len(body_terms) != len(fm_terms):
                    rep.warn(where, f"body Not: line has {len(body_terms)} terms "
                                    f"!= frontmatter not: {len(fm_terms)}")
                    if fix:
                        body = body[:m.start()] + render_not_line(fm_terms) + body[m.end():]

        # --- WARN: required conventional sections (concepts only) ------
        if fm.get("type") == "Concept":
            legacy = bundle.resolve().name in LEGACY_BODY_FORMAT_BUNDLES
            for sec in sections:
                if legacy and sec == LEGACY_WAIVED_SECTION:
                    continue
                if not re.search(rf"^#+\s+{re.escape(sec)}\s*$", body, re.M):
                    rep.warn(where, f"missing section: '{sec}'")

        # --- WARN: link resolution (incl. bare-relative body links) ----
        # The validator historically checked only /-rooted and ./ ../ links.
        # Bare-relative sibling links (e.g. `](mithya.md)`) and non-ASCII link
        # paths now get checked too — these were the two classes that slipped
        # past the frontmatter-level checks during the vedanta v0.3.0 upload.
        bare = [l for l in _BARE_LINK.findall(body) if "://" not in l]
        targets = list(fm.get("related") or []) + list(_INLINE_LINK.findall(body)) + bare
        for link in targets:
            if not resolve_link(link, path, bundle):
                rep.warn(where, f"unresolved link: {link}")
            if _NONASCII.search(link):
                rep.warn(where, f"non-ASCII path in link: {link}")

        # --- INFO: niceties --------------------------------------------
        ts = str(fm.get("timestamp", ""))
        if ts and not _ISO_DT.match(ts):
            rep.info(where, f"timestamp is date-only, not full ISO 8601 datetime: {ts}")
        if fm.get("type") == "Concept":
            rep.info(where, "generic type 'Concept' — consider a descriptive subtype")

        if fix:
            new_text = _reserialize(text, body)
            if new_text != text:
                path.write_text(new_text, encoding="utf-8")

    return rep



# ===========================================================================
# LAYER 2 — PROFILE CONFORMANCE (dharma-okf/1.0)
# ---------------------------------------------------------------------------
# Answers PROFILE.md §8: report BASE conformance (§1) and PROFILE conformance
# (§5 levels 0-3) SEPARATELY, so a consumer can tell "this is not OKF" from
# "this is OKF but not this profile."
#
# Layer 1 is validate() above. It is deliberately UNCHANGED: okf/tests/ asserts
# zero FAIL findings per bundle, and folding profile rules into it would make
# all 13 bundles fail --strict. The layers must be independently checkable,
# which is the thing §8 asks for.
#
# Three rules Layer 1 does not have:
#   R1  link FORM (§3.1)          — bundle-absolute body links
#   R2  citation INTEGRITY        — bracket-only [x.md] and bare-path forms
#   R3  index.md PRESENCE (§3.4)  — every dir holding concepts needs one
# ===========================================================================

_MD_LINK       = re.compile(r"\]\(([^)]+)\)")
_PSEUDO_LINK   = re.compile(r"\[[^\]]*\.md\](?!\()")
_BARE_PATH     = re.compile(r"(?<![(\[/\w.-])((?:\.\./)?(?:references|concepts)/[a-z0-9._-]+\.md)")
_FM_BLOCK      = re.compile(r"^---\n(.*?)\n---\n", re.S)


def _split_doc(text: str) -> tuple[str, str]:
    """Return (frontmatter, body). Empty frontmatter if the block is absent."""
    m = _FM_BLOCK.match(text)
    return (m.group(1), text[m.end():]) if m else ("", text)


def _body_links(body: str) -> list[str]:
    """Markdown link targets, excluding external URLs and pure anchors."""
    return [t for t in _MD_LINK.findall(body)
            if "://" not in t and not t.startswith("#")]


def _related_entries(fm: str) -> list[str]:
    """Every `related:` list item, whether or not the list is indented.

    The original pattern required `\\s+-\\s`, i.e. an INDENTED item. 124 of the
    322 files carrying `related:` write the list flush against the margin —
    valid YAML, and invisible to that pattern. Five bundles reported zero
    entries while carrying 425 between them. Corrected 2026-09-06; the total
    moved 1,074 -> 1,499. Scoring never depended on this (Finding C is
    reported, never scored), but the normalize-or-amend decision did.
    """
    m = re.search(r"^related:[ \t]*\n((?:[ \t]*-[ \t].*\n)+)", fm, re.M)
    return re.findall(r"-\s*(\S+)", m.group(1)) if m else []


# --- Level 3: trust and provenance (PROFILE.md §5, §2.5, §3.3) -------------
#
# Until 2026-09-10 this module did not measure Level 3 at all. It returned the
# constant `"level_3": False`, and two tests asserted that constant against
# itself. The consequence was proved, not assumed: 21 dharmic-ethics documents
# were given all four families in a scratch clone, and the coverage table still
# read L3 0/13 while the whole suite passed. A conformance table cannot be
# "generated, not maintained" (§5) while one of its rows is a literal.
#
# GATED, because §5 names exactly these four:
#   generated:        present
#   verified:         present, with at least one `human:` actor (§3.3 makes
#                     machine-only verification insufficient for this profile)
#   sources:          present and non-empty
#   okf_profile:      present
#
# REPORTED, NOT GATED, following this module's existing split (escaping links
# and `related:` form are reported and never scored):
#   generated.by absent            base §5.2 makes it REQUIRED within generated
#   `at` not an ISO 8601 datetime  base §5 preamble requires an explicit offset.
#                                  PROFILE §3.3 wrote `<date>` until 2026-09-11
#                                  and now states the base form; this check was
#                                  written against the base either way
#   sources[] entry with no resource   base §5.1 makes it REQUIRED within an entry
#   footnote label matching no sources[].id   §2.5's join key, silently broken
#   okf_profile value mismatch
#
# Footnotes are NOT gated. §2.5 is conditional ("Where a body claim rests on a
# specific source"), so a document with no such claim is conformant without one.
# Gating on them would invent a rule §5 does not state.

_HUMAN_ACTOR = re.compile(r"^human:\S")
_ISO_DT = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$")
_FOOTNOTE_DEF = re.compile(r"^\[\^([^\]]+)\]:", re.M)
TRUST_FAMILIES = ("generated", "verified", "sources", "okf_profile")


def _parse_fm(fm: str) -> dict:
    """Frontmatter as a mapping. Unparseable frontmatter scores as empty."""
    try:
        d = yaml.safe_load(fm)
    except Exception:
        return {}
    return d if isinstance(d, dict) else {}


def _verified_events(v: Any) -> list[dict]:
    """base §5.2: a list of {by, at}; a bare mapping is a one-element list."""
    if isinstance(v, dict):
        return [v]
    if isinstance(v, list):
        return [e for e in v if isinstance(e, dict)]
    return []


def trust_check(fm_text: str, body: str) -> tuple[set, list[str]]:
    """One document against §5 Level 3. Returns (families_present, findings)."""
    fm = _parse_fm(fm_text)
    present: set = set()
    findings: list[str] = []

    gen = fm.get("generated")
    if gen is not None:
        present.add("generated")
        if not isinstance(gen, dict) or not str(gen.get("by") or "").strip():
            findings.append("generated.by absent (base §5.2 REQUIRED)")
        at = str(gen.get("at") or "") if isinstance(gen, dict) else ""
        if at and not _ISO_DT.match(at):
            findings.append(f"generated.at is not an ISO 8601 datetime: {at}")

    events = _verified_events(fm.get("verified"))
    if events:
        if any(_HUMAN_ACTOR.match(str(e.get("by") or "")) for e in events):
            present.add("verified")
        else:
            findings.append("verified carries no human: actor (§3.3)")
        for e in events:
            at = str(e.get("at") or "")
            if at and not _ISO_DT.match(at):
                findings.append(f"verified.at is not an ISO 8601 datetime: {at}")

    src = fm.get("sources")
    ids: set = set()
    if isinstance(src, list) and src:
        present.add("sources")
        for i, s in enumerate(src):
            if not isinstance(s, dict) or not str(s.get("resource") or "").strip():
                findings.append(f"sources[{i}] has no resource (base §5.1 REQUIRED)")
            elif s.get("id"):
                ids.add(str(s["id"]))

    prof = fm.get("okf_profile")
    if prof is not None:
        present.add("okf_profile")
        if str(prof) != PROFILE_ID:
            findings.append(f'okf_profile is "{prof}", expected "{PROFILE_ID}"')

    for label in sorted(set(_FOOTNOTE_DEF.findall(body)) - ids):
        findings.append(f"footnote [^{label}] matches no sources[].id (§2.5)")

    return present, findings


def profile_check(bundle: Path) -> dict:
    """Score one bundle against PROFILE.md §5. Detection only; changes nothing."""
    name = bundle.name
    concepts = references = 0
    rel = absolute = pseudo = bare = 0
    related_abs = related_rel = 0
    no_link_concepts: list[str] = []
    unresolved: list[str] = []
    escaping: list[str] = []
    dirs_with_concepts: set[Path] = set()
    fm_in_subindex: list[str] = []
    trust_docs = 0
    trust_have = {f: 0 for f in TRUST_FAMILIES}
    trust_complete = 0
    trust_findings: list[str] = []

    for path in sorted(bundle.rglob("*.md")):
        if path.name in RESERVED:
            # §3.4: sub-directory indexes must be frontmatter-free (root exempt, §1.1)
            if path.name == "index.md" and path.parent != bundle:
                if _FM_BLOCK.match(path.read_text(encoding="utf-8")):
                    fm_in_subindex.append(str(path.relative_to(bundle)))
            continue

        text = path.read_text(encoding="utf-8")
        fm, body = _split_doc(text)
        m = re.search(r"^type:\s*(.+)$", fm, re.M)
        doctype = m.group(1).strip().strip("\"'") if m else ""
        if doctype == "Concept":
            concepts += 1
        elif doctype == "Reference":
            references += 1
        else:
            continue

        dirs_with_concepts.add(path.parent)
        where = str(path.relative_to(bundle))

        # --- Level 3: trust and provenance ---------------------------------
        trust_docs += 1
        present, tf = trust_check(fm, body)
        for fam in present:
            trust_have[fam] += 1
        if len(present) == len(TRUST_FAMILIES):
            trust_complete += 1
        trust_findings.extend(f"{where}: {m}" for m in tf)

        # --- R1: link form -------------------------------------------------
        links = _body_links(body)
        n_abs = sum(1 for t in links if t.startswith("/"))
        absolute += n_abs
        rel += len(links) - n_abs

        for t in links:
            if not resolve_link(t, path, bundle):
                unresolved.append(f"{where}: {t}")
            elif _escapes_bundle(t, path, bundle):
                escaping.append(f"{where}: {t}")

        # --- R2: citation integrity ---------------------------------------
        pseudo += len(_PSEUDO_LINK.findall(body))
        for mm in _BARE_PATH.finditer(body):
            if body[mm.start() - 1: mm.start()] not in "([":
                bare += 1

        # --- Level 2 presence floor ---------------------------------------
        if doctype == "Concept" and not links:
            no_link_concepts.append(where)

        # --- Finding C: related: form (reported, never scored) -------------
        for t in _related_entries(fm):
            if t.startswith("/"):
                related_abs += 1
            else:
                related_rel += 1

    missing_index = sorted(str(d.relative_to(bundle)) or "."
                           for d in dirs_with_concepts
                           if not (d / "index.md").exists())

    # ---- level scoring ----------------------------------------------------
    l2_failures = []
    if absolute:
        l2_failures.append(f"form: {absolute} bundle-absolute body link(s) (§3.1)")
    if no_link_concepts:
        l2_failures.append(
            f"presence: {len(no_link_concepts)} concept(s) with no resolvable body link")
    if pseudo:
        l2_failures.append(f"integrity: {pseudo} bracket-only pseudo-link(s)")
    if bare:
        l2_failures.append(f"integrity: {bare} bare-path citation(s)")

    l3_failures = []
    for fam in TRUST_FAMILIES:
        n = trust_have[fam]
        if n < trust_docs:
            label = "verified (human:)" if fam == "verified" else fam
            l3_failures.append(f"{label}: absent on {trust_docs - n} of {trust_docs} document(s)")
    if trust_docs == 0:
        l3_failures.append("no Concept or Reference documents to score")

    return {
        "bundle": name,
        "level_0": True,          # base conformance is Layer 1's verdict
        "level_1": True,          # not: + darshana + references/ — Layer 1 WARNs cover it
        "level_2": not l2_failures,
        "level_2b": not missing_index,
        "level_3": trust_docs > 0 and not l3_failures,
        "concepts": concepts,
        "references": references,
        "links": {
            "relative": rel,
            "absolute": absolute,
            "pseudo": pseudo,
            "bare_path": bare,
            "unresolved": len(unresolved),
            "escaping": len(escaping),
            "concepts_without_links": len(no_link_concepts),
            "related_absolute": related_abs,
            "related_relative": related_rel,
        },
        "indexes": {
            "dirs_with_concepts": len(dirs_with_concepts),
            "dirs_missing_index": len(missing_index),
            "missing": missing_index,
            "subindex_with_frontmatter": fm_in_subindex,
        },
        "level_2_failures": l2_failures,
        "level_3_failures": l3_failures,
        "trust": {
            "documents": trust_docs,
            "complete": trust_complete,
            **{f"has_{f}": trust_have[f] for f in TRUST_FAMILIES},
            "findings": len(trust_findings),
        },
        "detail": {
            "concepts_without_links": no_link_concepts[:20],
            "unresolved_links": unresolved[:20],
            "escaping_links": escaping[:40],
            "trust_findings": trust_findings[:40],
        },
    }


def profile_report(results: list[dict]) -> dict:
    """Aggregate per-bundle results into the §5 coverage table."""
    lv = {k: sum(1 for r in results if r[f"level_{k}"])
          for k in ("0", "1", "2", "2b", "3")}
    return {
        "generated": _dt.datetime.now(_dt.timezone.utc)
                        .replace(microsecond=0).isoformat(),
        "checker_version": PROFILE_CHECKER_VERSION,
        "profile": "dharma-okf/1.0",
        "corpus": {
            "bundles": len(results),
            "concepts": sum(r["concepts"] for r in results),
            "references": sum(r["references"] for r in results),
            "documents": sum(r["concepts"] + r["references"] for r in results),
        },
        "levels": lv,
        "totals": {
            "absolute_links": sum(r["links"]["absolute"] for r in results),
            "relative_links": sum(r["links"]["relative"] for r in results),
            "pseudo_links": sum(r["links"]["pseudo"] for r in results),
            "bare_path": sum(r["links"]["bare_path"] for r in results),
            "concepts_without_links": sum(r["links"]["concepts_without_links"] for r in results),
            "escaping_links": sum(r["links"]["escaping"] for r in results),
            "related_absolute": sum(r["links"]["related_absolute"] for r in results),
            "related_relative": sum(r["links"]["related_relative"] for r in results),
            "dirs_missing_index": sum(r["indexes"]["dirs_missing_index"] for r in results),
            "dirs_with_concepts": sum(r["indexes"]["dirs_with_concepts"] for r in results),
        },
        "trust": {
            "documents": sum(r["trust"]["documents"] for r in results),
            "complete": sum(r["trust"]["complete"] for r in results),
            **{f"has_{f}": sum(r["trust"][f"has_{f}"] for r in results)
               for f in TRUST_FAMILIES},
            "findings": sum(r["trust"]["findings"] for r in results),
        },
        "bundles": results,
    }


def print_profile_table(rep: dict) -> None:
    c, t = rep["corpus"], rep["totals"]
    print(f"\n=== PROFILE conformance — {rep['profile']} "
          f"(checker {rep['checker_version']}) ===")
    print(f"{c['bundles']} bundles · {c['concepts']} Concept · "
          f"{c['references']} Reference · {c['documents']} documents\n")
    hdr = (f"{'bundle':24}{'L0':>4}{'L1':>4}{'L2':>4}{'L2b':>5}{'L3':>4}"
           f"{'abs':>6}{'rel':>6}{'pseu':>6}{'bare':>6}{'0lnk':>6}{'noIdx':>7}")
    print(hdr); print("-" * len(hdr))
    tick = lambda b: " ✓" if b else " ✗"
    for r in rep["bundles"]:
        L = r["links"]
        print(f"{r['bundle']:24}{tick(r['level_0']):>4}{tick(r['level_1']):>4}"
              f"{tick(r['level_2']):>4}{tick(r['level_2b']):>5}{tick(r['level_3']):>4}"
              f"{L['absolute']:>6}{L['relative']:>6}{L['pseudo']:>6}{L['bare_path']:>6}"
              f"{L['concepts_without_links']:>6}{r['indexes']['dirs_missing_index']:>7}")
    print("-" * len(hdr))
    print(f"{'TOTAL':24}{'':>4}{'':>4}{'':>4}{'':>5}{'':>4}"
          f"{t['absolute_links']:>6}{t['relative_links']:>6}{t['pseudo_links']:>6}"
          f"{t['bare_path']:>6}{t['concepts_without_links']:>6}{t['dirs_missing_index']:>7}")
    lv = rep["levels"]
    n = c["bundles"]
    print(f"\n§5 coverage:  L0 {lv['0']}/{n}   L1 {lv['1']}/{n}   "
          f"L2 {lv['2']}/{n}   L2b {lv['2b']}/{n}   L3 {lv['3']}/{n}")
    print(f"related:  {t['related_absolute']} absolute / "
          f"{t['related_relative']} relative  (reported, not scored — §3.1 traversal note)")
    print(f"escaping: {t['escaping_links']} body link(s) resolve outside their bundle root "
          f"(reported, not scored — §3.1 disclosure)")
    tr = rep["trust"]
    print(f"trust:    generated {tr['has_generated']}/{tr['documents']} · "
          f"verified(human:) {tr['has_verified']}/{tr['documents']} · "
          f"sources {tr['has_sources']}/{tr['documents']} · "
          f"okf_profile {tr['has_okf_profile']}/{tr['documents']} · "
          f"all four {tr['complete']}/{tr['documents']}")
    if tr["findings"]:
        print(f"          {tr['findings']} trust finding(s) (reported, not scored)")
    for r in rep["bundles"]:
        if r["level_2_failures"]:
            print(f"\n  {r['bundle']} — Level 2:")
            for f in r["level_2_failures"]:
                print(f"      ✗ {f}")
        if r["level_3_failures"]:
            print(f"\n  {r['bundle']} — Level 3:")
            for f in r["level_3_failures"]:
                print(f"      ✗ {f}")

def _inject_not_line(body: str, line: str) -> str:
    """Insert a **Not:** line just after the first H1, else at the top."""
    m = re.search(r"^# .+$", body, re.M)
    if m:
        idx = m.end()
        return body[:idx] + "\n\n" + line + body[idx:]
    return line + "\n\n" + body


def _reserialize(original: str, new_body: str) -> str:
    """Replace only the body, leaving the original frontmatter text byte-for-byte."""
    lines = original.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return new_body
    count = 0
    for i, ln in enumerate(lines):
        if ln.strip() == "---":
            count += 1
            if count == 2:
                head_txt = "".join(lines[: i + 1])
                sep = "" if head_txt.endswith("\n") else "\n"
                tail = "" if new_body.endswith("\n") else "\n"
                return head_txt + sep + "\n" + new_body + tail
    return new_body


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Validate an OKF bundle.")
    default_bundle = Path(__file__).resolve().parent.parent / "dharma-foundation"
    ap.add_argument("bundle", nargs="?", default=str(default_bundle),
                    help="Path to the bundle root (default: ../dharma-foundation)")
    ap.add_argument("--require-section", action="append", dest="sections",
                    help="A section heading that must appear in every concept "
                         "(repeatable). Defaults to the dharma-bundle set.")
    ap.add_argument("--require-darshana", action="store_true", default=True)
    ap.add_argument("--no-require-darshana", action="store_false", dest="require_darshana")
    ap.add_argument("--require-structured-not", action="store_true", default=True)
    ap.add_argument("--no-require-structured-not", action="store_false",
                    dest="require_structured_not")
    ap.add_argument("--strict", action="store_true", help="treat WARN as failing")
    ap.add_argument("--fix", action="store_true",
                    help="regenerate each body '**Not:**' line from frontmatter")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--profile", action="store_true",
                    help="run LAYER 2 (profile conformance, PROFILE.md §5) and print the table")
    ap.add_argument("--profile-strict", action="store_true",
                    help="exit 1 if any bundle scores below --require-level")
    ap.add_argument("--require-level", default="2",
                    help="level floor for --profile-strict (default: 2)")
    ap.add_argument("--json", dest="json_path", default=None,
                    help="write the profile report as JSON (implies --profile)")
    ap.add_argument("--corpus", action="store_true",
                    help="treat the argument as the corpus root; score every bundle")
    args = ap.parse_args(argv)

    bundle = Path(args.bundle).resolve()
    if not bundle.is_dir():
        sys.stderr.write(f"Not a directory: {bundle}\n")
        return 2
    sections = args.sections if args.sections is not None else DEFAULT_SECTIONS

    # ---- LAYER 2 dispatch (profile conformance) --------------------------
    want_profile = args.profile or args.profile_strict or args.json_path
    if want_profile:
        if args.corpus:
            bundles = sorted(d for d in bundle.iterdir()
                             if d.is_dir() and d.name not in {"tests", "tools", "__pycache__"}
                             and (d / "index.md").exists())
        else:
            bundles = [bundle]
        prep = profile_report([profile_check(b) for b in bundles])
        if args.json_path:
            Path(args.json_path).write_text(
                _json.dumps(prep, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            if not args.quiet:
                print(f"profile report written: {args.json_path}")
        if not args.quiet:
            print_profile_table(prep)
        if args.profile_strict:
            floor = str(args.require_level)
            below = [r["bundle"] for r in prep["bundles"] if not r[f"level_{floor}"]]
            if below:
                if not args.quiet:
                    print(f"\nPROFILE-FAIL: {len(below)} bundle(s) below level {floor}: "
                          f"{', '.join(below)}")
                return 1
        if not (args.strict or args.fix) and args.corpus:
            return 0   # corpus mode is Layer 2 only; Layer 1 runs per bundle

    rep = validate(bundle, sections=sections,
                   require_darshana=args.require_darshana,
                   require_structured_not=args.require_structured_not,
                   fix=args.fix)

    n_md = sum(1 for p in bundle.rglob("*.md") if p.name not in RESERVED)
    if not args.quiet:
        for label, items in (("FAIL", rep.fails), ("WARN", rep.warns), ("INFO", rep.infos)):
            for line in items:
                print(f"[{label}] {line}")
        print(f"\n{n_md} concept files | "
              f"{len(rep.fails)} fail · {len(rep.warns)} warn · {len(rep.infos)} info")

    if rep.fails:
        return 1
    if args.strict and rep.warns:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
