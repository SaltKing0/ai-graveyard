---
name: Raijin
one_liner: Thunder god of CI — runs GitHub Actions workflows locally via act when GitHub Actions is down
author: SaltKing0
born: 2026-08-20
died: 2026-08-21
status: alive
model: none
framework: none
language: Go
cause: other
epitaph: "Not dead — the thunder merely waits for the next storm."
evidence: https://github.com/SaltKing0/raijin
lesson: CI is a service, not a guarantee. If the CI vendor is down, the workflow file itself is the contract — run it locally with the same container steps and report the result back as a check run.
---

Currently hibernating, not actually dead — the kami family (kagutsuchi,
fujin, raijin) is active and this entry uses the alive status badge.

Raijin checks the GitHub statuspage for the Actions component. When it
degrades, raijin runs the workflow file locally via act in a container,
streams the output, and can submit runs to a self-hosted raijin server
that reports a check run back to GitHub. It shares the ghhealth engine
with kagutsuchi and fujin.
