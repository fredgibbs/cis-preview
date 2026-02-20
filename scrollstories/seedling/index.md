---
title: Seedling
author: Fred Gibbs
layout: scrollstory
date: 2025-07-21
thumbnail: images/seedling-card.png
summary: Perfect for beginners getting comfortable with Markdown and digital essays. Basically section headings, a few images, and some pull quotes. Nothing fancy, but enough to make a visually compelling essay.
header-image: images/seedling-card.png
header-title:
header-position: 0px
geo: [37.88, -81.08]
placename: New River Gorge National Park
toc-section: first
tags:
    - history
    - campus
---

# A Seedling Essay
This essay demonstrates the **simplest ScrollStory approach**—perfect if you're just learning Markdown or want students to focus on writing rather than complex formatting. As you scroll through, notice the clean, uncluttered design that lets content breathe.

**What makes this a "Seedling" essay?** It uses only basic components: section headings, images with captions, pull quotes, and footnotes. No background switching, no side-scrolling—just straightforward digital storytelling that's more visually engaging than a standard web page.

The text below is mostly filler to show how an essay flows, but we'll call out key features as you encounter them.


## Your First Section Heading
{% include images/figure.html
class="right"
width="48%"
caption="This is a right-aligned image that takes up roughly half the page width. Notice how text wraps around it naturally. [Source](https://rmoa.unm.edu/docviewer.php?docId=nmu1unma028.xml)"
image-path="images/mvh-history-stays.jpg"
%}

This paragraph sits next to a **right-aligned image**. The ScrollStory layout gives images breathing room—you'll never see cramped text squished against a photo. The spacing and typography are designed to feel more like a magazine than a typical web page.

Notice the caption below the image includes a clickable source link. This is how you maintain scholarly rigor while keeping the visual design clean.[^1]

[^1]: Footnotes work normally in ScrollStories. Click the number to jump to the note, then click the return arrow to come back. This keeps your main text flowing while providing space for citations and elaboration.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pretium, nibh vel posuere pretium, neque ipsum maximus libero, ac maximus quam ante sit amet dolor. Integer pharetra semper sem sed sagittis. Curabitur mauris tortor, elementum non felis id, hendrerit efficitur metus.

Sed efficitur leo in magna pretium, euismod malesuada risus interdum. Proin sed libero et enim pulvinar convallis non eget est. Sed ultrices dui vitae enim semper accumsan. Duis quis aliquam nulla.


## Section Headings Create Visual Breaks
Each section heading (marked with `##` in Markdown) creates a clear visual break in your essay. This helps readers navigate long-form content and gives you natural places to shift topics or introduce new ideas.

**Why this matters for students:** Breaking essays into clear sections makes writing more manageable. Write one section at a time, preview it, then move to the next. No need to tackle the entire essay at once.

Praesent sed vehicula velit, vel hendrerit neque. Vivamus scelerisque sed nunc nec congue. Curabitur sapien risus, finibus id tincidunt iaculis, porta et ipsum. Cras eu mollis sapien. Sed a mauris finibus orci molestie mollis.


## Pull Quotes Add Emphasis
Pellentesque viverra hendrerit sapien eu consequat. Curabitur leo ante, vestibulum a tincidunt eget, placerat eu nunc. Donec ut sem mi. Vivamus commodo nec sem eget pretium. Nulla ullamcorper volutpat venenatis.

