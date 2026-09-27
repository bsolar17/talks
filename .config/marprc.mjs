// Light/dark switch injected into every generated deck.
// Starts from the system preference; press "t" or use the half-circle button to toggle.
// The choice is remembered and synced across windows (e.g. presenter view).
const schemeToggle = `
<style>
  html[data-scheme="light"] section { color-scheme: light !important; }
  html[data-scheme="dark"] section { color-scheme: dark !important; }
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

export default {
  inputDir: '..',
  theme: 'marp-theme.css',
  engine: ({ marp }) => {
    const render = marp.render.bind(marp)
    marp.render = (...args) => {
      const result = render(...args)
      return { ...result, html: result.html + schemeToggle }
    }
    return marp
  },
}
