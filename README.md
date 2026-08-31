# ⚰️ The AI Graveyard

A public archive of dead AI projects — MVPs, POCs, weekend hacks — and the
lessons they died with. Every gravestone is a single markdown file.

## Why

More AI projects are born (and die) than ever. The code rots in a branch,
the lessons evaporate. This repo turns abandoned projects into structured,
searchable data: what was built, what it died of, what the author learned.

## Contribute

1. Fork / branch
2. Copy `graves/_template.md` → `graves/<project-slug>.md`
3. Fill in the frontmatter (structured facts) + write the postmortem (free text)
4. Open a PR — CI validates the format automatically
5. On merge, the site rebuilds and deploys to GitHub Pages automatically

Rules:

- One project per file, small batches welcome
- Only submit projects you built or have permission to memorialize
- Be honest. The lesson is the point, not the shame.
- Want to stay private? Set `author: anonymous`

## Cause-of-death taxonomy

`model-too-dumb` · `api-costs` · `prompt-drift` · `shipped-by-platform` ·
`no-demand` · `fun-only` · `complexity` · `context-limits` · `latency` · `other`

## Local build

```bash
python3 scripts/build.py   # validates all graves, writes site/data/graves.json
```

Exit code 1 on any validation error (this is the CI gate).

## Site

Static and zero-dependency: `site/index.html` reads `site/data/graves.json`.
Aggregates (cause-of-death ranking, average lifespan, model usage) are
compiled by `scripts/build.py` at build time.

## Roadmap

- **Stage 1 (this repo):** PR-driven graves, static site, CI validation
- **Stage 2:** rich markdown rendering, per-grave permalinks, monthly digest auto-post
- **Stage 3:** submission form with auto-validation, anonymized aggregate API
