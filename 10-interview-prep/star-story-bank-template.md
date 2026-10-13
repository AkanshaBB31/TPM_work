# STAR Story Bank Template

Build a reusable bank of experience stories, each mapped to the competencies it demonstrates. A single strong story can answer several questions.

> **Confidentiality rule:** describe situations generically ("a payments integration for a large enterprise customer"). Never name employers' clients, internal systems or code names, or quote confidential figures. Use ranges or percentages where you need to.

## Competency coverage map

| Competency | Story #1 | Story #2 | Story #3 |
|---|---|---|---|
| Delivered a complex multi-team program | | | |
| Managed a critical dependency or risk | | | |
| Drove a release / go-no-go decision | | | |
| Handled an incident or crisis | | | |
| Resolved stakeholder conflict | | | |
| Influenced without authority | | | |
| Used data to change a decision | | | |
| Automated or scaled a process | | | |
| Failed and learned | | | |
| Improved team process or quality | | | |

## Story template

```markdown
### Story <n>: <short, generic title>

**Competencies:** <e.g. dependency management, escalation>

**Situation** (2–3 sentences): Context, scale, constraints. Keep it generic.

**Task** (1–2 sentences): What *you* were responsible for.

**Actions** (3–5 bullets, written with "I"):
- I …
- I …

**Result** (quantified): e.g. "launched on the original date; change failure rate fell from ~20% to under 10%"

**Learning:** What you'd do differently, or now do every time.

**Follow-up questions to prepare for:**
- What would you do if …?
- How did you measure …?
```

## Example (fictional)

### Story 1: Recovering a slipping integration milestone

**Competencies:** dependency management, escalation, stakeholder communication

**Situation:** A customer-facing launch depended on an API from another team, which was two weeks late with no committed date.
**Task:** As TPM, I had to protect the launch date without authority over the providing team.
**Actions:**
- I quantified the critical-path impact and logged it as a high risk.
- I agreed an interface contract so that our team could build against a stub.
- I escalated with two options (re-prioritise, or descope a sub-feature) and a recommendation.
- I set up a weekly dependency sync and a shared board.
**Result:** We launched on the original date with the sub-feature descoped, and it followed three weeks later.
**Learning:** I now require committed dates and contracts for every critical-path dependency at kickoff.
