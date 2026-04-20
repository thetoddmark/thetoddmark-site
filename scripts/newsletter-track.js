// Fire a GA4 event when a visitor subscribes via any Buttondown embed form.
// Uses transport_type:'beacon' so the event sends before the page navigates away.
(function () {
  document.querySelectorAll('.embeddable-buttondown-form').forEach(function (form) {
    form.addEventListener('submit', function () {
      if (typeof gtag !== 'function') return;
      gtag('event', 'newsletter_signup', {
        event_category: 'engagement',
        event_label: 'buttondown',
        transport_type: 'beacon'
      });
    });
  });
})();
