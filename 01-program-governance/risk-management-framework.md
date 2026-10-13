# Risk Management Framework

**Skill:** Program governance · **Competency:** Proactive risk identification and response

## 1. Lifecycle

```
Identify → Assess → Plan response → Monitor → Close, or convert to an issue
```

## 2. Identification techniques

- **Pre-mortem:** "It's launch day and we failed. Why?" Everyone writes silently first, then the reasons are shared.
- **Assumption audit:** list every assumption in the plan and ask *what if this is false?*
- **Dependency walk:** trace every external input to an owner and a committed date.
- **Historical review:** read the retrospectives and incident reviews from similar efforts.

## 3. Scoring: Probability × Impact

| P \ I | 1 Minimal | 2 Minor | 3 Moderate | 4 Major | 5 Severe |
|---|---|---|---|---|---|
| **5 Almost certain** | 5 | 10 | 15 | 20 | 25 |
| **4 Likely** | 4 | 8 | 12 | 16 | 20 |
| **3 Possible** | 3 | 6 | 9 | 12 | 15 |
| **2 Unlikely** | 2 | 4 | 6 | 8 | 10 |
| **1 Rare** | 1 | 2 | 3 | 4 | 5 |

| Score | Rating | Expected response |
|---|---|---|
| 15–25 | 🔴 High | Response plan within 48h; visible in the executive report and at steering |
| 8–14 | 🟠 Medium | Response plan within 1 week; reviewed weekly |
| 1–7 | 🟢 Low | Owner monitors; reviewed monthly |

Score impact as the **highest** of: schedule slip, scope loss, quality or compliance exposure, cost variance, or reputational damage.

## 4. Response strategies

| Strategy | When to use it |
|---|---|
| **Avoid** | Change the plan so the risk can't occur |
| **Mitigate** | Reduce its probability or impact |
| **Transfer** | Move the impact to a third party (contract, insurance, vendor SLA) |
| **Accept** | Low score, or a cost that isn't justified. Set a contingency. |
| **Escalate** | The response is outside the team's authority (see the [escalation playbook](../09-leadership/escalation-playbook.md)) |

## 5. Leading indicators

- Throughput or velocity falling for 2 or more sprints in a row
- A growing number of blocked items
- Defect inflow exceeding outflow for 3 or more weeks
- Repeated slips on dependency dates
- Unplanned work above roughly 20% of capacity

## 6. Reporting format

> **[🔴 R-07] Upstream release slip:** P4 × I4 = 16
> *Impact:* UAT start moves 1 week if this isn't resolved by <date>.
> *Response:* Mitigate. Build against a contract stub and integration-test once the API is available.
> *Ask:* None yet. Escalate on <date> if there's still no committed date.
