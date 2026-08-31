---
# ── Grabstein-Daten ──────────────────────────────────────────
# Copy this file to:  graves/<project-slug>.md
# Fill in every required field (*). Keep values on ONE line.
# Long text (the story) belongs in the body below the frontmatter.

name: MyProjectName                        # * project name
one_liner: What it did, in one sentence    # *
author: your-github-handle                 # * or "anonymous"
born: 2026-01-15                           # * start date (YYYY-MM-DD, best guess is fine)
died: 2026-03-02                           # * date you gave up (YYYY-MM-DD)
model: gpt-4o                              # main model (optional)
framework: LangChain                       # main framework (optional)
language: Python                           # main language (optional)
cause: api-costs                           # * exactly one of:
#     model-too-dumb      model was too weak for the use case
#     api-costs           API costs exploded
#     prompt-drift        not reproducible / quality drifted
#     shipped-by-platform the model vendor shipped it natively
#     no-demand           worked technically, nobody wanted it
#     fun-only            fun project, motivation faded
#     complexity          complexity / maintenance hell
#     context-limits      context window killed it
#     latency             too slow to be useful
#     other
epitaph: "R.I.P. — one funny sentence for the tombstone"   # optional, but encouraged
evidence: https://github.com/you/project   # repo / screenshot URL (optional)
lesson: What you would do differently next time            # * this is the gold
---

# Postmortem (optional, free text)

What happened, in your own words. What worked, where it went wrong,
and the moment you knew it was over. Max ~500 words — future you
(and everyone else) says thanks.
