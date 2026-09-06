"""Regression tests for LAYER 2 — profile conformance (PROFILE.md §5).

These lock the numbers measured against the corpus at commit 6015e11 so the
§5 coverage table can never silently drift again. The morning of 2026-08-06 was
spent correcting a hand-maintained table; this module is the mechanism that
stops the next one.

Two properties matter and are tested separately:

  1. LAYER 1 IS UNCHANGED. validate() must behave exactly as it did before the
     profile layer existed — the other seven modules depend on it, and folding
     profile rules into it would make all 13 bundles fail --strict.
  2. LAYER 2 REPRODUCES THE MEASUREMENTS. Every number here came from a script
     over a fresh clone, not from a planning document.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

OKF = Path(__file__).resolve().parents[1]          # okf/
TOOL = OKF / "tools" / "okf_validate.py"

BUNDLES = sorted(
    d.name for d in OKF.iterdir()
    if d.is_dir() and d.name not in {"tests", "tools", "__pycache__"}
    and (d / "index.md").exists()
)

# --- measured at 6015e11 -----------------------------------------------------
EXPECTED_TOTALS = {
    "absolute_links": 400,
    "relative_links": 913,
    "pseudo_links": 97,
    "bare_path": 56,
    "concepts_without_links": 50,
    "dirs_missing_index": 21,
    "dirs_with_concepts": 26,
    "related_absolute": 1499,
    "related_relative": 1,
    "escaping_links": 28,
}
EXPECTED_LEVELS = {"0": 13, "1": 13, "2": 5, "2b": 0, "3": 0}
EXPECTED_CORPUS = {"bundles": 13, "concepts": 310, "references": 132, "documents": 442}

# per-bundle absolute-link distribution (§3.1 gap — the five oldest bundles)
EXPECTED_ABSOLUTE = {
    "dharma-foundation": 136, "vedanta-epistemology": 89, "yoga-darshana": 84,
    "bhakti-marga": 46, "dharmic-ethics": 45,
}
EXPECTED_LEVEL_2_PASS = {
    "ayurveda-consciousness", "jyotisha-kala", "mimamsa-dharma",
    "nyaya-vaisheshika", "shakta-darshana",
}


@pytest.fixture(scope="module")
def report(tmp_path_factory) -> dict:
    out = tmp_path_factory.mktemp("profile") / "report.json"
    r = subprocess.run(
        [sys.executable, str(TOOL), str(OKF), "--corpus", "--json", str(out), "--quiet"],
        capture_output=True, text=True,
    )
    assert r.returncode == 0, f"checker failed: {r.stderr}"
    return json.loads(out.read_text(encoding="utf-8"))


# --- property 1: Layer 1 is untouched ---------------------------------------

def test_thirteen_bundles_discovered():
    assert len(BUNDLES) == 13, BUNDLES


@pytest.mark.parametrize("bundle", BUNDLES)
def test_layer1_still_exits_zero_without_profile_flags(bundle):
    """Base conformance must be unaffected by the profile layer's existence."""
    r = subprocess.run([sys.executable, str(TOOL), str(OKF / bundle)],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout
    assert "0 fail" in r.stdout


@pytest.mark.parametrize("bundle", BUNDLES)
def test_layer1_strict_still_passes(bundle):
    r = subprocess.run([sys.executable, str(TOOL), str(OKF / bundle), "--strict"],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout


# --- property 2: Layer 2 reproduces the measurements ------------------------

def test_corpus_shape(report):
    assert report["corpus"] == EXPECTED_CORPUS


def test_level_coverage(report):
    assert report["levels"] == EXPECTED_LEVELS


def test_totals(report):
    assert report["totals"] == pytest.approx(EXPECTED_TOTALS) or \
        {k: report["totals"][k] for k in EXPECTED_TOTALS} == EXPECTED_TOTALS


@pytest.mark.parametrize("bundle,count", sorted(EXPECTED_ABSOLUTE.items()))
def test_absolute_link_distribution(report, bundle, count):
    got = next(b for b in report["bundles"] if b["bundle"] == bundle)
    assert got["links"]["absolute"] == count


def test_only_five_bundles_carry_absolute_links(report):
    with_abs = {b["bundle"] for b in report["bundles"] if b["links"]["absolute"]}
    assert with_abs == set(EXPECTED_ABSOLUTE)


def test_pseudo_links_confined_to_upanishadic_core(report):
    """97 bracket-only [x.md] forms, all in one bundle. Audit finding A."""
    offenders = {b["bundle"]: b["links"]["pseudo"]
                 for b in report["bundles"] if b["links"]["pseudo"]}
    assert offenders == {"upanishadic-core": 97}


def test_bare_path_distribution(report):
    offenders = {b["bundle"]: b["links"]["bare_path"]
                 for b in report["bundles"] if b["links"]["bare_path"]}
    assert offenders == {"cosmology-creation": 55, "upanishadic-core": 1}


def test_level_2_presence_floor_drops_the_edgeless_bundles(report):
    """The whole point of the re-spec: a bundle with no graph must not pass."""
    passing = {b["bundle"] for b in report["bundles"] if b["level_2"]}
    assert passing == EXPECTED_LEVEL_2_PASS
    for name in ("upanishadic-core", "cosmology-creation", "sankhya-darshana"):
        b = next(x for x in report["bundles"] if x["bundle"] == name)
        assert not b["level_2"]
        assert any("presence:" in f for f in b["level_2_failures"])


def test_no_bundle_reaches_level_2b_or_3(report):
    assert not any(b["level_2b"] for b in report["bundles"])
    assert not any(b["level_3"] for b in report["bundles"])


def test_related_parser_reads_unindented_lists(report):
    """The 2026-09-06 checker defect, locked so it cannot come back.

    `_related_entries` required an INDENTED list item. 124 of the 322 files
    carrying `related:` write it flush against the margin, and five bundles
    therefore reported zero entries while holding 425 between them. Those five
    are the assertion: if the parser regresses, they go back to zero.
    """
    per = {b["bundle"]: b["links"]["related_absolute"] for b in report["bundles"]}
    formerly_invisible = {
        "ayurveda-consciousness": 97, "jyotisha-kala": 91, "mimamsa-dharma": 79,
        "nyaya-vaisheshika": 110, "sankhya-darshana": 48,
    }
    assert {k: per[k] for k in formerly_invisible} == formerly_invisible
    assert sum(per.values()) == 1499


def test_escaping_links_are_reported_but_never_scored(report):
    """§3.1 discloses that some body links leave the bundle root.

    26 point at the repository-root GENEALOGIES.md; 2 are cross-bundle. A
    base-conformant resolver may drop all of them (open-knowledge-format#14,
    acceptance criterion 5). The profile permits them; the count is what keeps
    the disclosure honest. It must never affect a level.
    """
    per = {b["bundle"]: b["links"]["escaping"]
           for b in report["bundles"] if b["links"]["escaping"]}
    assert per == {
        "bhakti-marga": 4, "cosmology-creation": 3, "dharma-foundation": 8,
        "dharmic-ethics": 2, "shakta-darshana": 9, "vedanta-epistemology": 2,
    }
    assert sum(per.values()) == 28
    # scoring is untouched: five bundles still pass Level 2, and two of the
    # bundles carrying escaping links are among them.
    passing = {b["bundle"] for b in report["bundles"] if b["level_2"]}
    assert passing == EXPECTED_LEVEL_2_PASS


def test_no_unresolved_body_links(report):
    """Distinct from form: every real markdown link must still resolve."""
    assert sum(b["links"]["unresolved"] for b in report["bundles"]) == 0


def test_subdirectory_indexes_carry_no_frontmatter(report):
    """PROFILE.md §3.4 asserts this; §1.1 exempts bundle roots only."""
    assert all(not b["indexes"]["subindex_with_frontmatter"] for b in report["bundles"])


def test_profile_strict_fails_below_level_two(report):
    r = subprocess.run(
        [sys.executable, str(TOOL), str(OKF), "--corpus",
         "--profile-strict", "--require-level", "2", "--quiet"],
        capture_output=True, text=True)
    assert r.returncode == 1, "8 bundles are below Level 2; strict mode must fail"


def test_profile_strict_passes_at_level_one(report):
    r = subprocess.run(
        [sys.executable, str(TOOL), str(OKF), "--corpus",
         "--profile-strict", "--require-level", "1", "--quiet"],
        capture_output=True, text=True)
    assert r.returncode == 0, "all 13 bundles are Level 1"
