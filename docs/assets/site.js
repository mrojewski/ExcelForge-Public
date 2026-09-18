(() => {
  'use strict';
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#navigation');
  const mobile = window.matchMedia('(max-width: 900px)');
  const links = [...nav.querySelectorAll('a')];
  const sections = links.map(link => document.querySelector(link.hash));

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
    if (!mobile.matches && focused === toggle) links[0].focus();
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
  links.forEach(link => link.addEventListener('click', () => {
    if (mobile.matches) {
      setMenu(false);
      const section = document.querySelector(link.hash);
      section.setAttribute('tabindex', '-1');
      section.focus({ preventScroll: true });
    }
  }));
  mobile.addEventListener('change', syncMenu);
  syncMenu();

  // Track section starts, including the long Guardian overview and the page end.
  let scheduled = false;
  function updateCurrent() {
    const threshold = document.querySelector('.site-header').getBoundingClientRect().height + 48;
    let active = sections[0];
    sections.forEach(section => {
      if (section.getBoundingClientRect().top <= threshold) active = section;
    });
    if (window.scrollY + window.innerHeight >= document.documentElement.scrollHeight - 2) {
      active = sections[sections.length - 1];
    }
    links.forEach(link => {
      if (link.hash === '#' + active.id) link.setAttribute('aria-current', 'location');
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
