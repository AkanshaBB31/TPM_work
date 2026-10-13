"""Classify defects against resolution SLOs and print a summary.

Portfolio example. Thresholds are illustrative; tune them to your own service
agreements. Uses only the Python standard library.

Usage:
    python slo_calculator.py sample-defects.csv [--as-of YYYY-MM-DD]

CSV columns: id,title,priority,area,created,resolved   (resolved may be blank)
"""
from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import date

# priority -> (target_days, warning_window_days); None = best effort, not tracked
TARGETS = {
    "P1": (3, 1),
    "P2": (14, 4),
    "P3": (30, 7),
    "P4": None,
}

STATES = ("MET", "BREACHED", "WARNING", "ON_TRACK")


def classify(created: date, resolved: date | None, priority: str, as_of: date) -> str | None:
    """Return the SLO state for one defect, or None if the priority has no target."""
    rule = TARGETS.get(priority)
    if rule is None:
        return None
    target, window = rule
    age = ((resolved or as_of) - created).days
    if resolved:
        return "MET" if age <= target else "BREACHED"
    if age > target:
        return "BREACHED"
    if age > target - window:
        return "WARNING"
    return "ON_TRACK"


def parse_date(value: str) -> date | None:
    return date.fromisoformat(value) if value else None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("csv_path")
    parser.add_argument("--as-of", type=date.fromisoformat, default=date.today())
    args = parser.parse_args()

    by_priority: dict[str, Counter] = defaultdict(Counter)
    warnings = []
    with open(args.csv_path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            created = parse_date(row["created"])
            resolved = parse_date(row["resolved"])
            state = classify(created, resolved, row["priority"], args.as_of)
            if state is None:
                continue
            by_priority[row["priority"]][state] += 1
            if state == "WARNING":
                target = TARGETS[row["priority"]][0]
                left = target - (args.as_of - created).days
                warnings.append((left, row["id"], row["priority"], row["area"], row["title"]))

    print(f"Defect SLO summary as of {args.as_of}\n")
    print(f"{'Priority':<9}{'Total':>6}" + "".join(f"{s:>10}" for s in STATES))
    totals: Counter = Counter()
    for prio in sorted(by_priority):
        c = by_priority[prio]
        totals.update(c)
        print(f"{prio:<9}{sum(c.values()):>6}" + "".join(f"{c[s]:>10}" for s in STATES))
    print(f"{'All':<9}{sum(totals.values()):>6}" + "".join(f"{totals[s]:>10}" for s in STATES))

    scored = totals["MET"] + totals["BREACHED"]
    if scored:
        print(f"\nAttainment (MET / (MET + BREACHED)): {totals['MET'] / scored:.0%}")

    if warnings:
        print("\nApproaching breach:")
        for left, tid, prio, area, title in sorted(warnings):
            print(f"  {tid}  {prio}  {area:<14} {left}d left  {title}")


if __name__ == "__main__":
    main()
