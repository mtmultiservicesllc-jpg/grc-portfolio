# 01 — System, Context, and Affected Persons

## 1.1 The organisation

**Northbridge Logistics** (scenario company) — regional third-party logistics provider.

| Attribute | Value |
|---|---|
| Headcount | 800 (US), 120 (Dublin, Ireland) |
| Annual applications received | ~12,000 |
| Roles screened by the system | Warehouse associate, forklift operator, CDL driver, dispatch coordinator |
| Recruiting team | 4 recruiters, 1 talent manager |
| Existing certifications | SOC 2 Type II (customer-driven), no ISMS certification |

The recruiting team is the operational reason this project exists: four people cannot read 12,000
résumés. That pressure is real, and an assessment that ignores it will be ignored in return.

## 1.2 The system

**TalentRank AI** (scenario vendor product) — SaaS résumé screening and ranking.

| Attribute | Value |
|---|---|
| Provider | Third-party SaaS vendor, US-based |
| Deployment | Integrated into the ATS via API |
| Input | Résumé text, application form fields, work-history dates |
| Model | Vendor-described "transformer-based ranking model" fine-tuned on the vendor's cross-client hiring outcome data |
| Output | Score 0–100 plus a ranked candidate list and three "match rationale" bullet points |
| Configured behaviour | Candidates scoring **below 40 are auto-rejected** with a templated email; 40–70 go to a review queue; above 70 surface at the top of the recruiter list |
| Human involvement today | None below 40. Recruiters see only the 40+ queue, ordered by score. |
| Volume | ~12,000 candidates/year; at current distribution, roughly 4,400 auto-rejected without human review |

## 1.3 What the system actually decides

This is the question that determines everything downstream, so it gets its own section.

The vendor's language is "decision support." The configuration says otherwise. A candidate scoring
39 is rejected, emailed, and never seen by a person. For that candidate the system is not support —
it **is** the decision. Every framework in scope keys its obligations to exactly this distinction:

- **EU AI Act Art. 26(2)** — deployer must assign human oversight to people with the competence and
  *authority* to act on it. There is no oversight of an outcome nobody sees.
- **Colorado SB 24-205** — obligations attach to a "consequential decision" in employment; an
  automated rejection is consequential by any reading.
- **Title VII** — liability follows the effect on protected groups, and is indifferent to whether a
  human or a model produced it.

**Finding F-01:** the auto-reject threshold converts a decision-support tool into an automated
decision system. This is the single highest-leverage change available, and it is a configuration
setting, not an engineering project.

## 1.4 Data used, and the proxy problem

| Data element | Discrimination risk | Note |
|---|---|---|
| Employment gap length | **High** | Correlates with caregiving (sex), disability, and incarceration history |
| Graduation year | **High** | A direct proxy for age (ADEA) |
| Name | **High** | Proxy for race and national origin; well-documented callback effects |
| ZIP code | **High** | Proxy for race and socioeconomic status in US metros |
| Résumé formatting / parsing quality | **Medium** | Penalises non-native English speakers and applicants using mobile-only tools |
| Prior employer names | **Medium** | Proxy for prestige and network access, not capability |
| Certifications (CDL, forklift) | **Low** | Genuinely job-related and defensible |

The model is fine-tuned on **the vendor's historical hiring outcomes across its client base**. If
those clients hired with bias, the model learned the bias and now reproduces it at a scale and speed
no human panel could reach. The vendor's answer — "we remove name, sex, and race before scoring" —
addresses the direct features and leaves every proxy in the table above intact.

## 1.5 Affected persons

Roughly 12,000 applicants a year, most of them applying for hourly warehouse and driving work. This
population is disproportionately likely to have non-linear work histories, gaps, and résumés written
without professional help — precisely the patterns the model penalises. They also have the least
practical ability to contest a rejection they never learn the reason for.

That asymmetry is the reason this assessment recommends a hard control rather than a policy
statement.
