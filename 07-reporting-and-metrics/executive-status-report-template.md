# Executive Status Report Template

**Skill:** Executive communication · **Competency:** Synthesis, decision framing and escalation

> **Rule:** an executive should understand the status in 30 seconds and know exactly what you need from them in 60. Lead with the conclusion, and keep it to one screen. Link to the detail rather than pasting it in.

---

## Program Phoenix: Week of 2026-05-04 *(fictional)*

**Overall: 🟠 Amber** (was 🟢 last week)
**Bottom line:** On track for feature-complete on 06-12. UAT start is at risk by 1 week because of a vendor API delay.

### Decisions / help needed
1. **Approve 2 weeks of contractor support for integration testing** by 05-08. *Recommendation: approve. It protects the launch date.* Without a decision, UAT slips 1 week.

### Health by dimension

| Dimension | Status | Trend | Comment |
|---|---|---|---|
| Schedule | 🟠 | ↓ | UAT at risk by +1 week (RAID R-07) |
| Scope | 🟢 | → | No change |
| Quality | 🟢 | ↑ | Open high-priority defects down from 9 to 4; SLO attainment 91% (target 90%) |
| Resourcing | 🟢 | → | |
| Budget | 🟢 | → | |

### Milestones

| Milestone | Baseline | Forecast | Status |
|---|---|---|---|
| Design complete | 03-20 | 03-20 | ✅ Done |
| Feature complete | 06-12 | 06-12 | 🟢 |
| UAT start | 06-15 | 06-22 | 🟠 |
| Launch | 07-06 | 07-06 | 🟢 |

### Quarterly commitments
9 of 24 delivered; 19–21 expected (see [commitment tracking](../01-program-governance/quarterly-commitment-tracking.md)).

### Progress since last update (outcomes, not activity)
- The product owner accepted the checkout flow
- Push preferences shipped a week early

### Top risks & issues

| ID | Description | Impact | Response | Owner |
|---|---|---|---|---|
| R-07 | Vendor sandbox unstable | UAT +1 week | Contract stub; contractor support (ask above) | QA lead |

### Next two weeks
- Integration testing against the stub
- Load test of the release candidate

---

## RAG definitions (agree these up front and include them in every report)

| Status | Meaning |
|---|---|
| 🟢 Green | On track; no help needed |
| 🟠 Amber | At risk; a recovery plan is in place; we may need help |
| 🔴 Red | Will miss a commitment without intervention; a decision or resources are needed now |

## Writing rules

- Write outcomes ("Checkout flow accepted"), not activity ("Worked on checkout").
- Every 🟠 or 🔴 needs a **cause, an impact and a plan**.
- Explain every status change since the last report.
- Show the trend, not just the current state.
- Never go straight from 🟢 to 🔴. If that happens, the earlier signals were missed.
