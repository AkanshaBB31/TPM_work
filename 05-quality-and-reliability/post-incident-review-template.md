# Post-Incident Review Template (Blameless)

**Skill:** Incident management · **Competency:** Building a learning culture and reducing operational risk

Hold the review within 3–5 business days of resolution. The aim is to improve **systems and conditions**, not to assign blame.

## Summary

| Field | Example (fictional) |
|---|---|
| Incident | EX-INC-014: checkout errors for some users |
| Severity | SEV-2 |
| Duration | 47 min (detected 14:03, resolved 14:50 UTC) |
| Customer impact | About 8% of checkout attempts failed |
| Detection | Error-rate alert |
| Review facilitator | <role> |

## Timeline

| Time (UTC) | Event |
|---|---|
| 13:58 | Config change deployed |
| 14:03 | Error-rate alert fired (**detection**) |
| 14:08 | Incident declared; incident commander assigned (**escalation**) |
| 14:20 | Cause identified |
| 14:41 | Config reverted (**mitigation**) |
| 14:50 | Error rate back to baseline (**resolved**) |

## Contributing factors

Use the *5 Whys* or a fishbone diagram. Ask **"What made this possible?"**, not "Who did this?"

## What went well / what was hard

-

## Actions

| Action | Type | Owner | Due | Tracked in |
|---|---|---|---|---|
| Add config validation to the pipeline | Prevent | | | |
| Alert on checkout success rate, not just errors | Detect | | | |
| Put risky configs behind feature flags | Mitigate | | | |

Track the actions in the backlog and review completion at the monthly operations review.

## Monthly executive incident summary

| Month | SEV-1 | SEV-2 | MTTD | MTTR | Repeat incidents | Overdue actions |
|---|---|---|---|---|---|---|
| | | | | | | |
