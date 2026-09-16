# Internal IT Audit Report — Information Security Management System

**Northgate Services LLC**
**Report reference:** IA-2026-01 · **Issued:** September 2026
**Classification:** Internal — not for external distribution
**Distribution:** Founder / Principal (management), engagement file

---

## 1. Executive summary

### Objective

To assess whether the controls protecting Northgate's hosted applications, their user data, and
the cloud services that support them are **designed** adequately to meet the organisation's stated
obligations under ISO/IEC 27001:2022, applicable privacy law, and customer contractual
requirements.

### Scope and period

Development, hosting and operation of Northgate's web applications, the personal data they hold,
and the supporting cloud services. Assessment performed August–September 2026. Field operations
of the subcontracting business were excluded — see §3.

### Overall opinion

> ## ⬤ UNSATISFACTORY — significant improvement required

**Seven findings were raised: one Critical, four High, two Medium.**

The estate holds other people's personal data across seven live applications and is supported by
eight third-party services, with no documented policy set, no tested backup, no logging, and no
multi-factor authentication on the two accounts that control everything else.

**The Critical finding is not a missing control on an important system. It is a chain.** The domain
registrar controls DNS for every company domain and therefore every email address. Email controls
password resets on every other service. Neither the registrar account nor the productivity-suite
administrator account enforces MFA. **A single credential compromise at the registrar is sufficient
to take control of the entire estate**, including the ability to lock the owner out of the recovery
path.

### The limitation that governs this report

**This is an assessment of control DESIGN. It offers no opinion on operating effectiveness.**

All 24 controls selected for testing are recorded as "Not started" in the control test log. No
control has yet operated over a period, been evidenced, or been sampled. An opinion on operating
effectiveness would therefore have no basis, and none is given here.

This is the correct position for a management system in its first cycle. It is stated plainly
because a report that implied tested controls where none were tested would be worthless — and
because the temptation to imply it is strongest when auditing one's own organisation.

### Independence

**This is a first-party assessment. The assessor is the organisation's principal and the developer
of the systems assessed.** It is not independent review and does not satisfy any requirement for
independent audit, certification audit, or customer assurance. Management responses in §5 were
provided by the same person who raised the findings. See §3.4.

---

## 2. Summary of findings

| Ref | Finding | Rating | Owner | Target |
|---|---|---|---|---|
| **F-01** | No MFA on the registrar and productivity-suite administrative accounts, which together control recovery for every other service | **Critical** | Security Lead | Week 1 |
| **F-02** | Backups are configured but have never been restore-tested | **High** | Security Lead | Week 2 |
| **F-03** | No secret scanning on source control; application dependencies not monitored for known vulnerabilities | **High** | Security Lead | Week 1–2 |
| **F-04** | Asset inventory incomplete; unmaintained applications may remain reachable from the internet with data attached | **High** | Security Lead | Week 1 |
| **F-05** | Applications collect personal data with no published privacy notice and no working deletion route | **High** | Security Lead | Week 3 |
| **F-06** | Single administrator across all systems; no break-glass procedure; critical accounts tied to a personal identity | **Medium** | Security Lead | Week 2 |
| **F-07** | No documented policy set, no incident response plan, and no logging on hosted applications | **Medium** | Security Lead | Week 2–3 |

### Rating definitions

| Rating | Meaning |
|---|---|
| **Critical** | Could result in loss of control of the estate, or a reportable breach, with no compensating control. Remediate immediately. |
| **High** | Material exposure of personal data, availability, or legal obligation. Remediate within the current cycle. |
| **Medium** | Control gap that increases the likelihood or consequence of another risk. Plan with a named date. |
| **Low** | Improvement opportunity. No exposure identified. |

---

## 3. Scope, method and limitations

### 3.1 In scope

Seven live applications; eight supporting third-party services (hosting platform, source control,
productivity suite, managed database, payment processor, **domain registrar**, AI model provider,
transactional email); the personal data these hold; and the workstation from which they are
administered.

### 3.2 Out of scope, deliberately

Field operations of the subcontracting business, and any client system Northgate does not host or
administer. The subcontracting side handles contract documents and personnel records carrying
flow-down obligations; this exclusion is recorded with a date to revisit, not omitted. **An
unstated scope gap becomes an audit finding. A stated one becomes a plan.**

### 3.3 Method

Risk identification applied a fixed six-question set to every service in scope:

1. Who can access it, and how is that access protected?
2. What happens if control of it is lost?
3. What happens if its contents leak?
4. How would anyone know something had gone wrong?
5. Who else has access, and under what contract?
6. What breaks if it disappears tomorrow?

