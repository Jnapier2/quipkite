# QuipKite

[![Showcase validation](https://github.com/Jnapier2/quipkite/actions/workflows/validate.yml/badge.svg)](https://github.com/Jnapier2/quipkite/actions/workflows/validate.yml)

![QuipKite simulated Solo preview](assets/quipkite-simulated-solo-preview.png)

**Make a spark worth keeping.**

QuipKite is an adults-only, short-form word game that turns small reactive choices into an unexpected shared-style story. The current public preview is intentionally simulated Solo play: no real person is connected.

[Play the simulated Solo preview](https://zappytap.itch.io/quipkite-simulated-solo-preview)

## What the preview demonstrates

- **A gentler opening:** Curated word choices replace the pressure of writing a perfect first message.
- **A focused Play Dock:** The active conversation stays centered, the transcript scrolls independently, and reaction choices remain within reach at the bottom on desktop and mobile layouts.
- **Choice-driven storytelling:** Each selection changes the next hand and the eventual landing, creating a compact story that can be saved as a postcard.
- **Shared moments without public chat:** Kite Knot reveals a Twin Spark or Crosswind Pair, Bridge Words bring earlier choices back into the story, and reversible depth settings let the tone deepen without locking the player in.
- **Private decisions stay separate:** Players can rate the experience privately and make an independent friendship choice without implying contact or relationship consent.
- **Progress worth returning to:** Completed flights award progress, private Landing Stamps, and keepsakes without paid boosts or streak-pressure mechanics.
- **Resilient local play:** Pause and resume, keyboard controls, recoverable saves, restricted-storage guidance, and responsive layouts keep the preview usable across common browser conditions.

## Product insight

Free-text chat creates both creative pressure and safety complexity. QuipKite tests a more structured interaction model: small choices create momentum, consent remains explicit, and the system—not another player—is responsible for keeping the round moving. That separation makes the experience easier to understand and gives future moderation and service design a clearer boundary.

## Verification snapshot

The public build is `0.26.1-play-dock-rc1` (`quipkite-0.26.1-play-dock-20260902-1`). Its release qualification recorded:

- 243 automated tests and 34 focused authority tests passed.
- 232 managed-file hashes agreed across package identity checks.
- 3,000 decks, 12,000 choices, and 138 reviewed words passed content validation.
- TypeScript, ESLint, the five-stage production build, performance budgets, and the production dependency audit passed with zero reported vulnerabilities.
- Four fresh-extraction browser checks at 390×844 and 1280×800 verified the centered conversation, independent transcript, bottom-docked choices, package-local privacy navigation, and no measured horizontal overflow.

The 59-entry browser-playable ZIP is identified by SHA-256 `EAFC51E923D25DD0AE88A42A6933A37DA67F7CE7D198695578E78AC3A38B3A75`. The exact package is public as itch.io upload `19076369`; the prior `0.26.0` upload remains retained as rollback. Physical iOS or Android hardware, Safari and Firefox, formal screen-reader testing, installed-PWA updates, signing, and antivirus reputation were not certified by this release.

## Public preview boundary

This is a simulated Solo prototype, not a live social or dating service. It has no real-person matchmaking, public chat, production accounts, payments, or automatic product telemetry. Local preview state is not evidence of an online account or durable cloud record.

This repository is a public product and verification overview. Proprietary game source, production plans, moderation operations, internal evidence, credentials, and unpublished builds are intentionally excluded.

## Rights and disclosure

Game direction, review, and release ownership are first-party work by Gateway Information Group LLC. Generative tools assisted portions of the code, copy, and marketing artwork; the artwork was derived from creator-owned QuipKite material. See [LICENSE.md](LICENSE.md) and [PRIVACY.md](PRIVACY.md).

Copyright © 2026 Gateway Information Group LLC. All rights reserved.
