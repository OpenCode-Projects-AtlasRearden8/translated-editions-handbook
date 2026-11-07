# Chapter 5 — Bilingual QA

**The one-sentence version:** you can't read the language, and you don't need to — you need to check the *things that don't depend on reading*: structure, completeness, consistency, glossary compliance, and one independent native pair of eyes on a sample.

This chapter is about verifying a translation you can't personally read. It's easier than it sounds, because a surprising amount of a book's quality is structural, and structure is language-neutral. The chapter has two halves: checks **you** can do without knowing the language, and checks you **delegate** to a separate, independent native speaker.

## 5.1 Why QA is a separate step from review

Your reviewer did excellent work. But they are one human who has been staring at this manuscript for weeks, and the failure modes that slip past a single reviewer are predictable:

- **Consistency drift.** Section 2 used "Cuaderno de trabajo" and section 9 used "Libro de ejercicios" for the same term. Both are fine alone; together they read as two different products.
- **Merge accidents.** Chapter 14's opening sentence is Chapter 13's closing sentence, or a paragraph was lost in a copy-paste. Reviewers don't lose paragraphs; file-assembly steps do.
- **Formatting regressions.** A table that was a table in English became a paragraph became a list of three broken lines. Numbered lists that restart where they shouldn't.
- **Skipped content.** Chapter Twenty-two got renumbered in the source during freeze, and the reviewer's QA sample missed it.
- **The classic:** the translator-notes block never got stripped and ships inside the book.

None of these are reading-the-language checks. All of them are checkable by you today, for free.

## 5.2 The structure-only pass (you can do this tonight)

Open both files (frozen English and reviewed translation), and run these checks chapter by chapter. A mechanical, honest process; 30–60 minutes per book.

