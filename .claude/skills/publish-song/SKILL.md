---
name: publish-song
description: Use when adding a new track/song to an Orphic FM album — covers metadata, assets, video, OG images, and devlog generation
---

# Publish Song

Add a new track to an Orphic FM album.

## Prerequisites

- MP4 video file for the track
- Album must already exist (album collection page in `albums/` and asset folder in `assets/albums/`)

## Steps

### 1. Gather Track Metadata

Collect from user (or infer from filename/video):

| Field | Required | Example |
|-------|----------|---------|
| `title` | yes | "Dog House" |
| `description` | yes | One-liner shown on page |
| `album` | yes | "0-2-1" |
| `track` | yes | Next integer in album sequence |
| `date` | yes | Today's date (ISO 8601) |
| `length` | yes | Extract via `ffprobe` |
| `tags` | yes | Array of content tags |
| `video_url` | yes | Cloudflare Workers URL (see step 3) |
| `tech_blurb` | no | One-line technical summary (triggers devlog page) |
| `tech_content` | no | Multi-line technical deep-dive |
| `tech_url` | no | Link to related commit/code |
| `featuredSong` | no | Boolean — highlights in gallery |
| `poster_url` | no | Falls back to album poster if omitted |
| `og_crop_gravity` | no | "top", "center", or "bottom" for OG image cropping |

**Get video duration:**
```bash
ffprobe -v quiet -show_entries format=duration -of csv=p=0 FILE.mp4
```

**Get video dimensions (for aspect_ratio if not 16:9):**
```bash
ffprobe -v quiet -show_entries stream=width,height -of csv=p=0 FILE.mp4
```

### 2. Create Track Poster (if desired)

Extract a representative frame from the video or use custom art.

```bash
# Extract frame at specific timestamp
ffmpeg -ss 00:01:00 -i FILE.mp4 -frames:v 1 -q:v 2 output.png
```

Place in: `assets/albums/{DATE}-{ALBUM}/{TrackName}Poster.png`

If no custom poster, omit `poster_url` — the album poster is used as fallback.

### 3. Upload Video via GitHub Release

Videos are served by a Cloudflare Worker (`worker/`) that **proxies GitHub Release assets**. The worker rewrites headers for iOS Safari inline playback but doesn't store files — the actual storage is a GitHub Release.

**Upload to the album's release:**
```bash
gh release upload {ALBUM}-assets /path/to/TrackName.mp4 --clobber
```

**Check existing assets:**
```bash
gh release view {ALBUM}-assets --json assets --jq '.assets[].name'
```

The video URL becomes:
`https://orphic-fm-video.orphic-fm.workers.dev/{ALBUM}-assets/{TrackName}.mp4`

### 4. Find Related Commit for Devlog

Search the orphic-fm-app repo for the commit that introduced the track's feature:

```bash
cd /Users/balch/Source/orphic-fm-app
git log --all --oneline --grep="TrackName" -i
```

If no direct match, search broader terms (e.g., the DSP feature name). Get the commit details:
```bash
git show HASH --format="%H%n%s%n%n%b" --stat
```

Read the relevant source file (e.g., a Vibe class) to understand the DSP/technical details for writing `tech_blurb` and `tech_content`. Use the commit hash for the `tech_url` field:
`https://github.com/balch/orphic-fm-app/commit/{HASH}`

### 5. Create Track Markdown File

Location: `_albums/{ALBUM}/{TrackName}.md`

Filename convention: PascalCase matching the track name (e.g., `DogHouse.md`, `LazySusan.md`).

Template:
```yaml
---
layout: album
title: "Track Title"
description: "Short description"
date: YYYY-MM-DD
album: "album-name"
track: N
length: "M:SS"
video_url: "https://orphic-fm-video.orphic-fm.workers.dev/{album}-assets/{TrackName}.mp4"
poster_url: "/assets/albums/{date}-{album}/{TrackName}Poster.png"
og_image: "/assets/albums/{date}-{album}/og-kebab-case-name.png"
tags: ["tag1", "tag2"]
tech_blurb: "One-line technical summary"
tech_content: |
  Multi-line technical description...
tech_url: "https://github.com/..."
---
```

### 6. Generate OG Image

```bash
python3 _tools/generate-og-images.py
```

Requires: `poster_url` and `tech_blurb` to be set in frontmatter. Generates `og-{slug}.png` in the album assets folder and updates the markdown frontmatter.

### 7. Generate Devlog Pages

```bash
ruby _tools/generate-devlog-pages.rb
```

Auto-creates redirect pages for tracks with `tech_blurb` set.

### 8. Local Preview

```bash
bundle exec jekyll serve
```

Verify:
- Track page renders at `/albums/{album}/{track-slug}/`
- Track appears in album collection page
- Video plays (if uploaded to Cloudflare)
- OG image looks correct
- Devlog redirect works (if tech_blurb set)

### 9. Commit and Deploy

Push to `main` — GitHub Actions handles build and deploy automatically.

## Naming Conventions

| Item | Convention | Example |
|------|-----------|---------|
| Markdown file | PascalCase | `DogHouse.md` |
| Poster image | PascalCase + "Poster" | `DogHousePoster.png` |
| OG image | kebab-case with `og-` prefix | `og-dog-house.png` |
| Video URL path | PascalCase | `DogHouse.mp4` |
| Asset folder | `{date}-{album}` | `2026-03-20-0-2-1` |

## Portrait Video Note

If the video is portrait (e.g., 720x1080), set `aspect_ratio` in frontmatter:
```yaml
aspect_ratio: "720/1080"
```
Check existing tracks for whether this album uses portrait video — if all tracks are portrait, the layout may already handle it.

## Common Mistakes

- Forgetting to set `tech_blurb` — OG image generation and devlog pages both depend on it
- Wrong track number — check existing tracks with `grep "^track:" _albums/{ALBUM}/*.md`
- Missing poster for OG generation — the `generate-og-images.py` script skips tracks without `poster_url`
