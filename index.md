---
layout: home
title: Home
---

<section class="hero-section">
  <div class="hero-content">
    <h1 class="hero-title">Orphic FM</h1>
    <p class="hero-subtitle">{{ site.description }}</p>
  </div>
</section>

{% assign all_tracks = site.albums | sort: 'date' | reverse %}
{% assign newest_track = all_tracks | first %}
{% assign latest_album_name = newest_track.album %}

{% assign latest_album_tracks = site.albums | where: "album", latest_album_name | sort: "track" %}
{% assign featured_track = latest_album_tracks | where: "featuredSong", true | first %}
{% unless featured_track %}
  {% assign featured_track = latest_album_tracks | first %}
{% endunless %}
{% assign latest_album = featured_track %}
{% if latest_album.album %}
{% assign latest_album_slug = latest_album.album | slugify %}
{% assign latest_album_url = "/albums/" | append: latest_album_slug | append: "/" %}
{% endif %}

{% assign featured_album_page = site.pages | where: "album", latest_album.album | first %}
{% assign featured_has_unique_art = false %}
{% if latest_album.poster_url and featured_album_page and latest_album.poster_url != featured_album_page.poster_url %}
  {% assign featured_has_unique_art = true %}
{% endif %}

{% if latest_album %}
<section id="featured-album" class="featured-hero">
  <!-- Background: song or album poster -->
  <div class="featured-hero-bg">
    {% if latest_album.poster_url %}
      <img src="{{ latest_album.poster_url | relative_url }}" alt="" loading="lazy"
        class="{% if featured_has_unique_art %}unique-bg{% endif %}">
      {% if featured_has_unique_art %}
        <img src="{{ latest_album.poster_url | relative_url }}" alt="" loading="lazy"
          class="unique-bg-sharp">
      {% endif %}
    {% endif %}
  </div>
  <div class="featured-hero-scrim"></div>

  <div class="featured-hero-inner">
    <!-- Text side -->
    <div class="featured-hero-text">
      <div class="section-label">Featured Track</div>
      <div class="featured-meta-top">
        <span>{{ latest_album.date | date: "%B %d, %Y" }}</span>
        {% if latest_album.length %}
          <span class="dot-separator"></span>
          <span>{{ latest_album.length }}</span>
        {% endif %}
      </div>
      <h2 class="featured-title">{{ latest_album.title }}</h2>

      {% if latest_album.description %}
        <div class="featured-body-text">
          {{ latest_album.description | markdownify }}
        </div>
      {% endif %}

      {% if latest_album.tags %}
        <div class="album-tags-list">
          {% for tag in latest_album.tags %}
            <span class="album-tag">#{{ tag }}</span>
          {% endfor %}
        </div>
      {% endif %}

      <!-- Equal-weight links: Album + Dev Log -->
      {% if latest_album.album %}
        <div class="featured-links">
          <a class="featured-link" href="{{ latest_album_url | relative_url }}">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <circle cx="12" cy="12" r="10"/><polygon points="10 8 16 12 10 16 10 8"/>
            </svg>
            {{ latest_album.album }}
          </a>
          {% assign featured_slug = latest_album.title | slugify %}
          <a class="featured-link devlog-link-btn" href="{{ '/devlog/' | append: featured_slug | append: '/' | relative_url }}">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/>
            </svg>
            Dev Log
          </a>
        </div>
      {% endif %}
    </div>

    <!-- Video side -->
    <div class="featured-hero-video">
      <div class="video-card">
        <div class="video-container" style="aspect-ratio: {{ latest_album.aspect_ratio | default: '16/9' }};">
          <video
            src="{{ latest_album.video_url }}"
            {% if latest_album.poster_url %}poster="{{ latest_album.poster_url | relative_url }}"{% endif %}
            playsinline
            loop
            muted
            autoplay
            controls></video>
        </div>
      </div>
    </div>
  </div>
</section>

{% assign album_names = "" %}
{% for t in all_tracks %}
  {% unless album_names contains t.album %}
    {% if album_names != "" %}{% assign album_names = album_names | append: "|" %}{% endif %}
    {% assign album_names = album_names | append: t.album %}
  {% endunless %}
{% endfor %}
{% assign album_list = album_names | split: "|" %}

