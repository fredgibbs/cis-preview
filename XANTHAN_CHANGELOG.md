# Changelog

All notable changes to Xanthan will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-01-04

### Added
- **Documentation auto-sync to templates**: All Xanthan documentation now automatically syncs to template repositories, ensuring docs always match code version
- **Centralized `/docs/` folder**: All documentation organized in clean `/docs/` structure (getting-started, content-design, navigation, scrollstories)
- **Documentation landing page**: New `/docs/index.md` provides organized access to all documentation sections
- **Template sync workflow**: Automated GitHub Actions workflow syncs code, docs, and examples from main Xanthan repo to all template repositories
- **Profile sidebar CSS**: New `sidebar.css` for portfolio-template with proper image sizing and responsive design

### Changed
- **ScrollStory examples location**: Moved from `/scrollstories/examples/` to `/scrollstories/` for cleaner structure
- **Documentation paths**: All internal links updated to use `/docs/` prefix for consistency
- **About and FAQs location**: Kept at root level (not synced to templates) as they're specific to main Xanthan site
- **Navigation structure**: Updated `top-nav.yml` to reflect new `/docs/` paths

### Fixed
- Profile sidebar image sizing issue in portfolio-template
- All internal documentation links updated to new structure

## [1.0.0] - 2026-01-01

- **Added**: First major release of Xanthan! Beginner-friendly web templates and extensive documentation for academics, educators, and students to build professional websites and collaborative projects with GitHub Pages.

- Start here: https://xanthan-web.github.io/


## Future Releases

Starting with 1.1.0, this changelog will document:
- **Added** for new features
- **Changed** for changes in existing functionality
- **Deprecated** for soon-to-be removed features
- **Removed** for now removed features
- **Fixed** for any bug fixes
- **Security** for vulnerability patches

[1.0.0]: https://github.com/xanthan-web/xanthan-web.github.io/releases/tag/v1.0.0
