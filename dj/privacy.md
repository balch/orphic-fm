---
layout: page
title: Orphic DJ — Privacy Policy
permalink: /dj/privacy/
---

_Last updated: 2026-05-03_

## Summary

**Orphic DJ does not collect, transmit, store, or share any personal information.**
The app runs entirely on your device. It does not connect to the internet, does
not contact any servers, and contains no analytics, advertising, tracking, or
crash-reporting SDKs.

## About the developer

Orphic DJ is developed and published as an independent project
under the **Orphic FM** banner. Questions about this policy can be sent to
**orphic.fm.apps@gmail.com**.

## What data the app accesses

The app does not collect or transmit any of the following:

- Personal information (name, email, phone, location, etc.)
- Device identifiers (advertising ID, IMEI, MAC, etc.)
- Usage analytics or telemetry
- Crash logs or diagnostics

The only state Orphic DJ persists is your **app preferences** (selected vibe,
panel knob positions, timer settings). These are stored locally on your device
via Android's standard preferences APIs and never leave the device.

## Permissions used

Orphic DJ requests the following Android permissions. Each is used solely for
the purpose described — none enables data collection.

| Permission | Why it is requested |
|------------|---------------------|
| `MODIFY_AUDIO_SETTINGS` | Required by Android's audio framework so the app can configure the output sample rate and buffer size for low-latency playback. |
| `FOREGROUND_SERVICE` and `FOREGROUND_SERVICE_MEDIA_PLAYBACK` | Allow the app to keep generating audio while the screen is off or another app is in the foreground, the same way music players continue playback in the background. |
| `POST_NOTIFICATIONS` | Used to display the standard "now playing" media notification with play/pause/skip controls. The notification is dismissed when playback stops. |

The app does **not** request `INTERNET`, `ACCESS_FINE_LOCATION`,
`READ_CONTACTS`, `READ_EXTERNAL_STORAGE`, or any other sensitive permission.

## Android Auto

Orphic DJ supports Android Auto. When connected to a compatible vehicle
infotainment system, the app exposes:

- The list of available "vibes" (preset names and BPM)
- Standard media playback controls (play, pause, skip, stop)
- Currently-playing track title, subtitle, and album artwork

This information is passed to the Android Auto operating system on the
vehicle's head unit only for display and playback control. Orphic DJ does not
send any data to Google, the vehicle manufacturer, or any third party.

## Children's privacy

Orphic DJ is intended for a general audience and is not directed at children
under 13. Because the app does not collect any information at all, no
information is collected from children.

## Changes to this policy

If this policy is updated, the new version will be posted at this URL with a
revised "Last updated" date. Material changes will be noted at the top of the
page.

## Contact

For privacy questions or requests, email **orphic.fm.apps@gmail.com**.
