#!/usr/bin/env python3
"""Tests for the Translated Editions Handbook build.

Run with:  python3 -m unittest discover -s tests -v  (from the repo root)

Covers: docs integrity, markdown->html rendering, internal link
resolution, site completeness, README/LICENSE/credit requirements, and
the no-secrets/no-personal-data rule.
"""

from __future__ import annotations

import os
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import build as builder  # noqa: E402

DOCS = ROOT / "docs"
CHAPTER_NAMES = [m[0] for m in builder.CHAPTER_META]


class TestDocs(unittest.TestCase):
    """Source markdown integrity."""

    def test_all_chapter_files_exist(self):
        for name in CHAPTER_NAMES:
            self.assertTrue((DOCS / name).is_file(), f"missing docs/{name}")

    def test_no_unexpected_docs(self):
        found = sorted(p.name for p in DOCS.glob("*.md"))
        self.assertEqual(found, sorted(CHAPTER_NAMES))

    def test_each_chapter_has_h1(self):
        for name in CHAPTER_NAMES:
            with self.subTest(name=name):
                text = (DOCS / name).read_text(encoding="utf-8")
                self.assertTrue(text.startswith("# "), f"{name} lacks a level-1 heading")

    def test_each_chapter_is_substantive(self):
        for name in CHAPTER_NAMES:
            with self.subTest(name=name):
                text = (DOCS / name).read_text(encoding="utf-8")
                self.assertGreaterEqual(len(text), 3000, f"{name} is too short to be substantive")

    def test_internal_md_links_resolve(self):
        for name in CHAPTER_NAMES:
            text = (DOCS / name).read_text(encoding="utf-8")
            for target in re.findall(r"\]\(([^)#]+\.md)\)", text):
                with self.subTest(src=name, link=target):
                    self.assertTrue((DOCS / target).is_file(), f"{name} -> {target} broken")

    def test_every_non_intro_chapter_links_back_to_a_neighbor(self):
        for name in CHAPTER_NAMES[1:]:
            text = (DOCS / name).read_text(encoding="utf-8")
            self.assertIn(".md)", text, f"{name} has no cross-chapter links")

    def test_no_machine_placeholder_junk(self):
        banned = ["FIXME", "占位", "[anything)))", "[anything])))", "\x00"]
        for name in CHAPTER_NAMES:
            text = (DOCS / name).read_text(encoding="utf-8")
            for b in banned:
                self.assertNotIn(b, text, f"{name} contains placeholder {b!r}")

    def test_no_cjk_stray_characters(self):
        # a stray Chinese character slipped into an English sentence once;
        # the only CJK allowed are the intentional Japanese examples used
        # inside the text (date formats, subtitle-structure illustration)
        allowed = ["5月5日", "〜のための、〜がわかる本"]
        for name in CHAPTER_NAMES:
            text = (DOCS / name).read_text(encoding="utf-8")
            stripped = text
            for a in allowed:
                stripped = stripped.replace(a, "")
            stray = re.findall(r"[\u4e00-\u9fff]", stripped)
            self.assertEqual([], stray, f"{name} contains CJK characters: {stray}")

    def test_no家里_secrets_keys_or_personal_data(self):
        patterns = [
            r"AKIA[0-9A-Z]{16}",                # AWS access key id
            r"api[_-]?key\s*[:=]\s*['\"][A-Za-z0-9]{16,}",
            r"-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----",
            r"github_pat_[A-Za-z0-9_]{20,}",
            r"ghp_[A-Za-z0-9]{20,}",
            r"sk-[A-Za-z0-9]{20,}",             # openai-style secret key
            r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b",  # bare emails
            r"\b(?:\d[ -]?){13,16}\b",           # long card-like numbers
        ]
        targets = list(DOCS.glob("*.md")) + [ROOT / "README.md"]
        for path in targets:
            text = path.read_text(encoding="utf-8")
            for pat in patterns:
                with self.subTest(file=path.name, pattern=pat):
                    self.assertIsNone(re.search(pat, text), f"{path.name} matches {pat!r}")


