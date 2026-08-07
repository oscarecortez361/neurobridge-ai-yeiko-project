# NeuroBridge AI: The Yeiko Project

NeuroBridge AI is a long-term assistive-technology concept focused on autism support, therapy progress, adaptive activities, and caregiver/therapist insights. This repository develops the project as a responsible AI and digital-twin platform rather than a one-off class assignment.

## Vision

The goal is to create a system that can represent a learner's therapy goals and session history as a changing digital profile, then use that information to support personalized activities and clearer progress tracking.

## Core ideas

- Digital twin inspired therapy profile
- Session and activity tracking
- Adaptive activity recommendations
- Caregiver and therapist dashboards
- Progress trends over time
- Explainable recommendation logic
- Privacy and consent by design
- Human-in-the-loop decisions

## Important boundary

NeuroBridge AI is an educational and research prototype. It is **not a diagnostic tool**, does not replace clinicians, and should not make medical or behavioral treatment decisions without qualified human oversight.

## Repository structure

```text
.
├── README.md
├── data/
│   └── synthetic_progress.csv
├── docs/
│   ├── ARCHITECTURE.md
│   └── RESPONSIBLE_AI.md
└── src/
    └── progress_demo.py
```

## Starter prototype

The initial prototype uses synthetic data to summarize progress across activities. No real patient or child data is required.

```bash
python src/progress_demo.py
```

## Roadmap

1. Synthetic progress tracking
2. Goal and activity data model
3. Caregiver/therapist dashboard
4. Explainable recommendation engine
5. Optional VR/AR therapy environment concepts
6. Digital twin state updates from session data
7. Strong privacy, consent, auditing, and role-based access controls

## Project status

**Early prototype / long-term platform concept.** Development starts with safe synthetic data and transparent logic before adding more advanced AI components.

## Author

Oscar Cortez  
AI and Robotics Engineering
