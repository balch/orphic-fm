#!/usr/bin/env python3
"""
Generate 1200x630 OG images for Orphic FM albums and songs.

Composites the album poster art (darkened, cropped to landscape) with:
  - Album or song title
  - Description text (tech_description for albums, tech_blurb for songs)
  - orphic.fm branding

Usage:
  python3 _tools/generate-og-images.py
"""

import os
import re
import glob
import textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# ── Config ──────────────────────────────────────────────────
OG_WIDTH = 1200
OG_HEIGHT = 630
MARGIN_X = 60
MARGIN_Y = 50
TEXT_AREA_WIDTH = OG_WIDTH - (MARGIN_X * 2)

# Fonts
FONT_TITLE = "/System/Library/Fonts/SFNS.ttf"
FONT_BODY = "/System/Library/Fonts/HelveticaNeue.ttc"

TITLE_SIZE = 52
BODY_SIZE = 24
BRAND_SIZE = 18

ROOT = Path(__file__).resolve().parent.parent


def parse_frontmatter(filepath):
    """Extract YAML frontmatter as a dict (simple parser, no PyYAML needed)."""
    text = filepath.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    fm = {}
    current_key = None
    current_val_lines = []
    for line in match.group(1).split("\n"):
        # Multiline value (indented continuation)
        if current_key and (line.startswith("  ") or line.startswith("\t")):
            current_val_lines.append(line.strip())
            continue
        # Flush previous key
        if current_key:
            fm[current_key] = "\n".join(current_val_lines).strip()
            current_key = None
            current_val_lines = []
        # New key: value
        kv = re.match(r'^(\w[\w_-]*)\s*:\s*(.*)', line)
        if kv:
            key = kv.group(1)
            val = kv.group(2).strip()
            # Handle YAML multiline indicator
            if val == "|" or val == ">":
                current_key = key
                current_val_lines = []
            else:
                # Strip quotes
                val = val.strip('"').strip("'")
                fm[key] = val
    if current_key:
        fm[current_key] = "\n".join(current_val_lines).strip()
    return fm


def load_poster(poster_path):
    """Load and crop poster to 1200x630 landscape with darkening."""
    img = Image.open(poster_path).convert("RGBA")

    # Scale to fill 1200x630
    scale = max(OG_WIDTH / img.width, OG_HEIGHT / img.height)
    new_w = int(img.width * scale)
    new_h = int(img.height * scale)
    img = img.resize((new_w, new_h), Image.LANCZOS)

    # Center crop
    left = (new_w - OG_WIDTH) // 2
    top = (new_h - OG_HEIGHT) // 2
    img = img.crop((left, top, left + OG_WIDTH, top + OG_HEIGHT))

    return img


def darken_image(img):
    """Apply dark gradient overlay for text readability."""
    overlay = Image.new("RGBA", (OG_WIDTH, OG_HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Bottom-heavy gradient: darker at bottom where text lives
    for y in range(OG_HEIGHT):
        # More aggressive darkening in bottom 60%
        t = y / OG_HEIGHT
        if t < 0.3:
            alpha = int(80 + t * 100)  # Light at top
        else:
            alpha = int(110 + (t - 0.3) * 200)  # Darker toward bottom
        alpha = min(alpha, 210)
        draw.line([(0, y), (OG_WIDTH, y)], fill=(0, 0, 0, alpha))

    return Image.alpha_composite(img, overlay)


def wrap_text_ellipsis(draw, text, font, max_width, max_lines):
    """Word-wrap text to fit within max_width, truncating with ellipsis."""
    # Clean up text: remove markdown bold/italic markers
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'`(.+?)`', r'\1', text)
    text = text.replace("\n", " ").strip()

    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test = f"{current_line} {word}".strip() if current_line else word
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] <= max_width:
            current_line = test
        else:
            if current_line:
                lines.append(current_line)
            current_line = word

            if len(lines) >= max_lines:
                break

    if current_line and len(lines) < max_lines:
        lines.append(current_line)

    # Truncate last line with ellipsis if we ran out of space
    if len(lines) == max_lines:
        remaining_words = words[sum(len(l.split()) for l in lines):]
        if remaining_words:
            last = lines[-1]
            while last:
                test = last + "..."
                bbox = draw.textbbox((0, 0), test, font=font)
                if bbox[2] - bbox[0] <= max_width:
                    lines[-1] = test
                    break
                last = " ".join(last.split()[:-1])

    return lines


