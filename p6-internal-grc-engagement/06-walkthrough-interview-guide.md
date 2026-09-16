# Walkthrough Interview Guide — What to Ask, and How

The questions an auditor actually asks, in the order that produces true answers.

---

## The rule that changes everything

**Never ask whether a control exists. Ask the person to describe what happened the last time.**

| Weak question | What you get | Strong question | What you get |
|---|---|---|---|
| "Do you review access quarterly?" | "Yes." | "Walk me through the last time someone left. Who removed their access, and how do you know it was removed?" | The truth, including that it took three weeks and nobody checked |
| "Do you have backups?" | "Yes." | "When did you last restore from one, and what did you restore?" | Usually silence |
| "Is MFA enabled?" | "Yes." | "Show me the list of admin accounts and their MFA status." | Two accounts exempted that nobody remembered |

A yes/no question invites the answer the person believes is expected. **A narrative question forces
them to reconstruct an actual event**, and gaps appear on their own without you accusing anyone.

This matters more than any framework knowledge. A junior who knows ISO 27001 by heart and asks
yes/no questions gathers nothing. A junior who asks "walk me through the last time" gathers findings.

---

## The three-move sequence

Every topic follows the same shape:

**1. Open — let them describe it in their words**
> "Walk me through how a new employee gets access to systems."

Say nothing while they talk. Do not fill silences. People fill silences with the part they were
going to leave out.

**2. Probe — go to the specific instance**
> "Think of the most recent one. Who was it, when, and what exactly happened?"

Abstractions hide exceptions. A specific instance cannot.

**3. Verify — ask for the artifact**
> "Can you show me the request or the ticket for that one?"

The gap between what someone says and what they can show you **is the finding**. Not a
disagreement — a finding.

---

## The follow-up ladder

When an answer sounds too clean, climb:

1. **"How often does that happen?"** — rare processes are rarely followed
2. **"When did it last happen?"** — "I'm not sure" is an answer
3. **"Who else can do that?"** — reveals undocumented access
4. **"What happens if that person is unavailable?"** — reveals single points of failure
5. **"Has it ever not worked?"** — people tell you about failures if you make it normal to have them
6. **"Show me."** — always the last step, always asked

Ask these calmly, in the same tone as the first question. The moment your tone changes, the person
starts defending instead of describing, and you stop learning anything.

---

## Who to interview, and what only they know

| Role | Ask them about | Do not ask them about |
|---|---|---|
| **Owner / executive** | Risk appetite, what would hurt the business, budget, what keeps them up at night | Technical configuration |
| **IT / engineering** | How systems actually work, what they worry about, shortcuts taken under deadline | Business impact |
| **Operations / front line** | What they really do versus what the policy says | Policy intent |
| **Finance** | Payment flows, vendor contracts, who can approve spend | Technical controls |
| **HR / people** | Joiner-mover-leaver process, screening, training completion | Systems |

**The front line is where policy meets reality**, and it is the interview juniors skip. The
policy says access is requested by ticket; the operator tells you the manager just sends a Slack
message. Both are true. Only the second one describes the control.

---

## Question bank by domain

For each: the opening question, the probe, the evidence to request, and the answer that should
worry you.

### Access management

**Open:** "Walk me through how someone gets access to a system on their first day."
**Probe:** "And when they leave — talk me through the most recent departure."
**Evidence:** User list per system with roles; the access request record for the last joiner; the
removal record for the last leaver.
**Red flag:** "It depends who it is." Undocumented discretion is the control not existing.

**Open:** "Who has administrator rights, and how did they get them?"
**Probe:** "When was that list last reviewed, and by whom?"
**Evidence:** Admin role export per system; the last review with a signature and date.
**Red flag:** A list longer than the person expected. They will say "that one shouldn't still be
there" — write down exactly those words.

### Change management

