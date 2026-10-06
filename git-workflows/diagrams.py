#!/usr/bin/env python3
"""Generates the commit-graph SVGs in img/ for git-workflows.md.

Usage: python3 diagrams.py [output dir]   (default: img/ next to this script)

img/two-directions.svg is not generated: it is written by hand.

Colors (Catppuccin Latte, readable on the white image background in both
themes): shared history grey, other people's commits peach, my commits green,
merge commits made by the platform mauve, master blue.
"""
import sys
from html import escape
from pathlib import Path

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / 'img'

C = dict(
    blue='#1e66f5', peach='#fe640b', green='#40a02b', mauve='#8839ef',
    red='#d20f39', teal='#179299',
    text='#4c4f69', sub='#8c8fa1', line='#9ca0b0',
)
COL, ROW, X0, Y0 = 72, 64, 40, 40  # grid: column width, row height, origin
FONT = "font-family='system-ui, -apple-system, Segoe UI, Helvetica, Arial, sans-serif'"


class Graph:
    """A commit graph laid out on a grid; the SVG is cropped to its content."""

    def __init__(self, x0=X0):
        self.x0 = x0
        self.commits = {}
        self.edges = []
        self.refs = {}
        self.extra = []
        self.bounds = [1e9, 1e9, -1e9, -1e9]

    def grow(self, x1, y1, x2, y2):
        b = self.bounds
        self.bounds = [min(b[0], x1), min(b[1], y1), max(b[2], x2), max(b[3], y2)]

    def c(self, name, col, row, color, parents=(), label=None, ghost=False):
        """A commit. Ghosts (dashed) are commits no longer on any branch."""
        x, y = self.x0 + col * COL, Y0 + row * ROW
        self.commits[name] = dict(x=x, y=y, color=C[color], ghost=ghost, parents=list(parents),
                                  label=name if label is None else label)
        for p in parents:
            self.edges.append((p, name, ghost))
        self.grow(x - 18, y - 18, x + 18, y + 18)
        return self

    def ref(self, commit, text, color, pos='right', kind='branch'):
        """A branch label (filled), or a remote-tracking one (kind='remote', dashed)."""
        self.refs.setdefault((commit, pos), []).append((text, color, kind))

    def text(self, x, y, s, color='text', size=15, anchor='start', weight='normal', italic=False):
        style = " font-style='italic'" if italic else ''
        self.extra.append(f"<text x='{x}' y='{y}' fill='{C[color]}' font-size='{size}' text-anchor='{anchor}' "
                          f"font-weight='{weight}'{style}>{escape(s)}</text>")
        w = len(s) * size * 0.56  # rough text width, for the bounds
        x1 = x - (w if anchor == 'end' else w / 2 if anchor == 'middle' else 0)
        self.grow(x1, y - size, x1 + w, y + 4)

    def lane(self, row, s, color):
        self.text(10, Y0 + row * ROW + 5, s, color, size=15, weight='bold')

    def path(self, a, b):
        A, B = self.commits[a], self.commits[b]
        x1, y1, x2, y2 = A['x'], A['y'], B['x'], B['y']
        if y1 == y2:
            return f"M{x1} {y1} L{x2} {y2}"
        if x2 - x1 <= COL:
            m = (x1 + x2) / 2
            return f"M{x1} {y1} C{m} {y1} {m} {y2} {x2} {y2}"
        if len(B['parents']) > 1 and B['parents'][0] != a:
            # Merged-in parent: stay on its own row, turn just before the merge
            k = x2 - COL
            return f"M{x1} {y1} L{k} {y1} C{k + COL / 2} {y1} {k + COL / 2} {y2} {x2} {y2}"
        # Branching off: turn just after the fork point, then stay on the new row
        k = x1 + COL
        return f"M{x1} {y1} C{x1 + COL / 2} {y1} {x1 + COL / 2} {y2} {k} {y2} L{x2} {y2}"

    def render(self, name):
        out = []
        for a, b, dashed in self.edges:
            dash = " stroke-dasharray='5 4'" if dashed else ''
            out.append(f"<path d='{self.path(a, b)}' fill='none' stroke='{C['line']}' stroke-width='3'{dash}/>")
        for k in self.commits.values():
            x, y = k['x'], k['y']
            if k['ghost']:
                out.append(f"<circle cx='{x}' cy='{y}' r='16' fill='#fff' stroke='{C['sub']}' "
                           f"stroke-width='2' stroke-dasharray='4 3'/>")
                fill = C['sub']
            else:
                out.append(f"<circle cx='{x}' cy='{y}' r='16' fill='{k['color']}' stroke='#fff' stroke-width='3'/>")
                fill = '#fff'
            size = 13 if len(k['label']) <= 2 else 11
            out.append(f"<text x='{x}' y='{y + 4.5}' fill='{fill}' font-size='{size}' font-weight='bold' "
                       f"text-anchor='middle'>{escape(k['label'])}</text>")
        for (n, pos), labels in self.refs.items():
            x, y = self.commits[n]['x'], self.commits[n]['y']
            cx = x + 24
            for text, color, kind in labels:
                w, h = len(text) * 7.6 + 16, 22
                if pos == 'right':
                    rx, ry = cx, y - h / 2
                    cx += w + 6
                elif pos == 'above':
                    rx, ry = x - w / 2, y - 22 - h
                    y -= h + 4
                else:  # below
                    rx, ry = x - w / 2, y + 22
                    y += h + 4
                if kind == 'branch':
                    out.append(f"<rect x='{rx:.1f}' y='{ry:.1f}' width='{w:.1f}' height='{h}' rx='5' fill='{C[color]}'/>")
                    tf = '#fff'
                else:  # remote-tracking
                    out.append(f"<rect x='{rx:.1f}' y='{ry:.1f}' width='{w:.1f}' height='{h}' rx='5' fill='#fff' "
                               f"stroke='{C[color]}' stroke-width='2' stroke-dasharray='4 3'/>")
                    tf = C[color]
                out.append(f"<text x='{rx + w / 2:.1f}' y='{ry + 15.5:.1f}' fill='{tf}' font-size='13' "
                           f"font-weight='bold' text-anchor='middle'>{escape(text)}</text>")
                self.grow(rx, ry, rx + w, ry + h)
        out += self.extra
        b, pad = self.bounds, 14
        x, y, w, h = b[0] - pad, b[1] - pad, b[2] - b[0] + 2 * pad, b[3] - b[1] + 2 * pad
        (OUT / f'{name}.svg').write_text(
            f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='{x:.0f} {y:.0f} {w:.0f} {h:.0f}' "
            f"width='{w:.0f}' height='{h:.0f}' {FONT}>\n" + '\n'.join(out) + '\n</svg>\n')


