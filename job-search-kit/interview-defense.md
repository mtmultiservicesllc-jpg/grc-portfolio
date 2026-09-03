# Interview Defense — The Questions That Will Be Asked

Every one of these has been chosen because it is the question a competent interviewer asks to find
out whether you actually did the work or downloaded it. The answers below are the *shape* of a good
answer. Rewrite each one in your own words — an answer you memorised sounds exactly like an answer
you memorised.

---

## On the portfolio itself

**"Are these real engagements?"**

Say it straight: no. They are constructed scenarios built on realistic system patterns, and each one
says so in writing. Then redirect to what is real: the legal analysis is current as of September
2026, the control design is what I would implement, and the judgment calls are mine and I will
defend any of them. A candidate who dresses up a lab as client work loses the room the moment one
detail does not hold.

**"Did AI write this?"**

I used AI as a drafting and research tool the same way I use a spreadsheet — and then I made every
decision in it and I can defend each one. Ask me why I excluded A.8.30 and kept A.7.9. Ask me why I
rejected the vendor's bias audit. That is where you will find out whether I understand it.

Then invite the challenge. The invitation is the answer.

---

## Project 1 — AI hiring assessment

**"Why did you say no to the auto-reject feature? The client wanted it."**

Because it converts a decision-support tool into an automated decision system, and that single
distinction is what every framework in scope keys its obligations to. Colorado attaches to
consequential decisions, Illinois prohibits discriminatory effect, Title VII does not care whether a
human or a model produced the outcome. And it was the cheapest fix available — a configuration
setting, one hour. I would rather spend my credibility on the change that costs nothing and removes
four of the highest risks than argue about documentation.

**"The EU deadline moved to December 2027. Why spend money now?"**

Because the EU deadline was never the binding one. Colorado's obligations took effect 30 June 2026,
Illinois' on 1 January 2026, NYC's have been live since 2023, and Title VII has no deadline. The
Digital Omnibus changed a filing date, not whether the system can discriminate. And the artefacts
are the same — impact assessment, human oversight, logging, bias testing. We build them once now or
twice later.

**"You rejected the vendor's bias audit. Isn't that overcautious?"**

The audit covered a superseded model version, was commissioned and paid for by the vendor, and
reported race and sex separately rather than intersectionally. NYC Local Law 144 requires an
*independent* audit published before use. Accepting it would not have been cautious or reckless — it
would have been a documented misrepresentation on the client's own website, which is worse than
publishing nothing.

**"What would change your recommendation?"**

If the vendor supplied a full training-data lineage and an independent audit on the production model
showing impact ratios above 0.80 across role families, I would reconsider the NYC hold. I would not
reconsider the auto-reject removal — that one is structural.

---

## Project 2 — ISO 27001 SoA

**"Walk me through an exclusion."**

A.7.1, physical security perimeters. The company has been fully remote since founding: no office, no
data centre, no leased space. There is no perimeter to define. Production is in AWS, where physical
perimeter security is the provider's responsibility under shared responsibility, and we verify it
annually through A.5.23 by reviewing the AWS ISO 27001 certificate and SOC 2 report. The control is
not absent from the ISMS — it is provided by a supplier whose provision we verify and evidence.

**"You excluded eight of fourteen physical controls. Why keep the other six?"**

Because remote working does not delete physical risk, it relocates it into sixty homes the company
does not control. Clear desk applies in a house with family members. Assets off-premises applies to
*every* asset we own in this model, which makes it more important here than in an office, not less.
The exclusions cover only what genuinely does not exist.

**"Which exclusion is weakest?"**

A.8.30, outsourced development. It depends on a business decision that could change in a single
quarter — the day they hire a development contractor, it becomes applicable. That is why it is
flagged for review at every management review rather than treated as settled.

---

## Project 3 — Automated access review

**"How do you know the automation actually improved the control?"**

I do not measure it by the reduction from 388 records to 89. I measure it by the retain rate. If
managers retain more than 60% of exceptions, the automation has not fixed rubber-stamping — it has
made it faster. That is the metric I would put in front of an audit committee, precisely because it
is the one that can embarrass the programme.

**"What did you deliberately leave manual?"**

The accept/revoke decision, the adequacy of compensating controls for SoD conflicts, threshold
tuning, and root-cause investigation when access survives offboarding. Automating detection does not
automate accountability. A rule cannot see business need — a dormant break-glass role is dormant by
design.

---

## Project 5 — FAIR quantification

**"These numbers are made up."**

They are estimates, and the workbook says so. FAIR does not produce facts, it produces a defensible
range from stated assumptions — and every input has a written basis you can challenge. Threat event
frequency comes from the vendor's two disclosed incidents in three years. The vulnerability factor
comes from the specific questionnaire gaps. Change an input, re-run it, get a different answer.
That is the point. A heat map cannot be challenged because it never said anything falsifiable.

**"Why not bring payroll in-house?"**

Because in-house models at $180K ALE against $165K remediated — statistically indistinguishable —
while costing an estimated $600K and nine months. It moves the risk onto our own balance sheet
without reducing it. The vendor is not the problem; the contract and three controls are.

---

## On your background

**"You have limited professional GRC experience."**

Agreed, and here is what I do have: I built and run the compliance program for my own
SAM-registered federal contracting company — policies, risk register, vendor screening, control
self-assessments with weighted scoring. I spent two years evaluating AI model outputs against
structured safety and policy rubrics, which is the human oversight layer NIST AI RMF and ISO 42001
require. And I have five worked assessments I will walk you through in detail. What I have not done
is administer an enterprise GRC platform in production, and I will not pretend otherwise.

Never apologise for the gap. State it, bound it, then move to what you bring.

**"Why is your Security+ expired?"**

Because I let the CEU cycle lapse while I was building the GRC practice, and CompTIA has no route
back except retaking the exam. It is booked for [date]. Say it in one sentence and move on. Anything
longer sounds like an excuse.

**"You're the founder of your own company. Why do you want this job?"**

Because I want to do GRC work at a scale a five-person company cannot give me, and learn from people
who have run certification audits and regulator conversations. The company continues as a
subcontracting business; this is where I want my professional depth to come from. Have this answer
ready — they will ask, and a vague answer reads as "he will leave in six months."

---

## Two questions to ask them

Good questions signal seniority faster than good answers.

1. "When your team finds a control deficiency the business does not want to fix, what happens next?"
   — tells you whether GRC has authority or is decoration.
2. "How are you approaching AI governance — are you being asked for it by customers yet, or is it
   still internal?" — shows you track the market, and their answer tells you exactly where you would
   add value.
