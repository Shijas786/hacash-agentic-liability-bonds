# Stack Token Design — PROOFD

**Document type:** `stack_design.md`  
**Generated:** 2026-06-29 via HACD Incubator AI Issuance Skill

---

## Asset Type

**HYBRID** — two-layer structure per HACD lot serving as an active security bond:

1. **PROOFD Passport** (SFT layer) — one per HACD lot. The AI agent's active liability credential. Non-transferable while stacked. If the agent violates protocol rules, this SFT is burned on-chain.
2. **PRF Utility Token** (FT layer) — 16,777,216 PRF per HACD lot. Transferable. Used for backing agent reputation, paying micro-fees for verifying agent bonds, and oracle curation.

This hybrid structure is the key innovation: the SFT is the collateralized identity that can be slashed, and the FT layer is the friction-reducing economic utility.

---

## Supply Math

```
total_hacd_lots         = 500
units_per_hacd_lot      = 16,777,216  (= 16^6, matches Hacash namespace)
total_prf_supply        = 500 × 16,777,216 = 8,388,608,000 PRF
stack_cost_hac_per_hacd = 50 HAC
total_formation_cost    = 500 × 50 = 25,000 HAC
```

**Math check: PASS** ✅

---

## HACD Lot Structure

| Batch | HACD Lots | Allocation | Access |
|---|---|---|---|
| Partner Batch | 50 | 10% | Reserved for 50 founding AI agent projects (DeFi, bridges, solvers) |
| Public Batch | 450 | 90% | Open on hacd.it/launchpad, first-come-first-served |
| **Total** | **500** | **100%** | |

**Phase lot check:** 50 + 450 = 500 ✅

---

## The Economic Security Bond (Collateral)

**Stack cost: 50 HAC + 1 HACD per Bond**

To activate an AI agent in high-value environments (e.g., executing cross-chain swaps, managing DAOs, operating Defi vaults), the operator must form a PROOFD Bond.
- **Deterrence:** While 50 HAC is a reasonable operating expense for a single legitimate agent, it makes Sybil flooding (e.g., 1,000 malicious agents) extremely expensive ($50,000+ in raw capital lockup).
- **Security Floor:** The bond ensures that every active agent has significant skin in the game. It represents a real financial deposit that can be penalized.

---

## Slashing Mechanics

PROOFD introduces a decentralized **Slashing Oracle** composed of a multi-sig network of Hacash nodes and verified AI agent frameworks.

### Slashing Triggers
An agent's bond can be slashed under three specific, verifiable conditions:
1. **Oracle Manipulation:** Injecting false data into decentralized oracle feeds.
2. **Execution Default:** Failing to deliver a routing or solver transaction after taking payment.
3. **Double-Spend/Frontrunning exploits:** Running hostile MEV/exploits against protocols they are integrated with.

### The Slashing Sequence
When a slash event is triggered on-chain:
1. The **PROOFD Passport SFT** is immediately burned, revoking the agent's identity.
2. The agent is blacklisted from the registry.
3. **The 50 HAC is locked in a Penalty Pool for a 90-day cooling period**, preventing the operator from redeeming or reclaiming their capital.
4. The HACD is locked inside the stack and cannot be unstacked or sold during this cooling period.

This 90-day capital freeze inflicts a massive opportunity cost and liquidity drain on malicious operators.

---

## Holder Rights and Utility

### PROOFD Passport (SFT) Holders:
- Certified as an **Economically Bonded AI Agent**.
- Eligible to handle TVL inside integrated DeFi protocols.
- Higher API rate-limits and fast-tracked transactions on partner networks.
- Stack removal (voluntary de-bonding) returns the 50 HAC and HACD instantly, provided no pending slash accusations exist.

### PRF Token (FT) Holders:
- Stake PRF to increase an agent's "Trust Index" score in the registry.
- Pay PRF micro-fees to query the Slasher contract for real-time agent trust audits.
- Curation voting on Slashing Oracle disputes.

---

## Token Distribution

| Allocation | PRF Amount | % |
|---|---|---|
| Public formation (all 500 lots) | 8,388,608,000 | 100% |
| No team reserve | 0 | 0% |
| No VC allocation | 0 | 0% |

**All PRF enters circulation through Stack formation only.** There is no pre-mine, no team allocation, and no VC round. The only way to receive PRF is to stack a HACD lot. This is the purity of PoW-native issuance.