{% if album_list.size > 0 %}
<section class="albums-section">
  <div class="container">
    <div class="section-label">Albums</div>
    <div class="albums-grid">
      {% for album_name in album_list %}
        {% assign album_slug = album_name | slugify %}
        {% assign album_url = "/albums/" | append: album_slug | append: "/" %}
        {% assign album_tracks_list = site.albums | where: "album", album_name | sort: "track" %}
        {% assign first_track = album_tracks_list | first %}
        {% assign album_page = site.pages | where: "album", album_name | first %}
        <a href="{{ album_url | relative_url }}" class="album-card">
          <div class="album-card-art">
            {% if first_track.poster_url %}
              <img src="{{ first_track.poster_url | relative_url }}" alt="{{ album_name }}" loading="lazy">
            {% endif %}
          </div>
          <div class="album-card-info">
            <h3 class="album-card-title">{{ album_name }}</h3>
            {% if album_page.description %}
              <p class="album-card-desc">{{ album_page.description | markdownify | strip_html | truncate: 100 }}</p>
            {% endif %}
            <span class="album-card-meta">{{ album_tracks_list.size }} tracks</span>
            {% assign album_tech_tracks = album_tracks_list | where_exp: "t", "t.tech_blurb" %}
            {% if album_tech_tracks.size > 0 %}
              <span class="tech-indicator-badge">
                <svg xmlns="http://www.w3.org/2000/svg" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
                Dev log
              </span>
            {% endif %}
          </div>
        </a>
      {% endfor %}
    </div>
  </div>
</section>
{% endif %}

<section class="gallery-section">
  <div class="container">
    <div class="section-label">Gallery</div>
    <div class="album-grid">
      {% assign gallery_tracks = all_tracks | where_exp: "item", "item.url != featured_track.url" | limit: 20 %}
      {% for album in gallery_tracks %}
        <div class="grid-item">
          <div class="grid-video-container" style="aspect-ratio: {{ album.aspect_ratio | default: '16/9' }};">
            <video
              src="{{ album.video_url }}"
              {% if album.poster_url %}poster="{{ album.poster_url | relative_url }}"{% endif %}
              class="video-lightbox-trigger"
              controls
              loop
              playsinline
              preload="none"></video>
            <div class="expand-overlay" title="Click to expand">
              <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"></path>
              </svg>
            </div>
          </div>
          <div class="grid-info">
            <a href="{{ album.url | relative_url }}" class="grid-title-link">
              <h3 class="grid-title">{{ album.title }}</h3>
            </a>
            <div class="grid-meta">
              <span>{{ album.date | date: "%B %d, %Y" }}</span>
              {% if album.album %}
                <span class="dot-separator"></span>
                <span>{{ album.album }}</span>
              {% endif %}
              {% if album.length %}
                <span class="dot-separator"></span>
                <span>{{ album.length }}</span>
              {% endif %}
            </div>
            {% if album.description %}
              <div class="grid-description">
                {{ album.description | markdownify }}
              </div>
            {% endif %}
          </div>
        </div>
      {% endfor %}
    </div>
  </div>
</section>
{% else %}
<section class="loading-state" style="text-align: center; padding: 10rem 0;">
  <div class="container">
    <p style="opacity: 0.3; font-size: 1.2rem; margin-bottom: 2rem;">Waiting for albums to sync...</p>
    <div style="font-size: 0.9rem; opacity: 0.5; max-width: 500px; margin: 0 auto; line-height: 1.6;">
      <p>If you just added a collection to <code>_config.yaml</code>, please <strong>restart</strong> the Jekyll server to pick up the new structure.</p>
    </div>
  </div>
</section>
{% endif %}

