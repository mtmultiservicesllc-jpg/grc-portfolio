# Risk Acceptance — Legacy Claims Database on Unsupported Database Version

**Risk ID:** R-2026-041 · **Requested by:** VP Operations · **Prepared by:** GRC
**Decision authority:** Chief Operating Officer (per risk policy: acceptances above $250K annualised exposure)
**Review date:** 31 March 2027 — this acceptance expires on that date whether or not anyone remembers

---

## What we are being asked to accept

The claims processing database runs on a database version that went end-of-support in June 2026. It
no longer receives security patches. It holds 340,000 customer claims records including names, dates
of birth, and bank account details for reimbursements.

Migration is scheduled for Q2 2027. The request is to run unpatched for approximately nine months.

## Why we cannot simply fix it now

The application layer was written against features removed in the supported version. Migrating
requires rewriting the reimbursement calculation module, which is the same module Finance depends on
for month-end close. Engineering estimates 14 weeks with two engineers who are currently committed to
the customer portal rebuild that the Board approved in July.

This is a real constraint, not an excuse. Pulling those engineers moves the portal launch past the
renewal date of our three largest contracts.

## What could go wrong, in plain terms

An unpatched database is not dangerous because it is old. It is dangerous because the vulnerabilities
found in it after June 2026 are published, and no fix will ever be issued. The window between
disclosure and exploitation for database software of this class is typically measured in weeks.

If that happens here, the realistic outcome is unauthorised access to 340,000 records containing
bank details. That triggers state breach notification in every state where we hold customers, likely
regulator contact, and customer notification during the same quarter as our contract renewals.

**Estimated exposure if it happens:** $1.8M–$4.2M (notification, credit monitoring, legal, regulatory
response, customer churn). **Estimated likelihood over nine months:** 12–18%, based on the exposure
profile below.

**Annualised loss expectancy: roughly $410K.** The cost of accelerating migration is roughly $340K in
delayed portal revenue plus two engineers for 14 weeks.

These numbers are close enough that this is a genuine business judgment, not a compliance formality.
That is exactly why it needs your signature rather than mine.

## What reduces the risk while we wait

These are conditions of the acceptance, not suggestions. If any of them is not in place by the date
shown, the acceptance is void and the risk returns to the register as untreated.

| # | Compensating control | Owner | In place by |
|---|---|---|---|
| 1 | Database removed from any internet-reachable path; access only from the application subnet | Head of Infrastructure | 30 September 2026 |
| 2 | Database-level activity monitoring with alerting on bulk reads and schema changes | Security Engineering | 15 October 2026 |
| 3 | Weekly review of published vulnerabilities for this version, with a named reviewer | GRC | Immediately, weekly |
| 4 | Encryption at rest verified; bank account fields tokenised in all non-production copies | Engineering | 31 October 2026 |
| 5 | Tested restore of this database, documented, quarterly | Infrastructure | 30 November 2026 |
| 6 | Incident runbook written specifically for compromise of this system | Security + GRC | 31 October 2026 |

With all six in place, likelihood drops to an estimated 5–7% and the residual annualised exposure to
roughly $180K.

## What would make us stop and reverse this decision

Any one of these ends the acceptance immediately and triggers emergency migration:

- A remotely exploitable vulnerability with public exploit code is published for this version
- Monitoring detects bulk read activity outside the application's normal pattern
- A customer contract or regulator requires supported software as an explicit condition
- The Q2 2027 migration date slips

## What we are giving up by accepting

Honest accounting, because a risk acceptance that only lists benefits is a sales document:

- We will fail this question in any customer security questionnaire that asks about supported
  software, and we will have to disclose it in the next SOC 2 examination as a known deficiency.
- If a breach happens, "we knew and accepted it" is a documented fact. That is the correct way to
  make this decision, and it is also the fact that appears in litigation. Accepting a risk knowingly
  is defensible; the memo is what makes it defensible, and it cuts both ways.
- The six compensating controls consume roughly 0.3 FTE for nine months.

## Recommendation

**Accept, with all six compensating controls as binding conditions and a hard expiry of 31 March 2027.**

The financial case is close to even, and the deciding factor is reversibility: the compensating
controls are cheap, fast, and independently valuable, and the trigger conditions give us a defined
way out. What I would not accept is this risk *without* the conditions — that version of the request
is a $410K exposure with no visibility and no exit.

---

| Role | Name | Decision | Date |
|---|---|---|---|
| Chief Operating Officer (accepting) | | ☐ Accept ☐ Accept with changes ☐ Reject | |
| VP Operations (requesting) | | ☐ Accepts control ownership | |
| GRC (preparing) | | Recommends accept with conditions | |

*Acceptance recorded as R-2026-041 in the risk register. Reviewed at each quarterly risk committee
until closed or expired.*
