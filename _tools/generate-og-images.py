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
MARGIN_X = 50
MARGIN_Y = 40
TEXT_PANEL_WIDTH = 520  # Left side text panel
TEXT_AREA_WIDTH = TEXT_PANEL_WIDTH - MARGIN_X - 20  # Text wrapping width

# Fonts
FONT_TITLE = "/System/Library/Fonts/SFNS.ttf"
FONT_BODY = "/System/Library/Fonts/HelveticaNeue.ttc"

TITLE_SIZE = 44
BODY_SIZE = 20
BRAND_SIZE = 16

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


def load_poster(poster_path, crop_gravity="center"):
    """Load and crop poster to 1200x630 landscape.

    crop_gravity controls vertical anchor: "top", "center", or "bottom".
    """
    img = Image.open(poster_path).convert("RGBA")

    # Scale to fill 1200x630
    scale = max(OG_WIDTH / img.width, OG_HEIGHT / img.height)
    new_w = int(img.width * scale)
    new_h = int(img.height * scale)
    img = img.resize((new_w, new_h), Image.LANCZOS)

    # Right-anchored horizontal crop (text panel covers the left)
    left = new_w - OG_WIDTH

    # Vertical crop based on gravity
    v_excess = new_h - OG_HEIGHT
    if crop_gravity == "top":
        top = 0
    elif crop_gravity == "bottom":
        top = v_excess
    else:
        top = v_excess // 2

    img = img.crop((left, top, left + OG_WIDTH, top + OG_HEIGHT))

    return img


def darken_image(img):
    """Apply left-to-right gradient overlay — dark on left for text, clear on right for art."""
    overlay = Image.new("RGBA", (OG_WIDTH, OG_HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    for x in range(OG_WIDTH):
        t = x / OG_WIDTH
        if t < 0.35:
            # Solid dark on the left text panel
            alpha = 200
        elif t < 0.65:
            # Fade out through the middle
            fade = (t - 0.35) / 0.30
            alpha = int(200 * (1 - fade))
        else:
            # Transparent on the right — art shows through
            alpha = 0
        draw.line([(x, 0), (x, OG_HEIGHT)], fill=(0, 0, 0, alpha))

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


def generate_og_image(poster_path, title, description, output_path, subtitle=None, crop_gravity="center"):
    """Generate a single OG image with text on the left, art on the right."""
    # Load and prepare poster
    poster = load_poster(poster_path, crop_gravity)
    img = darken_image(poster)

    draw = ImageDraw.Draw(img)

    # Load fonts
    try:
        font_title = ImageFont.truetype(FONT_TITLE, TITLE_SIZE)
    except Exception:
        font_title = ImageFont.truetype(FONT_BODY, TITLE_SIZE)
    font_body = ImageFont.truetype(FONT_BODY, BODY_SIZE)
    font_brand = ImageFont.truetype(FONT_BODY, BRAND_SIZE)

    # ── Left-panel layout: top-to-bottom ──
    y = MARGIN_Y

    # Brand line at top
    draw.text((MARGIN_X, y), "orphic.fm", font=font_brand,
              fill=(255, 255, 255, 100))
    y += BRAND_SIZE + 24

    # Subtitle (album name for songs)
    if subtitle:
        font_subtitle = ImageFont.truetype(FONT_BODY, 18)
        draw.text((MARGIN_X, y), subtitle, font=font_subtitle,
                  fill=(255, 255, 255, 120))
        y += 18 + 10

    # Title — may need to wrap for long titles
    title_lines = wrap_text_ellipsis(draw, title, font_title,
                                      TEXT_AREA_WIDTH, 2)
    line_height_title = TITLE_SIZE + 6
    for line in title_lines:
        draw.text((MARGIN_X, y), line, font=font_title,
                  fill=(255, 255, 255, 255))
        y += line_height_title
    y += 12

    # Thin separator line
    draw.line([(MARGIN_X, y), (MARGIN_X + 60, y)],
              fill=(255, 255, 255, 80), width=2)
    y += 16

    # Description text
    remaining_height = OG_HEIGHT - y - MARGIN_Y
    line_height_body = BODY_SIZE + 7
    max_desc_lines = min(8, remaining_height // line_height_body)
    desc_lines = wrap_text_ellipsis(draw, description, font_body,
                                     TEXT_AREA_WIDTH, max_desc_lines)
    for line in desc_lines:
        draw.text((MARGIN_X, y), line, font=font_body,
                  fill=(255, 255, 255, 180))
        y += line_height_body

    # Save
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
        crop_gravity = fm.get("og_crop_gravity", "center")
        slug = album_name.lower().replace(" ", "-")
        output_dir = poster_path.parent
        output_path = output_dir / "og-landscape.png"

        print(f"Album: {album_name}")
        generate_og_image(poster_path, album_name, description, output_path,
                         crop_gravity=crop_gravity)

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

        crop_gravity = fm.get("og_crop_gravity", "center")
        print(f"Song: {title} ({album})")
        generate_og_image(poster_path, title, description, output_path,
                         subtitle=f"Orphic FM — {album}",
                         crop_gravity=crop_gravity)

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
