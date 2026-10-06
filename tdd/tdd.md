---
author: Christian Apolloni
date: 2026-09-26
---

# Test-Driven Development (TDD)

**What it really is, why it matters, and practical advice you can use today**

---

## Why TDD?

- Designing for testability from the start leads to robust, maintainable code
- Small, verified steps make change **less risky and less stressful**
- Issues surface early, while they are still cheap to fix

**Today's Goal:**

- Understand TDD
- Learn practical workflows you can actually use
- Cut through the myths and confusion—see what works (and what doesn't)

---

## What Is TDD—In One Slide

- A software development process where **tests are written before code**
- Cycle: **Red ➜ Green ➜ Refactor**
  - Write a failing test, run it, see it fail (**Red**)
  - Write just enough code to pass the test (**Green**)
  - Clean up the code, tests stay green (**Refactor**)
- Repeat for each small behavior/change

---

## TDD's Origins: The XP Revolution

- Born from
  [Extreme Programming (XP)](https://en.wikipedia.org/wiki/Extreme_programming)
  in the 1990s
- "Test-first" pushed to its limits ➔ TDD
- Kent Beck calls it a **rediscovery**: an old book advised typing the expected
  output tape before writing the program
- Tooling made it practical: SUnit (Smalltalk), then JUnit (Beck & Gamma,
  1997) and the whole xUnit family
- 2002: Kent Beck, _Test-Driven Development: By Example_
- Key insight: early, repeated, automated feedback drives quality

---

## The TDD Cycle in Practice

1. Write a small test for new behavior ➔ run it, it fails (_Red_)
2. Implement just enough code to pass ➔ tests pass (_Green_)
3. Refactor: remove duplication, improve names and structure ➔ tests _still_
   pass (_Refactor_)

- Seeing the test fail first proves it can fail: a test that never fails tests
  nothing
- Keep a **test list**: write down the next ideas, but write only one test at a
  time
- Refactoring changes structure, not behavior—performance tuning is a separate
  step

_Each code change is verified, so you never wander far from working software
or spend hours tracking down what broke._

---

## Example: Fake It, Then Triangulate

```java
// Red: write a test, run it, see it fail
@Test
void addsTwoNumbers() {
    assertEquals(5, new Calculator().add(2, 3));
}

// Green: the simplest thing that passes ("fake it")
int add(int a, int b) {
    return 5;
}

// Red: a second example forces the real logic ("triangulate")
@Test
void addsNegativeNumbers() {
    assertEquals(0, new Calculator().add(-1, 1));
}

// Green: generalize; refactor if needed
int add(int a, int b) {
    return a + b;
}
```

When the implementation is obvious, just write it: small steps are an option,
not an obligation

---

## How TDD Makes Development More Efficient

- Catches mistakes and misunderstandings _immediately_, not weeks/months later
- Prevents "debugging spirals" and last-minute emergencies—a failing test
  pinpoints the problem as it happens
- Makes code safer to change and refactor (tests are always green or you know
  exactly what broke)
- Reduces context switching and long PR review cycles—work is done in small,
  verified steps
- Automated tests double as living documentation: easy onboarding & faster
  handoffs
- Less wasted time on QA catch-up, manual testing, or "works on my machine"
  problems
- Overall: More time building features, less time in bugfix or firefighting mode

---

## What the Research Says

- **Microsoft & IBM** (Nagappan et al., 2008), four industrial teams:
  - Pre-release defect density **40–90% lower** than similar non-TDD projects
  - Initial development time **15–35% higher**
- **What drives the benefits?** (Fucci et al., 2017), 39 professionals:
  - Quality and productivity followed **short, steady cycles**
  - Writing the test first or right after made no significant difference

TDD is an investment: you pay up front and save on debugging, rework and
defects. Much of the payoff comes from the **small steps**.

---

## Common TDD Myths (Reality Check)

- "TDD is about 100% coverage" ❌
- "TDD means writing all the tests up front" ❌
- "TDD means never debugging again" ❌
- "TDD is for trivial toy projects only" ❌

**Reality:** TDD is a thinking and design tool

---

## When TDD Fits—and When It Doesn't

- Not a religion, nor a silver bullet
- Every tool has pros, cons, ideal contexts, and a learning curve
- Some contexts—exploratory work, UI layout, hard-to-test systems—are less
  suited for strict TDD
- Legacy code is usually hard to test: expect difficulties at first, it gets
  easier as more of it becomes properly testable
- Use where it helps; when you skip it, know what you give up
  - "We do TDD, except when we're in a hurry": the hurry is when you need it
    most

---

## The Test Structure (Useful for More than Just Tests!)

- **Setup:** Prepare objects, state, dependencies
- **Exercise:** Do the action (call function, endpoint, UI action)
- **Verify:** Ensure the expected outcome
- **Teardown:** Clean up (optional, often implicit)

_The Four-Phase Test (Gerard Meszaros, xUnit Test Patterns); also known as
Arrange-Act-Assert_

---

## Why the Test Structure Matters

- Forces you to think about:
  - What needs to exist for success (dependencies, contracts)
  - How the system is used (APIs, UI, events)
  - What "correct" looks like for the user
- This structure **shapes your code**: better design, fewer surprises later

---

## What TDD Helps You Discover Early

- **Setup:**
  - Unexpected dependencies or poor encapsulation
- **Exercise:**
  - Missing or unclear required information
  - Awkward/unclear APIs
- **Verify:**
  - You can't observe the necessary outcome

Hard to test is often a sign of hard to use: listen to the tests

**Finding these in tests is fast and cheap; finding them in code review or prod
is not.**

---

## TDD: The Test Is the First User

- "First user" perspective:
  - Forces developer to use and think about their code like a real consumer
    would
  - Promotes better, more usable API/UX early
- Surfaces hidden edge cases, missing behaviors, or areas for improvement

---

## TDD vs BDD (Behavior-Driven Development)

- BDD (Dan North, 2006) builds on TDD, with a focus on concrete user scenarios
  and business outcomes
- **Given/When/Then:**
  - Given (setup)
  - When (exercise)
  - Then (verify)
- BDD helps when collaboration/communication between domains (devs, business,
  QA) matters most

---

## Practical TDD: Tips and Pitfalls

- Write tests that matter—focus on behaviors, not trivial getters/setters
- Test behavior, not implementation details: tests that break on every refactor
  get in the way
- Favor smaller, isolated tests, not monster end-to-end scripts—this makes
  debugging and iteration lightning fast
- Mocks/stubs: prefer real code paths where practical (the "classicist" school);
  the "mockist" school uses them to design interactions—pick deliberately
- Fixing a bug? Start with a failing test that reproduces it
- Let your tests drive better names, refactors, decoupling (good tests make
  changes _easier_ and _quicker_)
- Spikes and proofs of concept don't need the full discipline, but TDD can
  still help you explore and shape the design

---

## TDD in the Age of AI Agents

Agents iterate until a check passes: the tests become **the spec** and **the
stop condition**

- **You own Red**: write or review the tests first, see them fail for the right
  reason, then let the agent make them green
- **Guard the tests**: agents may "pass" by special-casing, weakening
  assertions, mocking everything or deleting tests ➔ keep tests off-limits
  while implementing, review test diffs first
- **Tests written after the code** tend to assert what it _does_, not what it
  _should_ do
- **Baby steps**: one test at a time keeps the diffs small enough to review
- **Refactor still matters**: agents produce working code fast—and duplication
  just as fast; a green suite makes cleanup cheap
- **Fast tests**: the suite runs in every iteration of the agent's loop

The agent writes the code; the tests say what "done" means

---

## Tests as a Language for Agents

A domain-specific test API makes tests cheap to write and easy to review, for
people and agents alike

```java
@Test
void rejectsOrderOverCreditLimit() {
    Customer customer = testHelper.customerWithCreditLimit(100); // Setup
    OrderResult result = testHelper.placeOrder(customer, 150);   // Exercise
    testHelper.assertRejected(result, "credit limit exceeded");  // Verify
}
```

- **Test helpers** (`testHelper`, builders, fixtures) speak the domain: the
  agent writes short tests instead of reinventing setup every time, and you
  review intent, not plumbing
- **Reference tests as templates**: _"`OrderServiceTest` is your template for
  how I want tests written"_, in the prompt or in `CLAUDE.md`/`AGENTS.md`
- **Consistency compounds**: each new test in the same style is one more example
  for the agent to follow

---

## TDD—Key Takeaways

- Maximizes feedback, minimizes costly surprises, and keeps **development
  velocity** sustainable
- Best used for new features, bug fixes, or as a design/thinking aid
- Use TDD to go faster and safer, not just to "increase test coverage"
- With AI agents, tests are how you tell them what "done" means
- Combine with other strategies and real-world pragmatism

---

## References

- Kent Beck, _Test-Driven Development: By Example_ (2002)
- Martin Fowler,
  [Test-Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html)
- Extreme Programming: <https://en.wikipedia.org/wiki/Extreme_programming>
- Gerard Meszaros, _xUnit Test Patterns_ (2007), Four-Phase Test:
  <http://xunitpatterns.com/Four%20Phase%20Test.html>
- Dan North, _Introducing BDD_ (2006): <https://dannorth.net/introducing-bdd/>
- Nagappan et al., _Realizing quality improvement through test driven
  development_ (2008):
  <https://www.microsoft.com/en-us/research/blog/exploding-software-engineering-myths/>
- Fucci et al., _A Dissection of the Test-Driven Development Process_ (2017):
  <https://arxiv.org/abs/1611.05994>
- Claude Code best practices, _Give Claude a way to verify its work_:
  <https://code.claude.com/docs/en/best-practices>

---

**Thank you!**

> Questions? Remarks? Discussion welcome!
