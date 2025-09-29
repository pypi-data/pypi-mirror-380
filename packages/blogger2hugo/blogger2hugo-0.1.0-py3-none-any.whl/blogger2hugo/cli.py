#!/usr/bin/env python3
"""
Blogger Atom → Hugo Markdown (configurable slugs, link sanitization, flat files).
"""

import argparse, pathlib, re, sys, xml.etree.ElementTree as ET
from datetime import datetime, timezone
from slugify import slugify
import html2text
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "app": "http://www.w3.org/2007/app",
}
KIND_SCHEME = "http://schemas.google.com/g/2005#kind"

def parse_args(argv=None):
    p = argparse.ArgumentParser(description="Blogger Atom → Hugo Markdown")
    p.add_argument("xml", help="Path to Blogger export .xml")
    p.add_argument("--out", default="content/blog", help="Output directory for posts (Hugo section)")
    p.add_argument("--pages-out", default="content/page", help="Output directory for pages")
    p.add_argument("--drafts", action="store_true", help="Include drafts (default: skip)")
    p.add_argument(
        "--slug-mode",
        choices=["link", "title", "id", "date-title", "id-title"],
        default="date-title",
        help="How to build the slug (default: date-title)",
    )
    p.add_argument(
        "--slugify",
        choices=["ascii", "unicode", "none"],
        default="ascii",
        help="Slugification style for text-based slugs (default: ascii)",
    )
    p.add_argument(
        "--links",
        default="notracking,nohash,unwrap-images",
        help="Comma flags: keep|text|notracking|nohash|unwrap-images (default: notracking,nohash,unwrap-images)",
    )
    p.add_argument(
        "--flat",
        action="store_true",
        help="Write posts as slug.md instead of slug/index.md",
    )
    return p.parse_args(argv)

def get_text(elem, path):
    x = elem.find(path, NS)
    return (x.text or "").strip() if x is not None else ""

def iso(s):
    try:
        dt = datetime.fromisoformat((s or "").replace("Z", "+00:00"))
        return dt.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
    except Exception:
        return s or ""

def extract_kind(entry):
    for c in entry.findall("atom:category", NS):
        term = c.get("term", "") or ""
        scheme = c.get("scheme", "") or ""
        if scheme == KIND_SCHEME:
            if term.endswith("#post"):  return "post"
            if term.endswith("#page"):  return "page"
    return "post"

def extract_labels(entry):
    labels, seen, out = [], set(), []
    for c in entry.findall("atom:category", NS):
        scheme = c.get("scheme") or ""
        term = c.get("term", "") or ""
        if scheme != KIND_SCHEME and term:
            labels.append(term)
    for l in labels:
        if l not in seen:
            out.append(l); seen.add(l)
    return out

def extract_link_slug(entry):
    # Prefer <link rel="alternate" href=".../YYYY/MM/slug.html">
    for l in entry.findall("atom:link", NS):
        if (l.get("rel") == "alternate") and l.get("href"):
            href = l.get("href")
            m = re.search(r"/([^/]+?)(?:\.html)?/?$", href)
            if m:
                return m.group(1)
    return None

def extract_post_id(entry):
    id_text = get_text(entry, "atom:id")
    m = re.search(r"post-(\d+)", id_text)
    return m.group(1) if m else None

def slugify_text(text: str, style: str) -> str:
    text = (text or "").strip()
    if not text:
        return ""
    if style == "ascii":
        return slugify(text)  # transliterate to ASCII
    if style == "unicode":
        return slugify(text, allow_unicode=True)  # keep original script; normalize separators
    # style == "none": minimal cleanup only
    cleaned = re.sub(r"[\\/]+", "-", text)
    cleaned = re.sub(r"\s+", "-", cleaned)
    cleaned = re.sub(r"-{2,}", "-", cleaned).strip("-")
    return cleaned

def html_to_md(html, link_flags):
    # Sanitize HTML first, then convert to Markdown
    soup = BeautifulSoup(html or "", "html.parser")
    flags = {f.strip().lower() for f in (link_flags or "").split(",") if f.strip()}

    # Remove common Blogger "more" markers (HTML comments sometimes become text nodes)
    for c in list(soup.descendants):
        if isinstance(c, str) and "more" in c.lower():
            if "<!--" in c or "-->" in c:
                try:
                    c.extract()
                except Exception:
                    pass

    for a in list(soup.find_all("a")):
        # unwrap image links
        if "unwrap-images" in flags and a.find("img"):
            img = a.find("img")
            a.replace_with(img)
            continue

        href = a.get("href")

        # convert all links to plain text
        if "text" in flags:
            a.replace_with(a.get_text(strip=False))
            continue

        # drop pure hash or javascript links
        if "nohash" in flags:
            if not href or href.startswith("#") or href.lower().startswith("javascript:"):
                a.replace_with(a.get_text(strip=False))
                continue

        # strip tracking params
        if "notracking" in flags and href:
            try:
                u = urlparse(href)
                qs = parse_qsl(u.query, keep_blank_values=True)
                qs = [(k, v) for (k, v) in qs if not (
                    k.lower().startswith("utm_")
                    or k.lower() in {"gclid", "fbclid", "spref", "zx", "m"}
                )]
                new_q = urlencode(qs, doseq=True)
                a["href"] = urlunparse((u.scheme, u.netloc, u.path, u.params, new_q, ""))  # drop fragment
            except Exception:
                pass

    # Convert HTML → Markdown
    h = html2text.HTML2Text()
    h.ignore_links = False  # link policy handled above
    h.body_width = 0
    h.ignore_images = False
    h.protect_links = True
    h.single_line_break = True
    md = h.handle(str(soup)).strip() + "\n"

    # Clean common Blogger artifacts in MD
    md = re.sub(r"\(\s*#more\s*\)", "", md, flags=re.IGNORECASE)
    md = re.sub(r"\[Read more\]\(\)", "", md, flags=re.IGNORECASE)
    return md

