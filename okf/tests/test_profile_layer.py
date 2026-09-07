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
import re
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

# --- measured after the normalization wave's link step ----------------------
# Before it (at 6015e11): absolute 400, relative 913, pseudo 97, bare 56,
# concepts_without_links 50, Level 2 5/13. Those five gaps are now zero and
# the 553 links they represent moved into the relative count: 913 + 400 + 97
# + 56 + 1 hand-written = 1467. The +1 is sankhya-darshana/sesvara-samkhya.md,
# the only concept in the corpus with no citation to convert.
EXPECTED_TOTALS = {
    "absolute_links": 0,
    "relative_links": 1501,
    "pseudo_links": 0,
    "bare_path": 0,
    "concepts_without_links": 0,
    "dirs_missing_index": 0,
    "dirs_with_concepts": 26,
    "related_absolute": 0,
    "related_relative": 1500,
    "escaping_links": 62,
}
EXPECTED_LEVELS = {"0": 13, "1": 13, "2": 13, "2b": 13, "3": 0}
EXPECTED_CORPUS = {"bundles": 13, "concepts": 310, "references": 132, "documents": 442}

# The §3.1 gap, closed. Kept as a record of what the wave converted, and as
# the shape any regression would take: dharma-foundation 136,
# vedanta-epistemology 89, yoga-darshana 84, bhakti-marga 46,
# dharmic-ethics 45 — 400 across the five bundles that predate the
# convention change at upanishadic-core.
FORMERLY_ABSOLUTE = {
    "dharma-foundation", "vedanta-epistemology", "yoga-darshana",
    "bhakti-marga", "dharmic-ethics",
}
EXPECTED_LEVEL_2_PASS = set(BUNDLES)          # all thirteen, from this wave on


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

def test_profile_section_5_matches_the_checker(report):
    """§5 says it is generated, not maintained. This is what enforces it.

    Until 2026-09-07 nothing did. The table was pasted from the checker by
    hand and a later edit could drift from it silently — which is exactly the
    failure §5 was re-specified to prevent on 2026-09-06, one layer up. The
    parse is deliberately literal: the level rows of the §5 table, read out of
    PROFILE.md, compared to a live run.
    """
    doc = (OKF.parent / "PROFILE.md").read_text(encoding="utf-8")
    rows = {
        "0":  r"\*\*0 — Base\*\*.*?\*\*(\d+) / 13\*\*",
        "1":  r"\*\*1 — Profile core\*\*.*?\*\*(\d+) / 13\*\*",
        "2":  r"\*\*2 — Graph interoperable\*\*.*?\*\*(\d+) / 13\*\*",
        "2b": r"\*\*2b — Progressive disclosure\*\*.*?\*\*(\d+) / 13\*\*",
        "3":  r"\*\*3 — Trust and provenance\*\*.*?\*\*(\d+) / 13\*\*",
    }
    documented = {}
    for level, pat in rows.items():
        m = re.search(pat, doc, re.S)
        assert m, f"§5 has no readable row for level {level}"
        documented[level] = int(m.group(1))
    assert documented == report["levels"], (
        f"PROFILE.md §5 says {documented}, the checker says {report['levels']}")


def test_corpus_shape(report):
    assert report["corpus"] == EXPECTED_CORPUS


def test_level_coverage(report):
    assert report["levels"] == EXPECTED_LEVELS


def test_totals(report):
    assert report["totals"] == pytest.approx(EXPECTED_TOTALS) or \
        {k: report["totals"][k] for k in EXPECTED_TOTALS} == EXPECTED_TOTALS


@pytest.mark.parametrize("bundle", sorted(FORMERLY_ABSOLUTE))
def test_converted_bundles_carry_no_absolute_links(report, bundle):
    """§3.1 requires the relative form in bodies. These five held all 400."""
    got = next(b for b in report["bundles"] if b["bundle"] == bundle)
    assert got["links"]["absolute"] == 0


def test_no_bundle_anywhere_carries_an_absolute_body_link(report):
    with_abs = {b["bundle"]: b["links"]["absolute"]
                for b in report["bundles"] if b["links"]["absolute"]}
    assert with_abs == {}


def test_no_bracket_only_pseudo_links_remain(report):
    """`see [references/x.md]` renders as literal text and builds no edge.

    97 of them, all in upanishadic-core, which is why that bundle had a
    relationship graph of exactly zero edges while passing Layer 1.
    """
    offenders = {b["bundle"]: b["links"]["pseudo"]
                 for b in report["bundles"] if b["links"]["pseudo"]}
    assert offenders == {}


