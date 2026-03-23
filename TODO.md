# TheToddMark — To-Do List
_Last updated: March 23, 2026_

---

## 🔲 Open Tasks

### 🟡 Lower Priority

#### 1. Compress cbd-planes.jpg (still large even as WebP)
- `cbd-planes.webp` is 1.7 MB — consider resizing to max 2400px wide before re-converting
- Other cbd-*.webp files are reasonable (294–582 KB)

#### 2. Audit shed-current-*.jpg images for resize opportunity
- These are 3–5 MB JPGs (1.2–2.4 MB as WebP) — likely far larger than needed for web display
- Consider resizing to max 2400px wide to reduce file sizes further

#### 3. Consider removing yt-avatars.json
- File contains base64 avatar data for 8 creators but is not referenced by any HTML or JS
- Either delete it or repurpose it — currently dead weight in the repo

---

## ✅ Completed Tasks

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
