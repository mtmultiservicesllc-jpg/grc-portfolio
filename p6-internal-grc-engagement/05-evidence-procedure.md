# Collecting Audit Evidence — How It Actually Works

Northgate Services LLC — ISMS · Procedure v1.0

---

## The chain, and where each tool sits

```
Source system          →  the place the fact lives (admin consoles, source control, hosting platform, registrar)
       ↓
Evidence artifact      →  a screenshot, an export, a log, a signed record
       ↓
Evidence repository    →  the document repository, one folder per test cycle. Never edited after filing.
       ↓
Control test log       →  a spreadsheet: one row per control per cycle, with the result
       ↓
Tableau / dashboard    →  reads the LOG only. Never holds the evidence itself.
```

**Tableau never touches evidence.** It reads status: tested or not, passed or failed, when, by whom,
next due. That separation is not a preference — it is what lets you publish a dashboard without
publishing your weaknesses.

---

## What counts as evidence, and what does not

An auditor reviewing your work asks one question of every artifact: **could someone else obtain
this same result independently?**

| Counts | Does not count |
|---|---|
| Screenshot showing the system, the setting, **and the system clock or a visible date** | A cropped image of a toggle |
| CSV export straight from the admin console, with the export timestamp | A hand-typed list of users |
| Restore log with start time, end time, outcome, tester name | "Backups are working" |
| A signed and dated acknowledgement | An email saying "yes we do that" |
| Configuration screenshot plus the URL bar showing which tenant | A screenshot with the org name cropped out |

**The single most common failure:** a screenshot that proves a setting exists but not *when* it was
observed or *where*. Always capture the full window — the clock in the menu bar, the URL, the
account name. It costs nothing and it is the difference between evidence and decoration.

---

## The five rules

1. **Date and source must be visible inside the artifact itself.** Not only in the filename — a
   filename can be changed by anyone.
2. **Record who captured it.** Evidence without a named collector cannot be questioned, which
   means it cannot be trusted.
3. **State how it was obtained**, so someone else can repeat it. "Admin console → Security →
   Authentication → 2-Step Verification, 11 Sep 2026" is reproducible. "MFA screenshot" is not.
4. **Document the population when you sample.** If you test 5 of 40 changes, say 5 of 40 and say
   how you picked them. An undocumented sample is an anecdote.
5. **Never edit filed evidence.** If it is wrong, capture it again and file both, with a note.
   Editing evidence is the one thing that ends an auditor's credibility permanently.

---

## Folder structure

```
/ISMS/
  /Evidence/
    /2026-Q3/
      /A.8.5-Secure-authentication/
        A.8.5_productivity-suite_mfa-enforcement_2026-09-11_MT.png
        A.8.5_productivity-suite_user-mfa-status_2026-09-11_MT.csv
        A.8.5_source-control_2fa-org-setting_2026-09-11_MT.png
        A.8.5_registrar_mfa-enabled_2026-09-11_MT.png
      /A.8.13-Backup/
        A.8.13_restore-test-log_2026-09-11_MT.md
        A.8.13_restored-record-count_2026-09-11_MT.png
  /Control-Test-Log.gsheet
  /Policies/
  /Risk-Register.gsheet
```

**Naming convention:**
```
<control-ref>_<system>_<what-it-shows>_<YYYY-MM-DD>_<initials>.<ext>
```

Boring, and that is the point. Six months later you will need to find the evidence for A.8.5 for
Q3 in under ten seconds, and you will.

---

## Evidence per control — what to actually go and get

See `control-test-log.csv`. The column that matters is **`evidence_required`**, because it tells
you what to capture rather than leaving you to guess.

A few that people get wrong:

**A.8.5 MFA** — a screenshot of the enforcement *policy* is not enough. Enforcement can be on while
individual accounts are exempted. You need the enforcement setting **and** the per-user status
export. Two artifacts, not one.

**A.8.13 Backup** — the existence of a backup is not evidence that it restores. The evidence is a
restore you actually performed: source, target, start time, end time, record count verified,
outcome, your name. A backup never restored is a hypothesis.

**A.5.23 Cloud services** — the provider's SOC 2 report is *their* evidence. *Your* evidence is a
dated note saying which report you read, on what date, and what you concluded. Filing their PDF
without that note proves you downloaded a file.

**A.8.32 Change management** — you test a sample. Document the population size, the sample size,
and how you selected it. Five changes picked because they were convenient is not a sample.

---

## Filling the log

One row per control per cycle. Fill these as you go:

| Column | What goes in it |
|---|---|
| `test_result` | Pass · Fail · Partial · Not tested |
| `evidence_ref` | The folder path, e.g. `2026-Q3/A.8.5/` |
| Add: `tested_on` | Date you performed the test |
| Add: `tested_by` | Your name |
| Add: `next_due` | Date, derived from frequency |

**Record Fail honestly.** You are testing your own company, and the temptation to record "Partial"
where the truth is "Fail" is exactly the bias this whole exercise exists to expose. A register full
of passes on a company with no written policies is not a register — it is a document that will
embarrass you when someone reads it properly.

---

## Then, and only then, the dashboard

Once the log has real rows, Tableau reads it and answers the questions management actually asks:

- How many controls are tested versus untested?
- What is the pass rate, and which controls fail?
- How many are overdue for retest?
- Which risks have no tested control behind them?

That last one is the interesting chart, and it needs the bridge table you built — risks joined to
controls joined to test results. **A risk whose treating control has never been tested is an
untreated risk wearing a treatment label.** Finding those is worth more than any visual.

---

## For the portfolio versus for real

| | Real work | Portfolio |
|---|---|---|
| Where the log lives | Private spreadsheet | Genericized CSV |
| Where evidence lives | Private repository, never published | Never published, ever |
| Dashboard | Reporting layer over the private log | Tableau Public, genericized data only |
| Company named? | Yes | No |

Publishing a control test log that shows which of your controls fail is handing someone a map. The
genericized version shows the *method* — which is what a hiring manager is actually assessing.
