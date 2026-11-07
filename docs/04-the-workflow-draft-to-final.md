# Chapter 4 — The Workflow: Draft to Final

**The one-sentence version:** freeze a clean source, translate with AI under strict constraints, review with a professional human, QA bilingually, re-layout, publish — in that order, with a written record at each step.

This chapter is the step-by-step operating procedure. If you follow only one chapter closely, follow this one — it's the one that keeps the other chapters honest. The timeline assumes one language and a 40,000–70,000-word book; scale times per language.

## 4.0 The timeline at a glance

| Week | What happens | Where you can slip |
|---|---|---|
| 1 | Source prep, freeze, terminology sheet, model selection | Anywhere — this is where most delay is healthy |
| 2 | AI translation draft (in sections), self-review pass, reviewer kickoff | Batch schedule |
| 3 | Human review pass (reviewer's main working weeks) | Reviewer's own calendar, allow buffer |
| 4 | Bilingual QA of sample chapters, terminology consistency, metadata and cover work in parallel with review | Overlap weeks 3 and 4 |
| 5 | Fix round from QA findings, second proof, re-layout | Cover/store setup slips are cheap |
| 6 | Upload, pre-publish checks, live, first 48-hour review watch | Price/promo scheduling |

Total: **6–10 weeks** from frozen source to live book. The multi-language overlap rule: once language #1 is fully finished (live, caught no QA bombs in 2 weeks), language #2 can begin.

## 4.1 Step 1 — Source freeze (the week that saves five)

Concretely:

1. **Choose the file format that helps the AI help you.** Markdown or clean DOCX work best. Markdown is the friendliest for AI translation because structure is explicit. If your book is in InDesign/Figma/Vellum, export to Markdown or DOCX *first*, translate that, and lay out from the translation. Structure survives; InDesign-specific styling doesn't.
2. **Fix the small stuff now.** For 60 minutes, hunt typos, dangling references, broken links, and figure captions. Every typo you catch now is caught in one language instead of three.
3. **Create the terminology sheet.** 30–50 entries minimum. Format them as a three-column table (see `docs/09-checklists-and-templates.md`, template 3): term / how you want it rendered (or don't translate) / any note. Names of your fictional characters, if you write fiction, go in here too, with a pronunciation guide if there's any risk of a mangling.
4. **Write the AI instruction block** (see 4.2). Save it as a file next to the source. You'll paste it into every batch.
5. **Pick a working model.** In 2026, broadly capable long-context models handle well-prepared book-length translation in designated output sections, staying consistent across batches. Test with two chapters first; compare against the raw free-tier model. For a manual-style book (like this one), mid-tier models do the job; for literary fiction, spend the extra token spend.

## 4.2 Step 2 — AI translation with real instructions

Weak prompt: "Translate this book to Spanish." This produces something that *technically* satisfies the model and *barely* respects anything else.

Robust prompt:

```text
You are a professional book translator. Translate the following section
of a book from English to [LANGUAGE].

Style guidance:
 - Neutral [LATIN AMERICAN / SPAIN / BRAZILIAN] variety, friendly plain
   English-expert tone aimed at beginners. Never condescending. Warm and direct.
 - Preserve all Markdown structure: headings, lists, tables, code fences,
   bold, italics, and links exactly as given.
 - DO NOT translate: glossary terms marked [DO-NOT-TRANSLATE], code
   snippets, URLs, or placeholder strings. Keep them byte-identical.
 - For glossary terms present in the terminology table below, use the
   given target-language rendering every time it appears.
 - Adapt cultural references ONLY when semantically required to read
   naturally; flag them in a separate "translator notes" block at the end,
   which I will strip before review.
 - Preserve paragraph breaks one-to-one. Do not summarize, do not omit,
   do not add.
 - Region conventions: dates DD/MM/YYYY, decimal comma, currency in
   USD with a reader-appropriate local convention noted in the notes block.

Terminology table:
 [paste table]

Translator notes block:
 [anything the model wants to flag]

SECTION TO TRANSLATE:

 [paste one chapter's text]
```

Batching and sanity-pass rules:

- **One chapter (or 3,000–6,000 words) per prompt.** Smaller batches stay consistent and make QA traceable. Merge text in a file per chapter after.
- **Keep a translation log** — one line per chapter: date, model version, prompt variant, "translator notes" flag count. If quality dips, the log tells you where backwards, and *that* chapter is what your reviewer spends extra time on.
- **One clean self-pass** before reviewer. Read the OTHER language? No — you can't. Read the *back-translated text for structure*: many AI models and hobby tools produce a rough English back-translation. Skip paragraphs that are missing, doubled, or mis-ordered, fix those before reviewer. What you can't catch in back-translation (idiom, register, humor) is what the reviewer is for.
- **Do not remove the translator-notes flag block in the file you hand the reviewer.** It's context that shows them where the model was unsure — which is often exactly where human judgment matters.

## 4.3 Step 3 — The human review contract and deliverable

Hire before QA, not after (Chapter [03](03-budgeting-ai-plus-human-review.md), section 3.3). The reviewer's job, precisely:

1. Read the AI draft chapter by chapter. Correct errors of meaning, register, idiom, grammar, and cultural misfit. Preserve the author's voice — you'll describe it in one page plus samples (a paragraph from your English intro, translated and *reviewed once* as the tone anchor).
2. Review consistent with the terminology sheet, updating it as needed ("I decided to render RoleMining as [X] everywhere").
3. Flag any section where the AI output didn't just need editing but was *structurally wrong* (paragraph or table mangled, meaning inverted).
4. Deliver: the corrected file, a change log, and short notes on the most common edits so you can adjust future prompts.

The deliverable is the **reviewer's corrected file**, not a "notes document." Save it separately from the AI draft (e.g., `chapter-07-reviewed-es.md`), and keep the AI draft versioned for QA random-sample checks (Chapter [05](05-bilingual-qa.md)). Exact contract clauses are in template 2 of Chapter 09.

## 4.4 Step 4 — Bilingual QA

Full walkthrough in Chapter [05](05-bilingual-qa.md). Here, just position it: **bilingual QA runs *after* review** — not instead of it and not before it. It's the check that the *reviewer's work product* made it back intact, consistent, and structurally sound. It costs you time and roughly $75–$150 and is the reason you didn't bite a nail about the reviewer.

## 4.5 Step 5 — Cover, subtitle, and re-layout

Full separate chapter: [06](06-covers-subtitles-and-re-layout.md). Summary for the timeline: cover text translation and spine/kerning check in week 4, interior regeneration in week 5.

## 4.6 Step 6 — Metadata and store setup

The unglamorous but revenue-wise enormous step. Store-side work per language:

1. **Keyword set in the target language.** Not your English keywords translated; yours re-researched in the target language (Chapter [07](07-marketing-to-readers-abroad.md) has a 30-minute keyword process). Spanish readers searching for "out-of-print self-publishing" search very differently from English ones.
2. **Title and subtitle.** Often adapted, not translated literally. A subtitle like "AI for People Who Hate Jargon" may become something like "AI in plain words — step by step, no tears" in the target language. This is a marketing decision (Chapter [06](06-covers-subtitles-and-re-layout.md)), not a translation one.
3. **Description/blurb.** Rewrite for the market's reading habits, not copy-translated. If your English blurb uses lots of short punchy lines and paragraph breaks, Spanish book descriptions often use longer flowing sentences. Your reviewer's input on the *blurb* specifically is worth its own small fee; it's the highest-conversion text you'll write.
4. **Categories.** Fetch the target-language categories for each store; they differ in structure. Where the English niche has an *underserved* market (Chapter [01](01-choosing-target-languages.md)), find the matching target-language category — don't lump into "Computers & Technology."
5. **Keywords in the right locale.** Spanish keywords for the Amazon.es store, Mexican Spanish keyword variants for Amazon.com.mx. How to verify: search each keyword yourself in that store's search bar and see what comes up. Ten minutes.

## 4.7 Step 7 — Publish, then watch for 48 hours

- Upload files, run pre-publish checks (Chapter [08](08-going-live-staying-live.md) has a full checklist).
- Always upload the *working files too* (cover PSD, interior template) somewhere you'll find them in two years when a typo report arrives.
- 48-hour watch: sample the book on the store's previewer, check the blurb renders, check the table of contents links in the store preview, buy (or gift) a copy to yourself on a second account to see the Kindle purchase flow end-to-end, and scan your first reviews if any appear. If the first three reviews in that language mention the same word (translated poorly, robotic, incoherent), you have a QA bug; stop promoting and patch.

## 4.8 The working-file tree

One directory per language edition, with consistent names. This is what it looks like on disk at the end of the process:

```text
translated-editions/
  book-title-es/
    00-source-frozen-en-2026-05-01.md       (frozen English source, one per language)
    01-terminology-sheet-es.xlsx or .md
    02-prompts/                              (one .txt per chapter batch + log)
    03-ai-draft/                             (chapter 1-N AI output, untouched)
    04-reviewer/                             (reviewed files + reviewer contract + change log)
    05-qa/                                   (sample check results, third-party QA notes)
    06-layout/                               (cover, interior templates, print-ready PDF if applicable)
    07-store/                                (metadata, blurb, keywords, store screenshots for your records)
    08-rights/                               (rights memo per Chapter 02 template)
    09-live/                                 (final uploaded files, ASIN + live date)
```

Future-you needs this directory more than present-you does. Any question three years later — "which translator did I use?", "which model version?", "is the source the same as the Spanish edition?" — is answered by looking in one folder.

## Bottom line

The workflow has seven steps and one invariant: **the source is frozen and every downstream artifact names it.** AI translation is a mid-sized cost that produces most of the words; a professional human reviewer converts that output into a book that reads like it was written for its market, not translated into it; bilingual QA then makes sure the whole chain stayed intact. Budget your timeline, not just your dollars — 6–10 weeks for a first edition, shorter for language #2 onward.

*Next: [Bilingual QA](05-bilingual-qa.md) — how to check work you cannot read yourself.*
