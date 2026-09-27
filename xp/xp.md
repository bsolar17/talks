# Extreme Programming (XP)

**What happens when you take good practices and turn the dial all the way up?**

---

## About Me & XP

**6 years** working with XP day-to-day at [Lifeware](https://www.lifeware.ch)

- ~20 collaborators at the time, incl. Kent Beck, the creator of XP
- Life Insurance SaaS, on-premise, web GUI
- 11 insurance companies
- ~800K active policies
- ~35K classes
- ~200K unit tests

---

## The Reference

- Kent Beck, _Extreme Programming Explained: Embrace Change_

---

## Historical Context: Software in the 1990s

- Dominant model: **Waterfall** and heavyweight processes
  - Big design up front, long phases, thick documents
  - Releases every 6–24 months
- Assumption: _change is expensive_, so prevent it
- Reality: requirements changed anyway ➔ late projects, failed projects
- 1996: Kent Beck, Ron Jeffries & others on the **Chrysler C3** project ➔ XP is
  born
- 2001: **Agile Manifesto**, Kent Beck is one of the 17 signatories

---

## The Impact of XP

Practices XP invented or made mainstream:

- **Test-Driven Development**
- **Continuous Integration** (➔ CI/CD pipelines)
- **Pair Programming** (➔ mob/ensemble programming)
- **Refactoring** as a daily activity
- **User Stories**, short iterations, small releases
- **Collective code ownership**, coding standards

How did one methodology give us so many things we now consider fundamental?

---

## The Core Idea

What happens if we take something known to be valuable about software
engineering and try to crank the dial up to 11?

- Start from something widely **believed to be good**
- Ask: _what happens if we do it uncompromisingly, to the **extreme**?_
- Sometimes the result works **surprisingly** well to the point of becoming
  **transformative**

---

## Example 1: Testing

- Testing is good
- Testing **earlier** is better
- Testing **before** implementing? Surprisingly, even better

➔ **Test-First Programming / TDD**

_Tests become a design tool, not just a safety check._

---

## Example 2: Code Review

- Code review is good
- **More frequent** code review is better
- Reviewing **continuously**, while the code is being written? Surprisingly,
  even better

➔ **Pair Programming**

_No review queue, no "LGTM" on a 2000-line PR._

---

## Example 3: Integration

- Integrating changes is necessary—and painful
- Integrating **more often** makes each integration smaller and easier
- Integrating **continuously**? Surprisingly, it becomes almost a non-event

➔ **Continuous Integration** ➔ **CI/CD**

_If it hurts, do it more often._

---

## Example 4: Design & Releases

- Good design is valuable ➔ improve design **every day** ➔ **Refactoring /
  Incremental Design**
- Customer feedback is valuable ➔ get it **all the time** ➔ **Small Releases,
  On-site Customer**

_Same pattern, every time._

---

## XP's Structure

```text
  Values       ➔  why we do it        (few, universal)
    ⬇
  Principles   ➔  bridge / guidelines (domain-specific reasoning)
    ⬇
  Practices    ➔  what we do daily    (concrete, situational)
```

- Practices without values are empty rituals
- Values without practices are wishful thinking
- Principles tell you how to **adapt** practices to your context

---

## Values

- **Communication**: many problems are made worse by someone not knowing
  something
- **Simplicity**: the simplest thing that could possibly work / YAGNI
- **Feedback**: fast, frequent, from code, customers, team, collaborators...
- **Courage**: making difficult decisions, supported by experience and
  discipline
- **Respect**: for all collaborators - and oneself

---

## Principles (selection)

- **Humanity**: software is built by people for people; meet their needs
- **Economics**: someone is paying for this; create ROI, deliver business value
- **Mutual Benefit**: every activity should benefit all parties / win-win
- **Self-Similarity**: apply the same patterns at every scale: if it does not
  scale find out why
- **Improvement**: "perfect" is a verb, not an adjective
- **Flow**: deliver continuously, not in big chunks
- **Redundancy**: critical problems or risks deserve multiple defenses /
  safeguards
- **Failure**: if you don't know which way is best, try one, or both. If trying
  is prohibitively expensive or dangerous, scale down / mitigate
- **Baby Steps**: small steps are cheap to take and to undo. Bridge large gaps
  with stepping stones.
- **Accepted Responsibility**: responsibility can't be assigned, only accepted

---

## Practices (primary)

| Team & Environment    | Planning        | Programming            |
| --------------------- | --------------- | ---------------------- |
| Sit Together          | Stories         | Pair Programming       |
| Whole Team            | Weekly Cycle    | Test-First Development |
| Informative Workspace | Quarterly Cycle | Incremental Design     |
| Energized Work        | Slack           | Ten-Minute Build       |
|                       |                 | Continuous Integration |

- Corollary practices: shared code, single code base, daily deployment,
  root-cause analysis...
- Start with the ones that address your biggest pain

---

## Synergy: The Whole Can Be Greater than The Sum of the Parts

```text
      Automated Tests
       ⬈          ⬊
 Refactoring  ⬌  Continuous Integration
```

- **Tests** make **refactoring** safe
- **Refactoring** keeps code simple, so **tests** stay easy to write
- **CI** runs the tests constantly, so breakage is found quickly
- Each practice covers the **weaknesses** of the others

Cherry-picking one practice in isolation often underdelivers: synergy effects
are significant

---

## The Human Side: Safety Fosters Courage

- **Sustainable pace** / Energized Work: tired developers make bad software
- **Disciplined risk control**: baby steps, tests, CI—builds are cheap and catch
  issues early
- **A safety net** from the methodology itself:
  - Break something? The tests tell you in minutes
  - Stuck? Your pair programming buddy is right there
  - Wrong direction? The next weekly cycle corrects it
- Result: developers dare to **change, clean up, and experiment**

Courage is not recklessness: it's what safety allows to try

---

## Criticism & Limits

- **All-or-nothing**: the practices depend on each other, but full adoption
  needs commitment at all organizational levels
- **Organizational fit**: on-site customer, sitting together, negotiated scope
  clash with outsourcing, distributed teams, strict hierarchies.
- **Regulated environments**: audits and compliance may require processes,
  documentation or up-front design XP deliberately tries to minimize
- **Pair programming**: perceived as costly, can be exhausting, not for every
  situation
- **Evolutionary design**: without constant refactoring discipline, architecture
  can drift
- **Dogmatism risk**: "extreme" can harden into orthodoxy, contradicting XP's
  own principles of reflection and improvement
- Even the **C3 project** was cancelled in 2000: it delivered on time but never
  achieved full scope before cancellation

XP is not a silver bullet: know what you give up when you compromise, and why

---

## XP in the Age of AI

Software is still built by people... but increasingly **with** AI

- **Test-First**: tests become the spec and the guardrail for generated code
- **Ten-Minute Build / CI**: more code, faster ➔ fast automated feedback matters
  even more
- **Simplicity / YAGNI**: code is now cheap to produce, but still costly to own
- **Baby Steps**: AI invites huge diffs; small, verified steps keep you in
  control
- **Pair Programming**: AI can be a tireless pair, but doesn't spread knowledge
  or ownership across the team
- **Accepted Responsibility**: the AI writes code, but people remain accountable

Kent Beck himself now experiments with "augmented coding": AI + TDD

---

## Key Conclusions

- XP's "extremes" became today's **industry standards**
- Uncompromising commitment can unlock results that compromised approaches might
  never reach
- **Compromises** can hide the benefits:
  - "We do TDD, except when we're in a hurry"
  - "We integrate continuously... every two months"
- The practices reinforce each other: **half-measures break the synergy**

---

## Your Turn: The "Extreme" Game

Pick something your team believes is good, and ask:

- _What if we pushed this to the **extreme**?_
- What would **break**? What would **hurt**?
- What would need to **work differently** for it not to break? To stop hurting?
- What could we **gain** from it?

Often, what breaks or hurts shows you exactly what has to improve next!

---

**Thank you!**

> Questions? Remarks? Discussion welcome!
