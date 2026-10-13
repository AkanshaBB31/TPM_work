# RAID Log Template

**Skill:** Program governance · **Standard:** PMBOK risk & issue management

A RAID log keeps **R**isks, **A**ssumptions, **I**ssues and **D**ependencies in one place, so nothing a delivery depends on stays implicit. Score risks with the [risk management framework](risk-management-framework.md).

## Definitions

| Type | It is… | Key question | Trigger to log |
|---|---|---|---|
| **Risk** | An uncertain future event that would affect objectives | What *might* happen? | "This could…" |
| **Assumption** | Something treated as true without proof | What are we betting on? | "We're planning as if…" |
| **Issue** | A risk that has already happened | What's hurting us now? | "This *is* happening" |
| **Dependency** | Work owned by someone else that we need | Who are we waiting on? | "We can't finish until…" |

## Log

| ID | Type | Description | Owner | P | I | Score | Response | Escalation trigger | Due | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| R-01 | Risk | Because the payment vendor's sandbox is unstable, integration testing may stall, delaying UAT | QA lead | 3 | 4 | 12 | **Mitigate:** build a contract stub; agree a sandbox SLA | Sandbox down > 2 days | 2026-05-10 | Open |
| A-01 | Assumption | Design system v3 components are ready before sprint 4 | Design lead | | | | Validate at sprint 3 review | Not confirmed by 04-20 | 2026-04-20 | Validating |
| I-01 | Issue | Staging data refresh failed; regression blocked for 2 teams | Platform lead | | 4 | | Manual reseed tonight; root cause by Friday | | 2026-04-15 | In progress |
| D-01 | Dependency | Identity team to ship SSO scopes API | Eng manager | | | | Weekly sync; interface contract agreed | Not in staging by 05-01 | 2026-05-01 | On track |

*All rows are fictional examples. Use roles, not names, in shared templates.*

## Operating rhythm

| When | What |
|---|---|
| Weekly | Owners update their items; the PM reviews everything scored ≥ 8 |
| Fortnightly | Steering review of the top 5 risks and any overdue dependencies |
| Monthly | Summary to sponsors: new, closed, trending up |
| Close-out | Turn closed items into lessons learned |

## Hygiene rules

- Every row has **exactly one named owner** and a **date**.
- Write risks as *"Because of [cause], [event] may occur, leading to [effect]."*
- An assumption left unvalidated for more than 2 weeks becomes a risk. One that turns out false becomes an issue immediately.
- A dependency without a committed date is a risk by default.
- Close an issue only when its root cause is addressed. Keep closed rows, with their resolution, so you have history.
