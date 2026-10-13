# TPM Work: Program & Delivery Management Portfolio

**Technical Program Management · Program Management · Release Management · Agile Delivery**

This is an open knowledge repository of frameworks, templates, playbooks and small automation examples that I use to run software delivery programs. I wrote it to show how I work: how I govern programs, ship releases safely, keep stakeholders aligned, turn tracker data into decisions, and automate the routine parts of program management.

Everything is written from scratch using public industry standards (PMBOK, Scrum Guide, ITIL 4, Google SRE, DORA). All examples use a fictional company, **Example Co.**, and invented data.

---

## Roles this portfolio supports

| Role | Where to look first |
|---|---|
| **Technical Program Manager** | [Technical Program Management](02-technical-program-management/), [Automation](08-automation/), [Release Management](04-release-management/) |
| **Program Manager** | [Program Governance](01-program-governance/), [Stakeholder Management](06-stakeholder-management/), [Reporting](07-reporting-and-metrics/) |
| **Release Manager** | [Release Management](04-release-management/), [Quality & Reliability](05-quality-and-reliability/) |
| **Project / Senior Project Manager** | [Program Governance](01-program-governance/), [Agile Delivery](03-agile-delivery/), [Leadership](09-leadership/) |

## Repository map

| # | Area | Highlights |
|---|---|---|
| 01 | [Program Governance](01-program-governance/) | RAID log, risk framework, decision log, quarterly commitment tracking, vendor management |
| 02 | [Technical Program Management](02-technical-program-management/) | Program charter, cross-team dependency management, operational readiness review |
| 03 | [Agile Delivery](03-agile-delivery/) | Sprint planning, sprint reporting & forecasting, stand-ups, retrospectives, Definition of Ready & backlog decomposition |
| 04 | [Release Management](04-release-management/) | Readiness checklist, change gate & go/no-go, rollback planning, release notes |
| 05 | [Quality & Reliability](05-quality-and-reliability/) | Defect SLO framework, triage, post-incident review, incident communication |
| 06 | [Stakeholder Management](06-stakeholder-management/) | Stakeholder map & RACI, communication plan |
| 07 | [Reporting & Metrics](07-reporting-and-metrics/) | Executive status report, metrics catalog, dashboard design, progress reporting |
| 08 | [Automation](08-automation/) | Scheduled alerting pattern, AI-assisted PM workflows, tracker hygiene, **runnable SLO calculator** |
| 09 | [Leadership](09-leadership/) | Escalation playbook, cross-functional collaboration |
| 10 | [Interview Prep](10-interview-prep/) | TPM interview guide, STAR story bank |

## Skills matrix

| Skill area | Evidence in this repo | Depth |
|---|---|---|
| Program governance | RAID, risk scoring, decision records, quarterly commitment baselines | ●●●●● |
| Release management | Readiness gates, go/no-go, rollback, release notes | ●●●●● |
| Quality & service levels | Defect SLO design, triage, warning/breach alerting | ●●●●● |
| Executive communication | One-screen status reports, RAG definitions, escalation framing | ●●●●○ |
| Metrics & reporting | Metric catalog with counter-metrics, dashboard design | ●●●●● |
| Workflow automation | Idempotent scheduled alerts, config-driven jobs, Python example | ●●●●○ |
| AI-assisted program management | Packaged agent workflows with human-in-the-loop guardrails | ●●●●○ |
| Agile delivery | Planning, capacity, forecasting, facilitation, retros | ●●●●○ |
| Stakeholder management | Power/interest mapping, RACI, communication cadence | ●●●●○ |
| Dependency & cross-team delivery | Dependency board, critical path, contract-first integration | ●●●●○ |
| Technical program management | Charter, operational readiness (observability, capacity, security) | ●●●○○ |
| Incident management | Blameless reviews, incident communication cadence | ●●●○○ |
| Vendor management | Vendor selection, SLAs, governance cadence | ●●●○○ |

## Operating principles

1. **Criteria over opinion.** "Ready" means the stated criteria are met, not that someone feels confident.
2. **Surface risk early.** Warn before breaches, and escalate before there are surprises.
3. **Automate the gathering, not the judgment.** Scripts and agents collect and summarise. People decide.
4. **One source of truth.** Reports are generated from the tracker, never copied by hand.
5. **Trends over snapshots.** Direction tells you more than a single value.

## Try the example

```bash
python 08-automation/examples/slo_calculator.py 08-automation/examples/sample-defects.csv --as-of 2026-03-31
```

It needs Python 3.8+ and only the standard library.

## How to use these templates

Each file stands alone. Copy it, replace the `<placeholders>`, and tune the thresholds. **Every number in this repo is illustrative**, not a benchmark.

## License & compliance

- Documentation: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · Code: [MIT](LICENSE)
- See [COMPLIANCE.md](COMPLIANCE.md). This repository contains no employer or client information, code, data or proprietary methods.