def generate_og_image(poster_path, title, description, output_path, subtitle=None):
    """Generate a single OG image."""
    # Load and prepare poster
    poster = load_poster(poster_path)
    img = darken_image(poster)

    draw = ImageDraw.Draw(img)

    # Load fonts
    try:
        font_title = ImageFont.truetype(FONT_TITLE, TITLE_SIZE)
    except Exception:
        font_title = ImageFont.truetype(FONT_BODY, TITLE_SIZE)
    font_body = ImageFont.truetype(FONT_BODY, BODY_SIZE)
    font_brand = ImageFont.truetype(FONT_BODY, BRAND_SIZE)

    # Layout from bottom up
    y_bottom = OG_HEIGHT - MARGIN_Y

    # Brand line at bottom
    brand_text = "orphic.fm"
    draw.text((MARGIN_X, y_bottom - 20), brand_text, font=font_brand,
              fill=(255, 255, 255, 120))

    # Description text
    max_desc_lines = 4
    desc_lines = wrap_text_ellipsis(draw, description, font_body,
                                     TEXT_AREA_WIDTH, max_desc_lines)
    line_height_body = BODY_SIZE + 8
    desc_block_height = len(desc_lines) * line_height_body

    y_desc_start = y_bottom - 20 - 30 - desc_block_height
    for i, line in enumerate(desc_lines):
        y = y_desc_start + i * line_height_body
        draw.text((MARGIN_X, y), line, font=font_body,
                  fill=(255, 255, 255, 200))

    # Subtitle (album name) above title for songs
    y_title_bottom = y_desc_start - 16

    if subtitle:
        font_subtitle = ImageFont.truetype(FONT_BODY, 20)
        title_bbox = draw.textbbox((0, 0), title, font=font_title)
        title_h = title_bbox[3] - title_bbox[1]

        subtitle_bbox = draw.textbbox((0, 0), subtitle, font=font_subtitle)
        subtitle_h = subtitle_bbox[3] - subtitle_bbox[1]

        y_subtitle = y_title_bottom - title_h - 8 - subtitle_h
        draw.text((MARGIN_X, y_subtitle), subtitle, font=font_subtitle,
                  fill=(255, 255, 255, 120))
        y_title = y_subtitle + subtitle_h + 8
    else:
        title_bbox = draw.textbbox((0, 0), title, font=font_title)
        title_h = title_bbox[3] - title_bbox[1]
        y_title = y_title_bottom - title_h

    # Title
    draw.text((MARGIN_X, y_title), title, font=font_title,
              fill=(255, 255, 255, 255))

    # Save as PNG (better for OG images than webp — universal support)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    img = img.convert("RGB")
    img.save(str(output_path), "PNG", quality=90)
    print(f"  Generated: {output_path.relative_to(ROOT)}")


def process_albums():
    """Generate OG images for album collection pages."""
    album_pages = list(ROOT.glob("albums/*.md"))
    for page_path in album_pages:
        fm = parse_frontmatter(page_path)
        if not fm.get("poster_url") or not fm.get("tech_description"):
            continue

        album_name = fm.get("album") or fm.get("title", "")
        poster_rel = fm["poster_url"].lstrip("/")
        poster_path = ROOT / poster_rel
        if not poster_path.exists():
            print(f"  SKIP (no poster): {page_path.name}")
            continue

        description = fm["tech_description"]
        slug = album_name.lower().replace(" ", "-")
        output_dir = poster_path.parent
        output_path = output_dir / "og-landscape.png"

        print(f"Album: {album_name}")
        generate_og_image(poster_path, album_name, description, output_path)

        # Update frontmatter to point to new OG image
        og_rel = "/" + str(output_path.relative_to(ROOT))
        update_frontmatter(page_path, "og_image", og_rel)


def process_songs():
    """Generate OG images for individual song pages."""
    song_files = list(ROOT.glob("_albums/**/*.md"))
    for song_path in song_files:
        fm = parse_frontmatter(song_path)
        if not fm.get("tech_blurb"):
            continue

        title = fm.get("title", "")
        album = fm.get("album", "")
        poster_rel = fm.get("poster_url", "").lstrip("/")
        if not poster_rel:
            continue
        poster_path = ROOT / poster_rel
        if not poster_path.exists():
            print(f"  SKIP (no poster): {song_path.name}")
            continue

        description = fm["tech_blurb"]
        slug = title.lower().replace(" ", "-")
        output_dir = poster_path.parent
        output_path = output_dir / f"og-{slug}.png"

        print(f"Song: {title} ({album})")
        generate_og_image(poster_path, title, description, output_path,
                         subtitle=f"Orphic FM — {album}")

        # Update frontmatter
        og_rel = "/" + str(output_path.relative_to(ROOT))
        update_frontmatter(song_path, "og_image", og_rel)


def update_frontmatter(filepath, key, value):
    """Update a frontmatter key in-place."""
    text = filepath.read_text(encoding="utf-8")
    pattern = rf'^({key}\s*:\s*).*$'
    replacement = f'{key}: "{value}"'
    new_text, count = re.subn(pattern, replacement, text, count=1, flags=re.MULTILINE)
    if count == 0:
        # Insert before closing ---
        new_text = re.sub(r'^(---\s*$)', f'{key}: "{value}"\n\\1', text,
                         count=1, flags=re.MULTILINE)
        # That replaces the first ---, we want the second one
        # Let's be more careful
        parts = text.split("---", 2)
        if len(parts) >= 3:
            new_text = parts[0] + "---" + parts[1] + f'{key}: "{value}"\n' + "---" + "---".join(parts[2:])
    filepath.write_text(new_text, encoding="utf-8")


def main():
    print("Generating OG images for Orphic FM...\n")
    process_albums()
    print()
    process_songs()
    print("\nDone!")


if __name__ == "__main__":
    main()
