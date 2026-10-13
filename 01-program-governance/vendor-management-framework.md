# Vendor Management Framework

**Skill:** Vendor & third-party management · **Competency:** Selecting, contracting and governing external partners so they deliver predictably

## 1. Lifecycle

```
Need → Market scan → Evaluate → Contract → Onboard → Govern → Renew / Exit
```

## 2. Evaluation scorecard

Weight each criterion before you look at any vendor, to avoid anchoring on a favourite.

| Criterion | Weight | Vendor A | Vendor B | Vendor C |
|---|---|---|---|---|
| Functional fit to requirements | 25% | | | |
| Security & compliance posture | 20% | | | |
| Reliability (published SLA, track record) | 15% | | | |
| Integration effort (APIs, docs, sandbox) | 15% | | | |
| Total cost of ownership (3 yr) | 15% | | | |
| Support model & responsiveness | 5% | | | |
| Exit cost / lock-in risk | 5% | | | |
| **Weighted score** | 100% | | | |

Score each criterion from 1 to 5, and record the evidence behind each score.

## 3. Contract essentials (work with legal and procurement)

- [ ] Measurable SLAs, with service credits for breaches
- [ ] Defined support tiers and response times
- [ ] Sandbox / test environment availability commitments
- [ ] Change-notification period for API deprecations
- [ ] Data protection, audit rights and breach notification terms
- [ ] Exit plan: data export format, transition assistance

## 4. Onboarding checklist

- [ ] Named contacts on both sides (delivery, technical, escalation)
- [ ] Shared integration plan with milestones in the program plan
- [ ] Vendor dependencies added to the [RAID log](raid-log-template.md)
- [ ] Access provisioned under least privilege

## 5. Governance cadence

| Cadence | Forum | Content |
|---|---|---|
| Weekly (during integration) | Working sync | Blockers, defects, upcoming milestones |
| Monthly | Service review | SLA performance, incidents, open actions |
| Quarterly | Business review | Roadmap alignment, cost, satisfaction, renewal outlook |

## 6. Vendor health indicators

| Signal | Healthy | Warning |
|---|---|---|
| SLA attainment | Meets the contracted target | 2 or more breaches in a quarter |
| Ticket response | Within the support tier | Repeated escalations needed |
| Milestone dates | Met | 2 or more slips |
| Communication | Proactive change notices | Surprises in production |

## 7. Risk patterns and mitigations

| Risk | Mitigation |
|---|---|
| Unstable sandbox blocks testing | Contract stubs, plus a sandbox availability clause |
| Breaking API change | A deprecation-notice clause and a version-pinning strategy |
| Single-vendor dependency | An abstraction layer and a documented fallback |
| Key vendor contact leaves | Named backups in the contract |
