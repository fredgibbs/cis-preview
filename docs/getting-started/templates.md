---
layout: xanthan
title: Choose a Template
date: 2026-02-14
---

<style>
.template-buttons {
  display: flex;
  gap: var(--spacing-xs);
  margin-top: var(--spacing-md);
}

.template-btn {
  padding: var(--spacing-xs) var(--spacing-md);
  font-size: 0.9rem;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border-medium);
  background: var(--bg-card);
  color: var(--text-body);
  text-decoration: none;
  cursor: pointer;
  text-align: center;
}

.template-btn:hover {
  background: var(--accent-border-weak);
  border-color: var(--accent-border);
}

.template-btn.primary {
  background: var(--accent-primary);
  color: var(--white);
  border-color: var(--accent-primary);
}

.template-btn.primary:hover {
  background: var(--interactive-hover);
  border-color: var(--interactive-hover);
}
</style>

# Choose a Template

Xanthan offers four starting points, each designed for a different kind of project. Pick the one closest to what you're building---you can always add features later.

Browse the options below, then click "Use this template" to jump into the setup process with the right instructions already loaded.

---

## Portfolio

{% include images/figure.html image-path="/assets/images/portfolio-screenshot.png" class="right" width="45%" alt-text="Portfolio template screenshot" caption="" %}

A personal or professional site for presenting your work, interests, and credentials. Comes with an about page, a CV, and sample project pages---the kind of structure that helps you own your professional identity rather than renting it from LinkedIn. This is the most common starting point for individual projects: a handful of pages with a clear top navigation bar connecting them.

<div class="template-buttons">
  <a class="template-btn primary" href="/docs/getting-started/?template=portfolio">Use this template</a>
  <a class="template-btn" href="https://xanthan-web.github.io/portfolio-template" target="_blank">View demo</a>
</div>

---

## Class Project

{% include images/figure.html image-path="/assets/images/class-project-screenshot.png" class="right" width="45%" alt-text="Class Project template screenshot" caption="" %}

Built for collaboration. Where the Portfolio template assumes one author with a few pages, this one assumes many contributors producing individual pieces---student essays, research entries, case studies---that belong together as a collection. Card-based directory pages organize contributions automatically, so the site grows as people add to it. The instructor sets up the structure; students fill it in.

<div class="template-buttons">
  <a class="template-btn primary" href="/docs/getting-started/?template=class-project">Use this template</a>
  <a class="template-btn" href="https://xanthan-web.github.io/class-project-template" target="_blank">View demo</a>
</div>

---

## ScrollStory

{% include images/figure.html image-path="/assets/images/forest-scroll.gif" class="right" width="45%" alt-text="ScrollStory template example" caption="" %}

A single immersive narrative rather than a multi-page site. Background images shift as you scroll, text panels slide in from the side, and the reading experience becomes part of the argument. If you've used ESRI StoryMaps or Knight Lab's StoryMap, this is the open-source alternative you actually own. Start here if your project is one sustained visual essay rather than a collection of separate pages.

<div class="template-buttons">
  <a class="template-btn primary" href="/docs/getting-started/?template=scrollstory">Use this template</a>
  <a class="template-btn" href="https://xanthan-web.github.io/scrollstory-template" target="_blank">View demo</a>
</div>

---

## Full Xanthan

Everything. All templates, all documentation, all components, all examples. More than most people need to start with, but useful if you want to see every feature in context before deciding what to keep. Also the right choice for instructors setting up a reference site or anyone who plans to build something that doesn't fit neatly into the categories above.

<div class="template-buttons">
  <a class="template-btn primary" href="/docs/getting-started/?template=xanthan">Use this template</a>
  <a class="template-btn" href="https://github.com/xanthan-web/xanthan" target="_blank">View on GitHub</a>
</div>

---

## Not sure?

Start with **Portfolio** if you're building something for yourself, or **Class Project** if you're working with students. You can always add ScrollStory features to either template later---the components are modular. The templates are starting points, not ceilings.
