# ISO/IEC 27001:2022 — A Statement of Applicability That Excludes Controls

**Analyst:** Moussa Touré · **Date:** September 2026
**Deliverable:** [`ISO27001-2022-Statement-of-Applicability.xlsx`](ISO27001-2022-Statement-of-Applicability.xlsx) — all 93 Annex A controls, 84 applicable, **9 excluded with documented rationale**

---

## The point of this project

Most SoAs mark all 93 controls applicable. It feels safe. It is also an admission that no risk
assessment took place — because if every control applies to every organisation regardless of what
that organisation does, the risk assessment did no work.

An auditor reading a 93-of-93 SoA asks one question: *"You have no offices. Explain A.7.1 physical
security perimeters."* The answer determines whether the ISMS is real.

This SoA excludes nine controls. Each exclusion is tied to a **factual attribute** of the
organisation, not a preference, and each becomes applicable the moment that attribute changes.

## Scenario

**Meridian Health Data, Inc.** — 60-person US SaaS company processing protected health information
for hospital customers. Fully remote since founding: no office, no data centre, no warehouse.
Production runs entirely in AWS. All engineering is done by direct employees. Pursuing ISO 27001
certification to unblock enterprise and EU deals.

**ISMS scope:** the SaaS platform processing customer PHI, its supporting AWS production
environment, and the remote workforce operating it.

## The nine exclusions

| Control | Exclusion rationale |
|---|---|
| A.7.1 Physical security perimeters | No company premises exist. AWS perimeter security inherited under the shared responsibility model, verified via A.5.23. |
| A.7.2 Physical entry | No entry points under company control. |
| A.7.3 Securing offices, rooms and facilities | No offices, rooms or facilities owned, leased or operated. |
| A.7.4 Physical security monitoring | No premises to monitor; logical monitoring covered by A.8.15 / A.8.16. |
| A.7.6 Working in secure areas | No secure areas exist; production access is logical only. |
| A.7.11 Supporting utilities | No facility requiring power, cooling or water; AWS responsibility. |
| A.7.12 Cabling security | No company-owned cabling; home networks covered by A.6.7 and A.8.1. |
| A.7.13 Equipment maintenance | No company-operated hardware; laptops leased with vendor replacement. |
| A.8.30 Outsourced development | All development by direct employees; no development contractor relationship exists. |

## The five physical controls I kept — and why that matters more

The easy version of this project excludes all fourteen A.7 controls because "we're remote." That
would be wrong, and it is exactly what an auditor probes.

| Kept control | Why it still applies to a company with no offices |
|---|---|
| A.7.5 Physical and environmental threats | Applies to the AWS regions in use; addressed through multi-AZ deployment. |
| A.7.7 Clear desk and clear screen | Applies in *home* working environments — arguably more exposed than an office, with household members and shared spaces. |
| A.7.8 Equipment siting and protection | Applies to company laptops in homes. |
| A.7.9 Security of assets off-premises | **Every** company asset is permanently off-premises in this model. This control carries more weight here than in an office-based company, not less. |
| A.7.10 Storage media | Removable media is blocked by endpoint policy; the control documents that prohibition and its exception process. |
| A.7.14 Secure disposal or re-use | Laptop return and certified wipe at offboarding. |

**The reasoning I would defend:** remote working does not delete physical risk, it relocates it into
sixty homes the company does not control. A.6.7 and the retained A.7 controls are where that risk is
managed. The exclusions cover only what genuinely does not exist.

## Inherited controls: the distinction that separates a real SoA from a template

Three of the exclusions above rest on AWS carrying the control under the shared responsibility
model. That is a legitimate basis — and it creates an obligation, not a free pass.

The obligation lives in **A.5.23 (information security for use of cloud services)** and **A.5.22
(monitoring and review of supplier services)**: Meridian reviews the AWS ISO 27001 certificate and
SOC 2 report annually and records that review as evidence. Without that, the exclusion is not
inheritance, it is abdication.

This is the sentence I would put to an auditor: *the physical controls are not absent from our ISMS,
they are provided by a supplier whose provision we verify annually and evidence in our SoA.*

## Implementation honesty

The SoA does not claim everything is implemented. Eleven applicable controls are marked **partially
implemented or planned**, with target dates:

- A.5.28 Collection of evidence — planned Q1 2027
- A.5.35 Independent review — planned Q4 2026 (external assessor; a 60-person company cannot staff an internal audit function)
- A.8.12 Data leakage prevention — planned Q1 2027
- A.8.23 Web filtering — planned Q1 2027
- Plus seven partially implemented (A.5.7, A.5.13, A.5.30, A.8.11, A.8.16, A.8.27, A.8.29)

An SoA claiming 93 of 93 implemented in a 60-person company is not credible, and a certification
auditor will find the gap faster by reading the claim than by testing the control. Declaring the gap
with an owner and a date is the stronger position.

## Judgment calls a reviewer could challenge

I would expect all three of these to come up, and I would defend them:

1. **A.5.7 threat intelligence at reduced scope.** Consuming CISA and H-ISAC advisories rather than
   running an intelligence function. Proportionate to 60 people; a challenger could argue PHI
   sensitivity warrants more.
2. **A.5.35 independent review outsourced.** Defensible for the size; a purist would want an internal
   audit programme as well.
3. **A.8.30 excluded.** The most fragile exclusion in the set, because it depends on a business
   decision that could change in a single quarter. It is flagged for review at every management
   review for exactly that reason.

---

*Scenario company. The control list, the exclusion logic, the shared-responsibility treatment and
the implementation status model are real practice.*
