"""Regression tests for okf_viz.py — the rebuilt visualizer generator.

Two properties, and they answer different questions.

  1. FRESHNESS. Every committed viz.html equals what the generator produces
     from the corpus as it stands. This is what makes the artifact a
     measurement rather than a claim: edit a concept without regenerating and
     this fails.

  2. FIDELITY. The generator reproduces the visualizers written by the tool it
     replaces — the 2026-07 artifacts, produced by
     okf/src/enrichment_agent/viewer/generator.py before Wave 0 removed it —
     byte-for-byte, from the corpus as it stood at each of those thirteen
     commits. Property 1 alone would be satisfied by a generator that is
     merely self-consistent. Property 2 is what establishes that this one is
     faithful to a tool that no longer exists.

The baselines are PINNED below rather than resolved as "the last commit
touching this file". They were resolved that way at first, and the 2026-09-07
regeneration immediately consumed the proof: eleven of the thirteen baselines
became the regeneration commit itself, so eleven fidelity assertions silently
collapsed into duplicates of property 1. A proof that any future regeneration
erases is not a proof. These SHAs are the last commits at which the ORIGINAL
generator wrote each file, and they do not move again.

Property 2 needs git history and is skipped where it is unavailable
(a shallow clone, an exported tree). Property 1 always runs.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

OKF = Path(__file__).resolve().parents[1]
TOOLS = OKF / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import okf_viz  # noqa: E402

TEMPLATE = (TOOLS / "viz_template.html").read_text(encoding="utf-8")
# The last commit at which the ORIGINAL generator wrote each viz.html, before
# it was removed with okf/src/ in Wave 0. Every one is 2026-07-14. Pinned, not
# derived: see the module docstring.
ORIGINAL_ARTIFACT = {
    "ayurveda-consciousness": "0cee812a179e8c17e09f593746ff18688edb7ea7",
    "bhakti-marga":           "d4448c65f1cedd0fa9c589f0795769ae5ee401f0",
    "cosmology-creation":     "fbe7ebb9f927150facddebf9ca84aec0049dd92f",
    "dharma-foundation":      "b12886da05d34a64b260d24ccf648a91f8aa962e",
    "dharmic-ethics":         "8e07e1f399884b1acf7d2216fc965f73b3a63dd9",
    "jyotisha-kala":          "0c2721e3dd2c1e82f92cd57a3cc713739afa2de3",
    "mimamsa-dharma":         "b129020915082d8d07a628efd3a00a476c411cb2",
    "nyaya-vaisheshika":      "67a4d508eb3ee2fbdebf3ff76c0bf82075134ba9",
    "sankhya-darshana":       "79bac6adcca8c74b523028dba26289601b5ab929",
    "shakta-darshana":        "7ccfc15f505e9519851d5d30fec91b923cca3096",
    "upanishadic-core":       "9d9a68c971725b46a7c01514083bd17c57981962",
    "vedanta-epistemology":   "e5cc5013e6d6ffba09e698deaf5d3a6cfbffb311",
    "yoga-darshana":          "47bed8a54fd77a244f57ec2d956cdd5da87b87f1",
}

BUNDLES = sorted(
    d.name for d in OKF.iterdir()
    if d.is_dir() and d.name not in {"tests", "tools", "__pycache__"}
    and (d / "index.md").exists()
)


def _git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(OKF.parent), *args],
                          capture_output=True, text=True)


def test_thirteen_bundles_and_a_template():
    assert len(BUNDLES) == 13, BUNDLES
    assert set(ORIGINAL_ARTIFACT) == set(BUNDLES), "a bundle has no pinned baseline"
    assert "@@BUNDLE_NAME@@" in TEMPLATE and "@@BUNDLE_JSON@@" in TEMPLATE


# --- property 1: freshness --------------------------------------------------

@pytest.mark.parametrize("bundle", BUNDLES)
def test_committed_viz_is_current(bundle):
    b = OKF / bundle
    assert (b / "viz.html").read_text(encoding="utf-8") == okf_viz.render(b, TEMPLATE), (
        f"{bundle}/viz.html is stale — regenerate with "
        f"`python okf/tools/okf_viz.py okf/{bundle}`")


@pytest.mark.parametrize("bundle", BUNDLES)
def test_generator_is_deterministic(bundle):
    b = OKF / bundle
    assert okf_viz.render(b, TEMPLATE) == okf_viz.render(b, TEMPLATE)


# --- property 2: fidelity to the tool this one replaces ---------------------

@pytest.mark.parametrize("bundle", BUNDLES)
def test_reproduces_the_original_generators_artifact(bundle, tmp_path):
    if _git("rev-parse", "--is-inside-work-tree").returncode != 0:
        pytest.skip("not a git work tree")
    sha = ORIGINAL_ARTIFACT[bundle]
    if _git("cat-file", "-e", f"{sha}^{{commit}}").returncode != 0:
        pytest.skip("baseline commit unavailable (shallow clone?)")
    committed = _git("show", f"{sha}:okf/{bundle}/viz.html")
    if committed.returncode != 0:
        pytest.skip("baseline blob unavailable (shallow clone?)")
    archive = subprocess.run(
        ["git", "-C", str(OKF.parent), "archive", sha, f"okf/{bundle}"],
        capture_output=True)
    if archive.returncode != 0:
        pytest.skip("baseline tree unavailable (shallow clone?)")
    subprocess.run(["tar", "-x", "-C", str(tmp_path)], input=archive.stdout, check=True)
    rebuilt = okf_viz.render(tmp_path / "okf" / bundle, TEMPLATE)
    assert rebuilt == committed.stdout, (
        f"{bundle}: the rebuilt generator does not reproduce the artifact the "
        f"original generator wrote at {sha[:7]} (2026-07-14)")
