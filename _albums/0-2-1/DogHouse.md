---
layout: album
title: "Dog House"
description: "Phrygian jam session using DJ to add some Coachella inspired texture."
date: 2026-04-13
album: "0-2-1"
track: 5
length: "3:05"
video_url: "https://orphic-fm-video.orphic-fm.workers.dev/0-2-1-assets/DogHouse.mp4"
poster_url: "/assets/albums/2026-03-20-0-2-1/DogHousePoster.png"
og_image: "/assets/albums/2026-03-20-0-2-1/og-dog-house.png"
tags: ["human", "pulsar", "DJ", "Coachella"]
tech_blurb: "First song on new standalone DJ App. This app uses modules from Orpheus (Pulsar, DJ, Leslie, and Distortion) and packages them in a mobile friendly UX allowing for quick and interesting Coachella inspired jams. "
tech_content: |
  Dog House is built on the Pulsar engine's transformation from a beat machine into a **generative song arrangement engine**. At its core, **Markov chord progressions** drive the harmonic movement — weighted probability matrices determine which chord follows the next, so no two plays through the same section sound identical. The arrangement is a **6-section graph** (intro → verse → chorus → solo → breakdown → outro) where transitions between sections are also probabilistic, creating songs that follow a familiar blues arc but never repeat exactly.

  Four virtual band members — Drummer, Bassist, Keys, and FX — interact through **personality traits** (loudness, creativity, swing, drag) and **handoff/pull-in matrices** that govern who plays lead and who locks in behind them. Each member runs **32-step patterns** with per-track bar strategies (Mutate, Fill, Call & Response) that evolve the patterns over time. In the solo section, **Jam mode** kicks in — band members lock into combos and riff on a shared **lick**, mutating it with each pass to create the spontaneous call-and-response feel of a live session. Dedicated Pulsar **delay and reverb** effect units (independent of the main voice chain) add spatial depth, while per-track **mod LFOs and hold-step logic** create evolving textures and drones beneath the arrangement.

  This track is also the debut of the standalone **DJ App**, which packages Orphic modules (Pulsar, DJ turntable, Leslie, and Distortion) into a mobile-friendly UX with full **Media Session integration** across Android, iOS, and macOS — complete with a foreground service to keep the jam alive when backgrounded.
tech_url: "https://github.com/balch/orphic-fm-app/commit/4e4d9f035f0745cbd51971ba80ba5a131bc6b0a2"
---
