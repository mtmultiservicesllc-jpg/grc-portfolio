# Publishing the Portfolio on GitHub

The projects are worth nothing in a folder on your Mac. This takes about 30 minutes.

## One repository, not five

Five thin repositories look like five abandoned experiments. One repository with five worked
assessments looks like a body of work.

**Repository name:** `grc-portfolio`
**Description:** "Worked GRC assessments — AI governance, ISO 27001, control automation, risk
quantification."
**Public.** A private portfolio is not a portfolio.

## Structure

```
grc-portfolio/
├── README.md                        <- the front page; most visitors read only this
├── p1-ai-hiring-assessment/
├── p2-iso27001-soa/
├── p3-continuous-access-review/
├── p4-risk-acceptance/
└── p5-tprm-fair/
```

## Steps

```bash
cd ~/Downloads/GRC-Portfolio
git init
git add .
git commit -m "GRC portfolio: five worked assessments"
```

Then on github.com: **New repository** → name `grc-portfolio` → Public → **do not** initialise with
a README (you already have one) → Create.

```bash
git remote add origin https://github.com/<your-username>/grc-portfolio.git
git branch -M main
git push -u origin main
```

## After pushing

1. **Pin the repository** to your GitHub profile (profile → Customize your pins).
2. **Add the link to your LinkedIn** — Featured section and the About text.
3. **Add it to your résumé** contact line, next to your email.
4. Set the repository's **About** field with the same one-line description and topics:
   `grc` `iso27001` `nist-ai-rmf` `risk-management` `compliance` `ai-governance`.

## The three-minute video, per project

The 2026 advice from hiring managers is explicit: they want to see how you think, not just what you
produced. A short screen recording beats another document.

Record with QuickTime (File → New Screen Recording). Three minutes, no editing, no script read
aloud. Structure:

1. **The situation** (20 s) — what the organisation wanted to do.
2. **The decision** (60 s) — what you recommended and, more importantly, what you refused.
3. **The hard part** (60 s) — the judgment call you were least certain about, and how you resolved it.
4. **What would change it** (30 s) — the fact that would flip your recommendation.

Upload unlisted to YouTube, link it at the top of that project's README.

Do not aim for polish. A slightly rough video of someone thinking clearly is more convincing than a
produced one, and far more convincing than nothing.

## What not to do

- Do not fabricate commit history to look busier. It fools no one who looks.
- Do not remove the "scenario company" disclaimers. They are what make the rest credible.
- Do not leave a project half-finished in the repository. Better four complete than five with a stub.
