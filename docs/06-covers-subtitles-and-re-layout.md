# Chapter 6 — Covers, Subtitles, and Re-Layout

**The one-sentence version:** a translated book should not *look* translated — the cover text, subtitle, interior layout, and store images need the small adaptations that make a new market's readers recognize it as a real book made for them.

This chapter covers the visual side of translation: what changes, what doesn't, how much effort each piece takes, and where "keeping it cheap-but-good" is actually possible. Two specific topics get their own sections because authors get them wrong most often: **subtitles** (what happens to the words under your title) and **re-layout** (whether the interior needs to look different in a new market).

## 6.1 The principle: native-looking, not native-faking

Readers in the target market make a 1-second judgment on the store page: *is this a real book here, or a translated one that doesn't belong?* The goal is the first impression, made honestly:

- The cover's typography follows the conventions the market already accepts.
- The subtitle hooks the reader in *their* language with *their* marketing style.
- The interior is not full of artifacts (weird paragraph breaks, American-style quotes and dates, half-working tables).
- Nothing pretends the book wasn't translated; and nothing advertises it loudly either. The copyright page handles the truth with a clean line — not a slogan.

We advise a translation line on your copyright page along these lines:

> *Spanish edition translated by [Name] from the original English edition, with AI-assisted translation tooling. Originally published in English in 2026 by Asdale Dynamics, LLC.*

Short, honest, and reads professionally in every market. Disclosure of AI is a values question more than a legal one (Chapter [02](02-rights-in-plain-english.md), section 2.5.3) — whatever you decide, put it on the copyright page, not the cover.

## 6.2 Covers: three cases by how your cover is built

### Case A — Typographic cover (title + name only, on background/texture)

- Cost: **$0**, your time only. Translate the title, translate your byline, adjust font size if the translated text is longer.
- Time: ~30 minutes if you have the editable cover file; 2–3 hours if you have to rebuild it from a flat image.
- Keep: original artwork/style — it's your brand across markets.
- Watch: translated titles *expand* in many languages. "Budgeting" becomes "Presupuestos" (fine) and "ADHD-Friendly Budgeting" becomes something 40% longer. Test at thumbnail size (roughly 100px wide) before committing: does the title still read on a phone? Many German and Spanish titles need a smaller font size or a two-line layout to survive thumbnail scale.

### Case B — Illustrated cover with embedded text

