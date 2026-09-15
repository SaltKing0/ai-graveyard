---
name: Tenjin
one_liner: A self-hosted personal agent harness — REPL, one-shot CLI and always-on gateway in one zero-dependency TypeScript binary
author: SaltKing0
born: 2026-08-21
died: 2026-09-15
status: dead
model: bring-your-own
framework: none
language: TypeScript
cause: complexity, inexperienced
epitaph: "1,956 tests passed. The first real start returned 401."
evidence: https://github.com/SaltKing0/Stealth
lesson: Green tests and closed issues are not evidence that the product works. My definition of done was "issue closed + suite green", and both are satisfiable without a working product. The acceptance gate has to be one path a stranger can run in 60 seconds, verified by a blackbox test that starts the real binary with the real config file and no environment variables. Corollary: a module with no caller is not finished, it is dead code with tests. And the inexperience is part of it — four construction sites for one object, an entry point that every command was appended to, distribution built before checking the name: those are first-timer failure modes, and no amount of test discipline catches them.
---

# Postmortem

Tenjin was a self-hosted personal agent harness in Bun + TypeScript with zero
runtime dependencies: an interactive REPL, a one-shot CLI, and an always-on
gateway with channels, scheduled jobs, heartbeats and a web console. It grew
to 32,413 lines across 153 source files, 153 test files, 1,956 passing tests,
699 commits and ~489 pull requests, of which 487 were closed. It was also the
first codebase of this size I had ever built.

**What worked.** The security and audit layer: a path/command guard, a
five-rung approval mode ladder, risk tiers, secret redaction, workspace
confinement and a JSONL audit trail — 1,970 lines wired into 16+ modules with
~10 dedicated test files. It was the part of the project that was both real
and reachable.

**Where it went wrong.** Four failures, all the same failure.

*The primary path was broken in main and stayed broken.* `src/index.ts:195`
built the `ProviderRegistry` with `undefined` as the keys argument; three
other call sites passed the configured keys correctly. The registry fell back
to `env.OPENAI_API_KEY`, so anyone who configured a provider the documented
way — in `providers.yaml` — got an empty bearer token and a 401 on the REPL,
the one-shot CLI and the TUI. The one-line fix sat open as PR #487 for
eleven days.

*The test suite could not see it.* Every end-to-end test spawned the real
binary with `ANTHROPIC_API_KEY` injected as an environment variable — exactly
the fallback that masked the bug. No test ran the binary with a provider
configured only in the YAML file.

*"Delivered" did not mean "active".* An orphan scan found 11–14 modules that
were built, test-covered and never imported at runtime: the local embedding
strategy, the grounding gate, the memory signals, the session event store,
the routing telemetry, the audit tracing. The product's memory, grounding and
telemetry claims were true in the tests and false in the product.

*Distribution was built for a name it could not have.* The cross-compiled
binary matrix, the one-command installer and the npm publish config were all
merged — for a package name that was already taken on npm. Zero git tags, one
version, and a 35-line changelog covering 487 closed items.

**The moment I knew.** I ran the primary path with my own configuration and
got a 401, after 1,956 tests had passed.

**Root cause.** Tenjin was three projects at once — a personal tool, a
shippable product, and a portfolio piece — and the definition of done was
"issue closed + suite green", which satisfies none of the three. The
architecture (a 1,090-line entry point, four construction sites for the same
registry, 14 unwired modules) is a symptom of that metric, not its cause.

**And I was inexperienced.** This was my first codebase at this scale, and it
shows in ways no test suite can catch: four construction sites for one object
instead of one, an entry point that every new command was appended to,
modules written and tested before anything called them, distribution
infrastructure built before checking whether the name was available. None of
those are architecture decisions anyone makes on purpose. They are what
"add, don't design" looks like when nobody has told you yet that it is a
choice.

**What I'd do differently.** One path a stranger can run in 60 seconds, and
that path is the acceptance gate. Check the name before building
distribution. A module without a caller is not finished. And pick one role
for the project, not three.