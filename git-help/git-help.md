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

# git Help

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

# Basic Concepts

---

## The Fundamental Problem

- I want to work on some files
- I want to know what changed compared to some reference version
- I want to know how a version came to be: how the files developed through
  history

---

## Basic Version Control

![](img/local.png)

---

## You Can Think About Deltas

![](img/deltas.png)

---

## You Can Think About Snapshots

![](img/snapshots.png)

---

## Learning How git Thinks

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

## Non-Distributed VCS (i.e., Not git)

![](img/centralized.png)

---

## Distributed VCS (i.e., git)

![](img/distributed.png)

---

## Remote Branches

![](img/remote-branches-1.png)

---

## You Can Work Independently on Your Local Branch

![](img/remote-branches-2.png)

---

## Eventually, You'll Have to Integrate…

![](img/remote-branches-3.png)

---

# Distributed Workflows

---

## Centralised

![](img/centralized_workflow.png)

---

## Integration Manager

![](img/integration-manager.png)

---

## Dictator

![](img/benevolent-dictator.png)

---

# How to Learn

---

## Read the Documentation

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

## Configure git to Force You to Think

`git pull --ff-only`

In `.gitconfig`:

```text
[pull]
        ff = only
```

---

## A Visual Tool Can Help to Make Sense of Things

- <https://git-scm.com/downloads/guis>

---

# Anatomy of a git Commit

---

## Commit Chain

![](img/commits-and-parents.png)

---

## Commit and Tree

![](img/commit-and-tree.png)

---

## A Commit SHA-1 Is Calculated from the Following Values

- Author name, email and timestamp
- Committer name, email and timestamp
- Parent(s) commit(s) SHA-1
- Tree SHA-1
- Commit message
- Signature, if the commit is signed

---

## This Makes the Whole Structure Consistency Verifiable

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

---

## References

- Scott Chacon, Ben Straub, _Pro Git_: <https://git-scm.com/book>; diagrams
  from the book, CC BY-NC-SA 3.0
- Git documentation: <https://git-scm.com/doc>
- Git logo by Jason Long, CC BY 3.0: <https://git-scm.com/downloads/logos>
- Merkle tree: <https://en.wikipedia.org/wiki/Merkle_tree>
- Practice: <https://learngitbranching.js.org/>

---

**Thank you!**

> Questions? Remarks? Discussion welcome!
