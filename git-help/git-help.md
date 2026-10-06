---
author: Christian Apolloni
date: 2026-10-01
style: |
  p:has(> img:only-child) {
    text-align: center;
  }
  p > img:only-child {
    max-width: 800px;
    max-height: 460px;
    box-sizing: border-box;
    padding: 12px;
    border-radius: 8px;
    background: light-dark(transparent, #fff);
  }
---

# git help

**A short overview of git's main concepts**

```text
usage: git [--version] [--help] [-C <path>] [-c name=value]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]
```

---

![bg right:30% contain](img/git-logo.png)

## git

***git /ɡɪt/ n brit slang***

1. a contemptible person, often a fool
2. a bastard

> *"I'm an egotistical bastard, so I name all my projects after myself.
> First Linux, now git."*
>
> Linus Torvalds

---

# Basic concepts

---

## The fundamental problem

- I want to work on some files
- I want to know what changed compared to some reference version
- I want to know how a version came to be: how the files developed through
  history

---

## Basic Version Control

![](img/local.png)

---

## You can think about deltas

![](img/deltas.png)

---

## You can think about snapshots

![](img/snapshots.png)

---

## Learning how git thinks

![](img/data-model-4.png)

---

## Working Tree / Version Database

![](img/areas.png)

---

## Revisions / References

![](img/branch-and-history.png)

---

## Branches

![](img/basic-rebase-1.png)

---

## Merge

![](img/basic-rebase-2.png)

---

## Rebase

![](img/basic-rebase-3.png)

---

# Remotes

---

## Non-distributed VCS (i.e., not git)

![](img/centralized.png)

---

## Distributed VCS (i.e., git)

![](img/distributed.png)

---

## Remote branches

![](img/remote-branches-1.png)

---

## You can work independently on your local branch

![](img/remote-branches-2.png)

---

## Eventually, you'll have to integrate…

![](img/remote-branches-3.png)

---

# Distributed workflows

---

## Centralised

![](img/centralized_workflow.png)

---

## Integration manager

![](img/integration-manager.png)

---

## Dictator

![](img/benevolent-dictator.png)

---

# How to learn

---

## Read the documentation

- <https://git-scm.com/doc>
- <https://git-scm.com/blog>
- <https://www.google.com>
- `git help`
- `git help everyday`

---

## Exercise

- Create your own local repository and play with it
- <https://learngitbranching.js.org/>
- <https://try.github.io>

---

## Configure git to force you to think

`git pull --ff-only`

In `.gitconfig`:

```text
[pull]
        ff = only
```

---

## A visual tool can help to make sense of things

- <https://git-scm.com/downloads/guis>

---

# Anatomy of a git commit

---

## Commit chain

![](img/commits-and-parents.png)

---

## Commit and tree

![](img/commit-and-tree.png)

---

## A commit SHA-1 is calculated from the following values

- Author name, email and timestamp
- Committer name, email and timestamp
- Parent(s) commit(s) SHA-1
- Tree SHA-1
- Commit message
- Signature, if the commit is signed

---

## This makes the whole structure consistency verifiable

- Git stores data in a specialized Merkle tree structure
  (<https://en.wikipedia.org/wiki/Merkle_tree>)
- Attempting to modify a commit will require to calculate a different SHA-1,
  otherwise the SHA-1 would not match with the data anymore.
- This includes attempting to modify anything in the directory tree referenced
  by the commit.
- This different SHA-1 has to be propagated to all the commit descendants,
  leading to different SHA-1s for all the descendants.
- Repeat recursively…
- **If the commit SHA-1 matches, the commit refers to exactly the same complete
  commit chain**
