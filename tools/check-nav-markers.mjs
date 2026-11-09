// From the repository root, serve docs with: python3 -m http.server 8765 --bind 127.0.0.1 --directory docs
// With Playwright and Google Chrome installed: node tools/check-nav-markers.mjs
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';

const { chromium } = createRequire(import.meta.url)('playwright');
const origin = 'http://127.0.0.1:8765';
const labels = {
  pl: ['Guardian', 'Ograniczenia', 'Pilot', 'Pobierz', 'Pomoc', 'O ExcelForge', 'Demo'],
  en: ['Guardian', 'Limitations', 'Pilot', 'Download', 'Help', 'About ExcelForge', 'Demo'],
};
const colors = ['rgb(123, 202, 98)', 'rgb(66, 189, 87)', 'rgb(34, 145, 59)', 'rgb(12, 107, 59)'];
const routes = [['/', 'pl'], ['/en/', 'en'], ['/demo/', 'pl'], ['/en/demo/', 'en']];
const viewports = [[1440, true], [901, true], [900, true], [390, true], [320, true], [320, false]];
const failures = [];
const browser = await chromium.launch({ channel: 'chrome' });

try {
  for (const [width, javaScriptEnabled] of viewports) {
    const context = await browser.newContext({ viewport: { width, height: 800 }, javaScriptEnabled });
    // Keep the regression test local, including on pages with analytics.
    await context.route('**/*', route =>
      new URL(route.request().url()).origin === origin ? route.continue() : route.abort()
    );
    const page = await context.newPage();
    page.setDefaultTimeout(5000);

    for (const [path, language] of routes) {
      const scenario = `${path} at ${width}px (JS ${javaScriptEnabled ? 'on' : 'off'})`;
      try {
        const response = await page.goto(origin + path);
        assert.equal(response.status(), 200);
        const nav = page.locator('#navigation');
        if (width <= 900 && javaScriptEnabled) {
          assert.equal(await nav.getAttribute('data-enhanced'), 'true');
          assert.equal(await nav.isVisible(), false);
          await page.locator('.menu-toggle').click();
        }
        await nav.waitFor({ state: 'visible' });
        const markers = await nav.locator('a').evaluateAll(links => links.map(link => {
          const marker = getComputedStyle(link, '::before');
          return [link.textContent.trim(), marker.backgroundColor, marker.content, link.getClientRects().length > 0];
        }));
        assert.deepEqual(markers.map(([label]) => label), labels[language]);
        assert(markers.every(([, , content, visible]) => content === '""' && visible));
        assert.deepEqual(markers.map(([, color]) => color), labels[language].map((_, i) => colors[i % colors.length]));
        console.log(`PASS: ${scenario}, 7/7 markers`);
      } catch (error) {
        failures.push(`${scenario}: ${error.message}`);
      }
    }
    await context.close();
  }
} finally {
  await browser.close();
}

assert.equal(failures.length, 0, failures.join('\n'));
