---
title: Map
layout: map
---

<!-- define JSON object for displaying data from site pages -->
<script id="page-data" type="application/json">
[
  {% assign first = true %}
  {% for page in site.pages %}
    {% if page.geo %}
      {% unless first %},{% endunless %}
      {
        "title": {{ page.title | jsonify }},
        "url": {{ page.url | jsonify }},
        "placename": {{ page.placename | jsonify }},
        "summary": {{ page.summary | jsonify }},
        "geo": {{ page.geo | jsonify }}
      }
      {% assign first = false %}
    {% endif %}
  {% endfor %}
]
</script>

<script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
<script src="https://cdn.jsdelivr.net/npm/js-yaml@4.1.0/dist/js-yaml.min.js"></script>

<link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />

<div id="map" style="height: 90vh"></div>

<script>
document.addEventListener("DOMContentLoaded", function() {
  // Get the JSON data from the script tag
  const pages = JSON.parse(document.getElementById('page-data').textContent);

  // Initialize the map
  var map = L.map('map').setView([39, -98], 4);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
    attribution: '© OpenStreetMap contributors'
  }).addTo(map);

  pages.forEach(page => {
    if (page.geo && page.geo.length === 2) {
      L.marker(page.geo)
        .addTo(map)
        .bindPopup(`<a href="{{site.baseurl}}${page.url}">
        <h4>${page.placename}</h4>
        <h5>${page.title}</h5>
        <div class="map-card">${page.summary}</div>
        </a>`);
    }
  });
});
</script>