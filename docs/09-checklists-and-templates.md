# Chapter 9 — Checklists and Templates

**The one-sentence version:** everything from the previous chapters, in copy-paste form — the budget worksheet, the translator contract, the terminology sheet, the QA log, the rights memo, and the launch-week sprint list.

Fill these in, save them in your edition's working folder (the tree from Chapter [04](04-the-workflow-draft-to-final.md), section 4.8), and you'll never lose the thread of a translated edition again.

---

## Template 1 — Translated edition budget worksheet

Copy the block, fill the numbers you get from real quotes. The example numbers come from Chapter [03](03-budgeting-ai-plus-human-review.md)'s "Recommended" Spanish scenario.

```text
TRANSLATED EDITION BUDGET — [LANGUAGE] edition of [BOOK TITLE]
Words in frozen source: [____]        Date source frozen: [YYYY-MM-DD]
Prepared by: [Author / LLC name]      Target launch: [YYYY-MM-DD]

1. AI translation draft cost                    $ [____]  ([model name/version])
2. Reviewer fee
   - full review pass (@ $[___]/1k words)      $ [____]
   - change-review pass(s) after QA            $ [____]
   - native blurb/subtitle re-write             $ [____]
   - market notes memo (optional add-on)        $ [____]
3. Second proofread (junior native, [__] hrs)   $ [____]
4. Cover adaptation
   - self-service text swap                    $ [____]
   - designer time (if needed)                 $ [____]
   - new local-script font license (if needed) $ [____]
5. Interior/layout
   - ebook reflow                              $ [____]
   - print: spine/page-count re-template       $ [____]
   - fixed-format re-pagination (if any)       $ [____]
6. Third-party QA spot-check ([__] words)       $ [____]
7. Ads/launch budget (optional)                 $ [____]
8. Contingency (10%)                            $ [____]
                                               --------
TOTAL                                           $ [____]

Reference point (2026 market): careful, human-reviewed, AI-assisted
translation of a 40-60k-word book should land in the $300-$900 range
per language. Quotes far below that = missing the human review step.
```

---

## Template 2 — Translator/reviewer agreement (one page, plain English)

Fill in the brackets, sign, move on. This template is deliberately simple and assumes a small independent arrangement; if you're engaging a translator through a platform (Fiverr, Upwork), their platform terms sit on top, and you attach this as the job's written brief. Not legal advice — have your counsel review before signing for your LLC.

```text
TRANSLATION SERVICES AGREEMENT

Date: [YYYY-MM-DD]
Between: [YOUR NAME / LLC], ("Client"), and [TRANSLATOR NAME], ("Translator").

1. Work. Client has created an original work entitled "[BOOK TITLE]"
   (the "Original Work") and wishes to produce a [LANGUAGE] translation
   (the "Translation"). Translator will review, correct, and approve a
   [LANGUAGE] translation of the Original Work produced by the Client
   using AI-assisted translation tools, and/or translate portions as
   agreed, delivering:
     - reviewed translation files per the agreed chapter schedule,
     - an updated terminology sheet,
     - a change log and notes on the most common corrections,
     - a native-language blurb/subtitle proposal (separate fee or bundled: ____).

2. Deadlines. First deliverable (chapters [N-M]) on [DATE]; full
   reviewed manuscript on [DATE]; change-review pass(es) within 10
   business days of receiving QA fixes.

3. Payment. Client will pay: $[____] for the review pass
   ($[____ per 1,000 words]), $[____] for change-review pass(es),
   $[____] by deposit on signing and the remainder within 30 days of
   final delivery. Expenses (fonts, platform fees) paid by: ____.

4. Copyright. To the greatest extent permitted by law, all rights in
   the Translation — including copyright — are assigned to Client upon
   payment, as a work made for hire and independent of any AI tooling
   used by Client. Translator retains portfolio/display rights in a
   brief excerpt solely to demonstrate their services (with an "AI-
   assisted draft reviewed by [Name]" attribution when shown).

5. Professional standard. Translator represents they are a native or
   fully professional speaker of [LANGUAGE], will work to professional
   publishing standards, and will flag (not silently pass) any content
   they believe to be factually, legally, or culturally risky in the
   target market.

6. Confidentiality. The manuscript is confidential until publication.

7. No further license. Translator grants no one else any right to
   publish or use the Translation.

Signed:  ______________________  (Client)
         ______________________  (Translator)
```