def title(g, row, s):
    """A panel title, above the commits on the given row."""
    g.text(0, Y0 + row * ROW - 44, s, 'sub', size=14, weight='bold')


def chain(g, names, row, color, start=0, parent=None, prefix=''):
    """Consecutive commits on one row; a name may carry its label after ':'."""
    prev = parent
    for i, n in enumerate(names):
        key, _, label = n.partition(':')
        g.c(prefix + key, start + i, row, color, [prev] if prev else [], label=label or key)
        prev = prefix + key
    return prev


def diverged(g, row, prefix=''):
    """The running example: master = A B C D (Alice), feature = A B X Y (me)."""
    chain(g, ['A', 'B'], row, 'text', prefix=prefix)
    chain(g, ['C', 'D'], row, 'peach', start=2, parent=prefix + 'B', prefix=prefix)
    chain(g, ['X', 'Y'], row + 1, 'green', start=2, parent=prefix + 'B', prefix=prefix)


def rebased(g, row, prefix=''):
    """The running example after a rebase: A B C D X' Y'."""
    chain(g, ['A', 'B'], row, 'text', prefix=prefix)
    chain(g, ['C', 'D'], row, 'peach', start=2, parent=prefix + 'B', prefix=prefix)
    chain(g, ["X:X'", "Y:Y'"], row, 'green', start=4, parent=prefix + 'D', prefix=prefix)


