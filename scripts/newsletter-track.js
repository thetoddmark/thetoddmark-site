// Fire a GA4 event when a visitor subscribes via any Buttondown embed form.
// Uses event_callback (GA4's official pattern) so the form only submits
// after GA4 has confirmed the event was dispatched. Falls back to 1s timeout
// in case gtag.js is slow or unavailable.
(function () {
  document.querySelectorAll('.embeddable-buttondown-form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      var submitted = false;
      function doSubmit() {
        if (!submitted) {
          submitted = true;
          form.submit();
        }
      }

      // Fallback: always submit within 1s even if GA4 never responds
      var fallback = setTimeout(doSubmit, 1000);

      if (typeof gtag !== 'function') {
        doSubmit();
        return;
      }

      gtag('event', 'newsletter_signup', {
        event_category: 'engagement',
        event_label: 'buttondown',
        event_callback: function () {
          clearTimeout(fallback);
          doSubmit();
        }
      });
    });
  });
})();
