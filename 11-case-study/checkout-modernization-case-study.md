# Case Study: Checkout Modernization Program

> **Fictional case study.** Example Co., Kestrel Pay, every team, person and number are invented. It shows how the frameworks in this repository fit together on a single program.

| | |
|---|---|
| **Organisation** | Example Co.: a mid-size online retailer |
| **Program** | Checkout Modernization |
| **Duration** | 26 weeks · 5 Jan – 26 Jun 2026 (Q1–Q2) |
| **Teams** | Checkout Web (6), Checkout API (5), Payments (4), QA (3), Platform/SRE (3, shared) |
| **External parties** | Identity team (internal dependency), Kestrel Pay (payment vendor) |
| **My role** | Technical Program Manager, accountable for delivery, governance and release |

---

## 1. The problem

Checkout was a module inside a legacy monolith. It was slow, fragile and released once a month.

| Baseline (Jan 2026) | Value |
|---|---|
| Checkout completion rate | 61% |
| Checkout p95 latency | 2.8 s |
| Change failure rate | 24% |
| Deployment frequency | ~1 per month |
| Open P1/P2 checkout defects | 18 |
| Defect SLO attainment | 78% |

---

## 2. Initiation (weeks 1–2)

**Framework used:** [Program charter](../02-technical-program-management/program-charter-template.md), [Stakeholder map & RACI](../06-stakeholder-management/stakeholder-map-and-raci.md), [Communication plan](../06-stakeholder-management/communication-plan-template.md)

**Charter outcomes (signed off at week 2)**

| Outcome | Measure | Baseline | Target |
|---|---|---|---|
| More customers complete checkout | Completion rate | 61% | ≥ 70% |
| Faster checkout | p95 latency | 2.8 s | < 1.5 s |
| Safer releases | Change failure rate | 24% | < 10% |
| Faster releases | Deployment frequency | Monthly | Weekly |
| Better quality | Defect SLO attainment | 78% | ≥ 90% |

**Scope:** a new checkout UI, a new checkout service, Kestrel Pay integration and saved carts.
**Explicitly out of scope:** loyalty points and international tax.

**Stakeholder insight:** the Head of Support was *Concerned*, because the last checkout change had caused a spike in tickets. I moved Support into "manage closely", invited them to defect triage and gave them a weekly SLO digest. By week 8 their stance was *Supportive*.

---

## 3. Planning (weeks 3–4)

**Framework used:** [Definition of Ready & backlog decomposition](../03-agile-delivery/definition-of-ready-and-backlog-decomposition.md), [Cross-team dependency management](../02-technical-program-management/cross-team-dependency-management.md), [RAID log](../01-program-governance/raid-log-template.md), [Quarterly commitment tracking](../01-program-governance/quarterly-commitment-tracking.md)

**Requirements readiness review:** the first draft of the PRD was 🟡 *Ready with gaps*, with **7 gaps**. The three most important:
1. No baseline for the latency target
2. No security or compliance requirements for card data
3. No error-state design for declined payments

All 7 were closed in 6 working days.

**Decomposition:** 5 epics → 41 stories → sequenced so that high-risk work came first.

| Epic | Stories | Risk |
|---|---|---|
| E1 New checkout UI | 11 | Medium |
| E2 Checkout service API | 10 | High |
| E3 Kestrel Pay integration | 9 | **High** |
| E4 Saved carts | 7 | Low |
| E5 Pay Later | 4 | Medium |

**Dependency board (week 4)**

| ID | Provider | Need | Need-by | Committed | Gap | Status |
|---|---|---|---|---|---|---|
| DEP-01 | Identity team | Session token API | 06 Mar | 13 Mar | −7 d | 🟠 |
| DEP-02 | Kestrel Pay | Stable sandbox with tokenisation | 20 Feb | "ASAP" | n/a | 🔴 |
| DEP-03 | Platform | Feature-flag service upgrade | 24 Apr | 17 Apr | +7 d | 🟢 |

**Top RAID risks**

