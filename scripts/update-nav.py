#!/usr/bin/env python3
"""
Nav redesign migration script.
Replaces the flat header nav + footer nav-links with a new dropdown nav.
Run from the site root: python3 scripts/update-nav.py
"""
import re, os, sys

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Which top-level nav item is active on each page
ACTIVE_MAP = {
    'start-here.html': 'start-here',
    'index.html': None,
    'work.html': 'bench',
    'about.html': 'about',
    'contact.html': 'contact',
    'contact-success.html': 'contact',
    'partner.html': 'partner',
    'my-kit.html': 'toolbox',
    'resources.html': 'toolbox',
    'listening.html': 'about',
    'wishlist.html': 'toolbox',
    'shed-upgrade.html': 'about',
    'restorations.html': 'bench',
    'builds.html': 'bench',
    'oddities.html': 'bench',
    'restoration-dresser-refresh.html': 'bench',
    'restoration-bulat-chefs-knife.html': 'bench',
    'restoration-german-perfect-handle.html': 'bench',
    'restoration-imperial-steak-knives.html': 'bench',
    'restoration-awl-marking-knife.html': 'bench',
    'restoration-bridgeport-multitool.html': 'bench',
    'restoration-mac-tools-screwdrivers.html': 'bench',
    'build-chip-breaker-screwdriver.html': 'bench',
    'products.html': None,
    '404.html': None,
}

LOGO_SVG = '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" style="height:38px;width:38px;flex-shrink:0;" aria-label="The Todd Mark logo" role="img">
  <circle cx="50" cy="50" r="47" fill="none" stroke="rgba(245,240,232,0.95)" stroke-width="3.5"/>
  <circle cx="50" cy="50" r="41" fill="none" stroke="rgba(245,240,232,0.45)" stroke-width="1.5"/>
  <circle cx="50" cy="50" r="38" fill="none" stroke="rgba(245,240,232,0.2)" stroke-width="1"/>
  <text x="50" y="36" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="700" fill="rgba(245,240,232,0.95)" text-anchor="middle" letter-spacing="2">THETODD</text>
  <text x="50" y="57" font-family="Arial Black,Arial,sans-serif" font-size="27" font-weight="900" fill="rgba(245,240,232,0.95)" text-anchor="middle" letter-spacing="-1">TM</text>
  <text x="50" y="73" font-family="Arial,Helvetica,sans-serif" font-size="9" font-weight="700" fill="rgba(245,240,232,0.95)" text-anchor="middle" letter-spacing="3">MARK</text>
</svg>'''

YT_SVG = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" style="width:22px;height:22px;" aria-hidden="true"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814z" fill="#FF0000"/><path d="M9.545 15.568V8.432L15.818 12z" fill="#fff"/></svg>'''

def a(key, active):
    return ' nav-active' if active == key else ''