Twenty-two risks were identified and scored likelihood × impact on a 1–5 scale. Twenty-four Annex A
controls were selected for testing and documented in the control test log with the evidence each
requires.

**The Critical finding did not come from the asset inventory. It came from mapping the dependencies
between assets** — which is why an hour spent on a dependency diagram preceded any scoring.

### 3.4 Limitations

1. **No operating-effectiveness testing.** As stated in §1. Design only.
2. **First-party.** The assessor is the principal and the systems' developer. Management responses
   in §5 are self-provided. An independent review is itself recorded as a finding in the risk
   register (R-21).
3. **Residual scores are estimates**, derived from a documented reduction assumption per risk band,
   not a re-score after testing. They are planning figures, not measurements.
4. **No penetration testing or vulnerability scanning** was performed against production systems
   within this engagement.

---

## 4. Control coverage

| | Count |
|---|---|
| Annex A controls assessed for applicability | 93 |
| Applicable | 82 |
| Excluded with documented rationale | 11 |
| Selected for testing this cycle | 24 |
| **Tested with evidence obtained** | **0** |

Exclusions rest on stated facts: no premises, no employees, no owned network, no outsourced
development. **Each exclusion names the fact it rests on and becomes applicable the day that fact
changes** — reviewed at every management review, not treated as settled.

The zero in the final row is the most important number in this report. It is the correct state for
a first cycle, and recording it honestly is what makes the document usable in the next one.

---

## 5. Detailed findings

---

### F-01 · No MFA on the accounts that control recovery for the entire estate

**Rating: CRITICAL** · Related risks: R-01, R-02, R-05

**Condition.**
Multi-factor authentication is not enforced on the domain registrar account or on the
productivity-suite administrative account. The productivity-suite administrator identity is also
the owner's daily-use account, with no separation between administrative and routine activity.

**Criteria.**
ISO/IEC 27001:2022 **A.8.5** Secure authentication; **A.8.2** Privileged access rights. Industry
baseline requires MFA on all administrative access, and separation of privileged identities from
daily-use accounts.

**Cause.**
Neither account is perceived as a system. The registrar is treated as a billing relationship and
appears on no asset list. MFA was enabled on user-facing applications first, because those are the
accounts that feel like security.

**Effect.**
The dependency path is:

```
Registrar (DNS)  ──►  company email  ──►  password reset on every other service
```

An attacker who obtains the registrar credential can redirect MX records, receive password-reset
mail for the hosting platform, source control, the database and the payment processor, and lock the
owner out of the recovery path in the same action. **Loss of this one account is loss of the
estate**, including the customer personal data held in the managed database. There is no
compensating control.

**Recommendation.**
1. Enable MFA on the registrar account using a hardware key or TOTP application — **not SMS**, which
   is defeated by the same attack path.
2. Enable MFA on the productivity-suite administrator account and create a separate administrative
   identity distinct from the daily-use account.
3. Store recovery codes for both offline, physically, outside the productivity suite.
4. Enable registrar lock on all domains.

**Management response.** Accepted. Both accounts to be secured in Week 1. Recovery codes to be
printed and stored offline. *(Response provided by the Founder, who is also the assessor — see
§3.4.)*

---

### F-02 · Backups exist but have never been restore-tested

**Rating: HIGH** · Related risk: R-04

**Condition.**
The managed database service performs automated backups. No restore has been performed, timed or
verified. There is no restore log, no recovery time objective, and no record of what a restored
dataset should contain.

**Criteria.**
ISO/IEC 27001:2022 **A.8.13** Information backup — requires that backup copies be **tested
regularly**, not merely taken.

**Cause.**
The backup is a provider feature enabled by default. A feature that is on is assumed to work.

**Effect.**
**A backup that has never been restored is a hypothesis, not a control.** Common failure modes —
partial schema coverage, an unrecoverable retention window, a restore that requires a plan tier the
account does not hold — are discovered only during an incident, at the moment recovery is needed.
The applications in scope hold user accounts and learner performance history; loss would be
unrecoverable and, depending on jurisdiction, notifiable.

**Recommendation.**
1. Perform one full restore to a non-production target for each application.
2. Record: source, target, start time, end time, record count verified, outcome, tester name.
3. Define an RTO and RPO per application from what the test actually demonstrated.
4. Schedule quarterly thereafter; a restore not performed in the quarter is a failed control, not a
   deferred task.

**Management response.** Accepted. One restore test per application in Week 2; quarterly cycle
established from the result. *(Self-provided — see §3.4.)*

