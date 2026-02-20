---
title: Component Library
layout: xanthan
date: 2026-02-14
---

{% include nav/scrollspy-toc.html %}

# Component Library

Every include in Xanthan, with its parameters and copy-paste code. These are reusable components you drop into any page using Liquid's `include` tag. They live in the `_includes/` directory and are organized by function.

---

## Inline Image

**File:** `images/figure.html`

Places an image in your content with caption and alt-text. Text wraps around `left` and `right` images.

```
{% raw %}{% include images/figure.html
  class="right"
  width="40%"
  caption="A descriptive caption"
  alt-text="Description for screen readers"
  image-path="/assets/images/photo.jpg"
%}{% endraw %}
```

| Parameter | Required | Default | Options / Notes |
|-----------|----------|---------|-----------------|
| `image-path` | yes | --- | Relative or absolute path to image |
| `class` | no | --- | `left`, `center`, `right` |
| `width` | no | `40%` | Any CSS width value |
| `caption` | no | --- | Supports Markdown |
| `alt-text` | no | uses caption | Accessibility text for screen readers |

**Side-by-side:** Use two `figure.html` includes with `class="left"` and `width="48%"`, then add `<p style="clear:both"></p>` after both.

---

## Jumbotron

**File:** `images/jumbotron.html`

Full-browser-width image, useful as a section divider or dramatic visual break. Breaks out of the page content margins.

```
{% raw %}{% include images/jumbotron.html
  height="50vh"
  image-path="/assets/images/backgrounds/pano-1.jpg"
  title="Section Title"
  text="Optional subtitle"
  background-position="center"
%}{% endraw %}
```

| Parameter | Required | Default | Notes |
|-----------|----------|---------|-------|
| `image-path` | yes | --- | Path to image |
| `height` | no | `40vh` | CSS height value |
| `title` | no | --- | Heading text overlaid on image |
| `text` | no | --- | Subtitle text overlaid on image |
| `background-position` | no | browser default | `center`, `top`, `bottom`, `200px`, `50% 80%` |

---

## Before/After Slider

**File:** `images/juxtapose.html`