<style>
  :root {
    --hero-font-size: clamp(4rem, 15vw, 12rem);
  }

  .hero-section {
    padding: 8rem 0 4rem;
    text-align: center;
    position: relative;
    z-index: 1;
  }
  
  .hero-title {
    font-size: var(--hero-font-size);
    font-weight: 800;
    letter-spacing: -0.05em;
    margin: 0;
    line-height: 1.05;
    padding-bottom: 0.05em;
    background: linear-gradient(180deg, #fff 0%, rgba(255,255,255,0.6) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 15px 30px rgba(0,0,0,0.4));
  }
  
  .hero-subtitle {
    font-size: clamp(1rem, 1.5vw, 1.2rem);
    opacity: 0.75;
    font-weight: 400;
    margin-top: 2rem;
    letter-spacing: 0.02em;
    max-width: 750px;
    margin-left: auto;
    margin-right: auto;
    line-height: 1.7;
    color: var(--text-secondary);
  }
  
  /* ── Featured Hero ── */
  .featured-hero {
    position: relative;
    overflow: hidden;
    margin-bottom: 2rem;
  }
  .featured-hero-bg {
    position: absolute;
    inset: 0;
    z-index: 0;
    overflow: hidden;
  }
  .featured-hero-bg img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center 30%;
    filter: blur(30px) brightness(0.3) saturate(1.4);
    transform: scale(1.1);
  }
  .featured-hero-bg img.unique-bg {
    display: none;
  }
  .featured-hero-bg img.unique-bg-sharp {
    display: none;
  }
  .featured-hero-scrim {
    position: absolute;
    inset: 0;
    z-index: 1;
    background: linear-gradient(
      to right,
      rgba(13, 13, 13, 0.8) 0%,
      rgba(13, 13, 13, 0.6) 40%,
      rgba(13, 13, 13, 0.3) 70%,
      rgba(13, 13, 13, 0.15) 100%
    );
  }
  .featured-hero-inner {
    position: relative;
    z-index: 2;
    display: flex;
    gap: 3rem;
    max-width: 1100px;
    margin: 0 auto;
    padding: 3rem 2rem 4rem;
    align-items: center;
  }
  .featured-hero-text {
    flex: 1;
    min-width: 0;
  }
  .featured-hero-video {
    width: 420px;
    flex-shrink: 0;
  }
  .featured-meta-top {
    font-size: 0.8rem;
    font-weight: 600;
    opacity: 0.3;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 0.75rem;
  }
  .featured-title {
    font-size: clamp(2rem, 4vw, 3rem);
    font-weight: 700;
    letter-spacing: -0.03em;
    margin: 0 0 1rem;
    line-height: 1.15;
    text-shadow: 0 2px 20px rgba(0,0,0,0.4);
  }
  .featured-body-text {
    font-size: 1.1rem;
    line-height: 1.6;
    opacity: 0.7;
    margin-bottom: 1.5rem;
    overflow: hidden;
  }
  .featured-body-text p {
    margin: 0;
  }
  .featured-links {
    display: flex;
    gap: 0.75rem;
    flex-wrap: wrap;
    margin-top: 1.5rem;
  }
  .featured-link {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 0.95rem;
    font-weight: 600;
    color: var(--accent-primary, #8b5cf6);
    text-decoration: none;
    padding: 0.65rem 1.25rem;
    border-radius: 100px;
    border: 1px solid rgba(139, 92, 246, 0.25);
    background: rgba(139, 92, 246, 0.08);
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    backdrop-filter: blur(8px);
  }
  .featured-link:hover {
    background: rgba(139, 92, 246, 0.18);
    border-color: rgba(139, 92, 246, 0.45);
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(139, 92, 246, 0.2);
  }

  .narrow {
    max-width: 850px;
  }

  .dot-separator {
    width: 4px;
    height: 4px;
    background: currentColor;
    border-radius: 50%;
  }

  .video-card {
    border-radius: 20px;
    overflow: hidden;
    background: #000;
    box-shadow: 0 20px 60px rgba(0,0,0,0.5), 0 0 0 1px rgba(255,255,255,0.05);
  }
  .video-container {
    position: relative;
    overflow: hidden;
    background: #000;
  }
  .video-container video {
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
    cursor: pointer;
  }
  
  
  .album-tags-list {
    display: flex;
    gap: 0.5rem;
    justify-content: flex-start;
    flex-wrap: wrap;
  }
  
  .album-tag {
    font-size: 0.8rem;
    opacity: 0.4;
    padding: 0.5rem 1.2rem;
    border-radius: 100px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: all 0.3s;
  }
  
  .album-tag:hover {
    opacity: 1;
    border-color: rgba(255, 255, 255, 0.3);
    background: rgba(255,255,255,0.05);
  }

  .albums-section {
    padding: 6rem 0;
    border-top: 1px solid rgba(255,255,255,0.05);
  }

  .albums-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 2rem;
  }

  .album-card {
    display: flex;
    gap: 1.5rem;
    padding: 1.5rem;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.06);
    background: rgba(255,255,255,0.02);
    text-decoration: none;
    color: inherit;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  }

  .album-card:hover {
    background: rgba(255,255,255,0.05);
    border-color: rgba(255,255,255,0.12);
    transform: translateY(-4px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.3);
  }

  .album-card-art {
    width: 120px;
    height: 120px;
    border-radius: 12px;
    overflow: hidden;
    flex-shrink: 0;
    background: #111;
    box-shadow: 0 8px 24px rgba(0,0,0,0.4);
  }

  .album-card-art img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }

  .album-card-info {
    display: flex;
    flex-direction: column;
    justify-content: center;
    min-width: 0;
  }

  .album-card-title {
    font-size: 1.3rem;
    font-weight: 700;
    margin: 0 0 0.5rem;
    letter-spacing: -0.01em;
  }

  .album-card-desc {
    font-size: 0.9rem;
    line-height: 1.5;
    opacity: 0.6;
    margin: 0 0 0.75rem;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .album-card-meta {
    font-size: 0.75rem;
    font-weight: 600;
    opacity: 0.35;
    text-transform: uppercase;
    letter-spacing: 0.15em;
  }

  .gallery-section {
    padding: 6rem 0 12rem;
    border-top: 1px solid rgba(255,255,255,0.05);
  }

  .section-label {
    font-size: 0.9rem;
    font-weight: 700;
    opacity: 0.7;
    text-transform: uppercase;
    letter-spacing: 0.25em;
    margin-bottom: 4rem;
    text-align: center;
    color: var(--text-primary);
  }

  .album-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 2rem;
    align-items: start;
  }

  .grid-item {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .grid-video-container {
    /* aspect-ratio set via inline style from front-matter */
    border-radius: 16px;
    overflow: hidden;
    background: #000;
    box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    position: relative;
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  }

  .grid-video-container:hover {
    transform: scale(1.02);
  }

  .grid-video-container video {
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
  }

  .expand-overlay {
    position: absolute;
    top: 10px;
    right: 10px;
    width: 40px;
    height: 40px;
    background: rgba(0, 0, 0, 0.7);
    backdrop-filter: blur(10px);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    opacity: 0;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    border: 1px solid rgba(255, 255, 255, 0.1);
    z-index: 10;
  }

  .expand-overlay svg {
    width: 24px;
    height: 24px;
  }


  .grid-video-container:hover .expand-overlay {
    opacity: 1;
  }

  .expand-overlay:hover {
    background: rgba(139, 92, 246, 0.9);
    border-color: rgba(139, 92, 246, 0.3);
    transform: scale(1.1);
  }

  .expand-overlay svg {
    color: white;
  }

  .grid-title-link {
    text-decoration: none;
    color: inherit;
    transition: color 0.3s;
  }

  .grid-title-link:hover {
    color: var(--accent-primary);
  }

  .grid-title-link:hover .grid-title {
    color: var(--accent-primary);
  }

  .grid-title {
    font-size: 1.1rem;
    font-weight: 600;
    margin: 0;
    letter-spacing: -0.01em;
  }

  .grid-meta {
    font-size: 0.8rem;
    opacity: 0.4;
    display: flex;
    align-items: center;
    gap: 0.75rem;
    margin-bottom: 0.5rem;
  }

  .grid-description {
    font-size: 0.9rem;
    line-height: 1.5;
    opacity: 0.6;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .mobile-only { display: none; }

  @media (max-width: 768px) {
    .mobile-only { display: block; }
    .desktop-only { display: none; }
    .albums-grid {
      grid-template-columns: 1fr;
    }
    .album-card-art {
      width: 80px;
      height: 80px;
    }
    .album-card {
      padding: 1rem;
      gap: 1rem;
    }
    .album-card-title {
      font-size: 1.1rem;
    }
    .album-grid {
      grid-template-columns: 1fr;
    }
    .gallery-section {
      padding: 4rem 0 8rem;
    }
    .video-container { border-radius: 20px; max-height: 70vh; }
    .video-card { border-radius: 16px; }
    .grid-video-container { max-height: 70vh; }
    :root {
      --hero-font-size: clamp(2.8rem, 12vw, 5rem);
    }
    .hero-section { padding: 8rem 0 4rem; }
    .hero-subtitle { margin-top: 1.5rem; }
    .featured-hero-inner {
      flex-direction: column;
      gap: 1.5rem;
      padding: 2rem 1.25rem 3rem;
    }
    .featured-hero-video {
      width: 100%;
    }
    .featured-hero-scrim {
      background: linear-gradient(
        to bottom,
        rgba(13, 13, 13, 0.85) 0%,
        rgba(13, 13, 13, 0.6) 60%,
        rgba(13, 13, 13, 0.4) 100%
      );
    }
    .featured-title { font-size: clamp(1.8rem, 8vw, 2.5rem); }
    .featured-meta-top { display: none; }
    .featured-body-text { font-size: 1rem; }
    .featured-links { justify-content: center; }
    .album-tags-list { justify-content: center; }
  }

  /* Album card dev log badge */
  .tech-indicator-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    font-size: 0.7rem;
    color: var(--accent-primary, #8b5cf6);
    opacity: 0.6;
    margin-top: 0.5rem;
  }
</style>
