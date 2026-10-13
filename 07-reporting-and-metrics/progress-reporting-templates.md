# Progress Reporting Templates

**Skill:** Status reporting & transparency · **Competency:** Consistent, low-effort progress visibility at every level

## 1. Daily async update (individual)

```markdown
**Done**
- <outcome>: <link to work item / code change>

**Today**
- <planned outcome>

**Blockers**
- <blocker>: need <who/what> by <when>     (or "None")
```

*Rules:* write outcomes, not activities; link the evidence; give every blocker a named ask.

## 2. Weekly activity recap (individual)

| Category | Items |
|---|---|
| Delivered | Work items closed, code changes merged |
| In progress | Item and the next step |
| Reviews & support | Code reviews, incidents assisted |
| Learning / improvement | Optional |
| Next week | Top 3 |

## 3. Team commitment scoreboard (quarterly)

| Commitment | Team | Status | Progress | Evidence | Risk |
|---|---|---|---|---|---|
| Self-service password reset | Team A | 🟢 In progress | 4 of 6 stories | Merged changes, demo | Low |
| Bulk export | Team B | 🟠 At risk | 1 of 5 stories | — | Upstream API |
| Search performance | Team A | ✅ Done | 3 of 3 | Release 4.2 | — |

**Summary line:** *7 of 10 commitments on track, 2 at risk, 1 done.* (Fictional.)

## 4. Evidence over self-reporting

Base status on **artifacts**, not self-reported percentages:
- Work-item state transitions
- Merged code changes linked to the work item
- Open review requests
- Demos and deployed environments

Automating the collection of this evidence (see [AI-assisted PM workflows](../08-automation/ai-assisted-pm-workflows.md)) cuts reporting effort and makes the reports more accurate. The person still edits before posting.
