---
title: Sapling
author: Fred Gibbs
layout: scrollstory
date: 2025-07-21
header-image: images/sapling-card.png
thumbnail: images/sapling-card.png
summary: Our Sapling essay uses a few more features than our Seed essay, including the simplest scrolly box.
header-title:
header-position: 0px
toc-section: second
geo: [41.240000, -81.550000]
placename: Cuyahoga Valley National Park
tags:
    - history
    - nature
    - campus
---

# A Sapling Essay
This essay demonstrates **intermediate ScrollStory features**—building on what you learned in Seedling by adding scrollyboxes, carousels, and more sophisticated visual storytelling. As you scroll, we'll point out what makes this more advanced than a Seedling essay.

**What makes this a "Sapling" essay?** It includes everything from Seedling (headings, images, footnotes, pull quotes) plus immersive components: text overlaying background images, image carousels for comparisons, and more dynamic pacing. This is where ScrollStories start feeling cinematic.

The text below includes both explanations and filler content to show how these components work in practice.


## Building on Seedling Basics
{% include images/figure.html
class="right"
width="48%"
caption="Right-aligned images still work exactly like Seedling. You already know this pattern. [Source](https://rmoa.unm.edu/docviewer.php?docId=nmu1unma028.xml)"
image-path="images/mvh-history-stays.jpg"
%}

Everything from Seedling still works here: images with captions, footnotes, section headings.[^note1] The Sapling template doesn't replace what you learned—it **adds** to it.

[^note1]: Footnotes continue to work exactly as before. All your Seedling skills carry forward.

This layered approach is intentional. Master the basics, then add complexity incrementally. You're not learning a whole new system; you're expanding your toolkit with a few powerful new components.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pretium, nibh vel posuere pretium, neque ipsum maximus libero, ac maximus quam ante sit amet dolor. Integer pharetra semper sem sed sagittis. Curabitur mauris tortor, elementum non felis id, hendrerit efficitur metus.


## Your First Scrollybox
Here's what makes Sapling different: keep scrolling and watch what happens next. You're about to see text appear **over** a background image, creating an immersive reading experience.

{% include scrollybox/bg.html
  image-path="images/mvh-women-supervision.jpg"
  above-box-space = "100vh"
  below-box-space = "80vh"
  box-content=' One stated reason for building a men-only dorm is that Hokona Hall could be freed up to be used as a women-only dorm, where they would have supervision "of the best sort".'
%}


## What Just Happened?
That was a **scrollybox**—text that appears in a semi-transparent box over a full-screen background image. As you scrolled, the background image stayed fixed while the text box scrolled into view, stayed visible, then scrolled away.

**Why use scrollyboxes?** They create moments of focus and drama. The full-screen image immerses readers in a visual context, while the overlay text provides commentary, quotations, or key points. It's like a visual pause in your narrative.

**Technical note:** The `above-box-space` and `below-box-space` parameters control how much blank scroll space appears before and after the text box. Adjust these to control pacing—more space = slower, more contemplative; less space = faster pacing.


