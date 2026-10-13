# 08 · Automation

Automating the routine parts of program management, such as alerts, digests, hygiene checks and report drafts, while people stay accountable for the judgment calls.

| File | Use it to… |
|---|---|
| [scheduled-alerting-pattern.md](scheduled-alerting-pattern.md) | Design reliable, low-noise scheduled jobs that read a tracker and post to chat |
| [ai-assisted-pm-workflows.md](ai-assisted-pm-workflows.md) | Package recurring PM tasks as safe, reusable AI-agent workflows |
| [tracker-hygiene-checks.md](tracker-hygiene-checks.md) | Keep the data behind reports and automation trustworthy |
| [examples/](examples/) | A runnable defect-SLO classifier using the Python standard library only |

## Run the example

```bash
python examples/slo_calculator.py examples/sample-defects.csv --as-of 2026-03-31
```

Example output (abridged):

```
Defect SLO summary as of 2026-03-31

Priority  Total       MET  BREACHED   WARNING  ON_TRACK
P1            3         1         1         0         1
P2            4         1         2         1         0
P3            3         0         1         1         1
All          10         2         4         2         2

Attainment (MET / (MET + BREACHED)): 33%

Approaching breach:
  EX-105  P2  Payments       3d left  Refund status not updating
  EX-104  P3  Notifications  4d left  Receipt email missing logo
```

All of the sample data is fictional.

**Skills shown:** workflow automation · idempotent job design · config-driven systems · AI agent design with guardrails · Python scripting
