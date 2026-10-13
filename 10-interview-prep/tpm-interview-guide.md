# TPM / Program Manager Interview Guide

## 1. What interviewers evaluate

| Dimension | What "strong" looks like |
|---|---|
| **Program execution** | Breaks ambiguity into a plan; manages dependencies and risk; delivers |
| **Technical depth** | Explains system design trade-offs; credible with engineers; asks the right questions |
| **Stakeholder management** | Aligns competing priorities; communicates up, down and across |
| **Leadership & influence** | Drives outcomes without authority; handles conflict |
| **Data & judgment** | Uses metrics to decide; knows which ones can be gamed |
| **Communication** | Structured, concise, conclusion first |

## 2. Common question types and answer frameworks

### a) "Tell me about a program you led end to end."
Use **STAR+**: Situation → Task → Actions (*your* actions, as "I", not "we") → Result (quantified) → **Learning**.
Relevant artifacts: [Program charter](../02-technical-program-management/program-charter-template.md), [Quarterly commitment tracking](../01-program-governance/quarterly-commitment-tracking.md).

### b) "A critical dependency is going to slip. What do you do?"
1. Quantify the impact on the critical path.
2. Explore options: re-sequence, stub or mock, descope, add resources, accept the slip.
3. Agree a recovery plan with the provider.
4. Escalate early, with options and a recommendation.
5. Communicate the change and update the plan and RAID log.
Relevant artifacts: [Dependency management](../02-technical-program-management/cross-team-dependency-management.md), [Escalation playbook](../09-leadership/escalation-playbook.md).

### c) "How do you decide whether a release is ready?"
Criteria over opinion: a gate with mandatory criteria and evidence, operational readiness, a tested rollback plan, and a go/no-go with written decisions.
Relevant artifacts: [Change gate & go/no-go](../04-release-management/change-readiness-gate-and-go-no-go.md), [Rollback plan](../04-release-management/rollback-planning-template.md).

### d) "Production is down. Walk me through your role."
Assign the roles (IC, tech lead, comms lead) → communicate on a fixed cadence → mitigate before root-causing → blameless review → track actions to closure.
Relevant artifacts: [Incident communication](../05-quality-and-reliability/incident-communication-playbook.md), [Post-incident review](../05-quality-and-reliability/post-incident-review-template.md).

### e) "Which metrics would you use to measure program health?"
Use balanced pairs: flow (cycle time, throughput), quality (escaped defects, change failure rate), predictability (say/do, commitment delivery %), plus counter-metrics. Never rank individuals.
Relevant artifact: [Metrics catalog](../07-reporting-and-metrics/delivery-metrics-catalog.md).

### f) "Two senior stakeholders want conflicting things."
Clarify each one's underlying goal → find shared outcomes → make the trade-off explicit with data → agree who has the decision right → record the decision → communicate it.
Relevant artifacts: [Stakeholder map & RACI](../06-stakeholder-management/stakeholder-map-and-raci.md), [Decision log](../01-program-governance/decision-log-template.md).

### g) "How have you used automation or AI to scale yourself?"
Describe the problem, the pattern (scheduled job or agent workflow), the guardrails (read-only access, human in the loop) and the measured result.
Relevant artifacts: [Scheduled alerting](../08-automation/scheduled-alerting-pattern.md), [AI-assisted PM workflows](../08-automation/ai-assisted-pm-workflows.md).

### h) System design for TPMs
You aren't expected to design like a staff engineer. You *are* expected to:
- clarify requirements and non-functional needs (scale, latency, availability)
- sketch the main components and data flow
- identify risks: single points of failure, data consistency, migration, rollout
- propose a phased delivery plan with milestones and rollback

## 3. Questions to ask the interviewer

- How are program priorities set, and who holds the decision rights?
- What does a TPM own here that engineering managers don't?
- How is TPM success measured in the first 6 months?
- What's the hardest cross-team dependency right now?

## 4. Preparation checklist

- [ ] 8–10 anonymised stories in the [STAR story bank](star-story-bank-template.md), covering every competency
- [ ] Each story has a quantified result. Use ranges or percentages if exact figures are confidential.
- [ ] A 2-minute "walk me through your background" pitch
- [ ] One system you can explain in depth: architecture, trade-offs, failure modes
- [ ] **Confidentiality check:** no employer-confidential names, numbers or details in any story
