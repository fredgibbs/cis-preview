---
title: Navigation
layout: xanthan
date: 2026-02-14
---

{% include nav/scrollspy-toc.html %}

# Navigation

As a site grows beyond a handful of pages, navigation becomes an argument about what matters and how things relate. Xanthan provides several navigation systems---from a top menu bar to auto-generated card directories to interactive maps---and you can combine them freely. A class project might use a top navbar for site-wide structure, cards on a landing page, a left sidebar for browsing essays, and a map for geographic context.

---

## Top navigation bar

The horizontal menu at the top of every page is controlled by a single YAML file: `_data/top-nav.yml`. No HTML, no coding---just a structured list of titles and URLs.

### Basic structure

```yaml
- title: "About"
  url: "/about"

- title: "Research"
  items:
    - title: "Overview"
      url: "/research/"
    - title: "Current Projects"
      url: "/research/current"
    - title: "Publications"
      url: "/publications"

- title: "Contact"
  url: "/contact"
```

This creates three menu entries: a direct link to About, a Research dropdown with three items, and a direct link to Contact.

### Two types of menu items

**Dropdown menus** group related pages under a label:

```yaml
- title: "Research"
  items:
    - title: "Overview"
      url: "/research/"
    - title: "Publications"
      url: "/publications"
```

**Direct links** go straight to a page with no dropdown:

```yaml
- title: "About"
  url: "/about"
```

### Adding dividers

Horizontal lines inside a dropdown help organize long menus:

```yaml
- title: "Content"
  items:
    - title: "Typography"
      url: "/editing/typography"
    - title: "Images"
      url: "/editing/images"

    - divider: true

    - title: "Previewing Locally"
      url: "/editing/previewing-locally"
```

### Common tasks

**Add a link to an existing menu** --- just add another `- title:` / `url:` pair under `items:`, matching the indentation (4 spaces):

```yaml
- title: "Research"
  items:
    - title: "Overview"
      url: "/research/"
    - title: "Datasets"
      url: "/datasets"
```

**Create a new dropdown** --- add a new top-level entry with `items:`:

```yaml
- title: "Teaching"
  items:
    - title: "Courses"
      url: "/teaching/courses"
    - title: "Advising"
      url: "/teaching/advising"
```

**Remove a menu** --- delete the entire block, from `- title:` through all its `items:`.

**Rename a menu** --- just change the `title:` text. The URL stays the same.

### URL guidelines

For pages on your site, always start with `/`:

```yaml
url: "/about"              # Correct
url: "/guides/tutorial"    # Correct
url: "about"               # Wrong - missing /
url: "about.md"            # Wrong - don't include .md
```

For external sites, use the full URL:

```yaml
url: "https://github.com/your-project"
```

URLs map directly to your file structure: `guides/tutorial.md` becomes `/guides/tutorial`. Folders with an `index.md` use a trailing slash: `projects/index.md` becomes `/projects/`.

### YAML syntax reminders

- **Indentation matters.** Use spaces, not tabs. Items under `items:` should be indented exactly 4 spaces.
- **Quotes are safer.** Always quote titles and URLs to avoid issues with special characters.
- **Space after colons.** `title: "Text"` works; `title:"Text"` breaks.

