"""Simple synthetic progress demo for NeuroBridge AI.

No real patient data is used. This script demonstrates how session scores
could be summarized before any recommendation logic is added.
"""

from collections import defaultdict


SYNTHETIC_SESSIONS = [
    {"activity": "communication", "score": 62},
    {"activity": "communication", "score": 68},
    {"activity": "communication", "score": 73},
    {"activity": "motor", "score": 70},
    {"activity": "motor", "score": 74},
    {"activity": "motor", "score": 77},
    {"activity": "attention", "score": 58},
    {"activity": "attention", "score": 63},
    {"activity": "attention", "score": 66},
]


def summarize_progress(sessions):
    grouped = defaultdict(list)
    for session in sessions:
        grouped[session["activity"]].append(session["score"])

    print("NeuroBridge AI - Synthetic Progress Summary\n")
    for activity, scores in grouped.items():
        change = scores[-1] - scores[0]
        trend = "improving" if change > 0 else "stable" if change == 0 else "declining"
        print(
            f"{activity:14s} start={scores[0]:>3}  latest={scores[-1]:>3}  "
            f"change={change:+3d}  trend={trend}"
        )


if __name__ == "__main__":
    summarize_progress(SYNTHETIC_SESSIONS)