def build_nav(active):
    start   = a('start-here', active)
    bench   = a('bench',   active)
    toolbox = a('toolbox', active)
    abt     = a('about',   active)
    contact = a('contact', active)
    partner = a('partner', active)

    def li_start():
        cls = f' class="nav-active"' if start else ''
        return f'<li{cls}><a href="/start-here">Start Here</a></li>'

    def li_contact():
        cls = f' class="nav-active"' if contact else ''
        return f'<li{cls}><a href="/contact">Contact</a></li>'

    def li_partner():
        cls = f' class="nav-active"' if partner else ''
        return f'<li{cls}><a href="/partner">Partner</a></li>'

    return f'''<nav aria-label="Main navigation">
  <a href="/" class="nav-logo" style="display:flex;align-items:center;text-decoration:none;">{LOGO_SVG}<span style="font-family:'DM Mono',monospace;font-size: 0.75rem;font-weight:400;letter-spacing:0.15em;text-transform:uppercase;color:rgba(245,240,232,0.88);margin-left:0.75rem;white-space:nowrap;">The Todd<span style="color:#c8853a;margin:0 0.15em;">·</span>Mark</span></a>
  <button class="nav-hamburger" id="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav-menu">
    <span></span>
    <span></span>
    <span></span>
  </button>
  <ul id="nav-menu">
    {li_start()}
    <li class="nav-has-dropdown{bench}">
      <button class="nav-dropdown-toggle" aria-expanded="false" aria-haspopup="true">The Bench <span class="nav-chevron" aria-hidden="true"></span></button>
      <ul class="nav-dropdown">
        <li><a href="/work">All Projects</a></li>
        <li><a href="/restorations">Restorations</a></li>
        <li><a href="/builds">Builds</a></li>
        <li><a href="/oddities">Oddities</a></li>
      </ul>
    </li>
    <li class="nav-has-dropdown{toolbox}">
      <button class="nav-dropdown-toggle" aria-expanded="false" aria-haspopup="true">Toolbox <span class="nav-chevron" aria-hidden="true"></span></button>
      <ul class="nav-dropdown">
        <li><a href="/my-kit">What I Use</a></li>
        <li><a href="/resources">Resources</a></li>
        <li><a href="/wishlist">Wishlist</a></li>
      </ul>
    </li>
    <li class="nav-has-dropdown{abt}">
      <button class="nav-dropdown-toggle" aria-expanded="false" aria-haspopup="true">About <span class="nav-chevron" aria-hidden="true"></span></button>
      <ul class="nav-dropdown">
        <li><a href="/about">Mark Todd</a></li>
        <li><a href="/shed-upgrade">The Workshop</a></li>
        <li><a href="/listening">What I&#8217;m Listening To</a></li>
      </ul>
    </li>
    {li_contact()}
    {li_partner()}
    <li><a href="https://www.youtube.com/@TheToddMark" target="_blank" rel="noopener noreferrer" aria-label="Watch on YouTube" style="display:flex;align-items:center;">{YT_SVG}</a></li>
  </ul>
</nav>'''

