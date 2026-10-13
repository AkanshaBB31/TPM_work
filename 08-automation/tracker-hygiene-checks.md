# Issue Tracker Hygiene Checks

**Skill:** Data quality for delivery reporting · **Competency:** Keeping the data behind reports and automation trustworthy

Reports and automation are only as good as the data underneath them. Run these checks weekly, ideally automatically, and send the results to item owners.

| Check | Rule (example) | Why it matters |
|---|---|---|
| Missing owner | Active item with no assignee | Nobody is accountable |
| Missing priority | Defect without a priority | SLOs can't be calculated |
| Missing target date | Release-bound item with no planned date | Readiness gates can't evaluate it |
| Stale item | "In progress" with no update for 14+ days | A hidden blocker or abandoned work |
| Status mismatch | Marked done, but linked defects are still open | False reporting |
| Done without release | Marked done, but no release date or version | Inflated delivery numbers |
| Orphan | Story not linked to an epic or goal | Untraceable work |
| Missing component | No product/component field | Breaks per-area reporting |
| Date drift | Target date changed 3+ times | A signal about planning quality |

## Output format

Group findings **by owner**, so that each person gets one list of their own fixes:

```
@Owner: 3 items need attention
• 2 stale "In progress" items (no update in 14+ days)
• 1 defect missing a priority
```

## Tips

- Track a hygiene score (% of items passing every check) over time, and celebrate improvement.
- Fix the process upstream with required fields and workflow validators, rather than chasing the same gaps every week.
- Show hygiene exceptions on dashboards instead of quietly excluding them (see the [dashboard guide](../07-reporting-and-metrics/dashboard-design-guide.md)).
