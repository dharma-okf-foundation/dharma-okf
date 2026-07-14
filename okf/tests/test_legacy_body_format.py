"""Regression test: the legacy-body-format waiver (decision 2026-07-14).

Five pre-canonical bundles (yoga-darshana, vedanta-epistemology, bhakti-marga,
upanishadic-core, cosmology-creation) carry their definitional content in named
scholarly sections rather than under the literal 'What It Actually Means'
heading. The validator waives that ONE heading for those bundle names only;
'Audience Metaphor' and 'Citations' stay required everywhere, and non-legacy
bundles still require the canonical heading.
"""
from __future__ import annotations

import sys
from pathlib import Path

OKF_ROOT = Path(__file__).resolve().parent.parent
TOOLS = OKF_ROOT / "tools"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import okf_validate as v  # noqa: E402

_DOC = """---
type: Concept
title: "Test"
description: "A test concept."
timestamp: "2026-07-14T00:00:00Z"
not:
  - term: "wrongword"
    instead: "test"
darshana: "test"
---
# Test

## Etymology

Scholarly definitional section under a legacy heading.

## Audience Metaphor

A metaphor.

## Citations

A citation.
"""


def _make_bundle(tmp_path: Path, name: str) -> Path:
    b = tmp_path / name
    (b / "concepts").mkdir(parents=True)
    (b / "concepts" / "test.md").write_text(_DOC, encoding="utf-8")
    return b


def _heading_warns(rep: v.Report) -> list[str]:
    return [w for w in getattr(rep, "warns", []) or []
            if "What It Actually Means" in str(w)]


def _run(bundle: Path) -> v.Report:
    return v.validate(bundle, sections=v.DEFAULT_SECTIONS,
                      require_darshana=False, require_structured_not=False,
                      fix=False)


def test_legacy_bundle_waives_canonical_heading(tmp_path):
    rep = _run(_make_bundle(tmp_path, "yoga-darshana"))
    assert not _heading_warns(rep)


def test_non_legacy_bundle_still_requires_heading(tmp_path):
    rep = _run(_make_bundle(tmp_path, "not-a-legacy-bundle"))
    assert _heading_warns(rep)


def test_waiver_set_is_exactly_the_five_pre_canonical_bundles():
    assert v.LEGACY_BODY_FORMAT_BUNDLES == {
        "yoga-darshana", "vedanta-epistemology", "bhakti-marga",
        "upanishadic-core", "cosmology-creation",
    }
