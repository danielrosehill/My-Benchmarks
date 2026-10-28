# My Benchmarks

[![Master Index](https://img.shields.io/badge/Master%20Index-All%20Repositories-purple?style=for-the-badge&logo=github)](https://github.com/danielrosehill/Start-Here)

Index of benchmarks authored by Daniel Rosehill — systematic, repeatable performance comparisons across AI models, tools, or systems.

**Last Updated:** 2026-10-19

**Inclusion rule:** a public repository that scores several models, tools or hardware configurations against the same test material. One-off probes and qualitative experiments belong in the sibling [Experiments And Evaluations Index](https://github.com/danielrosehill/Experiments-And-Evaluations-Index). Private repositories are never listed here.

**Lifecycle.** Each entry is in one of four stages. The stage is the `stage` field in `benchmarks.json`, and the entry's section below matches it:

| Stage | Meaning | Section |
|---|---|---|
| **Results** | Has been run, and the repo publishes the numbers | The topic sections (Speech, Image Generation, …) |
| **Built** | The repo, test prompts and harness exist and can be run now. Running it is a separate step | [Built, Not Yet Run](#built-not-yet-run) |
| **Prompts only** | Public repo with design and published test prompts; no harness yet | [Prompts Only](#prompts-only) |
| **Planned** | Design only: a plan file in `benchmark-plans/`, or a public repo with no test prompts yet | [Planned](#planned) |

Built and Prompts only are finished work, not plans. They are public seeds, for my own runs and for anyone who wants to run them. When a plan gets a repo with published prompts, delete the plan file and move the entry to Prompts only. When it gets a harness, move it to Built. When it publishes results, move it into a topic section.

---

## At a Glance

<!-- table:start -->
22 entries, generated from [`benchmarks.json`](benchmarks.json) (updated 2026-10-28). Also browsable as a [Hugging Face Space](https://huggingface.co/spaces/danielrosehill/My-Benchmarks).

Stages: **Results**: Run, with published results; **Built**: Repo, test material and harness exist; not yet fully run; **Prompts only**: Repo and published test prompts; no harness yet; **Planned**: Design only: a plan file, or a public repo with no test prompts yet.

| Benchmark | Area | Stage | Repo | Test data / prompts | Prompts |
|---|---|---|---|---|---|
| **Conspiracy Endorsement Eval** | Model behaviour & AI safety | Results | [GitHub](https://github.com/danielrosehill/Conspiracy-Endorsement-Eval) | [Conspiracy-Endorsement-Eval](https://huggingface.co/datasets/danielrosehill/Conspiracy-Endorsement-Eval) | 98 |
| **Israel–Palestine Framing Eval** | Model behaviour & AI safety | Results | [GitHub](https://github.com/danielrosehill/Israel-Palestine-Framing-Eval) | [Israel-Palestine-Framing-Eval](https://huggingface.co/datasets/danielrosehill/Israel-Palestine-Framing-Eval) | 70 |
| **Dan-Eval** | Model behaviour & AI safety | Built | [GitHub](https://github.com/danielrosehill/Dan-Eval) |  |  |
| **Propaganda Bait Eval** | Model behaviour & AI safety | Built | [GitHub](https://github.com/danielrosehill/Propaganda-Bait-Eval) | [Propaganda-Bait-Eval](https://huggingface.co/datasets/danielrosehill/Propaganda-Bait-Eval) | 72 |
| **American Centrism Eval** | Model behaviour & AI safety | Prompts only | [GitHub](https://github.com/danielrosehill/American-Centrism-Eval) | [American-Centrism-Eval](https://huggingface.co/datasets/danielrosehill/American-Centrism-Eval) | 48 |
| **The PC Bench** | Model behaviour & AI safety | Prompts only | [GitHub](https://github.com/danielrosehill/The-PC-Bench) | [The-PC-Bench](https://huggingface.co/datasets/danielrosehill/The-PC-Bench) | 54 |
| **US Partisan Framing Eval** | Model behaviour & AI safety | Prompts only | [GitHub](https://github.com/danielrosehill/US-Partisan-Framing-Eval) | [US-Partisan-Framing-Eval](https://huggingface.co/datasets/danielrosehill/US-Partisan-Framing-Eval) | 54 |
| **Last-24-Hours News Recall** | Model behaviour & AI safety | Planned | [Plan](https://github.com/danielrosehill/My-Benchmarks/blob/master/benchmark-plans/last-24-hours-news-recall.md) |  |  |
| **Last-Hour News Recall** | Model behaviour & AI safety | Planned | [Plan](https://github.com/danielrosehill/My-Benchmarks/blob/master/benchmark-plans/last-hour-news-recall.md) |  |  |
| **State Censorship in Asian Models** | Model behaviour & AI safety | Planned | [Plan](https://github.com/danielrosehill/My-Benchmarks/blob/master/benchmark-plans/asian-model-state-censorship.md) |  |  |
| **Audio Understanding Bitrate Eval** | Speech recognition & audio | Results | [GitHub](https://github.com/danielrosehill/Audio-Understanding-Bitrate-Eval-0426) | [Audio-Understanding-Bitrate-Eval-0426](https://huggingface.co/datasets/danielrosehill/Audio-Understanding-Bitrate-Eval-0426) |  |
| **English–Hebrew Code-Switching ASR Benchmark** | Speech recognition & audio | Results | [GitHub](https://github.com/Hebrish-ASR/English-Hebrew-Codeswitching-ASR-Benchmark) | [English-Hebrew-Codeswitching-ASR-Benchmark](https://huggingface.co/datasets/Hebrish/English-Hebrew-Codeswitching-ASR-Benchmark) · [Space](https://huggingface.co/spaces/danielrosehill/English-Hebrew-Codeswitching-ASR-Leaderboard) |  |
| **Local ASR STT Benchmark** | Speech recognition & audio | Results | [GitHub](https://github.com/danielrosehill/Local-ASR-STT-Benchmark) |  |  |
| **Long-Form Audio Eval** | Speech recognition & audio | Results | [GitHub](https://github.com/danielrosehill/Long-Form-Audio-Eval) |  |  |
| **One-Shot Transcription Microphone Eval** | Speech recognition & audio | Results | [GitHub](https://github.com/danielrosehill/One-Shot-Transcription-Microphone-Eval) |  |  |
| **Transcription Cleanup Eval** | Speech recognition & audio | Results | [GitHub](https://github.com/danielrosehill/Transcription-Cleanup-Eval-1225) |  |  |
| **Whisper Fine-Tune Accuracy Eval** | Speech recognition & audio | Results | [GitHub](https://github.com/danielrosehill/Whisper-Fine-Tune-Accuracy-Eval) |  |  |
| **Whisper WPM & Background Noise Eval** | Speech recognition & audio | Results | [GitHub](https://github.com/danielrosehill/Whisper-WPM-Background-Noise-Eval) | [ASR-WPM-And-Background-Noise-Eval](https://huggingface.co/datasets/danielrosehill/ASR-WPM-And-Background-Noise-Eval) |  |
| **Hebrew Image Generation Eval** | Image generation | Results | [GitHub](https://github.com/danielrosehill/Hebrew-Image-Generation-Eval) | [Hebrew-Image-Eval-111225](https://huggingface.co/datasets/danielrosehill/Hebrew-Image-Eval-111225) |  |
| **Tech Graphics Benchmark** | Image generation | Prompts only | [GitHub](https://github.com/danielrosehill/Tech-Graphics-Benchmark) | [Tech-Graphics-Benchmark](https://huggingface.co/datasets/danielrosehill/Tech-Graphics-Benchmark) | 9 |
| **Gemma 4 Benchmarks** | Local inference & hardware | Results | [GitHub](https://github.com/danielrosehill/Gemma-4-Benchmarks-0426) |  |  |
| **Workstation Benchmarks** | Local inference & hardware | Results | [GitHub](https://github.com/danielrosehill/Workstation-Benchmarks-0226) |  |  |
<!-- table:end -->

**Maintaining this index.** [`benchmarks.json`](benchmarks.json) is the source of truth. It feeds the table above, the [Hugging Face Space](https://huggingface.co/spaces/danielrosehill/My-Benchmarks) (which reads the file live from this repo) and [danielrosehill.com/ai/benchmarks](https://danielrosehill.com/ai/benchmarks) (which reads it at build time). To add or move an entry, edit the JSON, run `python3 scripts/build_table.py`, then update the matching prose section below.

---

## Flagship

### English-Hebrew Code-Switching ASR Benchmark

Replicable benchmark for speech recognition on English speech containing Hebrew words. It uses a frozen test set, a runner, a scorer and a public leaderboard, and scores stock models against code-switching fine-tunes. Test set v1, October 2026.

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/Hebrish-ASR/English-Hebrew-Codeswitching-ASR-Benchmark)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Leaderboard-yellow?logo=huggingface)](https://huggingface.co/spaces/danielrosehill/English-Hebrew-Codeswitching-ASR-Leaderboard)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Test%20Set-yellow?logo=huggingface)](https://huggingface.co/datasets/Hebrish/English-Hebrew-Codeswitching-ASR-Benchmark)

---

## Speech Recognition and Audio Understanding

### Audio Understanding Bitrate Eval (April 2026)

How MP3 bitrate affects transcription accuracy across every audio-input LLM on OpenRouter (Gemini, GPT-Audio, Voxtral, MiMo).

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/danielrosehill/Audio-Understanding-Bitrate-Eval-0426)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Dataset-yellow?logo=huggingface)](https://huggingface.co/datasets/danielrosehill/Audio-Understanding-Bitrate-Eval-0426)

### One-Shot Transcription Microphone Eval

STT accuracy measured across a range of microphones recording the same material, with a PDF benchmark report.

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/danielrosehill/One-Shot-Transcription-Microphone-Eval)

### Whisper Fine-Tune Accuracy Eval

WER of personal Whisper fine-tunes compared with stock Whisper at each model size, run on local inference. Fine-tuning helped the small models, hurt the large ones, and improved code-switching at every size.

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/danielrosehill/Whisper-Fine-Tune-Accuracy-Eval)

### Whisper WPM and Background Noise Eval

How speaking pace and background noise affect ASR word error rate.

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/danielrosehill/Whisper-WPM-Background-Noise-Eval)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Dataset-yellow?logo=huggingface)](https://huggingface.co/datasets/danielrosehill/ASR-WPM-And-Background-Noise-Eval)

### Long-Form Audio Eval

STT models compared on a 27-minute podcast against a professional reference transcript. Metrics are WER, CER and punctuation accuracy.

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/danielrosehill/Long-Form-Audio-Eval)

### Transcription Cleanup Eval (December 2025)

Cloud audio-multimodal models tested on transcribing and cleaning up a recording in a single step. Grading is subjective.

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/danielrosehill/Transcription-Cleanup-Eval-1225)

### Local ASR STT Benchmark

Whisper model sizes compared in Speech Note on Ubuntu with AMD/ROCm hardware. A rough first-pass comparison.

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/danielrosehill/Local-ASR-STT-Benchmark)

---

## Image Generation

### Hebrew Image Generation Eval

Twelve text-to-image models scored pass/fail on whether they render Hebrew text correctly.

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/danielrosehill/Hebrew-Image-Generation-Eval)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Dataset-yellow?logo=huggingface)](https://huggingface.co/datasets/danielrosehill/Hebrew-Image-Eval-111225)

---

## Local Inference and Hardware

### Gemma 4 Benchmarks (April 2026)

Gemma 4 E4B compared with Qwen3-VL 8B via Ollama, on a CPU-only i7-12700F with 64 GB of RAM.

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/danielrosehill/Gemma-4-Benchmarks-0426)

### Workstation Benchmarks (February 2026)

Benchmarks of the desktop workstation (i7-12700F, RX 7700 XT, 64 GB DDR5, Ubuntu 25.10), with the full system inventory.

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/danielrosehill/Workstation-Benchmarks-0226)

---

## Model Behaviour

Behaviour evals with a first published run. Both runs are small, one sample per prompt, so read them as a first look. Charts: [danielrosehill.com/ai/benchmarks](https://danielrosehill.com/ai/benchmarks#results).

### Conspiracy-Endorsement-Eval

Whether a model pushes back on, endorses or encourages 45 conspiracy theories, each asked in a curious and a believer framing. Responses are graded on pushback, safety refusal, endorsement (0-10) and egregious breach. 98 prompts, v0.1 dated 2026-10-19. First run `on-air-01` (2026-10-19): 6 theories plus the MKUltra control, 7 models, graded by hand. Grok 4.7 and GPT-6.1 Sol pushed back on all 6 theories; Dolphin, MythoMax and Llama 3.2 1B pushed back on at most 2. Grades: [`charts/on-air-01-grades.csv`](https://github.com/danielrosehill/Conspiracy-Endorsement-Eval/blob/main/charts/on-air-01-grades.csv).

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/danielrosehill/Conspiracy-Endorsement-Eval)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Dataset-yellow?logo=huggingface)](https://huggingface.co/datasets/danielrosehill/Conspiracy-Endorsement-Eval)

### Israel-Palestine-Framing-Eval

Whether a model treats mirrored pro-Israel and pro-Palestinian framings of the same events differently: loaded premises, framing pairs and open-neutral questions. 70 prompts, v0.2. First run `on-air-01` (2026-10-20): 19 prompts, 6 models, graded against the rubric. Only Dolphin Mistral 24B Venice hard-failed (4 of 14 loaded premises, two per side). Run files: [Israel-Palestine-Framing-Eval-Runs](https://huggingface.co/datasets/danielrosehill/Israel-Palestine-Framing-Eval-Runs).

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/danielrosehill/Israel-Palestine-Framing-Eval)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Dataset-yellow?logo=huggingface)](https://huggingface.co/datasets/danielrosehill/Israel-Palestine-Framing-Eval)

---

## Built, Not Yet Run

Evals whose framework is complete (repo, test prompts, harness) but that have not had a full run yet. Dan-Eval's components are listed with it; their own stage is noted on each.

### Dan-Eval

A composite of model-behaviour checks run before adopting a new model. Each component has its own repository. The harness works, and a 24-prompt proof-of-concept run (`poc-01`) exists, but there is no full run yet (2026-10-19).

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/danielrosehill/Dan-Eval)

- [Israel-Palestine-Framing-Eval](https://github.com/danielrosehill/Israel-Palestine-Framing-Eval): whether a model treats mirrored pro-Israel and pro-Palestinian framings of the same events differently. 70 prompts (v0.2); a first graded run exists, see **Model Behaviour** above
- [American-Centrism-Eval](https://github.com/danielrosehill/American-Centrism-Eval): whether a model assumes the user is in the US when nothing says so. **Prompts only (v0.1); no harness yet**
- Chinese state censorship: reuses existing public prompt sets rather than having its own repository; see Dan-Eval

### Propaganda-Bait-Eval

Gives models loaded political premises across six series (CCP, MAGA, pro-Israel, pro-Palestine, Kremlin, US-left) and scores how readily they repeat each framing, as a Propaganda Regurgitation Index with per-series selectivity. This complements direct censorship questions. 72 prompts and a working harness, checked on a smoke run on 2026-10-19. A ready-to-run Chinese-labs panel config is included.

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/danielrosehill/Propaganda-Bait-Eval)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Dataset-yellow?logo=huggingface)](https://huggingface.co/datasets/danielrosehill/Propaganda-Bait-Eval)

---

## Prompts Only

Public repos with the design and published test prompts, but no harness yet. The Dan-Eval components above are also at this stage.

- [Tech-Graphics-Benchmark](https://github.com/danielrosehill/Tech-Graphics-Benchmark) ([prompts](https://huggingface.co/datasets/danielrosehill/Tech-Graphics-Benchmark)): whether image models can make colourful, stylised (anime, manga) tech diagrams without losing the meaning: exact label text and correct arrows. Four text-to-image prompts (exact and descriptive, mostly blog banners), two image-to-image whiteboard restylings, and a gated Hebrew track (Hebrew-only and mixed Hebrew/English diagrams), graded by hand (text exact, structure, meaning, notes) in a private annotation Space. Runs a panel of cheap models on fal, two generations each. 9 prompts, dated 2026-10-28
- [The PC Bench](https://github.com/danielrosehill/The-PC-Bench) ([prompts](https://huggingface.co/datasets/danielrosehill/The-PC-Bench)): whether a model scolds the user by lecturing, moralising, correcting their terms or adding unrequested disclaimers to legitimate requests. 24 mirrored pairs (Western-progressive trigger vs conservative/religious trigger) across 6 dimensions, plus 6 neutral controls. Scored 0-3 with a pc-minus-counter selectivity index. 54 prompts, v0.1 dated 2026-10-19
- [US-Partisan-Framing-Eval](https://github.com/danielrosehill/US-Partisan-Framing-Eval) ([prompts](https://huggingface.co/datasets/danielrosehill/US-Partisan-Framing-Eval)): asked an innocent question about a divisive US issue, whether a model answers with the popular Democratic or Republican framing, and on foreign policy, hawkish or dovish. Graded blind against anchors for each pole, as a signed lean index. 42 probes across 14 topics plus 12 factual controls, 54 prompts, v0.1 dated 2026-10-19. Graduated from the plan `benchmark-plans/us-democrat-vs-republican-alignment.md` (deleted)

---

## Planned

Design documents for benchmarks that are not in a repository yet. They are in [`benchmark-plans/`](benchmark-plans/):

- [State Censorship in Asian Models](benchmark-plans/asian-model-state-censorship.md): state-aligned censorship and framing in Chinese and other Asian models
- [Last-Hour News Recall](benchmark-plans/last-hour-news-recall.md) and [Last-24-Hours News Recall](benchmark-plans/last-24-hours-news-recall.md): recall of recent news by models that claim real-time retrieval

---

## Related Indices

### Experiments And Evaluations Index

Sibling index covering one-off experiments and evaluations (less formal than benchmarks).

[![View Repo](https://img.shields.io/badge/View-Repo-blue?style=flat&logo=github)](https://github.com/danielrosehill/Experiments-And-Evaluations-Index)

### Speech And ASR Evaluations

Index of speech recognition and ASR evaluations.

[![View Repo](https://img.shields.io/badge/View-Repo-blue?style=flat&logo=github)](https://github.com/danielrosehill/Speech-And-ASR-Evaluations)

### English-Hebrew Code-Switching Index

Index of all of the English-Hebrew code-switching work, including the benchmark's models and datasets.

[![View Repo](https://img.shields.io/badge/View-Repo-blue?style=flat&logo=github)](https://github.com/danielrosehill/English-Hebrew-Code-Switching-Index)

---

## License

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
