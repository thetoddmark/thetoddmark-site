/* Shared photo lightbox - click any content photo to view it large.
   Binds to images inside .article-body / .post-body (and anything marked
   [data-lightbox]). Skips images that are already links or buttons, and any
   image marked [data-nozoom]. Injects its own CSS and markup, so a page only
   needs: <script src="/scripts/lightbox.js" defer></script>

   Kept deliberately ASCII-only: this file is served without a charset, so
   literal glyphs would be decoded as Latin-1 and render as mojibake. */
(function () {
  var CONTAINERS = '.article-body, .post-body, [data-lightbox]';
  var imgs = [], cur = 0, lb;

  var CSS = [
    '.lb-backdrop { display:none; position:fixed; inset:0; z-index:1000; background:rgba(28,26,23,0.96); align-items:center; justify-content:center; padding:1.5rem; cursor:zoom-out; }',
    '.lb-backdrop.lb-open { display:flex; }',
    '.lb-inner { position:relative; display:flex; flex-direction:column; align-items:center; cursor:default; max-width:min(90vw,1200px); }',
    '.lb-inner img { display:block; max-width:min(90vw,1200px); max-height:80vh; width:auto; height:auto; object-fit:contain; border-radius:2px; cursor:default; user-select:none; box-shadow:0 8px 48px rgba(0,0,0,0.6); }',
    '.lb-caption { margin-top:0.75rem; font-family:\'DM Mono\',monospace; font-size:0.75rem; letter-spacing:0.1em; text-transform:uppercase; color:rgba(245,240,232,0.55); text-align:center; max-width:640px; line-height:1.6; min-height:1.2em; }',
    '.lb-counter { font-family:\'DM Mono\',monospace; font-size:0.75rem; letter-spacing:0.15em; color:rgba(200,133,58,0.65); margin-top:0.35rem; text-align:center; }',
    '.lb-close { position:fixed; top:1.25rem; right:1.5rem; background:none; border:none; color:rgba(245,240,232,0.5); font-size:1.5rem; line-height:1; cursor:pointer; padding:0.35rem 0.6rem; transition:color 0.2s; z-index:1001; font-family:sans-serif; }',
    '.lb-close:hover { color:#c8853a; outline:none; }',
    '.lb-prev, .lb-next { position:fixed; top:50%; transform:translateY(-50%); background:none; border:none; color:rgba(245,240,232,0.60); font-size:2.5rem; line-height:1; cursor:pointer; padding:1rem 0.9rem; transition:color 0.2s; z-index:1001; user-select:none; font-family:sans-serif; }',
    '.lb-prev { left:0.75rem; }',
    '.lb-next { right:0.75rem; }',
    '.lb-prev:hover, .lb-next:hover { color:#c8853a; outline:none; }',
    '.lb-nav-hidden { visibility:hidden; pointer-events:none; }',
    '.lb-zoomable { cursor:zoom-in; }',
    '@media (max-width:640px) {',
    '  .lb-prev { left:0.15rem; font-size:1.8rem; }',
    '  .lb-next { right:0.15rem; font-size:1.8rem; }',
    '  .lb-close { top:0.6rem; right:0.6rem; }',
    '  .lb-inner img { max-height:70vh; }',
    '}'
  ].join('\n');

  var MARKUP =
    '<button class="lb-close" id="lb-close" aria-label="Close image viewer">\u2715</button>' +
    '<button class="lb-prev" id="lb-prev" aria-label="Previous image">\u2039</button>' +
    '<div class="lb-inner" id="lb-inner">' +
      '<img id="lb-img" src="" alt="" tabindex="0" />' +
      '<div class="lb-caption" id="lb-caption" aria-live="polite"></div>' +
      '<div class="lb-counter" id="lb-counter" aria-live="polite"></div>' +
    '</div>' +
    '<button class="lb-next" id="lb-next" aria-label="Next image">\u203a</button>';

  /* Caption lookup covers both markup conventions used on the site:
     <figure><figcaption> on article pages, .photo-caption on post pages. */
  function captionFor(img) {
    var fig = img.closest('figure');
    if (fig) {
      var fc = fig.querySelector('figcaption');
      if (fc) return fc.textContent.trim();
    }
    var block = img.closest('.photo-block');
    if (block) {
      var pc = block.querySelector('.photo-caption');
      if (pc) return pc.textContent.trim();
    }
    return '';
  }

  function eligible(img) {
    if (img.hasAttribute('data-nozoom')) return false;
    if (img.closest('a, button, [role="button"], [onclick]')) return false;
    if (img.id && img.id.indexOf('lb-') === 0) return false;
    /* Several pages keep hidden <img> elements purely as lightbox data sources. */
    if (img.offsetParent === null || !img.getBoundingClientRect().width) return false;
    return true;
  }

  function open(i) {
    cur = i;
    var img = imgs[i];
    var full = document.getElementById('lb-img');
    full.src = img.currentSrc || img.src;
    full.alt = img.alt || '';
    document.getElementById('lb-caption').textContent = captionFor(img);
    document.getElementById('lb-counter').textContent =
      imgs.length > 1 ? (i + 1) + ' \u2013 ' + imgs.length : '';
    document.getElementById('lb-prev').classList.toggle('lb-nav-hidden', i === 0);
    document.getElementById('lb-next').classList.toggle('lb-nav-hidden', i === imgs.length - 1);
    lb.classList.add('lb-open');
    full.focus();
    document.body.style.overflow = 'hidden';
  }

  function close() {
    lb.classList.remove('lb-open');
    document.body.style.overflow = '';
    if (imgs[cur]) imgs[cur].focus();
  }

  function nav(dir) {
    var next = cur + dir;
    if (next >= 0 && next < imgs.length) open(next);
  }

  function init() {
    /* A page that still carries its own inline lightbox keeps it - don't double-bind. */
    if (document.getElementById('lb')) return;

    var scopes = document.querySelectorAll(CONTAINERS);
    if (!scopes.length) return;
    Array.prototype.forEach.call(scopes, function (scope) {
      Array.prototype.forEach.call(scope.querySelectorAll('img'), function (img) {
        if (eligible(img)) imgs.push(img);
      });
    });
    if (!imgs.length) return;

    var style = document.createElement('style');
    style.textContent = CSS;
    document.head.appendChild(style);

    lb = document.createElement('div');
    lb.className = 'lb-backdrop';
    lb.id = 'lb';
    lb.setAttribute('role', 'dialog');
    lb.setAttribute('aria-modal', 'true');
    lb.setAttribute('aria-label', 'Image viewer');
    lb.innerHTML = MARKUP;
    document.body.appendChild(lb);

    imgs.forEach(function (img, i) {
      img.classList.add('lb-zoomable');
      img.setAttribute('tabindex', '0');
      img.setAttribute('role', 'button');
      img.setAttribute('aria-label', 'View larger: ' + (img.alt || 'photo'));
      img.addEventListener('click', function (e) { e.stopPropagation(); open(i); });
      img.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(i); }
      });
    });

    document.getElementById('lb-close').addEventListener('click', close);
    lb.addEventListener('click', function (e) { if (e.target === this) close(); });
    document.getElementById('lb-prev').addEventListener('click', function (e) { e.stopPropagation(); nav(-1); });
    document.getElementById('lb-next').addEventListener('click', function (e) { e.stopPropagation(); nav(1); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('lb-open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft')  { e.preventDefault(); nav(-1); }
      if (e.key === 'ArrowRight') { e.preventDefault(); nav(1); }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