{% include typography/aside.html class="right" text="
This is a pull quote—a design element that highlights important text or quotations. It appears as a semi-transparent box to the right of your main text. Use these sparingly for maximum impact." %}

The pull quote you just saw is created with a simple `include` command in Markdown. It's one of many reusable components in Xanthan. You can put important quotes, key statistics, or memorable phrases in these boxes to create visual interest and emphasize crucial points.

Duis eros odio, fringilla et pulvinar vitae, eleifend quis elit. Sed eleifend lectus in bibendum elementum. Vivamus ut velit dignissim, cursus libero nec, commodo orci. Morbi lacus metus, posuere ut pretium ac, malesuada id ligula. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed consequat, lacus id blandit ornare, mi nisi rutrum ante, vitae dignissim mauris nisl mattis nisl.


### Subsection Headings (Optional)
If you need more structure within a section, use subsection headings (marked with `###`). These are slightly smaller than main section headings and help organize complex topics without breaking up the flow too much.

**Most student essays won't need subsections**—stick with main sections (`##`) unless you're writing something particularly detailed. Simpler is usually better.

Duis ut dui dolor. Integer eu lectus at tellus accumsan euismod eget a ligula. Morbi venenatis, elit eu varius fermentum, ligula est dictum massa, sit amet ullamcorper augue nisl ut nunc. Integer placerat vitae metus vitae faucibus.


## Images Can Be Different Widths
{% include images/figure.html class="right" width="60%" caption="This image is set to 60% width instead of 48%, giving it more prominence. You can adjust image widths to suit your content. [Source](https://rmoa.unm.edu/docviewer.php?docId=nmu1unma028.xml)" image-path="images/mvh-floorplan.jpg" %}

The image to the right is **wider than the previous one** (60% instead of 48%). You control this with the `width` parameter in the image code. Want a small image? Use 30%. Want something that dominates? Try 70%.

Images can also be left-aligned (use `class="left"`) or centered full-width (we'll show that in more advanced essays). For Seedling level, right-aligned images at 48-60% width work well for most purposes.

Duis vehicula erat et diam pharetra iaculis. Etiam rutrum scelerisque nunc, ut interdum justo pellentesque sit amet. Vivamus cursus massa mauris, a finibus felis laoreet quis. Integer vel molestie neque.


## The Rhythm of a ScrollStory
By now you've scrolled through several sections and noticed the **rhythm** of a ScrollStory: heading, text, image, text, pull quote, text. This creates a visual cadence that keeps readers engaged without overwhelming them.

**For your own essay:** Think about pacing. Where do readers need a visual break? Where should an image reinforce your argument? When does a pull quote emphasize a key point? These decisions make the difference between a wall of text and an engaging narrative.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus pretium, nibh vel posuere pretium, neque ipsum maximus libero, ac maximus quam ante sit amet dolor. Integer pharetra semper sem sed sagittis. Aliquam in sapien mauris. Aliquam erat volutpat.

Nunc congue ultrices lacus, a efficitur massa pulvinar at. Sed luctus orci sed sem commodo, in rhoncus orci sagittis. Duis in sagittis arcu. Donec dictum aliquam congue. Nulla varius ipsum vitae nibh dapibus, et tincidunt turpis gravida.


## Block Quotes for Extended Quotations
Sed efficitur leo in magna pretium, euismod malesuada risus interdum. Proin sed libero et enim pulvinar convallis non eget est. Sed ultrices dui vitae enim semper accumsan. Duis quis aliquam nulla. Aenean scelerisque lacus vel pretium viverra.

> This is a block quote, created by putting a `>` symbol before your text. Use these for extended quotations from primary sources, scholarly works, or historical documents. They're visually distinct from pull quotes—block quotes span the full text width, while pull quotes float to the side.

Block quotes work well when you want to quote an entire paragraph or passage, while pull quotes are better for short, punchy excerpts you want to highlight visually.


## What You've Learned So Far
If you can create this Seedling essay, you can:
- Structure content with section headings
- Add images with captions and source links
- Include footnotes for citations
- Use pull quotes for emphasis
- Format block quotes for extended quotations
- Control image sizes and placement

**That's enough to create compelling digital scholarship.** The Sapling and Forest essays add more sophisticated features, but this foundation works for most student projects and many professional ones too.

Duis eros odio, fringilla et pulvinar vitae, eleifend quis elit. Sed eleifend lectus in bibendum elementum. Vivamus ut velit dignissim, cursus libero nec, commodo orci. Morbi lacus metus, posuere ut pretium ac, malesuada id ligula.


## Ready to Create Your Own?

**New to Xanthan?** Start with the [Getting Started guide](../../../docs/getting-started/) to create your own site first. Once you have a working site, come back here to build your ScrollStory.

**Already have a site based on a Xanthan template?** To make your own Seedling essay:

1. **Duplicate this folder** (`scrollstories/seedling/`) and rename it for your topic
2. **Replace the text** with your own content, keeping the same structure
3. **Add your own images** to the `images/` folder
4. **Update the header** at the top (title, author, date, etc.)
5. **Preview and adjust** spacing, image sizes, and flow

Start simple. Get comfortable with the basics. You can always add complexity later by copying and pasting elements from the other essays.

{% include scrollybox/auto-scroll.html speed=1.5 %}
