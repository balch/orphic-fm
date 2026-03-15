# Orphic FM

Music and visualizations at [orphic.fm](https://orphic.fm). Built with Jekyll and hosted on GitHub Pages.

## Publishing New Album Videos

Video MP4s are stored as GitHub Release assets (not in git) to keep the repo small.

### Steps

1. **Create a release for the album:**
   ```bash
   gh release create <album-slug>-assets --title "<Album Name> Assets" --notes "MP4 video assets for <Album Name>"
   ```

2. **Upload MP4s:**
   ```bash
   gh release upload <album-slug>-assets *.mp4
   ```
   > **Note:** GitHub replaces spaces in filenames with dots. `My Song.mp4` becomes `My.Song.mp4` in the release URL. Name files without spaces to avoid confusion, or use the dot form in `video_url`.

3. **Verify the upload:**
   ```bash
   gh release view <album-slug>-assets
   ```

4. **Set `video_url` in each track's front matter** to the Cloudflare Worker proxy URL:
   ```yaml
   video_url: "https://orphic-fm-video.orphic-fm.workers.dev/<album-slug>-assets/<filename>.mp4"
   ```
   > Videos are proxied through a Cloudflare Worker (`worker/`) that serves correct `Content-Type: video/mp4` headers. GitHub Release URLs serve `application/octet-stream`, which prevents playback on iOS Safari.

5. **Commit and push** the markdown changes. The MP4s stay out of git.

### Existing Releases

| Release Tag | Album |
|---|---|
| `bootstrap-assets` | Bootstrap |
| `crossing-the-chasm-assets` | Crossing the Chasm |

## Video Proxy (Cloudflare Worker)

The `worker/` directory contains a Cloudflare Worker that proxies GitHub Release video assets with correct HTTP headers for iOS Safari compatibility.

- **Why:** GitHub Release assets are served with `Content-Type: application/octet-stream` and `Content-Disposition: attachment`, which prevents inline video playback on iOS Safari.
- **Deployed at:** `https://orphic-fm-video.orphic-fm.workers.dev`
- **URL pattern:** `/<release-tag>/<filename.mp4>`

To redeploy after changes:
```bash
cd worker && npx wrangler deploy
```

## Updating the Synth

The `synth/` folder contains the Orpheus web synth build. It's deployed to `orphic.fm/synth/` but unlisted (blocked from search engines via `robots.txt`).

To update: replace the files in `synth/`, commit, and push.

## Local Development

```bash
bundle exec jekyll serve
```

Videos load from the Cloudflare Worker proxy (which fetches from GitHub Releases), so an internet connection is needed for video playback during local development.
