#!/usr/bin/env ruby
# Generates per-song devlog redirect pages so each track gets its own
# shareable URL with correct OG meta tags.
#
# Reads _albums/**/*.md, finds tracks with tech_blurb, and creates
# lightweight markdown stubs under devlog/<slug>/index.md that redirect
# to /devlog/#<slug>.
#
# Run before jekyll build. Called by the GitHub Actions workflow.

require "yaml"
require "date"
require "fileutils"

ROOT = File.expand_path("..", __dir__)
DEVLOG_DIR = File.join(ROOT, "devlog")

def slugify(title)
  title.downcase.gsub(/[^a-z0-9\s-]/, "").gsub(/\s+/, "-").gsub(/-+/, "-").sub(/^-/, "").sub(/-$/, "")
end

def yaml_quote(str)
  return '""' if str.nil? || str.empty?
  %("#{str.gsub('"', '\\"')}")
end

# Clean previously generated stub pages
Dir.glob(File.join(DEVLOG_DIR, "*/index.md")).each { |f| File.delete(f) }

count = 0
Dir.glob(File.join(ROOT, "_albums", "**", "*.md")).each do |track_file|
  content = File.read(track_file)
  next unless content =~ /\A---\s*\n(.*?\n)---\s*\n/m

  front_matter = YAML.safe_load($1, permitted_classes: [Date])
  next unless front_matter && front_matter["tech_blurb"]

  title      = front_matter["title"]
  tech_blurb = front_matter["tech_blurb"]
  desc       = front_matter["description"]
  og_image   = front_matter["og_image"]
  poster_url = front_matter["poster_url"]
  slug       = slugify(title)
  image      = og_image || poster_url
  blurb      = tech_blurb || desc

  dir = File.join(DEVLOG_DIR, slug)
  FileUtils.mkdir_p(dir)

  File.write(File.join(dir, "index.md"), <<~FRONTMATTER)
    ---
    layout: devlog-song
    title: #{yaml_quote(title)}
    description: #{yaml_quote(blurb)}
    og_image: #{yaml_quote(image || "")}
    poster_url: #{yaml_quote(poster_url || "")}
    track_slug: #{yaml_quote(slug)}
    permalink: /devlog/#{slug}/
    ---
  FRONTMATTER

  count += 1
  puts "  Generated: /devlog/#{slug}/"
end

puts "Done. #{count} devlog song pages generated."
