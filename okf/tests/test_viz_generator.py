"""Regression tests for okf_viz.py — the rebuilt visualizer generator.

Two properties, and they answer different questions.

  1. FRESHNESS. Every committed viz.html equals what the generator produces
     from the corpus as it stands. This is what makes the artifact a
     measurement rather than a claim: edit a concept without regenerating and
     this fails.

  2. FIDELITY. The generator reproduces each committed viz.html byte-for-byte
     from the corpus AS IT WAS when that file was last written — thirteen
     different baseline commits, because the 2026-07 enrichment waves
     regenerated only the bundles they touched. Property 1 alone would be
     satisfied by a generator that is merely self-consistent; property 2 is
     what establishes that this one is faithful to the tool it replaces.

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
def test_reproduces_the_committed_artifact_at_its_own_baseline(bundle, tmp_path):
    if _git("rev-parse", "--is-inside-work-tree").returncode != 0:
        pytest.skip("not a git work tree")
    r = _git("log", "-1", "--format=%H", "--", f"okf/{bundle}/viz.html")
    if r.returncode != 0 or not r.stdout.strip():
        pytest.skip(f"no history for okf/{bundle}/viz.html")
    sha = r.stdout.strip()
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
        f"{bundle}: generator does not reproduce the artifact committed at {sha[:7]}")
