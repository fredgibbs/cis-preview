---
title: Essays
layout: base
header-title: Essays
---

{% assign all_pages = site.pages %}
{% assign cards = all_pages | where_exp: "p", "p.path contains 'essays/'" %}

{% include nav/card-grid.html cards=cards %}
