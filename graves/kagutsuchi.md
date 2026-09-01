---
name: Kagutsuchi
one_liner: Fire god of GitHub outages — TUI reliability monitor with live component status, incident history, own uptime measurement, and outage alerts
author: SaltKing0
born: 2026-08-20
died: 2026-08-22
status: alive
model: none
framework: none
language: Go
cause: other
epitaph: "Not dead — the fire burns through the dark."
evidence: https://github.com/SaltKing0/kagutsuchi
lesson: Do not trust a platform's status page alone. Ping the platform yourself, persist your own uptime numbers, and alert on the difference — vendor status pages lag and understate.
---

Currently hibernating, not actually dead — the kami family (kagutsuchi,
fujin, raijin) is active and this entry uses the alive status badge.

Kagutsuchi is a TUI reliability monitor for GitHub: live status of all
11 services, 90-day incident history, a Red-Squares heatmap, and its own
independent health measurement that pings github.com and api.github.com
every 60s. Outage alerts go to desktop and Telegram, and on recovery the
daemon can trigger fujin flush and raijin run — the kami family chains
itself together.
