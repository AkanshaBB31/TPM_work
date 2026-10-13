# Scheduled Alerting & Reporting Pattern

**Skill:** Workflow automation · **Competency:** Replacing manual status checks with reliable, low-noise automated signals

A tool-agnostic design for unattended jobs that read an issue tracker, apply rules, and post results to a chat channel or a published page. Use it for SLO alerts, readiness reports, daily digests and new-item alerts.

## 1. Architecture

```
┌───────────┐   ┌──────────┐   ┌──────────┐   ┌───────────┐   ┌──────────────┐
│ Scheduler │──▶│  Fetch   │──▶│ Evaluate │──▶│  Render   │──▶│   Deliver    │
│ (cron)    │   │ (API +   │   │ (rules + │   │ (markdown │   │ (webhook /   │
│           │   │  query)  │   │  config) │   │  / HTML)  │   │  page)       │
└───────────┘   └──────────┘   └──────────┘   └───────────┘   └──────────────┘
                     ▲              ▲                               │
                     └──── config.yaml (queries, thresholds) ───────┤
                                                                    ▼
                                                     state store (watermark / sent IDs)
```

## 2. Alert archetypes

| Archetype | Cadence | Content | Noise control |
|---|---|---|---|
| **New-item alert** | Frequent (e.g. every 15 min) | Items created since the last run | Watermark; post nothing if empty |
| **Daily digest** | Once a day | Counts by priority × area | Always posts, so silence is never mistaken for "all clear" |
| **Approaching breach** | Once a day | Items in the warning window | Grouped by owner; once per item per day |
| **Breached** | Once a day | Items past target | Repeats daily until resolved |
| **Readiness report** | T-N / T-1 before a review | Gate results per item | Published page plus a summary post |

## 3. Design rules

1. **Config-driven.** Queries, thresholds, schedules and destinations live in config, never in code.
2. **Idempotent.** A re-run must never double-post. Persist a watermark or the IDs already sent.
3. **Defined empty-state behaviour.** Event alerts stay silent; digests say "0 open".
4. **Actionable payload.** Item link, owner, priority, time left and a link to the filtered list. Nothing else.
5. **Grouped.** One message per owner or area, not one per item.
6. **Non-interactive.** A scheduled job can't ask questions. It fails loudly rather than guessing.
7. **Fail visibly.** If the query fails, post a *health* alert to the job owner. Never stay silent.
8. **Least privilege.** Read-only tracker token; webhook scoped to one channel.
9. **Secrets outside the code,** in a secret store or environment variables.
10. **Explicit time zones** in schedules and message timestamps.
11. **Documented owner** for the automation itself.

## 4. Example config (fictional)

```yaml
jobs:
  - name: slo-warning-digest
    schedule: "0 8 * * 1-5"          # weekday mornings, team time zone
    query: "type = Defect AND status in (Open, 'In Progress')"
    evaluator: slo_warning           # see 05-quality-and-reliability/defect-slo-framework.md
    group_by: [component, priority]
    deliver: { kind: chat_webhook, secret_ref: SLO_ALERT_WEBHOOK }

  - name: new-critical-alert
    schedule: "*/15 * * * *"
    query: "type = Defect AND priority = P1"
    evaluator: new_since_watermark
    deliver: { kind: chat_webhook, secret_ref: ONCALL_WEBHOOK }
```

## 5. Pseudocode

```python
def run(now):
    last_run = state.get("last_run", default=now - interval)
    items = tracker.search(QUERY, updated_after=last_run)   # read-only
    groups = classify(items)                 # priority, area, SLO bucket
    if job.is_event_alert and not groups:
        state.set("last_run", now)
        return
    chat.post(render(groups, now))
    state.set("last_run", now)               # only after a successful post
```

The classification logic should be a plain, unit-testable function, separate from the scheduler. See [`examples/slo_calculator.py`](examples/slo_calculator.py).

## 6. Message format

```
⚠️ 3 defects approaching SLO breach: Payments area
• EX-2210  P2  Refund status not updating    1d 4h left  @owner
• EX-2231  P3  CSV export timezone off       2d left     @owner
• EX-2240  P3  Receipt email logo missing    5d left     @owner
View all → <dashboard link>
```

Lead with the count and the action, group by owner, and link to the detail. *(Fictional data.)*

## 7. Failure handling

| Failure | Behaviour |
|---|---|
| Tracker API unavailable | Retry with backoff, then alert the job owner. Never post partial data. |
| Query unexpectedly returns zero rows | Flag it as suspicious: the query may be broken |
| Webhook rejected | Log it and alert through a secondary channel |

## 8. Maturity path

1. Manual weekly report
2. Scheduled summary
3. Threshold alerts with owners tagged
4. Trend detection ("this area's inflow doubled week on week")
5. AI-drafted narrative with linked evidence, reviewed by a person (see [AI workflows](ai-assisted-pm-workflows.md))
