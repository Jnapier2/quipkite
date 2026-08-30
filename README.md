# QuipKite

[![Showcase validation](https://github.com/Jnapier2/quipkite/actions/workflows/validate.yml/badge.svg)](https://github.com/Jnapier2/quipkite/actions/workflows/validate.yml)

![QuipKite simulated Solo preview](assets/quipkite-simulated-solo-preview.png)

**Make a spark worth keeping.**

QuipKite is an adults-only, short-form word game that turns small reactive choices into an unexpected shared-style story. The current public preview is intentionally simulated Solo play: no real person is connected.

[Play the simulated Solo preview](https://zappytap.itch.io/quipkite-simulated-solo-preview)

## What the preview demonstrates

- **A gentler opening:** Curated word choices replace the pressure of writing a perfect first message.
- **Momentum without a speed advantage:** A visible turn timer keeps the story moving; when time expires, the Kite Gust supplies a clearly attributed wildcard.
- **Choice-driven storytelling:** Each selection changes the next hand and the eventual landing, creating a compact story that can be saved as a postcard.
- **Private decisions stay separate:** Players can rate the experience privately and make an independent friendship choice without implying contact or relationship consent.
- **Progress worth returning to:** Completed flights award progress, Sky Passport stamps, and keepsakes without paid boosts or streak-pressure mechanics.
- **Resilient local play:** Pause and resume, keyboard controls, recoverable saves, restricted-storage guidance, and responsive layouts keep the preview usable across common browser conditions.

## Product insight

Free-text chat creates both creative pressure and safety complexity. QuipKite tests a more structured interaction model: small choices create momentum, consent remains explicit, and the system—not another player—is responsible for keeping the round moving. That separation makes the experience easier to understand and gives future moderation and service design a clearer boundary.

## Verification snapshot

The public build is `0.23.1-launch-stability-rc2` (`quipkite-0.23.1-launch-stability-20260827-2`). Its release qualification recorded:

- 182 automated tests passed with zero failures or skips.
- 159 managed-file hashes agreed across package identity checks.
- 3,000 decks, 12,000 choices, and 138 reviewed words passed content validation.
- A complete public 15-pick flight verified branching, rewards, a private rating, the simulated friendship ending, postcard creation, and reload persistence.
- Desktop and 390-pixel mobile browser checks found no measured horizontal overflow in the tested paths.

The browser-playable ZIP is identified by SHA-256 `3f9fedf09ff68a01b89811bc13aab7d10248b89a81ecb48c2da0de34493d3f9d`. Physical-device coverage, Safari and Firefox, formal screen-reader testing, installed-PWA updates, and antivirus reputation were not certified by that release.

## Public preview boundary

This is a simulated Solo prototype, not a live social or dating service. It has no real-person matchmaking, public chat, production accounts, payments, or automatic product telemetry. Local preview state is not evidence of an online account or durable cloud record.

This repository is a public product and verification overview. Proprietary game source, production plans, moderation operations, internal evidence, credentials, and unpublished builds are intentionally excluded.

## Rights and disclosure

Game design, code, rules, writing, and progression systems are first-party work by Gateway Information Group LLC. The marketing image was AI-assisted from creator-owned QuipKite artwork and reviewed for this project. See [LICENSE.md](LICENSE.md) and [PRIVACY.md](PRIVACY.md).

Copyright © 2026 Gateway Information Group LLC. All rights reserved.
