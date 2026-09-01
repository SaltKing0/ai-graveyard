---
name: Fūjin
one_liner: Wind god of Git pushes — wraps git push with automatic multi-remote failover to Gitea/Forgejo/GitLab when GitHub is down
author: SaltKing0
born: 2026-08-20
died: 2026-08-22
status: alive
model: none
framework: none
language: Go
cause: other
epitaph: "Not dead — the wind merely rests between storms."
evidence: https://github.com/SaltKing0/fujin
lesson: When a primary platform goes down, the fix is a queue plus a second remote — not a retry loop. Pushes that land on a failover forge must be resynced back, or the primary drifts.
---

Currently hibernating, not actually dead — the kami family (kagutsuchi,
fujin, raijin) is active and this entry uses the alive status badge.

Fūjin wraps `git push` with automatic multi-remote failover. When
Kagutsuchi (fire) reports the outage, Fūjin (wind) carries your commits
to a failover forge instead of failing. Offline pushes queue in SQLite
and flush when any remote is healthy again, and `fujin resync` carries
failover pushes back to the primary so GitHub never drifts behind.
