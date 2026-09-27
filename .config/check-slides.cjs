#!/usr/bin/env node
// Checks the generated decks in headless Chrome:
// - reports slides whose content overflows the slide
// - verifies the light/dark toggle (system preference, "t" key, button)
//
// Usage: node .config/check-slides.cjs [deck.html ...]   (default: every */*.html)
// Set CHROME_PATH to use another Chrome/Chromium binary.

const { execSync } = require('node:child_process')
const fs = require('node:fs')
const path = require('node:path')

// Reuse the puppeteer-core bundled with the installed Marp CLI
const marpBin = fs.realpathSync(execSync('command -v marp').toString().trim())
const puppeteer = require(require.resolve('puppeteer-core', { paths: [path.dirname(marpBin)] }))

const chrome = process.env.CHROME_PATH || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
const root = path.resolve(__dirname, '..')
const decks = process.argv.length > 2
  ? process.argv.slice(2).map((d) => path.resolve(d))
  : fs.readdirSync(root, { withFileTypes: true })
      .filter((d) => d.isDirectory() && !d.name.startsWith('.'))
      .flatMap((d) => fs.readdirSync(path.join(root, d.name))
        .filter((f) => f.endsWith('.html'))
        .map((f) => path.join(root, d.name, f)))

const background = (page) =>
  page.evaluate(() => getComputedStyle(document.querySelector('section')).backgroundColor)
const isDark = (rgb) => rgb.match(/\d+/g).slice(0, 3).reduce((a, b) => a + +b, 0) < 384

;(async () => {
  const browser = await puppeteer.launch({ executablePath: chrome, headless: true })
  let failed = false

  for (const deck of decks) {
    const page = await browser.newPage()
    const errors = []
    page.on('pageerror', (e) => errors.push(e.message))
    await page.setViewport({ width: 1280, height: 720 })
    const url = 'file://' + deck
    const problems = []

    // Overflow: how much (in slide pixels) the content is taller than the slide's inner area
    await page.goto(url, { waitUntil: 'load' })
    const count = await page.evaluate(() => document.querySelectorAll('section').length)
    const overflowing = []
    for (let i = 1; i <= count; i++) {
      await page.goto(`${url}#${i}`, { waitUntil: 'load' })
      const over = await page.evaluate((i) => {
        const s = document.querySelectorAll('section')[i - 1]
        const style = getComputedStyle(s)
        const room = s.clientHeight - parseFloat(style.paddingTop) - parseFloat(style.paddingBottom)
        const scale = s.getBoundingClientRect().height / s.offsetHeight
        const first = s.firstElementChild, last = s.lastElementChild
        if (!first) return 0
        const used = (last.getBoundingClientRect().bottom - first.getBoundingClientRect().top) / scale
        return Math.round(used - room)
      }, i)
      if (over > 0) overflowing.push(`${i} (+${over}px)`)
    }
    if (overflowing.length) problems.push(`overflowing slides: ${overflowing.join(', ')}`)

    // Light/dark toggle
    for (const scheme of ['dark', 'light']) {
      await page.emulateMediaFeatures([{ name: 'prefers-color-scheme', value: scheme }])
      await page.evaluate(() => localStorage.clear())
      await page.goto(url, { waitUntil: 'load' })
      const start = isDark(await background(page))
      if (start !== (scheme === 'dark')) problems.push(`does not follow system ${scheme} mode`)
      await page.keyboard.press('t')
      if (isDark(await background(page)) === start) problems.push('"t" does not toggle')
      await page.click('button.scheme-toggle')
      if (isDark(await background(page)) !== start) problems.push('toggle button does not toggle')
    }
    await page.evaluate(() => localStorage.clear())

    if (errors.length) problems.push(`page errors: ${errors.join('; ')}`)
    console.log(`${path.relative(root, deck)} (${count} slides): ${problems.length ? '\n  - ' + problems.join('\n  - ') : 'ok'}`)
    failed ||= problems.length > 0
    await page.close()
  }

  await browser.close()
  process.exit(failed ? 1 : 0)
})()
