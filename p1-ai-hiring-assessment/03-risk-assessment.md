# 03 — Risk Assessment (NIST AI RMF 1.0)

Scoring: Likelihood 1–5 × Impact 1–5. Risk appetite set with the executive sponsor: anything scoring
**≥15 must be treated before go-live**; 8–14 requires a documented, time-bound plan; ≤7 is accepted
and monitored.

## GOVERN — is anyone actually accountable?

| ID | Risk | L | I | Score |
|---|---|---|---|---|
| G-01 | No named owner for AI outcomes. The vendor points to the deployer, the recruiting team points to the tool, and no one signs. | 5 | 4 | **20** |
| G-02 | No AI use-case inventory. This system was procured through the ATS renewal and never went through a risk review. | 5 | 3 | **15** |
| G-03 | Contract has no audit rights, no model-change notification, and no indemnity for discrimination claims. | 4 | 5 | **20** |
| G-04 | Recruiters have had no training on how scores are produced or when to override them. | 5 | 3 | **15** |

**The finding that matters:** G-03 is the one people skip. If the vendor silently ships a new model
version, every bias audit and impact assessment on file describes a system that no longer exists.
Model-change notification is not a nice-to-have clause — it is what keeps the entire evidence base
valid.

## MAP — do we understand the context and who gets hurt?

| ID | Risk | L | I | Score |
|---|---|---|---|---|
| M-01 | Proxy discrimination via employment gaps, graduation year, and ZIP code — protected characteristics reconstructed from permitted features. | 5 | 5 | **25** |
| M-02 | Training data reflects the vendor's clients' historical hiring patterns, encoding their past bias into Northbridge's future decisions. | 4 | 5 | **20** |
| M-03 | Disability-related accommodation needs invisible to the model; non-linear histories read as instability. | 4 | 4 | **16** |
| M-04 | No documented job-relatedness analysis linking scored features to actual performance in warehouse and driving roles. | 5 | 4 | **20** |

**M-04 is the quiet one.** Under Title Vll, if a screen produces adverse impact, the employer must
show the screen is job-related and consistent with business necessity. Nobody at Northbridge can
currently explain why graduation year predicts forklift performance — because it does not. That is a
losing position in litigation, and it is also just a bad screen.

## MEASURE — would we even know if it were discriminating?

| ID | Risk | L | I | Score |
|---|---|---|---|---|
| MS-01 | No adverse-impact monitoring. Selection rates by protected group are not calculated at all. | 5 | 5 | **25** |
| MS-02 | Vendor bias audit is inadequate: superseded model version, race and sex reported separately rather than intersectionally, no impact ratio by role family, auditor paid by and reporting to the vendor. | 5 | 4 | **20** |
| MS-03 | No model-drift detection; scores could shift materially with no alert. | 4 | 3 | **12** |
| MS-04 | Rejection decisions are not logged with the score and feature contributions, so no rejection can be reconstructed or explained later. | 5 | 4 | **20** |

**On rejecting the vendor's audit.** An audit commissioned and paid for by the vendor, covering a
model version that is no longer in production, is not an "independent bias audit" for NYC LL144
purposes. Accepting it would have let this project proceed faster. It would also have left
Northbridge publishing an audit result it cannot stand behind — which is worse than publishing
nothing, because it is a documented misrepresentation.

## MANAGE — can we respond when something goes wrong?

| ID | Risk | L | I | Score |
|---|---|---|---|---|
| MG-01 | Auto-rejection removes human review entirely for ~4,400 candidates a year. | 5 | 5 | **25** |
| MG-02 | No candidate appeal or human-review request channel. | 4 | 4 | **16** |
| MG-03 | No kill switch — no defined trigger or authority to disable scoring mid-cycle. | 3 | 5 | **15** |
| MG-04 | No incident process for an AI-caused discriminatory outcome; the existing security IR plan does not cover it. | 4 | 4 | **16** |

## Summary

**Twelve risks scored ≥15; four at the maximum 25.** All four maximum-severity risks — M-01,
MS-01, MG-01, and by extension MS-04 — collapse into a single root cause:

> The system makes consequential decisions autonomously, and the organisation has no way to see,
> explain, or reverse them.

Remove the autonomy and add measurement, and every one of those four drops to a manageable level.
That is the whole recommendation in one sentence, and it is why the control set in
[`04-controls-and-human-oversight.md`](04-controls-and-human-oversight.md) leads with a configuration
change rather than a policy.
