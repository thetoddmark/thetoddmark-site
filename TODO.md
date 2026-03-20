# TheToddMark — To-Do List
_Last updated: March 20, 2026_

---

## 🔲 Open Tasks

### 🔴 High Priority

#### 1. Migrate from Netlify to GitHub Pages
Steps (in order):
- [ ] Add a `CNAME` file to the repo root containing: `thetoddmark.com`
- [ ] On GitHub.com: go to repo **Settings → Pages → Source → Deploy from branch → main → / (root)**
- [ ] Set custom domain to `thetoddmark.com` in GitHub Pages settings
- [ ] Update DNS at your registrar/host:
  - Add 4 A records pointing to GitHub Pages IPs:
    `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
  - Add a CNAME record: `www` → `<yourgithubusername>.github.io`
- [ ] Wait for GitHub to issue SSL cert (up to 24 hours; usually under 1 hour)
- [ ] Verify site loads correctly at https://thetoddmark.com
- [ ] Verify www.thetoddmark.com redirects to thetoddmark.com
- [ ] Delete or archive the Netlify project (gleeful-lily-f39b5c)
- [ ] Update PROJECT-NOTES.md to reflect new deploy method
- [ ] Note: `_redirects` is a Netlify-specific file — it does nothing on GitHub Pages (safe to leave, harmless)

---

### 🟠 Medium Priority

#### 2. Fix products.html base64 images
- [ ] Audit all base64-encoded images in `products.html` (currently 87 KB file)
- [ ] Export each base64 image as an external `.jpg` + `.webp` file into `images/`
- [ ] Replace inline base64 `<img src="data:...">` with `<picture>` elements using WebP + JPEG fallback
- [ ] Verify all product images render correctly after replacement

#### 3. Organise stray root-level images
- [ ] Move chip-breaker-screwdriver images from repo root into `images/`:
  - `cbd-grain.jpg` (1.2 MB)
  - `cbd-hero.jpg` (1.6 MB)
  - `cbd-inuse.jpg` (2.5 MB)
  - `cbd-planes.jpg` (4.2 MB)
- [ ] Move `mark-portrait.png` (3.7 MB) into `images/` if not already referenced from there
- [ ] Update all `src` references in `build-chip-breaker-screwdriver.html` and `about.html` accordingly
- [ ] Confirm `og-image.jpg`, `favicon.jpg`, and `tm-logo.jpg` in root are intentionally there (some root placement may be required)

#### 4. Replace base64 YouTube avatars in yt-avatars.json
- [ ] Audit `yt-avatars.json` — currently contains base64 avatar data for 8 creators
- [ ] Replace each base64 blob with a direct YouTube CDN avatar URL (pattern already established for A Plane Life and Gordon Addison)
- [ ] Verify avatars still load on `resources.html`

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