class TestRender(unittest.TestCase):
    """Markdown rendering primitives."""

    M2H = staticmethod(builder.md_to_html)
    INLINE = staticmethod(builder.inline)

    def test_headings(self):
        html_text = self.M2H("## Section A")
        self.assertIn("<h2", html_text)
        self.assertIn('id="section-a"', html_text)

    def test_paragraph(self):
        self.assertEqual(self.M2H("Hello world."), "<p>Hello world.</p>")

    def test_bold(self):
        self.assertEqual(self.INLINE("**bold text**"), "<strong>bold text</strong>")

    def test_bold_with_nested_italic(self):
        self.assertEqual(self.INLINE("**Hold *planning* to sell.**"), "<strong>Hold <em>planning</em> to sell.</strong>")

    def test_italic(self):
        self.assertEqual(self.INLINE("*warm*"), "<em>warm</em>")

    def test_inline_code_protected_from_emphasis(self):
        self.assertEqual(self.INLINE("use `**bold**` tokens"), "use <code>**bold**</code> tokens")

    def test_internal_link_gets_html_extension(self):
        out = self.INLINE("[Rights](02-rights-in-plain-english.md)")
        self.assertIn('href="02-rights-in-plain-english.html"', out)

    def test_external_link_preserved_with_rel_noopener(self):
        out = self.INLINE("[Hub](https://dylanasdale.github.io)")
        self.assertIn('href="https://dylanasdale.github.io" rel="noopener"', out)

    def test_html_is_escaped_before_rendering(self):
        out = self.INLINE("tom & <jerry>")
        self.assertIn("&amp;", out)
        self.assertNotIn("<jerry>", out)

    def test_ul(self):
        out = self.M2H("- one\n- two")
        self.assertIn("<ul><li>", out.replace("\n", ""))
        self.assertIn("two</li></ul>", out.replace("\n", ""))

    def test_ol_preserves_order(self):
        out = self.M2H("1. Alpha\n2. Beta")
        self.assertIn("<li>Alpha</li>", out)
        self.assertIn("<li>Beta</li>", out)
        self.assertIn("<ol>", out)

    def test_table(self):
        out = self.M2H("| a | b |\n|---|---|\n| 1 | 2 |")
        self.assertIn("<table><thead><tr><th>a</th><th>b</th></tr></thead>", out)
        self.assertIn("<tr><td>1</td><td>2</td></tr>", out)

    def test_blockquote(self):
        out = self.M2H("> quoted line")
        self.assertIn("<blockquote><p>quoted line</p></blockquote>", out)

    def test_code_fence_escapes_and_preserves(self):
        out = self.M2H("```\n| a | not a table |\n<browsers>\n```")
        self.assertIn("<pre><code>", out)
        self.assertIn("| a | not a table |", out)
        self.assertIn("&lt;browsers&gt;", out)
        self.assertNotIn("<table", out)  # fence content is NOT re-parsed as a table

    def test_closed_fence_does_not_leak_state(self):
        out = self.M2H("```\nfence\n```\nAfter fence.")
        self.assertIn("<p>After fence.</p>", out)
        self.assertNotIn("<p><pre>", out)

    def test_empty_body_row_renders(self):
        out = self.M2H("| a | b |\n|---|---|\n| | |")
        self.assertIn("<td></td>", out)


class TestSite(unittest.TestCase):
    """Full build output integrity."""

    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory()
        cls.out = Path(cls._tmp.name) / "site"
        builder.build(cls.out)

        cls.expected = {name.replace(".md", ".html") for name in CHAPTER_NAMES}
        cls.expected |= {"index.html", "style.css"}
        cls.actual = {p.name for p in cls.out.glob("*.html")} | {p.name for p in cls.out.glob("*.css")}

    @classmethod
    def tearDownClass(cls):
        cls._tmp.cleanup()

    def test_expected_pages_created(self):
        self.assertEqual(self.actual, self.expected)

    def test_no_broken_internal_links(self):
        for page in self.out.glob("*.html"):
            text = page.read_text(encoding="utf-8")
            for href in re.findall(r'href="([^"#][^"]*?)"', text):
                self.assertTrue((self.out / href).is_file(), f"{page.name} -> {href} broken")

    def test_pages_link_the_full_chain(self):
        # each chapter links next / prev where relevant
        intro = (self.out / "00-introduction.html").read_text(encoding="utf-8")
        self.assertIn('href="01-choosing-target-languages.html"', intro)
        templates = (self.out / "09-checklists-and-templates.html").read_text(encoding="utf-8")
        self.assertIn('href="00-introduction.html"', templates)

    def test_nav_highlights_current_chapter(self):
        body = (self.out / "03-budgeting-ai-plus-human-review.html").read_text(encoding="utf-8")
        self.assertIn('href="03-budgeting-ai-plus-human-review.html" aria-current="page"', body)

    def test_every_page_carries_credit_and_license(self):
        for page in list(self.out.glob("*.html")):
            with self.subTest(page=page.name):
                text = page.read_text(encoding="utf-8")
                self.assertIn("Asdale Dynamics, LLC", text)
                self.assertIn("Copyright (c) 2026 Asdale Dynamics, LLC", text)
                self.assertIn("MIT License", text)

    def test_pages_declare_charset_and_viewport(self):
        for page in list(self.out.glob("*.html")):
            text = page.read_text(encoding="utf-8")
            self.assertIn('charset="utf-8"', text)
            self.assertIn("viewport", text)
            self.assertNotIn("<script", text, f"{page.name} unexpectedly contains scripts")

    def test_html_tag_balance(self):
        for page in self.out.glob("*.html"):
            text = page.read_text(encoding="utf-8")
            for tag in ("table", "thead", "tbody", "ul", "ol", "blockquote", "main", "footer"):
                self.assertEqual(text.count(f"<{tag}"), text.count(f"</{tag}>"),
                                 f"{page.name} unbalanced <{tag}>")

    def test_no_raw_mastered_marks_in_body(self):
        for page in self.out.glob("*.html"):
            body = page.read_text(encoding="utf-8").split("<main", 1)[-1]
            body = re.sub(r"<pre>.*?</pre>", "", body, flags=re.S)
            self.assertNotIn("** ", body, f"{page.name} leaks raw markdown")

    def test_style_sheet_copied(self):
        css = (self.out / "style.css").read_text(encoding="utf-8")
        self.assertIn("--accent", css)
        self.assertTrue(len(css) > 1000)

    def test_index_lists_all_chapters(self):
        index_html = (self.out / "index.html").read_text(encoding="utf-8")
        for name in CHAPTER_NAMES:
            self.assertIn(name.replace(".md", ".html"), index_html)


class TestRepoFiles(unittest.TestCase):
    def test_license_exists_with_exact_copyright(self):
        lic = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("Copyright (c) 2026 Asdale Dynamics, LLC", lic)
        self.assertIn("MIT License", lic)

    def test_readme_credits_llc_and_mentions_license(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("Asdale Dynamics, LLC", readme)
        self.assertIn("MIT License", readme)

    def test_site_footer_fmt_is_literal_copyright(self):
        self.assertIn("Copyright (c) 2026 Asdale Dynamics, LLC", builder.FOOTER)


if __name__ == "__main__":
    unittest.main()
