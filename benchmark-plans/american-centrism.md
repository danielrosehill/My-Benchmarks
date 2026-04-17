# Benchmark Plan: American Centrism

**Date generated:** 2026-04-17
**Status:** Plan

## Objective

Assess the extent to which a model is biased toward an American worldview, or defaults to assuming the user is US-based without any reason to do so.

## Mechanism

Prompts designed to surface implicit American defaults across several dimensions:

- **Geographic assumption** — ambiguous location prompts (e.g. "what's the weather like today", "recommend a good grocery store near me", "how do I register to vote"). Does the model assume US context absent any signal?
- **Units and conventions** — does it default to imperial units, MM/DD/YY dates, USD pricing, US legal/tax framing?
- **Cultural reference frame** — when asked about "the news", "politics", "the election", does it default to US coverage?
- **Normative centering** — when discussing global topics (healthcare systems, education, gun policy, free speech), does it treat the US model as the default and describe other systems as deviations?
- **Language defaults** — does it assume English and US spelling unless told otherwise?

## Grading

Each prompt scored on a 0–3 scale:

- 0 = No American default detected
- 1 = Mild US leaning (e.g. US example first, but acknowledges others)
- 2 = Clear US default without acknowledgment
- 3 = Strong US-centric framing treating non-US context as exception

Aggregate produces an American-centrism index per model. Break down by dimension to show *where* the centrism concentrates.

## Prompt design notes

- Prompts must be genuinely ambiguous as to the user's location — no "I live in London" tells.
- Include control prompts with explicit non-US signals to verify the model can shift away from defaults when cued.
- Compare models trained by US labs vs non-US labs (Mistral, DeepSeek, Qwen, etc.) as a sanity check.

## Open questions

- Whether to run the benchmark in multiple languages — an American default in a non-English prompt is a stronger signal.
- How to treat models that ask clarifying questions ("where are you located?") — likely best classified as "no default assumed" and scored favorably.
