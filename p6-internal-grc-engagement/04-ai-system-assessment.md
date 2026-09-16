# 04 — AI System Governance Assessment

**System:** AI-assisted licensure exam preparation platform (direct-to-consumer)
**Provider:** Northgate Services LLC · **Assessor:** Moussa Touré — first-party
**Frameworks:** EU AI Act (post–Digital Omnibus) · NIST AI RMF 1.0 · ISO/IEC 42001
**September 2026**

---

## The headline

**Not a high-risk AI system under EU AI Act Annex III today — and it becomes one the day an
educational institution deploys it to evaluate its students.** The regulatory position is
comfortable. The real risk is somewhere else, and it is not comfortable at all:

> An AI that confidently produces a wrong clinical rationale is teaching a future practitioner
> something that can hurt a patient at the bedside.

That is the finding this assessment is built around. Everything else is secondary.

---

## 1. System description

| Attribute | Value |
|---|---|
| Purpose | Practice questions, explanations and readiness feedback for licensure candidates |
| Users | Individual students, direct to consumer |
| Deployed by institutions? | **No.** This single fact decides the classification |
| AI role | Question and rationale generation; adaptive sequencing; readiness estimate |
| Model | Third-party LLM API |
| Personal data | Account, email, answer history, performance by topic |
| Outputs that influence a person | Readiness estimate, topic recommendations, explanations of professional reasoning |

The classification, the controls and the honest risk picture all move depending on whether the AI
**generates** professional content or only **sequences** pre-written content. Generation is a
materially different risk profile, and this system generates.

---

## 2. EU AI Act classification

**Provider status:** Northgate is the **provider** — the system is placed on the market under its
own name.

**Annex III point 3 — education and vocational training** covers AI used to determine admission,
evaluate learning outcomes including to steer the learning process, assess the appropriate level of
education, or monitor prohibited behaviour during tests.

**Analysis.** Those points are framed around use *in education and vocational training
institutions*. A direct-to-consumer self-study tool does not determine admission, does not issue an
outcome any institution relies on, and does not proctor. A readiness estimate the learner uses to
decide when to book their own exam is self-directed, not an institutional determination.

**Conclusion: not Annex III high-risk in the current B2C configuration.**

**The condition that flips it.** The moment an institution licenses the platform to assess its
students — to steer their learning, gate progression, or predict who may sit the exam — point 3(b)
applies and the system becomes high-risk. Full Annex III obligations arrive **2 December 2027**
under the Digital Omnibus deferral.

This matters commercially, not only legally: **B2B expansion into institutions is a classification
change, not just a new customer segment.** Price and plan for it now.

**What applies today: Article 50 transparency**, in force since 2 August 2026 — users must be
informed they are interacting with an AI system, and AI-generated content must be marked.

---

## 3. Risk analysis (NIST AI RMF)

Likelihood × Impact, 1–5. Treat above 15 before scaling.

### MAP — what can this system actually do to someone?

| ID | Risk | L | I | Score |
|---|---|---|---|---|
| N-01 | **Hallucinated professional content.** A generated rationale states a wrong dose, contraindication or priority sequence. The learner memorises it and applies it in practice. | 4 | 5 | **20** |
| N-02 | **Outdated guidance.** Standards change; a model trained on older material teaches superseded protocol as current. | 4 | 4 | **16** |
| N-03 | **Miscalibrated readiness score.** A learner books the exam on a confident prediction and fails — a real fee and months lost, on the system's advice. | 3 | 4 | **12** |
| N-04 | **Differential performance.** Explanations pitched at native-English reading level disadvantage internationally educated candidates, a large share of this population. | 3 | 4 | **12** |
| N-05 | **Fabricated citations.** The model attributes guidance to a source that does not say it — worse than no citation, because it manufactures false confidence. | 3 | 4 | **12** |

**N-01 is the whole assessment.** Every other risk here is ordinary product risk. This one has a
patient at the end of it. A preparation tool sits upstream of professional practice, which makes
**content quality a safety control, not a quality-of-service metric.**

