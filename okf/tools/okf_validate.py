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
    for ch in s:
        if quote:
            if ch == quote:
                quote = None
            buf.append(ch)
        elif ch in "\"'":
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
    args = ap.parse_args(argv)

    bundle = Path(args.bundle).resolve()
    if not bundle.is_dir():
        sys.stderr.write(f"Not a directory: {bundle}\n")
        return 2
    sections = args.sections if args.sections is not None else DEFAULT_SECTIONS

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
