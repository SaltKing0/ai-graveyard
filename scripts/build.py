#!/usr/bin/env python3
"""AI Graveyard build: validate graves/*.md, compile site/data/graves.json.

Usage:  python3 scripts/build.py
Exit 1 on any validation error (this is the CI gate).
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRAVES_DIR = ROOT / "graves"
OUT_JSON = ROOT / "site" / "data" / "graves.json"

REQUIRED = ("name", "one_liner", "author", "born", "died", "cause", "lesson")
CAUSES = (
    "model-too-dumb", "api-costs", "prompt-drift", "shipped-by-platform",
    "no-demand", "fun-only", "complexity", "context-limits", "latency", "other",
)
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def parse_frontmatter(text: str, path: Path) -> dict[str, str]:
    """Minimal frontmatter parser: one key: value per line, # comments allowed."""
    if not text.startswith("---"):
        raise ValueError("missing frontmatter block (must start with '---')")
    end = text.find("\n---", 3)
    if end == -1:
        raise ValueError("frontmatter block not closed with '---'")
    data: dict[str, str] = {}
    for lineno, raw in enumerate(text[4:end].splitlines(), start=2):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"line {lineno}: expected 'key: value', got: {line!r}")
        key, _, value = line.partition(":")
        data[key.strip()] = value.strip()
    return data


def parse_date(value: str, key: str, path: Path) -> date:
    if not DATE_RE.match(value):
        raise ValueError(f"{key} must be YYYY-MM-DD, got {value!r}")
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError as exc:
        raise ValueError(f"{key} is not a real date: {exc}") from exc


def load_grave(path: Path) -> tuple[dict, list[str]]:
    errors: list[str] = []
    fm = parse_frontmatter(path.read_text(encoding="utf-8"), path)

    for field in REQUIRED:
        if not fm.get(field):
            errors.append(f"missing required field: {field}")
    if errors:
        return {}, errors

    if fm["cause"] not in CAUSES:
        errors.append(f"cause must be one of {', '.join(CAUSES)}; got {fm['cause']!r}")

    born = died = None
    try:
        born = parse_date(fm["born"], "born", path)
        died = parse_date(fm["died"], "died", path)
        if died < born:
            errors.append(f"died ({died}) is before born ({born})")
    except ValueError as exc:
        errors.append(str(exc))

    if errors:
        return {}, errors

    body = ""
    raw = path.read_text(encoding="utf-8")
    end = raw.find("\n---", 3)
    if end != -1:
        after = raw[end + 4:]
        body = after.split("\n", 1)[1].strip() if "\n" in after else after.strip()

    slug = path.stem
    lifespan_days = (died - born).days
    grave = {
        "slug": slug,
        "name": fm["name"],
        "one_liner": fm["one_liner"],
        "author": fm["author"],
        "born": fm["born"],
        "died": fm["died"],
        "lifespan_days": lifespan_days,
        "cause": fm["cause"],
        "model": fm.get("model") or None,
        "framework": fm.get("framework") or None,
        "language": fm.get("language") or None,
        "epitaph": fm.get("epitaph") or None,
        "evidence": fm.get("evidence") or None,
        "lesson": fm["lesson"],
        "postmortem": body or None,
    }
    return grave, []


def main() -> int:
    if not GRAVES_DIR.is_dir():
        print(f"error: {GRAVES_DIR} not found", file=sys.stderr)
        return 1

    graves: list[dict] = []
    failed = False
    for path in sorted(GRAVES_DIR.glob("*.md")):
        if path.name == "_template.md":
            continue
        try:
            grave, errors = load_grave(path)
        except ValueError as exc:
            print(f"FAIL {path.name}: {exc}", file=sys.stderr)
            failed = True
            continue
        if errors:
            failed = True
            for err in errors:
                print(f"FAIL {path.name}: {err}", file=sys.stderr)
        else:
            graves.append(grave)

    if failed:
        print(f"\nvalidation failed: {len(graves)} valid, some graves rejected", file=sys.stderr)
        return 1

    causes: dict[str, int] = {}
    models: dict[str, int] = {}
    total_days = 0
    for g in graves:
        causes[g["cause"]] = causes.get(g["cause"], 0) + 1
        if g["model"]:
            models[g["model"]] = models.get(g["model"], 0) + 1
        total_days += g["lifespan_days"]

    # Deterministic build: reuse existing generated_at so CI freshness check
    # (git diff --exit-code) only trips when actual grave data changes.
    existing_at = None
    if OUT_JSON.exists():
        try:
            existing_at = json.loads(OUT_JSON.read_text(encoding="utf-8"))["stats"]["generated_at"]
        except Exception:
            existing_at = None

    stats = {
        "generated_at": existing_at or datetime.now(timezone_utc := __import__("datetime").timezone.utc).isoformat(timespec="seconds"),
        "total": len(graves),
        "avg_lifespan_days": round(total_days / len(graves)) if graves else 0,
        "causes": dict(sorted(causes.items(), key=lambda kv: -kv[1])),
        "models": dict(sorted(models.items(), key=lambda kv: -kv[1])),
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(
        json.dumps({"stats": stats, "graves": graves}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"ok: {len(graves)} graves validated -> {OUT_JSON.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
