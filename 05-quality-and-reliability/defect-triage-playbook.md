# Defect Triage Playbook

**Skill:** Quality management · **Competency:** Prioritisation and cross-functional facilitation

## Roles

| Role | Responsibility |
|---|---|
| Triage lead (rotating) | Runs the session, keeps the timeboxes, makes the final priority call |
| Product | Confirms business impact |
| Engineering | Assesses severity and effort; assigns an owner |
| QA | Confirms reproducibility; identifies test gaps |
| Support | Brings customer impact and frequency |

## Cadence

| Session | Length | Scope |
|---|---|---|
| Daily | 15 min | New defects since the last triage (P1s are triaged immediately, outside the cadence) |
| Twice weekly | 30 min | P3/P4 backlog |
| Weekly ageing review | 30 min | WARNING items and anything that hasn't moved in 7 days: still valid? Still the right priority? |

## Flow

```
New defect
  ├─ Duplicate? ───────────────► Link & close
  ├─ Can't reproduce / missing info? ─► Request info (SLO clock paused)
  ├─ Working as designed? ─────► Convert to an enhancement, or close with an explanation
  ▼
Impact × urgency → Priority → Owner → Target date from the SLO → Tell the reporter
```

## Impact × urgency matrix

| | Urgency high | Urgency medium | Urgency low |
|---|---|---|---|
| **Impact: widespread** | P1 | P2 | P3 |
| **Impact: many users** | P2 | P2 | P3 |
| **Impact: few users** | P3 | P3 | P4 |

Targets come from the [defect SLO framework](defect-slo-framework.md).

## Minimum good bug report

- [ ] Steps to reproduce; expected vs. actual result
- [ ] Environment and version
- [ ] Scope of impact (how many users or accounts, and which segment)
- [ ] Evidence: logs, recordings, with **sensitive data removed**

## Required fields before leaving triage

- [ ] Priority · [ ] Component · [ ] Environment · [ ] Owner · [ ] Target date

## Quality checks for the triage itself

- Is priority based on customer or business impact, not on who raised it?
- Does every triaged item have an owner and a date?
- Are there **clusters** (same component, same release) that call for a root-cause review?

## Outputs

- An updated tracker, which is the single source of truth
- Escalations for any new P1 (see the [escalation playbook](../09-leadership/escalation-playbook.md))
- Clusters flagged for problem management