def old_xy(g, row, prefix=''):
    """X, Y as they were before a rebase."""
    g.c(prefix + 'Xo', 2, row, 'green', [prefix + 'B'], label='X', ghost=True)
    g.c(prefix + 'Yo', 3, row, 'green', [prefix + 'Xo'], label='Y', ghost=True)


# --- The example ------------------------------------------------------------

g = Graph()
diverged(g, 0)
g.ref('D', 'origin/master', 'peach', kind='remote'); g.ref('Y', 'feature', 'green')
g.text(g.commits['D']['x'] + 152, g.commits['D']['y'] + 5, 'Alice pushed C, D', 'peach', size=13, italic=True)
g.text(g.commits['Y']['x'] + 106, g.commits['Y']['y'] + 5, 'I committed X, Y locally', 'green', size=13, italic=True)
g.render('example')

# --- 1. Getting up to date --------------------------------------------------

g = Graph()
title(g, 0.5, 'git merge origin/master')
diverged(g, 1)
g.c('M', 4, 2, 'green', ['Y', 'D'])
g.ref('D', 'origin/master', 'peach', 'above', kind='remote'); g.ref('M', 'feature', 'green')
g.render('catch-up-merge')

g = Graph()
title(g, 0.5, 'git rebase origin/master')
rebased(g, 1)
old_xy(g, 2.5)
g.ref('D', 'origin/master', 'peach', 'below', kind='remote'); g.ref('Y', 'feature', 'green')
g.text(g.commits['Yo']['x'] + 30, g.commits['Yo']['y'] + 5, 'old commits, no longer referenced', 'sub', size=13, italic=True)
g.render('rebase')

# --- 2. Updating origin/master ----------------------------------------------

g = Graph()
title(g, 0.5, 'Pushing feature to master: rejected, origin/master is not an ancestor of feature')
diverged(g, 1)
g.ref('D', 'origin/master', 'peach', kind='remote'); g.ref('Y', 'feature', 'green')
g.text(g.commits['Y']['x'] + 112, g.commits['Y']['y'] + 5, '✗ rejected', 'red', size=14, weight='bold')
g.render('not-updated')

g = Graph()
title(g, 0.5, '1. git merge origin/master: M exists only locally')
diverged(g, 1)
g.c('M', 4, 2, 'green', ['Y', 'D'])
g.ref('D', 'origin/master', 'peach', 'above', kind='remote'); g.ref('M', 'feature', 'green')
title(g, 3.5, '2. Push to master: fast-forward')
diverged(g, 4, prefix='2')
g.c('2M', 4, 5, 'green', ['2Y', '2D'], label='M')
g.ref('2M', 'feature', 'green'); g.ref('2M', 'origin/master', 'peach', kind='remote')
g.render('merged-update')

g = Graph()
title(g, 0.5, "1. git rebase origin/master: X', Y' exist only locally")
rebased(g, 1)
old_xy(g, 2)
g.ref('D', 'origin/master', 'peach', 'above', kind='remote'); g.ref('Y', 'feature', 'green')
title(g, 3.5, '2. Push to master: fast-forward')
rebased(g, 4, prefix='2')
g.ref('2Y', 'feature', 'green'); g.ref('2Y', 'origin/master', 'peach', kind='remote')
g.render('rebased-update')

g = Graph()
title(g, 0.5, 'Merged by the platform with a merge commit')
diverged(g, 1)
g.c('M', 4, 1, 'mauve', ['D', 'Y'])
g.ref('M', 'origin/master', 'peach', kind='remote'); g.ref('Y', 'origin/feature', 'green', 'below', kind='remote')
title(g, 3.75, '…or rebased by the platform')
rebased(g, 4.25, prefix='2')
old_xy(g, 5.25, prefix='2')
g.ref('2Y', 'origin/master', 'peach', kind='remote'); g.ref('2Yo', 'origin/feature', 'green', kind='remote')
g.render('pr-merged')

