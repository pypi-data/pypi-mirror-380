# Blogger → Hugo Markdown Converter

Convert a Blogger Atom export (`blogger.xml`) into [Hugo](https://gohugo.io/) Markdown files.  
Supports configurable slugs, link sanitization, and choice between flat files (`slug.md`) or nested (`slug/index.md`).

---

## Features

- **Slug control**:
  - `--slug-mode link | title | id | date-title | id-title`
  - `--slugify ascii | unicode | none`
- **Link sanitization**:
  - Strip tracking params (`utm_*`, `gclid`, etc.)
  - Drop hash-only links
  - Optionally unwrap image lightbox links
  - Or strip all links to plain text
- **Flat file option**:  
  Use `--flat` to write `post.md` instead of `post/index.md`.
- **Draft handling**:  
  Drafts skipped by default; include with `--drafts`.
- **Pages vs posts**:  
  Blogger "pages" exported separately (`--pages-out`).

---

## Installation

Requires Python 3.8+.

```bash
pip install html2text python-slugify beautifulsoup4
````

Save the script as `blogger2hugo`.

---

## Usage

Export your blog from Blogger:
**Settings → Back up content → Download** → `blogger.xml`.

Convert:

```bash
python blogger2hugo blogger.xml --out content/blog
```

### Common options

* **Slug mode**

  ```bash
  --slug-mode date-title   # YYYYMMDD-my-title
  --slug-mode link         # from Blogger’s canonical link
  --slug-mode id           # numeric post ID
  --slug-mode title        # slugified title
  --slug-mode id-title     # <id>-<title>
  ```

* **Slugify style**

  ```bash
  --slugify ascii     # transliterate to ASCII (default)
  --slugify unicode   # keep original script (e.g. فارسی titles)
  --slugify none      # minimal cleanup only
  ```

* **Flat files**

  ```bash
  --flat
  # results in content/blog/2023/01/my-post.md
  # instead of content/blog/2023/01/my-post/index.md
  ```

* **Link sanitization**

  ```bash
  --links keep
  --links text
  --links notracking,nohash,unwrap-images   # default
  ```

* **Pages output**

  ```bash
  --pages-out content/page
  ```

---

## Examples

Keep Unicode slugs, clean links, and flat files:

```bash
python blogger2hugo blogger.xml \
  --out content/blog \
  --slug-mode date-title \
  --slugify unicode \
  --links notracking,nohash,unwrap-images \
  --flat
```

Use Blogger IDs as slugs, keep original link structure:

```bash
python blogger2hugo blogger.xml \
  --out content/blog \
  --slug-mode id
```

Include drafts:

```bash
python blogger2hugo blogger.xml --out content/blog --drafts
```

---

## Output structure

Example with `--flat --slug-mode date-title --slugify unicode`:

```
content/
└── blog/
    └── 2023/
        └── 01/
            ├── 20230120-hello-world.md
            └── ...
```

Each Markdown file contains YAML front matter:

```yaml
---
title: "hello-wrold
date: "2023-01-10T08:30:00Z"
lastmod: "2023-01-10T08:45:00Z"
draft: false
tags:
  - "Example"
slug: "20230110-hello-wrold"
---
```

Followed by the body in Markdown.

---

## Notes

* Images are left as-is; for local copies, run a separate fetcher.
* Blogger “read more” markers are removed.
* Pages and posts are separated (`--out`, `--pages-out`).
* Compatible with Hugo extended.

---