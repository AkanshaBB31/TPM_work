# 11 · Case Study

A **fictional, end-to-end program** that applies the frameworks in this repository to one 26-week delivery, from charter to close-out. Templates show *what* I use; this case study shows *how they work together* when a real program hits real problems: a failing vendor, a slipping dependency, a production incident.

| File | Use it to… |
|---|---|
| [checkout-modernization-case-study.md](checkout-modernization-case-study.md) | Read the full narrative with every table, decision and outcome |
| [Interactive web version](../docs/case-study.html) | See the same story with KPI tiles, interactive charts, a phase timeline and an incident timeline |

> **Everything here is invented.** Example Co., Kestrel Pay, the teams, the people and all the numbers are fictional. They're there to show method and judgment, not to describe any real organisation.

---

## Program at a glance

| | |
|---|---|
| **Organisation** | Example Co.: a mid-size online retailer |
| **Program** | Checkout Modernization: replace a legacy checkout module with a new service, a redesigned UI, a new payment provider and saved carts |
| **Duration** | 26 weeks (Q1–Q2 2026) |
| **Scale** | 5 teams, 21 people, 1 external vendor, 3 cross-team dependencies, 41 stories |
| **Role shown** | Technical Program Manager: accountable for delivery, governance, release and stakeholder communication |

## The story in 60 seconds

1. **Initiation:** a charter set five measurable targets. A concerned Support leader was brought in early and became an ally.
2. **Planning:** a readiness review found 7 gaps in the requirements before any code was written. A dependency board exposed a vendor with no committed date, which became the top risk.
3. **Execution:** that risk materialised in sprint 4 (68% say/do). An SBAR escalation got a decision within 48 hours: build a contract stub, and add a vendor SLA. A low-demand feature was deferred to protect the launch date.
4. **Quality:** defect SLOs, daily triage and an automated digest raised SLO attainment from 78% to 93%.
5. **Release:** an operational readiness review added a payment-success alert. A criteria-based gate approved 11 of 14 items, and the go/no-go chose a phased rollout behind feature flags.
6. **Incident:** at 25% rollout, that new alert caught a payment-timeout fault in 3 minutes. Flag rollback resolved it in 38 minutes, and the rollout finished 11 days later.
7. **Outcome:** every charter target was met, and the lessons were turned into new default criteria.

## Results

| Measure | Baseline | Target | Result |
|---|---|---|---|
| Checkout completion | 61% | ≥ 70% | **71%** ✅ |
| p95 checkout latency | 2.8 s | < 1.5 s | **1.2 s** ✅ |
| Change failure rate | 24% | < 10% | **8%** ✅ |
| Deployment frequency | Monthly | Weekly | **~2 per week** ✅ |
| Defect SLO attainment | 78% | ≥ 90% | **93%** ✅ |
| Open P1/P2 defects | 18 | n/a | **4** |
| Quarterly commitments | 18 | n/a | **16 delivered**, 1 deferred by decision, 1 slipped |
| Weekly reporting effort | ~3 h | n/a | **~45 min** |

## Phase-by-phase framework map

Each phase links to the reusable framework it applies.

