(() => {
  'use strict';
  const duration = 1300;
  const stagger = 70;
  const easing = 'cubic-bezier(0.25, 0.1, 0.25, 1)'; // Homepage's "ease", no overshoot.
  const totalDuration = duration + 3 * stagger;
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const replay = document.querySelector('#replay');
  const status = document.querySelector('#motion-status');
  const variants = [...document.querySelectorAll('[data-variant]')];
  const fromTransforms = ['rotateY(-85deg)', 'rotateX(85deg)', 'rotateX(-85deg)', 'rotateY(85deg)'];
  const toTransforms = ['rotateY(0deg)', 'rotateX(0deg)', 'rotateX(0deg)', 'rotateY(0deg)'];
  let animations = [];
  let generation = 0;

  function showStatic() {
    generation += 1;
    animations.forEach(animation => animation.cancel());
    animations = [];
    variants.forEach(variant => variant.classList.remove('is-playing'));
  }

  function syncPreference() {
    showStatic();
    replay.disabled = reducedMotion.matches;
    status.textContent = reducedMotion.matches
      ? 'Ograniczenie ruchu jest włączone. Logo pozostaje statyczne, również po użyciu przycisku.'
      : 'Gotowe do porównania. Przycisk odtwarza wszystkie warianty jednocześnie.';
  }

  function play(frame = null) {
    showStatic();
    if (reducedMotion.matches) {
      syncPreference();
      return;
    }
    const currentGeneration = generation;
    const startTime = document.timeline.currentTime;
    variants.forEach(variant => {
      const isCube = variant.dataset.variant === 'c';
      const targets = [...variant.querySelectorAll(isCube ? '.cube' : '.surface')];
      targets.forEach((target, index) => {
        const frames = [
          { transform: fromTransforms[index], ...(isCube ? {} : { opacity: 0 }) },
          { transform: toTransforms[index], ...(isCube ? {} : { opacity: 1 }) }
        ];
        const animation = target.animate(frames, {
          duration, delay: index * stagger, easing, iterations: 1, fill: 'both'
        });
        animation.startTime = startTime;
        if (frame !== null) {
          animation.pause();
          animation.currentTime = frame;
        }
        animations.push(animation);
      });
      variant.classList.add('is-playing');
    });
    status.textContent = frame === null
      ? 'Porównanie w toku — jeden przebieg, 1,51 s łącznie.'
      : `Klatka kontrolna: ${frame} ms z ${totalDuration} ms. Przycisk uruchamia pełne porównanie.`;
    // Cancelling/replaying must not let an older completion hide a newer run.
    Promise.all(animations.map(animation => animation.finished)).then(() => {
      if (generation !== currentGeneration) return;
      showStatic();
      status.textContent = 'Koniec porównania. Wszystkie warianty pokazują oryginalne logo ExcelForge.';
    }).catch(() => { /* Cancellation on replay or a preference change is expected. */ });
  }

  if (typeof Element.prototype.animate !== 'function') {
    status.textContent = 'Ta przeglądarka pokazuje statyczny podgląd logo.';
    return;
  }
  replay.addEventListener('click', () => play());
  reducedMotion.addEventListener('change', syncPreference);
  syncPreference();

  // DEV-only deterministic visual QA; uses the same animations, never bypasses reduce.
  // Example: logo-motion-lab.html?frame=350 (milliseconds including stagger).
  const frameParam = new URLSearchParams(window.location.search).get('frame');
  const frame = frameParam !== null && /^\d+$/.test(frameParam)
    ? Math.min(Number(frameParam), totalDuration) : null;
  const image = document.querySelector('.static-logo');
  const ready = image.decode ? image.decode() : Promise.resolve();
  ready.then(() => window.requestAnimationFrame(() => play(frame))).catch(() => {
    showStatic();
    replay.disabled = true;
    status.textContent = 'Nie udało się wczytać źródłowego logo.';
  });
})();
