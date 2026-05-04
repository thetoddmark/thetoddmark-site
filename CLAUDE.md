# thetoddmark.com — Claude Instructions

## Site Overview
Static HTML/CSS/JS site deployed on Cloudflare Pages. Auto-deploys on push to `main`.
All pages are hand-coded HTML files. No build step, no framework.

## Git Rules
- NEVER use `git add -A` or `git add .` — add files by name only
- NEVER push — the user always runs `git push` manually
- Commit early and often when asked; use descriptive messages

## URL Convention
All internal links and canonical/og:url values use **clean URLs without `.html`**:
- Correct: `/wagner-electrolysis`, `/restoration-stanley-no5half`
- Wrong: `/wagner-electrolysis.html`, `/restoration-stanley-no5half.html`

Cloudflare Pages serves `foo.html` at `/foo` automatically.

## Project Numbering
Projects are numbered sequentially across **all types** (restorations + builds):
- Current highest: **No. 10** (Wagner Ware Sidney-O — wagner-electrolysis)
- Restorations: 01, 02, 04, 05, 06, 07, 09, 10
- Builds: 03 (Chip Breaker), 08 (MCM Dresser)
- Before assigning a number to a new post, grep all HTML files for the current highest `article-eyebrow` number

## CSS Variables (defined in each page's `<style>` block)
```
--amber: #c8853a
--amber-text: #b8732a
--warm-white: #f5f0e8
--ink: #1c1a17
--ink-soft: #4a4540
--ink-faint: #8a8178
--cream: #ede8df
--border: rgba(28,26,23,0.1)
--serif: 'Cormorant Garamond', serif
--body-font: 'Jost', sans-serif
--mono: 'DM Mono', monospace
```
When adding a new page, copy the full `:root` / variable block from an existing post. Always verify that any `var(--xxx)` used in new code is actually defined in that page's `<style>`.

## Amazon Affiliate
Tag: `thetoddmark-20`
Use either `amzn.to` short links or `amazon.com/s?k=...&tag=thetoddmark-20`.

## New Write-Up Checklist
Run through **every item** when adding a new post. Do not skip steps.

### 1. The post file itself
- [ ] `article-eyebrow` uses next sequential number (check existing files first)
- [ ] `<link rel="canonical">` uses clean URL (no `.html`)
- [ ] `<meta property="og:url">` uses clean URL (no `.html`)
- [ ] All `var(--xxx)` CSS variables are defined in the page's `<style>` block
- [ ] Prev/back nav link points to the correct previous project
- [ ] Forward nav slot exists (use a dimmed "Next →" placeholder if no next post yet)

### 2. sitemap.xml
- [ ] Add new `<url>` entry with clean URL and today's date as `<lastmod>`

### 3. work.html
- [ ] Add gallery card at the **top** of `.gallery-grid` (newest first)
- [ ] Update previous top card's position if needed

### 4. restorations.html (restorations only — skip for builds)
- [ ] Add project card at the **top** of the grid (newest first)

### 5. Previous post
- [ ] Update the previous post's forward nav from the dimmed "Next →" placeholder to an actual link to the new post

### 6. index.html — four spots to update
- [ ] **Photo strip**: update if new post should be the featured image (top slot = newest)
- [ ] **Recent Work section**: update if new post should appear here
- [ ] **Latest Write-Up bar**: update number, title, teaser text, and link
- [ ] **Stats counter**: increment "Restorations" or add a new stat type if needed

### 7. Final check
- [ ] `grep -r "\.html" *.html` — confirm no internal links end in `.html`
- [ ] Verify the new post URL works in browser before closing

## Key Files
| File | Purpose |
|------|---------|
| `index.html` | Homepage — photo strip, recent work, latest write-up bar, stats |
| `work.html` | All projects gallery (lightbox cards) |
| `restorations.html` | Restorations-only grid |
| `sitemap.xml` | SEO sitemap — update with every new post |
| `my-kit.html` | Gear/supply list — add product cards when a new post introduces new supplies |

## Product Cards (my-kit.html)
- Use `<picture>` with `.webp` source + `.jpg` fallback when webp is available
- Image size: `width:80px;height:80px;object-fit:contain`
- Grid wrapper uses inline style — there is **no** `.products-grid` CSS class
- Required classes: `product-brand`, `product-name`, `product-desc`, `product-note`
