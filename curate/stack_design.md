# Stack Design: CURATE Economic Escrow & Slashing

## Escrow Parameters
- **Collateral Locker:** Hacash Layer-1 Stack Escrow Contract.
- **Required Inputs:** 1 HACD + 75 HAC per bonded oracle node.
- **Escrow Period:** Infinite (assets remain locked to keep the oracle validator passport active).
- **Graceful De-bonding:** Node operators can safely unlock and retrieve their 75 HAC + 1 HACD by initiating a 14-day de-bonding cooling cooling period.

## Slashing Mechanics
- **Oracle Consensus Monitoring:** A decentralized network of validator nodes continuously checks API data feed responses.
- **Slashing Trigger:** If an oracle node submits data feed inputs that deviate by >5% from consensus average (or fails uptime guarantees), a dispute is raised.
- **Slashing Execution:**
  - The CURATE Passport SFT is burned on-chain.
  - The 75 HAC collateral is immediately transferred from stack escrow to the **Hacash Penalty Pool**.
  - The collateral remains frozen inside the Penalty Pool for **120 days** before the owner can retrieve it, penalizing malicious behavior.

## Technical Specifications Check
- **total_supply:** 6,710,886,400 CRT
- **total_hacd_lots:** 400 lots
- **units_per_hacd_lot:** 16,777,216 CRT
- **stack_cost_hac_per_hacd:** 75 HAC