# ── CSS ────────────────────────────────────────────────────────────────────────
NAV_CSS = """
  /* ── NAV v2: dropdown redesign ── */

  /* Override old nav ul gap/alignment via ID */
  #nav-menu {
    list-style: none;
    display: flex;
    align-items: center;
    gap: 1.75rem;
  }
  #nav-menu > li { list-style: none; }

  /* Dropdown parent */
  .nav-has-dropdown { position: relative; }

  /* Toggle button mimics nav link styling */
  .nav-dropdown-toggle {
    background: none;
    border: none;
    font-family: 'DM Mono', monospace;
    font-size: 0.75rem;
    font-weight: 300;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: rgba(245,240,232,1);
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 0.35em;
    padding: 0;
    line-height: 1;
    transition: color 0.2s;
    white-space: nowrap;
  }
  .nav-dropdown-toggle:hover,
  .nav-has-dropdown:hover > .nav-dropdown-toggle { color: var(--amber-text); }

  /* Active state for dropdown parents and direct links */
  li.nav-active > a { color: var(--amber-text) !important; }
  li.nav-active > .nav-dropdown-toggle { color: var(--amber-text) !important; }

  /* Chevron: CSS triangle */
  .nav-chevron {
    display: inline-block;
    width: 0; height: 0;
    border-left: 3.5px solid transparent;
    border-right: 3.5px solid transparent;
    border-top: 4.5px solid currentColor;
    transition: transform 0.2s;
    flex-shrink: 0;
    margin-top: 1px;
  }
  .nav-dropdown-toggle[aria-expanded="true"] .nav-chevron {
    transform: rotate(180deg);
  }

  /* Desktop dropdown panel (hover + JS open) */
  @media (min-width: 641px) {
    .nav-dropdown {
      position: absolute;
      top: calc(100% + 10px);
      left: 50%;
      transform: translateX(-50%);
      background: rgba(26,20,9,0.98);
      border: 1px solid rgba(200,133,58,0.18);
      border-radius: 3px;
      padding: 0.4rem 0;
      min-width: 190px;
      list-style: none;
      margin: 0;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.15s;
      z-index: 200;
      -webkit-backdrop-filter: blur(8px);
      backdrop-filter: blur(8px);
    }
    /* Invisible bridge: keeps :hover active over the gap between nav item and panel */
    .nav-has-dropdown::after {
      content: '';
      position: absolute;
      top: 100%;
      left: -8px;
      right: -8px;
      height: 12px;
    }
    .nav-has-dropdown:hover .nav-dropdown,
    .nav-has-dropdown.is-open .nav-dropdown {
      opacity: 1;
      pointer-events: auto;
    }
    .nav-dropdown li { list-style: none; }
    .nav-dropdown a {
      display: block;
      padding: 0.45rem 1.2rem;
      font-family: 'DM Mono', monospace;
      font-size: 0.7rem;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: rgba(245,240,232,0.7);
      text-decoration: none;
      white-space: nowrap;
      transition: color 0.15s, background 0.15s;
    }
    .nav-dropdown a:hover {
      color: rgba(245,240,232,1);
      background: rgba(200,133,58,0.08);
    }
    .nav-dropdown a.nav-placeholder {
      color: rgba(245,240,232,0.28);
      cursor: default;
      pointer-events: none;
    }
  }

  /* Mobile: full-screen overlay with inline expanding dropdowns */
  @media (max-width: 640px) {
    #nav-menu {
      display: none;
      position: fixed;
      top: 56px;
      left: 0; right: 0; bottom: 0;
      background: rgba(28,26,23,1);
      flex-direction: column;
      align-items: stretch;
      justify-content: flex-start;
      gap: 0;
      z-index: 300;
      overflow-y: auto;
      padding: 0.75rem 0 2.5rem;
    }
    #nav-menu.nav-open { display: flex; }
    #nav-menu > li { width: 100%; text-align: center; }

    #nav-menu > li > a {
      display: block;
      padding: 0.9rem 2rem;
      font-size: 1.1rem !important;
      letter-spacing: 0.12em;
      color: rgba(245,240,232,1) !important;
      font-weight: 400 !important;
    }
    .nav-dropdown-toggle {
      font-size: 1.1rem !important;
      letter-spacing: 0.12em !important;
      color: rgba(245,240,232,1) !important;
      font-weight: 400 !important;
      padding: 0.9rem 2rem !important;
      width: 100%;
      justify-content: center;
    }
    .nav-dropdown {
      display: none;
      list-style: none;
      margin: 0;
      padding: 0.1rem 0 0.5rem;
      background: rgba(255,255,255,0.04);
    }
    .nav-has-dropdown.is-open .nav-dropdown { display: block; }
    .nav-dropdown a {
      display: block;
      padding: 0.6rem 2rem;
      font-family: 'DM Mono', monospace;
      font-size: 0.75rem;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: rgba(245,240,232,0.6);
      text-decoration: none;
    }
    .nav-dropdown a:hover,
    .nav-dropdown a:focus { color: rgba(245,240,232,0.95); }
    .nav-dropdown a.nav-placeholder { color: rgba(245,240,232,0.25); pointer-events: none; }
  }
"""

