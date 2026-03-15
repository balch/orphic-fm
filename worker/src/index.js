// Cloudflare Worker that proxies GitHub Release video assets
// with correct Content-Type and Content-Disposition headers
// so iOS Safari can play them inline.
//
// URL pattern: /<release-tag>/<filename.mp4>
// e.g. /crossing-the-chasm-assets/6-7.mp4

const GITHUB_REPO = "balch/orphic-fm";

const MIME_TYPES = {
  ".mp4": "video/mp4",
  ".webm": "video/webm",
  ".mov": "video/quicktime",
  ".m4v": "video/x-m4v",
};

export default {
  async fetch(request) {
    const url = new URL(request.url);
    const path = url.pathname;

    // Health check
    if (path === "/" || path === "/health") {
      return new Response("ok");
    }

    // Extract /<tag>/<filename> from path
    const match = path.match(/^\/([^/]+)\/(.+)$/);
    if (!match) {
      return new Response("Not found. Use /<release-tag>/<filename>", { status: 404 });
    }

    const [, tag, filename] = match;
    const ext = filename.substring(filename.lastIndexOf(".")).toLowerCase();
    const contentType = MIME_TYPES[ext];

    if (!contentType) {
      return new Response("Unsupported file type", { status: 400 });
    }

    const githubUrl = `https://github.com/${GITHUB_REPO}/releases/download/${tag}/${filename}`;

    // Fetch from GitHub, following the redirect to the CDN
    const originResponse = await fetch(githubUrl, {
      headers: {
        "User-Agent": "orphic-fm-video-proxy",
      },
      redirect: "follow",
    });

    if (!originResponse.ok) {
      return new Response("Video not found", { status: originResponse.status });
    }

    // Build response with correct headers for iOS Safari
    const headers = new Headers();
    headers.set("Content-Type", contentType);
    headers.set("Content-Disposition", "inline");
    headers.set("Accept-Ranges", "bytes");
    headers.set("Access-Control-Allow-Origin", "*");
    headers.set("Cache-Control", "public, max-age=86400, s-maxage=604800");

    // Preserve Content-Length if present
    const contentLength = originResponse.headers.get("Content-Length");
    if (contentLength) {
      headers.set("Content-Length", contentLength);
    }

    return new Response(originResponse.body, {
      status: 200,
      headers,
    });
  },
};
