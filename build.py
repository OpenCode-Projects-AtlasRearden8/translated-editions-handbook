#!/usr/bin/env python3
"""Build the Translated Editions Handbook static site from docs/.

Stdlib only. Reads every .md file in docs/, renders it to HTML with a
minimal Markdown subset (headings, paragraphs, bold/italic/code, links,
lists, tables, blockquotes, fenced code blocks), and writes the pages
plus a generated index into site/ (or another output directory).

Usage:
    python3 build.py              # build into ./site
    python3 build.py /tmp/out     # build into another directory
"""

from __future__ import annotations

import html
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
ASSETS = ROOT / "assets"
DEFAULT_OUT = ROOT / "site"

BOOK_TITLE = "Selling Translated Editions"
BOOK_SUB = "A Handbook for Authors"
BYLINE = "by Dylan Asdale · Asdale Dynamics, LLC"

CHAPTER_META = [
    ("00-introduction.md", "Why translated editions, what's covered, and the three myths worth killing first."),
    ("01-choosing-target-languages.md", "A six-factor scoring sheet to pick a language you can actually reach — not just the biggest one."),
    ("02-rights-in-plain-english.md", "Who may translate what. Four author situations, AI-specific rights notes, and a rights memo you can adapt."),
    ("03-budgeting-ai-plus-human-review.md", "Honest 2026 price ranges: where every dollar goes and the cheapest version that still protects your name."),
    ("04-the-workflow-draft-to-final.md", "The week-by-week operating procedure, from frozen source file to live listing."),
    ("05-bilingual-qa.md", "How to check a translation you can't read: structural passes, glossary compliance, one independent native check."),
    ("06-covers-subtitles-and-re-layout.md", "Covers, subtitle transcreation, typographic conventions, page-count math, and fonts for new scripts."),
    ("07-marketing-to-readers-abroad.md", "Keywords in-language, foreign review velocity, per-market channels, and pricing by market."),
    ("08-going-live-staying-live.md", "Publish-day checklist, the first 48 hours, royalty bands, and a maintenance cadence that keeps editions alive."),
    ("09-checklists-and-templates.md", "Copy-paste templates: budget worksheet, translator agreement, terminology sheet, QA log, rights memo, launch sprint."),
]

FOOTER = """<footer>
  <div class="wrap">
    <p>Selling Translated Editions · A Handbook for Authors · by Dylan Asdale</p>
    <p>Published by <strong>Asdale Dynamics, LLC</strong> · Released under the MIT License ·
       Copyright (c) 2026 Asdale Dynamics, LLC</p>
    <p class="fine">Educational material only — not legal advice. Built as a static site; no trackers, no data collection.</p>
  </div>
</footer>
"""


# ---------------------------------------------------------------- helpers

def strip_md(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    return re.sub(r"[*_`]", "", text)


def doc_title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def inline(text: str) -> str:
    """Inline formatting: code spans first, then links, then bold/italic."""
    protected: list[str] = []

    def protect_code(m: re.Match) -> str:
        protected.append(m.group(1))
        return f"\x00{len(protected) - 1}\x00"

    text = re.sub(r"`([^`]+)`", protect_code, text)
    text = html.escape(text, quote=False)

    def link(m: re.Match) -> str:
        label, target = m.group(1), m.group(2)
        if target.startswith(("http://", "https://", "mailto:")):
            href = html.escape(target, quote=True)
            return f'<a href="{href}" rel="noopener">{label}</a>'
        target = re.sub(r"\.md(?=#|$)", ".html", target)
        return f'<a href="{html.escape(target, quote=True)}">{label}</a>'

    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<![*\w])\*([^*\n]+)\*(?![*\w])", r"<em>\1</em>", text)
    # stray single asterisks left unmatched (shouldn't happen in our docs) -> literal

    for idx, content in enumerate(protected):
        text = text.replace(f"\x00{idx}\x00", "<code>" + html.escape(content) + "</code>")
    return text


def slug_heading(text: str, used: dict[str, int]) -> str:
    base = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-") or "heading"
    base = re.sub(r"-+", "-", base)
    n = used.get(base, 0)
    used[base] = n + 1
    return base if n == 0 else f"{base}-{n}"


