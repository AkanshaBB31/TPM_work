# AI-Assisted Program Management Workflows

**Skill:** AI-assisted productivity · **Competency:** Designing safe, repeatable AI-agent workflows for delivery management

Vendor-neutral patterns for using LLM agents with tool access to automate recurring program-management work, **while keeping a person accountable**.

## 1. Workflow catalog

| Workflow | Input | Agent does | Person does |
|---|---|---|---|
| **Meeting → action items** | Notes / transcript | Extracts actions, owners, due dates and the supporting evidence; drafts tickets | Approves each item before it's created |
| **Findings → tickets** | Audit, health check or retro findings | Drafts tickets with the evidence attached | Approves; sets priority |
| **Requirements readiness review** | PRD + upstream goal doc | Checks it against the [Definition of Ready](../03-agile-delivery/definition-of-ready-and-backlog-decomposition.md); lists gaps | Decides whether it's ready |
| **Requirements → backlog** | Approved PRD | Proposes an epic → story breakdown with acceptance criteria | Re-sizes, re-orders, approves |
| **Status report draft** | Tracker query + last report | Drafts the bottom line, RAG and changes since last week | Edits tone; adds the asks |
| **Progress digest** | Completed items, merged code changes, blockers | Drafts a daily or weekly update | Edits before posting |
| **Release notes draft** | Released change list | Groups changes into New / Improved / Fixed in customer language | Removes internal details |
| **Readiness check** | Release candidates | Evaluates the [gate criteria](../04-release-management/change-readiness-gate-and-go-no-go.md) and lists the gaps | Makes the go/no-go call |
| **Dashboard refresh** | Tracker export | Rebuilds the data file and the static page | Spot-checks numbers; publishes |

## 2. Package each workflow as a reusable "skill"

Each workflow is a short, version-controlled instruction file:

```markdown
---
name: weekly-status-draft
description: Draft the weekly executive status from tracker data.
  Use on Friday mornings. Not for incident updates.
---
1. Query open commitments for the current quarter (read-only).
2. Compare them with last week's snapshot; list status changes.
3. Fill in the executive status template. Never invent risks, asks or numbers.
4. Cite the source item for every claim.
5. Output the draft only. Do not send it.
```

Every skill defines:
- a **trigger description**: when to use it, and when *not* to
- **inputs** (query, date range, team)
- **steps**: a deterministic procedure
- an **output contract**: the format, where it goes, and what "done" means

## 3. Interactive vs. unattended variants

| Variant | Behaviour |
|---|---|
| Interactive | Can ask clarifying questions; shows output in the chat |
| Unattended (scheduled) | Takes every input from config; never asks; publishes and reports; fails loudly |

Keeping two variants stops scheduled runs from hanging on a question nobody is there to answer.

## 4. The action-item extraction rule set

| Field | Rule |
|---|---|
| Action | Starts with a verb; one deliverable |
| Owner | One named person or role |
| Due date | Explicit, or a default (e.g. +5 business days) flagged for confirmation |
| Evidence | A quote or link back to the source |

**Don't extract** decisions (they go to the [decision log](../01-program-governance/decision-log-template.md)), FYIs, or vague intentions ("we should look into…").

Review table, shown before anything is created *(fictional)*:

| # | Action | Owner | Due | Create? |
|---|---|---|---|---|
| 1 | Draft rollback runbook for v4.3 | Eng lead | 05-12 | ✅ |
| 2 | Confirm UAT environment dates with the platform team | TPM | 05-09 | ✅ |
| 3 | "Look into performance" | ? | ? | ❌ needs clarification |

## 5. Guardrails (non-negotiable)

1. **Read-only by default.** Write actions (creating tickets, posting messages) need explicit confirmation, or are limited to known destinations.
2. **Human in the loop** for anything outward-facing and for any judgment call.
3. **Grounded output.** Every generated claim links to its source record. No invented numbers.
4. **Deterministic where possible.** Scripts count and filter; the AI writes the narrative.
5. **No secrets in prompts or skill files.**
6. **Data boundaries.** The agent runs under the user's own permissions and access is never widened for it. Confidential data stays inside approved tools.
7. **Version the prompts** like code, with reviews and a changelog.
8. **Auditability.** Log what was generated, from which inputs, and who approved it.

## 6. Measuring value

| Metric | How to measure |
|---|---|
| Time saved | Report preparation time before vs. after (measure your own baseline) |
| Accuracy | Errors caught at human review, per report |
| Consistency | % of outputs that match the template |
| Adoption | People or teams using the workflow each week |