| # | Check | How |
|---|---|---|
| 1 | **Paragraph count per chapter** | Count blank-line-separated paragraphs. Should match within a paragraph or two (short paragraph merges are OK; a 19-paragraph gap is not). |
| 2 | **Heading count and order** | Every `##` in English has a matching `##` in translation, in the same order. Same for `###`. |
| 3 | **Tables survived** | Count table header rows (`|---|`), and each table's row count — many AI models turn tables into flat lists when tired. |
| 4 | **Code blocks survived** | Count fenced code blocks. Their *content* should be identical (you compare the code; code doesn't translate). |
| 5 | **Links intact** | Same link count per chapter, and every URL byte-identical. |
| 6 | **Bold/italic markers similar** | A mismatch isn't fatal but a *pattern* of missing `**bold**` is a sign of a bad merge. |
| 7 | **Numbered lists, step counts** | Chapter titled "7 steps in this workflow" — the target language chapter still has 7 numbered items. |
| 8 | **Numbers and units unchanged** | Any number in a German translation looks identical to English one unless your reviewer presumably converted to local convention — spot-check a handful. |
| 9 | **Notes blocks stripped** | Search for strings like "Translator:", "Notas del traductor", "[note-to-self". Nothing flagged should reach the reader. |
| 10 | **No leftover English sentences** | Regex search for `\b(the|and|with|of|you|this)\b` inside long sentences — a couple of hits is nothing, but the classic failure of one full paragraph remaining in English is found fast by scanning for dense clusters of hit-lines. |

Each check is one command away in practice:

```bash
# paragraph counts per chapter, side by side
grep -c '^$' book-source-en-2026-05-01.md
grep -c '^$' chapter-07-reviewed-es.md

# heading counts
grep -c '^## ' book-source-en.md
grep -c '^## ' book-final-es.md

# URL survival (all URLs identical)
grep -o 'https://[^ )"]*' book-source-en.md | sort | uniq -c | sort -rn
grep -o 'https://[^ )"]*' book-final-es.md  | sort | uniq -c | sort -rn

# leftover-English scan (best-effort heuristic; you eyeball the hits)
grep -nE '\b(the|and|with|of|you|this|that)\b' book-final-es.md
```

If any tool above is unfamiliar, it's `grep` — a standard terminal text-search utility that exists on every laptop; paste commands into your system's terminal. This is one of the rare moments it's worth being able to run two commands, and it saves one reviewer round-trip ($50+).

## 5.3 The glossary compliance pass

Open the terminology sheet and your reviewed file. For each glossary term that *should* be translated, search the reviewed file for the term's target-language spelling. For each that should remain in English (product names, code, acronyms like KDP Select), search for the English string and count instances.

Two things this pass catches that a reviewer often doesn't realize mattered:

- A decision the reviewer made *silently* differently from the glossary: renamed a concept mid-book. Ask them; a silent half-book rename is the most expensive bug to fix later.
- **Accidental translation of protected strings.** If "KDP Select" is showing up as "KDP Selección," your reviewer (or the model) has caught a flow-error; this term must be byte-protected everywhere.

Consistency is a reader-visible feature. A book that says the same thing two ways reads as sloppy in *every* language.

## 5.4 The self-index pass

A translated book teases readers in the front matter. Check:

- Table of contents page (or chapter list): every chapter title matches the actual chapter headings, one-to-one, no stale entries from English.
- Numbered chapter names ("Chapter 7 — Budgeting") — the number matches everywhere.
- Cross-references: "see Chapter 5" points to a chapter that exists in the translated edition with the same number.
- Hyperlinked TOCs (EPUB): click-test every link. Every one.

## 5.5 The independent native check (the "third pair of eyes")

This is the part you cannot fake, cannot self-serve, and should assign to a **different person** than your reviewer. Not because your reviewer didn't try — because a fresh reader catches what a tired one can't, and because QA's purpose is *independent* confirmation that the pipeline stayed intact.

**What to hire for:** a native speaker of the language who reads your niche, **12–20 pages (or 2,000–3,000 words) you select** — for a book, that's typically the opening two chapters plus two random mid-book chapters — and gives you written feedback in that language. Cost: $50–$150. Deliverable: short answers to 8 questions.

**The 8 questions:**

1. Does this read like it was written by a human, for a native reader, or does anything ring machine-translated?
2. Are any sentences confusing, ambiguous, or do they need to be re-read?
3. Does the tone match "friendly expert explaining things plainly," or does it read too formal/too casual in places?
4. Are any idioms or jokes broken or nonsensical?
5. Are examples and references sensible for a reader in this country, or do they scream "this was written for an American audience"?
6. Technical terms (from the terminology sheet) — do they read as correct, native, current? Or stilted, dated, or non-standard?
7. Any claim that would be *factually odd, legally risky, or culturally off* in this country? (e.g., "Amazon US. In your country, the top-of-market competitor may be different.")
8. Anything embarrassing — in the language itself or its cultural echo?

**How to pick QA pages:** open a random page; if it starts mid-paragraph, move back one page. Pick three starting points spread across the book. Write the page numbers (or chapter names) in your QA log. Three segments sampled *well* catch most consistency and tone failures.

**A free supplement:** ask a *reader* you trust, ideally one who reads in that language, to simply read the sample story with their own eyes. Even without a professional's editing lens, pure reader reaction will catch tone failures and awkwardness that structure-based checkers miss. A reader from your own fan base is the best free QA there is. Be careful not to send files outside the community in a way that leaks an unpublished final file, if that matters to you.

## 5.6 What bilingual QA can't catch

Be humble about the limits of the process:

- **A subtle mistranslation of a fact** that the reviewer misread in the source won't necessarily be caught in the sample. Professional colleagues reading for meaning is the main defense; the third pair of eyes is the backup.
- **A good joke that becomes okay-but-not-funny.** The joke works; the comedy dies in flight. It happens. Most translated books accept some humor loss.
- **Market-fit problems.** The translation could be flawless and the book still not attract that market because the *topic framing* doesn't resonate. That's a marketing question (Chapter [07](07-marketing-to-readers-abroad.md)), not a QA one.

If the third pair of eyes finds a *meaning error*, that's a stop-the-presses finding — don't just patch those pages. Ask your reviewer to do a targeted re-read of the surrounding section, pay them a small extra fee, and log what failed. Reviewers with a diagnosed blind spot usually fix it for the rest of the book for free, because it's in both of your interests.

## 5.7 When QA finds problems: the fix round

- **Structure errors** (missing paragraph, mangled table): patch the specific location, re-run the structure pass for the whole chapter. Fast, free.
- **Consistency errors** (glossary divergence): decide the winning term with your reviewer, apply the fix across the file, update the glossary. One communication round. 1–2 days.
- **Tone errors** (machine-ringing, joke died, idiom broken): reviewer fixes; if more than 3–4 clusters of them, pay for a light second review pass rather than a single patch round.
- **Content errors** (meaning inverted, claim odd): reviewer rechecks; you confirm in English, then re-run third-party QA on the fixed section only.

The fix round plus re-verification is typically 3–5 working days. It is part of the plan, not a disruption — schedule it.

## 5.8 QA log template

You keep a log per language. And add short entries — even ugly text beats no record.

```text
QA LOG — ES edition, 2026-05-14 to 2026-05-22

STRUCTURE PASS (me):
 - para counts OK (CH 1-24, CH 12 had -2 = reviewer merged two paras, OK)
 - CH 7: table in 5.2 lost a row → restored from AI draft, verified with reviewer
 - links count differs by 1: found leftover "preface" link in CH 1, removed

GLOSSARY PASS (me):
 - "trabajo freelance" → reviewer used "trabajo autónomo" CH 3 vs "freelance" CH 9
   → decided with reviewer: "freelance" is the market-standard use in this genre, updated
 - no accidental translation of product names; KDP Select OK everywhere

THIRD-PAIR QA (M. Ruiz, 2026-05-19):
Sample: CH1 (pages 1-14), CH9, CH17 (random start p. 148)
 - Q1: reads human, good warmth. 3 sentences in CH1 flagged for re-read → fixed
 - Q3: CH17 slightly too formal, softened 5 sentences
 - Q5: "American audience" feel in CH9 example (US-only retail references) →
     reviewer swapped to EU/MX equivalents in CH9 CH10 CH11 (cascades)
 - Q8: none
Bugs found: 6 (3 structure, 2 consistency, 1 content)
Fix round: 4 days, re-QA on CH9 only, M. Ruiz confirms
Sign-off: 2026-05-22
```

## Bottom line

You cannot read the language, so you check everything that doesn't need reading: structure, glossary, TOC, leftover source artifacts. Then one independent native professional does the shortcut you can't: they *read* a sample and tell you whether the book reads like a human wrote it for them. The combination of a mechanical pass you can do tonight and a $75 third-pair-of-eyes check is what turns "I hope it's good" into "I know it's good enough to stand behind."

*Next: [Covers, Subtitles, and Re-Layout](06-covers-subtitles-and-re-layout.md) — what has to change visually, so the book reads as native and not as translated.*