| ID | Risk | P×I | Response |
|---|---|---|---|
| R-01 | Because Kestrel Pay's sandbox is unstable, integration testing may stall, delaying feature-complete | 4×4 = **16** 🔴 | Mitigate: contract stub; escalate for a sandbox SLA |
| R-02 | Legacy cart data may not map cleanly to the new model, risking data loss at cut-over | 3×4 = 12 🟠 | Mitigate: dry-run migrations every sprint |
| R-03 | Shared SRE capacity may be pulled into other incidents | 3×3 = 9 🟠 | Accept, and book SRE time for launch weeks |

**Quarterly commitments baselined:** Q1 = 8 commitments, Q2 = 10 commitments.

---

## 4. Execution (weeks 5–22)

**Framework used:** [Sprint planning](../03-agile-delivery/sprint-planning-playbook.md), [Sprint reporting & forecasting](../03-agile-delivery/sprint-reporting-and-forecasting.md), [Escalation playbook](../09-leadership/escalation-playbook.md), [Decision log](../01-program-governance/decision-log-template.md)

**Sprint predictability**

| Sprint | Committed | Completed | Say/Do | Note |
|---|---|---|---|---|
| S1 | 34 | 28 | 82% | Ramp-up |
| S2 | 36 | 32 | 89% | |
| S3 | 38 | 35 | 92% | |
| **S4** | **38** | **26** | **68%** | Vendor sandbox down 6 days |
| S5 | 36 | 33 | 92% | Contract stub in place |
| S6 | 38 | 36 | 95% | |
| S7 | 40 | 37 | 93% | |
| S8 | 38 | 36 | 95% | |
| S9 | 32 | 31 | 97% | Hardening sprint |

**The sprint 4 dip and the escalation.** R-01 materialised, and the sandbox was down for 6 of 10 days. I escalated to the VP of Engineering and the vendor manager using SBAR:

> **S:** The Kestrel Pay sandbox has been unavailable for 6 of the last 10 days. **B:** We've raised 4 vendor tickets since 20 Feb and synced weekly; there's no SLA on the sandbox. **A:** Each further week of instability moves feature-complete by about a week and puts the June launch at risk. **R:** Approve (a) building a contract stub this sprint, and (b) a sandbox-availability clause in the renewal. Decision needed by 20 Mar.

**Decisions recorded**

| ID | Decision | Why |
|---|---|---|
| DEC-003 | Release behind feature flags with phased rollout (5% → 25% → 100%) | Decouples deploy from release; limits the blast radius |
| DEC-004 | Build a Kestrel Pay contract stub; add a sandbox SLA to the vendor renewal | Unblocks the teams; transfers the risk to the vendor |
| DEC-006 | Defer **Pay Later (E5)** to Q3 | Protects the launch date; fewer than 8% of users had asked for it |

**Executive status, week 12** ([template](../07-reporting-and-metrics/executive-status-report-template.md)):

> **Overall: 🟠 Amber** (was 🟢). **Bottom line:** feature-complete forecast moves from 15 May to 22 May because of vendor sandbox instability; the launch date of 5 June is held by using buffer. **Decision needed:** approve deferring Pay Later to Q3 (recommended).

---

## 5. Quality governance (throughout)

**Framework used:** [Defect SLO framework](../05-quality-and-reliability/defect-slo-framework.md), [Triage playbook](../05-quality-and-reliability/defect-triage-playbook.md), [Scheduled alerting](../08-automation/scheduled-alerting-pattern.md), [Tracker hygiene](../08-automation/tracker-hygiene-checks.md)

- Defect SLOs published at week 3; triage moved from ad hoc to **daily 15 minutes plus a weekly ageing review**.
- A **daily SLO digest** (an automated chat post grouped by owner) replaced manual chasing.
- Weekly **tracker hygiene** checks raised data quality from **71% to 94%**, which made the dashboards trustworthy.

| Week | 2 | 6 | 10 | 14 | 18 | 22 | 26 |
|---|---|---|---|---|---|---|---|
| SLO attainment | 78% | 81% | 83% | 88% | 91% | 91% | **93%** |

---

## 6. Release (weeks 21–24)

**Framework used:** [Operational readiness review](../02-technical-program-management/operational-readiness-review.md), [Change gate & go/no-go](../04-release-management/change-readiness-gate-and-go-no-go.md), [Release readiness checklist](../04-release-management/release-readiness-checklist.md), [Rollback plan](../04-release-management/rollback-planning-template.md)

