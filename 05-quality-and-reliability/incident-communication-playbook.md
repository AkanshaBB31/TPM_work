# Incident Communication Playbook

**Skill:** Crisis & incident communication · **Competency:** Keeping stakeholders informed during incidents, so that engineers can focus on fixing them

Poor communication turns a technical incident into a trust incident. This playbook separates **fixing** from **informing**.

## 1. Roles

| Role | Responsibility |
|---|---|
| Incident commander (IC) | Owns the response; makes the decisions; doesn't debug |
| Technical lead | Leads diagnosis and the fix |
| **Communications lead** (often the TPM) | Owns every update to stakeholders and customers |
| Scribe | Keeps the timeline for the [post-incident review](post-incident-review-template.md) |

## 2. Update cadence by severity (illustrative)

| Severity | Internal update | Customer/status page | Executive notification |
|---|---|---|---|
| SEV-1 (major outage) | Every 30 min | Within 15 min of declaration, then every 30–60 min | Immediately |
| SEV-2 (partial degradation) | Every 60 min | If customer-visible | Within 1 hour |
| SEV-3 (minor) | At start and end | Usually not | Daily summary |

**Always say when the next update will come, and keep to it,** even if there's no news.

## 3. Templates

### Initial notice
```
[SEV-<n>] <Service/feature> degraded. Investigating.
Impact:  <who is affected and how; what still works>
Started: <time, tz>
Status:  Investigating
Next update: <time, tz>
IC: <role>   Channel: <incident channel>
```

### Progress update
```
[SEV-<n>] Update <#>: <one-line status>
What we know: <cause if known, or "still investigating">
What we're doing: <current mitigation>
Customer impact now: <better / same / worse>
Next update: <time, tz>
```

### Resolution
```
[SEV-<n>] Resolved: <service> back to normal as of <time, tz>.
Duration: <x min>. Impact: <summary>.
Cause (preliminary): <one line>.
Post-incident review scheduled for <date>.
```

## 4. Writing rules

- **Impact first,** in plain language. No internal jargon in customer messages.
- **Don't speculate** about the cause in external messages.
- **No blame,** and no names, in any update.
- **One channel per audience:** an incident channel for responders, a status page for customers, a summary email for executives.
- Time zones are always explicit.

## 5. Audience matrix

| Audience | Needs to know | Channel |
|---|---|---|
| Responders | Everything technical | Incident chat channel |
| Support | Impact, workaround, customer wording | Support channel + macro |
| Executives | Impact, ETA, business risk, asks | Short email / chat DM |
| Customers | Impact, what to do, when it'll be fixed | Status page |

## 6. After the incident

- Send the resolution summary within 24 hours
- Share the post-incident review outcomes with the affected stakeholders
- Track customer-facing follow-ups (credits, apologies) to closure
