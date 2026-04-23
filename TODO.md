# TheToddMark — To-Do List
_Last updated: April 23, 2026_

---

## 🔲 Open Tasks

### Content
- [ ] **Restoration No. 10** — next write-up when ready

### Analytics & Email
- [ ] **Mark `newsletter_signup` as GA4 key event** — Reminder set for 7:45 AM April 24. Go to GA4 → Admin → Data display → Events → Recent events → click the star next to `newsletter_signup`.

### Growth
- [ ] **Forum thread replies** — 9 Sawmill Creek threads researched and ready to post. Reminder set for Monday April 27. Account pending approval as of April 23 — check email for approval notice before posting.
- [ ] **Additional forum posts (WoodNet + Patriot Woodworker)** — 8 threads found across two forums. Patriot Woodworker account pending approval as of April 23 (same as Sawmill Creek). Check email for approval before posting. Threads:
  - **WoodNet** — [Tool handle finish](https://forums.woodnet.net/showthread.php?tid=7303127) → /restoration-mac-tools-screwdrivers
  - **WoodNet** — [Camellia oil](https://forums.woodnet.net/showthread.php?tid=7336059) → /restoration-stanley-no5half
  - **WoodNet** — [Removing rust from old plane](https://forums.woodnet.net/showthread.php?tid=7342602) → /restoration-stanley-no5half
  - **WoodNet** — [Soak tanks for tool cleanup](https://forums.woodnet.net/showthread.php?tid=7326089) → /restoration-stanley-no5half
  - **WoodNet** — [Marking Knives](https://forums.woodnet.net/showthread.php?tid=7175318) → /restoration-awl-marking-knife
  - **Patriot Woodworker** — [Perfect Handle Screwdriver](https://thepatriotwoodworker.com/forums/topic/23721-perfect-handle-straight-slot-screwdriver/) → /restoration-german-perfect-handle
  - **Patriot Woodworker** — [Electrolysis rust removal](https://thepatriotwoodworker.com/forums/topic/7511-electrolysis-rust-removal/) → /restoration-stanley-no5half
  - **Patriot Woodworker** — [Refurb old Irwin Screwdriver](https://thepatriotwoodworker.com/forums/topic/29345-refurb-old-irwin-screwdriver/) → /restoration-mac-tools-screwdrivers
  - Ask Claude to generate draft replies when ready to post.

---

## ✅ Completed Tasks

### Session: April 2, 2026
- [x] **Buttondown sending domain verified** — added NS records in Cloudflare delegating `mail.thetoddmark.com` to Buttondown (ns1/ns2.onbuttondown.com); both records immediately verified; SPF/DKIM/DMARC/click tracking now managed by Buttondown
- [x] **YouTube backlinks** — added thetoddmark.com link to both video descriptions (Butcher Block Countertop + Channel Trailer already had it)

### Session: March 31, 2026 (continued)
- [x] **Fixed 3 WAVE contrast errors** — raised `.process-desc` opacity, footer visited link opacity, and Mac Tools italic description opacity; remaining 3 WAVE "errors" are confirmed false positives (rgba transparency)
- [x] **Fixed `.about-strip-num` contrast** — changed from `--amber-text` to `--amber` for better contrast on cream
- [x] **Fixed `.btn-ghost` contrast** — added `.about-strip .btn-ghost { color: var(--ink-faint) }` so "Get in Touch" is legible on light background
- [x] **Added YouTube link to footer** — all 19 pages updated
- [x] **Fixed DMARC record** — moved from `_dmarc.mail` to `_dmarc` in Cloudflare DNS
- [x] **Fixed index.html title** — 45 → 52 chars ("& Finds" added)
- [x] **Fixed index.html meta description** — 187 → 155 chars (trimmed to fit 120–160 target)
- [x] **HubSpot score: 89/100** — SEO 30/30, Security 10/10, Performance 29/30; mobile 20/30 is a false positive
- [x] **WAVE: 0 errors, 8.7/10 AIM** — all device-dependent handlers fixed; 3 remaining contrast "errors" are WAVE false positives

### Session: March 31, 2026
- [x] **Set up Cloudflare** — DNS moved from Namecheap nameservers to Cloudflare; CDN active, Browser Cache TTL → 1 month, Crawler Hints on, Always use HTTPS on, 0-RTT + Early Hints enabled, SSL/TLS → Full
- [x] **Shed image mobile srcset** — created `shed-current-1-xs.jpg/webp` at 320×240; added `srcset` + `sizes` to serve xs on ≤600px screens, sm on larger
- [x] **Fixed forced reflow** — removed dead `setVh()` function from index.html (set `--vh` CSS var that was never used anywhere)
- [x] **Fixed LCP preload fetchpriority** — added `fetchpriority="high"` to `<link rel="preload">` for index-hero.webp in index.html `<head>`
- [x] **Fixed all onmouseover/onmouseout event handlers site-wide** — replaced inline JS hover handlers with CSS `:hover` classes across all 14 affected HTML files; zero remaining instances
- [x] **Fixed rotated photo** — `shed-current-3.jpg/webp` was stored landscape (EXIF rotation stripped during prior resize); rotated 90° CW to correct portrait orientation; updated width/height in shed-upgrade.html

### Session: March 30, 2026
- [x] **Fixed sub-12px font sizes site-wide** — replaced all 0.55–0.72rem values with 0.75rem across all 19 HTML files
- [x] **Fixed amber-text contrast on dark backgrounds** — injected CSS cascade rule scoping `--amber-text: var(--amber)` to `nav`, `footer`, and `[style*="background:var(--ink)"]` elements; `--amber` (#c8853a) is 5.46:1 on `--ink`, passing WCAG AA
- [x] **Fixed rgba transparent color contrast** — replaced low-opacity inline colors across 11 HTML files: `rgba(200,133,58,0.6)→0.9`, `rgba(245,240,232,0.35)→0.6`, `rgba(245,240,232,0.4)→0.6`, `#6a6058→#a09080`
- [x] **Optimized shed LCP image** — resized shed-current-1-sm.jpg/webp from 600×450 to 520×390 (webp: 70→46 KiB, 34% savings); removed `loading="lazy"`, added `fetchpriority="high"`; LCP improved 3.9s → 1.7s; PageSpeed desktop 87 → 99
- [x] **Installed Microsoft Clarity** (project ID: `w41lq1gqm2`) on all 19 HTML pages — session recording and heatmaps now active

---

## ✅ Completed Tasks

### Session: March 23, 2026 (continued — SEO/meta pass + nav fix)
- [x] **Fixed partner.html and shed-upgrade.html nav** — both used old `nav ul a` CSS (0.62rem/400wt, 2rem gap, mobile overlay at top:0); updated to canonical `nav a` (0.7rem/300wt, 2.5rem gap, overlay at top:56px); added missing `.nav-logo` and `.nav-hamburger span` styles; removed redundant mobile hamburger span rules
- [x] **Added og:image + twitter:image to partner.html** — was the only page missing social preview image
- [x] **Fixed JSON-LD broken string in restoration-german-perfect-handle.html** — curly-quote `"Perfect Handle"` inside JSON string was terminating the field early; fixed with Unicode escapes; description now complete
- [x] **Fixed malformed JSON-LD in 404.html** — JS compatibility block was inside the `<script type="application/ld+json">` tag (missing closing `</script>`); split into two separate script tags
- [x] **Fixed shed-upgrade.html meta description** — replaced `&times;` and `&prime;` HTML entities with plain text (entities don't render in social previews)
- [x] **Validated all 24 JSON-LD blocks** across all pages — all pass JSON.parse

### Session: March 23, 2026 (continued — accessibility & contrast pass)
- [x] **Fixed h1→h3 heading hierarchy skip** in work.html (7 card-titles h3→h2) and products.html (5 section headers h3→h2); both pages now h1→h2 clean
- [x] **Added missing width/height attributes** to 195 img tags across 12 pages — eliminates CLS-causing layout shifts; zero images skipped (all dims resolved from files)
- [x] **Fixed color contrast site-wide** — added `--amber-text: #a0621a` to `:root` on all 19 pages; replaced 421 `color: var(--amber)` text uses with `color: var(--amber-text)`; ratio on cream improves 2.69:1 → 4.65:1 (WCAG AA ✅); decorative/background/border uses of `--amber` unchanged

### Session: March 23, 2026 (continued — image resizing pass)
- [x] **Resized 60 restoration article images** across 7 pages — all images >1600px wide shrunk to 1600px max; WebP regenerated in-place; **~84 MB total freed**
  - German Perfect Handle: ph-tools-arrival, ph-before-wood, ph-before-blade, ph-before-closeup + all 40 other ph-* images
  - Awl/Marking Knife: 5 finished photos (4032→1600px)
  - Bulat chef's knife: 6 images (2048–3086px → 1600px)
  - Chip Breaker Screwdriver build: 8 cbd-* images including cbd-inuse (4284px), cbd-kit-* (4157–3675KB → 200–400KB)
  - Bridgeport Multitool: 2 images (1908→1600px)
- [x] **Resized 9 product thumbnail images** in products.html — 400–748px → 160px (2× retina for 80px display); scotchbrite-pads alone 257KB → 7KB
- [x] **Resized shed-current-1.jpg for index.html** — created `shed-current-1-sm.jpg` at 600×450px (2400px original); updated index.html to use `<picture>` with small variant

### Session: March 23, 2026 (continued — index.html base64 extraction)
- [x] **Extracted 8 base64 images from index.html** — HTML file 1,152 KB → 84 KB (−1,043 KB, 93% reduction)
  - Hero logo: `data:image/jpeg;base64` → `images/index-hero.jpg` + `.webp`; wrapped in `<picture>`
  - 7 Mac Tools lightbox photos: extracted as `images/index-mac-before1/2`, `index-mac-mid1/2`, `index-mac-after1/2/3` (jpg + webp)
- [x] **Fixed hero image LCP** — removed `loading="lazy"` and `decoding="async"`; added `fetchpriority="high"` and `width`/`height` attributes
- [x] **Added `<link rel="preload">` for hero image** in `<head>` — browser fetches it at parse time
- [x] **Fixed malformed `lb-main-img` tag** in index.html — stray `/ loading="lazy"` removed (same fix previously done in work.html and products.html)

### Session: March 23, 2026 (continued — Lighthouse pass)
- [x] **Removed `loading="lazy"` from `bpmt-gallery-img`** in work.html — was LCP element causing 18,410ms element render delay
- [x] **Added missing `alt` attributes** to `cbd-gallery-img`, `sd-gallery-img`, `mac-gallery-img` in work.html; fixed stray `/ ` malformed self-closers
- [x] **Removed Cloudflare email-decode.min.js 404 script** from 9 pages — leftover from Netlify migration
- [x] **Converted Google Fonts to async preload** on all 19 pages — eliminates ~1,850ms render-blocking per page; `rel="preload" as="style"` + onload swap + noscript fallback

### Session: March 23, 2026 (continued)
- [x] **Fixed double-nested `<picture>` bug in products.html** — 4 product cards (Walrus Oil, Fiebing's, Renaissance Wax, Oxalic Acid) had broken outer `<picture>` wrapper with no `<img>`; removed duplicates
- [x] **Fixed malformed `lb-main-img` tag in products.html** — stray `/ loading="lazy"` was self-closing the tag; same issue previously fixed in work.html
- [x] **Resized cbd-planes.jpg to 2400px wide** — 4.2 MB → 1.2 MB JPG; WebP regenerated 1.6 MB → 680 KB
- [x] **Resized shed-current-*.jpg to 2400px wide** — 3.8–5.5 MB → 811 KB–1.4 MB JPG; WebP regenerated 1.1–2.3 MB → 280–762 KB
- [x] **Deleted yt-avatars.json** — confirmed no references anywhere; removed dead weight from repo

### Session: March 23, 2026
- [x] **Organised stray root-level images** — moved cbd-*.jpg and mark-portrait.png into `images/`
  - Updated `src` references in `build-chip-breaker-screwdriver.html` and `about.html`
  - Updated og:image/twitter:image absolute URLs for cbd-planes.jpg
  - Confirmed `favicon.jpg`, `og-image.jpg`, `tm-logo.jpg` intentionally remain in root
  - `.DS_Store` removed from git tracking (already in .gitignore)
- [x] **Generated WebP versions** for all 21 images that lacked `.webp` counterparts
  - cbd-*.jpg, resources-photo-*.jpg, shed-*.jpg all now have WebP pairs
  - HTML `<picture>` elements were already in place — WebP files just needed to exist
- [x] **Sitemap updated** (`sitemap.xml`)
  - Added 3 missing pages: `restoration-bulat-chefs-knife`, `restoration-imperial-steak-knives`, `shed-upgrade`
  - Updated `<lastmod>` dates across all 17 pages to reflect recent sessions
- [x] **WebP fallback audit complete** — all img tags already wrapped in `<picture>` elements

### Session: March 20, 2026
- [x] **Replaced base64 images in resources.html** — 1.2 MB → 97 KB (92% reduction)
  - 15 YouTube creator avatars replaced with YouTube CDN URLs (`yt3.googleusercontent.com`)
  - 7 lightbox restoration photos extracted as real `.jpg` files in `images/`
  - `yt-avatars.json` identified as unused file (not referenced anywhere)
- [x] **Migrated hosting from Netlify to GitHub Pages**
  - CNAME file already present in repo (`thetoddmark.com`)
  - GitHub Pages enabled: Deploy from branch → main → / (root)
  - DNS updated at Namecheap: 4 GitHub A records + www CNAME → thetoddmark.github.io
  - SSL cert issued, Enforce HTTPS enabled
  - Site confirmed live at https://thetoddmark.com
  - Netlify project (gleeful-lily-f39b5c) deleted; plan downgraded to free
  - PROJECT-NOTES.md updated to reflect GitHub Pages as deploy method
- [x] **Fixed nav bar height inconsistency** on `partner.html` and `shed-upgrade.html`
  - Both pages used `padding: 0.85rem 2.5rem` without an explicit height
  - All other pages use `height: 64px; padding: 0 3rem` — applied same to both affected pages
  - Nav is now consistent at 64px across the entire site

### Session: March 19, 2026
- [x] **Hamburger menu keyboard navigation** overhauled across all 19 pages
  - Escape key closes menu and returns focus to toggle
  - Opening menu moves focus to first nav link
  - Tab key trapped within open menu (Shift+Tab returns to toggle)
  - Body scroll locked when menu open, restored on close
  - `aria-expanded` properly managed on all implementations
- [x] **Fixed malformed `loading` attribute** on 15 hidden lightbox `<img>` tags in work.html

### Session: March 18, 2026
- [x] Added Restoration No. 09 (`restoration-bulat-chefs-knife.html`) — Bulat Damascus chef's knife
- [x] Added 5 belt sander update photos + new Section 06 to German Perfect Handle article
- [x] Products page: added Bucktool belt sander + non-woven belts; upgraded 4 existing tool cards with Amazon affiliate links
- [x] Products page: removed duplicate unlinked DeWalt card; reordered What I Use section
- [x] Resources page: fixed 3 broken YouTube links; added The Wood Whisperer card; merged section 04 into section 03
- [x] Resources page: fixed wrong avatar images for A Plane Life and Gordon Addison
- [x] work.html: added Bulat gallery card + lightbox JS entry; JSON-LD updated to 11 items
- [x] index.html: Bulat added as first Recent Work item; stat updated 6 → 7 Restorations
- [x] All write-up pages: reduced dark hero header height (7rem → 5rem top padding)
- [x] Bulat article: fixed title visibility, moved hero photo, corrected rivets description, added lightbox
