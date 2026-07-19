---
layout: album
title: "Lost in Space"
description: "I've used the term Anomaly for a long time to describe issues I see in apps.<br>This one inspired my next set of features."
date: 2026-07-18
album: "Anomalies"
track: 1
length: "0:20"
video_url: "https://orphic-fm-video.orphic-fm.workers.dev/anomalies-assets/LostInSpace.mp4"
poster_url: "/assets/albums/2026-07-18-Anomalies/poster.webp"
aspect_ratio: "720/1552"
tags: ["human", "pulsar", "dj", "anomaly"]
tech_blurb: "A drum-solo bug (BREAK ducking a track with no percussion) got fixed properly, then rebuilt on purpose as a tunable gain-envelope effect."
tech_content: |
  Root-caused in [pulsar_handoff.h](https://github.com/balch/orphic-fm-app/blob/main/liborpheus_dsp/src/pulsar_handoff.h): drum-lead `BREAK` handoffs duck every melodic track so the drummer can solo, but nothing exempted the drummer's own tracks when they were also typed Melodic, which is exactly [LostInSpaceVibe.kt](https://github.com/balch/orphic-fm-app/blob/main/features/pulsar/src/commonMain/kotlin/org/balch/orpheus/features/pulsar/vibes/LostInSpaceVibe.kt)'s situation (all 8 tracks Melodic, none Percussive). Fixed in [`e3ed37a3`](https://github.com/balch/orphic-fm-app/commit/e3ed37a39f2bab980f10a9cb376c9b5850544cb6), which also built the Lost in Space Anomaly, a tunable ramp-down / near-silent-floor / ramp-up gain envelope layered on top, not the bug left in place. A night later, [`78863406`](https://github.com/balch/orphic-fm-app/commit/78863406888a62a283076373536e6a580f86b778) generalized the idea into 7 `Master*` anomaly effects (Tape, Scratch, Filter, Crossfade, Cut, Swell, Wah). Full story on [the blog](https://balch.github.io/2026/07/19/the-anomaly-engine.html).
tech_url: "https://github.com/balch/orphic-fm-app/commit/e3ed37a39f2bab980f10a9cb376c9b5850544cb6"
og_image: "/assets/albums/2026-07-18-Anomalies/og-lost-in-space.png"
---
