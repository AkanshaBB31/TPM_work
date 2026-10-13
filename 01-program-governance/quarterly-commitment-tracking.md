# Quarterly Commitment Tracking Framework

**Skill:** Program governance · **Competency:** Portfolio planning and delivery assurance

A lightweight way to make quarterly commitments visible, measurable and honest. It works for any organisation that plans in quarters and executes in sprints.

## 1. Principles

1. **A commitment is a promise with a date.** It has one owner, one target quarter and a clear definition of done.
2. **Lock the baseline.** Snapshot the committed list on day 1. Anything added later counts as *scope added*.
3. **Never blend quarters.** Report each quarter on its own, because averaging across quarters hides a bad one.
4. **Done means in customers' hands.** An item counts as delivered only when it's released to production, or to another agreed final environment.

## 2. Commitment register

| ID | Commitment | Owner (role) | Program | Target Qtr | Size | Status | Confidence | Target date | Actual date |
|---|---|---|---|---|---|---|---|---|---|
| C-01 | Self-serve onboarding flow | Growth EM | Growth | Q2 | L | In progress | 🟢 High | 2026-06-12 | |
| C-02 | Audit log export | Platform EM | Platform | Q2 | M | At risk | 🟠 Medium | 2026-05-29 | |
| C-03 | Mobile push preferences | Mobile EM | Engagement | Q2 | S | Done | | 2026-04-30 | 2026-04-28 |

- **Status flow:** Not started → In progress → In review/test → Released → Done
- **Off-track states:** *At risk* (still achievable with intervention) and *Slipped* (moved to a later quarter). A slipped item stays in its original quarter's report as a miss.
- **Confidence** is set by the owner each week, not inferred by the PM.

## 3. Weekly scorecard

```
Q2 Commitments: Week 7 of 13
──────────────────────────────────────
Committed (baseline)      24
Delivered                  9   (38%)
On track                  10
At risk                    3   → see risk notes
Slipped                    2   → moved to Q3, reasons logged
Scope added mid-quarter    4   (tracked separately)
Expected landing       19–21 of 24 (79–88%)
```

Give expected landing as a **range**. A single number implies false precision.

## 4. Views every report should support

- Filter by program, team, quarter (current by default), status and confidence
- **Data hygiene exception:** items marked done but without a release date. Surface these rather than hiding them.

## 5. Cadence

| When | What | Who |
|---|---|---|
| Quarter start | Lock and publish the baseline | PM + owners |
| Weekly | Update confidence and refresh the scorecard | Owners → PM |
| Bi-weekly | Steering review of at-risk items | PM + sponsors |
| Quarter end | Close out: % delivered, slip reasons, lessons learned | PM |

## 6. Close-out questions

- What share of slips came from estimation, dependencies, scope change or capacity?
- Did mid-quarter additions displace committed work?
- Were risks raised early (more than 3 weeks before the slip) or late?
