# QuipKite

[![Showcase validation](https://github.com/Jnapier2/quipkite/actions/workflows/validate.yml/badge.svg)](https://github.com/Jnapier2/quipkite/actions/workflows/validate.yml)

![QuipKite simulated Solo preview](assets/quipkite-simulated-solo-preview.png)

**Make a spark worth keeping.**

QuipKite is an adults-only, short-form word game that turns small reactive choices into an unexpected shared-style story. The current public preview is intentionally simulated Solo play: no real person is connected.

[Play the simulated Solo preview](https://zappytap.itch.io/quipkite-simulated-solo-preview)

## What the preview demonstrates

- **A gentler opening:** Curated word choices replace the pressure of writing a perfect first message.
- **A clearer story view:** An illustrated setting, a focused current beat, collapsible history, and an anchored choice dock make the next decision easier to follow. Standard flights use an explicit Send confirmation; selecting a word in a choice-driven story advances it immediately.
- **Choice-driven storytelling:** Each selection changes the next hand and the eventual landing, creating a compact story that can be saved as a postcard.
- **Shared moments without public chat:** Kite Knot reveals a Twin Spark or Crosswind Pair, Bridge Words bring earlier choices back into the story, and reversible depth settings let the tone deepen without locking the player in.
- **Private decisions stay separate:** Players can rate the experience privately and make an independent friendship choice without implying contact or relationship consent.
- **Progress worth returning to:** Completed flights award progress, private Landing Stamps, and keepsakes without paid boosts or streak-pressure mechanics.
- **Resilient local play:** Pause and resume, keyboard controls, recoverable saves, restricted-storage guidance, and responsive layouts keep the preview usable across common browser conditions.

## Product insight

Free-text chat creates both creative pressure and safety complexity. QuipKite tests a more structured interaction model: small choices create momentum, consent remains explicit, and the system—not another player—is responsible for keeping the round moving. That separation makes the experience easier to understand and keeps the boundaries of simulated play explicit.

## Verification snapshot

The current public preview is `0.32.0-storycraft-growth-rc1`. Storycraft connects earned Flight XP to new choices in compact branching stories. Illustrated settings, postcard endings, optional sound and ambience, adjustable text, and Untimed Solo for standard flights remain available.

An October 4, 2026 review verified all 60 recorded payload hashes in the browser package, which contains 61 regular files and one empty directory entry. Its SHA-256 is `CDBEE20B3B446161B74048E9E121128DFB8A8DCEC9C3A664A2257115FE2DB79C`, published as itch.io upload `19560446`. All 61 hosted files were compared with the archive: 60 matched exactly, and the entry page retained the original HTML followed only by the inspected platform loader. This was an artifact and public-delivery review; it did not rerun the application's automated tests or certify physical devices, screen readers, or endpoint-security compatibility.

## Try a short story

Open the [public preview](https://zappytap.itch.io/quipkite-simulated-solo-preview), press **Run game**, and review the age and community prompts. For Storycraft, open **Stories → Explore choice-driven stories → Storycraft**. Selecting a word advances a choice-driven story immediately. Standard flights instead let you select a word and confirm it with **Send**. Try a different choice on another visit and compare how the story unfolds.

The cover above is promotional artwork, not a screenshot of the current interface. The public preview page includes interface images and current play instructions.

## Public preview boundary

This is a simulated Solo prototype, not a live social or dating service. It has no real-person matchmaking, public chat, production accounts, payments, or automatic product telemetry. Local preview state is not evidence of an online account or durable cloud record.

This repository is a public product and verification overview. Proprietary game source, production plans, moderation operations, internal evidence, credentials, and unpublished builds are intentionally excluded.

## Rights and disclosure

Game direction, review, and release ownership are first-party work by Gateway Information Group LLC. Generative tools assisted portions of the code, copy, and marketing artwork; the artwork was derived from creator-owned QuipKite material. See [LICENSE.md](LICENSE.md) and [PRIVACY.md](PRIVACY.md).

Copyright © 2026 Gateway Information Group LLC. All rights reserved.