def test_no_bare_path_citations_remain(report):
    """`see references/x.md` — same defect, different spelling. 55 + 1."""
    offenders = {b["bundle"]: b["links"]["bare_path"]
                 for b in report["bundles"] if b["links"]["bare_path"]}
    assert offenders == {}


def test_every_concept_now_carries_a_resolvable_body_link(report):
    """The Level 2 presence floor, satisfied corpus-wide.

    The three bundles that failed it — upanishadic-core 26, cosmology-creation
    23, sankhya-darshana 1 — are the assertion. Their 49 came free with the
    citation-form fix; sankhya's one had no citation to convert and was
    written by hand.
    """
    offenders = {b["bundle"]: b["links"]["concepts_without_links"]
                 for b in report["bundles"] if b["links"]["concepts_without_links"]}
    assert offenders == {}
    for name in ("upanishadic-core", "cosmology-creation", "sankhya-darshana"):
        b = next(x for x in report["bundles"] if x["bundle"] == name)
        assert b["level_2"], b["level_2_failures"]


def test_all_thirteen_bundles_reach_level_2(report):
    passing = {b["bundle"] for b in report["bundles"] if b["level_2"]}
    assert passing == EXPECTED_LEVEL_2_PASS
    assert all(not b["level_2_failures"] for b in report["bundles"])


def test_every_directory_holding_concepts_carries_an_index(report):
    """PROFILE.md §3.4 — progressive disclosure, satisfied corpus-wide.

    21 directories lacked one: every `concepts/` directory in all thirteen
    bundles, plus `references/` in the eight bundles from upanishadic-core
    onward. A 442-document corpus meant for context-window-bounded reading
    could be navigated only from the bundle root, one hop, with nothing in
    between.
    """
    offenders = {b["bundle"]: b["indexes"]["dirs_missing_index"]
                 for b in report["bundles"] if b["indexes"]["dirs_missing_index"]}
    assert offenders == {}
    assert all(b["level_2b"] for b in report["bundles"])


def test_level_3_is_still_untouched(report):
    """The trust families are the next wave, not this one."""
    assert not any(b["level_3"] for b in report["bundles"])


def test_related_parser_reads_unindented_lists(report):
    """The 2026-09-06 checker defect, locked so it cannot come back.

    `_related_entries` required an INDENTED list item. 124 of the 322 files
    carrying `related:` write it flush against the margin, and five bundles
    therefore reported zero entries while holding 425 between them. Those five
    are the assertion: if the parser regresses, they go back to zero.

    The entries have since been normalized to the relative form, so the count
    that proves the parser sees them is now `related_relative`. Both list
    styles survive the normalization — the rewrite preserved each file's own
    indentation rather than imposing one.
    """
    per = {b["bundle"]: b["links"]["related_relative"] for b in report["bundles"]}
    formerly_invisible = {
        "ayurveda-consciousness": 97, "jyotisha-kala": 91, "mimamsa-dharma": 79,
        "nyaya-vaisheshika": 110, "sankhya-darshana": 48,
    }
    assert {k: per[k] for k in formerly_invisible} == formerly_invisible
    assert sum(per.values()) == 1500


def test_no_absolute_related_entries_remain(report):
    """Finding C, closed by ruling: normalize rather than amend.

    1,499 of 1,500 entries were bundle-absolute. Nothing traverses `related:`,
    so this changes no graph — it removes the corpus's second link convention,
    leaving one form in bodies and the same form in frontmatter.
    """
    offenders = {b["bundle"]: b["links"]["related_absolute"]
                 for b in report["bundles"] if b["links"]["related_absolute"]}
    assert offenders == {}
    assert sum(b["links"]["related_relative"] for b in report["bundles"]) == 1500


def test_escaping_links_are_reported_but_never_scored(report):
    """§3.1 discloses that some body links leave the bundle root.

    26 point at the repository-root GENEALOGIES.md; 36 are cross-bundle links
    expressing school-relativity, added by the 2026-09 wave. A base-conformant
    resolver may drop all of them (open-knowledge-format#14, acceptance
    criterion 5), which is why PROFILE.md §3.1 discloses them by count. The
    profile permits them; this number is what keeps the disclosure true. It
    must never affect a level.
    """
    per = {b["bundle"]: b["links"]["escaping"]
           for b in report["bundles"] if b["links"]["escaping"]}
    assert per == {
        "ayurveda-consciousness": 7, "bhakti-marga": 4, "cosmology-creation": 7,
        "dharma-foundation": 11, "dharmic-ethics": 2, "mimamsa-dharma": 3,
        "nyaya-vaisheshika": 7, "sankhya-darshana": 5, "shakta-darshana": 9,
        "vedanta-epistemology": 2, "yoga-darshana": 5,
    }
    assert sum(per.values()) == 62
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


