---
layout: album
title: "Itchy Scratchy"
description: "New dual turntable module with scratch physics and crossfade bring DJ-style performance to the synth engine."
date: 2026-03-22
album: "0-2-1"
track: 3
length: "2:21"
featuredSong: true
video_url: "https://orphic-fm-video.orphic-fm.workers.dev/0-2-1-assets/ItchyScratchy.mp4"
poster_url: "/assets/albums/2026-03-20-0-2-1/ItchyScratchyPoster.png"
og_image: "/assets/albums/2026-03-20-0-2-1/og-itchy-scratchy.png"
tags: ["human", "dj", "turntable", "scratch"]
tech_blurb: "A full-stack DJ turntable — C++ DSP with circular buffer capture and cubic Hermite interpolation playback, dual decks with per-source selection, and a constant-power crossfader."
tech_content: |
  Itchy Scratchy puts the new DJ turntable front and center. The C++ DSP layer captures audio into a **circular buffer** and plays it back with **cubic Hermite interpolation**, giving scratches that warm, vinyl-like pitch response. Each deck can tap any source — Synth, Drums, Bass, or Master — and a **constant-power crossfader** blends between them without volume dips at center. On the Kotlin side, an MVI ViewModel drives a **60Hz physics simulation** for platter momentum, while the Compose UI renders **radial waveform platters** and a vertical crossfader in the Cleveland Guardians palette.
tech_url: "https://github.com/balch/orphic-fm-app/commit/f2e044f4"
---