---

## Template 3 — Terminology sheet (pre-translation)

Make this 30–60 rows long. Anything the *AI or a new reader* could plausibly get wrong belongs here. The `Keep as-is` column decides behavior: "translate" means "use my target rendering," "keep" means "leave byte-identical."

```text
TERMINOLOGY SHEET — [LANGUAGE] edition of [BOOK TITLE]

| English term             | Target rendering        | Keep as-is? | Note                                  |
|--------------------------|-------------------------|-------------|---------------------------------------|
| KDP Select               | (keep English)          | keep        | Amazon product name                   |
| work-for-hire            | [target rendering]      | translate   | legal term — reviewer should confirm the
                                                          target-market equivalent is the right register |
| plain English            | [target rendering]      | translate   | the book's core phrase; register matters   |
| [acronym: LLM, API, FPA] | [decide per market]     | see note    | some markets expand acronyms; reviewer call |
| [character name]         | [target rendering]      | translate   | include pronunciation note for the reviewer  |
| [measurement: 16 oz]     | [target: 473 ml or keep] | translate  | metric in most non-US markets                |
| [date format: May 5]     | locale format           | translate   | 5 de mayo / 5. Mai / 5月5日                    |
```

Notes for whoever fills it in:

- Reviewer *may* change any translate row — that's the system working. They update the sheet when they do, so it stays the single source of truth.
- Rows you can't decide *before* translation (e.g., "should LLM be expanded in Japanese?") are rows for the reviewer's kickoff call, not for you.

---

## Template 4 — The AI translation instruction block

This is the prompt-and-constraint text from Chapter [04](04-the-workflow-draft-to-final.md), in fill-in form. Save it in `02-prompts/` and reuse as-is per chapter.

```text
[LANGUAGE]: ____   VARIETY: (LATIN AMERICAN / SPAIN / BRAZILIAN / etc.) ____

Persona: professional book translator.
Source: the chapter text below, formatted in Markdown.

Rules:
 1. Style: warm, plain, direct; expert explaining to a beginner; never
    condescending. Match the tone of the reviewer-approved sample
    paragraph attached.
 2. Preserve Markdown structure exactly: headings (#/##/###), lists,
    tables, code fences, bold/italic, links. None dropped, none merged.
 3. Do NOT translate: strings marked keep-as-is in the terminology
    sheet, any code or code-adjacent syntax, any URL, any placeholder
    like {name} or {{var}}.
 4. Terminology sheet below is binding; use exactly those renderings.
 5. Adapt culture-bound references ONLY when needed to read naturally;
    flag every adaptation in a "Translator notes" block after the text.
 6. One-to-one paragraph matching. No summarizing, no additions, no
    omissions. If the source has an error, translate faithfully and
    flag it in the notes block — do NOT fix it silently.
 7. Numbers: dates to [locale format], decimals to [comma/point],
    measurements converted where the target market's convention is
    unambiguous (and flag ambiguous ones).
 8. Output: ONLY the translation and the notes block. No commentary.

TERMINOLOGY SHEET: [paste current version]
REVIEWER-APPROVED SAMPLE PARAGRAPH: [paste]

SECTION TO TRANSLATE:
[paste one chapter / 3,000-6,000 words]
```

---

## Template 5 — Bilingual QA logging sheet

The QA log from Chapter [05](05-bilingual-qa.md), in fill-in form. Ugly-but-real beats nonexistent.

```text
QA LOG — [LANGUAGE] edition of [BOOK TITLE]

STRUCTURE PASS (run by me, date ____)
 - paragraph count per chapter: OK / chapter [__] off by [__] (reason: ____)
 - headings (#/##/###): OK / mismatch at [__]
 - tables: rows intact? [Y/N per table that failed: __]
 - code blocks: [___] in source, [___] in translation (differs: ____)
 - links: [__] in source, [__] in translation (differs: ____)
 - leftover English scan: [strings found: ____]
 - translator-notes blocks stripped from final: [Y/N]

GLOSSARY PASS (date ____)
 - terms checked: [__] / divergences found: [list]
 - decided with reviewer on [date]: [term → rendering, everywhere]

THIRD QA PASS (name ____, date ____)
 Sample: [chapter/pages]
 Q1 reads-human        : [notes]
 Q2 confusing sentences: [notes]
 Q3 tone               : [notes]
 Q4 humour/idiom       : [notes]
 Q5 local fit          : [notes]
 Q6 terminology        : [notes]
 Q7 risky claims       : [notes]
 Q8 embarrassing       : [notes]

Bugs found: [__] total ([__] structure, [__] consistency, [__] content, [__] tone)
Fix round: [dates]   Re-QA scope: [sections only / full pass]
Sign-off date: ____
```

