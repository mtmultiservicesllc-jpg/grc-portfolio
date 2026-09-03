# 02 — Regulatory Applicability: What Actually Binds, and When

Most published guidance on this topic is out of date. The EU timeline moved in 2026, and analyses
written before then describe obligations on a schedule that no longer exists. Dates below are
current as of September 2026 and each one is sourced.

## 2.1 EU AI Act — high-risk, but not yet on the clock

**Classification.** AI intended to be used for recruitment or selection — in particular to filter
applications and evaluate candidates — falls under **Annex III, point 4(a)**: high-risk. Northbridge
is a **deployer**, not a provider; the vendor is the provider.

**The Digital Omnibus changed the date.** Obligations for standalone Annex III high-risk systems
were deferred from 2 August 2026 to **2 December 2027**. Annex I embedded-product AI moved to
2 August 2028.

**What did NOT move.** Article 50 transparency obligations applied from **2 August 2026** and were
not deferred — AI-interaction disclosure, synthetic content marking, deepfake labelling. Generative
systems already on the market before that date had until **2 December 2026** for machine-readable
marking. Prohibited practices have been enforceable since 2 February 2025.

**What this means here.** Northbridge's Dublin operation will be in scope of the full Article 26
deployer obligations from December 2027: human oversight by competent, authorised staff; input data
relevance; log retention; worker notification before putting the system into service; and
cooperation with authorities. Today, only the Article 50 transparency duty bites — and only for the
candidate-facing chatbot the ATS uses, not the ranking model itself.

**My reading, stated plainly:** the deferral buys sequencing time, not a pass. Fifteen months is
roughly one procurement cycle plus one bias-audit cycle. A company that starts in December 2027
starts late.

## 2.2 United States — already in force

| Law | Effective | What it requires | Applies here? |
|---|---|---|---|
| **NYC Local Law 144** | July 2023 | Annual **independent** bias audit by a third party; results published on the employer's site for 6+ months; candidate notice ≥10 business days before use; alternative process where reasonable | **Yes** — for NYC-based roles. Penalties $500 first violation, up to $1,500 per subsequent violation, counted per candidate per day in practice |
| **Colorado SB 24-205** | 30 June 2026 | Annual impact assessments for consequential employment decisions; risk management program aligned to **NIST AI RMF or ISO/IEC 42001**; notice to candidates before an adverse AI-driven decision; human review rights; public disclosure. Exemption below 50 employees | **Yes** if Northbridge hires into Colorado — and the alignment clause is why the NIST AI RMF mapping in this repo is not academic |
| **Illinois HB 3773** (amends the Illinois Human Rights Act) | 1 January 2026 | Prohibits AI use that produces a discriminatory effect on protected classes in recruitment and hiring; prohibits ZIP code as a proxy; requires notice of AI use | **Yes** if hiring in Illinois. The explicit ZIP-code prohibition maps directly to a feature this model uses |
| **Illinois AIVIA** (820 ILCS 42) | 2020 | Notice, explanation, consent, deletion on request for AI video-interview analysis | Not currently — no video analysis in scope |
| **Title VII / ADEA / ADA** (federal) | Long-standing | Disparate-impact liability regardless of intent or mechanism; the **four-fifths rule** is the conventional screening test for adverse impact | **Yes — everywhere, always.** No deadline, no grace period, no exemption |
| **California FEHA automated-decision rules** | Rules finalised through 2026; opt-out provisions | Treats automated decision systems as covered employment practices | Monitor — confirm status before any California deployment |

## 2.3 The sequencing conclusion

Laying the dates on one line makes the answer obvious:

```
Jan 2026        Jun 2026        Aug 2026         Dec 2027
Illinois        Colorado        EU Art. 50       EU Annex III
HB 3773         SB 24-205       transparency     high-risk
   |               |                |                |
   +---------------+----------------+----------------+
                   ALREADY BINDING          <-- deferred, not cancelled
```

Three US regimes are already live. The EU obligation arrives in December 2027 and demands the same
underlying artefacts — impact assessment, human oversight, logging, bias testing. Building those
artefacts once, now, to the December 2027 standard satisfies the US obligations today and the EU
obligation on arrival.

**Recommendation R-01:** adopt NIST AI RMF as the single control backbone. Colorado names it
explicitly, ISO/IEC 42001 maps to it cleanly, and EU Article 26 obligations sit on top of it without
rework. One framework, four jurisdictions.

---

**Sources**

- [EU AI Act August 2026: What Applies After the Digital Omnibus — Certivo](https://www.certivo.com/blog-details/eu-ai-act-august-2026-what-applies-after-the-digital-omnibus)
- [EU AI Act Omnibus Agreement — Postponed High-Risk Deadlines — Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)
- [EU AI Act's High-Risk Deadline: Deferred, Not Cancelled — Cloud Security Alliance](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-high-risk-deadline-omnibus-20260/)
- [AI Hiring Laws by State 2026 — NYC bias audits, Illinois, Colorado SB 205](https://www.ailawsbystate.com/blog/ai-hiring-laws-by-state-compliance-map)
- [Colorado Postpones Implementation as Illinois Disclosure Law Takes Effect — Seyfarth Shaw](https://www.seyfarth.com/news-insights/artificial-intelligence-legal-roundup-colorado-postpones-implementation-of-ai-law-as-california-finalizes-new-employment-discrimination-regulations-and-illinois-disclosure-law-set-to-take-effect.html)
