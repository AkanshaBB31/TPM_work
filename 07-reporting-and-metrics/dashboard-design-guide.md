# Delivery Dashboard Design Guide

**Skill:** Data visualisation & operational reporting · **Competency:** Building self-serve, decision-oriented program-health and defect-trend dashboards

## 1. Start from the decision, not the data

For each panel, write down *who* looks at it, *how often* and *which decision* it informs. **If no decision depends on a panel, remove it.**

| Audience | Question | Panel |
|---|---|---|
| Executive | Will we deliver what we promised this quarter? | Commitment scorecard |
| Executive | Is quality getting better or worse? | Defect inflow vs. outflow trend; KPI tiles |
| Release manager | Is this release ready? Did the last one introduce risk? | Readiness summary; defects by found-in version |
| Delivery lead | What needs my attention today? | Exceptions: blocked, at risk, SLO warnings |
| Engineering manager | Where is work or pain concentrated? | Breakdown by component × priority; workload by owner |
| Support lead | Are customer commitments being met? | SLO attainment by customer segment |

## 2. Layout hierarchy

```
┌──────────────────────────────────────────────────────────────┐
│ Title · scope selector · "data as of" timestamp                │
├──────────────────────────────────────────────────────────────┤
│ KPI tiles (4–6 max): Open P1/P2 │ SLO attainment │ Ready % │ ↑↓ │
├───────────────────────────────┬──────────────────────────────┤
│ Breakdown: priority × area     │ Exceptions list (actionable) │
├───────────────────────────────┴──────────────────────────────┤
│ Trends: inflow vs. outflow (12 weeks) · age heatmap            │
├──────────────────────────────────────────────────────────────┤
│ Detail table: filter, sort, search, export; rows link to source│
└──────────────────────────────────────────────────────────────┘
```

**Top:** what someone reads in 10 seconds. **Middle:** what needs action. **Bottom:** detail for anyone who wants to dig in. For larger programs, use a **home page plus detail pages** (one per release or team).

## 3. Every number is a doorway

- Clicking any KPI tile or chart segment opens **the items behind it**, in a filtered table or a side panel.
- Make clickability visible *before* the click: a hover state, a pointer cursor, a "→" hint.
- Show active filters in a filter bar with a one-click "clear".
- Never make a static number look clickable, or a clickable one look static.

## 4. Trust signals

- One **"data as of"** timestamp in a fixed place.
- Metric definitions next to the metric, behind an ⓘ tooltip.
- **Explain every flag:** each red cell shows *why* it's red.
- Show data-hygiene exceptions (e.g. *done without a release date*) instead of quietly dropping them.
- Every row links back to the source tracker item.

## 5. Generic data model

| Field | Purpose |
|---|---|
| id, title | Identification (internal editions only) |
| type | Incident / defect / request / story |
| priority, severity | Segmentation |
| component / product area | Concentration analysis |
| status, status category | Open vs. closed |
| created, resolved | Ageing, inflow/outflow, SLO |
| found-in version, environment | Release quality, escape rate |
| owner | Workload, routing |

## 6. Chart rules

- One message per chart. **The title states the takeaway** ("P2 backlog grew 20% in Q3").
- Use a consistent colour per priority across all charts.
- Never rely on colour alone: pair it with text or icons, and check contrast in light and dark themes.
- Prefer bars to pies with more than 4 slices.
- Default to the current period. Never average separate planning periods without labelling it.
- The layout must work at phone width.

## 7. Optional composite health score

A score helps rank areas, but always **show its components next to it**.

```
health = 100
       − 15 × open P1 count
       −  5 × SLO breaches
       −  2 × SLO warnings
       − 10 × (inflow > outflow for 3 consecutive weeks)
```

*The weights are illustrative. Calibrate them against your own history.*

## 8. Pipeline & maintenance

```
Saved tracker queries ─► Fetch (API) ─► Evaluate rules ─► Render (static page) ─► Publish
         ▲                                    ▲
     config file                    thresholds in config
```

- Keep extraction, transformation and presentation as **separate steps**.
- Keep queries and thresholds in **version-controlled config**, never hard-coded.
- For small audiences with stable questions, a static page rebuilt from a data file is often faster and cheaper than heavy BI tooling.
- Use scheduled refreshes for the baseline and on-demand refreshes for live reviews.
- Put the dashboard behind the same access controls as the source data.
- Publishing is part of the Definition of Done. A change that isn't live hasn't shipped.

## 9. Example insight narrative (fictional)

> Open P1/P2 defects fell 30% month on month, but **one product area accounts for 45% of new P3s**, concentrated in the two weeks after the last release. *Recommendation:* add a targeted regression pack for that area before the next release.
