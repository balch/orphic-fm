---
layout: album
title: "Handwavey"
description: "MediaPipe + ML + ASL = Maestro Mode. In this master-POS, Orpheus is accompanied by the Ant-Band and conducted for the first time using the new ASL Maestro Feature. This song is sponsored by the Terro."
date: 2026-02-22
album: "Crossing the Chasm"
track: 3
video_url: "https://orphic-fm-video.orphic-fm.workers.dev/crossing-the-chasm-assets/handwavey.mp4"
poster_url: "/assets/albums/2026-02-08-Crossing-The-Chasm/AntBandHandwavey.jpg"
og_image: "/assets/albums/2026-02-08-Crossing-The-Chasm/poster-small.webp"
aspect_ratio: "1006/1080"
tags: ["human", "maestro", "strings", "Ant-Band"]
tech_blurb: "The debut of Maestro Mode. Camera-based hand tracking via MediaPipe landed the day before, and ASL gesture routing was finalized the same day this was recorded."
tech_content: |
  The first track performed using **Maestro Mode** -- conducting the synth with hand gestures via **MediaPipe**. Camera-based hand tracking was added on February 21st, along with CPU-saving inactive DSP plugin disabling. On recording day (Feb 22nd), Maestro Mode was reworked to use **individual voice gating** with Thumbs-Up hold control, ASL gesture control routing was made context-dependent, and state snapshotting was centralized for REPL and gestures. The `core:foundation` module had also been decomposed into specialized modules with a **JVM 21** upgrade just two days prior. The aspect ratio (`1006/1080`) captures the portrait-mode camera view of the hand tracking in action.
tech_url: "https://github.com/balch/orphic-fm-app/commit/a85dacea"
---
