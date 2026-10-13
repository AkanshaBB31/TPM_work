# Change Readiness Gate & Go/No-Go Meeting

**Skill:** Release governance · **Standard:** ITIL 4 Change Enablement (CAB / change authority)

Without explicit criteria, readiness reviews turn into status meetings, and decisions go to whoever sounds most confident. A **gate** makes readiness a checkable state that's evaluated *before* the meeting, so the meeting only has to deal with exceptions.

---

## Part 1: The gate

An item is **Ready** only when **all mandatory criteria** pass. Advisory signals add context but never block on their own.

### Mandatory criteria (examples; tailor them to your process)

| # | Criterion | Evidence source | Pass rule |
|---|---|---|---|
| M1 | Planned date falls in the review window | Planned release date | Within the configured window |
| M2 | Work is complete and verified | Tracker status | Status is in your organisation's "verified" set |
| M3 | Test evidence exists | Linked test run | A passing regression run since the last code change |
| M4 | Rollback plan exists | Linked document | Reviewed by the owning team |
| M5 | No blocking defects | Linked defects | Zero open defects at the highest severity |

### Advisory signals

| # | Signal | Why it matters |
|---|---|---|
| A1 | Stakeholder acceptance completed | Reduces acceptance surprises |
| A2 | Release owner assigned | Someone is accountable |
| A3 | Change is unplanned / expedited | Gets closer scrutiny |

### Outcome states

| State | Meaning | Action |
|---|---|---|
| ✅ Ready | All mandatory criteria pass | Consent agenda: approve without discussion |
| 🟡 At risk | A gap that can be fixed before the review | Nudge the owner about the specific gap |
| 🔴 Not ready | A gap that can't be fixed in time | Defer to the next window, or escalate |
| ⚪ Out of window | Planned outside this window | Listed for awareness |

### Example (fictional)

| Item | M1 | M2 | M3 | M4 | M5 | Outcome | Gap |
|---|---|---|---|---|---|---|---|
| Checkout redesign | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ Ready | |
| Search ranking v2 | ✅ | ✅ | ❌ | ✅ | ✅ | 🟡 At risk | No regression run since the last merge |
| Loyalty points API | ✅ | ❌ | ❌ | ❌ | ✅ | 🔴 Not ready | Still in development |
| Admin audit log | ❌ | ✅ | ✅ | ✅ | ✅ | ⚪ Out of window | Next cycle |

### Design notes

- **Make the criteria data-driven.** Each one should map to a tracker field or link. A criterion that can't be checked automatically gets skipped under pressure.
- **Keep thresholds in version-controlled config,** not in people's heads.
- **Show the reason, not just the flag.** "Not ready: no test evidence" gets fixed faster than a red cell.
- The evaluation is easy to automate (see the [scheduled alerting pattern](../08-automation/scheduled-alerting-pattern.md)).

---

## Part 2: The go/no-go meeting (30 min)

### Timeline

| When | Activity |
|---|---|
| T-N days | Pull candidates with a saved query; evaluate the gate; publish the readiness report |
| T-1 day | Owners close gaps; re-run the gate. 🟡/🔴 owners prepare a recommendation (fix, defer or accept the risk) |
| T-0 | Meeting. **Cancel it if no decision-maker can attend.** |

### Agenda

| Time | Segment | Output |
|---|---|---|
| 0–5 | **Consent agenda:** read out the ✅ items; approve unless someone objects | Bulk approval |
| 5–20 | **Exceptions:** each 🟡/🔴 owner presents the gap, the options and a recommendation | A decision per item |
| 20–25 | **Operational check:** on-call, rollback, communications | Confirmation |
| 25–30 | **Recap:** read back each decision and its owner | [Decision log](../01-program-governance/decision-log-template.md) entry |

### Decision options

- **Go:** ship as planned
- **Go with conditions:** ship if a named condition is met by a set time
- **No-go, defer:** move to the next window
- **No-go, escalate:** a cross-team blocker needs sponsor input

**Decision rule:** any failed gate means **No-go** unless the accountable approver records a waiver that names the risk.

### Anti-patterns

- Walking through every item one by one, whether it's ready or not
- Deciding without the release owner present
- Treating "we'll monitor closely" as a mitigation plan
- Leaving the meeting without written decisions
