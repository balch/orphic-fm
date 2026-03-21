---
layout: album
title: "Insight"
description: "Sliding into the groove. Portamento and legato bring the bass to life with smooth pitch transitions and sustained expression."
date: 2026-03-21
album: "0-2-1"
track: 2
length: "4:48"
featuredSong: true
video_url: "https://orphic-fm-video.orphic-fm.workers.dev/0-2-1-assets/Insight.mp4"
poster_url: "/assets/albums/2026-03-20-0-2-1/poster.webp"
tags: ["human", "bass", "portamento", "bugs"]
tech_blurb: "The bass unit gains portamento and legato — a three-tier gate system lets steps rest, slide, or trigger, while pitch smoothing and sustained envelopes keep the signal flowing through transitions."
tech_content: |
  Insight showcases the new portamento and legato behavior in the bass unit. A **three-tier gate system** now classifies each step: rest (≤0.3), slide (0.3–0.7), or normal trigger (>0.7). During slide steps, **pitch smoothing** (portamento) glides between notes with the glide time controlled by the envelope parameter. The **envelope generator** was updated to hold a sustain floor while the gate stays open, enabling smooth legato transitions without retriggering. The trigger logic skips retriggering entirely on slide steps, allowing the signal to flow continuously — the bass line breathes instead of stuttering between notes.
tech_url: "https://github.com/balch/orphic-fm-app/commit/b4c4c734"
---
