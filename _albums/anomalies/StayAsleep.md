---
layout: album
title: "Stay Asleep"
description: "A slow blues vibe on an empty street that needs help waking up. A new viz that shows what's really going on behind the scenes.<br>My homage to a classic."
date: 2026-09-20
album: "Anomalies"
track: 3
length: "2:19"
video_url: "https://orphic-fm-video.orphic-fm.workers.dev/anomalies-assets/StayAsleep.mp4"
poster_url: "/assets/albums/2026-07-18-Anomalies/StayAsleepPoster.png"
aspect_ratio: "1200/1080"
tags: ["human", "pulsar", "dj", "tv", "noir"]
featuredSong: true
tech_blurb: "A one-pass 'sound walk' pulsar vibe — bass, DX keys, street sounds, one spoken line — paired with a purpose-built visualizer: a news broadcast whose face dissolves as the song plays."
tech_content: |
  Built in [`69933cf98`](https://github.com/balch/orphic-fm-app/commit/69933cf985e98a21a52c7bd5020fbcf644c34af6) as [StayAsleepVibe.kt](https://github.com/balch/orphic-fm-app/blob/main/features/pulsar/src/commonMain/kotlin/org/balch/orpheus/features/pulsar/vibes/StayAsleepVibe.kt): a one-pass sound walk that plays once and hands off — OSC bass sliding from the fourth down to the root under a single ringing kick, DX keys answering at twice the bass's rate, off-eighth re-picks in the alley and the chase, street footsteps, a passing train, sirens, and one spoken line held back for the closing `awake` section. That line was tuned in [`0b079532c`](https://github.com/balch/orphic-fm-app/commit/0b079532ce521ac27adfd578ed82bca792a7bba0) and [`c4bf61abc`](https://github.com/balch/orphic-fm-app/commit/c4bf61abcaf5e0dde9729374ad6020e2c3033eb9) so the setup and punchline land once, on the last downbeat, instead of repeating through the chase. A matching visualizer shipped alongside it: [FaceMorphViz.kt](https://github.com/balch/orphic-fm-app/blob/main/features/visualizations/src/commonMain/kotlin/org/balch/orpheus/features/visualizations/viz/FaceMorphViz.kt) draws a news broadcast on an old TV set, rabbit ears and all, whose story graphic is a face that dissolves eyes-first as the song plays — surging on loud passages, snapping to black-and-white on kicks, tearing on drum hits — introduced in [`1c6bb331c`](https://github.com/balch/orphic-fm-app/commit/1c6bb331ca175de6dd8ab443b0494064a20bcfa7).
tech_url: "https://github.com/balch/orphic-fm-app/commit/69933cf985e98a21a52c7bd5020fbcf644c34af6"
og_image: "/assets/albums/2026-07-18-Anomalies/og-stay-asleep.png"
---
