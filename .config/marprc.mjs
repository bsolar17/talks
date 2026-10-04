// Extras injected into every generated deck.

// Light/dark switch.
// Starts from the system preference; press "t" or use the half-circle button to toggle.
// The choice is remembered and synced across windows (e.g. presenter view).
const schemeToggle = `
<style>
  html[data-scheme="light"] :is(section, body) { color-scheme: light !important; }
  html[data-scheme="dark"] :is(section, body) { color-scheme: dark !important; }
  /* Fill the space around the slide (window not 16:9) with the slide background
     (Catppuccin base, see marp-theme.css) instead of black */
  @media screen {
    body[data-bespoke-view=""] {
      color-scheme: light dark;
      background: light-dark(#eff1f5, #1e1e2e);
    }
  }
  /* Same look as Marp's built-in control buttons: 32px box, white stroked SVG */
  button.scheme-toggle {
    width: 32px;
    height: 32px;
    background: transparent url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ccircle cx='50' cy='50' r='33' fill='none' stroke='%23fff' stroke-width='5'/%3E%3Cpath d='M50 17a33 33 0 0 1 0 66z' fill='%23fff'/%3E%3C/svg%3E") no-repeat center / contain;
    overflow: hidden;
    text-indent: 100%;
    white-space: nowrap;
  }
</style>
<script>
(() => {
  const key = 'marp-color-scheme'
  const root = document.documentElement
  const current = () =>
    root.dataset.scheme ||
    (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')
  const apply = (scheme) => { if (scheme) root.dataset.scheme = scheme }
  const toggle = () => {
    const next = current() === 'dark' ? 'light' : 'dark'
    apply(next)
    try { localStorage.setItem(key, next) } catch {}
  }

  try { apply(localStorage.getItem(key)) } catch {}
  addEventListener('storage', (e) => { if (e.key === key) apply(e.newValue) })
  document.addEventListener('keydown', (e) => {
    if (e.key === 't' && !e.altKey && !e.ctrlKey && !e.metaKey) toggle()
  })
  document.addEventListener('DOMContentLoaded', () => {
    const osc = document.querySelector('.bespoke-marp-osc')
    if (!osc) return
    const button = document.createElement('button')
    button.className = 'scheme-toggle'
    button.tabIndex = -1
    button.title = 'Toggle light/dark (t)'
    button.textContent = 'Toggle light/dark'
    button.addEventListener('click', toggle)
    osc.appendChild(button)
  })
})()
</script>
`

// Shrinks the text of slides whose content doesn't fit, until it does:
// too tall for the slide, or code blocks too wide.
// Runs before Marp's viewer script, while all slides are still laid out.
const fitSlides = `
<script>
for (const slide of document.querySelectorAll('section')) {
  const style = getComputedStyle(slide)
  const base = parseFloat(style.fontSize)
  const room = slide.clientHeight - parseFloat(style.paddingTop) - parseFloat(style.paddingBottom)
  // Height of the content, in slide pixels (the slide itself is scaled to the window)
  const used = () => {
    const first = slide.firstElementChild, last = slide.lastElementChild
    if (!first) return 0
    const scale = slide.getBoundingClientRect().height / slide.offsetHeight
    return (last.getBoundingClientRect().bottom - first.getBoundingClientRect().top) / scale
  }
  const codeTooWide = () => [...slide.querySelectorAll('pre')].some((pre) => pre.scrollWidth > pre.clientWidth)
  const overflows = () => used() > room || codeTooWide()
  for (let scale = 0.98; overflows() && scale >= 0.5; scale -= 0.02) {
    slide.style.fontSize = base * scale + 'px'
  }
}
</script>
`

export default {
  themeSet: 'marp-theme.css',
  theme: 'auto', // the @theme name declared in marp-theme.css
  engine: ({ marp }) => {
    // Newlines inside a paragraph are just source wrapping, not line breaks
    marp.markdown.set({ breaks: false })
    const render = marp.render.bind(marp)
    marp.render = (...args) => {
      const result = render(...args)
      return { ...result, html: result.html + fitSlides + schemeToggle }
    }
    return marp
  },
}
