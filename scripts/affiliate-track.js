// Fire a GA4 event on every affiliate link click.
// All affiliate links open in a new tab (_blank), so no event_callback needed.
(function () {
  document.querySelectorAll('a[href*="thetoddmark-20"]').forEach(function (link) {
    link.addEventListener('click', function () {
      if (typeof gtag !== 'function') return;
      gtag('event', 'affiliate_click', {
        event_category: 'affiliate',
        event_label: link.textContent.trim().slice(0, 100),
        link_url: link.href
      });
    });
  });
})();
