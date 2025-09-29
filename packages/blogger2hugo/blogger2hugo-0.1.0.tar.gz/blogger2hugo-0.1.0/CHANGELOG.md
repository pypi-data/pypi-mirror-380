# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- (Planned) Optional asset downloader for images to local `static/` folder.
- (Planned) Config file support (`pyproject.toml` table).

### Changed
- (Planned) Better handling of `<!-- more -->` markers in edge cases.

### Fixed
- (Planned) Extra whitespace around converted links in some HTML fragments.

---

## [0.1.0] - 2025-09-28
### Added
- CLI `blogger2hugo` to convert Blogger Atom export to Hugo Markdown.
- **Slug control** via `--slug-mode` (`link | title | id | date-title | id-title`).
- **Slugify style** via `--slugify` (`ascii | unicode | none`) to avoid unwanted transliteration.
- **Link sanitization** via `--links`:
  - `notracking` strips `utm_*`, `gclid`, `fbclid`, `spref`, `zx`, `m`
  - `nohash` drops hash-only and `javascript:` links
  - `unwrap-images` removes lightbox `<a>` wrappers around `<img>`
  - `text` converts links to plain text
- **Flat output option** `--flat` (`slug.md`) or nested (`slug/index.md`).
- Drafts skipped by default; include with `--drafts`.
- Separate output roots for posts (`--out`) and pages (`--pages-out`).
- YAML front matter with `title`, `date`, `lastmod`, `tags`, `slug`.

[0.1.0]: https://pypi.org/project/blogger2hugo/
