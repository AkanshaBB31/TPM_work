// TPM_work portfolio site: theme toggle and table-of-contents highlighting.
(function () {
  var root = document.documentElement, btn = document.getElementById('themeBtn');
  if (btn) btn.addEventListener('click', function () {
    var cur = root.getAttribute('data-theme');
    var dark = cur ? cur === 'dark' : window.matchMedia('(prefers-color-scheme: dark)').matches;
    var next = dark ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('cs-theme', next); } catch (e) {}
  });

  var cur = document.querySelector('.sidenav a[aria-current="page"]');
  if (cur && window.innerWidth <= 760) cur.scrollIntoView({ block: 'nearest', inline: 'center' });

  var links = Array.prototype.slice.call(document.querySelectorAll('.toc a'));
  if (!links.length || !('IntersectionObserver' in window)) return;
  var byId = {};
  links.forEach(function (a) { byId[a.getAttribute('href').slice(1)] = a; });
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) {
        links.forEach(function (a) { a.classList.remove('active'); });
        var a = byId[e.target.id]; if (a) a.classList.add('active');
      }
    });
  }, { rootMargin: '-60px 0px -70% 0px' });
  Object.keys(byId).forEach(function (id) { var h = document.getElementById(id); if (h) io.observe(h); });
})();
