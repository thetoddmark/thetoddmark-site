// Fire a GA4 event when a visitor subscribes via any Buttondown embed form.
// Intercepts submit, fires the event, then waits 300ms before allowing navigation.
(function () {
  document.querySelectorAll('.embeddable-buttondown-form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      if (typeof gtag !== 'function') return;
      e.preventDefault();
      gtag('event', 'newsletter_signup', {
        event_category: 'engagement',
        event_label: 'buttondown'
      });
      setTimeout(function () { form.submit(); }, 300);
    });
  });
})();
