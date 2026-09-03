# AI Hiring System — Governance Assessment & Deployment Decision

**Analyst:** Moussa Touré · **Date:** September 2026
**Frameworks:** EU AI Act (post–Digital Omnibus) · NIST AI RMF 1.0 · ISO/IEC 42001 · NYC LL144 · Colorado SB 24-205 · Illinois HB 3773 · Title VII

---

## The decision

A logistics company wants to deploy a third-party AI résumé-screening system that ranks candidates
0–100 and **automatically rejects everyone below 40**, across 12,000 applications a year in the US
and Ireland.

**My recommendation: conditional GO — with three things removed or fixed first.**

| Scope | Decision | Why |
|---|---|---|
| Auto-rejection below a score threshold | **NO-GO** | Removes the human from a consequential decision. This single feature is what turns an advisory tool into a legal and ethical liability under Colorado SB 24-205, Illinois HB 3773, and Title VII disparate-impact doctrine. |
| US roles outside NYC (advisory ranking only) | **GO — 90-day pilot** | Acceptable residual risk once ranking is advisory, recruiters are trained, and adverse-impact monitoring runs monthly. |
| NYC roles | **HOLD** | LL144 requires an independent bias audit published *before* use, plus 10 business days' candidate notice. The vendor's audit does not qualify — see below. |
| Ireland (EU) roles | **NO-GO for now** | Annex III high-risk obligations were deferred to 2 December 2027, but the vendor cannot yet supply the Article 26 deployer documentation. Deploying now creates a rebuild in 2027 at higher cost. |

**The judgment call I would defend in a room:** the deferral of the EU high-risk deadline to December
2027 is *not* a reason to wait. Colorado's obligations landed 30 June 2026, Illinois' on 1 January
2026, NYC's have been live since 2023, and Title VII never had a deadline. The EU delay changes the
paperwork date, not the discrimination risk.

---

## What is in this repository

| File | What it contains |
|---|---|
| [`01-system-and-context.md`](01-system-and-context.md) | The system, the data, the decision it influences, and who it affects |
| [`02-regulatory-applicability.md`](02-regulatory-applicability.md) | Which laws apply, which do not, and the dates that actually bind — post–Digital Omnibus |
| [`03-risk-assessment.md`](03-risk-assessment.md) | Risk analysis structured on the four NIST AI RMF functions |
| [`04-controls-and-human-oversight.md`](04-controls-and-human-oversight.md) | The control set, and what "meaningful human oversight" has to mean to be real |
| [`05-decision-memo.md`](05-decision-memo.md) | The one-page memo an executive signs |
| [`risk-register.csv`](risk-register.csv) | 12 risks, scored, owned, with residual risk after treatment |

---

## Why this assessment looks different from most

Three deliberate choices:

1. **I say no to something.** An assessment that approves everything is not an assessment. The
   auto-reject threshold is where the real risk sits, and removing it is what makes the rest
   acceptable.
2. **I priced the delay.** The EU deferral is widely read as "we have until 2027." I treat it as a
   sequencing question — build once to the December 2027 standard, or build twice.
3. **I rejected the vendor's bias audit and said precisely why.** It covers a superseded model
   version, reports race and sex separately rather than intersectionally, and gives no
   adverse-impact ratio by role family. Accepting it would have been the easy path and the wrong one.

---

## Assumptions and limits

This is a constructed scenario built on a realistic system pattern, not a live client engagement.
The company is fictional; the legal analysis, the framework mappings, and the control design are
real and current as of September 2026. Where the law is unsettled — California's FEHA automated
decision system rules were still being finalised at the time of writing — I say so rather than
inventing certainty.
