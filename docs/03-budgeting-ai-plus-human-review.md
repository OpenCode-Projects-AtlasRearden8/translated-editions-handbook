# Chapter 3 — Budgeting: AI Translation + Human Review

**The one-sentence version:** a careful, human-reviewed AI-assisted translation of a typical 40,000–60,000-word nonfiction or short-fiction book costs roughly **$300–$900 per language** in the 2026 market — and every dollar below that range usually comes out of quality, not luck.

This chapter gives you honest numbers: what things cost, what the cheapest truly-insurable version of the project looks like, where authors waste money, and where under-spending hurts. All figures are in USD and describe realistic 2026 market rates; adjust for inflation and for your own research when you get real quotes.

## 3.1 What the full pipeline actually consists of

Moving a book from English to another language, done right, involves these components. Each has its own cost shape.

| # | Component | Who/what does it | Cost shape |
|---|---|---|---|
| 1 | Source prep (frozen file, clean markdown/DOCX, no track changes, notes resolved) | You | Free, but see 3.2 for why it isn't trivial |
| 2 | AI translation draft | You + AI (any capable long-context model) | $0–$30 in API/subscription costs depending on model and length |
| 3 | Human review / edit of the translation | A native-speaking professional | **$150–$600** (the big line item) |
| 4 | Proofread of the final reviewed file (light read for typos/formatting) | Same person or a second, cheaper pair of eyes | $0–$150 |
| 5 | QA (bilingual sample checks, terminology sheet, metadata) | You + reviewer | $0 (your time) or bundled into #3 |
| 6 | Cover adaptation | You (or designer, if you don't make covers) | $0–$100 "text shipment" changes; ~$50–$250 if a designer touches it |
| 7 | Interior re-layout | You (template regeneration) | $0–$50 for float/fixed-format book |
| 8 | Store setup and metadata | You | Free (Amazon/KDP, Draft2Digital) |

The numbers that surprise new author-translators: **#1 and #5 are free but dominate quality**, and **#3 is the only step that reliably protects your name.**

## 3.2 The one cost you can't buy your way out of: preparing the source

What AI translation models do well now: faithful transfer of text that's already clean, well-structured, and free of ambiguity. What they do badly, or inconsistently: guess what you meant if you haven't decided yet.

So the preparation step — your first real job — includes:

- **Freeze the content.** Pick the exact version. Copy it to a file named `book-source-en-2026-05-01.docx` (or `.md`) and translate *that*. Offline-fix a typo? Update the frozen file and note it. Change your mind mid-stream? Re-do the affected sections through the full pipeline. Do not let source and translated edition drift.
- **Kill ambiguity.** Resolve every dangling pronoun, every "see the chapter before this," every note-to-self in comments. AI translation carries unresolved ambiguity into another language and *multiplies* there, where you can't see it.
- **Terminology list.** Make a small table of 30–50 domain-specific terms before translating: names of your frameworks, acronyms (KDP Select, LLM, FFXIV, XR), recurring jokes, product names, place names, whether bullets should be translated at all. Hand this to both the AI (as a glossary/prompt constraint) and the human reviewer (who will keep it consistent).
- **Format decisions.** If your English book has tables, code blocks, or sidebars, decide now that they'll be translated as their own blocks. AI models handle this well when told; badly when surprised.
- **Cut what shouldn't cross borders.** Anything that doesn't read well in translation usually shows up during prep: US-only jokes, regionally specific measurements (give metric wherever it isn't semantically dangerous), and American cultural references with no equivalent. Your reviewer will catch more; you catch the big ones now for free.

For a typical book, this prep is a **full working week of real time**, and it's the difference between a translation that needs one careful pass and one that needs three. A rushed source file costs the reviewer more, which the reviewer wisely quotes into the next revision's fee.

## 3.3 What human review costs, honestly

This is the step where naive authors and professional translators both get fed up with each other, so let's be concrete. Rates for *reviewing a quality AI-assisted draft of a book* vary by language pair and translator seniority. In 2026, for reference:

| Language | Typical review rate, per 1,000 words | What this implies for a 50,000-word book |
|---|---|---|
| Spanish (Latin American) | $8–$18 | $400–$900 |
| Portuguese (Brazilian) | $7–$15 | $350–$750 |
| Italian, French, German | $10–$25 | $500–$1,250 |
| Japanese | $12–$30 | $600–$1,500 |
| Hindi, Indonesian, Tagalog, Vietnamese | $5–$12 | $250–$600 |

Ways to land at the low end *without* cutting quality corners:

- **AI did the heavy lifting.** The reviewer is not translating from scratch; they are reviewing a draft that's already 80–90% senible. Quote the task honestly as "review/edit of AI-assisted draft" — it is a different task from translation, priced lower, and experienced translators know it.
- **Your source was prepared.** The cleaner the source, the fewer "wait, what does the author mean" queries they send you back, the less back-and-forth, the lower the bill.
- **You pay for milestones, not goodwill.** A reviewer who is paid 3 chapters up front, then per-delivery, moves faster than one holding an unpaid invoice at the end.
- **A lighter final proof.** If your reviewer is senior, hire a second, junior native speaker to proofread the final file rather than paying the senior to re-read. Cheaper for the last 5% of polish.

Ways authors blow the budget (so you can avoid them):

1. **Going back to the reviewer four times because the English source kept changing.** Each re-open costs $50–$150.
2. **Unnecessarily re-reviewing the *whole book* after a 2% fix.** Contract for *pass-review of changed sections only* after the first full pass. Get this in writing.
3. **Using Fiverr/Upwork at the absolute cheapest rate and then re-doing everything.** A $100 review of bad AI output is $100 spent on doing it once.
4. **Paying a translator full translation rate when you wanted a review rate** because you asked for the wrong deliverable. Be explicit in the job posting.

## 3.4 The scenario-cased budget (what you'd actually pay)

Using honest middle-rate numbers for a **50,000-word Spanish edition with a prepared source**:

| Scenario | AI draft | Review | Extra QA/design/layout | Total | Notes |
|---|---|---|---|---|---|
| **Minimum viable** | $0 (free-tier AI) | $400 (regional rate, new freelancer) | $0 (you do cover and layout) | **$400** | One full human pass, no second proof |
| **Recommended** | $10 (better model/API) | $500 (experienced reviewer) | $100 (second-pass proofread, ~2 hours; a template cleanup) | **$600** | The version we recommend for a serious book |
| **Conservative** | $20 (premium API) | $700 (senior reviewer with niche knowledge) | $200 (designer adjusts cover) + $100 proofread | **$1,020** | For a book with your name's integrity riding on it in a market you'll expand into |
| **Multi-language starter pack** | $30 | $1,500 (2 languages × $500, senior shared) + $300 | $400 | **~$2,200** | Two coordinated editions (e.g., es + pt) with shared QA infrastructure |

The multi-language scenario has a hidden efficiency worth naming: **the second language costs less than the first**. Your frozen source file, terminology sheet, review contract template, cover template, and QA process all exist after the first pass. The second language's marginal cost is essentially AI + new reviewer + your QA time. Plan for a **catalog**, not one-off, and your per-language cost drops 20–40% by edition three.

## 3.5 Where to spend and where to save

**Spend on:**

1. **The reviewer.** Language-matched, genre-matched, and fluent *in your niche vocabulary*. A reviewer who has translated books in your genre is worth 2x a reviewer who has translated *documents*.
2. **Prepared source.** An extra week of prep will save a month of re-reviews. The prep is free but time-intensive; it is the highest-ROI hour count in the whole pipeline.
3. **The model, where it matters.** Difference between a cheap and mid-tier model on draft translation quality for well-structured nonfiction is smaller than the difference between a bad and a good reviewer — but on tricky fiction, historically-inaccurate idiomatic dialogue, or technical code, premium model tiers matter. For a how-to book, a mid-tier model is fine.

**Save on:**

1. **You.** Freezer-prep, glossary, layout, and store setup are your work; not paying those out is how the arithmetic works for solo authors.
2. **Cover tweaks vs. cover rebuilds.** If your cover is typographic (just the title + name on a clean background), translating it is a 15-minute budget ($0); if it's an elaborate illustrated scene with side text (Chapter [06](06-covers-subtitles-and-re-layout.md)), plan $50–$250 for a designer.
3. **Avoid mid-process re-model switches.** Pick a model, run through, review. Switching models mid-book costs you redo time for marginal quality gains you likely can't measure.

## 3.6 Revenue-share alternative (Babelcube-style platforms)

There are platforms where you publish a translation and the translator gets a percentage of sales instead of an upfront fee (Babelcube historically is the example; smaller marketplaces come and go). Three things to know:

- **The math**: A revenue-share translator takes, say, 30–50% of net forever. Over a book that eventually earns $4,000, that's $1,200–$2,000 versus your $500 upfront. **If you're confident in demand, paying is cheaper.** If you're testing a language you're unsure about, revenue-share costs nothing until it works.
- **The control trade**: On some platforms the translator's leverage includes *how* the translation reads. You still own the copyright in most revenue-share contracts, but the working relationship is brokered and less personal than a direct hire.
- **The QA gap**: Revenue-share platforms rarely give you a second pair of eyes on the *reviewer's* work. Your bilingual QA (Chapter [05](05-bilingual-qa.md)) becomes more important, not less.

We consider revenue-share a **legitimate trial channel** for a book in a language that has scored 18–21 on the Chapter [01](01-choosing-target-languages.md) sheet — worth testing, not obviously worth paying full rate for yet.

## 3.7 Budget worksheet (with the numbers filled in for you)

This is the worksheet from Chapter [09](09-checklists-and-templates.md) with example numbers, for the "Recommended" Spanish scenario above:

```
TRANSLATED EDITION BUDGET — Spanish edition, 50,000-word nonfiction book
Author/LLC: Asdale Dynamics, LLC   Source frozen: 2026-05-01

AI translation draft                    $   10   (mid-tier model, ~$0.0002/word w/ glossary)
Reviewer fee (senior native, 1 full pass + 1 change review)
  - review pass                         $  450
  - final change review pass            $   50
Second proofread (junior native, 2h)    $  100
Cover text shipment + spine check         $   0   (typographic cover, I do it)
Interior re-layout (template)             $   0   (same template)
Terminology sheet creation                 $   0   (my time, 4 hours)
Bilingual QA (sample checks)               $   0   (my time + 3rd-party check ~$75)
Third-party spot-check QA, 2,000 words   $   75
Contingency (10%)                        $   68
                                         ------
TOTAL                                   $  753
```

Where the contingency is genuinely there to be spent: a re-review because the reviewer took a month off, a per-country pricing adjustment you hadn't predicted, a cover designer fee if the text doesn't fit the cover, or a small rush fee when your launch date collides with Amazon promotion scheduling.

## Bottom line

A realistic, well-budgeted translated edition — of a prepared, frozen source — costs **$400–$1,000 per language** in 2026, with most of the variance in the reviewer's rate and seniority. The cheapest safe version of the project is: prepared source, mid-tier model for the draft, one experienced native reviewer, one junior proofread, and you doing everything else. Two languages in one calendar window cost less than two languages in two windows, because the second language reuses your process. And if a platform wants to translate your book for free in exchange for its rights, read Chapter [02](02-rights-in-plain-english.md) twice before you accept.

*Next: [The Workflow: Draft to Final](04-the-workflow-draft-to-final.md) — week by week, what actually happens.*
