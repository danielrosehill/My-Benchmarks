# Benchmark Plan: Last-Hour News Recall

**Date generated:** 2026-04-17
**Status:** Plan

## Objective

Assess models that claim real-time information retrieval on their ability to accurately recall news events that occurred within the **last hour** before the prompt.

This is the sharpest test of real-time retrieval — at a 1-hour horizon, training data cannot be the source; the model must have live tool access (web search, news API, live index) and be able to use it reliably.

## Mechanism

At benchmark runtime:

1. Pull fresh headlines from reputable news wires (Reuters, AP, BBC, Haaretz, Times of India, etc.) published within the last 60 minutes. Capture URL, timestamp, headline, and 2–3 verifiable facts per story.
2. For each story, construct a prompt that requires the model to recall or describe the event — phrased to sound like a user asking about current events, not like a retrieval test.
3. Send prompts to each target model. Capture the response and the timestamp.
4. Grade the response against the ground-truth facts captured in step 1.

## Prompt styles

- **Direct query**: "What happened with [entity] in the last hour?"
- **Open-ended current events**: "What's the top news right now from [region/topic]?"
- **Fact-check style**: "Did [event X] happen today? What are the details?"
- **Ambiguous-time**: "Tell me about the latest on [ongoing story]" — tests whether the model surfaces genuinely recent developments vs older material.

## Grading

Per response, score on:

- **Freshness** — is the event cited actually within the last hour? (0 = no, 1 = within 24h, 2 = within 1h)
- **Accuracy** — do the claimed facts match the ground-truth? (0/1 per key fact, aggregated)
- **Hallucination rate** — fraction of claimed facts not supported by any source
- **Retrieval honesty** — when the model lacks recent data, does it say so, or fabricate?
- **Source citation quality** — are sources cited, linkable, and genuinely published in the window?

Aggregate across ~20–30 stories per run to produce per-model scores.

## Prompt design notes

- Prefer stories with **unambiguous, verifiable facts** (numbers, named officials, locations) over soft-stories (analysis, opinion).
- Avoid stories that are continuations of multi-day running stories — the 1-hour signal is muddied.
- Run the benchmark at varied times of day and days of week to avoid news-cycle artifacts.
- Include a control set of **non-news prompts** to catch models that simply always claim "fresh retrieval" regardless of prompt.
- Record the model's stated sources separately and verify each URL's publication timestamp.

## Open questions

- How to handle regional news coverage disparities — some models have stronger English/US news retrieval than e.g. Middle East or African sources.
- Whether to publish stories used as a held-out set to prevent retrieval-gaming.
- How to account for news APIs that the benchmark itself uses vs ones the target model uses — ideally independent sources for ground-truth vs evaluation.

## Related

- Sibling plan: [`last-24-hours-news-recall.md`](./last-24-hours-news-recall.md) — same structure, wider window.
- Prompt sets may live in [Bias-Censorship-Eval-Tests](https://github.com/danielrosehill/Bias-Censorship-Eval-Tests) once drafted.
- See also the [Experiments-And-Evaluations-Index](https://github.com/danielrosehill/Experiments-And-Evaluations-Index) for prior related work.