def md_to_html(md_text: str) -> str:
    """Render our Markdown subset to an HTML fragment."""
    lines = md_text.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    used: dict[str, int] = {}

    state = {"code": False}

    def header(level: int, text: str) -> str:
        plain = strip_md(text)
        return (
            f'<h{level} id="{slug_heading(plain, used)}">{inline(text)}</h{level}>'
        )

    para: list[str] = []
    code_lines: list[str] = []

    def flush_para() -> None:
        nonlocal para
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para = []

    def flush_list(items: list[str], ordered: bool) -> None:
        if not items:
            return
        tag = "ol" if ordered else "ul"
        out.append(f"<{tag}>")
        for item in items:
            if ordered:
                item = re.sub(r"^\s*\d+\.\s+", "", item)
            else:
                item = re.sub(r"^\s*[-*]\s+", "", item)
            out.append("<li>" + inline(item.strip()) + "</li>")
        out.append(f"</{tag}>")

    def flush_quote(qlines: list[str]) -> None:
        if not qlines:
            return
        inner = [inline(q.strip()) for q in qlines]
        out.append("<blockquote><p>" + "</p><p>".join(inner) + "</p></blockquote>")

    i = 0
    n_lines = len(lines)
    while i < n_lines:
        line = lines[i]

        # fenced code blocks
        if line.lstrip().startswith("```"):
            flush_para()
            if not state["code"]:
                state["code"] = True
                code_lines = []
            else:
                state["code"] = False
                out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
            i += 1
            continue
        if state["code"]:
            code_lines.append(line)
            i += 1
            continue

        # headings
        m = re.match(r"^(#{1,6})\s+(.+?)\s*#*\s*$", line)
        if m:
            flush_para()
            out.append(header(len(m.group(1)), m.group(2)))
            i += 1
            continue

        # horizontal rule
        if re.match(r"^\s*(---+|\*\*\*+|___+)\s*$", line):
            flush_para()
            out.append("<hr>")
            i += 1
            continue

        # table (row followed by a separator row)
        if (line.lstrip().startswith("|") and i + 1 < n_lines
                and re.match(r"^\s*\|[\s:\-|]*\-\-[\s:\-|]*$", lines[i + 1])):
            flush_para()
            header_cells = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2
            rows = []
            while i < n_lines and lines[i].lstrip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            out.append("<table><thead><tr>"
                       + "".join(f"<th>{inline(c)}</th>" for c in header_cells)
                       + "</tr></thead>")
            out.append("<tbody>")
            for r in rows:
                cells = r + [""] * (len(header_cells) - len(r))
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in cells[: len(header_cells)]) + "</tr>")
            out.append("</tbody></table>")
            continue

        # blockquote
        if line.lstrip().startswith(">"):
            flush_para()
            qlines = []
            while i < n_lines and lines[i].lstrip().startswith(">"):
                qlines.append(lines[i].lstrip()[1:].lstrip())
                i += 1
            flush_quote(qlines)
            continue

        # lists
        if re.match(r"^\s*[-*]\s+", line):
            flush_para()
            items = []
            while i < n_lines and re.match(r"^\s*[-*]\s+", lines[i]):
                items.append(lines[i])
                i += 1
            flush_list(items, ordered=False)
            continue
        if re.match(r"^\s*\d+\.\s", line):
            flush_para()
            items = []
            while i < n_lines and re.match(r"^\s*\d+\.\s", lines[i]):
                items.append(lines[i])
                i += 1
            flush_list(items, ordered=True)
            continue

        # blank line
        if not line.strip():
            flush_para()
            i += 1
            continue

        para.append(line.strip())
        i += 1

    flush_para()
    if state["code"]:  # unterminated fence
        out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
    return "\n".join(out)


# ---------------------------------------------------------------- page shell

NAV_ITEMS = [
    ("Introduction", "00-introduction.html"),
    ("Languages", "01-choosing-target-languages.html"),
    ("Rights", "02-rights-in-plain-english.html"),
    ("Budget", "03-budgeting-ai-plus-human-review.html"),
    ("Workflow", "04-the-workflow-draft-to-final.html"),
    ("QA", "05-bilingual-qa.html"),
    ("Layout", "06-covers-subtitles-and-re-layout.html"),
    ("Marketing", "07-marketing-to-readers-abroad.html"),
    ("Going Live", "08-going-live-staying-live.html"),
    ("Templates", "09-checklists-and-templates.html"),
]

PAGE_TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · {book}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="masthead">
  <div class="wrap">
    <a class="brand" href="index.html">
      <span class="brand-book">{book}</span>
      <span class="brand-sub">{sub}</span>
    </a>
    <p class="byline">{byline}</p>
  </div>
</header>
<nav class="chapter-nav" aria-label="Chapters">
  <div class="wrap">
    {nav_links}
  </div>
</nav>
<main class="wrap">
<article class="chapter">
{content}
</article>
<nav class="pager">
  {prev}
  {next}
  <a class="toc-link" href="index.html">Contents</a>
