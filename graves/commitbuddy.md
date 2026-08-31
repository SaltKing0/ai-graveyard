---
name: CommitBuddy
one_liner: CLI that watches staged diffs and writes conventional-commit messages
author: anonymous
born: 2026-01-05
died: 2026-02-27
model: claude-sonnet-4
framework: none
language: Rust
cause: api-costs
epitaph: "847 commits summarized beautifully. Not one bill paid."
lesson: Before building any tool that makes an LLM call per user action, model the cost at 100 users and 50 calls/day — not at "me using it once". The unit economics die long before the tech does.
---

It worked great. Fast, small Rust binary, streamed the commit message
into the terminal, people in my team actually installed it. That was the
problem.

I paid for the API key. Ten users, each committing ~15 times a day, each
commit a full diff context. My monthly bill went from coffee money to
"that is a nice dinner for two" in three weeks.

I tried smaller models (quality dropped, users noticed), caching (commit
messages are unique by nature), and a free tier (rate limits made it
useless at 5pm on a Friday).

The honest math: a good commit message is worth maybe 2 cents of value
to a user. The API call cost 4 cents. You cannot build a product on a
negative margin per action, and nobody wants to enter a credit card for
git tooling.

Lesson filed under: the model is a supplier, and suppliers send invoices.