**Open:** "Take me through how a change reaches production."
**Probe:** "Tell me about the last emergency change. What was different?"
**Evidence:** Sample of five changes with review records; the emergency change procedure.
**Red flag:** "Emergencies go straight through." That is the real process; the documented one is
decoration.

### Backup and recovery

**Open:** "If the main database were lost right now, what would you do?"
**Probe:** "When did you last actually do that, and how long did it take?"
**Evidence:** Restore log with times and outcome; the backup configuration.
**Red flag:** "We'd restore from the backup" said with confidence and no date attached.

### Third parties

**Open:** "Which outside companies can reach your customer data?"
**Probe:** "How did you decide they were safe to use?"
**Evidence:** Subprocessor list; DPA per provider; assurance reports with the date they were read.
**Red flag:** A list that grows while they think about it. The ones remembered last are the
unassessed ones.

### Incidents

**Open:** "Tell me about the last security incident, however small."
**Probe:** "Who decided it was over? What changed afterwards?"
**Evidence:** Incident record; the plan; evidence of any resulting change.
**Red flag:** "We've never had one." Everyone has had one. It means they are not detecting or not
recording — and either is the finding.

### Data and privacy

**Open:** "What personal data do you hold, and where does it live?"
**Probe:** "If someone asked you to delete all their data today, what would you do?"
**Evidence:** Data inventory; privacy notice; a completed deletion request.
**Red flag:** Hesitation on where it lives. You cannot protect what you cannot locate.

### Logging and monitoring

**Open:** "If someone accessed customer data at 3am on a Sunday, how would you find out?"
**Probe:** "Has anyone ever looked at those logs? When, and why?"
**Evidence:** Retention configuration; a sample entry; evidence of a review.
**Red flag:** "We have logs." Logs nobody reads are storage, not monitoring.

### Policies

**Open:** "How do people know what they're supposed to do about security?"
**Probe:** "When was that last updated, and what prompted the update?"
**Evidence:** Policy set with version and approval dates; training completion records.
**Red flag:** A policy approved once, years ago, with no revision. It describes a company that no
longer exists.

---

## What to do with contradictions

You will get answers that conflict — the manager says one thing, the operator another. This is
normal and it is useful. Do not resolve it in the room and do not tell one that the other
disagreed.

Write both down with attribution and dates, then go and look at the system. **The system is the
tie-breaker.** The gap between the two accounts is often the most valuable finding in the
engagement, because it tells you the control is not understood the same way by the people
operating it.

---

## The tone that gets you the truth

You are not there to catch anyone. Say so, and mean it:

> "I'm documenting how things actually work, not how they're supposed to work. If there's a
> shortcut everyone takes, that's what I need to know — a control that doesn't match reality is my
> problem to fix, not yours to hide."

People tell auditors the truth when telling the truth is not punished. **A junior auditor who
sounds like an inspector gets a clean story and finds nothing.** One who sounds genuinely curious
gets shown the workaround on the second day.

And when someone admits a gap: thank them, write it down, and move on. No reaction. The moment you
look pleased to have found something, the interview is over even if the person keeps talking.

---

## After the interview — same day

1. Write your notes up **within an hour**. Memory degrades faster than you think, and "I'll do it
   tomorrow" produces notes you cannot rely on.
2. Send a short summary back to the interviewee: *"Here's what I understood. Correct me where I
   got it wrong."* This costs ten minutes and eliminates the entire category of findings based on
   misunderstanding.
3. Convert each observation into a row in the test log: what must be true, what evidence proves it,
   what you were told, what you saw.
4. List what you still need. That list becomes the PBC request.

---

## Applying this when you are the subject

You are interviewing yourself, which is harder, not easier. Two things help:

**Write the answers down before you check.** Answer each opening question from memory first, then
go and look. Where memory and reality differ is exactly where your register is wrong — and you
will not notice if you look first and write after.

**Use the probe questions on yourself without mercy.** "When did I last restore a backup?" has a
date or it does not. "I'd restore from the hosting provider" is not an answer, it is a hope.
