---
name: hacd-ai-issuance-skill
description: >-
  Designs, verifies, and packages Hacash Stack Asset configurations and
  cohort submissions for the Hacash Labs Incubator.
---

# Hacash Stack Asset AI Issuance Skill

## Overview
This skill provides a structured workflow for configuring, mathematically validating, and packaging Hacash L1 Stack Asset configurations and cohort documentation.

## Dependencies
None.

## Quick Start
To validate a stack launch spec file:
```bash
python3 proofd/validate_launch_spec.py proofd/launch_spec.json --strict
```

## Workflow

### 1. Specification Engineering
1. Create a `launch_spec.json` following the official schema.
2. Verify parameters satisfy the mathematical constraints:
   - `total_hacd_lots` * `units_per_hacd_lot` = `total_prf_supply`
   - `total_hacd_lots` * `stack_cost_hac_per_hacd` = `total_formation_cost_hac`
   - VC and team allocations must be `0` (fair launch).

### 2. Cohort Refactoring (Economic Slashing Model)
Ensure all documents align with the economic liability architecture:
1. `stack_design.md`: Document the escrow mechanism, slashing consensus triggers, and the 90-day Penalty Pool freeze.
2. `issuer_faq.md`: Answer questions regarding staking risk, de-bonding delays, and PRF utility.
3. `project_profile.md`: Outline registration metadata.
4. `incubator_fit_review.md`: Complete Hacash technical feasibility fit scores.

### 3. Interactive Web3 Portal Verification
Prototype landing pages (`index.html`) featuring:
1. Web3 wallet injection (`window.ethereum` and `window.injectedWeb3`).
2. Client-side fetching to Hacash RPC node (`nodeapi.hacash.org`) to load account assets and diamond counts.
3. Extension-approved signing requests to sign stack authorization payloads.

## Common Mistakes
1. **Redirecting Actions Externally:** Landing page action buttons should trigger local wallet/modal flows directly instead of redirecting to `hacd.it`.
2. **Mock Wallet Fallbacks:** Always implement simulated sandbox mock fallbacks for review agents who do not have wallet extensions installed.