- Cost: **$30–$150** in designer time (Fiverr, hire your original designer, or a local designer found through translator contacts) if the text is baked into artwork; **$0–$50** if you have the layered file and can redo the text layer yourself.
- Keep: the illustration. Change: only the text, and consider the fonts — thin display fonts that look elegant in Latin script often lose personality in, e.g., German with its longer compound words, or fully die in Japanese/Chinese scripts, where you should budget for a local-script font (that one's a real cost: a licensed Japanese font for commercial use runs $50–$500 by typeface and weight).
- Watch for scripts you can't design for: for Chinese/Japanese/Korean, Russian/Cyrillic, Arabic, and Hindi (Devanagari), the local-script font is standard-issue, and front-cover text in those languages deserves review by a native speaker even if the translation body came from your reviewer — visual register (which font is "serious" vs "gimmicky") is a design judgment, not a translation one. Your reviewer may know a designer; ask.

### Case C — Text-heavy cover / series brand with recurring layout

- Cost: **$50–$250** for a template re-setup; each subsequent book in the series costs almost zero, as the template holds.
- This is the "translate the whole template once, then just swap titles" setup. If you're doing a series — or plan to — build the translated version as a *template*, then edit per book.
- Watch: if your series covers contain cover *quotes* ("As seen in...!" or "The #1 thriller of the year"), do not translate claims you can't substantiate in that market. A claim that was true on US stores ("over 50,000 copies sold") can go up in translation IF the number counts global sales (say it: "over 50,000 copies sold worldwide"), and must be re-stated if it counted US-only units. Substantiated numbers — fine to translate with context. Unsubstantiated hype — cut it in every language.

## 6.3 Subtitles: translate, adapt, or re-think?

The subtitle is the most *marketing*-sensitive piece of text in your whole translated edition. A subtitle is a promise + a positioning statement. That means it should be re-thought, not translated. Here's the decision tree:

```
Is your subtitle a "descriptive" subtitle (names the content: "A Practical
Guide to X")?
  → TRANSLATE literally with light polish. Reviewer polish, not a rewrite.

Is your subtitle a "positioned" subtitle (has an angle, a promise, a
target-audience hook: "AI for People Who Hate Jargon")?
  → ADAPT. Ask your reviewer: "How would a book like this be subtitled
    in a bookstore where you live? Give 3 options."
  → Pick the one with the right blend of accuracy + market tone.

Is your subtitle a "hypnotic" subtitle (pure sizzle: "The Book That
Changes Everything")?
  → RE-THINK from scratch for the market. These don't travel; even the
    best translation often lands flat. Cheap to write a new one; expensive
    to launch on a flat one.
```

Examples from the three starter languages from Chapter [01](01-choosing-target-languages.md):

- **Spanish/Latin American:** readers tolerate longer, warmer, more benefit-forward subtitles than US English ones. "Presupuestos para gente ocupada: organización del dinero en 20 minutos a la semana" (a wordy but warm subtitle) is *fine* in Spanish, where in US English it would feel padded. Write the subtitle *for Spanish rhythm.*
- **German:** compound nouns are normal and expected; "Der KI-Leitfaden für alle ohne Vorwissen" is natural. Brevity matters less than *precision* — vague hype subtitles read unserious in the German book market.
- **Japanese:** subtitles often carry a "for whom + what changes" frame with a dash structure (〜のための、〜がわかる本). A native Japanese subtitle writer shortens and restructures description far more aggressively than Latin-script markets allow. Trust your reviewer's restructuring here rather than asking them to translate your line.

Whatever the language, one rule is universal: **the cover subtitle and the store blurb's first line should not say the same sentence.** You have two attention hooks; use both.

## 6.4 Re-layout — does the interior actually need to change?

The honest answer is: **less than you think, more than zero.** A typical English book's EPUB or print interior transfers well structurally. What genuinely needs adaptation:

### 6.4.1 Punctuation and typographic conventions

| English convention | Common in other languages | Fix in layout? |
|---|---|---|
| Quotation marks " " | Spanish « ", German " „ , French « » , Japanese 「 」 | Yes, usually; your reviewer's final file will carry these naturally if they worked in a text editor that uses them. Verify at layout, because some conversions fall back to straight quotes mechanically. |
| Straight apostrophe ' | Curly ' in print-quality books in all languages | Yes — cosmetic but professional. |
| Dates (May 5, 2026) | 5 May 2026 in most of Europe; 2026/05/05 in Japanese | Yes — the reviewing pass and the translator notes should have flagged, but check the layout pass. |
| Decimal separator (1.5) | 1,5 in most of Europe and Latin America | Yes — number errors are rare in AI output but painful when present (a reader seeing a price "1.5" in a German book reads it as 15). |
| Percent spacing (% vs. %) | Most European languages add a space before the % sign | Yes. |
| Narrative section title case | Most non-English languages use sentence case for headings | Your choice — match what the target market's book covers naturally use. Reviewer can tell you. |

### 6.4.2 Length and layout pressure

There is one deep physical fact: **translated text is usually 10–25% longer or shorter than the English original**, depending on language pair (French and Spanish typically expand; Japanese and Chinese often contract). Consequences:

- **Print books: page count changes.** A 280-page book becomes ~310 in Spanish. This affects print cost (KDP's per-page print pricing on your POD rates), and — small thing — it changes your *cover spine width*. Order a fresh template with the correct page count. This is a real re-layout task.
- **Ebooks: mostly no impact.** Reflowable EPUB handles length change invisibly. Fixed-format books (children's, manga, technical) need re-pagination, and panel-length text boxes might not hold the longer text — a fixed-format re-layout is one of the few genuinely labor-intensive tasks in translation.
- **PDF-style products (workbooks, printables):** length changes will break every hard line break. Budget real layout time for these; they're closer to "re-typeset" than "translate."

### 6.4.3 Local conventions you should consider but rarely must adopt

- **Hardcover "reading position" and margins** in German-language prints follow local standards (e.g., German books commonly use different margins and hyphenation settings). For POD through KDP and most local stores, matching exact German print norms is nice-to-have, not required. The exception: if you'll sell into a physical distributor chain worth caring about, hire a local print professional (your reviewer can refer).
- **Reading direction** for Arabic, Hebrew, and books written right-to-left: not just layout mirroring but *entire book flow* — a full re-layout in every sense. This is a specialist job; the budget should reflect it (this contributes to why RTL languages score lower on the Chapter [01](01-choosing-target-languages.md) sheet for first translations).

## 6.5 The right-script font problem (Cyrillic, CJK, Devanagari, Arabic)

A note worth its own half-page when you go beyond Latin-script languages. English fonts — including the font currently on your cover — usually don't cover other scripts, giving your cover text a mismatched "system default" look that reads as obviously foreign to the reader.

Practical options, in ascending cost:

1. **Pick one well-supported local-script font from Google Fonts.** Free, covers most scripts, commercial use cleared. Quality tiers vary; your reviewer or a local designer makes the final call.
2. **Use a mainstream typeface that has a multilingual superfamily.** Companies like Google (Noto family is the big free one) ship each script at a quality standard that looks designed. This is often the best cheap path for a series.
3. **License one commercial local typeface.** Real money ($50–$500+ per weight) but gives your genre's cover a "genuinely local" look. Only worth it when this series is your primary market bet.

None of these is a pure "cost" decision for one book: the practical takeaway is that **non-Latin-script covers are priced like half a design project minimum**, and if you scored a language whose script is hard on the Chapter [01](01-choosing-target-languages.md) sheet, budget this way.

## 6.6 Store images (the ones readers never notice until they're wrong)

Amazon's product page, Google Play, and Apple Books show not just a cover but *images that come with the listing*: series banners, "Look inside" screenshots, and editorial category banners. What needs translation attention:

- **The "Look Inside" preview** is a real reader-item in every market. Make sure the sample chapters Amazon serves (the free preview's opening pages) are your book's *actual* opening pages, which puts the first translated chapter under readers' eyes. Nothing to translate separately — the preview is auto-generated from the file, but double-check it after upload.
- **A+ Content / Enhanced Brand content**, if you use it (available to some authors through Amazon Brand Registry), needs full translation into the target language, including any "chart," "screenshot," or "callout panel" images containing text. If a graphic says "Step 1: Setup," that's cover-supply text and needs the same treatment a cover would.
- **Author photo and bio** carry over fine — but the *bio* text on your author page should be translated in the target language (see Chapter [07](07-marketing-to-readers-abroad.md), section 7.6).

## Bottom line

A translated book has to *look* like it belongs in its market: cover text that survives thumbnail size in the new language, a subtitle adapted rather than translated, punctuation and date/number conventions updated at layout, page count recalculated for print, and — for non-Latin scripts — real font decisions made with a native speaker's help. Keep what makes it yours (cover art, layout template, series branding), change what makes it foreign (embedded English text, US-only conventions, untranslated store page assets). Doing this well is mostly cheap; doing it badly is what makes a good translation read like a bad one.

*Next: [Marketing to Readers Abroad](07-marketing-to-readers-abroad.md) — how readers in the new market find out you exist.*