**The operational readiness review found 2 gaps** (both closed):
1. There was no alert on the **payment success rate**, only on HTTP errors. An alert was added.
2. The load test only reached 1.2× peak. It was re-run at 2×, which exposed a connection-pool limit, and the limit was fixed.

**Gate at T-3 (2 June): 14 items**

| Outcome | Count | Detail |
|---|---|---|
| ✅ Ready | 11 | Consent agenda |
| 🟡 At risk | 2 | Missing regression runs, which were fixed by T-1 |
| 🔴 Not ready | 1 | Gift-card split payment, deferred to v5.1 |

**Go/no-go (4 June):** **Go with conditions.** Phased rollout via flags; the payment-success alert must be live; rollback by flag rehearsed (measured at 4 minutes).

---

## 7. The incident (week 23)

**Framework used:** [Incident communication](../05-quality-and-reliability/incident-communication-playbook.md), [Post-incident review](../05-quality-and-reliability/post-incident-review-template.md)

At 25% rollout, on 11 June, **3.1% of card payments for one card network failed**.

| Time | Event |
|---|---|
| 12:41 | Lunchtime traffic peak |
| 12:44 | **New payment-success-rate alert fires** (the ORR action) |
| 12:47 | SEV-2 declared; I take the communications lead role; first update posted |
| 12:58 | Cause narrowed to the new service's vendor timeout (2 s), which was too low under peak |
| 13:13 | Rollout flag turned off; traffic back on the legacy path |
| 13:19 | Payment success back to baseline; incident resolved after **38 min** |

**Post-incident review actions**
- **Prevent:** timeout values validated in config review; load test includes vendor latency
- **Detect:** an automated canary-analysis step was added between rollout stages
- **Mitigate:** timeout raised to 5 s, with retry and backoff

Rollout resumed on 17 June and reached 100% on 22 June with no further incidents.

---

## 8. Outcomes (week 26)

| Measure | Baseline | Target | Result | |
|---|---|---|---|---|
| Checkout completion | 61% | ≥ 70% | **71%** | ✅ |
| p95 latency | 2.8 s | < 1.5 s | **1.2 s** | ✅ |
| Change failure rate | 24% | < 10% | **8%** | ✅ |
| Deployment frequency | Monthly | Weekly | **~2 per week** | ✅ |
| Defect SLO attainment | 78% | ≥ 90% | **93%** | ✅ |
| Open P1/P2 checkout defects | 18 | n/a | **4** | ✅ |
| Q1 commitments | 8 | n/a | **7 of 8** (88%) | 🟢 |
| Q2 commitments | 10 | n/a | **9 of 10** (90%); Pay Later deferred by decision | 🟢 |
| Weekly status-reporting effort | ~3 h | n/a | **~45 min** (automated drafts) | ✅ |

---

## 9. Lessons learned

| What worked | What I'd change |
|---|---|
| **Contract-first integration** recovered about 2 weeks after the vendor sandbox failed | Put **sandbox SLAs in vendor contracts** from the start, not at renewal |
| The **ORR** added the alert that detected the incident within 3 minutes | Make **2× peak load testing** a default criterion, not an ORR finding |
| **Phased rollout plus flag rollback** kept customer impact to 25% of traffic for 38 minutes | Add **automated canary analysis** from the first rollout stage |
| **Early escalation with options** got a decision within 48 hours | **Baseline success metrics earlier.** The latency baseline was a PRD gap |
| **Automated digests and hygiene checks** made governance cheaper | |

---

## Framework map

| Phase | Frameworks applied |
|---|---|
| Initiation | Charter · Stakeholder map & RACI · Communication plan |
| Planning | DoR & decomposition · Dependency board · RAID · Risk framework · Quarterly commitments · Vendor management |
| Execution | Sprint planning · Sprint reporting & forecasting · Stand-ups · Escalation · Decision log · Executive status |
| Quality | Defect SLOs · Triage · Scheduled alerting · Tracker hygiene · Dashboards · Metrics catalog |
| Release | ORR · Change gate & go/no-go · Readiness checklist · Rollback · Release notes |
| Incident | Incident communication · Post-incident review |
| Close-out | Retrospective · Quarterly close-out · Lessons learned |

🌐 **Interactive version:** [case-study.html](../docs/case-study.html)
