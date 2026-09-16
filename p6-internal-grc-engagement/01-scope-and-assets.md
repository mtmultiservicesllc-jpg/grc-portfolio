# 01 — ISMS Scope and Asset Inventory

**Northgate Services LLC** · v1.0 · September 2026

---

## 1. Scope statement

> The information security management system covers the **development, hosting and operation of
> Northgate's web applications and SaaS products**, the personal data of their users, and the
> supporting cloud services used to build, deploy and run them.
>
> **Out of scope:** field operations of the subcontracting business, and any client system
> Northgate does not host or administer.

**Why scoped this way.** The hosted applications are where the organisation holds other people's
data, and therefore where the obligations live. A scope covering the whole company would produce a
large document nobody maintains. **A narrow scope that is genuinely operated beats a broad one that
is aspirational** — and that is the position certification auditors take.

**The scope decision that required thought:** the subcontracting side handles contract documents
and personnel records for federal work. Those carry flow-down obligations. They were excluded from
this cycle deliberately, not by omission, and the exclusion is recorded with a date to revisit —
because an unstated scope gap becomes an audit finding, while a stated one becomes a plan.

---

## 2. Application inventory

| # | Application | Purpose | Personal data | Payment data | Status |
|---|---|---|---|---|---|
| A-01 | Exam preparation SaaS | AI-assisted licensure exam practice | Accounts, email, performance history | Processor-held | Live |
| A-02 | Company website | Corporate presence | Contact submissions | None | Live |
| A-03 | Content generation product | Vertical SaaS | Accounts | Processor-held | Live |
| A-04 | Reference application | Consumer utility | Minimal | None | Live |
| A-05 | Client-facing prototype | In development | None yet | None | Development |
| A-06 | Portfolio demonstration | Technical demonstration | None | None | Demo |
| A-07 | Game platform title | Monetised game on a third-party platform | Platform-held | Platform-held | Live |

**The inventory question that produced a finding:** *is anything still deployed that is no longer
maintained?*

A live application with unpatched dependencies and a database still attached is the
highest-probability incident in an estate like this, and it is invisible to everyone because nobody
thinks about it. Decommissioning one is the cheapest risk reduction available to an organisation of
this size — and it came out of the inventory, not out of a scan.

---

## 3. Supporting services

| # | Service | Role | Data it can reach | Criticality |
|---|---|---|---|---|
| S-01 | Hosting platform | Deployment, runtime | Application data in transit, environment variables | High |
| S-02 | Source control | Code, CI | Source, and secrets if committed | High |
| S-03 | Productivity suite | Email, documents, forms | Business email, client documents | High |
| S-04 | Managed database | Application storage | All application personal data | High |
| S-05 | Payment processor | Payments | Cardholder data (processor-side), customer email | Medium |
| S-06 | **Domain registrar** | DNS control | **Total control of every domain and email address** | **Critical** |
| S-07 | AI model provider | Inference | Whatever prompts contain | Medium |
| S-08 | Transactional email | Delivery | User email addresses | Medium |

---

## 4. Dependency analysis — where the real finding came from

```
   Registrar (DNS)  ──►  Hosting platform  ──►  Database
        │                      ▲                    │
        │                      │                    ▼
   Productivity suite     Source control      AI model provider
   (email, password            │
    resets, documents)    CI/CD deploy
```

Read as an attacker would: **registrar → email → password resets on everything else.**

This is why S-06 and S-03 carry more weight in this estate than any application-level control. The
registrar is almost always the least-protected account in a small company and the most catastrophic
to lose, and it appears on no asset list because nobody thinks of it as a system.

**An asset inventory alone would not have surfaced this. Mapping the dependencies did.** That is
the argument for spending an hour on a diagram before scoring anything.

---

## 5. Data categories

| Category | Location | Sensitivity | Driver |
|---|---|---|---|
| Application user accounts | Managed database | Medium | State privacy laws; GDPR where EU users exist |
| Learner performance data | Managed database | Medium — reveals a person's competence | Sector expectations |
| Contact submissions | Productivity suite | Low–medium | — |
| Payment data | Processor-held | High, but not held by Northgate | PCI DSS SAQ-A |
| Contracting records | Productivity suite | Medium–high | Contract flow-down clauses |
| **Source code and secrets** | Source control | **High** | — |

**The question that decides GDPR exposure:** does any application have EU or UK users? A publicly
reachable SaaS usually does, whether or not it targeted them. If yes, a privacy notice, a lawful
basis and a working deletion route are required — and that belongs in the risk register, not in a
footnote.

---

## 6. How this document is used

1. It defines what the risk register may contain. A risk against an asset not in the inventory is
   a scoping error.
2. It is versioned and dated. A scope statement without a version is not a scope statement.
3. It is reviewed at each management review, because the exclusions in the Statement of
   Applicability rest on facts recorded here — no premises, no employees, no owned network. The
   day one of those changes, controls become applicable automatically.

**Do not skip ahead to the risk register.** Assessing an estate you have not inventoried is how
assessments produce confident, wrong answers.
