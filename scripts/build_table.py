"""Regenerate the "At a glance" table in README.md from benchmarks.json.

Usage: python3 scripts/build_table.py [--check]
--check exits 1 if README.md is out of date, without writing.
"""
import json, pathlib, sys, urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
START, END = "<!-- table:start -->", "<!-- table:end -->"
STAGE_ORDER = ["results", "built", "prompts", "planned"]
CAT_ORDER = ["behaviour", "speech", "image", "hardware"]


def link(url, label):
    return f"[{label}]({url})" if url else ""


def hf_label(url):
    return urllib.parse.urlparse(url).path.split("/")[-1] if url else ""


def render(reg):
    rows = sorted(reg["benchmarks"], key=lambda b: (CAT_ORDER.index(b["category"]), STAGE_ORDER.index(b["stage"]), b["name"]))
    out = [
        f"{len(rows)} entries, generated from [`benchmarks.json`](benchmarks.json) (updated {reg['updated']}). "
        "Also browsable as a [Hugging Face Space](https://huggingface.co/spaces/danielrosehill/My-Benchmarks).",
        "",
        "Stages: " + "; ".join(f"**{v['label']}**: {v['meaning']}" for v in reg["stages"].values()) + ".",
        "",
        "| Benchmark | Area | Stage | Repo | Test data / prompts | Prompts |",
        "|---|---|---|---|---|---|",
    ]
    for b in rows:
        repo = link(b.get("repo"), "GitHub") or link(b.get("plan"), "Plan")
        data = link(b.get("dataset"), hf_label(b.get("dataset")))
        if b.get("space"):
            data = (data + " · " if data else "") + link(b["space"], "Space")
        out.append(
            f"| **{b['name']}** | {reg['categories'][b['category']]} | {reg['stages'][b['stage']]['label']} | {repo} | {data} | {b.get('prompts', '')} |"
        )
    return "\n".join(out)


def main():
    reg = json.loads((ROOT / "benchmarks.json").read_text())
    for b in reg["benchmarks"]:
        assert b["stage"] in reg["stages"] and b["category"] in reg["categories"], b["id"]
    readme = (ROOT / "README.md").read_text()
    head, rest = readme.split(START)
    _, tail = rest.split(END)
    new = f"{head}{START}\n{render(reg)}\n{END}{tail}"
    if "--check" in sys.argv:
        sys.exit(0 if new == readme else 1)
    (ROOT / "README.md").write_text(new)


if __name__ == "__main__":
    main()
