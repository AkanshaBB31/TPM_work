# Sprint Reporting & Forecasting

**Skill:** Agile delivery governance · **Competency:** Sprint transparency, predictability tracking and range-based forecasting

## Part 1: One-page sprint report

The report answers four questions: *What did we commit to? What did we finish? What changed? What do we need?*

---

### Sprint 4: Team Atlas · 2026-04-13 → 2026-04-24 *(fictional)*

**Headline:** Delivered 31 of 38 committed points (82%). Checkout redesign shipped. Two stories carried over because of a late API contract change.

| Committed | Completed | Say/Do | Carried over | Added mid-sprint | Defects closed |
|---|---|---|---|---|---|
| 38 pts | 31 pts | 82% | 7 pts (2 stories) | 5 pts | 9 |

**Sprint goal outcome**
- ✅ Checkout redesign live for 100% of web users
- ⚠️ Saved-cart API is code complete; release blocked on contract sign-off

**Carry-over analysis**

| Item | Points | Reason | Plan |
|---|---|---|---|
| Saved-cart API | 5 | Upstream contract changed on day 6 | Top of next sprint |
| Cart analytics events | 2 | Under-estimated | Re-estimated to 3 |

**Risks & asks:** the platform team should confirm the contract freeze by Tuesday.
**Retro highlights:** keep pairing on complex stories; lock interface contracts before planning.

---

## Part 2: Predictability metrics

> Use velocity to **forecast**, never to judge. Never compare velocity across teams.

| Metric | Formula | Healthy signal (illustrative) |
|---|---|---|
| Velocity | Points completed per sprint | Stable band (±20%) |
| Say/Do ratio | Completed committed ÷ committed | 80–100% |
| Scope churn | (Added + removed mid-sprint) ÷ committed | < 15% |
| Carry-over rate | Carried-over points ÷ committed | < 15% |
| Rolling average | Mean of the last 3–6 sprints | Planning baseline |

### Trend table

| Sprint | Quarter | Committed | Completed | Say/Do | Added | Carried |
|---|---|---|---|---|---|---|
| S1 | Q1 | 40 | 30 | 75% | 6 | 10 |
| S2 | Q1 | 36 | 32 | 89% | 3 | 4 |
| S3 | Q1 | 38 | 35 | 92% | 2 | 3 |
| **Q1 avg** | | **38** | **32.3** | **85%** | | |
| S1 | Q2 | 38 | 31 | 82% | 5 | 7 |

**Rule:** roll up each quarter on its own, so that one quarter never hides another.

## Part 3: Forecasting the backlog

```
Remaining backlog:         120 pts
Rolling velocity (last 4): 30–35 pts
Forecast: 120 / 35 = 3.4 … 120 / 30 = 4.0  →  4 sprints (range 4–5 with buffer)
```

Always forecast as a **range**. For flow-based teams, use throughput (items per week) and Monte Carlo simulation instead of points.

## Anti-patterns

- Inflating estimates to "hit" velocity
- Counting partially done stories
- Re-baselining the commitment mid-sprint to hide misses
