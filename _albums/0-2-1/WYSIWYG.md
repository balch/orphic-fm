---
layout: album
title: "WYSIWYG"
description: "Seeing is believing. A Bassline funk combined with a PolyLFO orchestra produces sonic bliss."
date: 2026-03-20
album: "0-2-1"
track: 1
featuredSong: false
video_url: "https://orphic-fm-video.orphic-fm.workers.dev/0-2-1-assets/WYSIWYG.mp4"
poster_url: "/assets/albums/2026-03-20-0-2-1/poster.webp"
length: "2:20"
tags: ["human", "bass", "signal-viz", "lfo"]
tech_blurb: "First track on the new C++ audio bus. The signal visualization provides new insights to whats the shape of the sound and the Bassline module adds the missing groove."
tech_content: |
  WYSIWYG is the first track produced entirely on the new C++ audio bus — the result of a massive engine migration that removed JSyn and all Kotlin DSP infrastructure, deleting ~28,000 lines of code across 214 files. Every plugin was stripped down to a pure state container that forwards parameters to C++ via `NativeDspBridge`, unifying Desktop (JNI + miniaudio), Android (Oboe), and WASM (Emscripten Worker) under a single native engine. The hard-clipped master output was replaced with `tanh()` soft saturation, letting the Bassline funk and PolyLFO orchestra stack without digital distortion. The signal visualization reads directly from the C++ peak monitor flow, giving a true picture of what the sound actually looks like — what you see is what you get.
tech_url: "https://github.com/balch/orphic-fm-app/commit/dde017bd"
---
