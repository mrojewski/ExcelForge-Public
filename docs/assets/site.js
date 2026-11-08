(() => {
  'use strict';
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#navigation');
  if (!toggle || !nav) return;

  const mobile = window.matchMedia('(max-width: 900px)');
  const links = [...nav.querySelectorAll('a[href]')];
  const sections = new Map();
  for (const link of links) {
    if (link.origin === location.origin && link.pathname === location.pathname &&
        link.search === location.search && link.hash) {
      const section = document.getElementById(link.hash.slice(1));
      if (section) sections.set(link, section);
    }
  }

  // Without JS, navigation stays visible. Enhanced mobile navigation is a disclosure.
  nav.dataset.enhanced = 'true';
  toggle.hidden = false;
  function setMenu(open) {
    toggle.setAttribute('aria-expanded', String(open));
    nav.hidden = mobile.matches && !open;
  }
  function syncMenu() {
    const focused = document.activeElement;
    setMenu(false);
    if (mobile.matches && nav.contains(focused)) toggle.focus();
    if (!mobile.matches && focused === toggle) links[0]?.focus();
  }
  toggle.addEventListener('click', () => setMenu(toggle.getAttribute('aria-expanded') !== 'true'));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && mobile.matches && !nav.hidden) {
      setMenu(false);
      toggle.focus();
    }
  });
  document.addEventListener('click', event => {
    if (mobile.matches && !nav.hidden && !event.target.closest('.site-header')) setMenu(false);
  });
  links.forEach(link => link.addEventListener('click', event => {
    if (!mobile.matches || event.defaultPrevented || event.button !== 0 ||
        event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;

    setMenu(false);
    const section = sections.get(link);
    if (section) {
      section.setAttribute('tabindex', '-1');
      section.focus({ preventScroll: true });
    }
  }));
  mobile.addEventListener('change', syncMenu);
  syncMenu();
  if (!sections.size) return;

  // Track section starts, including the long Guardian overview and the page end.
  const sectionLinks = [...sections.keys()];
  let scheduled = false;
  function updateCurrent() {
    const threshold = document.querySelector('.site-header').getBoundingClientRect().height + 48;
    let active = sectionLinks[0];
    sections.forEach((section, link) => {
      if (section.getBoundingClientRect().top <= threshold) active = link;
    });
    if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 2) {
      active = sectionLinks[sectionLinks.length - 1];
    }
    sectionLinks.forEach(link => {
      if (link === active) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
    scheduled = false;
  }
  function scheduleUpdate() {
    if (!scheduled) {
      scheduled = true;
      window.requestAnimationFrame(updateCurrent);
    }
  }
  window.addEventListener('scroll', scheduleUpdate, { passive: true });
  window.addEventListener('resize', scheduleUpdate);
  window.addEventListener('hashchange', scheduleUpdate);
  updateCurrent();
})();
