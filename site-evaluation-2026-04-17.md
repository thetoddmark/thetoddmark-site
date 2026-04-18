# The Todd·Mark — Master Site Evaluation & Improvement Document

*Compiled April 17, 2026 — incorporates three multi-agent evaluations + visual design critique*

---

## VISUAL DESIGN CRITIQUE

### 1. Homepage Structure

The 50/50 hero split (text left, illustration right) is a confident layout choice, but the illustration side is underworked. The hand-plane SVG is elegant, but `<div class="hero-visual">` is just a `background: var(--cream)` slab with two radial gradient overlays. Nothing in it communicates craft, texture, or workshop atmosphere. Visitors who arrive without prior context are reading copy before they've seen a single real object. **The right half of your homepage should show a photo, not a diagram.**

The stats strip is strong conceptually — five concrete claims at a glance. The WA state SVG map is a nice touch. The weakness is that "$0 New Tools Purchased" has no framing. Without knowing the site, a visitor doesn't know if that's a boast, a constraint, or a joke. One additional word ("Budget: $0 New Tools") would resolve it.

The homepage sells categories (Restorations, Builds, Oddities) before it sells the person. There's no face, no voice, no "why this person, why these objects" moment until the About strip near the bottom. That strip exists but arrives too late and says too little.

### 2. Retention Engine

The site has a retention problem built into its structure. After reading any project page, there's no **next project** prompt, no **you might also like**, and the newsletter CTA only appears in the footer — the lowest-attention zone on any page. The post-project moment, after someone has read 800 words and seen all the photos, is when they're most likely to subscribe. That's where the newsletter form should be.

The "Supplies Used" section in restorations is smart — it's exactly where a reader wants to know what you used. But there are no Amazon affiliate links in at least two of those sections (Bridgeport multitool, Imperial steak knives). That's leaving the most natural conversion moment empty.

### 3. Typography

The type hierarchy is genuinely well done. Cormorant Garamond at `clamp(3rem, 5vw, 5rem)` for the hero title reads as editorial without feeling precious. DM Mono for labels at `0.75rem` with `0.12–0.22em` letter-spacing is controlled and legible. Jost 300 at 1rem/1.7 line-height for body is comfortable.

The only crack: `--ink-faint` is defined two different ways across the site. Hub pages (index.html) set it as `#6b6358` (a warm-gray hex); category/project pages (restorations, builds) define it as `rgba(28,26,23,0.5)` — which renders as a cooler, flatter gray. These are visually different. Any element using `--ink-faint` across page types will look slightly different. Not noticeable at a glance, but it's an inconsistency in a system that otherwise shows real attention to color.

### 4. Color & Texture

The amber/ink/cream palette is cohesive and clearly intentional. The noise texture overlay (`body::before` with an inline SVG feTurbulence) is a smart detail — adds grain without loading an image file. The amber gradient accents on dark backgrounds (page-headers) are restrained and effective.

The one missed opportunity: the `hero-visual` right panel is a flat cream slab. It's the largest unbroken area of color on the homepage and it's doing nothing. A real photograph here — even at 50% opacity over the cream — would transform the first impression.

### 5. Spacing

Section padding at `7rem 5rem` on desktop is generous and confident. The 5-column stats strip at full width is appropriately dense. The project card grids (`repeat(2, 1fr)` with `2rem` gap on category pages) feel right.

The one tight spot is mobile — at 768px, the stats strip drops to `repeat(2, 1fr)`, which means 5 stats across 2 columns leaves one item on its own row. That orphaned stat (whichever falls last) will look slightly odd. Worth checking which stat ends up alone and whether it's the right one to be visually isolated.

### 6. Photography

The photography is the strongest asset on the site and the most under-displayed. Card images use `aspect-ratio: 3/2` with `object-fit: cover`, which is correct. But `transition: transform 0.4s ease` on hover scale (1.03) is subtle to the point of barely registering — could go to 1.05 for more presence.

The oddities.html feature images now sit side-by-side correctly, but they lack `width` and `height` attributes, causing layout shift during load. This is the only remaining CLS issue confirmed from source.

### 7. Visual Hierarchy

The amber `→` links (`.proj-card-link`) are correctly subdued as secondary elements. The amber-text color on DM Mono labels is a clean system. The section numbering (`01 —`, `02 —`) adds structure without being heavy.

The page headers (dark background, amber eyebrow, white serif title, muted subtitle) are consistent across all category pages — good system discipline.

