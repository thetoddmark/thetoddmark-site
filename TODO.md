# TheToddMark — To-Do List
_Last updated: March 20, 2026_

---

## 🔲 Open Tasks

### 🟠 Medium Priority

#### 2. ~~Fix products.html base64 images~~ — Already clean
- products.html only contains one tiny SVG noise texture (intentional); no JPEG base64 found

#### 3. Organise stray root-level images
- [ ] Move chip-breaker-screwdriver images from repo root into `images/`:
  - `cbd-grain.jpg` (1.2 MB)
  - `cbd-hero.jpg` (1.6 MB)
  - `cbd-inuse.jpg` (2.5 MB)
  - `cbd-planes.jpg` (4.2 MB)
- [ ] Move `mark-portrait.png` (3.7 MB) into `images/` if not already referenced from there
- [ ] Update all `src` references in `build-chip-breaker-screwdriver.html` and `about.html` accordingly
- [ ] Confirm `og-image.jpg`, `favicon.jpg`, and `tm-logo.jpg` in root are intentionally there (some root placement may be required)

---

### 🟡 Lower Priority

#### 5. Add WebP fallback to any remaining plain `<img>` JPEGs
- [ ] Audit all HTML pages for `<img>` tags referencing `.jpg` files directly (not inside `<picture>`)
- [ ] Wrap any found in `<picture><source type="image/webp" ...><img ...></picture>` elements
- [ ] Confirm `.webp` counterparts exist in `images/` for each

#### 6. Remove .DS_Store from repo
- [ ] Check if `.DS_Store` is tracked: `git ls-files --error-unmatch .DS_Store`
- [ ] If tracked: `git rm --cached .DS_Store` then commit
- [ ] Confirm `.gitignore` already includes `.DS_Store` (it does)

#### 7. Sitemap audit
- [ ] Review `sitemap.xml` — last modified dates are from March 2026; confirm all 19 pages are listed
- [ ] Confirm no stale/removed pages remain in the sitemap
- [ ] Update `<lastmod>` dates as needed after any major content changes

---

## ✅ Completed Tasks

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
  - Netlify project (gleeful-lily-f39b5c) deleted
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