---

### F-03 · No secret scanning; dependencies not monitored for known vulnerabilities

**Rating: HIGH** · Related risks: R-03, R-08

**Condition.**
Secret scanning and push protection are not enabled on source-control repositories. Dependency
vulnerability alerting is not enabled. No inventory exists of which credentials have been committed
historically, and no remediation SLA is defined by severity.

**Criteria.**
ISO/IEC 27001:2022 **A.8.28** Secure coding; **A.8.8** Management of technical vulnerabilities.

**Cause.**
Repositories were created for speed of delivery. Platform security settings are opt-in and were
never visited.

**Effect.**
Environment variables, API keys and model-provider credentials are handled routinely during
development. Without push protection, a single commit exposes a working credential — permanently,
because git history retains it after deletion from the working tree. Without dependency alerting,
a known-exploited vulnerability in an application dependency remains live indefinitely, with no
mechanism by which anyone would learn of it. **Neither gap produces any signal when it fails.**

**Recommendation.**
1. Enable secret scanning and push protection on every repository.
2. Scan full history; **rotate every credential found, not only those in the current tree**.
3. Enable dependency alerting; set a remediation SLA — Critical 7 days, High 30 days.
4. Move all runtime secrets to the hosting platform's environment-variable store.

**Management response.** Accepted. Settings enabled in Week 1; history scan and rotation in Week 2.
*(Self-provided — see §3.4.)*

---

### F-04 · Asset inventory incomplete; unmaintained applications may remain internet-reachable

**Rating: HIGH** · Related risk: R-09

**Condition.**
The application inventory was completed during this engagement and is the first such record. It
could not be confirmed that every historical deployment has been decommissioned. Deployments may
remain publicly reachable with dependencies unpatched and a database still attached.

**Criteria.**
ISO/IEC 27001:2022 **A.5.9** Inventory of information and associated assets.

**Cause.**
Rapid deployment on a platform where publishing is a single command, over a period with no asset
register. Nothing in the workflow prompts decommissioning.

**Effect.**
**An abandoned live application is the highest-probability incident in an estate of this shape, and
it is invisible to everyone because nobody thinks about it.** It receives no patching, no
monitoring and no attention, while remaining reachable and potentially holding data. It is not
covered by any control in the Statement of Applicability, because it is not known to exist.

**Recommendation.**
1. Enumerate every deployment across the hosting platform and every DNS record at the registrar.
2. For each: identify owner, purpose, data held, last update.
3. Decommission or access-restrict anything unmaintained; export and delete attached data first.
4. Make inventory reconciliation a quarterly control with a dated evidence artifact.

**Management response.** Accepted. Full enumeration in Week 1. *(Self-provided — see §3.4.)*

---

### F-05 · Personal data collected with no privacy notice and no deletion route

**Rating: HIGH** · Related risk: R-07

**Condition.**
Live applications collect account data, email addresses and behavioural performance history. No
privacy notice is published on the applications reviewed. No account-deletion function exists, and
no deletion request has ever been processed end to end.

**Criteria.**
ISO/IEC 27001:2022 **A.5.34** Privacy and protection of PII. US state privacy statutes; GDPR
Articles 13, 15 and 17 where EU or UK users exist.

**Cause.**
Products were built and launched before any privacy obligation was assessed. The assumption that
the applications have no EU users has never been tested against actual traffic.

**Effect.**
A publicly reachable SaaS generally acquires EU or UK users whether or not it targeted them.
Learner performance data reveals a person's competence and is more sensitive than the account
record that carries it. **An inability to honour a deletion request is not only a legal exposure;
it is an operational one** — the request arrives by email and there is no procedure, no owner and
no defined timeframe.

**Recommendation.**
1. Publish a privacy notice per application: data collected, purpose, lawful basis, retention,
   subprocessors, contact route.
2. Implement account deletion in-product; document what it removes and what it retains, and why.
3. Check analytics for EU/UK traffic and record the finding, rather than assuming.
4. Process one test deletion request end to end and file it as evidence.

**Management response.** Accepted. Notices and deletion route in Week 3. *(Self-provided — see
§3.4.)*

---

### F-06 · Single administrator, no break-glass, critical accounts on a personal identity

**Rating: MEDIUM** · Related risks: R-05, R-19

**Condition.**
One individual holds administrative access to every system. There is no documented recovery
procedure and no second party able to regain access. Critical service accounts are registered to a
personal named identity rather than a role address.

**Criteria.** ISO/IEC 27001:2022 **A.5.2** Information security roles; **A.8.2** Privileged access.

