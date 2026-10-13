# Definition of Ready & Backlog Decomposition

**Skill:** Backlog management & requirements engineering · **Competency:** Turning product intent into deliverable work

## 1. Work hierarchy

```
Initiative / Goal       → quarterly business outcome
  └── Epic / Feature    → shippable capability (1–3 sprints)
        └── Story       → user-visible slice that fits in one sprint
              └── Task  → engineering step (hours to 2 days)
```

## 2. Requirements readiness review

Run this before a requirements document (PRD) or epic goes to planning. It catches gaps while they're still cheap to fix.

| Area | Ready when… |
|---|---|
| **Traceability** | Links to the business goal it supports; every requirement maps to a goal |
| **Problem** | States the user or business problem and its evidence, not only a solution |
| **Goals & non-goals** | Both explicit; non-goals prevent scope creep |
| **Success metrics** | Measurable, with a baseline and a target |
| **Users & journeys** | Primary personas and key journeys described |
| **Functional requirements** | Numbered, testable, prioritised (MoSCoW) |
| **Non-functional requirements** | Performance, security, accessibility, compliance |
| **Edge cases** | Error states and boundary conditions described |
| **Dependencies** | Other teams and systems listed, with dates |
| **Clarity** | No unresolved "TBD"s on the critical path; open questions have owners and due dates |
| **Feasibility** | Engineering has reviewed technical risk; rough size known; designs exist for UI changes |

| Outcome | Meaning |
|---|---|
| ✅ Ready | Proceed to backlog breakdown |
| 🟡 Ready with gaps | Can start; gaps are tracked as tasks |
| 🔴 Not ready | Back to the author with specific feedback |

> An AI assistant can do a first pass against this checklist (see [AI-assisted PM workflows](../08-automation/ai-assisted-pm-workflows.md)). A person still makes the readiness call.

## 3. Breakdown steps

1. **List the user journeys** in the requirement.
2. **Slice vertically.** Each story is a thin, testable, end-to-end slice, not a single layer.
3. **Check INVEST:** Independent, Negotiable, Valuable, Estimable, Small, Testable.
4. **Add non-functional work explicitly:** performance testing, security review, docs, release notes.
5. **Map dependencies.** Log cross-team ones in the [dependency board](../02-technical-program-management/cross-team-dependency-management.md).
6. **Sequence the work.** High-risk and high-learning items go first. Use a time-boxed **spike** when uncertainty is too high to estimate.

## 4. Story-splitting patterns

| Pattern | Example |
|---|---|
| By workflow step | "Add to cart" before "Checkout" |
| By business rule | Standard shipping first, express later |
| By data variation | One currency first, then multi-currency |
| Happy path first | Success flow, then error handling |
| By interface / platform | API first, then web, then mobile |

## 5. Story-level Definition of Ready

- [ ] Story in "As a / I want / so that" form, or a clear job statement
- [ ] Acceptance criteria in Given/When/Then form
- [ ] Estimated by the team; no bigger than half a sprint
- [ ] Dependencies identified and unblocked, or explicitly accepted
- [ ] UX/design attached where relevant

## 6. Team Definition of Done

- [ ] Code reviewed and merged; automated tests pass
- [ ] Acceptance criteria verified
- [ ] Documentation and release-notes entry updated
- [ ] Deployed to the agreed environment
- [ ] No open critical or high defects against the story

## 7. Worked example (fictional)

**Epic:** Self-service password reset

| Story | Acceptance criteria (abridged) |
|---|---|
| Request reset link | Given a registered email, when I submit, then I receive a link within 2 minutes |
| Set new password | Given a valid link, when I set a compliant password, then I can log in |
| Expired link | Given a link past its expiry, then I see a clear message and can request a new one |
| Audit trail | Every reset attempt is logged with a timestamp and its outcome |

**Traceability check:** every requirement maps to at least one story, and every story maps back to the epic goal.
