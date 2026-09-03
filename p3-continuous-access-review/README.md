# From Quarterly Spreadsheet to Continuous Control — Privileged Access Review

**Analyst:** Moussa Touré · **Date:** September 2026
**Controls addressed:** ISO/IEC 27001:2022 A.5.15, A.5.18, A.8.2, A.8.3 · NIST SP 800-53 AC-2, AC-6(7) · SOC 2 CC6.1–CC6.3 · HIPAA §164.308(a)(4)

---

## The control before

Every quarter, someone exports 388 entitlement rows to a spreadsheet, splits it by manager, and
emails each manager their tab with the subject line "Please review by Friday."

What happens next is the same in every organisation I have seen described:

- The manager has 40 rows and eleven minutes.
- Everything is approved.
- The spreadsheet comes back signed.
- The auditor sees a signed spreadsheet and the control passes.

The control produces evidence. It does not produce security. Asking a human to attest to 40 records
they cannot meaningfully evaluate guarantees rubber-stamping — and the rubber stamp is what gets
filed as proof.

## The control after

Run the exception engine against the same three exports. It applies five rules and returns only what
a human actually needs to decide.

```
$ python3 access_review.py
Entitlements evaluated : 388
Exceptions for review  : 89 (26 critical, 63 high)
Manual review reduced by 77.1%
```

**Managers now review 89 records instead of 388.** More importantly, they review 89 records that
each come with a stated reason, a recommended action, and a severity — which is a question a human
can answer well.

### The five rules

| # | Rule | Severity | Why it fires |
|---|---|---|---|
| 1 | Orphaned account | Critical | Entitlement with no matching HR record — terminated or never onboarded |
| 2 | Access retained after termination | Critical | Still entitled N days after termination date |
| 3 | Segregation of duties conflict | Critical | Holds both sides of a conflicting pair in one system |
| 4 | Privileged access without approval | High | Privileged role with no approved, unexpired request on file |
| 5 | Dormant privileged access | High | Privileged role unused beyond the threshold (default 45 days) |
| 6 | Role inconsistent with job function | High | Production engineering role held by Sales, Marketing or Support |

SoD pairs encoded: deploy + approve deployment · create vendor + approve payment · grant IAM +
delete audit logs · modify payroll + approve payroll.

## What is deliberately still manual, and why

This is the part most automation write-ups skip, and it is the part an auditor asks about.

| Stays manual | Reason |
|---|---|
| The accept / revoke decision on every exception | Business need is context a rule cannot see. A dormant `break_glass` role may be dormant *by design* — that is the point of break-glass access. |
| SoD compensating controls | "Remove one side" is not always possible in a 60-person company. Someone must decide whether a documented compensating control is adequate, and own that decision. |
| Rule threshold tuning | The 45-day dormancy threshold is a judgment about the business, not a technical constant. It is reviewed quarterly. |
| Terminated-user root cause | The tool detects that access survived offboarding. Why the offboarding process failed is an investigation. |

**Automating the detection does not automate the accountability.** The tool decides what to look at;
a named human still decides what to do, and signs.

## Attestation form design (Google Forms)

Exceptions are pushed into a Google Form so managers respond in a structured, timestamped way rather
than by email reply.

| Field | Type | Note |
|---|---|---|
| Exception ID | Pre-filled | Links the response back to the run |
| Employee / role / system | Pre-filled | Manager does not retype anything |
| Decision | Required choice | Revoke · Retain — business need · Retain — compensating control |
| Justification | Required free text, min 20 chars | **Required on "Retain" only.** Friction is placed exactly where the risky answer is |
| Compensating control description | Conditional | Shown only if "Retain — compensating control" |
| Manager attestation | Required checkbox | "I confirm this access is necessary for this person's current role" |

Responses land in Sheets, feed the metrics tab, and become the audit evidence. Retention: 3 years.

**The design choice worth defending:** justification is mandatory only for *retain*, not for
*revoke*. Revoking is the safe default and should be frictionless; retaining is the decision that
creates risk and should cost thirty seconds of writing. Putting equal friction on both encourages
managers to pick whichever is faster, which is usually retain.

## Metrics that show whether the control is working

| Metric | Target | What a bad number means |
|---|---|---|
| Exceptions per run | Downward trend | Flat means findings are being retained, not fixed |
| **Retain rate** | **< 40%** | Above 60% means managers are rubber-stamping again, in a new format |
| Mean time to revoke (critical) | < 5 business days | Detection without action is not a control |
| Orphaned accounts | 0 | Any non-zero means offboarding is broken upstream |
| Repeat exceptions | Downward | The same finding recurring means the root cause was never addressed |

The retain rate is the honest one. If it climbs above 60%, the automation has not fixed the
rubber-stamp problem — it has made it faster. That is the metric I would report to the audit
committee, because it is the one that can embarrass the programme.

## Files

| File | Contents |
|---|---|
| [`access_review.py`](access_review.py) | The exception engine — runnable, no dependencies beyond the standard library |
| `sample-data/entitlements.csv` | 388 entitlements across 5 systems (synthetic) |
| `sample-data/hr_roster.csv` | 60 employees, 3 terminated (synthetic) |
| `sample-data/approvals.csv` | Approved privileged access requests (synthetic) |
| `output/exceptions.csv` | 89 exceptions, sorted by severity, with owner and recommended action |
| `output/metrics.csv` | Control health metrics for the run |

```bash
python3 access_review.py --dormant-days 45
```

*Synthetic data. The rule logic, the manual/automated boundary, and the metric design are real
practice.*
