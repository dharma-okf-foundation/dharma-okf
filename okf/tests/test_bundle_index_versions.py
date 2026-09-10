"""Regression tests for bundle-root index.md version prose.

WHY THIS EXISTS
---------------
`wiki/operations/okf-publishing-lessons.md` §22 records that the 2026-09
normalization wave restamped `bundle_version` on all 442 documents and left
`README.md`'s Release column describing the pre-wave state for six commits,
because nothing in the repository reads prose. §22's closing paragraph names
the durable fix:

    "The durable version is a checker rule or a test ... that would have
    caught the fourth item on the day it broke, without anyone remembering
    to look. Until such a test exists, this section is a checklist and
    carries a checklist's reliability."

This module is that test, for the file class where the same defect was found
again on 2026-09-09: bundle-root `index.md` bodies. Fifteen self-version
claims across ten files stated a `bundle_version` one to three patches old,
including `cosmology-creation`'s H1 heading and `upanishadic-core`'s CC BY-SA
attribution string -- the string third parties are told to cite this corpus by.

WHAT IS AND IS NOT A VERSION
----------------------------
Bundle-root index bodies are full of `<digit>.<digit>.<digit>` strings that are
not versions at all: scriptural verse citations such as `BS 2.1.33`,
`BS 1.1.2`, `BhP 1.2.23`, `BU 1.4.10`, `CU 6.8.7`. A bare three-component
regex flags every one of them.

The discriminator is the `v` prefix: this corpus writes versions as `v0.7.3`
and never writes verse citations that way. The one exception is the
`**Version:** `0.2.2`` label form in `yoga-darshana`, matched separately.
Verified 2026-09-09 against all 13 bundles: zero false positives, zero misses.
"""
from __future__ import annotations

import re
from pathlib import Path

import pytest

OKF = Path(__file__).resolve().parents[1]          # okf/

BUNDLES = sorted(
    d.name for d in OKF.iterdir()
    if d.is_dir() and d.name not in {"tests", "tools", "__pycache__"}
    and (d / "index.md").exists()
)

# A version reference: 'v' preceded by a non-alphanumeric (or start of line),
# then major.minor.patch. Excludes verse citations, which carry no 'v'.
_VERSION = re.compile(r"(?<![A-Za-z0-9])v(\d+\.\d+\.\d+)")
# The label form, which omits the 'v': **Version:** `0.2.2`
_LABEL = re.compile(r"(?i)\*\*version:\*\*\s*`?(\d+\.\d+\.\d+)`?")
# A line pointing into another bundle's directory.
_OTHER_BUNDLE = re.compile(r"okf/([a-z-]+)/")
_FRONTMATTER_VERSION = re.compile(r'^bundle_version:\s*"?([\d.]+)"?', re.M)


def _split(path: Path) -> tuple[str, list[tuple[int, str]]]:
    """Return (bundle_version, [(line_no, line)]) for the WHOLE file.

    Frontmatter was excluded in the first revision of this module, and the
    2026-09-09 commit paid for it: `cosmology-creation` had its body line
    corrected to the namespaced tag while `release_tag: "v0.7.0"` sat
    fourteen lines above it in frontmatter, unread and unchanged, leaving
    the file contradicting itself. `bundle_version` itself is invisible to
    both patterns below because it carries no `v` prefix, so no exclusion
    is needed.
    """
    text = path.read_text(encoding="utf-8")
    match = _FRONTMATTER_VERSION.search(text)
    assert match, f"{path} carries no bundle_version"
    lines = text.splitlines()
    return match.group(1), [(i + 1, lines[i]) for i in range(len(lines))]


def _claims(bundle: str):
    """Yield (line_no, version, line, other_bundle_or_None) for one index."""
    version, body = _split(OKF / bundle / "index.md")
    for line_no, line in body:
        found = [m.group(1) for m in _VERSION.finditer(line)]
        found += [m.group(1) for m in _LABEL.finditer(line)]
        if not found:
            continue
        other = _OTHER_BUNDLE.search(line)
        other_name = other.group(1) if other and other.group(1) != bundle else None
        for value in found:
            yield line_no, value, line, other_name, version


@pytest.mark.parametrize("bundle", BUNDLES)
def test_index_self_version_matches_frontmatter(bundle):
    """A bundle's own version, stated in its index body, matches its frontmatter.

    This is the §22 defect: prose stating a version that a later patch bump
    silently falsified, invisible to the checker, the corpus validator and
    every other test because none of them read prose.
    """
    stale = [
        f"{bundle}/index.md:{line_no} says v{value}, "
        f"bundle_version is {version} | {line.strip()[:90]}"
        for line_no, value, line, other, version in _claims(bundle)
        if other is None and value != version
    ]
    assert stale == [], "stale self-version claim(s):\n  " + "\n  ".join(stale)


@pytest.mark.parametrize("bundle", BUNDLES)
def test_cross_bundle_references_use_minor_series(bundle):
    """A reference to ANOTHER bundle names its minor series, not its patch.

    A patch-level cross-reference is falsified by a patch bump in a bundle the
    referring file has no reason to be re-read for, which is how six of these
    went stale unnoticed. Measured 2026-09-09: 110 cross-bundle references
    already used the two-component form and 6 used three components -- and all
    6 of those were stale. The convention is the corpus's own; this locks it.
    """
    offenders = [
        f"{bundle}/index.md:{line_no} -> {other} pinned at v{value} "
        f"(use the minor series) | {line.strip()[:80]}"
        for line_no, value, line, other, _ in _claims(bundle)
        if other is not None
    ]
    assert offenders == [], ("patch-level cross-bundle reference(s):\n  "
                             + "\n  ".join(offenders))


@pytest.mark.parametrize("bundle", BUNDLES)
def test_no_index_calls_a_shipped_bundle_planned(bundle):
    """No index describes a bundle that exists as planned or forthcoming.

    Publishing lessons §22 rule 2: a forward-looking claim "becomes false by
    being honoured, which is the one failure mode nobody re-reads for." Three
    such rows survived the 2026-09-09 commit -- `bhakti-marga` calling
    `dharmic-ethics` (v0.5) and `upanishadic-core` (v0.6) planned, and
    `dharmic-ethics` saying the same of `upanishadic-core` -- while the rows
    directly above them in the same tables were being corrected.

    A forward reference to a bundle that genuinely does not exist yet is
    legitimate and is deliberately not flagged: the test fires only when the
    named bundle is present in the corpus.
    """
    forward = re.compile(r"(?i)\b(planned|forthcoming|will treat|will cover|not yet built)\b")
    _, lines = _split(OKF / bundle / "index.md")
    offenders = []
    for line_no, line in lines:
        if not forward.search(line):
            continue
        for other in _OTHER_BUNDLE.finditer(line):
            name = other.group(1)
            if name != bundle and (OKF / name).is_dir():
                offenders.append(
                    f"{bundle}/index.md:{line_no} calls {name} planned, but it "
                    f"is published | {line.strip()[:80]}")
    assert offenders == [], ("forward-looking claim(s) already honoured:\n  "
                             + "\n  ".join(offenders))