</nav>
</main>
{footer}
</body>
</html>
"""

INDEX_TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{book} · {sub}</title>
<meta name="description" content="A plain-English handbook for independent authors selling translated editions: languages, budgets, bilingual QA, rights, and marketing abroad.">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="masthead masthead-home">
  <div class="wrap">
    <p class="kicker">A Handbook for Authors</p>
    <h1>{book}</h1>
    <p class="lede">How to take your book into other languages: choosing where to go, paying for AI-assisted translation with real human review, checking the result like a pro, protecting your rights, and finding readers who don't speak your language.</p>
    <p class="byline">{byline}</p>
    <p class="cta"><a class="button" href="00-introduction.html">Start reading — Introduction →</a></p>
  </div>
</header>
<main class="wrap">
<section class="toc-grid" aria-label="Table of contents">
{toc}
</section>
<section class="note">
  <h2>What you'll learn</h2>
  <ul class="cols">
    <li><strong>Pick the right market.</strong> Score languages on niche demand, competition, reachability, and reviewer availability — not raw size.</li>
    <li><strong>Own the process.</strong> Freeze your source, brief the AI properly, and hire one professional native reviewer per language.</li>
    <li><strong>Check what you can't read.</strong> Bilingual QA: mechanical passes you run tonight, plus an independent native sample check that catches tone failures.</li>
    <li><strong>Look native.</strong> Cover text, subtitles, punctuation conventions, page counts, and fonts that make the book read as local.</li>
    <li><strong>Protect yourself.</strong> Plain-English rights: who may translate, what to get in writing, and what "free" platform offers really cost.</li>
    <li><strong>Get read abroad.</strong> In-language keywords, review velocity, per-market channels, and price bands — the boring money details.</li>
  </ul>
  <p class="fine">This handbook stays out of two neighbor subjects on purpose: everyday personal AI translation, and general wide-store distribution. See the README for how the three handbooks divide territory.</p>
</section>
</main>
{footer}
</body>
</html>
"""


def render_nav(current: str | None) -> str:
    links = []
    for label, href in NAV_ITEMS:
        if href == current:
            links.append(f'<a href="{href}" aria-current="page">{label}</a>')
        else:
            links.append(f'<a href="{href}">{label}</a>')
    return "\n    ".join(links)


def short_title(t: str) -> str:
    t = strip_md(t)
    if t.startswith("Chapter ") and " — " in t:
        t = t.split(" — ", 1)[1]
    return t


def chapter_kicker(i: int) -> str:
    return f'<p class="chapter-kicker">Chapter {i}</p>'


def render_index() -> str:
    toc_items = []
    for i, (fname, desc) in enumerate(CHAPTER_META):
        title = short_title(doc_title(DOCS / fname))
        toc_items.append(
            f'<a class="toc-card" href="{fname.replace(".md", ".html")}">'
            f'<span class="toc-num">{i:02d}</span>'
            f"<h3>{html.escape(title)}</h3>"
            f"<p>{html.escape(desc)}</p></a>"
        )
    return INDEX_TMPL.format(
        book=BOOK_TITLE,
        sub=BOOK_SUB,
        byline=BYLINE,
        toc="\n".join(toc_items),
        footer=FOOTER,
    )


def build(out: Path = DEFAULT_OUT) -> list[Path]:
    out.mkdir(parents=True, exist_ok=True)
    (out / "style.css").write_text((ASSETS / "style.css").read_text(encoding="utf-8"), encoding="utf-8")
    index_path = out / "index.html"
    index_path.write_text(render_index(), encoding="utf-8")
    written: list[Path] = [index_path, out / "style.css"]

    md_files = sorted(DOCS.glob("*.md"))
    for idx, md_file in enumerate(md_files):
        text = md_file.read_text(encoding="utf-8")
        body = md_to_html(text)

        lines = body.split("\n")
        if lines and lines[0].startswith("<h1"):
            display = short_title(doc_title(md_file))
            lines[0] = f'<h1 id="top">{inline(display)}</h1>'
        if idx > 0:
            lines.insert(1, chapter_kicker(idx))
        body = "\n".join(lines)

        title = short_title(doc_title(md_file))
        desc = next((m[1] for m in CHAPTER_META if m[0] == md_file.name), title)
        current = md_file.name.replace(".md", ".html")
        prev_cell = nxt_cell = '<span class="pager-ghost"></span>'
        if idx > 0:
            prev_f = md_files[idx - 1]
            prev_cell = f'<a href="{prev_f.name.replace(".md", ".html")}">← {html.escape(short_title(doc_title(prev_f)))}</a>'
        if idx + 1 < len(md_files):
            nxt_f = md_files[idx + 1]
            nxt_cell = f'<a href="{nxt_f.name.replace(".md", ".html")}">{html.escape(short_title(doc_title(nxt_f)))} →</a>'

        page = PAGE_TMPL.format(
            title=title,
            book=BOOK_TITLE,
            sub=BOOK_SUB,
            byline=BYLINE,
            desc=html.escape(desc, quote=True),
            nav_links=render_nav(current),
            prev=prev_cell,
            next=nxt_cell,
            content=body,
            footer=FOOTER,
        )
        p = out / current
        p.write_text(page, encoding="utf-8")
        written.append(p)
    return written


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT
    files = build(target)
    print(f"built {len(files)} files into {target}")
