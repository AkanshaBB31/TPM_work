# Escalation Playbook

**Skill:** Leadership & governance · **Competency:** Escalating early and constructively

## 1. Escalation is a tool, not a failure

Escalate when you need a decision or resource from above your level **and** the options get worse after a deadline. Escalating early, with options, protects commitments. Escalating late, with only problems, damages trust.

## 2. When to escalate

| Trigger | Example |
|---|---|
| A decision outside your authority | A scope vs. date trade-off |
| A high risk with no mitigation in the team's control | A [RAID](../01-program-governance/raid-log-template.md) score of 15 or more |
| A dependency missed with no recovery plan | No committed date after 2 follow-ups |
| An SLO breach is likely or has happened, with no ETA | A P1 past target |
| Conflicting priorities between teams | Two teams need the same specialist |

## 3. Levels (response times illustrative)

| Level | To | When | Expected response |
|---|---|---|---|
| L0 | Peer / dependency owner | First contact | 1–2 business days |
| L1 | Team leads / delivery lead | L0 unresolved, or a dependency at risk | 1 business day |
| L2 | Engineering / product manager | A milestone at risk | 1 business day |
| L3 | Director / sponsor / steering | A quarterly commitment or a customer at risk | Same day, or next steering if not critical |

## 4. The escalation message

Use **SBAR** (Situation, Background, Assessment, Recommendation). It's also known as SCQA (Situation, Complication, Question, Answer).

```
Subject: [Decision needed by <date>] <short issue>

Situation:      <one sentence: what's happening>
Background:     <context and what's been tried>
Assessment:     <impact on scope / time / cost / quality, and the cost of waiting>
Options:
  A. <option>: pros / cons
  B. <option>: pros / cons
Recommendation: <A or B, and why>
Ask:            <the specific decision or resource, from whom, by when>
```

> **Example (fictional):** The SSO API isn't in staging yet (**S**). It was agreed for 05-01, and we've synced weekly since 04-10 (**B**). Each day of delay pushes the onboarding launch by a day, and after 05-08 it moves into next quarter (**A**). Please help prioritise the API with the identity team's manager this week, or approve descoping SSO from the first release (**R**).

## 5. Do / don't

| Do | Don't |
|---|---|
| Tell the person you're escalating past, *before* you do it | Blindside anyone |
| Bring options and a recommendation | Bring only problems |
| Use dates, data and links | Use adjectives and unproven urgency |
| Handle sensitive topics 1:1 | Escalate in a group channel what should be a private conversation |
| Close the loop: record the outcome in the [decision log](../01-program-governance/decision-log-template.md) and tell everyone affected | Leave escalations hanging |