# --- the versioning contract, amended 2026-09-07 -----------------------------
# VERSIONING.md rule 2: a wave bumps a bundle's version ONCE and writes it to
# every document in the bundle and to its root index.md. Before the amendment a
# bundle carried two or three values at once and 93 documents carried none.
EXPECTED_BUNDLE_VERSION = {
    "dharma-foundation": "0.1.4", "yoga-darshana": "0.2.2",
    "vedanta-epistemology": "0.3.3", "bhakti-marga": "0.4.3",
    "dharmic-ethics": "0.5.3", "upanishadic-core": "0.6.2",
    "cosmology-creation": "0.7.3", "shakta-darshana": "0.8.2",
    "nyaya-vaisheshika": "0.9.1", "mimamsa-dharma": "0.10.1",
    "ayurveda-consciousness": "0.11.1", "jyotisha-kala": "0.12.1",
    "sankhya-darshana": "0.13.3",
}


def _doc_versions(bundle: str):
    """{bundle_version value: count} across the bundle's Concept/Reference docs."""
    import okf_validate as v
    out = {}
    for p in sorted((OKF / bundle).rglob("*.md")):
        if p.name in v.RESERVED:
            continue
        fm, _ = v._split_doc(p.read_text(encoding="utf-8"))
        m = re.search(r"^type:\s*(.+)$", fm, re.M)
        if (m.group(1).strip().strip("\"'") if m else "") not in ("Concept", "Reference"):
            continue
        mv = re.search(r"^bundle_version:\s*(.+)$", fm, re.M)
        key = mv.group(1).strip().strip("\"'") if mv else "(absent)"
        out[key] = out.get(key, 0) + 1
    return out


@pytest.mark.parametrize("bundle,expected", sorted(EXPECTED_BUNDLE_VERSION.items()))
def test_bundle_version_is_uniform_across_the_bundle(bundle, expected):
    got = _doc_versions(bundle)
    assert got == {expected: sum(got.values())}, (
        f"{bundle}: expected every document at {expected}, found {got}")


@pytest.mark.parametrize("bundle,expected", sorted(EXPECTED_BUNDLE_VERSION.items()))
def test_root_index_uses_bundle_version_and_matches(bundle, expected):
    """One key name across all thirteen roots, and it agrees with the documents."""
    import okf_validate as v
    fm, _ = v._split_doc((OKF / bundle / "index.md").read_text(encoding="utf-8"))
    assert not re.search(r"^version:", fm, re.M), (
        f"{bundle}/index.md frontmatter still uses the legacy `version:` key")
    m = re.search(r'^bundle_version:\s*"?([^"\n]+)"?\s*$', fm, re.M)
    assert m and m.group(1).strip() == expected, (
        f"{bundle}/index.md: expected bundle_version {expected}")


def test_no_document_anywhere_lacks_a_bundle_version():
    """93 documents carried none before this wave; dharma-foundation had zero."""
    missing = {b: _doc_versions(b).get("(absent)", 0) for b in BUNDLES}
    assert {k: v for k, v in missing.items() if v} == {}


def test_profile_strict_now_passes_at_level_two(report):
    """The wave's headline: --require-level 2 goes green for the first time."""
    r = subprocess.run(
        [sys.executable, str(TOOL), str(OKF), "--corpus",
         "--profile-strict", "--require-level", "2", "--quiet"],
        capture_output=True, text=True)
    assert r.returncode == 0, "all 13 bundles are Level 2 after the link step"


def test_profile_strict_now_passes_at_level_2b(report):
    """All thirteen bundles clear the progressive-disclosure floor."""
    r = subprocess.run(
        [sys.executable, str(TOOL), str(OKF), "--corpus",
         "--profile-strict", "--require-level", "2b", "--quiet"],
        capture_output=True, text=True)
    assert r.returncode == 0, "all 13 bundles are Level 2b after the index step"


def test_profile_strict_still_fails_at_level_3(report):
    """Level 3 is 0/13 and remains the corpus's open frontier."""
    r = subprocess.run(
        [sys.executable, str(TOOL), str(OKF), "--corpus",
         "--profile-strict", "--require-level", "3", "--quiet"],
        capture_output=True, text=True)
    assert r.returncode == 1, "no bundle reaches Level 3 yet"


def test_profile_strict_passes_at_level_one(report):
    r = subprocess.run(
        [sys.executable, str(TOOL), str(OKF), "--corpus",
         "--profile-strict", "--require-level", "1", "--quiet"],
        capture_output=True, text=True)
    assert r.returncode == 0, "all 13 bundles are Level 1"
