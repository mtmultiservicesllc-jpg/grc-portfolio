# Decision Memo — AI Résumé Screening Deployment

**To:** COO, Northbridge Logistics · **From:** GRC · **Date:** September 2026
**Decision required:** approve, modify, or reject deployment of TalentRank AI

---

## Recommendation

**Approve a 90-day pilot in US roles outside New York City, with the automatic rejection feature
switched off. Hold New York City and Ireland.**

## Why, in four sentences

The tool solves a real problem — four recruiters cannot read 12,000 applications, and today the
overflow is handled by whoever gets to the pile first, which is not fair either. The risk is not the
ranking; it is the configuration that rejects roughly 4,400 people a year with no human involvement,
which is the point at which three US laws and federal discrimination law all attach. Turning that
setting off costs one hour and removes the four highest risks we identified. What remains is a
ranking tool that helps recruiters prioritise, under measurement we can act on.

## What I need approved

| # | Item | Cost | Timing |
|---|---|---|---|
| 1 | Disable auto-rejection; ranking advisory only | Config change | Before go-live |
| 2 | Independent bias audit, commissioned by us | $15–25K | 6–8 weeks |
| 3 | Monthly adverse-impact monitoring | ~2 h/month internal | Ongoing from day 1 |
| 4 | Contract amendment: audit rights, model-change notice, indemnity | Legal time | Next renewal |
| 5 | Recruiter training and override logging | 3 hours × 5 people | Before go-live |

## What we are choosing not to do, and why

**New York City — hold.** Local Law 144 requires an independent bias audit published before use and
10 business days' candidate notice. The vendor's audit does not qualify: it covers a superseded
model version, was paid for by the vendor, and reports race and sex separately rather than
intersectionally. Using it would be a documented misrepresentation on our own website. Estimated
unblock: 8 weeks.

**Ireland — hold.** EU AI Act high-risk obligations for this category were deferred to 2 December
2027, so we are not late. But the vendor cannot yet supply the deployer documentation those
obligations require, and deploying now means building the compliance package twice. Revisit at the
vendor's next release, target Q1 2027.

## The question I expect from the board

*"The EU pushed its deadline to December 2027 — why are we spending money now?"*

Because the EU deadline is not the binding one. Colorado's obligations took effect 30 June 2026,
Illinois' on 1 January 2026, New York City's have been live since 2023, and Title VII has no
deadline at all. The EU delay changed a filing date; it did not change whether this system can
produce a discriminatory outcome. The work we do now for Colorado is the same work the EU will ask
for in December 2027 — impact assessment, human oversight, logging, bias testing. We build it once
or we build it twice.

## If we do nothing

We continue auto-rejecting ~4,400 candidates a year with no record of why, no ability to explain any
individual decision, and no monitoring that would tell us if the pattern is skewed. Exposure ranges
from LL144 penalties accruing per candidate per day to a Title VII disparate-impact claim we could
not currently defend, because we have no job-relatedness analysis for the features being scored.

The cheapest risk reduction available to us is a configuration setting. I recommend we start there.

---

**Sign-off**

| Role | Name | Decision | Date |
|---|---|---|---|
| COO (sponsor) | | ☐ Approve ☐ Modify ☐ Reject | |
| Head of Legal | | ☐ Concur ☐ Concur with conditions | |
| Talent Manager (control owner) | | ☐ Accepts ownership | |
