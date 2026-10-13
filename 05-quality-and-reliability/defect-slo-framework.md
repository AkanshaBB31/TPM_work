# Defect Resolution SLO Framework

**Skill:** Service level management · **Competency:** Quality governance and proactive risk detection
**Standards:** ITIL incident & problem management, Google SRE (SLIs/SLOs)

> **Every threshold here is illustrative.** Agree real values with support, engineering and customer-facing teams, based on customer impact and contracts.

## 1. Why defect SLOs?

Without explicit targets, defects get prioritised by whoever shouts loudest. SLOs give you:
- a shared, objective definition of *late*
- an **early warning** before a commitment is missed
- trend data that shows whether quality is improving

## 2. Priority model

Rate *severity* (technical impact) and *priority* (business urgency) separately. **Priority drives the SLO.** Derive it from the impact × urgency matrix in the [triage playbook](defect-triage-playbook.md).

| Priority | Definition | Example (fictional) |
|---|---|---|
| **P1** | Core function down or data at risk; no workaround | Customers can't complete checkout |
| **P2** | Major function impaired; workaround exists | Reports load, but export fails |
| **P3** | Minor function impaired | Sorting is wrong on one column |
| **P4** | Cosmetic | Typo in a tooltip |

## 3. Targets (illustrative defaults)

```yaml
slo:
  P1: { target_days: 3,  warn_within_days: 1 }
  P2: { target_days: 14, warn_within_days: 4 }
  P3: { target_days: 30, warn_within_days: 7 }
  P4: null                       # best effort
active_states: [Open, In Progress, Reopened, In Review]
clock: calendar_days             # or business_days
```

## 4. Classification

```
age = (resolved_at or now) − created_at

resolved and age ≤ target         → ✅ MET
resolved and age > target         → ❌ BREACHED (closed late)
open     and age > target         → ❌ BREACHED (open)
open     and age > target − warn  → ⚠️ WARNING
otherwise                         → 🟢 ON TRACK
```

**Attainment % = MET ÷ (MET + BREACHED)**

A working implementation: [`slo_calculator.py`](../08-automation/examples/slo_calculator.py).

## 5. Decisions to make up front

| Question | Common choice |
|---|---|
| Calendar or business days? | Calendar days: simpler, and closer to what customers experience |
| When does the clock start? | At triage confirmation, unless contracts say otherwise |
| Does it pause while waiting on the customer? | Yes, but log each pause and cap the total |
| What if the priority changes? | Measure against the **highest** priority the defect ever had |
| Reopened defects? | Resume the original clock; don't reset it |
| What counts as resolved? | The fix is deployed to production, not just merged |

## 6. Reporting views

| View | Question it answers |
|---|---|
| **By priority** | Are we meeting our commitments on critical issues? |
| **By product area / component** | Which area is falling behind? |
| **By customer segment / environment** | Who is feeling the impact? |
| **Trend** | Is weekly attainment improving? |
| **Action list** | Which WARNING items, sorted by time left, need an owner today? |

Summary shape (fictional data):

| Priority | Total | Met | Breached | Warning | On track | Attainment |
|---|---|---|---|---|---|---|
| P1 | 12 | 10 | 1 | 1 | 0 | 91% |
| P2 | 40 | 30 | 4 | 3 | 3 | 88% |
| P3 | 95 | 80 | 3 | 4 | 8 | 96% |

## 7. Alerting cadence

| Alert | Frequency | Audience | Content |
|---|---|---|---|
| New critical defect | Near real time | On-call, leads | Item, priority, area |
| Approaching breach | Daily | Owning teams | WARNING items + time left, grouped by owner |
| Breached | Daily | Leads & managers | BREACHED items grouped by area |
| Digest | Weekly | Leadership | Attainment %, trend, top risks |

Implementation pattern: [scheduled alerting](../08-automation/scheduled-alerting-pattern.md).

## 8. Breach response

1. The owner posts a recovery ETA and the blocker within 1 business day.
2. No owner or no ETA → escalate to the engineering manager.
3. Repeated breaches in one area → a problem-management review of the root cause, not the symptoms.

## 9. Pitfalls

- **Priority gaming:** audit downgrades. A sudden drop in P1 volume is a signal.
- **Overwritten history:** trackers overwrite priority and status, so rebuild history from the change log and keep daily snapshots so that trend lines stay stable.
- **Alert fatigue:** send one grouped digest per owner, not one message per defect.
