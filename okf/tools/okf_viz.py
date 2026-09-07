#!/usr/bin/env python3
"""okf_viz.py — regenerate a bundle's self-contained viz.html.

Reconstructed 2026-09-07. The generator that produced the committed
visualizers was `okf/src/enrichment_agent/viewer/generator.py`, removed with
`okf/src/` in Wave 0 (see CHANGELOG, "Wave 0"). The artifacts survived their
tool, which is why this file exists: an artifact nobody can rebuild is a claim,
not a measurement — the same objection PROFILE.md §5 answers for the
conformance table.

Nothing here was invented. The HTML template is byte-identical across all
thirteen committed visualizers and was extracted from them verbatim
(`viz_template.html`). The data shape, the JSON serialization, the node
ordering and the size formula were all derived from the committed output and
then proved against it: `okf/tests/test_viz_generator.py` regenerates every
bundle at the commit where its viz.html was last written and requires a
byte-for-byte match, thirteen times.

Three findings from that proof, recorded because each is a trap:

  * Frontmatter must be parsed as YAML, not by regex. In a single-quoted
    scalar `''` is one apostrophe; a regex reads it as two.
  * Bodies are `strip("\n")` at both ends.
  * Documents are ordered by sorted FILE PATH, extension included — not by
    concept id. "guru-shishya-parampara.md" precedes "guru.md" because "-"
    sorts before "."; drop the extension and the order reverses.
    `bhakti-marga` is the only bundle in the corpus where those two orders
    differ, and it is the one that caught the error.

Usage:
    python okf/tools/okf_viz.py <bundle-dir>              # write viz.html
    python okf/tools/okf_viz.py <bundle-dir> --check      # exit 1 if stale
"""
import json, os, re, sys
from pathlib import Path

import yaml

RESERVED = {"index.md", "log.md"}
PALETTE = {"BigQuery Dataset": "#8b5cf6", "BigQuery Table": "#3b82f6",
           "Reference": "#10b981", "Concept": "#f59e0b"}
_FM   = re.compile(r"^---\n(.*?)\n---\n", re.S)
_LINK = re.compile(r"\]\(([^)]+)\)")

def split_doc(text):
    m = _FM.match(text)
    return (m.group(1), text[m.end():]) if m else ("", text)

def fields(fm):
    """Frontmatter as YAML. A regex cannot unescape a single-quoted scalar:
    'upanishadic-core\'\'s avidya' is one apostrophe, not two."""
    try:
        d = yaml.safe_load(fm)
    except Exception:
        d = None
    return d if isinstance(d, dict) else {}

def scalar(d, key):
    v = d.get(key)
    return None if v is None else (v if isinstance(v, str) else str(v))

def seq(d, key):
    v = d.get(key)
    if isinstance(v, list): return [x if isinstance(x, str) else str(x) for x in v]
    return []

def to_id(target, doc_rel, bundle):
    raw = target.split("#", 1)[0]
    if "://" in raw or not raw.endswith(".md"): return None
    base = bundle if raw.startswith("/") else (bundle / doc_rel).parent
    try:
        p = (base / raw.lstrip("/")).resolve().relative_to(bundle.resolve())
    except Exception:
        return None
    return "/".join(p.with_suffix("").parts)

def build(bundle: Path):
    docs = {}
    for p in sorted(bundle.rglob("*.md")):
        if p.name in RESERVED: continue
        fm, body = split_doc(p.read_text(encoding="utf-8"))
        d = fields(fm)
        typ = scalar(d, "type")
        if typ not in ("Concept", "Reference"): continue
        rel = p.relative_to(bundle)
        docs["/".join(rel.with_suffix("").parts)] = (rel, d, body.strip("\n"))
    # Document order is the sorted FILE PATH, extension included — not the id.
    # "guru-shishya-parampara.md" sorts before "guru.md" ("-" < "."), and the
    # reverse once ".md" is stripped. bhakti-marga is the only bundle where the
    # two orders differ, and it is the one that caught this.
    nodes, bodies = [], {}
    for nid in docs:
        rel, d, body = docs[nid]
        typ = scalar(d, "type")
        nodes.append({"data": {
            "id": nid, "label": scalar(d, "title") or nid, "type": typ,
            "description": scalar(d, "description") or "",
            "resource": scalar(d, "resource") or "",
            "tags": seq(d, "tags"),
            "color": PALETTE.get(typ, "#999999"),
            "size": min(30 + len(body) // 200, 90)}})
        bodies[nid] = body
    edges = []
    for nid in docs:
        rel, d, body = docs[nid]
        targets, seen = [], set()
        for t in [m.group(1) for m in _LINK.finditer(body)] + seq(d, "related"):
            tid = to_id(t, rel, bundle)
            if tid and tid in docs and tid != nid and tid not in seen:
                seen.add(tid); targets.append(tid)
        for tid in targets:
            edges.append({"data": {"id": f"{nid}__{tid}", "source": nid, "target": tid}})
    return {"nodes": nodes, "edges": edges, "bodies": bodies,
            "types": sorted({n["data"]["type"] for n in nodes}), "palette": PALETTE}

def render(bundle: Path, template: str) -> str:
    return (template.replace("@@BUNDLE_NAME@@", bundle.name)
                    .replace("@@BUNDLE_JSON@@", json.dumps(build(bundle))))

TEMPLATE = Path(__file__).with_name("viz_template.html")


def main(argv):
    if not argv:
        print(__doc__.strip().splitlines()[0]); return 2
    bundle = Path(argv[0])
    check = "--check" in argv[1:]
    out = render(bundle, TEMPLATE.read_text(encoding="utf-8"))
    target = bundle / "viz.html"
    if check:
        cur = target.read_text(encoding="utf-8") if target.exists() else None
        if cur == out:
            print(f"{bundle.name}: viz.html is current"); return 0
        print(f"{bundle.name}: viz.html is STALE"); return 1
    target.write_text(out, encoding="utf-8")
    print(f"{bundle.name}: wrote {target} ({len(out)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
