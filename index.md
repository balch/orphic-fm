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
{% assign featured_track = latest_album_tracks | first %}
{% assign latest_album = featured_track %}
{% if latest_album.album %}
{% assign latest_album_slug = latest_album.album | slugify %}
{% assign latest_album_url = "/albums/" | append: latest_album_slug | append: "/" %}
{% endif %}

{% if latest_album %}
<section id="featured-album" class="featured-album-section">
  <div class="container narrow">
    <div class="section-label">Featured Track</div>
    <div class="album-container">
      <div class="video-side">
        <div class="video-card large">
          <div class="video-container">
            <video 
              src="{{ latest_album.video_url | relative_url }}" 
              {% if latest_album.poster_url %}poster="{{ latest_album.poster_url | relative_url }}"{% endif %}
              playsinline 
              loop 
              muted 
              autoplay
              controls></video>
          </div>
        </div>

        {% if latest_album.tags %}
          <div class="album-tags-list">
            {% for tag in latest_album.tags %}
              <span class="album-tag">#{{ tag }}</span>
            {% endfor %}
          </div>
        {% endif %}

        {% if latest_album.album %}
          <div class="album-link-section mobile-only">
            <span class="album-link-label">From the album</span>
            <a class="album-link" href="{{ latest_album_url | relative_url }}">
              {{ latest_album.album }}
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M7 17L17 7M17 7H7M17 7v10"/>
              </svg>
            </a>
          </div>
        {% endif %}
      </div>

      <div class="album-info">
        <div class="album-header-group">
          <div class="album-meta-top">
            <span class="album-date">{{ latest_album.date | date: "%B %d, %Y" }}</span>
            {% if latest_album.length %}
              <span class="dot-separator"></span>
              <span class="album-length">{{ latest_album.length }}</span>
            {% endif %}
          </div>
          <h2 class="album-display-title">{{ latest_album.title }}</h2>
        </div>

        {% if latest_album.description %}
          <div class="album-body-text">
            {{ latest_album.description | markdownify }}
          </div>
        {% endif %}

        {% if latest_album.album %}
          <div class="album-link-section desktop-only">
            <span class="album-link-label">From the album</span>
            <a class="album-link" href="{{ latest_album_url | relative_url }}">
              {{ latest_album.album }}
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M7 17L17 7M17 7H7M17 7v10"/>
              </svg>
            </a>
          </div>
        {% endif %}
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
              <p class="album-card-desc">{{ album_page.description | strip_html | truncate: 100 }}</p>
            {% endif %}
            <span class="album-card-meta">{{ album_tracks_list.size }} tracks</span>
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
          <div class="grid-video-container">
            <video 
              src="{{ album.video_url | relative_url }}" 
              {% if album.poster_url %}poster="{{ album.poster_url | relative_url }}"{% endif %}
              class="video-lightbox-trigger"
              controls
              loop 
              playsinline></video>
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
  
  .featured-album-section {
    padding-bottom: 8rem;
    position: relative;
  }
  
  .narrow {
    max-width: 850px;
  }
  
  .album-container {
    display: grid;
    grid-template-columns: 1.1fr 1fr;
    gap: 3.5rem;
    align-items: flex-start;
  }

  .video-side {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
  }
  
  .video-card {
    border-radius: 40px;
    overflow: hidden;
    background: #050505;
    box-shadow: 0 60px 120px rgba(0,0,0,0.6), 0 0 0 1px rgba(255,255,255,0.05);
    transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    position: relative;
  }

  .video-card.large {
    border-radius: 40px;
  }
  
  .video-card:hover {
    transform: scale(1.01);
  }
  
  .video-container {
    position: relative;
    border-radius: 40px;
    overflow: hidden;
    aspect-ratio: 16/9;
    background: #000;
  }
  
  .video-container video {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    cursor: pointer;
  }
  
  .album-info {
    text-align: left;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  
  .album-header-group {
    margin-bottom: 2rem;
  }
  
  .album-meta-top {
    font-size: 0.8rem;
    font-weight: 600;
    opacity: 0.3;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 1rem;
    margin-bottom: 0.75rem;
    will-change: transform, opacity;
  }
  
  .dot-separator {
    width: 4px;
    height: 4px;
    background: currentColor;
    border-radius: 50%;
  }

  .album-album {
    color: inherit;
    text-decoration: none;
    opacity: 0.85;
    transition: opacity 0.3s;
  }
  .album-album:hover {
    opacity: 1;
  }
  
  .album-display-title {
    font-size: clamp(2rem, 4vw, 3rem);
    font-weight: 700;
    letter-spacing: -0.02em;
    margin: 0;
    line-height: 1.2;
  }
  
  .album-body-text {
    font-size: 1.1rem;
    line-height: 1.6;
    opacity: 0.7;
    margin-bottom: 1.5rem;
    font-weight: 400;
    overflow: hidden;
  }

  .album-body-text p {
    margin: 0;
  }

  .album-link-section {
    margin-bottom: 1.5rem;
    text-align: left;
  }

  .album-link-label {
    display: block;
    font-size: 0.75rem;
    font-weight: 600;
    opacity: 0.4;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    margin-bottom: 0.75rem;
  }

  .album-link {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--accent-primary, #8b5cf6);
    text-decoration: none;
    padding: 0.75rem 1.5rem;
    border-radius: 100px;
    border: 1px solid rgba(139, 92, 246, 0.2);
    background: rgba(139, 92, 246, 0.05);
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }

  .album-link:hover {
    background: rgba(139, 92, 246, 0.15);
    border-color: rgba(139, 92, 246, 0.4);
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(139, 92, 246, 0.2);
  }

  .album-link svg {
    transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }

  .album-link:hover svg {
    transform: translate(2px, -2px);
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
  }

  .grid-item {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .grid-video-container {
    aspect-ratio: 16/9;
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
    object-fit: cover;
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
    .video-container { border-radius: 20px; }
    .video-card { border-radius: 20px; }
    :root {
      --hero-font-size: clamp(2.8rem, 12vw, 5rem);
    }
    .hero-section { padding: 8rem 0 4rem; }
    .hero-subtitle { margin-top: 1.5rem; }
    .album-container { 
      grid-template-columns: 1fr;
      gap: 2rem; 
    }
    .album-info { text-align: center; order: -1; }
    .album-link-section { text-align: center; }
    .album-tags-list { justify-content: center; }
    .album-display-title { font-size: clamp(1.8rem, 8vw, 2.5rem); }
    .album-meta-top { display: none; }
    .album-body-text { font-size: 1rem; margin-bottom: 1.5rem; }
  }
</style>
