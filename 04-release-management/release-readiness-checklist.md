# Release Readiness Checklist

**Skill:** Release management · **Standard:** ITIL 4 Release & Change Enablement

Use this checklist for each release candidate. Feed the results into the [go/no-go](change-readiness-gate-and-go-no-go.md) 24–48 hours before the release window.

- **Gate** rows (🔒) block the release if they fail, unless an approver records an exception.
- **Every tick needs evidence**, either a link or an artifact. A tick without evidence doesn't count.

## Release: `<version>` · Window: `<date, time, tz>` · Release owner: `<role>`

### 1. Scope

| Check | Gate | Evidence | ☐ |
|---|---|---|---|
| Scope frozen; item list attached | 🔒 | | ☐ |
| Every item in a release-eligible state and linked to an approved backlog item | 🔒 | | ☐ |
| Late additions approved by the release owner | 🔒 | | ☐ |
| Descoped items moved to a later release and communicated | | | ☐ |

### 2. Quality

| Check | Gate | Evidence | ☐ |
|---|---|---|---|
| Regression suite passed on the release-candidate build | 🔒 | | ☐ |
| No open highest-severity defects; next-severity defects accepted in writing | 🔒 | | ☐ |
| Security scan: no new critical or high findings, or exceptions documented | 🔒 | | ☐ |
| Performance compared with the previous release (e.g. no regression > 10%) | | | ☐ |

### 3. Operational readiness

| Check | Gate | Evidence | ☐ |
|---|---|---|---|
| Deployment runbook reviewed (and rehearsed, for major releases) | 🔒 | | ☐ |
| [Rollback plan](rollback-planning-template.md) written and tested | 🔒 | | ☐ |
| Database migrations backward compatible; tested forward and back | 🔒 | | ☐ |
| On-call confirmed for the release window | 🔒 | | ☐ |
| Monitoring and alerts cover the new functionality | | | ☐ |
| Feature-flag states and defaults documented | | | ☐ |
| [Operational readiness review](../02-technical-program-management/operational-readiness-review.md) passed (new services) | 🔒 | | ☐ |

### 4. Dependencies

| Check | Gate | Evidence | ☐ |
|---|---|---|---|
| Upstream/downstream components released or version-compatible | 🔒 | | ☐ |
| Vendor or third-party changes confirmed | | | ☐ |

### 5. Business readiness

| Check | Gate | Evidence | ☐ |
|---|---|---|---|
| Stakeholder demo / acceptance sign-off | | | ☐ |
| [Release notes](release-notes-framework.md) drafted | | | ☐ |
| Support briefed on changes and known issues | 🔒 | | ☐ |
| Customer communications scheduled (if user-visible) | | | ☐ |

### 6. Governance

| Check | Gate | Evidence | ☐ |
|---|---|---|---|
| Change request raised and approved per policy | 🔒 | | ☐ |
| Release window respects freeze periods | 🔒 | | ☐ |
| Go/no-go decision recorded | 🔒 | | ☐ |

## Sign-off

| Role | Name | Decision | Date | Notes |
|---|---|---|---|---|
| Release owner | | Go / No-Go | | |
| QA lead | | Go / No-Go | | |
| Engineering lead | | Go / No-Go | | |
| Product owner | | Go / No-Go | | |

**Exceptions granted:** *(item, reason, approver, expiry)*