---

## Template 6 — Rights memo

The full plain-English version from Chapter [02](02-rights-in-plain-english.md), section 2.7, standing alone:

```text
TRANSLATION RIGHTS MEMO — [LANGUAGE] edition of [BOOK TITLE]
Date: [YYYY-MM-DD]

ORIGINAL WORK. [Book Title], copyright (c) [year] [author / LLC name].
I own, or am authorized to license, the original work and hold the
exclusive right to create and publish translations of it. Evidence:
[describe — e.g., "original is self-published by me via KDP; no
publishing or collaboration agreement restricts derivatives" / "signed
agreement dated ____ grants me subsidiary/translation rights" / "co-
owner agreement dated ____, signed by all owners, permits translations
with shared proceeds split ____"].

THIS TRANSLATION. Created by me with AI-assisted translation tools and
reviewed, corrected, and approved by [Translator Name], a professional
[native language] translator, on [date], under the services agreement
dated [date] assigning the Translation's copyright to [me / my LLC].

SCOPE. Worldwide, all channels, no exclusivity granted, no third-party
translation license currently in force.

KNOWN LIMITS. [Quoted/cited material that I don't own and how its
permission covers translation / image licenses in use / AI-disclosure
policy of each store, re-read on [date] / any promised exclusivity to a
platform, e.g. Amazon's translation program, and its terms].

OS RECORD. Frozen source: [filename, date, hash or drive location].
Final files: [location]. Translator contract: [location, signed date].

Signed: [Name], [role], [LLC]
```

---

## Template 7 — Launch-week sprint list

The first week after publish, in one page. Daily, 30 minutes.

```text
DAY 1  - Upload complete; personal purchase flow verified in target market;
         Look-Inside sample correct; price matches bands; ads paused.
       - Tell translator, send live link, ask for listing proofread.
DAY 2  - Announce in your own newsletter + the 2 channels picked in Ch 7.
       - Post the "how I translated this with AI + human review" story
         in one indie-author community (markets the method, sells the book
         incidentally).
DAY 3  - Apply translator's listing-proofer notes (blurb line edits, keyword
         changes).
       - Set first small book ad: [store] ads, 3-5 verified keywords
         only, $3-5/day.
DAY 4  - Send 5-10 ARC copies to readers in the language who asked.
       - Add translated edition to your author-site hub page (if any).
DAY 5  - Check first search-placement for your keywords; adjust metadata
         if a keyword returned junk.
       - Contact 3 communities/podcasts/book-clubs in the language using
         the translator's market memoir (Template: market notes memo).
DAY 6  - Break. Honestly.
DAY 7  - Review week's numbers; pick next week's ONE marketing action,
         not five.
```

---

## Template 8 — Second-edition (content-update) translation pass

When your English book gets a real second edition, this is the *cheap-path* plan that preserves your whole pipeline:

```text
SECOND EDITION, [LANGUAGE] — UPDATE TRIPWIRE PLAN

1. DIFF the English sources: old frozen file vs. new edition file.
   List new/changed/deleted paragraphs. (One page.)
2. Estimate: [__] new words to AI-draft + [__] changed words to
   re-translate; deleted sections = drop.
3. Send your ORIGINAL reviewer (or their successor) only:
     - the new/changed sections as AI drafts,
     - the updated terminology sheet,
     - the previous reviewed file for consistency anchoring.
   Fee: per-1,000-words changed, typically 30-50% of full rate.
4. Run QA structure pass + third QA pass on changed sections only.
5. Re-layout (page counts shift), re-upload, price unchanged.
6. Update rights memo + QA log with a "second edition" entry.
```

---

## One last note

Everything in this handbook reduces to one practice: **write things down while they're true.** The frozen file date, the terminology decisions, the reviewer's contract, the QA bugs, the rights memo, the price bands you checked. Six files of plain text per edition costs you an hour to keep current, and it's what makes translated edition #4 a weekend project instead of a six-week scramble. Future-you, running three languages you'd forgotten the details of, says thank you.

*Back to the start: [Introduction](00-introduction.md)*