def build_slug(entry, dt, mode, slugify_style: str):
    title = get_text(entry, "atom:title") or ""
    link_slug_raw = extract_link_slug(entry) or ""
    post_id = extract_post_id(entry) or ""
    date_prefix = dt.strftime("%Y%m%d") if dt else ""

    # Apply chosen slugification to human strings
    title_slug = slugify_text(title, slugify_style)
    link_slug = slugify_text(link_slug_raw, slugify_style)

    if mode == "link":
        base = link_slug or title_slug or post_id
    elif mode == "title":
        base = title_slug or link_slug or post_id
    elif mode == "id":
        base = post_id or link_slug or title_slug
    elif mode == "date-title":
        base = f"{date_prefix}-{(title_slug or link_slug or post_id)}".strip("-")
    elif mode == "id-title":
        base = f"{post_id}-{(title_slug or link_slug)}".strip("-")
    else:
        base = title_slug or link_slug or post_id

    if not base:
        base = date_prefix or "post"
    return base

def write_md(base_dir: pathlib.Path, entry, kind: str, *, slug_mode: str, slugify_style: str, link_flags: str, flat: bool):
    title = get_text(entry, "atom:title")
    content_html = get_text(entry, "atom:content") or get_text(entry, "atom:summary")
    published = iso(get_text(entry, "atom:published"))
    updated = iso(get_text(entry, "atom:updated"))
    tags = extract_labels(entry)

    dt = None
    try:
        dt = datetime.fromisoformat((published or "").replace("Z", "+00:00")).astimezone(timezone.utc)
    except Exception:
        pass

    slug = build_slug(entry, dt, slug_mode, slugify_style)

    # Destination path
    if dt:
        year = f"{dt.year:04d}"
        month = f"{dt.month:02d}"
        dir_date = base_dir / year / month
    else:
        dir_date = base_dir

    dir_date.mkdir(parents=True, exist_ok=True)

    if flat:
        out_file = dir_date / f"{slug}.md"
    else:
        post_dir = dir_date / slug
        post_dir.mkdir(parents=True, exist_ok=True)
        out_file = post_dir / "index.md"

    # Front matter (YAML)
    fm_title = (title or slug).replace('"', '\\"')
    front = [
        "---",
        f'title: "{fm_title}"' if fm_title else "title:",
        f'date: "{published}"' if published else "date:",
        f'lastmod: "{updated}"' if updated else "lastmod:",
        "draft: false",
        f'slug: "{slug}"' if slug else "slug:",
    ]

    if tags:
        front.append("tags:")
        for t in tags:
            safe_t = (t or "").replace('"', '\\"')
            front.append(f'  - "{safe_t}"')
    else:
        front.append("tags: []")

    front.append("---\n")

    md = html_to_md(content_html, link_flags=link_flags)
    out_file.write_text("\n".join(front) + md, encoding="utf-8")
    return out_file

def run(xml_path: pathlib.Path, out_posts: pathlib.Path, out_pages: pathlib.Path, *, drafts: bool, slug_mode: str, slugify_style: str, link_flags: str, flat: bool) -> list[pathlib.Path]:
    out_posts.mkdir(parents=True, exist_ok=True)
    out_pages.mkdir(parents=True, exist_ok=True)

    tree = ET.parse(xml_path)
    root = tree.getroot()

    made: list[pathlib.Path] = []
    for entry in root.findall("atom:entry", NS):
        kind = extract_kind(entry)

        # Skip drafts by default
        if not drafts:
            ctrl = entry.find("app:control", NS)
            if ctrl is not None:
                d = ctrl.find("app:draft", NS)
                if (d is not None) and (d.text or "").lower() == "yes":
                    continue

        base = out_pages if kind == "page" else out_posts
        path = write_md(
            base,
            entry,
            kind,
            slug_mode=slug_mode,
            slugify_style=slugify_style,
            link_flags=link_flags,
            flat=flat,
        )
        made.append(path)

    return made

def main(argv=None):
    args = parse_args(argv)
    xml_path = pathlib.Path(args.xml)
    out_posts = pathlib.Path(args.out)
    out_pages = pathlib.Path(args.pages_out)

    made = run(
        xml_path=xml_path,
        out_posts=out_posts,
        out_pages=out_pages,
        drafts=args.drafts,
        slug_mode=args.slug_mode,
        slugify_style=args.slugify,
        link_flags=args.links,
        flat=args.flat,
    )

    print(f"Wrote {len(made)} Markdown files")
    for p in made:
        print(p)

if __name__ == "__main__":
    sys.exit(main())
