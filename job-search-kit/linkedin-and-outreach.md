# LinkedIn Posts and Outreach Templates

Everything here is written to be edited. Post it exactly as-is and it will read like everyone else's
AI-assisted content. Change the sentences that do not sound like you — especially the openings.

---

## LinkedIn headline and About

**Headline** (this is what recruiters search):
> GRC & IT Audit Analyst | AI Governance (NIST AI RMF, ISO/IEC 42001) | ISO 27001 · SOC 2 · NIST 800-171 | Bilingual EN/FR

**About** — first two lines matter most, the rest is behind "see more":

> I build compliance programs for organisations that do not have one yet, and I evaluate AI systems
> for the risks nobody wrote a control for.
>
> Two years evaluating AI model outputs against structured safety and policy rubrics gave me
> something most GRC practitioners are still reading about: direct experience of the human oversight
> layer that NIST AI RMF and ISO/IEC 42001 require.
>
> I run the compliance program for a SAM-registered federal and state contractor — policies, risk
> register, vendor screening, control self-assessments with weighted scoring — so I understand the
> contractor side of NIST SP 800-171 and CMMC from the inside, not from a slide deck.
>
> Frameworks I work in: ISO/IEC 27001:2022, NIST CSF 2.0, NIST SP 800-53 and 800-171, SOC 2, HIPAA,
> PCI DSS, SOX 404, NIST AI RMF, ISO/IEC 42001.
>
> Portfolio of worked assessments: [link]

---

## Post 1 — the AI Act deadline (publish this one first)

> Most GRC teams still have "2 August 2026" written in their AI Act plan.
>
> That date moved.
>
> The Digital Omnibus deferred high-risk obligations for Annex III standalone systems — including AI
> used in recruitment and employment — to **2 December 2027**. Annex I embedded product AI went to
> August 2028.
>
> What did NOT move: Article 50 transparency obligations applied from 2 August 2026. Chatbot
> disclosure, synthetic content marking, deepfake labelling. Those are live now.
>
> Here is where I think teams will get this wrong. The deferral is being read as breathing room. For
> a US company it changes almost nothing, because the binding dates were never European:
>
> · Illinois HB 3773 — 1 January 2026
> · Colorado SB 24-205 — 30 June 2026
> · NYC Local Law 144 — since 2023
> · Title VII — no deadline, ever
>
> The EU moved a filing date. It did not move the risk of a discriminatory outcome.
>
> I worked through what this means for a company running AI résumé screening across US and EU
> operations — classification, controls, and a go/no-go recommendation. Link in comments.
>
> If you have an Annex III system in scope: has your plan been updated since the omnibus, or is it
> still on the old timeline?

---

## Post 2 — the SoA that excludes controls

> I wrote an ISO 27001 Statement of Applicability that excludes 9 of the 93 Annex A controls.
>
> Most SoAs mark all 93 applicable. It feels safe. It is also an admission that no risk assessment
> happened — because if every control applies to every organisation regardless of what that
> organisation does, the risk assessment did no work.
>
> The company in this scenario has no offices. Fully remote since founding. So A.7.1 physical
> security perimeters is excluded — there is no perimeter to define.
>
> But I kept six of the fourteen physical controls, and that is the part worth arguing about.
>
> Clear desk and clear screen still applies, in sixty homes with family members and shared spaces.
> Security of assets off-premises applies to *every* asset the company owns in this model — which
> makes it more important here than in an office, not less.
>
> Remote working does not delete physical risk. It relocates it somewhere the company does not
> control.
>
> The exclusion I am least comfortable with: A.8.30 outsourced development. It rests on a business
> decision that could change in one quarter. Flagged for review at every management review for
> exactly that reason.
>
> Full SoA with rationale for all 93: [link]

---

## Post 3 — the access review metric

> "We reduced manual access review from 388 records to 89."
>
> That is not the metric I would report.
>
> Here is the one I would: **the retain rate.**
>
> The old control was a quarterly spreadsheet emailed to managers with "please review by Friday."
> Forty rows, eleven minutes, everything approved, spreadsheet returns signed. The auditor sees a
> signed spreadsheet and the control passes. It produced evidence, not security.
>
> I automated the detection — orphaned accounts, access after termination, SoD conflicts, dormant
> privileged roles, privileged access with no approval. 77% fewer records for a human to look at.
>
> But if managers retain more than 60% of the exceptions, I have not fixed rubber-stamping. I have
> made it faster.
>
> That is why the retain rate goes to the audit committee, not the reduction percentage. The
> reduction number flatters the project. The retain rate can embarrass it.
>
> Pick the metric that can embarrass you. That is the one that is measuring something.

---

## Post 4 — FAIR

> A CFO asked me whether a payroll vendor was worth keeping.
>
> The vendor questionnaire came back "amber."
>
> "Amber" is not an input to a budget decision.
>
> So I quantified it. FAIR model, 100,000-iteration Monte Carlo, every input documented with its
> basis:
>
> · Current state: $724K annualised loss expectancy, $2.34M at P95
> · With contract and control remediation: $165K, at a cost of $95K
> · Bring it in-house: $180K — and a $600K build
>
> In-house does not reduce the risk. It moves it onto our own balance sheet at a cost of $600K and
> nine months. The vendor was never the problem. The contract and three controls were.
>
> The objection I get every time: "these numbers are made up."
>
> They are estimates, and the model says so. Every input has a written basis you can challenge —
> change it, re-run it, get a different answer. That is the point. A heat map cannot be challenged,
> because it never said anything falsifiable.
>
> Model and workbook: [link]

---

## Outreach — hiring manager (LinkedIn DM or email)

Keep it under 120 words. Nobody reads more from a stranger.

> Subject: GRC analyst — AI governance, with worked examples
>
> Hi [Name],
>
> I saw [company] is hiring a [role]. Rather than send a résumé into the pile, here is a piece of
> work: an EU AI Act and NIST AI RMF assessment of an AI hiring system, with a go/no-go
> recommendation — including why I rejected the vendor's bias audit. [link]
>
> Background: I run the compliance program for a SAM-registered federal contractor, and spent two
> years evaluating AI model outputs against safety and policy rubrics — the human oversight layer AI
> RMF and ISO 42001 ask for.
>
> If it is useful, I would welcome fifteen minutes. If the timing is wrong, no reply needed.
>
> Moussa Touré

---

## Outreach — CPA firms doing federal audits

For GRF CPAs & Advisors, Williams Adley, and their peers. Lead with the contractor angle, because
that is what they do not have in-house.

> Subject: IT audit — contractor-side perspective on 800-171 and CMMC
>
> Hi [Name],
>
> I am a GRC analyst moving toward IT audit, and I have something most junior candidates do not: I
> run a SAM-registered, DBE-certified subcontracting company, so I have lived the compliance burden
> your federal audit clients carry — SAM, UEI, flow-down clauses, 800-171 self-assessment.
>
> I have a portfolio of worked assessments — ISO 27001 SoA, AI Act evaluation, FAIR vendor
> quantification: [link]
>
> Would you be open to a short conversation about junior IT audit roles, or what you look for in
> them?
>
> Moussa Touré · [phone]

---

## Posting rules

- One post a week. Consistency beats volume.
- Put the link in the **first comment**, not the post body — reach is throttled on posts with links.
- End on a question. Comments are what carry a post to people outside your network.
- Reply to every comment within a few hours.
- Never post about looking for work in the same post as the technical content. Let the work do it.
