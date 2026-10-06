---
author: Christian Apolloni
date: 2026-09-26
---

# Extreme Programming (XP)

**Embrace Change**

---

## About Me & XP

**6 years** (2006-2013) working with XP day-to-day at [Lifeware](https://www.lifeware.ch)

- ~20 collaborators at the time, incl. Kent Beck, the creator of XP
- Life Insurance outsourcing: SaaS hosted by Lifeware, web GUI
- 11 insurance companies
- ~800K active policies
- ~35K classes
- ~200K unit tests

---

## The Reference

- Kent Beck with Cynthia Andres, _Extreme Programming Explained: Embrace
  Change_, 2nd edition (2004)

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

Kent Beck's image: a control board with a knob for each practice known to work.
What happens if we turn every knob up to 10?

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
- Customer feedback is valuable ➔ get it **all the time** ➔ **Daily
  Deployment, Real Customer Involvement**

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

- **Communication**: everyone is part of the team; work together face to face,
  from requirements to code
- **Simplicity**: do what is needed and asked for, but no more; take small,
  simple steps
- **Feedback**: deliver working software every iteration, demo early and
  often, listen, and adapt (the process too)
- **Courage**: tell the truth about progress and estimates, adapt to change;
  no one works alone, and principles guide you through uncertainty
- **Respect**: everyone contributes value; developers and customers respect
  each other's expertise; teams own their work

_Based on Don Wells,
[extremeprogramming.org](http://www.extremeprogramming.org/values.html)_

---

## Principles (selection)

- **Humanity**: software is built by people for people; meet their needs
- **Economics**: someone is paying for this; create ROI, deliver business value
- **Mutual Benefit**: every activity should benefit all parties / win-win
- **Self-Similarity**: try reusing a solution's structure at other scales. It
  won't always fit, but proven structures are a good starting point
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
| Whole Team            | Weekly Cycle    | Test-First Programming |
| Informative Workspace | Quarterly Cycle | Incremental Design     |
| Energized Work        | Slack           | Ten-Minute Build       |
|                       |                 | Continuous Integration |

- Corollary practices: shared code, single code base, daily deployment,
  root-cause analysis...
- Start with the ones that address your biggest pain, but expect the full
  payoff only once the supporting practices are in place

---

## An XP Team in Practice

| Rhythm    | What happens                                            | Feedback from  |
| --------- | ------------------------------------------------------- | -------------- |
| Minutes   | In pairs: failing test ➔ make it pass ➔ refactor        | Tests          |
| Hours     | Integrate; the ten-minute build runs all the tests      | CI             |
| Daily     | Stand-up, rotate pairs, ask the customer what's unclear | Team, customer |
| Weekly    | Customer picks stories; demo; retrospective             | Customer, team |
| Quarterly | Themes, big-picture planning, reflect on the process    | Business       |

Feedback loops at every timescale: the shorter the loop, the cheaper the
correction

---

## Synergy: The Whole Can Be Greater than The Sum of the Parts

```text
       Automated Tests
        ⤢           ⤡
Refactoring   ↔   Continuous Integration
```

- **Tests ↔ Refactoring**: tests make refactoring safe; refactoring keeps
  code simple and easy to test
- **Tests ↔ CI**: tests give integration a meaning beyond "it compiles"; CI
  runs them constantly, so breakage is found in minutes
- **Refactoring ↔ CI**: frequent small merges make wide refactorings
  feasible; well-factored code keeps changes local and conflicts rare

Cherry-picking one practice in isolation often underdelivers: synergy effects
are significant

---

## Mutual Benefit: Customer and Supplier on the Same Side

Fixed-scope contracts can set customer and supplier against each other:

- The supplier protects itself with exhaustive specifications: long, expensive
  pre-studies before any code is written
- Changes after sign-off are billed as change requests: _"it works as
  specified"_
- The customer pays for every lesson learned along the way, the supplier
  profits from them

XP looks for **win-win** instead:

- **Negotiated Scope Contract**: fix time, cost and quality; negotiate scope as
  you learn
- **Pay-Per-Use**: the supplier earns when the software delivers value
- Weekly cycles: the customer can change priorities without penalty

"Working as specified" is not the same as working for the customer

---

## The Human Side: Sustainability

Software is a marathon, not a sprint: XP aims for a pace you can keep for years

- **Energized Work**: tired developers make bad software; overtime is a warning
  sign, not a habit
- **Safety nets** keep mistakes small and stress low: baby steps, tests, CI
  - Break something? The tests tell you in minutes
  - Stuck? Your pair programming buddy is right there
  - Wrong direction? The next weekly cycle corrects it
- **Courage** grows from safety: developers dare to change, clean up, and
  experiment—courage is not recklessness
- **Code stays changeable**: constant cleanup keeps the cost of change low
  instead of piling up debt

Burnout and technical debt are the same mistake: borrowing from the future

---

## Baby Steps: Splitting Large Changes

A large change is scary: long-lived branch, painful merge, huge review,
big-bang release, hard to roll back

- Split it into **small steps**, each leaving the system working: tests green,
  integrated, deployable
- Each step is easy to review and cheap to undo: risk and complexity stay
  **manageable**
- Not trivial: finding the steps is a **skill**, and the path is often longer
  - _"Make the change easy (warning: this may be hard), then make the easy
    change"_ (Kent Beck)
  - **Parallel change**: expand ➔ migrate ➔ contract
  - **Branch by abstraction**, **feature flags**: integrate unfinished work
    without exposing it
  - **Strangler fig**: a new component takes over a legacy one's capabilities
    one by one, until the old one can be removed

If the gap is too large, build stepping stones

---

## Criticism & Limits

- **All-or-nothing**: the practices depend on each other, but full adoption
  needs commitment at all organizational levels
- **Organizational fit**: real customer involvement, sitting together,
  negotiated scope clash with distributed teams, strict hierarchies, and
  outsourcing development without also outsourcing ownership
- **Regulated environments**: audits and compliance may require processes,
  documentation or up-front design XP deliberately tries to minimize
- **Pair programming**: perceived as costly, can be exhausting, not for every
  situation
- **Evolutionary design**: without constant refactoring discipline, architecture
  can drift
- **Dogmatism risk**: "extreme" can harden into orthodoxy, but XP is
  fundamentally pragmatic: practices serve the values and adapt to context
- Even the **C3 project** was cancelled in 2000: it went live in 1997 paying
  ~10,000 employees, but never covered all payrolls

XP is not a silver bullet: know what you give up when you compromise, and why

---

## XP and Scrum: Siblings

|             | XP                                    | Scrum                                   |
| ----------- | ------------------------------------- | --------------------------------------- |
| Origin      | 1996, Chrysler C3                     | 1993, Easel Corp.; 1995 at OOPSLA       |
| Focus       | How to **build software**             | How to **organize work**                |
| Cycle       | Weekly                                | Sprint, one month or less               |
| Roles       | Whole team, real customer involvement | Product Owner, Scrum Master, Developers |
| Engineering | TDD, pairing, CI, refactoring...      | Left open: "purposefully incomplete"    |

- Their founders all signed the Agile Manifesto in 2001: Beck, Schwaber,
  Sutherland

---

## XP and Scrum: Mutual Influence

Scrum ➔ XP

- **Daily stand-up**: Coplien's pattern (1993) ➔ Scrum's daily scrum ➔ XP
  core practice (1998); XP teams later adopted Scrum's three questions
- 1995: Kent Beck asked Jeff Sutherland for Scrum's papers while shaping XP;
  according to Sutherland, XP would take the engineering practices and Scrum
  the team management

XP ➔ Scrum

- Early Scrum was pitched as a wrapper around XP: _XP@Scrum_ (Schwaber),
  _XBreed_ (Beedle), the first Scrum book (2001)
- **User stories**, **velocity**, **planning poker**: XP ideas, now everyday
  Scrum vocabulary
- The **Certified Scrum Developer** course teaches XP's engineering practices:
  TDD, pairing, refactoring, CI

---

## Scrum Needs Engineering Practices

- Scrum fits into **traditional large organizations**: its roles map onto
  existing ones, sprints feed planning and reporting, SAFe/LeSS scale it up,
  certifications make it trainable
- Sprints alone don't keep the code healthy: _"after a while progress is slow
  because the code base is a mess"_ (Martin Fowler, 2009)
- Scrum + XP complement each other: Scrum organizes **what** and **when**, XP
  keeps the code **able to change**

Sprints don't make you agile if the code can't change

---

## XP in the Age of AI

Software is still built by people... but increasingly **with** AI

- **Test-First**: tests become the spec and the guardrail for generated code
- **Ten-Minute Build / CI**: more code, faster ➔ fast automated feedback matters
  even more
- **Simplicity / YAGNI** (You Aren't Gonna Need It): code is now cheap to
  produce, but still costly to own
- **Baby Steps**: AI invites huge diffs; small, verified steps keep you in
  control
- **Pair Programming**: AI can be a tireless pair, but doesn't spread knowledge
  or ownership across the team
- **Accepted Responsibility**: the AI writes code, but people remain accountable

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

![bg right:40%](img/wizards.png)

## From Wizards to Great Habits

- _"I'm not a great programmer; I'm just a good programmer with great
  habits"_, Kent Beck
- A good methodology, applied diligently, makes the "magic" repeatable: many
  developers can become wizards

---

## Your Turn: The "Extreme" Game

Pick something your team believes is good, then:

1. **Why** is it good? Which **values** or **principles** does it serve?
2. _What if we pushed it to the **extreme**?_
   - What would **break**? What would **hurt**?
   - What would need to **work differently** for it not to break? To stop
     hurting?
   - What could we **gain** from it?
3. Does the extreme version still serve **the same values**? If not, you've
   gone too far

Often, what breaks or hurts shows you exactly what has to improve next!

---

## References

- Kent Beck with Cynthia Andres, _Extreme Programming Explained: Embrace
  Change_, 2nd edition (2004)
- Don Wells, XP values: <http://www.extremeprogramming.org/values.html>
- Manifesto for Agile Software Development: <https://agilemanifesto.org/>
- The Scrum Guide: <https://scrumguides.org/scrum-guide.html>
- Martin Fowler, _Flaccid Scrum_ (2009):
  <https://martinfowler.com/bliki/FlaccidScrum.html>
- Martin Fowler's bliki: _ParallelChange_, _BranchByAbstraction_,
  _StranglerFigApplication_: <https://martinfowler.com/bliki/>
- Chrysler C3:
  <https://en.wikipedia.org/wiki/Chrysler_Comprehensive_Compensation_System>
- Daily stand-up: <https://agilealliance.org/glossary/daily-meeting/>
- Jeff Sutherland, _Origins of Scrum_ (2007):
  <http://jeffsutherland.com/scrum/2007/07/origins-of-scrum.html>
- XP@Scrum, XBreed:
  <https://www.computerworld.com/article/1363906/xp-scrum-join-forces.html>
- Kent Beck, _Tidy First? Example_ ("make the change easy"):
  <https://tidyfirst.substack.com/p/tidy-first-example>
- "Great habits", from Fowler's _Refactoring_ (1999):
  <https://en.wikiquote.org/wiki/Kent_Beck>

---

**Thank you!**

> Questions? Remarks? Discussion welcome!