Draggable slider for comparing two images. Uses the [Juxtapose](https://juxtapose.knightlab.com/) library.

```
{% raw %}{% include images/juxtapose.html
  image1="/assets/images/before.jpg"
  image2="/assets/images/after.jpg"
  caption="Before and after renovation."
  starting-position="50%"
%}{% endraw %}
```

| Parameter | Required | Default | Notes |
|-----------|----------|---------|-------|
| `image1` | yes | --- | Left image path |
| `image2` | yes | --- | Right image path |
| `caption` | no | --- | Caption below slider |
| `starting-position` | no | `50%` | Initial slider position |

---

## Image Carousel

**File:** `images/carousel.html`

Slideshow of multiple images with optional titles and captions. Requires pre-defined lists.

```
{% raw %}{% assign images =
"/assets/images/photo-1.jpg,
/assets/images/photo-2.jpg,
/assets/images/photo-3.jpg" | split: ','
%}

{% assign headers =
"First Title,,Third Title" | split: ','
%}

{% assign captions =
"Caption for first image|
Caption for second image|
" | split: '|'
%}

{% include images/carousel.html
  width="80%"
  class="center"
  images=images
  headers=headers
  captions=captions
%}{% endraw %}
```

| Parameter | Required | Default | Notes |
|-----------|----------|---------|-------|
| `images` | yes | --- | Pre-assigned list of image paths (comma-separated) |
| `headers` | no | --- | Slide titles (comma-separated; use empty values to skip) |
| `captions` | no | --- | Slide captions (pipe-separated to allow commas in text) |
| `width` | no | `100%` | CSS width |
| `class` | no | --- | `left`, `center`, `right` |
| `id` | no | `carouselExample` | Unique ID (required for multiple carousels on one page) |

---

## Alert Box

**File:** `typography/alert.html`

Colored callout box for tips, warnings, or important information.

```
{% raw %}{% include typography/alert.html
  class="info"
  title="Note"
  text="Your message here. **Markdown** is supported."
%}{% endraw %}
```

| Parameter | Required | Default | Notes |
|-----------|----------|---------|-------|
| `class` | yes | --- | `info` (blue), `warning` (yellow), `danger` (red), `success` (green) |
| `text` | yes | --- | Alert content; supports Markdown |
| `title` | no | --- | Bold heading at top of alert |

---

## Pull Quote / Aside

**File:** `typography/aside.html`

Styled sidebar text that floats alongside content. Good for highlighting key quotes or tangential points.

```
{% raw %}{% include typography/aside.html
  class="right"
  width="40%"
  text="The interesting thing about this approach is that it challenges conventional assumptions."
%}{% endraw %}
```

| Parameter | Required | Default | Notes |
|-----------|----------|---------|-------|
| `text` | yes | --- | Quote or aside content; supports Markdown |
| `class` | no | `right` | `left` or `right` |
| `width` | no | `40%` | CSS width |

---

## Audio Player

**File:** `media/audio.html`

HTML5 audio player. See [Media](../editing/media) for details on hosting audio files.

```
{% raw %}{% include media/audio.html
  src="/assets/audio/interview.mp3"
%}{% endraw %}
```

| Parameter | Required | Default | Notes |
|-----------|----------|---------|-------|
| `src` | yes | --- | Path to audio file (MP3, WAV, OGG) |

---

## Scrollspy Table of Contents

**File:** `nav/scrollspy-toc.html`

Floating sidebar that auto-generates a table of contents from all `h2` headings on the page. Highlights the current section as the reader scrolls.

```
{% raw %}{% include nav/scrollspy-toc.html %}{% endraw %}
```

No parameters. Place near the top of your page content (after front matter). On mobile, it collapses to a static block above the content.

---

## Card: Table of Contents

**File:** `nav/card-toc.html`

Renders a list of compact, text-focused cards from a set of pages.

```
{% raw %}{% assign card_pages = site.pages | where_exp: "page", "page.path contains 'essays/'" %}

{% include nav/card-toc.html rows = card_pages %}{% endraw %}
```

| Parameter | Required | Notes |
|-----------|----------|-------|
| `rows` | yes | A Liquid-assigned collection of pages |

Pages should have `title`, `author`, and `summary` in their front matter for best results.

---

## Card: Stacked

**File:** `nav/card-stack.html`

Wide horizontal cards with larger images, stacked vertically.

```
{% raw %}{% assign stacked_cards = site.pages | where_exp: "page", "page.path contains 'essays/'" %}

{% include nav/card-stack.html cards = stacked_cards %}{% endraw %}
```

| Parameter | Required | Notes |
|-----------|----------|-------|
| `cards` | yes | A Liquid-assigned collection of pages |

---

## Card: Grid

**File:** `nav/card-grid.html`

Traditional card grid layout with balanced text and images.

```
{% raw %}{% assign stories = site.pages | where_exp: "page", "page.path contains 'essays/'" %}

{% include nav/card-grid.html cards = stories %}{% endraw %}
```

| Parameter | Required | Notes |
|-----------|----------|-------|
| `cards` | yes | A Liquid-assigned collection of pages |

---

## Interactive Map

**File:** `nav/map.html`

Leaflet-based map that auto-generates markers from pages with `geo` front matter.

```
{% raw %}{% include nav/map.html
  height="600px"
  width="100%"
  start_coords="[39.8283, -98.5795]"
  zoom=4
%}{% endraw %}
```

| Parameter | Required | Default | Notes |
|-----------|----------|---------|-------|
| `height` | no | `700px` | CSS height |
| `width` | no | `100%` | CSS width |
| `start_coords` | no | `[44.967, -103.767]` | Initial center `[lat, lng]` |
| `zoom` | no | `4` | Zoom level 1--18 |
| `id` | no | `map` | Unique ID for multiple maps |

Pages appear as markers when they have `geo: [lat, lng]` in their front matter. Optional fields: `placename`, `summary`, `header-image`.

---

## Breadcrumbs

**File:** `nav/breadcrumbs.html`

Auto-generated navigation trail based on the page's URL path.

```
{% raw %}{% include nav/breadcrumbs.html %}{% endraw %}
```

No parameters. Renders a trail like: Home > Section > Page.

---

## Feature Row

**File:** `layout/feature-row.html`

A horizontal row with text and a button link. Useful for landing pages or feature lists.

```
{% raw %}{% include layout/feature-row.html
  title="Explore Projects"
  text="See what students have built with Xanthan."
  link="/projects/"
  button="View Projects"
  text-width="50"
%}{% endraw %}
```

| Parameter | Required | Default | Notes |
|-----------|----------|---------|-------|
| `title` | yes | --- | Heading text |
| `text` | yes | --- | Description text |
| `link` | yes | --- | Button destination URL |
| `button` | no | uses `title` | Button label |
| `text-width` | no | `50` | Percentage width of text area |

---

## Header Image (via front matter)

**File:** `layout/header-image.html`

This include is called automatically by the page layout when `header-image` is present in the front matter. You don't call it directly---just add these fields to your page:

```yaml
---
header-image: /assets/images/backgrounds/canyon.jpg
header-height: 50vh
header-position: center
---
```

| Front matter field | Default | Notes |
|--------------------|---------|-------|
| `header-image` | --- | Path to image (required to trigger header) |
| `header-height` | `40vh` | CSS height |
| `header-position` | browser default | `center`, `top`, `200px`, etc. |

---

## Peekaboo Background

**File:** `scrollybox/bg.html`

A fixed background image that is revealed as page content scrolls over it, creating a parallax-like effect.

```
{% raw %}{% include scrollybox/bg.html
  height="40vh"
  image-path="/assets/images/backgrounds/pano-1.jpg"
%}{% endraw %}
```

| Parameter | Required | Default | Notes |
|-----------|----------|---------|-------|
| `image-path` | yes | --- | Path to image |
| `height` | no | `40vh` | CSS height |

---

## ScrollStory components

The `scrollybox/` directory contains several additional includes for building ScrollStory narratives. These are documented in the [ScrollStories](/docs/scrollstories) section:

| Include | Purpose |
|---------|---------|
| `scrollybox/bg-switch.html` | Switch background images as the reader scrolls |
| `scrollybox/bg-sticky.html` | Background stays fixed while text scrolls over it |
| `scrollybox/bg-multi-long.html` | Multiple background sections in sequence |
| `scrollybox/auto-scroll.html` | Side-scrolling text panels |

See the [ScrollStory examples](/docs/scrollstories) for these components in action.
