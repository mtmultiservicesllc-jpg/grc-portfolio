# Vendor Risk in Dollars — FAIR Quantification of a Payroll SaaS Provider

**Analyst:** Moussa Touré · **Date:** September 2026
**Deliverable:** [`TPRM-FAIR-Quantification.xlsx`](TPRM-FAIR-Quantification.xlsx) — questionnaire scoring, FAIR inputs, 100,000-iteration Monte Carlo, executive summary

---

## The question that started this

The CFO asked: *"Is this payroll vendor worth the money, or should we bring it back in-house?"*

A red-amber-green vendor rating cannot answer that question. "Amber" is not an input to a budget
decision. The only honest answer is in dollars, with the uncertainty shown rather than hidden.

## Scenario

Payroll SaaS provider holding PII and bank account details for 800 employees. Contract renewal in 90
days. The security questionnaire came back at **55% — the "conditional" band**, with five material
gaps.

## What the questionnaire found

| Gap | Weight | Why it drives loss |
|---|---|---|
| No 72-hour breach notification commitment in contract | 9 | We learn about our own breach late, and our regulatory clock has already started |
| No MFA on administrative access | 9 | The single control most correlated with credential-based compromise |
| No right to audit or receive audit reports | 8 | We cannot verify any other answer on this questionnaire |
| No tested incident response plan | 8 | An untested plan is a document, not a capability |
| Subprocessor list not disclosed | 7 | Fourth-party exposure we cannot see or assess |

The questionnaire finds the gaps. It does not price them — which is why the score alone should not
decide the renewal.

## What the quantification found

| Scenario | Annualised loss expectancy | P95 (bad year) | P(loss > $1M) |
|---|---|---|---|
| **Current state** | **$724K** | $2.34M | 22% |
| **Option B — remediate contract and controls** | **$165K** | $1.04M | 6% |
| Option C — bring payroll in-house | $180K | — | — |

**Cost of Option B: $95K** (contract negotiation, MFA enforcement, IR plan development and testing,
audit rights).

**Risk reduction: $559K per year. Return on control investment: 5.9x.**

## Recommendation: Option B

Renew with remediation. Three reasons, in the order I would give them to a CFO:

1. **The remediation pays back nearly six times over in year one.** Few security investments have a
   business case this clean, and this one comes from fixing a contract and turning on MFA.
2. **In-house is not cheaper.** Option C models at $180K ALE — statistically indistinguishable from
   the remediated vendor — while costing an estimated $600K to build and nine months to deliver.
   Bringing it in-house moves the risk onto our own balance sheet without reducing it. The vendor is
   not the problem; the contract and three controls are.
3. **The gaps are contractual, not architectural.** Every one of the five findings is fixable at
   renewal, which is precisely the moment we have leverage. That leverage disappears the day we sign.

## What I would tell the board about the numbers

**Read the distribution, not the average.** The $724K mean is what to budget. The $2.34M P95 is what
to survive. A board shown only the average is unprepared for the year that goes wrong, and the year
that goes wrong is the only one anyone remembers.

**These are estimates, and I will say so.** FAIR does not produce facts; it produces a defensible
range from stated assumptions. Every input in the workbook has a written basis — the threat event
frequency comes from the vendor's two disclosed incidents in three years, the vulnerability factor
from the specific questionnaire gaps. Anyone can challenge an input and re-run the model. **That is
the point.** A heat map cannot be challenged, because it never said anything falsifiable.

**What would change the answer.** If the vendor refuses the audit rights clause, the vulnerability
factor cannot be reduced as modelled, remediated ALE rises above $300K, and Option C becomes
competitive. The recommendation is conditional on what we can actually negotiate — I would not
present it as settled before the contract conversation happens.

## Method

- **Model:** FAIR — Loss Event Frequency = Threat Event Frequency × Vulnerability; Total Loss =
  Primary Loss + (Secondary Loss Event Frequency × Secondary Loss Magnitude)
- **Distributions:** BetaPERT on minimum / most likely / maximum estimates, the standard treatment
  for expert-estimated inputs
- **Iterations:** 100,000, seeded for reproducibility — anyone can re-run and get these exact numbers
- **Inputs documented:** every factor carries a written basis in the *FAIR Inputs* sheet

```bash
python3 build_fair_model.py
```

## Files

| File | Contents |
|---|---|
| [`build_fair_model.py`](build_fair_model.py) | The model — questionnaire scoring, PERT sampling, Monte Carlo, workbook generation |
| [`TPRM-FAIR-Quantification.xlsx`](TPRM-FAIR-Quantification.xlsx) | Executive summary · FAIR inputs with basis · simulation results · questionnaire scoring |

*Scenario vendor. The FAIR method, the input documentation discipline, and the decision logic are
real practice.*
