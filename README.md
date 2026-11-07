# Translated Editions Handbook

A beginner-friendly, plain-English manual for independent authors who want to sell **translated editions** of their books — how to choose target languages, budget AI-assisted translation with real human review, run bilingual QA, handle covers/subtitles/re-layout, protect your rights, and market to readers abroad.

Written in the same spirit as The Massive AI Manual: like a friend would explain it — plain English, step by step, never condescending.

## What's inside

- **`docs/`** — 10 chapters in Markdown:
  1. `00-introduction.md` — who this is for, what's covered, three myths worth killing
  2. `01-choosing-target-languages.md` — a six-factor scoring sheet for picking your first (and second) language
  3. `02-rights-in-plain-english.md` — who may translate what, four common author situations, AI-specific rights notes
  4. `03-budgeting-ai-plus-human-review.md` — honest 2026 dollar ranges, budget worksheet, the spend/save split
  5. `04-the-workflow-draft-to-final.md` — week-by-week operating procedure, source freeze, AI prompts, hiring the reviewer
  6. `05-bilingual-qa.md` — checking a translation you can't read: structural passes, glossary pass, the independent native check
  7. `06-covers-subtitles-and-re-layout.md` — cover text, subtitle transcreation, typographic conventions, fonts, re-layout
  8. `07-marketing-to-readers-abroad.md` — keywords in-language, foreign review velocity, per-market social channels, pricing by market
  9. `08-going-live-staying-live.md` — pre-publish checklist, first 48 hours, royalty bands, maintenance cadence
  10. `09-checklists-and-templates.md` — copy-paste templates: budget sheet, translator agreement, terminology sheet, QA log, rights memo, launch sprint
- **`site/`** — the same handbook as a static HTML site (built from `docs/`, no external dependencies, no JS needed)
- **`build.py`** — builds the site from `docs/` (Python 3 standard library only)
- **`tests/test_build.py`** — verifies links, rendering, and site integrity (also stdlib only: `python3 -m unittest`)

## How to run it

Everything is local and offline. Requires Python 3.8+.

```bash
# build the static site from docs/
python3 build.py

# view it (any static file server works)
python3 -m http.server 8000 --directory site
# then open http://localhost:8000

# run the tests
python3 -m unittest discover -s tests -v
```

`build.py` regenerates every file in `site/` from `docs/`, so edits go in Markdown and rebuild — never edit `site/`.

## How this handbook differs from its neighbors

This is one of three handbooks with deliberately separate scopes:

- **This handbook (translated-editions-handbook)** — selling *translated editions* of a book: language selection, translation budgeting and QA, rights for translations, marketing abroad.
- **everyday-translation-with-ai-guide** — using AI translation in *personal everyday life* (travel, reading, chat).
- **publishing-beyond-kdp** — distributing to *non-Amazon stores* in general (wide stores, aggregators), independent of translation.

Where topics overlap (e.g., wide stores appear here only insofar as they matter to a translated edition; rights on the original book appear only where they bear on translation), each handbook points to its neighbor rather than duplicating.

## Credits and license

- Written by Dylan Asdale. Published by **Asdale Dynamics, LLC** — beginner-friendly AI education, books, guides, and practical tools.
- Hub site: https://dylanasdale.github.io
- This handbook is educational material only and is **not legal advice**; translation and publishing rights carry real money, so verify with counsel where stakes are high.
- Operating principles: local-first (works offline), no secrets, no API keys, no personal data in files.
- Licensed under the MIT License — see [`LICENSE`](LICENSE). *Copyright (c) 2026 Asdale Dynamics, LLC*
