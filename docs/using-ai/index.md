---
title: Using AI Assistance
layout: xanthan
date: 2026-02-16
---

# Using AI Assistance

Most website frameworks assume you'll learn their technical stack before you can shape your site. Xanthan takes a different approach: its architecture is designed to be legible---not just to you, but to AI assistants. This means you can describe what you want in plain language and get results that actually work, because the AI can read the same structure you're working with.

This isn't a gimmick. It changes what's practical. Tasks that would normally require hours of learning CSS, HTML, or template syntax---redesigning your color palette, adding a new page with image carousels, building a ScrollStory section---become conversations. You describe what you want. The AI proposes changes. You look at the result and decide: yes, no, or try again. You stay in the editorial role; the AI handles the implementation.

## Why Xanthan works well with AI

Most websites are a tangle of files where changing one thing can break something else in an unpredictable way. Xanthan is structured differently:

- **Named design variables** like `--accent-primary` and `--spacing-md` mean the AI can change your site's color palette or spacing rhythm in one place and have it cascade consistently everywhere
- **Modular components** with documented parameters (image figures, alert boxes, carousels, navigation cards) mean the AI knows exactly what options are available and how to use them
- **Clear file organization** --- CSS in `assets/css/`, layouts in `_layouts/`, reusable pieces in `_includes/` --- means the AI knows where to make changes without guessing
- **YAML configuration** for navigation means restructuring your site's menu is a conversation, not a puzzle

In practice, this means prompts like *"give my site a warmer, more earthy feel"* or *"add a before/after image slider comparing these two photos"* produce working results---because the AI can see the design system and knows how to work within it.

## The range of what's possible

If you've never used AI for anything technical, start with something small: [Your First AI Edit](first-edit) walks through changing a color, swapping a font, and asking the AI to explain what it's doing. These are genuinely useful tasks, and they'll show you how the conversation works.

Once you've seen how it feels, the range opens up considerably:

- **Reshape the feel of your site** --- change the entire color palette, switch from sans-serif to serif, adjust spacing and rhythm
- **Add new pages and content** --- create a CV page, build a project gallery, set up a card-based directory
- **Work with components** --- add image carousels, before/after sliders, pull quotes, alert boxes, audio players
- **Build ScrollStory sections** --- create scrolling narratives with background images, side-scrolling text panels, parallax effects
- **Understand and fix things** --- ask the AI to explain any piece of code, diagnose why something looks wrong, suggest alternatives

See [Building with AI](prompts) for specific examples across all of these.

## Setting up

You'll need a local development environment and an AI assistant:

1. **Set up local editing** --- follow the [Editing Workflows](../editing/) guide to get VS Code and your project running locally
2. **Install an AI assistant** in VS Code:
   - **GitHub Copilot** --- free for students and educators ([apply here](https://education.github.com/))
   - **Continue** --- free and open source ([install from VS Code extensions](https://marketplace.visualstudio.com/items?itemName=Continue.continue))
   - **Cursor** --- AI-first editor based on VS Code ([download](https://cursor.sh))
3. **Preview locally** --- [previewing locally](../editing/previewing-locally) lets you see changes instantly rather than waiting for GitHub to rebuild

## Giving AI context about your project

AI assistants work better when they understand what they're working with. The first time you use an AI assistant with your Xanthan site, give it some context:

> *"I'm working on a Jekyll site built with the Xanthan framework. The design system uses CSS custom properties defined in assets/css/base.css. Components are in _includes/ and are used with Liquid include tags. Navigation is configured in _data/nav-top.yml."*

You only need to do this once per conversation. After that, the AI will make suggestions that fit Xanthan's patterns rather than generic web development advice.

For even better results, you can paste a section of the [Component Library](../reference/component-library) or [Pages & Front Matter](../reference/pages-and-front-matter) reference into the conversation when asking about those topics.

## You're the editor

This is worth saying plainly: using AI to build your site doesn't mean the AI is making decisions for you. You describe what you want. The AI translates that into code. You look at the result and judge whether it's right. If it's not, you say what's wrong and the AI tries again.

This is the same relationship an author has with a typesetter, or a director has with a camera operator. The technical skill is real, but the vision is yours. The AI can write CSS; it can't tell you whether your site should feel warm or clinical, whether your images should be large and dramatic or small and documentary. Those are your calls.

## Privacy note

When using AI assistants, your code is sent to the AI service for processing. Don't include sensitive information (passwords, API keys) in files where you're using AI assistance. Most educational licenses and free tiers are appropriate for academic and personal sites.

## Next steps

- **New to AI-assisted editing?** Start with [Your First AI Edit](first-edit)
- **Ready for more?** Browse [Building with AI](prompts) for ideas organized by what you're trying to accomplish
