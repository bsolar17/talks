# Agent notes

Marp slide decks, one directory per talk; see `README.md` for building.

## Git

- Linear history on `master`, no merge commits; small, focused commits
- Subject: imperative, capitalized, no prefix (no `feat:`, `docs:`...)
- Pushing to `master` publishes to GitHub Pages: only push when asked
- Generated `*.html` is git-ignored, never commit it

## Decks

- After editing, run `marp <deck>.md`, then `node .config/check-slides.cjs`
  as a separate command (chaining them can hang); fix any overflow it reports
- A change to a deck may need the same change in its translation
  (`talk.xx.md`)
- Style: Markdown wrapped at 80 columns, Title Case slide headings, straight
  quotes, code examples in Java
