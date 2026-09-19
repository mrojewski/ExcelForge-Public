// Run with: node tools/check-motion-lab.mjs
// Lifecycle tests; no browser installation or project dependencies needed.
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';

const source = readFileSync(new URL('../docs/dev/logo-motion-lab.js', import.meta.url), 'utf8');
const flush = async () => { for (let i = 0; i < 8; i++) await Promise.resolve(); };

function boot({ reduce = false, query = '' } = {}) {
  const records = [];
  const preference = { matches: reduce, addEventListener(type, fn) { this.change = fn; } };
  const button = { disabled: true, addEventListener(type, fn) { this.click = fn; } };
  const status = { textContent: '' };
  const variants = ['a', 'b', 'c'].map(name => ({
    dataset: { variant: name },
    classList: { playing: false, add() { this.playing = true; }, remove() { this.playing = false; } },
    querySelectorAll() {
      return Array.from({ length: 4 }, () => ({
        animate(frames, options) {
          let resolve, reject;
          const finished = new Promise((yes, no) => { resolve = yes; reject = no; });
          const record = {
            variant: name, frames, options, finished, resolve,
            cancel() { this.cancelled = true; reject(new Error('cancelled')); },
            pause() { this.paused = true; }
          };
          records.push(record);
          return record;
        }
      }));
    }
  }));
  vm.runInNewContext(source, {
    URLSearchParams, Promise,
    Element: { prototype: { animate() {} } },
    window: { matchMedia: () => preference, location: { search: query }, requestAnimationFrame: fn => fn() },
    document: {
      timeline: { currentTime: 500 },
      querySelector: selector => selector === '#replay' ? button : selector === '#motion-status' ? status : { decode: () => Promise.resolve() },
      querySelectorAll: () => variants
    }
  });
  return { records, preference, button, status, variants };
}

// Even QA frame URLs and direct replay events cannot override a reduced-motion preference.
const reduced = boot({ reduce: true, query: '?frame=350' });
await flush();
assert.equal(reduced.records.length, 0);
assert.equal(reduced.button.disabled, true);
reduced.button.click();
await flush();
assert.equal(reduced.records.length, 0);
assert(reduced.variants.every(v => !v.classList.playing));

// All variants share a start time and the same overlapping four-block rhythm.
const normal = boot();
await flush();
assert.equal(normal.records.length, 12);
assert(normal.records.every(r => r.startTime === 500 && r.options.duration === 1300 && r.options.iterations === 1));
assert.deepEqual(normal.records.map(r => r.options.delay), [0, 70, 140, 210, 0, 70, 140, 210, 0, 70, 140, 210]);
assert(normal.records.every(r => r.options.easing === 'cubic-bezier(0.25, 0.1, 0.25, 1)'));

// Old finish microtasks must not reset a newer replay to the static image.
normal.records.forEach(r => r.resolve());
normal.button.click();
await flush();
assert(normal.variants.every(v => v.classList.playing));
normal.button.click();
normal.button.click();
await flush();
assert.equal(normal.records.length, 48);
assert(normal.records.slice(0, 36).every(r => r.cancelled));
assert(normal.variants.every(v => v.classList.playing));

// Changing the preference mid-flight cancels motion; replay remains guarded.
normal.preference.matches = true;
normal.preference.change();
await flush();
assert(normal.records.every(r => r.cancelled));
assert(normal.variants.every(v => !v.classList.playing));
normal.button.click();
await flush();
assert.equal(normal.records.length, 48);
normal.preference.matches = false;
normal.preference.change();
assert.equal(normal.button.disabled, false);
assert.equal(normal.records.length, 48); // No surprise autoplay when preference changes back.
normal.button.click();
normal.records.slice(-12).forEach(r => r.resolve());
await flush();
assert(normal.variants.every(v => !v.classList.playing));
assert.match(normal.status.textContent, /Koniec porównania/);

console.log('PASS: reduced-motion startup/replay, mid-flight cancellation, synchronized timing, rapid replay, stale finish race, static completion.');
