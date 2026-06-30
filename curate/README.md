# CURATE — PoW-Backed Economic Bonding & Slashing for AI Data Oracles

> **Decentralized economic liability middleware for oracle nodes and data curators — built on Hacash Stack Asset Protocol.**

**HACD Incubator Cohort 2 Submission**  
**Ticker:** `CRT` · **Type:** HYBRID (SFT + FT) · **Lots:** 400 · **Stack Cost:** 75 HAC + 1 HACD

---

## 👁️ Core Vision

Decentralized oracles feed data into smart contracts and AI agents. However, data curators are vulnerable to false submissions and security bribes because **there are no financial penalties for malicious oracles.**

**CURATE solves this using Hacash's physical scarcity:**
- **Oracle Collateral Bond:** To register an active API node, operators must stack **75 HAC** and **1 HACD** into escrow.
- **On-Chain Slashing:** If an oracle node submits false inputs (deviating from validator consensus), its CURATE Passport SFT is burned on-chain.
- **Penalty Pool Lock:** The 75 HAC collateral is immediately frozen inside the Hacash **Penalty Pool for 120 days**, punishing the operator's capital.

---

## 📂 Repository File Index

All required cohort files are generated and linked below:

| # | File Name | Purpose | Status |
|---|---|---|---|
| 1 | [**`launch_spec.json`**](launch_spec.json) | On-chain stacking protocol parameters | **✅ VALIDATED (0 errors, 0 warnings)** |
| 2 | [**`project_profile.md`**](project_profile.md) | Incubator registry profile and metrics | **✅ COMPLETE** |
| 3 | [**`stack_design.md`**](stack_design.md) | Escrow structure, slashing triggers, and 120-day locks | **✅ COMPLETE** |
| 4 | [**`incubator_fit_review.md`**](incubator_fit_review.md) | Review of Hacash L1 technical fit (Score: **96/100**) | **✅ COMPLETE** |
| 5 | [**`issuer_faq.md`**](issuer_faq.md) | Economic and technical oracle queries FAQ | **✅ COMPLETE** |
| 6 | [**`launchpad_copy.md`**](launchpad_copy.md) | Launchpad copy and main features | **✅ COMPLETE** |
| 7 | [**`x_announcement.md`**](x_announcement.md) | Social media drafts and posting sequence | **✅ COMPLETE** |
| 8 | [**`review_checklist.md`**](review_checklist.md) | Quality checks and self-audit confirmations | **✅ COMPLETE** |

---

## 📊 Economic Specifications

- **Total HACD Lots:** 400 lots
- **Collateral Stack Cost:** 75 HAC per lot
- **Total locked HAC:** 30,000 HAC in escrow
- **Units per Lot:** 16,777,216 CRT
- **Total Supply:** 6,710,886,400 CRT
- **Team Allocation / Pre-Mine:** 0% (100% fair launch)

To run validation checks locally:
```bash
python3 validate_launch_spec.py launch_spec.json --strict
```

---

## ⚠️ Disclosures

*Disclaimer: This project and its tokens are utility credits. Participating in stacking is not an investment, not financial advice, and involves slashing risk.*
