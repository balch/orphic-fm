---
layout: album
title: "Rust Belt"
description: "New vibe to showcase the weather effects. Thunderclaps, rolling thunder and evolving rain intensity integrate with the lick as it mutates with the storm. Inspired by the live music playing at Barrel House Saloon in Sandusky, OH, watching the thunder and lightning roll in over Lake Erie."
date: 2026-09-06
album: "Anomalies"
track: 2
length: "3:35"
video_url: "https://orphic-fm-video.orphic-fm.workers.dev/anomalies-assets/RustBelt.mp4"
poster_url: "/assets/albums/2026-07-18-Anomalies/RustBeltPoster.jpg"
aspect_ratio: "756/491"
og_crop_gravity: center
tags: ["human", "pulsar", "dj", "storm", "anomaly"]
tech_blurb: "New storm and weather effects evolve with a swampy bass lick inspired by an intimate moment on the shores of Lake Erie (and a Pretenders classic). "
tech_content: |
  Rust Belt is a swampy heartland-rock pocket at 87 BPM in D Dorian inspired by the Pretenders classic. The bass evolves the pocket, adding a round, fingered two-bar hook that never transposes until the chorus asks it to (IV → bVII → i; in dorian the major IV is the money chord).

  **What shipped.** [`e6e1b9c53`](https://github.com/balch/orphic-fm-app/commit/e6e1b9c53d427ac30003e67f40f5671a879b1182) added three pieces of arrangement machinery that were built together and share one wire: a storm voice, a per-edge transition-effect bank, and a per-track breathe cycle.

  The storm is a **9th Pulsar voice**, not a graph unit. [`pulsar_storm.h`](https://github.com/balch/orphic-fm-app/blob/main/liborpheus_dsp/src/pulsar_storm.h) is 1,272 lines, seeded per instance and driven only by `pulsar_rng`, so a given seed always renders the same audio — no allocation, no statics, no logging after `Init`.

  **Rain** is two fields at once, and voicing only one of them is what makes it read as a leak. Near field: Bernoulli dust, each drop a one-sample impulse into a band-pass it re-tunes on the way in, so every drop is its own size. Far field: a diffuse wash of the thousands of drops too distant to resolve, dark and gusting, rising super-linearly so it's a hint behind a drizzle and the body of a downpour. Density is mapped **geometrically**, not linearly — a linear sweep spends its whole bottom half above the rate at which the ear stops resolving individual drops. The particle field and the smooth-random LFO are both adapted from Mutable Instruments Plaits (MIT, © Emilie Gillet).

  **Thunder** is a five-octave fractal sum starting at 0.12 Hz (8.3 s) and doubling up to 1.9 Hz, undulating deep enough that troughs land 20 dB under the crests — the front swells and recedes as it travels rather than sitting at one level. Distance darkens the roll, but only so far: the pulsar's output high-pass sits at 55 Hz, and a deeper tilt would push a far strike's whole band underneath it and simply delete the thunder.

  **Lightning** is a cascade, not a hit — and it falls. Four transients step down 3400 → 1900 → 950 → 420 Hz on widening gaps (32 / 42 / 52 ms), with tails that *lengthen* on the way down (35 → 130 ms) because a lower band rings longer. The tails overlap the next onset on purpose: the "clap-clap" is carried by the attacks, and a strike that went silent between steps was four ticks. A band-pass alone was a filter ping — the textbook synthetic transient, and exactly what the ear test called synthy — so a parallel **grit** path gives every hit a torn broadband body beside its pitch, a crackle modulator rips its amplitude, and a Lorenz stream wanders both the centre and the pitch/grit balance so no two cracks are the same shape. The descent runs crack → tear → boom → sub without a hole in it.

  Then **terrain echo**: five irregularly spaced taps (37 / 71 / 118 / 179 / 247 ms) off one mono line with no feedback, so the tail is bounded by the longest tap by construction. The spacing is deliberately non-harmonic — evenly spaced taps comb, and a doubling chain reads as a tempo-synced delay rather than as ground. Distance is the whole dial and it runs the right way round: a bolt directly overhead barely echoes, a distant one answers off the hills for a quarter second.

  **Breathe** is what makes it more than a weather layer. A bar-clocked swell sinks a track's gain toward a floor and closes its tone with it, then rises back. In **downpour** the kit drops out and everyone else keeps playing *under* the roar — buried, not absent — breathing on co-prime periods of 2, 3 and 5 bars, so their swells only re-converge every 30 bars, far longer than the section lives. The ensemble audibly decoheres instead of just getting quieter. Then **cloud break** snaps every voice onto one shared 3-bar breath and walks the kit back in under full rain: the band reassembles in a single move. `bars = 0` is exactly unity — the caller skips the audio path rather than multiplying by a computed 1.0 — so a vibe with no breathe renders bit-identically to a build without the feature.

  [`68b00e82d`](https://github.com/balch/orphic-fm-app/commit/68b00e82d9aa802ecf3d42976af9d435bde501ec) wired the storm into the arrangement as one deliberate lap instead of a weighted graph: every section is worth hearing, and the downpour is worth hearing exactly once, which is also what pins the song near three minutes. [`1439739`](https://github.com/balch/orphic-fm-app/commit/1439739743b275654538985bcc86ab235f5f2b32) pushed the cloud break's energy to 0.90 — above the verse it returns to, so the peak of the storm reads as a peak instead of a lull — and stretched its exit ramp to three bars so the macros have room to walk home before the band arrives. Recorded a few hours later.
tech_url: "https://github.com/balch/orphic-fm-app/commit/e6e1b9c53d427ac30003e67f40f5671a879b1182"
og_image: "/assets/albums/2026-07-18-Anomalies/og-rust-belt.png"
---
