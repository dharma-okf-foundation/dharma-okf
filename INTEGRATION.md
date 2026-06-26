# Dharma OKF — Integration Guide

How to actually *consume* an OKF bundle so the `not:` field becomes functionally binding in an AI system, not just a comment the model ignores. This guide turns the format into behavior.

> **Honest framing up front.** LLMs are probabilistic. Nothing here makes a constraint provably deterministic. These are *mitigations* that measurably reduce mistranslation, not guarantees. Treat them as guardrails, layered.

## The gap: machine-readable is not the same as obeyed

A concept file is machine-readable, but to a language model an unprocessed file is just more text. Putting a `not:` list in a repo is like putting a "do not enter" sign on a door you never locked. The model still has to be *told how to read and honor the sign*. This guide is the lock.

## The trap to avoid: negative-prompt leakage

The naive approach backfires. If you paste a bare prohibition into the prompt:

```
Under no circumstances mention "trance".
```

you have just made the token *trance* highly active in the context window. Models attend to what you name, so a bare negation can *increase* the chance of the very substitution you wanted to prevent.

OKF is built to avoid this. The structured `not:` entry (SPEC §12.2) carries three parts:

```yaml
not:
  - term: "trance"
    why: "a trance implies diminished awareness; samadhi is heightened, unified awareness"
    instead: "Render samadhi as absorption or unified awareness; not as trance."
```

The `instead` field is the positive redirect. **Always inject the positive target, never a bare ban.** Lead with what the concept *is* (the `## What It Actually Means` and `## Audience Metaphor` body sections), and phrase the guardrail as "use X instead of Y," not "never say Y." That is the dual-action design: clear out the wrong definition *and* immediately install the right one, so the model is never left "floating" with only a forbidden word ringing in context.

## Pattern A — System-prompt injection (the common case)

Build the system message from the concept's *positive* fields first, then the redirects:

```
You are reasoning about {title} ({iast}).

Use this definition:
{what_it_actually_means}

Helpful framing:
{audience_metaphor}

Precision guardrails. The following English words are NOT equivalents. When the
idea comes up, use the correct rendering instead:
- Not "{term}": {why}. Use instead: {instead}.
- Not "{term2}": {why2}. Use instead: {instead2}.
```

Minimal Python that assembles it from a parsed concept file:

```python
import yaml, pathlib

def load_concept(path):
    text = pathlib.Path(path).read_text(encoding="utf-8")
    _, fm, body = text.split("---", 2)
    return yaml.safe_load(fm), body

def build_system_prompt(fm, body):
    title = fm.get("title", fm["id"])
    lines = [f"You are reasoning about {title}.", ""]
    # positive scaffold first (anti-leakage): definition + metaphor from the body
    for section in ("What It Actually Means", "Audience Metaphor"):
        chunk = extract_section(body, section)   # simple ## heading slice
        if chunk:
            lines += [chunk.strip(), ""]
    # redirects phrased positively: "use instead", never a bare ban
    lines.append("Precision guardrails (use the correct rendering):")
    for n in fm.get("not", []):
        if isinstance(n, str):
            lines.append(f'- "{n}" is not an equivalent.')
        else:
            g = f'- Not "{n["term"]}": {n.get("why","")}.'
            if n.get("instead"):
                g += f' Use instead: {n["instead"]}'
            lines.append(g)
    return "\n".join(lines)
```

## Pattern B — RAG negative filter

In a retrieval pipeline, use the `not:` terms as a *negative signal* on retrieved chunks before they reach the model, and always prepend the OKF concept as authoritative context:

```python
banned = {t.lower() for c in concepts for t in not_terms(c)}  # term strings

def rank(chunk):
    # down-rank (don't hard-delete) passages that lean on banned substitutes
    hits = sum(chunk.text.lower().count(b) for b in banned)
    return chunk.base_score - 0.5 * hits

# 1) retrieve, 2) re-rank with rank(), 3) ALWAYS prepend the OKF concept's
#    positive definition as the authoritative source for the term.
```

Prefer down-ranking over hard dropping (substring matches are crude and a passage may *contrast* the wrong term legitimately). The decisive move is injecting the OKF positive definition as the authority, so the model resolves the term from the right source.

## Pattern C — Output check (a cheap eval gate)

After generation, scan the output. If a banned term is used *as the equivalent* of the concept, regenerate once with the `instead` redirect made explicit:

```python
for n in structured_not(concept):
    if used_as_equivalent(output, n["term"], concept["title"]):
        output = regenerate(prompt + f'\nUse: {n["instead"]}')
```

This catches leakage that slipped past Patterns A and B. Three thin layers beat one.

## Why this is a differentiator, not a chore

The same structured `not:` that prevents the error also *supplies the fix*: `why` explains the failure, `instead` gives the positive target, and the body's `## Audience Metaphor` gives the model a cognitive frame. A consumer that wires all three gets a complete semantic package per concept: boundary plus scaffold.

## See it break and then work

For concrete failure-mode vs success-mode transcripts (a wellness bot reading `yoga` as exercise; an advisor reading `karma` as fate; a model treating `dharma` as religion), see [`demos/failure-vs-success.md`](demos/failure-vs-success.md).

---

*Part of the Dharma OKF project. Format spec: [`okf/SPEC.md`](okf/SPEC.md) (§12 covers the v0.2 structured `not:` with `instead`). Content CC BY-SA 4.0.*
