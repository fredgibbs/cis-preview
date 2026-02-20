---
title: Color Palette Comparison
layout: xanthan
date: 2024-12-02
---

# Color Palette Comparison

Compare different color palettes for Xanthan. Click the buttons to switch between options and see how they affect the entire site.

<style>
/* Palette definitions */
.palette-current {
  --demo-primary: #c05131;
  --demo-secondary: #8a9a7b;
  --demo-accent: #f59e0b;
  --demo-bg: #F5EFE6;
  --demo-bg-secondary: #e8dcc8;
  --demo-bg-nav: #3d2817;
  --demo-text: #3a1602;
  --demo-text-light: #ffffff;
}

.palette-digital-scholar {
  --demo-primary: #4f46e5;
  --demo-secondary: #475569;
  --demo-accent: #f59e0b;
  --demo-bg: #ffffff;
  --demo-bg-secondary: #f8fafc;
  --demo-bg-nav: #1e293b;
  --demo-text: #0f172a;
  --demo-text-light: #cbd5e1;
}

.palette-friendly-modern {
  --demo-primary: #6b8e7f;
  --demo-secondary: #b8956a;
  --demo-accent: #f59e0b;
  --demo-bg: #fdfcfb;
  --demo-bg-secondary: #f5f3f0;
  --demo-bg-nav: #3d4e42;
  --demo-text: #2d3e35;
  --demo-text-light: #e8e4df;
}

.palette-minimal-clean {
  --demo-primary: #18181b;
  --demo-secondary: #71717a;
  --demo-accent: #22c55e;
  --demo-bg: #fafafa;
  --demo-bg-secondary: #f4f4f5;
  --demo-bg-nav: #18181b;
  --demo-text: #09090b;
  --demo-text-light: #e4e4e7;
}

/* Demo components */
.palette-demo {
  margin: 2rem 0;
  padding: 2rem;
  border: 2px solid #ddd;
  border-radius: 8px;
  background: var(--demo-bg);
}

.demo-nav {
  background: var(--demo-bg-nav);
  color: var(--demo-text-light);
  padding: 0.5rem 1rem;
  border-radius: 4px;
  margin-bottom: 1rem;
  display: flex;
  gap: 1rem;
  align-items: center;
}

.demo-nav-brand {
  font-weight: 600;
  font-size: 1.1rem;
}

.demo-nav-link {
  color: var(--demo-text-light);
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background 0.2s;
}

.demo-nav-link:hover {
  background: var(--demo-primary);
}

.demo-content {
  background: var(--demo-bg-secondary);
  padding: 1.5rem;
  border-radius: 4px;
  color: var(--demo-text);
}

.demo-heading {
  color: var(--demo-primary);
  margin-bottom: 0.5rem;
}

.demo-text {
  color: var(--demo-text);
  margin-bottom: 1rem;
}

.demo-link {
  color: var(--demo-primary);
  text-decoration: underline;
}

.demo-button {
  background: var(--demo-primary);
  color: var(--demo-text-light);
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
  transition: opacity 0.2s;
}

.demo-button:hover {
  opacity: 0.9;
}

.demo-secondary-button {
  background: var(--demo-accent);
  color: var(--demo-text-light);
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
  margin-left: 0.5rem;
}

.demo-accent-text {
  color: var(--demo-accent);
  font-weight: 600;
}

.switcher-buttons {
  display: flex;
  gap: 1rem;
  margin: 2rem 0;
  flex-wrap: wrap;
}

.switcher-button {
  padding: 0.75rem 1.5rem;
  border: 2px solid #333;
  border-radius: 6px;
  background: white;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.2s;
}

.switcher-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.switcher-button.active {
  background: #333;
  color: white;
}

.color-info {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin: 2rem 0;
}

.color-swatch {
  padding: 1rem;
  border-radius: 6px;
  text-align: center;
  font-size: 0.9rem;
}
</style>

<div class="switcher-buttons">
  <button class="switcher-button active" onclick="switchPalette('current')">Current (Earthy)</button>
  <button class="switcher-button" onclick="switchPalette('digital-scholar')">Digital Scholar</button>
  <button class="switcher-button" onclick="switchPalette('friendly-modern')">Friendly Modern</button>
  <button class="switcher-button" onclick="switchPalette('minimal-clean')">Minimal Clean</button>
