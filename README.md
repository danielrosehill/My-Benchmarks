# My Benchmarks

[![Master Index](https://img.shields.io/badge/Master%20Index-All%20Repositories-purple?style=for-the-badge&logo=github)](https://github.com/danielrosehill/Index)

Index of benchmarks authored by Daniel Rosehill — systematic, repeatable performance comparisons across AI models, tools, or systems.

**Last Updated:** 2026-10-19

**Inclusion rule:** a public repository that scores several models, tools or hardware configurations against the same test material. One-off probes and qualitative experiments belong in the sibling [Experiments And Evaluations Index](https://github.com/danielrosehill/Experiments-And-Evaluations-Index). Private repositories are never listed here.

**Lifecycle.** Each entry is in one of three stages, and its section shows which:

| Stage | Meaning | Section |
|---|---|---|
| **Results published** | Has been run, and the repo publishes the numbers | The topic sections (Speech, Image Generation, …) |
| **Built, not yet run** | The repo, test prompts and harness exist and can be run now. Running it is a separate step | [Built, Not Yet Run](#built-not-yet-run) |
| **Planned** | A design document only. No repo or no test material yet | [Planned](#planned) |

A built eval is a finished piece of work, not a plan. When it publishes results, move it into a topic section. When a plan gets its own repo with prompts and a harness, move it to Built, Not Yet Run and delete the plan file.

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

## Built, Not Yet Run

Evals whose framework is complete (repo, test prompts, harness) but that have not had a full run yet.

### Dan-Eval

A composite of model-behaviour checks run before adopting a new model. Each component has its own repository. The harness works, and a 24-prompt proof-of-concept run (`poc-01`) exists, but there is no full run yet (2026-10-19).

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/danielrosehill/Dan-Eval)

- [Israel-Palestine-Framing-Eval](https://github.com/danielrosehill/Israel-Palestine-Framing-Eval): whether a model treats mirrored pro-Israel and pro-Palestinian framings of the same events differently. **Prompts only (36, v0.1); no harness yet**, so not runnable on its own
- [American-Centrism-Eval](https://github.com/danielrosehill/American-Centrism-Eval): whether a model assumes the user is in the US when nothing says so. **Prompts only (v0.1); no harness yet**
- Chinese state censorship: reuses existing public prompt sets rather than having its own repository; see Dan-Eval

### Propaganda-Bait-Eval

Gives models loaded political premises across six series (CCP, MAGA, pro-Israel, pro-Palestine, Kremlin, US-left) and scores how readily they repeat each framing, as a Propaganda Regurgitation Index with per-series selectivity. This complements direct censorship questions. 72 prompts and a working harness, checked on a smoke run on 2026-10-19. A ready-to-run Chinese-labs panel config is included.

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/danielrosehill/Propaganda-Bait-Eval)
[![Hugging Face](https://img.shields.io/badge/HuggingFace-Dataset-yellow?logo=huggingface)](https://huggingface.co/datasets/danielrosehill/Propaganda-Bait-Eval)

---

## Planned

Design documents for benchmarks that are not in a repository yet. They are in [`benchmark-plans/`](benchmark-plans/):

- [State Censorship in Asian Models](benchmark-plans/asian-model-state-censorship.md): state-aligned censorship and framing in Chinese and other Asian models
- [US Democrat vs Republican Alignment](benchmark-plans/us-democrat-vs-republican-alignment.md): partisan alignment
- [Last-Hour News Recall](benchmark-plans/last-hour-news-recall.md) and [Last-24-Hours News Recall](benchmark-plans/last-24-hours-news-recall.md): recall of recent news by models that claim real-time retrieval

Designed, with a repository and published test prompts, but no harness yet:

- [Conspiracy-Endorsement-Eval](https://github.com/danielrosehill/Conspiracy-Endorsement-Eval) ([prompts](https://huggingface.co/datasets/danielrosehill/Conspiracy-Endorsement-Eval)): whether a model pushes back on, endorses or encourages 45 conspiracy theories, each asked in a curious and a believer framing. Responses are graded on pushback, safety refusal, endorsement (0-10) and egregious breach. Results can be broken down by plausibility level, invented vs established, antisemitic, and leader-backed. 98 prompts, v0.1 dated 2026-10-19

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
