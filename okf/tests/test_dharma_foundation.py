"""Regression test: the dharma-foundation bundle must stay conformant.

Runs the OKF validator over okf/dharma-foundation and asserts there are zero
FAIL-level findings. WARN/INFO are reported but do not fail the suite (use
`--strict` on the CLI for that). This locks in the audit fixes so they cannot
silently regress.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

OKF_ROOT = Path(__file__).resolve().parent.parent
TOOLS = OKF_ROOT / "tools"
BUNDLE = OKF_ROOT / "dharma-foundation"

if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import okf_validate as v  # noqa: E402

DHARMA_SECTIONS = ["What It Actually Means", "Audience Metaphor", "Citations"]


@pytest.fixture(scope="module")
def report() -> v.Report:
    return v.validate(
        BUNDLE,
        sections=DHARMA_SECTIONS,
        require_darshana=True,
        require_structured_not=True,
        fix=False,
    )


def test_bundle_exists():
    assert BUNDLE.is_dir(), f"bundle not found: {BUNDLE}"
    concepts = list((BUNDLE / "concepts").glob("*.md"))
    assert len(concepts) == 25, f"expected 25 concepts, found {len(concepts)}"


def test_no_fail_level_findings(report: v.Report):
    assert report.fails == [], "FAIL-level conformance issues:\n" + "\n".join(report.fails)


def test_every_concept_has_darshana_and_structured_not(report: v.Report):
    # darshana / why warnings are the v0.2 signal; assert none remain.
    offenders = [w for w in report.warns
                 if "darshana" in w or "has no 'why'" in w or "bare string" in w]
    assert offenders == [], "v0.2 field gaps:\n" + "\n".join(offenders)


def test_no_broken_links(report: v.Report):
    broken = [w for w in report.warns if "unresolved link" in w]
    assert broken == [], "broken links:\n" + "\n".join(broken)


def test_not_line_parity(report: v.Report):
    drift = [w for w in report.warns if "body Not:" in w or "no '**Not:**'" in w]
    assert drift == [], "body/frontmatter not: drift:\n" + "\n".join(drift)


def test_splitter_ignores_parenthetical_commas():
    # the false-positive guard from the audit
    terms = v.split_top_level_commas(
        "Salvation, Heaven, Kaivalya (a type of mokṣa, not a synonym)"
    )
    assert terms == ["Salvation", "Heaven", "Kaivalya (a type of mokṣa, not a synonym)"]