</div>

<div id="demo-container" class="palette-demo palette-current">

  ## Navigation Demo

  <div class="demo-nav">
    <span class="demo-nav-brand">Xanthan</span>
    <a href="#" class="demo-nav-link">Instructions</a>
    <a href="#" class="demo-nav-link">Components</a>
    <a href="#" class="demo-nav-link">FAQs</a>
  </div>

  ## Content Demo

  <div class="demo-content">
    <h2 class="demo-heading">Welcome to Xanthan</h2>
    <p class="demo-text">
      Build professional portfolios, class projects, and digital narratives.
      <a href="#" class="demo-link">Learn more about our features</a>.
    </p>
    <p class="demo-text">
      This template emphasizes <span class="demo-accent-text">sustainability</span> and
      <span class="demo-accent-text">ownership</span> of your content.
    </p>
    <button class="demo-button">Get Started</button>
    <button class="demo-secondary-button">View Examples</button>
  </div>

  ## Heading Hierarchy

  <h1 style="color: var(--demo-primary);">H1 Heading - Primary Color</h1>
  <h2 style="color: var(--demo-secondary);">H2 Heading - Secondary Color</h2>
  <h3 style="color: var(--demo-primary); opacity: 0.8;">H3 Heading - Primary Variant</h3>
  <h4 style="color: var(--demo-accent);">H4 Heading - Accent Color</h4>

  ## Color Reference

  <div id="color-reference" class="color-info">
    <!-- Will be populated by JavaScript -->
  </div>

</div>

<script>
function switchPalette(palette) {
  const container = document.getElementById('demo-container');
  const buttons = document.querySelectorAll('.switcher-button');

  // Remove all palette classes
  container.className = 'palette-demo palette-' + palette;

  // Update active button
  buttons.forEach(btn => btn.classList.remove('active'));
  event.target.classList.add('active');

  // Update color reference
  updateColorReference();
}

function updateColorReference() {
  const container = document.getElementById('demo-container');
  const styles = window.getComputedStyle(container);

  const colors = {
    'Primary': styles.getPropertyValue('--demo-primary'),
    'Secondary': styles.getPropertyValue('--demo-secondary'),
    'Accent': styles.getPropertyValue('--demo-accent'),
    'Background': styles.getPropertyValue('--demo-bg'),
    'Nav Background': styles.getPropertyValue('--demo-bg-nav'),
    'Text': styles.getPropertyValue('--demo-text')
  };

  const reference = document.getElementById('color-reference');
  reference.innerHTML = '';

  for (const [name, value] of Object.entries(colors)) {
    const swatch = document.createElement('div');
    swatch.className = 'color-swatch';
    swatch.style.background = value;
    swatch.style.color = name.includes('Nav') || name === 'Text' ? '#fff' : '#000';
    swatch.innerHTML = `<strong>${name}</strong><br>${value}`;
    reference.appendChild(swatch);
  }
}

// Initialize
updateColorReference();
</script>

---

## Palette Descriptions

### Current (Earthy)
**Vibe:** Natural, organic, traditional academia
- Warm terra cotta, sage green, sand tones
- **Best for:** Sites wanting a handcrafted, artisanal feel

### Digital Scholar (Recommended)
**Vibe:** Modern academic, professional, intelligent
- Indigo (authority), slate gray (structure), amber (highlight)
- **Best for:** Contemporary digital humanities projects

### Friendly Modern
**Vibe:** Warm Southwest, natural, approachable
- Sage green (grounded), warm clay (structure), amber gold (energy)
- **Best for:** Regional projects, nature-focused work, accessible scholarship

### Minimal Clean
**Vibe:** Ultra-modern, professional, timeless
- Near-black, grays, green accent
- **Best for:** Professional portfolios, minimalist design

---

## Next Steps

1. View this page and try each palette
2. Navigate around your site with your favorite active
3. Check component pages to see how it affects real content
4. Once decided, I can implement your choice site-wide

**Note:** These are live demos - changes here don't affect your actual site until you choose one to implement.