### MEASURE — would anyone know?

| ID | Risk | L | I | Score |
|---|---|---|---|---|
| N-06 | No measured factual accuracy rate for generated content | 5 | 4 | **20** |
| N-07 | No user route to flag a wrong answer or rationale | 4 | 4 | **16** |
| N-08 | Model version not pinned — provider updates silently change behaviour | 4 | 3 | **12** |
| N-09 | No log linking a shown explanation to the prompt and model version that produced it | 4 | 3 | **12** |

### GOVERN / MANAGE

| ID | Risk | L | I | Score |
|---|---|---|---|---|
| N-10 | No subject-matter expert reviews generated content | 4 | 5 | **20** |
| N-11 | No stated position on whether user data trains the provider's models | 4 | 3 | **12** |
| N-12 | No incident path for "the product taught something dangerous" | 3 | 4 | **12** |
| N-13 | No spend cap on the model API — a leaked key is an unbounded bill | 3 | 4 | **12** |

---

## 4. Controls

| # | Control | Treats | Effort |
|---|---|---|---|
| C-01 | **Qualified practitioner review before publication.** No AI-generated professional rationale reaches a learner unreviewed. Start with highest-traffic topics; expand by usage. | N-01, N-10 | Ongoing, paid reviewer |
| C-02 | **Pin the model version** and re-validate a sample of outputs on every provider update. | N-08 | 1 hour, plus per update |
| C-03 | **"Report this question" on every item**, routed to a review queue with a turnaround target. Track flag rate per topic — a spike is the earliest safety signal available. | N-07, N-01 | 1 day to build |
| C-04 | **Accuracy benchmark.** A fixed set of items with verified answers, re-run monthly. Publish the rate internally; treat a drop as an incident. | N-06 | 2 days to build |
| C-05 | **Ground generation in an approved source set** rather than open generation; cite the source and never let the model invent one. | N-02, N-05 | Retrieval work |
| C-06 | **Calibrate the readiness score** against actual outcomes; state the confidence interval instead of a bare number. | N-03 | Ongoing |
| C-07 | **Plain-language pass** on explanations; test comprehension with internationally educated candidates. | N-04 | Content work |
| C-08 | **Prompt and output logging** with model version, defined retention. | N-09 | Configuration |
| C-09 | **Provider data-use position confirmed and published** in the privacy notice; disable training on customer data where offered. | N-11 | 1 hour |
| C-10 | **Spend caps and usage alerts** on every AI provider account. | N-13 | 15 minutes |
| C-11 | **Article 50 disclosure** in the interface: explanations are AI-generated and reviewed, and are not a substitute for an instructor. | Legal | 1 hour |
| C-12 | **Content incident procedure**: from "a user reports dangerous guidance" to removal, correction, and notification of affected learners. | N-12 | 1 day |

---

## 5. Decision

**Continue operating, with C-03, C-10 and C-11 implemented this month, and C-01 begun before any
paid marketing push.**

The reasoning, as I would defend it:

- **The regulatory position is not the binding constraint — content accuracy is.** Scaling user
  numbers before C-01 multiplies exposure to N-01 linearly, and N-01 is the risk with a patient at
  the end of it.
- C-03 and C-10 are hours of work and remove real exposure immediately. There is no argument for
  deferring them.
- **C-01 costs real money** — a qualified reviewer is not free — and that is precisely why it is
  the control most likely to be quietly skipped. Naming it here with a trigger ("before any paid
  marketing push") is how it survives contact with the budget.

**What would change this decision:** any move toward institutional deployment. That flips the EU AI
Act classification to high-risk with a December 2027 obligation date, and raises the consequence of
every risk in section 3 — because an institution's students cannot choose a different tool.

---

## 6. Declared limitations

**First-party assessment.** The assessor is the organisation's principal and the system's developer.
This is not independent review, and it does not satisfy any requirement for an independent audit.

Its purpose is to establish a baseline and a control roadmap for a system the organisation operates,
and to be honest about where the real risk sits. It should not be presented to a customer or a
regulator as independent assurance.