**Cause.** Organisational reality — a founder-operated company with no employees.

**Effect.**
This is not primarily a segregation-of-duties issue; at this headcount, segregation is not
achievable and the Statement of Applicability records that fact. It is an **availability and
continuity** issue. If the individual is unavailable, or the personal identity is lost or
compromised, there is no path back into the estate. The dependency on a single identity compounds
F-01: the same account is both the sole administrator and the recovery route.

**Recommendation.**
1. Document a break-glass procedure; store recovery codes for every critical service offline in a
   sealed envelope with a named holder.
2. Migrate critical service accounts to role addresses (`admin@`, `billing@`).
3. Verify recovery methods on every account and record the verification date.
4. Re-assess when headcount changes — this finding converts to a segregation finding at that point.

**Management response.** Accepted. Break-glass documented and role addresses migrated in Week 2.
*(Self-provided — see §3.4.)*

---

### F-07 · No policy set, no incident response plan, no logging

**Rating: MEDIUM** · Related risks: R-20, R-16, R-12

**Condition.**
No approved information security policies exist. No incident response plan is documented. Hosted
applications have no application or administrative access logging, and no retention period is
defined.

**Criteria.**
ISO/IEC 27001:2022 **A.5.1** Policies; **A.5.24** Incident management planning; **A.8.15** Logging.

**Cause.**
Documentation is perceived as overhead in an organisation of one, where every practice lives in a
single person's head.

**Effect.**
Three distinct consequences:

- **Policies:** the first customer security questionnaire or certification attempt stops here.
  There is nothing to attach, and nothing an auditor can test against.
- **Incident response:** decisions during an incident are made under pressure, without predefined
  notification thresholds or timeframes — precisely when a documented sequence is worth the most.
- **Logging:** without logs, an incident cannot be scoped. The question "what did they access, and
  when?" has no answer, which converts a contained event into a worst-case disclosure assumption.
  **Logs nobody keeps are not a monitoring gap; they are an investigation gap.**

**Recommendation.**
1. Adopt a minimal policy set — acceptable use, access control, incident response, vendor
   management, data protection — each versioned, dated and approved. Short and real beats long and
   aspirational.
2. Write a one-page IR plan: detect, contain, assess, notify, learn. Include notification
   thresholds and who decides.
3. Enable platform logging with a defined retention period; review monthly and evidence the review.

**Management response.** Accepted. Policy set and IR plan in Week 2; logging in Week 3.
*(Self-provided — see §3.4.)*

---

## 6. Remediation plan

| Week | Findings addressed | Deliverable |
|---|---|---|
| 1 | F-01, F-03, F-04 | MFA enforced with offline recovery codes; secret scanning and dependency alerting on; complete asset enumeration |
| 2 | F-02, F-03, F-06, F-07 | Restore test per application, logged; credential rotation complete; break-glass documented; policy set and IR plan approved |
| 3 | F-05, F-07 | Privacy notices published; deletion route live and tested; logging enabled with retention |
| 4 | — | PCI DSS SAQ-A scope confirmed; contractual flow-downs reviewed; management review |

---

## 7. Follow-up

Each finding is tracked in the risk register with an owner and a target date. **A finding is closed
only when the evidence named in the control test log has been obtained and filed** — not when the
remediation is believed to be done.

Re-test is scheduled for Q4 2026. At that point the controls will have operated for a period, and
an operating-effectiveness opinion becomes possible for the first time. **That report, not this one,
is the one a customer or certification body can rely on.**

---

## 8. Appendix — controls selected for testing

24 Annex A controls with the evidence each requires and its test frequency are documented in
[`07-control-test-log.csv`](07-control-test-log.csv). All are recorded "Not started" as at the date
of this report.

Controls span: policies (A.5.1), asset inventory (A.5.9), access rights (A.5.18), supplier security
and agreements (A.5.19, A.5.20, A.5.23), incident preparation (A.5.24), legal obligations (A.5.31),
privacy (A.5.34), independent review (A.5.35), awareness (A.6.3), remote working (A.6.7), off-premises
assets (A.7.9), endpoints (A.8.1), privileged access (A.8.2), authentication (A.8.5), capacity
(A.8.6), vulnerabilities (A.8.8), backup (A.8.13), logging (A.8.15), cryptography (A.8.24), secure
coding (A.8.28), environment separation (A.8.31), and change management (A.8.32).

---

*Report IA-2026-01 · Northgate Services LLC · Genericized from a real first-party engagement.
Company, product and infrastructure names are replaced; scope, findings, ratings, control decisions
and reasoning are as executed.*
