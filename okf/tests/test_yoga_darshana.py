"""Regression test: the yoga-darshana bundle must stay conformant (OKF v0.2)."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

OKF_ROOT = Path(__file__).resolve().parent.parent
TOOLS = OKF_ROOT / "tools"
BUNDLE = OKF_ROOT / "yoga-darshana"

if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import okf_validate as v  # noqa: E402

SECTIONS = ["Audience Metaphor", "Citations"]


@pytest.fixture(scope="module")
def report() -> v.Report:
    return v.validate(BUNDLE, sections=SECTIONS, require_darshana=True,
                      require_structured_not=True, fix=False)


def test_bundle_exists():
    assert BUNDLE.is_dir()
    assert len(list((BUNDLE / "concepts").glob("*.md"))) == 26


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
