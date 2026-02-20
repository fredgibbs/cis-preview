---
title: Documentation
layout: base
date: 2026-01-04
summary: Complete documentation for the Xanthan framework
---

# Xanthan Documentation

This documentation matches the version of Xanthan code in your repository. For the latest features and updates, visit [xanthan-web.github.io/xanthan](https://xanthan-web.github.io/xanthan/).

Choose a section to explore:

{% assign getting_started = site.pages | where_exp: "page", "page.path contains 'docs/getting-started'" | sort: "order" %}
{% assign content_design = site.pages | where_exp: "page", "page.path contains 'docs/content-design'" | sort: "order" %}
{% assign navigation = site.pages | where_exp: "page", "page.path contains 'docs/navigation'" | sort: "order" %}
{% assign scrollstories = site.pages | where_exp: "page", "page.path contains 'docs/scrollstories'" | sort: "order" %}

## Getting Started

{% include nav/card-toc.html rows=getting_started %}

---

## Content & Design

{% include nav/card-toc.html rows=content_design %}

---

## Navigation

{% include nav/card-toc.html rows=navigation %}

---

## ScrollStories

{% include nav/card-toc.html rows=scrollstories %}

---

## Additional Resources

- [Main Xanthan Site](https://xanthan-web.github.io/xanthan/) - Latest documentation and updates
- [FAQs](/faqs) - Common questions and answers
- [About Xanthan](/about) - Philosophy and approach

---

{: .text-muted}
**Note:** You can safely delete this `/docs/` folder whenever you want. However, you might keep it for reference and remove the link from your top-nav.