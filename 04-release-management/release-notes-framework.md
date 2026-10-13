# Release Notes Framework

**Skill:** Change communication · **Competency:** Turning engineering changes into communication suited to each audience

## 1. Principle: capture at merge, compile at release

Hand-written notes drift from what actually shipped. Capture change metadata **when the change is made**, then *compile* the release notes.

```
Per-change entry (at merge) ──► Collected between release tags ──► Edited by a person ──► Published editions
                                                                                         ├── Customer
                                                                                         ├── Support / internal
                                                                                         └── Operator
```

## 2. Per-change entry schema

```yaml
change_ref: <work item or PR reference>
component: <component>
type: feature | improvement | fix | security | deprecation | breaking
summary: "You can now…"          # one sentence, user language, ≤ 200 chars
customer_visible: true | false
requires_action: none | config | migration | client-update
risk: low | medium | high
```

**Validation rules (automatable)**
- `summary` is present and short
- `breaking` changes include migration steps
- Customer-visible summaries contain no internal jargon or identifiers

## 3. Template

```markdown
# <Product> <Version>: Release Notes
Release date: YYYY-MM-DD

## Highlights
- 2–4 bullets on what matters most to users

## ✨ New features
- **<Feature>:** what it does and who benefits

## 🛠 Improvements
- <Change>, with the measurable effect if known

## 🐞 Fixes
- Fixed <symptom> when <condition>

## ⚠️ Breaking changes & required actions
| Change | Who is affected | Action required | Deadline |
|---|---|---|---|

## Deprecations
- <Item>: removal planned in <version/date>

## Known issues
- <Issue>, with a workaround

---
## Operator / internal appendix (never published externally)
| Item | Feature flag | Default | Owning team | Rollback impact |
|---|---|---|---|---|
- Config changes · Migrations (reversible?) · Component version changes
```

## 4. Worked example (fictional)

> **Example App 2.8.0**
> **✨ Saved carts:** save a cart and finish checking out on any device.
> **🛠** The checkout page loads about 30% faster on mobile.
> **🐞** Fixed discount codes not applying to bundled items.
> **⚠️ Known issue:** saved carts expire after 30 days. A configurable expiry is planned.

## 5. Style rules

- Describe the **effect**, not the implementation. Write "Search results load faster", not "Refactored the query builder".
- One change per bullet, one sentence each.
- Describe the symptom that was fixed, not its internal cause.
- Never include internal ticket IDs, hostnames, code names or people's names in customer editions.
- Group by impact, not by team.
