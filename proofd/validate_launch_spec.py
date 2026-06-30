#!/usr/bin/env python3
"""
PROOFD launch_spec.json validator
Adapted from HACD Incubator AI Issuance Skill validator pattern.
Usage: python3 validate_launch_spec.py launch_spec.json [--strict]
"""

import json
import sys
import argparse

def validate(spec_path, strict=False):
    print(f"\n{'='*60}")
    print(f"  HACD Stack Token Validator — PROOFD")
    print(f"  File: {spec_path}")
    print(f"{'='*60}\n")

    with open(spec_path) as f:
        spec = json.load(f)

    errors = []
    warnings = []

    # ── Math checks
    lots = spec["issuance"]["total_hacd_lots"]
    units = spec["issuance"]["units_per_hacd_lot"]
    declared_supply = spec["issuance"]["total_prf_supply"]
    calculated_supply = lots * units

    print(f"[CHECK] Supply math: {lots} × {units:,} = {calculated_supply:,}")
    if calculated_supply != declared_supply:
        errors.append(f"Supply mismatch: declared {declared_supply:,} ≠ calculated {calculated_supply:,}")
    else:
        print(f"  ✓ PASS — declared supply matches\n")

    stack_cost = spec["issuance"]["stack_cost_hac_per_hacd"]
    declared_formation = spec["issuance"]["total_formation_cost_hac"]
    calculated_formation = lots * stack_cost

    print(f"[CHECK] Formation cost: {lots} × {stack_cost} HAC = {calculated_formation:,} HAC")
    if calculated_formation != declared_formation:
        errors.append(f"Formation cost mismatch: declared {declared_formation} ≠ calculated {calculated_formation}")
    else:
        print(f"  ✓ PASS — formation cost matches\n")

    # ── Phase lot check
    partner = spec["phases"][0]["hacd_lots"]
    public = spec["phases"][1]["hacd_lots"]
    phase_sum = partner + public

    print(f"[CHECK] Phase lots: {partner} (partner) + {public} (public) = {phase_sum}")
    if phase_sum != lots:
        errors.append(f"Phase lot mismatch: {partner} + {public} = {phase_sum} ≠ {lots}")
    else:
        print(f"  ✓ PASS — phase lots sum to total\n")

    # ── Distribution check
    team_pct = spec["distribution"]["team_reserve_pct"]
    vc_pct = spec["distribution"]["vc_allocation_pct"]
    public_pct = spec["distribution"]["public_formation_pct"]

    print(f"[CHECK] Distribution: team={team_pct}%, vc={vc_pct}%, public={public_pct}%")
    if team_pct + vc_pct + public_pct != 100:
        errors.append("Distribution percentages do not sum to 100")
    else:
        print(f"  ✓ PASS — distribution sums to 100%\n")

    # ── Validator status
    declared_status = spec.get("validator_status", "UNKNOWN")
    declared_errors = spec.get("validator_checks", {}).get("errors", -1)

    print(f"[CHECK] Declared validator status: {declared_status}")
    if declared_status == "PASS" and declared_errors == 0:
        print(f"  ✓ PASS — validator status consistent\n")
    else:
        warnings.append("Validator status or error count may need review")

    # ── Items needing confirmation
    pending = spec.get("items_needs_confirmation", [])
    if pending:
        print(f"[WARN] {len(pending)} items need issuer confirmation before launch:")
        for item in pending:
            print(f"  ⚠  {item}")
            warnings.append(f"Needs confirmation: {item}")
        print()

    # ── Final result
    print(f"{'='*60}")
    if errors:
        print(f"  RESULT: ❌ FAIL — {len(errors)} error(s), {len(warnings)} warning(s)")
        for e in errors:
            print(f"  ERROR: {e}")
    else:
        print(f"  RESULT: ✅ PASS — 0 errors, {len(warnings)} warning(s)")

    print(f"{'='*60}\n")

    if strict and warnings:
        print(f"Strict mode: {len(warnings)} warnings treated as errors.")
        sys.exit(1)

    if errors:
        sys.exit(1)
    else:
        print("Ready for HACD Labs submission: https://hacd.it/incubator")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate HACD launch_spec.json")
    parser.add_argument("spec", help="Path to launch_spec.json")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    args = parser.parse_args()
    validate(args.spec, strict=args.strict)
