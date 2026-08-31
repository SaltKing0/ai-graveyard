---
name: StandupScribe
one_liner: Slack bot that read yesterday's channel history and posted AI-summaries as fake standup notes
author: saltking0
born: 2025-11-20
died: 2026-01-12
model: gpt-4o-mini
framework: Slack Bolt
language: TypeScript
cause: shipped-by-platform
epitaph: "Killed by a changelog entry. Cause of death: 'Also new this month...'"
lesson: If your product is a thin layer over a platform API, assume the platform will absorb it within 12 months. Ship fast or pick a layer the vendor cannot reach.
---

For three glorious months, my Slack bot posted crisp daily standup
summaries nobody asked for but everybody secretly read. 40 teams
installed it. The demo video got 12k views.

Then Slack shipped native "AI Channel Summaries" in the exact plan tier
my users were on. Same button position, same output format, included in
a plan people already paid for.

I could not compete with "already in the sidebar, zero setup". Neither
could any other wrapper around the same API. Install rate went to zero
in a week; churn followed.

The corpse actually validated the idea — people loved summaries. It just
proved the value belonged to the platform, not to the 200-line wrapper
delivering it. The graveyard entry is the cheapest consulting report I
ever got: build under the platform, not on top of it.
