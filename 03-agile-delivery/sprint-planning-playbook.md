# Sprint Planning Playbook

**Skill:** Agile delivery · **Standard:** Scrum Guide

## Inputs (must exist before planning)

- [ ] Backlog ordered by the product owner
- [ ] Top items meet the [Definition of Ready](definition-of-ready-and-backlog-decomposition.md)
- [ ] Team capacity calculated (leave, holidays, on-call, ceremonies)
- [ ] Last sprint's carry-over reviewed
- [ ] Known dependencies and release dates visible

## Capacity calculation

```
Available days    = Team members × Sprint days − Leave − Holidays
Focus factor      = 0.6–0.8   (meetings, support, reviews)
Planned capacity  = Available days × Focus factor
```

*Example (fictional):* 6 people × 10 days − 4 days of leave = 56 days. 56 × 0.7 ≈ **39 focus days**.

If you plan in story points, plan to the **rolling 3-sprint average velocity**, scaled by this sprint's capacity relative to normal (see [forecasting](sprint-reporting-and-forecasting.md)).

## Agenda (2-week sprint, about 2 hours)

| Time | Part | Output |
|---|---|---|
| 15 min | **Why:** the product owner proposes the sprint goal | Draft goal |
| 60 min | **What:** the team pulls items up to capacity | Sprint backlog |
| 35 min | **How:** break items into tasks; surface risks and dependencies | Task plan, owners |
| 10 min | **Commit:** confidence vote (fist-of-five) | Final sprint goal |

## Capacity allocation

| Bucket | Typical share |
|---|---|
| Sprint goal work | 60–70% |
| Production defects / support | 10–20% |
| Tech debt & improvements | 10–15% |
| Buffer | 5–10% |

## A good sprint goal

- One or two sentences, outcome-focused, testable
- ✅ "Customers can reset their password by email without contacting support"
- ❌ "Complete tickets 1–14"

## Anti-patterns

- Planning to 100% capacity
- Pulling in items that aren't ready
- Treating the sprint goal as optional
- Leaving cross-team dependencies unspoken
