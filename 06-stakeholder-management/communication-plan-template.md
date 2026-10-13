# Communication Plan Template

**Skill:** Stakeholder communication · **Competency:** Designing a reliable information cadence

| Communication | Audience | Purpose | Format / channel | Cadence | Owner | Automated? |
|---|---|---|---|---|---|---|
| Stand-up / async update | Delivery team | Coordination, blockers | 15-min sync or chat post | Daily | Scrum master / each dev | Partly: drafted from tracker & code activity |
| New critical defect alert | On-call, leads | Fast response | Chat channel | Near real time | Delivery lead | ✅ |
| Defect SLO digest | Owning teams, support lead | Prevent & escalate breaches | Chat channel digest | Daily, start of day | Delivery lead | ✅ |
| Sprint report | Team + stakeholders | Transparency | One page / dashboard | Per sprint | Scrum master | Partly |
| Release readiness report | Go/no-go attendees | Decision input | Published dashboard | T-N and T-1 days | Release manager | ✅ |
| Release notes | Customers, support | Awareness of changes | Docs site / email | Per release | Product owner | Drafted from the tracker |
| Executive status | Sponsors, leadership | Decisions, risk visibility | One-page report | Weekly | TPM | Drafted, then edited by a person |
| Steering review | Sponsors | Governance, escalations | Meeting + short deck | Monthly / bi-weekly | TPM | No |
| Quarter close-out | All stakeholders | Outcomes vs. goals, lessons | Document + meeting | Quarterly | TPM | No |
| Incident updates | Varies by severity | Trust during incidents | See the [incident playbook](../05-quality-and-reliability/incident-communication-playbook.md) | Per incident | Comms lead | Templates |

## Principles

- **Push the exceptions, pull the detail.** Alerts carry only what needs action. Dashboards hold everything else.
- **One channel per purpose.** Don't mix alerts with discussion.
- **Automate the routine** and spend the time saved on messages that need judgment.
- **Meetings are for decisions,** not for reading out status that's already written down.
- **A single source of truth.** Every message links to the same dashboard.
