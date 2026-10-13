# Rollback Planning Template

**Skill:** Release risk management · **Standards:** ITIL change enablement, SRE practices

A rollback plan answers one question: **if this release goes wrong, how do we get back to a known-good state, and how quickly?** Agree it *before* release day.

## 1. Summary

| Field | Value |
|---|---|
| Release | `<version>` |
| Previous known-good version | |
| Rollback decision authority | e.g. on-call engineering lead |
| Max time to decide | e.g. 30 min after the first trigger |
| Target time to complete rollback | e.g. ≤ 20–30 min |
| Point of no return | The step after which only a roll-forward is possible |

## 2. Triggers (any one; values illustrative)

| Signal | Threshold |
|---|---|
| Error rate | > 2× the pre-release baseline for 10 min |
| Latency (p95) | > 1.5× baseline for 10 min |
| Critical user journey | Synthetic check fails twice in a row |
| Data integrity | Any confirmed corruption |
| Severity-1 incident | Declared and attributed to the release |

## 3. Strategy by change type

| Change type | Preferred rollback | Notes |
|---|---|---|
| Feature behind a flag | **Turn the flag off** | Instant; no deploy (preferred) |
| Stateless service | Redeploy the previous artifact / blue-green switch | Keep the previous version warm |
| Config change | Revert the config | Version-controlled config only |
| Schema migration | Expand/contract (backward compatible) | Avoid destructive migrations in the same release |
| Data backfill | Restore a snapshot / run a compensating job | Take the snapshot before running |
| Last resort | Forward fix | Only if the above aren't possible and the fix takes < 1 hour |

## 4. Runbook

| # | Step | Owner | Est. | Verification |
|---|---|---|---|---|
| 1 | Announce the rollback in the incident channel | Release owner | 1 min | Acknowledged by on-call |
| 2 | Turn off flags / switch traffic / redeploy | On-call engineer | 5–10 min | The version endpoint shows the previous version |
| 3 | Run smoke tests on critical journeys | QA | 10 min | All pass |
| 4 | Confirm metrics are stable | On-call engineer | 10 min | Errors back to baseline |
| 5 | Notify stakeholders | Release owner | 5 min | Update sent (see [incident communication](../05-quality-and-reliability/incident-communication-playbook.md)) |

## 5. Data considerations

- Can the old version read data written by the new one?
- What happens to records created during the release window?
- Are any migrations irreversible? If so, where's the backup?

## 6. Rehearsal

- [ ] Rollback rehearsed in pre-production within the last 30 days
- [ ] Measured rollback time: ____ min

## 7. After a rollback

- Blameless [post-incident review](../05-quality-and-reliability/post-incident-review-template.md) within 3–5 business days
- Agree the criteria for re-release; run a fresh go/no-go
