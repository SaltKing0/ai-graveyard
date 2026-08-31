---
name: QueryBeast
one_liner: RAG chatbot over our Notion workspace so the team could "just ask the wiki"
author: saltking0
born: 2026-02-10
died: 2026-04-18
model: gpt-4o
framework: LangChain
language: Python
cause: prompt-drift
epitaph: "It answered correctly exactly once. The team still talks about it like a comet."
lesson: RAG quality is 90% chunking and evaluation, 10% prompt. I built zero evals, so every "fix" was vibes — and half of them silently regressed other queries.
evidence: https://github.com/saltking0/querybeast
---

Built it in a weekend, demo went great. The system prompt was basically a
personality cult around "always cite the source".

Week two: teammates started asking real questions. It hallucinated a
vacation policy with impressive confidence. I patched the prompt. That
broke the HR questions. I patched again. Two weeks later the prompt was
300 lines long and I was afraid to touch it.

The kill shot: someone asked the same question twice and got two
different answers. Not slightly different — completely different. I had
no eval set, so I literally could not tell if my latest prompt change had
made things better or worse. I was tuning a machine with no gauge.

Shut it down on a Tuesday. The Notion search bar, it turns out, had a
100% answer rate.