## Pull Quotes Still Work
{% include typography/aside.html class="left" text="
This left-aligned pull quote is the same component you learned in Seedling. Sapling essays can mix scrollyboxes with traditional pull quotes depending on what fits your narrative." %}

Notice how this pull quote appears alongside regular text, while the scrollybox took over the entire screen. Different tools for different purposes:

- **Pull quotes** emphasize key text within ongoing paragraphs
- **Scrollyboxes** create immersive moments that break away from normal flow

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed consequat, lacus id blandit ornare, mi nisi rutrum ante, vitae dignissim mauris nisl mattis nisl. Praesent sed vehicula velit, vel hendrerit neque.


## Image Carousels for Comparisons
Below you'll see an **image carousel**—multiple images you can click through. This is perfect when you want readers to compare several images without cluttering the page.

{% assign images =
"images/mvh-menu.jpg,
images/mvh-history-stays.jpg,
images/mvh-room-cost.jpg" | split: ','
%}

{% include images/carousel.html
id="first"
images=images
%}

**Why use carousels?** When you have 3-5 related images (historical documents, different views of a building, a sequence of photos), a carousel lets readers compare them side-by-side without scrolling past each one. Click the arrows or dots to move between images.

**Accessibility note:** Always include captions and source links so screen readers and citations work properly.


## Larger Images
{% include images/figure.html class="right" width="60%" caption="This image is 60% width instead of 48%, giving it more visual weight. Adjust widths based on what the image needs. [Source](https://rmoa.unm.edu/docviewer.php?docId=nmu1unma028.xml)" image-path="images/mvh-floorplan.jpg" %}

Just like in Seedling, you control image sizes with the `width` parameter. A floorplan or map might need 60-70% width to be legible, while a portrait might look better at 40%.

Duis ut dui dolor. Integer eu lectus at tellus accumsan euismod eget a ligula. Morbi venenatis, elit eu varius fermentum, ligula est dictum massa, sit amet ullamcorper augue nisl ut nunc.


## Block Quotes for Primary Sources
Sed efficitur leo in magna pretium, euismod malesuada risus interdum. Proin sed libero et enim pulvinar convallis non eget est.

> As of 1967 this was the design for the first floor of La Posada, reflecting the original design of Ernest J. Kump, lead design architect, and the alteration made by Sherman Smith. [Source](https://rmoa.unm.edu/docviewer.php?docId=nmu1unma028.xml)

Block quotes span the full text width and are perfect for extended quotations from archival sources, documents, or scholarly works. They're visually distinct from the scrollybox overlays and pull quotes.


## What You've Learned in Sapling
If you can create a Sapling essay, you can:

- **Use scrollyboxes** to overlay text on full-screen background images
- **Control pacing** with scroll space parameters
- **Add image carousels** for comparing multiple related images
- **Mix components** - scrollyboxes, pull quotes, carousels, and standard images in one essay
- **Create immersive narratives** that feel more like multimedia stories than traditional web pages

**This is enough for most sophisticated digital humanities projects.** The Forest essay adds background switching and side-scrolling for even more cinematic effects, but Sapling gives you all the tools for compelling visual scholarship.


## Bibliography

- Hooker, Van Dorn, Melissa Howard, and V. B Price. _Only in New Mexico: An Architectural History of the University of New Mexico: The First Century, 1889-1989_. Albuquerque, NM: University of New Mexico Press, 2000.

- University of New Mexico. Bainbridge Bunting Photograph Collection, 1870-1980, collection PICT 000-385, box 6	folder 102. Center for Southwest Research, University Libraries, University of New Mexico.

- University of New Mexico. Dept. of Facility Planning architectural drawings, 1892-2011, collection SWA UNMFPLAN Drawings, Stack 13	Drawer 01. Center for Southwest Research, University Libraries, University of New Mexico.

- University of New Mexico. Dept. of Facility Planning Records, 1889-, collection UNMA 028,Box  34. Center for Southwest Research, University Libraries, University of New Mexico.

---

## Ready to Create Your Own?

**New to Xanthan?** Start with the [Getting Started guide](../../../docs/getting-started/) to create your own site first. Once you have a working site, come back here to build your ScrollStory.

**Already have a Xanthan site?** To make your own Sapling essay:

1. **Duplicate this folder** (`scrollstories/sapling/`) and rename it for your topic
2. **Replace the text** with your own content, keeping the structure
3. **Add your own images** to the `images/` folder
4. **Update the front matter** at the top (title, author, date, header image, etc.)
5. **Customize components** - Add or remove scrollyboxes, carousels, and asides as needed

**What makes Sapling different from Seedling?**
- Background scrollyboxes for immersive text overlays
- Image carousels for comparing multiple images
- More sophisticated visual storytelling
- All Seedling components still work

Ready for even more? Check out the [Forest template](../forest/) for advanced features like background switching and side-scrolling.

{% include scrollybox/auto-scroll.html speed=1.5 %}
