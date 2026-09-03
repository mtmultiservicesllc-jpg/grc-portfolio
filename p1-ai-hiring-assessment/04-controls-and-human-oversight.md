# 04 — Control Set and What Human Oversight Has to Mean

## 4.1 Controls, in the order they should be implemented

| # | Control | Treats | Effort | Owner |
|---|---|---|---|---|
| C-01 | **Disable the auto-reject threshold.** Ranking becomes advisory; every rejection is made by a named recruiter. | MG-01, M-01 | 1 hour (config) | Talent Manager |
| C-02 | **Remove or neutralise proxy features**: graduation year, ZIP code, employment-gap length. Where the vendor cannot remove them, document the residual and monitor its effect. | M-01, M-03 | Vendor change request | Vendor + GRC |
| C-03 | **Monthly adverse-impact monitoring.** Selection rate by race, sex, and age band, per role family, applying the four-fifths rule. Any ratio below 0.80 triggers review within 5 business days. | MS-01 | 1 day to build, 2 h/month | GRC |
| C-04 | **Decision logging.** For every candidate: score, top contributing features, recruiter action, timestamp, and outcome. Retained 3 years. | MS-04, MG-02 | ATS configuration | IT + GRC |
| C-05 | **Independent bias audit** commissioned by Northbridge, not the vendor, covering the production model version, reported intersectionally and by role family. Annual. Published before NYC use. | MS-02 | 6–8 weeks, external | GRC + Legal |
| C-06 | **Contract amendment**: audit rights, model-change notification within 30 days, discrimination indemnity, data-deletion terms, right to exit on audit failure. | G-03 | Renewal cycle | Legal + Procurement |
| C-07 | **Named accountable owner** for AI hiring outcomes (Talent Manager), with the AI system entered in a use-case inventory reviewed quarterly. | G-01, G-02 | 1 week | Executive sponsor |
| C-08 | **Recruiter training + override log.** How scores are produced, what they miss, when to override, and a required free-text reason on every override. | G-04 | 3 hours + refresher | GRC |
| C-09 | **Candidate notice and human-review channel.** Notice at application (10+ business days ahead where NYC applies) and a working route to request human review. | MG-02, LL144, CO, IL | 2 weeks | Talent + Legal |
| C-10 | **Kill switch** with defined triggers (impact ratio <0.80 for two consecutive months, unnotified model change, regulatory action) and a single named authority to pull it. | MG-03 | 1 day | Talent Manager |
| C-11 | **Job-relatedness analysis** documenting why each scored feature predicts performance in these roles. Anything that fails gets removed. | M-04 | 2–3 weeks | GRC + Ops |
| C-12 | **Annual impact assessment** on the Colorado SB 24-205 template, reusable as the EU Article 26 evidence base in 2027. | Colorado, EU 2027 | 2 weeks/year | GRC |

## 4.2 What "human oversight" must actually mean

This is where most AI governance programs fail, so it is worth being blunt about it.

A recruiter reviewing a list sorted by AI score, under time pressure, with 12,000 applications a
year, is not exercising oversight. They are ratifying. The research on automation bias is
consistent: people accept algorithmic recommendations at very high rates, and the acceptance rate
rises as workload rises. Writing "a human reviews all decisions" into a policy while leaving that
setup unchanged produces a document that is true on paper and false in practice — and an auditor who
pulls the override log will find it.

Meaningful oversight requires four things:

1. **Authority** — the recruiter can reject the model's ranking without seeking approval. (EU AI Act
   Art. 26(2) requires precisely this: competence *and* authority.)
2. **Capability** — they understand what the score is built from, and what it cannot see.
3. **Friction where it counts** — a required reason field on any override, which both slows the
   reflex and creates the evidence trail.
4. **Measurement** — the override rate is monitored. **An override rate near zero is a red flag, not
   a success metric.** If recruiters never disagree with the model, there is no oversight happening,
   whatever the policy says.

That fourth point is the one I would put in front of an executive. It converts oversight from an
assertion into something you can measure and fail.

## 4.3 Framework mapping

| Control | NIST AI RMF | ISO/IEC 42001 | EU AI Act (from Dec 2027) | US law |
|---|---|---|---|---|
| C-01, C-08 | MANAGE 2.1, GOVERN 3.2 | 8.3 operational controls | Art. 26(2) human oversight | CO human review |
| C-03, C-05 | MEASURE 2.11 | 9.1 monitoring | Art. 26(5) monitoring | LL144, Title VII |
| C-04 | MEASURE 2.8, MANAGE 4.1 | 8.4 documented information | Art. 26(6) logs | CO records |
| C-06 | GOVERN 6.1 (third party) | 8.1 supplier controls | Art. 25 responsibilities | — |
| C-07, C-12 | GOVERN 1.1, MAP 1.1 | 6.1 risk, 5.3 roles | Art. 26(1) | CO impact assessment |
| C-09 | MANAGE 4.3 | 8.5 | Art. 26(7) worker notice | LL144, CO, IL |
| C-11 | MAP 3.1 | 6.1.2 | Art. 26(4) input data | Title VII business necessity |

## 4.4 Residual risk after treatment

With C-01 through C-12 implemented, the four maximum-severity risks drop as follows:

| Risk | Before | After | Rationale |
|---|---|---|---|
| MG-01 auto-rejection | 25 | 6 | Every rejection now has a named human decision-maker |
| M-01 proxy discrimination | 25 | 10 | Proxies removed or monitored; residual remains because proxies can never be fully eliminated from free-text résumés |
| MS-01 no monitoring | 25 | 5 | Monthly four-fifths testing with a defined trigger |
| MS-04 no logging | 20 | 5 | Full decision logs, 3-year retention |

**Residual risk I would accept and state openly:** proxy discrimination cannot be driven to zero.
Résumé free text carries signals of class, origin, and education that no feature removal eliminates.
The honest position is that this system is monitored, reversible, and better instrumented than the
unaided human screening it replaces — not that it is fair.
