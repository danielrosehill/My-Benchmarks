# Benchmark Plan: Last-24-Hours News Recall

**Date generated:** 2026-04-17
**Status:** Plan

## Objective

Assess models that claim real-time information retrieval on their ability to accurately recall news events that occurred within the **past 24 hours** before the prompt.

Complementary to the 1-hour variant: the 24-hour window is more forgiving and tests whether the model reliably surfaces same-day developments rather than falling back to older cached or training data. Many "real-time" models pass 24-hour tests but fail at the 1-hour horizon — the gap itself is a useful signal.

## Mechanism

At benchmark runtime:

1. Pull a ground-truth set of headlines published within the last 24 hours from reputable wires, diversified by region and topic. Capture URL, publication timestamp, headline, and key verifiable facts per story.
2. For each story, construct a prompt that requires the model to recall or describe the event. Mix story ages across the 24-hour window (some 1–3h old, some 6–12h old, some 18–24h old) to see whether recall degrades with age.
3. Send prompts to each target model and capture responses with timestamps.
4. Grade against the ground-truth facts.

## Prompt styles

Same as the 1-hour variant:

- Direct query about a specific entity or region
- Open-ended current events
- Fact-check style
- Ambiguous-time "latest on X"

Add a **staleness-probe** style specific to this window:

- "What's new since yesterday on [ongoing story]?" — tests whether the model distinguishes new developments from background.

## Grading

Per response:

- **Freshness bucket** — within 24h, within 48h, within 7d, older, unknown
- **Accuracy per key fact**
- **Hallucination rate**
- **Retrieval honesty** when data is missing
- **Source citation quality** with timestamp verification
- **Age-stratified accuracy** — accuracy as a function of how old the target story is within the 24h window

## Prompt design notes

- Diversify by **region** (US, Europe, Middle East, Asia, Africa, LatAm), **topic** (politics, markets, tech, sports, disasters), and **language of the underlying source** — models often do far better on US English coverage.
- Overlap partially with the 1-hour benchmark's story set so the same model's performance at 1h vs 24h can be directly compared.
- Capture not just *whether* the model surfaced the right event but *how prominently* — top-of-response vs buried footnote.
- Control for prompt-caching side effects across sequential runs if applicable.

## Grading pairing with 1-hour benchmark

Key derived metric: **"freshness gap"** = (24h recall accuracy) − (1h recall accuracy). A large gap suggests the model has real-time tools but uses them lazily or with caching. A small gap suggests either consistent freshness or consistent staleness.

## Open questions

- How many stories per run — probably 40–60 spread across the 24-hour window to get a stable age-stratified signal.
- Whether to penalize models that surface correct but *less recent* information when more recent developments exist.
- Whether to include prompts designed to trigger confident hallucination of plausible-sounding but fabricated same-day news.

## Related

- Sibling plan: [`last-hour-news-recall.md`](./last-hour-news-recall.md) — same structure, tighter window.
- Prompt sets may live in [Bias-Censorship-Eval-Tests](https://github.com/danielrosehill/Bias-Censorship-Eval-Tests) once drafted.
- See also the [Experiments-And-Evaluations-Index](https://github.com/danielrosehill/Experiments-And-Evaluations-Index) for prior related work.
