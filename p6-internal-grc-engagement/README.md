# Internal GRC Engagement — Cloud-Hosted Small Business

**Analyst:** Moussa Touré · September 2026
**Scope:** ISO/IEC 27001:2022 assessment, AI system governance review, evidence programme
**Subject:** Northgate Services LLC — a SAM-registered federal and state contractor operating a small portfolio of hosted web applications

---

## What this is, stated plainly

This is a **first-party internal engagement, published in genericized form.**

The company, product and infrastructure names are replaced. The scope, the risk profile, the
control decisions, the exclusions, the evidence design and the reasoning are real — they come from
an engagement I ran end to end on an organisation of exactly this shape.

**Why it is genericized, and not anonymised badly:** a real risk register is a list of
**unremediated weaknesses** attached to a named company. Publishing that hands an attacker a map
and hands a competitor a brief. What can be published is the **method** — which is also the only
part a hiring manager is actually assessing.

If that sounds like an excuse, it is the same judgement applied here as in every other case in this
portfolio: publish the reasoning, never the exposure.

---

## The organisation

| Attribute | Value |
|---|---|
| Type | Multiservice subcontractor, federal and state registered |
| Headcount | Founder plus engaged subcontractors |
| Premises | None — fully remote |
| Technology | Hosted web applications on a serverless platform; source control, productivity suite, managed database, AI model APIs |
| Data held | Application user accounts, contact submissions, business and contracting records |
| Certifications | None at engagement start |

This shape is common and under-served: a company small enough to have no security function, but
holding other people's data and bidding for work where customers will eventually send a security
questionnaire.

---

## What was produced

| File | What it is |
|---|---|
| [`01-scope-and-assets.md`](01-scope-and-assets.md) | ISMS scope statement, application inventory, supporting-service inventory, data map, dependency analysis |
| [`02-risk-register.xlsx`](02-risk-register.xlsx) | 22 risks, scored, owned, with treatment and target |
| [`03-statement-of-applicability.xlsx`](03-statement-of-applicability.xlsx) | All 93 Annex A controls — 82 applicable, **11 excluded with documented rationale** |
| [`04-ai-system-assessment.md`](04-ai-system-assessment.md) | EU AI Act and NIST AI RMF assessment of the company's own AI product |
| [`05-evidence-procedure.md`](05-evidence-procedure.md) | How evidence is captured, named, stored and what disqualifies it |
| [`06-walkthrough-interview-guide.md`](06-walkthrough-interview-guide.md) | The questions, by domain, with red flags |
| [`07-control-test-log.csv`](07-control-test-log.csv) | 24 controls: what must be true, what evidence proves it, frequency |
| [`data/`](data/) | Three-table model — risks, controls, and the bridge — for the reporting layer |

---

## The four decisions worth defending

**1. A narrow scope, deliberately.**
The ISMS covers the hosted applications, their user data, and the cloud services that run them.
It excludes field operations of the subcontracting business. A broad scope nobody maintains is
worth less than a narrow one that is genuinely operated — and certification auditors say exactly
that.

**2. Eleven exclusions from Annex A, each tied to a fact.**
No premises, no employees, no owned network, no outsourced development. Each exclusion names the
fact it rests on and becomes applicable the moment that fact changes. Reviewed at every management
review, not treated as settled.

**3. The dependency analysis, not the asset list, drove the priorities.**
The highest-severity finding was not a missing control on a critical system. It was the path:
**domain registrar → email → password resets on everything else.** The registrar was the
least-protected account in the estate and the most catastrophic to lose. An asset inventory alone
would not have surfaced that; mapping the dependencies did.

**4. The AI product was assessed as not high-risk — with the condition that flips it.**
Direct-to-consumer self-study is not an institutional assessment under EU AI Act Annex III(3).
The day a school licenses it to evaluate its students, it becomes high-risk with a December 2027
obligation date. That is a commercial constraint on the product roadmap, not just a legal note.

---

## The finding that mattered most

Not a control gap. A measurement gap:

> **Most controls in the Statement of Applicability are marked "Not started."**

That is the correct state for an ISMS in its first month, and recording it honestly is what makes
the document usable. An SoA claiming 93 of 93 implemented in a company of this size is the fastest
way to lose an auditor's trust — and the temptation to write it is strongest when you are assessing
your own organisation.

The declared conflict of interest appears in the engagement documents for the same reason:

> *This assessment was performed by the organisation's own principal. It is a first-party
> assessment and does not substitute for independent audit.*

That sentence costs nothing and is the first thing a certification auditor looks for.

---

## Method

Risk identification used a fixed six-question set applied to every service in scope:

1. Who can access it, and how is that access protected?
2. What happens if control of it is lost?
3. What happens if its contents leak?
4. How would anyone know something had gone wrong?
5. Who else has access, and under what contract?
6. What breaks if it disappears tomorrow?

Applied across the estate, this produces the register. The skill is not memorising a list of
risks — it is knowing which questions generate the list.

Scoring is likelihood × impact on a 1–5 scale, with treatment required above 15. **Residual scores
are an estimate derived from a documented reduction assumption, not a re-score after testing** —
stated as a limitation rather than presented as measurement.

---

*Genericized from a real first-party engagement. Frameworks, control decisions, exclusion logic and
evidence design are as executed.*