| Phase (weeks) | What happened | Frameworks applied |
|---|---|---|
| Initiation (1–2) | Charter, outcomes, stakeholder analysis | [Program charter](../02-technical-program-management/program-charter-template.md) · [Stakeholder map & RACI](../06-stakeholder-management/stakeholder-map-and-raci.md) · [Communication plan](../06-stakeholder-management/communication-plan-template.md) |
| Planning (3–4) | Requirements review, backlog, dependencies, risks, commitments | [Definition of Ready](../03-agile-delivery/definition-of-ready-and-backlog-decomposition.md) · [Dependency management](../02-technical-program-management/cross-team-dependency-management.md) · [RAID log](../01-program-governance/raid-log-template.md) · [Risk framework](../01-program-governance/risk-management-framework.md) · [Quarterly commitments](../01-program-governance/quarterly-commitment-tracking.md) · [Vendor management](../01-program-governance/vendor-management-framework.md) |
| Execution (5–22) | Sprints, vendor escalation, decisions, executive reporting | [Sprint planning](../03-agile-delivery/sprint-planning-playbook.md) · [Sprint reporting](../03-agile-delivery/sprint-reporting-and-forecasting.md) · [Escalation](../09-leadership/escalation-playbook.md) · [Decision log](../01-program-governance/decision-log-template.md) · [Executive status](../07-reporting-and-metrics/executive-status-report-template.md) |
| Quality (1–26) | SLOs, triage, automated digests, data hygiene | [Defect SLOs](../05-quality-and-reliability/defect-slo-framework.md) · [Triage](../05-quality-and-reliability/defect-triage-playbook.md) · [Scheduled alerting](../08-automation/scheduled-alerting-pattern.md) · [Tracker hygiene](../08-automation/tracker-hygiene-checks.md) · [Dashboards](../07-reporting-and-metrics/dashboard-design-guide.md) |
| Release (21–24) | Operational readiness, gate, go/no-go, rollback | [ORR](../02-technical-program-management/operational-readiness-review.md) · [Change gate & go/no-go](../04-release-management/change-readiness-gate-and-go-no-go.md) · [Readiness checklist](../04-release-management/release-readiness-checklist.md) · [Rollback plan](../04-release-management/rollback-planning-template.md) · [Release notes](../04-release-management/release-notes-framework.md) |
| Incident (23) | SEV-2 detection, communication, rollback, review | [Incident communication](../05-quality-and-reliability/incident-communication-playbook.md) · [Post-incident review](../05-quality-and-reliability/post-incident-review-template.md) |
| Close-out (26) | Outcomes vs. charter, lessons learned | [Retrospective](../03-agile-delivery/retrospective-playbook.md) · [Metrics catalog](../07-reporting-and-metrics/delivery-metrics-catalog.md) |

## Skills demonstrated

| Competency | Where it shows up |
|---|---|
| Program initiation & outcome definition | A charter with measurable baselines and targets |
| Requirements & backlog management | 7 PRD gaps closed before build; risk-first sequencing |
| Dependency & vendor management | Dependency board, contract-first stub, vendor SLA clause |
| Risk management & escalation | RAID scoring; SBAR escalation that got a decision in 48 hours |
| Decision governance | Three logged decisions, including a scope trade-off to protect the date |
| Agile delivery & forecasting | Sprint predictability tracking, dip analysis, recovery |
| Quality & service-level management | SLO attainment from 78% to 93%; P1/P2 defects from 18 to 4 |
| Release management | ORR, criteria-based gate, go-with-conditions, phased rollout |
| Incident management & communication | 3-minute detection, 38-minute resolution, blameless review |
| Executive communication | A week-12 Amber status with a clear decision ask |
| Automation | Automated SLO digests and hygiene checks; reporting time down 75% |

## How to view the interactive version

- **On the web:** once GitHub Pages is enabled (Settings → Pages → *Deploy from a branch* → `main` / `/docs`), it's served at **https://akanshabb31.github.io/TPM_work/case-study.html**, alongside an HTML version of every framework in this repo.
- **Locally:** open `docs/case-study.html` in any browser. It's a single self-contained file with no dependencies.

The interactive page includes outcome KPI tiles, a clickable phase timeline, a sprint-predictability chart, an SLO-attainment trend with hover tooltips (each chart has a data-table view), the dependency board, the release gate results and the incident timeline. It supports light and dark themes and works at phone width.

## How to use this as a reader

- **Hiring managers:** read *The story in 60 seconds*, then the incident and lessons sections. They show judgment under pressure.
- **Practitioners:** follow the framework links from each phase to reuse the templates.
- **Interview prep:** this is the model for the stories in the [STAR story bank](../10-interview-prep/star-story-bank-template.md).