# ── JS ─────────────────────────────────────────────────────────────────────────
NAV_JS = """\
<script>
(function() {
  var toggle = document.getElementById('nav-toggle');
  var navUl = document.getElementById('nav-menu');
  if (!toggle || !navUl) return;

  function openMenu() {
    navUl.classList.add('nav-open');
    toggle.classList.add('is-open');
    toggle.setAttribute('aria-label', 'Close menu');
    toggle.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
    var first = navUl.querySelector('a, button');
    if (first) first.focus();
  }
  function closeMenu() {
    navUl.classList.remove('nav-open');
    toggle.classList.remove('is-open');
    toggle.setAttribute('aria-label', 'Open menu');
    toggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
    closeAllDropdowns();
  }
  function closeAllDropdowns() {
    navUl.querySelectorAll('.nav-has-dropdown.is-open').forEach(function(el) {
      el.classList.remove('is-open');
      var btn = el.querySelector('.nav-dropdown-toggle');
      if (btn) btn.setAttribute('aria-expanded', 'false');
    });
  }

  toggle.addEventListener('click', function() {
    navUl.classList.contains('nav-open') ? closeMenu() : openMenu();
  });

  navUl.querySelectorAll('.nav-dropdown-toggle').forEach(function(btn) {
    btn.addEventListener('click', function() {
      var li = btn.closest('.nav-has-dropdown');
      var opening = !li.classList.contains('is-open');
      closeAllDropdowns();
      if (opening) {
        li.classList.add('is-open');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });

  navUl.querySelectorAll('li:not(.nav-has-dropdown) > a').forEach(function(link) {
    link.addEventListener('click', function() { closeMenu(); });
  });
  navUl.querySelectorAll('.nav-dropdown a').forEach(function(link) {
    link.addEventListener('click', function() { closeMenu(); });
  });

  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' || e.keyCode === 27) {
      if (navUl.classList.contains('nav-open')) { closeMenu(); toggle.focus(); return; }
      var openDd = navUl.querySelector('.nav-has-dropdown.is-open');
      if (openDd) {
        openDd.classList.remove('is-open');
        var btn = openDd.querySelector('.nav-dropdown-toggle');
        if (btn) { btn.setAttribute('aria-expanded', 'false'); btn.focus(); }
      }
    }
  });

  document.addEventListener('click', function(e) {
    if (!e.target.closest('.nav-has-dropdown')) closeAllDropdowns();
  });
})();
</script>"""

# ── FOOTER ─────────────────────────────────────────────────────────────────────
# The new footer keeps only copyright/ko-fi/logo; drops the nav-links div.
# (All those links now live in the header dropdown.)

def process_file(path, active_key):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Replace <nav> block
    nav_pattern = re.compile(
        r'<nav\s+aria-label="Main navigation">.*?</nav>',
        re.DOTALL
    )
    new_nav = build_nav(active_key)
    if nav_pattern.search(content):
        content = nav_pattern.sub(new_nav, content, count=1)
    else:
        print(f'  WARNING: no nav block found in {os.path.basename(path)}')

    # 2. Inject new nav CSS before </head>
    # Avoid double-injection if script is re-run
    if '/* ── NAV v2: dropdown redesign ── */' not in content:
        css_block = f'  <style>\n{NAV_CSS}\n  </style>\n'
        content = content.replace('</head>', css_block + '</head>', 1)

    # 3. Replace the nav JS block (works for both IIFE and arrow-function variants)
    script_pat = re.compile(r'<script>([\s\S]*?)</script>', re.DOTALL)

    def replace_nav_script(m):
        body = m.group(1)
        if "getElementById('nav-toggle')" in body or 'getElementById("nav-toggle")' in body:
            return NAV_JS
        return m.group(0)

    content = script_pat.sub(replace_nav_script, content)

    # 4. Remove footer nav-links div (all those links now live in the header)
    footer_links_pat = re.compile(
        r'\s*<div class="footer-links"[^>]*>.*?</div>',
        re.DOTALL
    )
    content = footer_links_pat.sub('', content)

    if content != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    html_files = [f for f in os.listdir(SITE_DIR) if f.endswith('.html')]
    unknown = [f for f in html_files if f not in ACTIVE_MAP]
    if unknown:
        print(f'WARNING: unmapped files (will be skipped): {unknown}')

    changed = 0
    for filename, active_key in ACTIVE_MAP.items():
        path = os.path.join(SITE_DIR, filename)
        if not os.path.exists(path):
            print(f'  SKIP (not found): {filename}')
            continue
        modified = process_file(path, active_key)
        status = 'UPDATED' if modified else 'unchanged'
        print(f'  [{status}] {filename}')
        if modified:
            changed += 1

    print(f'\nDone. {changed} file(s) modified.')


if __name__ == '__main__':
    main()
