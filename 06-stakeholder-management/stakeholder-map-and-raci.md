# Stakeholder Map & RACI

**Skill:** Stakeholder management · **Standard:** PMBOK stakeholder engagement

## 1. Power / interest grid

```
              HIGH INTEREST
                   │
    Keep           │   Manage
    satisfied      │   closely
  ─────────────────┼─────────────────  HIGH POWER ▶
    Monitor        │   Keep
                   │   informed
                   │
              LOW INTEREST
```

## 2. Register

| Stakeholder (role) | Power | Interest | Quadrant | Current stance | Desired stance | What they care about | Engagement approach | Owner |
|---|---|---|---|---|---|---|---|---|
| Executive sponsor | H | H | Manage closely | Supportive | Champion | Business outcome, risk | Fortnightly 1:1; executive report | TPM |
| Head of Support | M | H | Keep informed | Concerned | Supportive | Defect SLOs, known issues | Weekly SLO digest; triage invite; early release notes | QA lead |
| Security lead | H | M | Keep satisfied | Neutral | Supportive | Release risk | Early design review; release gate | Eng lead |
| Finance partner | H | L | Keep satisfied | Neutral | Neutral | Budget variance | Monthly summary | TPM |
| End-user group | L | H | Keep informed | Concerned | Supportive | Usability, change impact | Demos, release notes | Product |

*Use roles, not real names, in shared templates.*

**Stance scale:** Resistant → Concerned → Neutral → Supportive → Champion

Revisit the register at each phase gate, because stakeholders move between quadrants as a program progresses.

## 3. RACI for key activities

| Activity | Sponsor | TPM / PM | Product | Eng lead | QA | Support |
|---|---|---|---|---|---|---|
| Scope sign-off | A | C | R | C | I | I |
| Quarterly commitment baseline | I | A | R | R | C | I |
| Release go/no-go | I | A/R | C | C | C | I |
| Defect prioritisation | I | C | A | R | R | C |
| Status reporting | I | A/R | C | C | C | I |
| Customer communication | I | R | A | C | I | C |

*R = Responsible · A = Accountable (exactly one per row) · C = Consulted · I = Informed*

## 4. Engagement principles

- **No surprises:** bad news reaches sponsors in person *before* it appears in a report.
- **Tailor the depth:** executives get outcomes and asks; teams get detail.
- **Frame requests in terms of their goals,** not yours.
- **One source of truth:** every report links to the same tracker or dashboard.
