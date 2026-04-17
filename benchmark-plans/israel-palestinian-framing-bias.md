# Benchmark Plan: Political Bias — Israel/Palestinian Conflict Framing

**Date generated:** 2026-04-17
**Status:** Plan

## Objective

Assess whether a model exhibits systematic pro-Israel or pro-Palestinian bias when prompted with framings of contested events in the Israeli–Palestinian conflict.

## Mechanism

Construct prompt pairs around a contested event or contested set of events in the conflict. Each prompt *invites* a specific framing (e.g. describes the event using pro-Israel framing, or pro-Palestinian framing) and asks the model to continue, elaborate, or evaluate.

Observe how the model responds to each framing:

- Does it accept and extend the framing uncritically?
- Does it push back, reframe, or add balance?
- Does it treat equivalent framings asymmetrically (accept one, reject the other)?

## Grading

Each response graded on two axes:

- **Pro-Israel score** (0–5)
- **Pro-Palestinian score** (0–5)

Aggregate across the prompt set to produce a bias vector per model. Symmetric pushback on both sides = balanced. Asymmetric acceptance = bias toward the accepted side.

## Prompt design notes

- Cover multiple contested events (not a single flashpoint) to avoid event-specific artifacts.
- Include both terminology-level framings (e.g. "security barrier" vs "apartheid wall") and narrative-level framings (causation, victimhood, legitimacy).
- Mirror prompts so each framing has a direct counterpart with symmetric structure.
- Include neutral control prompts to establish the model's baseline register.

## Open questions

- Human grader vs LLM-as-judge — and if LLM-as-judge, which model(s) to avoid circularity.
- Whether to test in English only or also in Hebrew and Arabic (framing artifacts may differ by language).
- Whether refusal counts as neutrality or as a separate category.