# --- 3. History shapes: the same three features, three ways -----------------

g = Graph()
g.c('m0', 0, 0, 'text', label='')
g.c('a1', 1, 1, 'green', ['m0'], label='').c('b1', 1, 2, 'mauve', ['m0'], label='')
g.c('m1', 2, 0, 'peach', ['m0'], label='')
g.c('a2', 2, 1, 'green', ['a1'], label='')
g.c('a3', 3, 1, 'green', ['a2', 'm1'], label='')
g.c('b2', 3, 2, 'mauve', ['b1'], label='')
g.c('M1', 4, 0, 'text', ['m1', 'a3'], label='')
g.c('c1', 5, 3, 'teal', ['M1'], label='')
g.c('b3', 5, 2, 'mauve', ['b2', 'M1'], label='')
g.c('M2', 6, 0, 'text', ['M1', 'b3'], label='')
g.c('c2', 6, 3, 'teal', ['c1'], label='')
g.c('c3', 7, 3, 'teal', ['c2', 'M2'], label='')
g.c('M3', 8, 0, 'text', ['M2', 'c3'], label='')
g.ref('M3', 'master', 'blue')
g.render('history-merge')

g = Graph()
g.c('m0', 0, 0, 'text', label='')
g.c('m1', 1, 0, 'peach', ['m0'], label='')
g.c('a1', 2, 0, 'green', ['m1'], label='').c('a2', 3, 0, 'green', ['a1'], label='')
g.c('b1', 4, 0, 'mauve', ['a2'], label='').c('b2', 5, 0, 'mauve', ['b1'], label='')
g.c('c1', 6, 0, 'teal', ['b2'], label='').c('c2', 7, 0, 'teal', ['c1'], label='')
g.ref('c2', 'master', 'blue')
g.render('history-linear')

g = Graph()
g.c('m0', 0, 0, 'text', label='')
g.c('m1', 1, 0, 'peach', ['m0'], label='')
g.c('a1', 2, 1, 'green', ['m1'], label='').c('a2', 3, 1, 'green', ['a1'], label='')
g.c('M1', 4, 0, 'text', ['m1', 'a2'], label='')
g.c('b1', 5, 1, 'mauve', ['M1'], label='').c('b2', 6, 1, 'mauve', ['b1'], label='')
g.c('M2', 7, 0, 'text', ['M1', 'b2'], label='')
g.c('c1', 8, 1, 'teal', ['M2'], label='').c('c2', 9, 1, 'teal', ['c1'], label='')
g.c('M3', 10, 0, 'text', ['M2', 'c2'], label='')
g.ref('M3', 'master', 'blue')
g.render('history-semi')

# --- 4. Workflow examples on GitHub: branches as GitHub shows them ----------

g = Graph()
diverged(g, 0.5)
g.c('M', 4, 0.5, 'mauve', ['D', 'Y'])
g.ref('M', 'master', 'blue'); g.ref('Y', 'feature', 'green')
g.text(g.commits['M']['x'], g.commits['M']['y'] - 28, 'merge commit created by GitHub', 'sub', size=13, anchor='middle', italic=True)
g.text(g.commits['Y']['x'] + 108, g.commits['Y']['y'] + 5, 'checks ran on a test merge of Y with C', 'red', size=13, italic=True)
g.render('gh-merge')

g = Graph()
title(g, 0.5, 'Squash and merge')
diverged(g, 1)
g.c('S', 4, 1, 'mauve', ['D'])
g.ref('S', 'master', 'blue'); g.ref('Y', 'feature', 'green')
g.text(g.commits['S']['x'], g.commits['S']['y'] - 28, 'X + Y as one new commit', 'sub', size=13, anchor='middle', italic=True)
title(g, 3.5, 'Rebase and merge')
rebased(g, 4, prefix='2')
old_xy(g, 5, prefix='2')
g.ref('2Y', 'master', 'blue'); g.ref('2Yo', 'feature', 'green')
g.render('gh-squash-rebase')

