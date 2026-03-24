# TheToddMark — To-Do List
_Last updated: March 23, 2026_

---

## 🔲 Open Tasks

### Lighthouse — Remaining Performance Wins
_(all performance items complete — awaiting new audit results)_

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
