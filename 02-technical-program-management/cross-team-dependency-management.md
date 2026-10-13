# Cross-Team Dependency Management

**Skill:** Technical program management · **Competency:** Delivering outcomes that span multiple teams, systems and release cycles

Most program slips are dependency slips. This playbook makes dependencies explicit, dated and owned.

## 1. Dependency types

| Type | Example (fictional) | Typical risk |
|---|---|---|
| **Technical / API** | Checkout needs a new endpoint from the Identity service | Contract churn, late delivery |
| **Data** | Analytics needs a new event schema | Schema mismatch |
| **Environment** | Integration testing needs a shared staging slot | Contention |
| **Release** | Mobile release must follow a backend release | Version incompatibility |
| **Vendor** | Payment provider must enable a feature | No control over the timeline |
| **People / skills** | Only one engineer knows the legacy module | Single point of failure |

## 2. Dependency board

| ID | Consumer team | Provider team | What's needed | Need-by | Committed date | Gap (days) | Status | Contract agreed? |
|---|---|---|---|---|---|---|---|---|
| DEP-01 | Checkout | Identity | SSO scopes API | 05-01 | 05-08 | **−7** | 🟠 At risk | ✅ |
| DEP-02 | Analytics | Checkout | `order_completed` v2 event | 05-15 | 05-10 | +5 | 🟢 | ✅ |
| DEP-03 | Mobile | Platform | Feature flag SDK upgrade | 06-01 | — | n/a | 🔴 No commitment | ❌ |

**Rules**
- A gap below zero, or a blank committed date, automatically creates a RAID risk.
- Every dependency has a named owner on **both** sides.

## 3. Mapping the critical path

1. List the milestones and the work packages behind them.
2. Draw the dependency arrows (provider → consumer).
3. Find the longest chain. That's the critical path.
4. Put the most management attention on items that are **on the critical path and owned outside your team**.

```
[Identity API]──▶[Checkout integration]──▶[E2E test]──▶[Launch]
       ▲                                       ▲
[Contract sign-off]               [Staging slot booked]
```

## 4. De-risking techniques

| Technique | How it helps |
|---|---|
| **Contract-first** | Agree the API/event schema early; both sides build against it |
| **Stubs & mocks** | The consumer isn't blocked by the provider's timeline |
| **Feature flags** | Decouple deploy from release; ship dark |
| **Version compatibility** | Backward-compatible changes with expand/contract migrations |
| **Integration milestones** | Schedule an early "first call works" milestone, not just the final date |
| **Buffer on the critical path** | Explicit buffer for external dependencies only |

## 5. Cadence

- **Weekly 15-minute dependency sync:** active dependencies only, sorted by gap.
- **Escalate** when a dependency is on the critical path with a negative gap and no recovery plan (see the [escalation playbook](../09-leadership/escalation-playbook.md)).

## 6. Health metrics

- % of dependencies with a committed date
- % with an agreed contract
- Count of dependencies with a negative gap
- Average slip of dependency dates per quarter
