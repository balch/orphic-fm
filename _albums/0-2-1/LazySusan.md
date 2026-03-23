---
layout: album
title: "Lazy Susan"
description: "The Leslie Horn Panel adds chorus you can feel with your ears. Headphones on for this one."
date: 2026-03-22
album: "0-2-1"
track: 4
length: "4:01"
video_url: "https://orphic-fm-video.orphic-fm.workers.dev/0-2-1-assets/LazySusan.mp4"
poster_url: "/assets/albums/2026-03-20-0-2-1/LazySusanPoster.png"
og_image: "/assets/albums/2026-03-20-0-2-1/og-lazy-susan.png"
tags: ["human", "leslie", "cowbell"]
tech_blurb: "A dual-rotor Leslie simulation — Linkwitz-Riley crossover splits the signal into horn and drum channels, each with independent rotor inertia and stereo amplitude modulation."
tech_content: |
  Lazy Susan showcases the new Horn (Leslie rotary speaker) DSP effect. The C++ engine splits the input through a **Linkwitz-Riley crossover** into separate horn and drum rotor channels, each spinning with **independent inertia** to model the real-world lag of heavy rotating elements. **Stereo amplitude modulation** recreates the Doppler-like swirl that defines the Leslie sound. On the Kotlin side, a **physics-based animation** drives the rotor visuals in the HornPanel, with tactile controls for Speed, Ratio, Depth, Amount, Mix, and Brake. Rotor phase and audio peaks feed back into the engine's **visualization ring buffers**, so you can watch the rotors spin in sync with what you hear.
tech_url: "https://github.com/balch/orphic-fm-app/commit/77a0b6d3"
---
