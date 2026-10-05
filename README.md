# Talks

Slide decks written in Markdown and built with [Marp](https://marp.app/).
Each talk lives in its own directory.
A translation sits next to the English deck, named after it with the language
code appended, e.g. `xp/xp.de.md`.

Published at <https://bsolar17.github.io/talks/>.

## Building

From the repo root:

```sh
marp '*/*.md'
```

Each deck's HTML is written next to its Markdown (and ignored by git).

Slides whose content doesn't fit are shrunk automatically when the deck is
shown. To find the ones that still overflow, and to check the light/dark
toggle:

```sh
node .config/check-slides.cjs
```
