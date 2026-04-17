#!/usr/bin/env python3
"""
Local dev server for thetoddmark-site.
Mimics Cloudflare Pages: maps /work → work.html, /about → about.html, etc.
Run from the site root: python3 scripts/serve.py
"""
import http.server, os, sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 7474
SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=SITE_DIR, **kwargs)

    def translate_path(self, path):
        # Strip query string
        path = path.split('?', 1)[0].split('#', 1)[0]
        # Decode %XX
        import urllib.parse
        path = urllib.parse.unquote(path)

        full = os.path.normpath(os.path.join(SITE_DIR, path.lstrip('/')))

        # Exact file match (images, CSS, JS, etc.)
        if os.path.isfile(full):
            return full

        # Directory → index.html
        if os.path.isdir(full):
            candidate = os.path.join(full, 'index.html')
            if os.path.isfile(candidate):
                return candidate

        # Clean URL: /work → work.html
        candidate = full + '.html'
        if os.path.isfile(candidate):
            return candidate

        # Fallback — let the parent handle it (will 404)
        return full

    def log_message(self, fmt, *args):
        # Quiet: only log non-200s
        if args and str(args[1]) not in ('200', '304'):
            super().log_message(fmt, *args)

if __name__ == '__main__':
    os.chdir(SITE_DIR)
    with http.server.HTTPServer(('', PORT), Handler) as httpd:
        print(f'Serving at http://localhost:{PORT}/')
        print('Press Ctrl-C to stop.')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\nStopped.')
