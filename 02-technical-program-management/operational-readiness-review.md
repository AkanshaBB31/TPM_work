# Operational Readiness Review (ORR)

**Skill:** Technical program management · **Competency:** Observability governance and non-functional readiness
**Standards:** Google SRE production readiness, ITIL service transition

Functional tests show that a feature *works*. An ORR shows that it can be **operated**: monitored, scaled, secured, supported and recovered. Run it before the first production launch of a new service or major capability, ideally 1–2 weeks before go/no-go.

## 1. Observability

- [ ] Service-level indicators defined (availability, latency, error rate) with SLO targets
- [ ] Dashboards exist for the key user journeys, not just infrastructure
- [ ] Alerts are tied to SLOs and symptoms, not only to causes
- [ ] Every alert links to a runbook
- [ ] Logs are structured, searchable, and free of secrets and personal data
- [ ] Distributed tracing covers cross-service calls
- [ ] Synthetic checks cover critical journeys

## 2. Capacity & performance

- [ ] Expected peak load estimated, with headroom (e.g. 2× peak)
- [ ] Load test run against the release candidate; results recorded
- [ ] Autoscaling limits and quotas reviewed
- [ ] Downstream dependencies can absorb the new load

## 3. Resilience

- [ ] Failure modes documented (dependency down, slow, returning errors)
- [ ] Timeouts, retries with backoff, and circuit breakers configured
- [ ] Graceful degradation defined for non-critical features
- [ ] Backup and restore tested; RPO/RTO documented
- [ ] [Rollback plan](../04-release-management/rollback-planning-template.md) tested

## 4. Security & compliance

- [ ] Threat model reviewed
- [ ] Authentication and authorisation follow least privilege
- [ ] Secrets in a secret manager; none in code or config
- [ ] Dependency and container scans clean, or exceptions approved
- [ ] Data classification and retention rules applied

## 5. Support readiness

- [ ] On-call rota and escalation path defined
- [ ] Runbooks for the top failure scenarios
- [ ] Support team trained; known issues documented
- [ ] The [incident communication plan](../05-quality-and-reliability/incident-communication-playbook.md) covers this service

## 6. Outcome

| Area | Owner | Status | Gaps / actions |
|---|---|---|---|
| Observability | | 🟢 / 🟡 / 🔴 | |
| Capacity | | | |
| Resilience | | | |
| Security | | | |
| Support | | | |

**Rule:** any 🔴 blocks launch unless the accountable owner records an exception with an expiry date. ORR gaps feed the [release readiness checklist](../04-release-management/release-readiness-checklist.md).

## 7. TPM's role

The TPM doesn't answer these questions. The TPM makes sure **the right owner answers each one**, with evidence, before the deadline, and that the gaps are tracked to closure.
