#!/usr/bin/env python3
"""
Continuous privileged access review.

Replaces a quarterly spreadsheet-and-email access review with an automated exception
engine. The design principle: managers should not be asked to attest to 400 access
records. They should be asked about the 12 that look wrong.

Inputs  : entitlements.csv (from the IdP / cloud IAM export)
          hr_roster.csv    (from the HRIS)
          approvals.csv    (approved privileged access requests)
Outputs : exceptions.csv   (what a human must decide on)
          metrics.csv      (control health over time)

Usage: python3 access_review.py [--dormant-days 45] [--outdir .]
"""

import argparse
import csv
import datetime as dt
import os
import sys
from collections import defaultdict

# Segregation-of-duties pairs: holding both roles in the same system is a conflict.
SOD_CONFLICTS = [
    ({"deploy_production", "approve_deployment"}, "Can deploy and approve own deployment"),
    ({"create_vendor", "approve_payment"}, "Can create a vendor and pay it"),
    ({"admin_iam", "audit_logs_delete"}, "Can grant access and erase the record of it"),
    ({"modify_payroll", "approve_payroll"}, "Can change and approve payroll"),
]

PRIVILEGED_ROLES = {
    "admin_iam", "deploy_production", "db_admin_prod", "audit_logs_delete",
    "approve_payment", "approve_payroll", "security_admin", "break_glass",
}

SEVERITY_ORDER = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}


def read_csv(path):
    if not os.path.exists(path):
        sys.exit(f"Missing input file: {path}")
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def parse_date(value):
    if not value:
        return None
    return dt.datetime.strptime(value.strip(), "%Y-%m-%d").date()


def run(args):
    today = dt.date.today()
    entitlements = read_csv(os.path.join(args.indir, "entitlements.csv"))
    roster = {r["employee_id"]: r for r in read_csv(os.path.join(args.indir, "hr_roster.csv"))}
    approvals = read_csv(os.path.join(args.indir, "approvals.csv"))

    approved = {(a["employee_id"], a["role"]) for a in approvals
                if a["status"].lower() == "approved"
                and (not a["expires"] or parse_date(a["expires"]) >= today)}

    exceptions = []
    roles_by_person = defaultdict(set)

    for e in entitlements:
        emp_id = e["employee_id"]
        role = e["role"]
        system = e["system"]
        last_used = parse_date(e.get("last_used"))
        person = roster.get(emp_id)
        roles_by_person[(emp_id, system)].add(role)

        # 1. Orphaned account — access with no active HR record
        if person is None:
            exceptions.append(dict(
                severity="Critical", finding="Orphaned account",
                employee_id=emp_id, name=e.get("display_name", "UNKNOWN"),
                system=system, role=role,
                detail="Active entitlement with no matching HR record. Terminated or never onboarded.",
                action="Disable immediately, then investigate how it survived offboarding.",
                owner="IT Security"))
            continue

        if person["status"].lower() == "terminated":
            term = parse_date(person.get("termination_date"))
            days = (today - term).days if term else "unknown"
            exceptions.append(dict(
                severity="Critical", finding="Access retained after termination",
                employee_id=emp_id, name=person["name"], system=system, role=role,
                detail=f"Terminated {days} days ago and still entitled.",
                action="Revoke now. Raise an offboarding process incident.",
                owner="IT Security"))
            continue

        privileged = role in PRIVILEGED_ROLES

        # 2. Privileged access with no approval record
        if privileged and (emp_id, role) not in approved:
            exceptions.append(dict(
                severity="High", finding="Privileged access without approval",
                employee_id=emp_id, name=person["name"], system=system, role=role,
                detail="Privileged role held with no approved, unexpired access request on file.",
                action="Manager confirms business need or access is revoked at the next cycle.",
                owner=person["manager"]))

        # 3. Dormant privileged access
        if privileged and last_used and (today - last_used).days > args.dormant_days:
            exceptions.append(dict(
                severity="High", finding="Dormant privileged access",
                employee_id=emp_id, name=person["name"], system=system, role=role,
                detail=f"Privileged role unused for {(today - last_used).days} days "
                       f"(threshold {args.dormant_days}).",
                action="Revoke unless the manager documents a standby justification.",
                owner=person["manager"]))

        # 4. Role inconsistent with department
        if privileged and person["department"].lower() in ("sales", "marketing", "support") \
                and role in ("db_admin_prod", "deploy_production", "admin_iam"):
            exceptions.append(dict(
                severity="High", finding="Role inconsistent with job function",
                employee_id=emp_id, name=person["name"], system=system, role=role,
                detail=f"Privileged engineering role held by {person['department']}.",
                action="Manager justifies or access is revoked.",
                owner=person["manager"]))

    # 5. Segregation of duties conflicts
    for (emp_id, system), roles in roles_by_person.items():
        person = roster.get(emp_id)
        if not person or person["status"].lower() == "terminated":
            continue
        for pair, description in SOD_CONFLICTS:
            if pair.issubset(roles):
                exceptions.append(dict(
                    severity="Critical", finding="Segregation of duties conflict",
                    employee_id=emp_id, name=person["name"], system=system,
                    role=" + ".join(sorted(pair)),
                    detail=description,
                    action="Remove one side of the conflict, or document a compensating control "
                           "with a named reviewer.",
                    owner=person["manager"]))

    exceptions.sort(key=lambda x: (SEVERITY_ORDER[x["severity"]], x["system"], x["name"]))

    # ---- outputs ----
    os.makedirs(args.outdir, exist_ok=True)
    exc_path = os.path.join(args.outdir, "exceptions.csv")
    fields = ["severity", "finding", "employee_id", "name", "system", "role",
              "detail", "action", "owner"]
    with open(exc_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(exceptions)

    total_entitlements = len(entitlements)
    reviewed_by_human = len(exceptions)
    counts = defaultdict(int)
    for e in exceptions:
        counts[e["severity"]] += 1

    metrics = [
        ("run_date", today.isoformat()),
        ("entitlements_evaluated", total_entitlements),
        ("exceptions_raised", reviewed_by_human),
        ("critical", counts["Critical"]),
        ("high", counts["High"]),
        ("medium", counts["Medium"]),
        ("manual_review_reduction_pct",
         round(100 * (1 - reviewed_by_human / total_entitlements), 1) if total_entitlements else 0),
    ]
    with open(os.path.join(args.outdir, "metrics.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["metric", "value"])
        w.writerows(metrics)

    print(f"Entitlements evaluated : {total_entitlements}")
    print(f"Exceptions for review  : {reviewed_by_human} "
          f"({counts['Critical']} critical, {counts['High']} high)")
    print(f"Manual review reduced by {metrics[-1][1]}%")
    print(f"Written: {exc_path}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--dormant-days", type=int, default=45)
    p.add_argument("--indir", default="sample-data")
    p.add_argument("--outdir", default="output")
    run(p.parse_args())