g = Graph()
title(g, 0.5, 'Update branch (default): merge')
diverged(g, 1)
g.c('U', 4, 2, 'green', ['Y', 'D'])
g.ref('D', 'master', 'blue', 'above'); g.ref('U', 'feature', 'green')
title(g, 3.5, 'Update with rebase')
rebased(g, 4, prefix='2')
old_xy(g, 5, prefix='2')
g.ref('2D', 'master', 'blue', 'above'); g.ref('2Y', 'feature', 'green')
g.render('gh-update-branch')

g = Graph()
chain(g, ['A', 'B'], 0, 'text')
chain(g, ['C', 'D'], 0, 'peach', start=2, parent='B')
chain(g, ['X', 'Y'], 1, 'green', start=2, parent='B')
chain(g, ['P', 'Q'], 2, 'teal', start=3, parent='C')
g.c('U', 4, 1, 'green', ['Y', 'D'])
g.c('N', 5, 0, 'mauve', ['D', 'Q'])
chain(g, ['Z', 'W'], 1, 'green', start=5, parent='U')
g.c('E', 6, 0, 'peach', ['N'])
g.c('M', 7, 0, 'mauve', ['E', 'W'])
g.ref('M', 'master', 'blue'); g.ref('W', 'feature', 'green', 'below'); g.ref('Q', 'bugfix', 'teal')
g.render('gh-circuit')

g = Graph()
title(g, 0.5, 'feature is behind master: merging is blocked')
diverged(g, 1)
g.ref('D', 'master', 'blue'); g.ref('Y', 'feature', 'green')
g.text(g.commits['Y']['x'] + 108, g.commits['Y']['y'] + 5, '✗ out of date', 'red', size=14, weight='bold')
title(g, 3.5, 'feature updated, checked, rebased onto master: now bugfix is behind')
rebased(g, 4, prefix='2')
chain(g, ['Z'], 5, 'teal', start=4, parent='2D', prefix='2')
g.ref('2Y', 'master', 'blue'); g.ref('2Z', 'bugfix', 'teal')
g.text(g.commits['2Z']['x'] + 100, g.commits['2Z']['y'] + 5, '✗ out of date', 'red', size=14, weight='bold')
g.render('gh-linear')

# Merge queue with the "merge" method: queue entries are merge commits on top
# of master and of the entries ahead; master fast-forwards to a green entry.
g = Graph(x0=170)
title(g, 0.5, '1. Queued: merge commits on top of master, on gh-readonly-queue/… branches')
for row in (1, 5):
    g.lane(row, 'master', 'blue'); g.lane(row + 1, 'merge queue', 'mauve'); g.lane(row + 2, 'pull requests', 'sub')
chain(g, ['A', 'B'], 1, 'text')
chain(g, ['C', 'D'], 1, 'peach', start=2, parent='B')
chain(g, ['X', 'Y'], 3, 'green', start=2, parent='B')
chain(g, ['Z'], 3, 'teal', start=5, parent='D')
g.c('Q1', 4, 2, 'mauve', ['D', 'Y'], label='M1')
g.c('Q2', 6, 2, 'mauve', ['Q1', 'Z'], label='M2')
g.ref('D', 'master', 'blue')
g.text(g.commits['Q2']['x'] + 30, g.commits['Q2']['y'] + 5, 'CI: M1 ✓, M2 running', 'sub', size=13, italic=True)
title(g, 4.5, '2. M1 is green: master fast-forwards to exactly the tested commit')
chain(g, ['A', 'B'], 5, 'text', prefix='2')
chain(g, ['C', 'D'], 5, 'peach', start=2, parent='2B', prefix='2')
chain(g, ['X', 'Y'], 7, 'green', start=2, parent='2B', prefix='2')
chain(g, ['Z'], 7, 'teal', start=5, parent='2D', prefix='2')
g.c('2Q1', 4, 5, 'mauve', ['2D', '2Y'], label='M1')
g.c('2Q2', 6, 6, 'mauve', ['2Q1', '2Z'], label='M2')
g.ref('2Q1', 'master', 'blue')
g.render('gh-merge-queue')