If your navigation disappears after an edit, paste your file into a [YAML validator](https://www.yamllint.com/) to spot syntax errors.

### Complete example

```yaml
- title: "About"
  url: "/about"

- title: "Research"
  items:
    - title: "Overview"
      url: "/research/"
    - title: "Current Projects"
      url: "/research/current"
    - title: "Publications"
      url: "/publications"

- title: "Teaching"
  items:
    - title: "Courses"
      url: "/teaching/courses"
    - title: "Advising"
      url: "/teaching/advising"

- title: "Contact"
  url: "/contact"
```

---

## Card-based navigation

Cards are visual directory pages that automatically generate links to every page in a specified folder. Each card pulls its title, author, summary, and thumbnail from the page's front matter---so the cards stay current as you add and edit pages.

### How cards work

Cards use two lines of Liquid code. The first line gathers all pages from a folder; the second renders them using a card template:

```
{% raw %}{% assign card_pages = site.pages | where_exp: "page", "page.path contains 'essays/'" %}

{% include nav/card-toc.html rows = card_pages %}{% endraw %}
```

Change `essays/` to whatever folder your pages live in. The card include handles the rest.

### Card styles

Xanthan includes three card layouts. All use the same two-line pattern---just swap the include file.

#### Table of Contents cards

Compact, text-focused cards in a vertical list. Shows title, author, and summary.

```
{% raw %}{% assign card_pages = site.pages | where_exp: "page", "page.path contains 'essays/'" %}

{% include nav/card-toc.html rows = card_pages %}{% endraw %}
```

{% assign card_pages = site.pages | where_exp: "page", "page.path contains 'scrollstories/examples'" %}

{% include nav/card-toc.html rows = card_pages %}

#### Stacked cards

Wide horizontal cards with larger images and more prominent titles, stacked vertically.

```
{% raw %}{% assign stacked_cards = site.pages | where_exp: "page", "page.path contains 'essays/'" %}

{% include nav/card-stack.html cards = stacked_cards %}{% endraw %}
```

{% assign stacked_cards = site.pages | where_exp: "page", "page.path contains 'scrollstories/examples'" %}
{% include nav/card-stack.html cards = stacked_cards %}

#### Grid cards

Traditional card grid---square or rectangular cards with balanced text and images.

```
{% raw %}{% assign stories = site.pages | where_exp: "page", "page.path contains 'essays/'" %}

{% include nav/card-grid.html cards = stories %}{% endraw %}
```

{% assign essays = site.pages | where_exp: "page", "page.path contains 'scrollstories/examples'" %}
{% include nav/card-grid.html cards = essays %}

### Making your pages card-ready

Cards look best when pages have rich front matter. At minimum, include `title` and `summary`. For cards with images, add a `thumbnail` or `header-image`:

```yaml
---
title: Acequia Landscapes
author: Carlos Medina
summary: How community irrigation systems shaped settlement patterns in the Rio Grande Valley.
header-image: images/acequia-card.jpg
---
```

---

## Left sidebar navigation

The left sidebar provides persistent navigation for all pages in a folder, visible while reading any page in that section. Useful for course projects, documentation, or any collection where readers need to jump between related pages.

**[See the left nav demo](../navigation/nav-left-demo)** to see this layout in action.

### Setting it up

**1.** Set the layout in each page's front matter:

```yaml
---
layout: nav-left
title: Your Page Title
---
```

**2.** Define navigation sections in `_data/nav-sections.yml`:

```yaml
sections:
  - name: essays
    display: "Student Essays"
  - name: resources
    display: "Resources"
```

**3.** Assign pages to sections using `toc-section` and `order`:

```yaml
---
layout: nav-left
title: River Towns
toc-section: essays
order: 3
---
```

Pages are automatically grouped by `toc-section` and sorted by `order`.

### Customization

Edit `assets/css/nav-left.css` to change sidebar width (default: 25vw), colors, fonts, or spacing.

### File structure

```
_layouts/nav-left.html          # Layout template
_data/nav-sections.yml          # Section configuration
assets/css/nav-left.css         # Sidebar styling
_includes/nav/nav-left.html     # Navigation component
```

---

## Profile sidebar

The profile sidebar layout displays a personal card on the left---photo, name, bio, and links---with page content on the right. Ideal for personal portfolio sites.

**[See the profile sidebar demo](../navigation/nav-profile-demo)** to see this layout in action.

### Setting it up

Set the layout in your page's front matter:

```yaml
---
layout: nav-profile
title: Your Page Title
---
```

Configure the sidebar in `_data/nav-profile.yml`:

```yaml
settings:
  links_font_weight: normal

image_url: /assets/images/profile/profile-sample.jpg
alt_text: "Description of your photo"
name: Your Name
description: A brief bio or tagline

links:
  - title: Website
    url: https://example.com
    icon: fas fa-globe
  - title: GitHub
    url: https://github.com/username
    icon: fab fa-github
  - title: Email
    url: mailto:you@example.com
    icon: fas fa-envelope
```

### Common icons

The sidebar uses [Font Awesome](https://fontawesome.com/icons) icons:

| Icon | Code |
|------|------|
| Website | `fas fa-globe` |
| GitHub | `fab fa-github` |
| Email | `fas fa-envelope` |
| Twitter/X | `fab fa-twitter` |
| LinkedIn | `fab fa-linkedin` |
| ORCID | `fab fa-orcid` |
| University | `fas fa-university` |

---

## Interactive maps

The map component automatically displays markers for any page with geographic coordinates. Clicking a marker shows the page title, summary, and a link.

### Adding a page to the map

Include `geo` and (optionally) `placename` in the page's front matter:

```yaml
---
title: Seedling
geo: [37.88, -81.08]
placename: New River Gorge National Park
summary: Perfect for beginners getting comfortable with digital essays.
header-image: images/seedling-card.png
---
```

### Displaying a map on a page

```
{% raw %}{% include nav/map.html
  height="600px"
  width="100%"
  start_coords="[39.8283, -98.5795]"
  zoom=4
%}{% endraw %}
```

| Parameter | Default | What it does |
|-----------|---------|--------------|
| `id` | `"map"` | Unique ID (needed for multiple maps on one page) |
| `height` | `700px` | CSS height |
| `width` | `100%` | CSS width |
| `start_coords` | `[44.967, -103.767]` | Initial center point as `[lat, lng]` |
| `zoom` | `4` | Initial zoom level (1--18, higher = closer) |

### Finding coordinates

1. Open [Google Maps](https://maps.google.com)
2. Right-click on the location
3. Click the coordinates at the top of the menu to copy them
4. Use the format `[lat, lng]` in your front matter

### Zoom level guide

| Level | View |
|-------|------|
| 4--6 | Country or region |
| 10--14 | City |
| 15--18 | Street level |

---

## Scrollspy table of contents

For long pages, a scrollspy table of contents creates a floating sidebar that tracks your reading position. It automatically generates links from all `h2` headings on the page.

```
{% raw %}{% include nav/scrollspy-toc.html %}{% endraw %}
```

Add this line near the top of your page content (after the front matter). The TOC will appear as a sticky panel on the right side of the page, highlighting the current section as you scroll.

---

## Breadcrumbs

Breadcrumbs show the current page's location in the site hierarchy:

```
{% raw %}{% include nav/breadcrumbs.html %}{% endraw %}
```

This renders a trail like: Home > Research > Current Projects

---

## Mixing navigation types

These systems are modular---use them together. A typical class project might combine:

- **Top nav** for site-wide structure (always visible)
- **Left sidebar** on essay pages for quick navigation between student work
- **Cards** on a landing page for a visual directory
- **Map** to show geographic distribution of topics

The top nav is site-wide (controlled by `top-nav.yml`). Everything else is page-level---add or remove it from individual pages as needed.
