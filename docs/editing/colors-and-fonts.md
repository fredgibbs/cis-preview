---
layout: xanthan
title: Colors & Fonts
---

# Colors & Fonts
The fastest way to personalize your site is to change colors and fonts in `assets/css/base.css`. These are small, targeted changes---no need to create a separate file. If you want to develop a complete visual identity, see [Themes](themes).

## Changing Colors

The `:root` section of `base.css` defines color "variables" that your whole site uses. Change one variable, and every element using that color updates automatically:

```css
:root {
  /* Named colors - your palette */
  --sage: #6b8e7f;
  --warm-white: #f5f3f0;
  --golden-clay: #b8956a;

  /* Semantic variables - what colors are used for */
  --bg-page: var(--warm-white);
  --text-body: var(--sage-dark);
  --accent-primary: var(--sage);
}
```

### Two-Tier Color System

Xanthan uses a two-tier system:

1. **Named colors** - Your actual color palette (e.g., `--sage: #6b8e7f`)
2. **Semantic variables** - What those colors are used for (e.g., `--bg-page: var(--sage)`)

To change colors:
- **Quick changes:** Just change what a semantic variable points to
- **Complete redesign:** Define new named colors, then update semantic variables

### Example: Quick Color Swap

Change the page background from warm white to light blue:

```css
:root {
  /* Add your new color */
  --light-blue: #e3f2fd;

  /* Update the semantic variable */
  --bg-page: var(--light-blue);  /* was var(--warm-white) */
}
```

### Example Palettes

#### Dark Theme
```css
--navy: #1a1a1a;
--cream: #e0e0e0;
--teal: #00ff88;

--bg-page: var(--navy);
--text-body: var(--cream);
--accent-primary: var(--teal);
```

#### High Contrast
```css
--pure-white: #ffffff;
--pure-black: #000000;
--bright-blue: #0055ff;

--bg-page: var(--pure-white);
--text-body: var(--pure-black);
--accent-primary: var(--bright-blue);
```

---

## Changing Fonts

In `base.css`, update the font variables:

```css
:root {
  --font-heading: 'Your Heading Font', sans-serif;
  --font-body: 'Your Body Font', sans-serif;
  --font-mono: 'Your Code Font', monospace;
}
```

**Remember:** Add the font import at the top of `base.css`:

```css
@import url('https://fonts.googleapis.com/css2?family=Your+Font&display=swap');
```

## Adjusting Sizes

In `assets/css/typography.css`, adjust heading sizes:

```css
h1 {
  font-size: 2.5rem;  /* Larger headings */
}

p {
  font-size: 1.2rem;   /* Bigger body text */
  line-height: 1.8;    /* More line spacing */
}
```

## Changing Spacing

In `base.css`, adjust spacing variables:

```css
:root {
  --spacing-sm: 1.5rem;   /* More space */
  --spacing-md: 2rem;
  --spacing-lg: 3rem;
}
```

---

## Color Selection Tools

- [Coolors](https://coolors.co/) - Generate color palettes
- [Adobe Color](https://color.adobe.com/) - Color wheel and palette tools
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) - Ensure text readability

---

## Tips

**Contrast matters:** Ensure text is readable against backgrounds. Use contrast checkers.

**Test with real content:** View changes across different page types---home, essays, guides.

**Use browser DevTools:** Right-click any element and choose "Inspect" to see which CSS rules apply. You can experiment with changes in the browser before editing files.

**Hex codes:** Colors use 6-digit codes like `#6b8e7f`. `#ffffff` = white, `#000000` = black.

---

## Troubleshooting

**Colors didn't change:**
- Clear browser cache (Cmd+Shift+R on Mac, Ctrl+Shift+R on Windows)
- Check that you saved `base.css`
- Verify the variable name matches exactly

**Some elements unchanged:**
- Your selector might need to be more specific
- Check if another CSS file is overriding your changes

---

## Next Steps

- See [Typography](typography) for text formatting and hierarchy
- See [Themes](themes) to create a complete custom visual identity
- Explore the [Color Palettes](../reference/color-palettes) comparison tool
