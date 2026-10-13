# Decision Log Template

**Skill:** Decision governance · **Practice:** Adapted from Architecture Decision Records (ADRs) for delivery, scope and technical choices

Decisions get lost in meetings and chat threads. A decision log records **what** was decided, **why**, **who** decided it and **what was rejected**, so the same questions don't keep coming back.

## When to log

Log a decision if it:
- changes scope, dates, cost, architecture or customer commitments
- is hard to reverse
- chooses between options that were all seriously considered
- involved disagreement (record the dissent as well as the outcome)
- would confuse someone joining in three months

## Index

| ID | Date | Decision | Decider | Status |
|---|---|---|---|---|
| DEC-001 | 2026-02-12 | Defer offline mode to the next release | Product director | Accepted |
| DEC-002 | 2026-03-04 | Adopt a fortnightly release train | Delivery lead | Superseded by DEC-009 |

## Record template

```markdown
### DEC-<n>: <short title>

- **Date:** YYYY-MM-DD
- **Status:** Proposed | Accepted | Rejected | Superseded by DEC-<n>
- **Decide (one accountable person):** <role>
- **Recommend / Agree / Input / Perform:** <roles>   ← RAPID roles
- **Informed:** <roles / channels>

**Context:** What forced a decision? Which constraints apply?

**Options considered**
| Option | Pros | Cons |
|---|---|---|
| A | | |
| B | | |
| Do nothing | | |

**Decision:** The chosen option, in one sentence, and the deciding factor.

**Consequences:** What gets easier, what gets harder, and which new risks to log in the RAID log.

**Revisit by:** <date or trigger>
```

## Worked example (fictional)

**DEC-001: Defer offline mode to the next release.** Offline sync testing found data-conflict edge cases, and fixing them would delay launch by 3 weeks. The options were (1) delay the release and keep the scope, or (2) launch on time without offline mode. **Option 2 was chosen.** The launch is tied to an external event that can't move, and offline mode affects fewer than 10% of target users. *Consequences:* Support publishes a known-limitation FAQ, and offline mode becomes the first epic of the next release.

## Rules

1. One decision per record.
2. Accepted records are never edited. Supersede them with a new record.
3. Link each decision from the RAID items and backlog items it affects.
