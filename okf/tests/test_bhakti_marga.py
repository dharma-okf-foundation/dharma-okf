"""Regression test: the bhakti-marga bundle must stay conformant (OKF v0.2).

Runs the OKF validator over okf/bhakti-marga and asserts zero FAIL-level
findings and no v0.2 field gaps, broken links, or not-line drift. Adds two
checks the validator itself does not perform (the gaps that bit vedanta):
bare-relative body links must resolve, and every slug/filename must be ASCII.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

import pytest

OKF_ROOT = Path(__file__).resolve().parent.parent
TOOLS = OKF_ROOT / "tools"
BUNDLE = OKF_ROOT / "bhakti-marga"

if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import okf_validate as v  # noqa: E402

SECTIONS = ["Audience Metaphor", "Citations"]
_LINK = re.compile(r"\]\(([^)]+?\.md)(?:#[^)]*)?\)")


@pytest.fixture(scope="module")
def report() -> v.Report:
    return v.validate(BUNDLE, sections=SECTIONS, require_darshana=True,
                      require_structured_not=True, fix=False)


def test_bundle_exists():
    assert BUNDLE.is_dir()
    assert len(list((BUNDLE / "concepts").glob("*.md"))) == 15


def test_no_fail_level_findings(report: v.Report):
    assert report.fails == [], "\n".join(report.fails)


def test_v02_fields_present(report: v.Report):
    off = [w for w in report.warns
           if "darshana" in w or "has no 'why'" in w or "bare string" in w]
    assert off == [], "\n".join(off)


def test_no_broken_links(report: v.Report):
    assert [w for w in report.warns if "unresolved link" in w] == []


def test_not_line_parity(report: v.Report):
    assert [w for w in report.warns if "body Not:" in w or "no '**Not:**'" in w] == []


def test_bare_relative_body_links_resolve():
    """Validator only checks /-rooted and ./ links; cover bare-relative siblings."""
    broken = []
    for f in sorted((BUNDLE / "concepts").glob("*.md")):
        body = f.read_text(encoding="utf-8").split("\n---\n", 1)[-1]
        for link in _LINK.findall(body):
            if link.startswith("http"):
                continue
            if link.startswith("/"):
                tgt = (BUNDLE / link.lstrip("/")).resolve()
            else:
                tgt = (f.parent / link).resolve()
            if not tgt.exists():
                broken.append(f"{f.name}: {link}")
    assert broken == [], "broken body links:\n" + "\n".join(broken)


def test_all_slugs_ascii():
    """Filenames and in-link slugs must be pure ASCII (URL portability)."""
    bad = []
    for f in BUNDLE.rglob("*.md"):
        try:
            f.name.encode("ascii")
        except UnicodeEncodeError:
            bad.append(f"filename: {f.name}")
        body = f.read_text(encoding="utf-8")
        for link in _LINK.findall(body):
            try:
                link.encode("ascii")
            except UnicodeEncodeError:
                bad.append(f"{f.name} link: {link}")
    assert bad == [], "non-ASCII slugs:\n" + "\n".join(bad)
