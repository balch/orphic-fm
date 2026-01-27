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

{% assign albums = site.albums | sort: 'date' | reverse %}
{% assign latest_album = albums | first %}
{% if latest_album.album %}
{% assign latest_album_slug = latest_album.album | slugify %}
{% assign latest_album_url = "/albums/" | append: latest_album_slug | append: "/" %}
{% endif %}

{% if latest_album %}
<section id="featured-album" class="featured-album-section">
  <div class="container narrow">
    <div class="album-container">
      <div class="video-card large">
        <div class="video-container">
          <video 
            src="{{ latest_album.video_url | relative_url }}" 
            class="video-lightbox-trigger"
            {% if latest_album.poster_url %}poster="{{ latest_album.poster_url | relative_url }}"{% endif %}
            playsinline 
            loop 
            muted 
            autoplay></video>
          <div class="sound-toggle" aria-label="Toggle Sound">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M11 5L6 9H2v6h4l5 4V5z"></path>
              <line x1="23" y1="9" x2="17" y2="15"></line>
              <line x1="17" y1="9" x2="23" y2="15"></line>
            </svg>
          </div>
        </div>
      </div>

      <div class="album-info">
        <div class="album-header-group">
          <div class="album-meta-top">
            <span class="album-date">{{ latest_album.date | date: "%B %d, %Y" }}</span>
            {% if latest_album.album %}
              <span class="dot-separator"></span>
              <a class="album-album" href="{{ latest_album_url | relative_url }}">{{ latest_album.album }}{% if latest_album.track %} — Track {{ latest_album.track }}{% endif %}</a>
            {% endif %}
            {% if latest_album.length %}
              <span class="dot-separator"></span>
              <span class="album-length">{{ latest_album.length }}</span>
            {% endif %}
          </div>
          <h2 class="album-display-title">{{ latest_album.title }}</h2>
        </div>

        <div class="album-body-text">
          {{ latest_album.description | markdownify }}
        </div>

        {% if latest_album.tags %}
          <div class="album-tags-list">
            {% for tag in latest_album.tags %}
              <span class="album-tag">#{{ tag }}</span>
            {% endfor %}
          </div>
        {% endif %}
      </div>
    </div>
  </div>
</section>

<section class="gallery-section">
  <div class="container">
    <div class="section-label">Gallery</div>
    <div class="album-grid">
      {% for album in albums %}
        {% unless album.url == latest_album.url %}
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
                  <span>{{ album.album }}{% if album.track %} #{{ album.track }}{% endif %}</span>
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
        {% endunless %}
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
    padding: 12rem 0 6rem;
    text-align: center;
    position: relative;
    z-index: 1;
  }
  
  .hero-title {
    font-size: var(--hero-font-size);
    font-weight: 800;
    letter-spacing: -0.07em;
    margin: 0;
    line-height: 0.85;
    background: linear-gradient(180deg, #fff 0%, rgba(255,255,255,0.4) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  
  .hero-subtitle {
    font-size: clamp(1.1rem, 2vw, 1.5rem);
    opacity: 0.4;
    font-weight: 300;
    margin-top: 2rem;
    letter-spacing: 0.05em;
  }
  
  .featured-album-section {
    padding-bottom: 12rem;
    position: relative;
  }
  
  .narrow {
    max-width: 1000px;
  }
  
  .album-container {
    display: flex;
    flex-direction: column;
    gap: 4rem;
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
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
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
    justify-content: center;
    gap: 1rem;
    margin-bottom: 1rem;
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
    font-size: clamp(2.5rem, 5vw, 4rem);
    font-weight: 700;
    letter-spacing: -0.03em;
    margin: 0;
  }
  
  .album-body-text {
    font-size: 1.25rem;
    line-height: 1.7;
    opacity: 0.7;
    margin-bottom: 3rem;
    font-weight: 400;
  }
  
  .album-tags-list {
    display: flex;
    gap: 0.5rem;
    justify-content: center;
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

  .gallery-section {
    padding: 6rem 0 12rem;
    border-top: 1px solid rgba(255,255,255,0.05);
  }

  .section-label {
    font-size: 0.8rem;
    font-weight: 600;
    opacity: 0.3;
    text-transform: uppercase;
    letter-spacing: 0.2em;
    margin-bottom: 4rem;
    text-align: center;
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

  @media (max-width: 768px) {
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
    .album-container { gap: 2.5rem; }
    .album-display-title { font-size: clamp(2rem, 8vw, 3rem); }
    .album-body-text { font-size: 1.1rem; margin-bottom: 2rem; }
  }
</style>
