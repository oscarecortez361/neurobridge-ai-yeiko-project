# NeuroBridge AI Architecture

## Conceptual layers

1. **Session data layer** — synthetic or properly consented observations from activities and therapy sessions.
2. **Digital profile / twin state** — current goals, recent performance, trends, preferences, and support context.
3. **Analytics layer** — progress summaries, trend detection, and later anomaly detection.
4. **Recommendation layer** — future explainable suggestions for activities or follow-up questions.
5. **Human review layer** — caregiver, therapist, or clinician reviews any recommendation before it affects care.
6. **Dashboard layer** — clear visualization of goals, trends, and changes over time.

## Design goals

- privacy first
- explainable outputs
- human oversight
- synthetic data for early development
- no diagnostic claims in the prototype
- clear audit trail of recommendations and overrides

## Digital twin interpretation

The 'twin' is not a perfect copy of a person. It is a structured, changing software representation of selected therapy goals and observed progress used to support visualization and decision support.