### 8. Craft Details

Strengths worth keeping:
- `border-top: 1px solid var(--border-warm)` on card bodies (the amber-tinted border) is a lovely detail
- Reveal animations (translateY 18px, 0.55s ease) are tasteful and don't interfere
- The noise texture layer is good craft
- `will-change: transform, opacity` cleanup after animation completes shows real attention

Weaknesses:
- The nav JS (~70 lines of IIFE) is duplicated in every single HTML file. It works, but it's ~14KB of redundant script per page.
- `image-rendering: crisp-edges` on all images is wrong for photography — that property is for pixel art. It may subtly degrade photo rendering in some browsers. Remove it or scope it only to SVG/icon elements.

### 9. Mobile Aesthetic

The hamburger menu, mobile nav drawer, and breakpoints at 768px and 480px are well-executed for a hand-built site. The one technical risk is `build-chip-breaker-screwdriver.html` — its photo grid uses `minmax(180px,1fr)` which may not collapse properly at 375px (iPhone SE). Worth verifying at that viewport.

### Homepage Redesign Blueprint

If you want to evolve the homepage without rebuilding it:

1. **Replace the SVG illustration with a real photograph** in `.hero-visual`. Best candidate: a high-contrast shop scene or a single beautifully lit restored tool. The current cream slab with two gradient overlays is a placeholder aesthetic.

2. **Move the About strip earlier.** Currently it appears below the Restorations and Builds sections. It should be the second section, immediately after the stats strip — you want the visitor to understand who's doing this before they see the portfolio.

3. **Add a newsletter module to the homepage** between the about strip and the footer. Current implementation only surfaces Buttondown in the footer. One inline signup block mid-page would meaningfully increase subscriber conversion.

4. **Add an "as seen in" or credential line** to the hero. Even "Seen on Reddit's r/handtools" or "Covering the Pacific Northwest maker scene since 2025" establishes authority immediately. Right now the hero copy is confident but unanchored.

---

## MASTER IMPROVEMENT PLAN

### TIER 1 — Quick Wins (hours, not days)

**1. Add `<meta name="description">` to index.html**
The homepage is the only page missing a meta description. Every other page has one. This is the single highest-impact SEO gap on the site. Target: 150–160 characters, include "vintage tool restoration," "Seattle," and "The Todd·Mark."

**2. Add Amazon affiliate links to two restoration pages**
- `restoration-bridgeport-multitool.html` — Supplies Used section exists, links missing
- `restoration-imperial-steak-knives.html` — same
Use tag `thetoddmark-20`. Both pages have the structural container. Just needs the product links.

**3. Add `og:image` to restorations.html and oddities.html**
Both pages are missing Open Graph image tags. Social shares will show no preview image. Use the best project photo you have. Format: `<meta property="og:image" content="https://thetoddmark.com/images/[filename]">`.

**4. Add `width` and `height` to oddities.html feature images**
`rca-victor-before.png` and `rca-victor-render.png` have no explicit dimensions. This causes layout shift during load (CLS). Add actual pixel dimensions to both `<img>` tags.

**5. Fix `image-rendering: crisp-edges` on photography**
In index.html's cross-browser compat block, `image-rendering: crisp-edges` applies to all images via the `img` selector. This is meant for pixel art, not photographs. Remove it or scope it to `.icon, svg` only.

---

### TIER 2 — Medium Effort (days)

**6. Add newsletter signup to category pages**
restorations.html, builds.html, and oddities.html should each have an inline Buttondown signup block — not just a footer link. Best placement: just above the footer, or between the card grid and footer. The current footer-only position is the lowest-conversion location possible.

**7. Add newsletter signup immediately after Supplies Used on project pages**
Every restoration article's "Supplies Used" section is a conversion moment. The reader has just finished the project and wants to know what you used — they're already engaged. A single inline signup ("Get notified when the next restoration drops") placed *after* the supplies list would outperform the footer CTA.

**8. Consolidate `--ink-faint` CSS variable**
Hub pages: `--ink-faint: #6b6358` (hex)
Category/project pages: `--ink-faint: rgba(28,26,23,0.5)` (rgba)
These render differently. Pick one and apply it across all files. The hex `#6b6358` is the warmer, more intentional value — the rgba version was likely a copy-paste from a different variable. Recommend standardizing on `#6b6358`.

