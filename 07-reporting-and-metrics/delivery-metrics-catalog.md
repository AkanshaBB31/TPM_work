# Delivery Metrics Catalog

**Skill:** Metrics design · **Standards:** DORA, Kanban flow metrics, Scrum
**Competency:** Defining measurable, unambiguous KPIs that are hard to game

## 1. Principles

1. **Measure outcomes and flow, not busyness.**
2. **Pair every metric with a counter-metric,** so one can't be gamed at another's expense.
3. **Trends beat snapshots:** show at least six periods.
4. **Track no more than 6–8 headline metrics.** Tracking everything means acting on nothing.
5. **Every metric has an owner and a "so what":** if it moves, who acts, and how?
6. **Never use team metrics to rank individuals.**

## 2. Catalog

### Flow & predictability: *are we delivering, and can people plan around us?*

| Metric | Formula | Watch for | Can be gamed by | Counter-metric |
|---|---|---|---|---|
| Throughput | Items completed per period | Sustained drops | Splitting work artificially | Cycle time |
| Cycle time (p50 / p85) | Done − started | A growing tail | Starting work late | Throughput |
| Work-item age | Now − started (in-progress items) | Stuck items | — | WIP |
| WIP | Items in progress | Above team capacity | — | Throughput |
| Say/Do ratio | Completed committed ÷ committed | Consistently < 80% | Under-committing | Velocity trend |
| Commitment delivery % | Delivered ÷ quarterly baseline | Misses | Committing to less | Scope delivered vs. roadmap |
| Release date variance | Actual − planned release date | Growing variance | Padding plans | Lead time |
| Readiness at T-N | % of release items passing the gate N days out | Late readiness | — | Change failure rate |
| Unplanned work ratio | Ad hoc items ÷ total | > ~20% | Mis-labelling | Ticket inflow |

### Software delivery performance (DORA)

| Metric | Definition |
|---|---|
| Deployment frequency | How often you deploy to production |
| Lead time for changes | Commit → running in production |
| Change failure rate | Deployments causing a failure, hotfix or rollback ÷ total |
| Time to restore (MTTR) | Failure → recovery |

### Quality: *are we delivering well?*

| Metric | Formula | Watch for | Can be gamed by | Counter-metric |
|---|---|---|---|---|
| Escaped defects | Production defects per release | Upward trend | Not logging defects | Support ticket volume |
| Defect inflow vs. outflow | Created vs. resolved per week | Inflow > outflow for 3+ weeks | Reclassifying tickets | Category mix |
| Defect SLO attainment | Met ÷ (Met + Breached) | Below target | Downgrading priority | Priority-change audit |
| Reopen rate | Reopened ÷ resolved | Rising | Not reopening | Escaped defects |
| MTTR (incidents) | Σ duration ÷ incidents | Rising | Closing incidents early | Repeat incidents |

### Stakeholder value

| Metric | Definition |
|---|---|
| Demo acceptance rate | Items accepted at the first demo |
| Customer-reported issues | Volume and severity by segment |

## 3. Metric definition card (fill one in per metric)

```
Name:
Question it answers:
Formula:
Data source:
Refresh cadence:
Owner:
Target / threshold (illustrative until calibrated):
Paired counter-metric:
Known caveats:
```

## 4. Anti-patterns

- Comparing velocity across teams
- Setting targets on metrics the team directly controls (Goodhart's law)
- Dashboards with no decision attached

## References

- Forsgren, Humble & Kim, *Accelerate* (DORA)
- Vacanti, *Actionable Agile Metrics for Predictability*