**9. Rewrite builds.html intro copy**
Current subtitle: "Kit builds, fabrications, and hands-on project work. The kind of thing you want or need — around the house or to freshen things up." — This is generic placeholder copy. The builds category needs a real voice, same energy as the restorations header. Describe the *posture* behind the builds (utility over aesthetics, made from available materials, workshop-first thinking, etc.).

**10. Add metrics and one integration example to partner.html**
Brand managers making partnership decisions need numbers. If you can share even a range ("X monthly readers," "X newsletter subscribers," "X YouTube subscribers"), add it to the partner page. One concrete past integration example ("I incorporated Brand X's finishing oil into a knife restoration and linked from the supplies section") would significantly increase inquiry-to-deal conversion.

**11. Replace SVG illustration with a photograph in the hero**
The `.hero-visual` right panel currently shows a cream background with gradient overlays. A real workshop photo here would transform the first impression. See Design Critique §1 above.

**12. Externalize the navigation JavaScript**
The ~70-line nav dropdown IIFE is copy-pasted into every HTML file. This is ~14KB of redundant script across ~25 pages. Create a `/nav.js` file, load it with `<script src="/nav.js" defer></script>`. Reduces per-page weight, centralizes any future nav changes.

**13. About page — rewrite around the WHY**
The current about.html doesn't answer the most important question: why vintage tools specifically? What happened that made Mark Todd start picking up old, neglected objects and restoring them? The origin moment — the first tool, the first estate sale, the realization — is the hook that makes this a site about something rather than just a portfolio. One specific anecdote beats three paragraphs of general description.

---

### TIER 3 — Significant Investment (weeks)

**14. Add previous/next navigation to individual project pages**
Currently there's no way to navigate between projects from a project page — you have to go back to the category page. A simple `<nav class="project-nav">` with Previous and Next links at the bottom of each article would dramatically increase pages-per-session.

**15. Document at least one failure**
Every project on the site currently succeeds. Every restoration comes out clean. This is aesthetically satisfying but slightly incredible — it reads as curated perfection rather than authentic documentation. One project where something went wrong (warped handle, metal too far gone, finish that didn't take), documented honestly, would make every other project more believable. It's also more interesting to read.

**16. Serialized project journal for Oddities**
The RCA Victor radio is in-progress. The current oddities.html page acknowledges this but treats it as a holding page. Consider starting a proper build thread *now*, even with just 2-3 photos and a few hundred words of process notes. The "follow along" mechanic — new entry, then newsletter or social notification — is how you build a returning audience rather than a one-visit readership.

**17. Replace the hero illustration with a photo**
The hand-plane SVG is a placeholder aesthetic — functional but not emotionally resonant. A real photograph of the workshop, a finished tool, or the process would communicate everything the current hero attempts to describe.

---

### ONGOING

**18. Google Search Console monitoring**
Sitemap resubmitted April 17, 2026. Over the next 2–4 weeks, watch for:
- Index coverage (all 22 URLs indexed, none flagged)
- Core Web Vitals (especially CLS from the oddities images)
- Any mobile usability issues flagged at 375px

**19. Affiliate link hygiene**
As new restoration articles are published, add Amazon Associates links (tag: `thetoddmark-20`) to Supplies Used sections at time of writing, not retroactively. The two existing gaps (Bridgeport, Imperial steak knives) are worth going back to fix, but establishing the habit forward is the real goal.

**20. Newsletter cadence**
Buttondown is in place but the signup CTA is currently footer-only. Until the inline newsletter modules are added (see items 6 and 7), any traffic arriving at a project page has almost no way to subscribe unless they scroll to the very bottom. Prioritize the inline modules.

---

## WHAT'S ALREADY DONE (April 17, 2026 session)

- Stats strip: 5-column layout, WA state map at 170%, correct order
- Oddities: new body copy, side-by-side images, Reddit link in status bar, centered feature card and coming-soon section
- RCA Victor images: renamed from spaces/wrong extension, src updated in HTML
- work.html + resources.html: `alt=""` added to all hidden preload and lightbox images
- start-here.html: `og:url` added
- sitemap.xml: 4 missing pages added, lastmod dates updated
- Google Search Console: sitemap resubmitted successfully
- Deployment confirmed: GitHub Pages auto-deploys from main merge in ~3 minutes; Cloudflare is DNS-only proxy

---

*Priority order for next session: item 1 (meta description) → item 2 (affiliate links) → item 3 (og:image) → item 4 (image dimensions) → items 6/7 (newsletter placement).*
