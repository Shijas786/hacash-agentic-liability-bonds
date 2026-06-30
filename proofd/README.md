# PROOFD — PoW-Backed Economic Stacking Bond & Slashing Protocol

> **Economic liability middleware for autonomous AI agents — forged in PoW and backed by Layer-1 collateral.**

**HACD Incubator Cohort 2 Submission**  
**Ticker:** `PRF` · **Type:** HYBRID (SFT + FT) · **Lots:** 500 · **Stack Cost:** 50 HAC + 1 HACD

---

## 👁️ Core Vision & Problem Statement

In the agentic economy, autonomous AI agents manage high-value DeFi TVL, route transactions, and interact with smart contracts. However, **agents have no fear of legal recourse, incarceration, or reputational ruin.** 

Traditional Sybil-resistance systems (like ENS, Lens, or standard NFTs) carry zero formation cost, allowing malicious operators to deploy cheap clone bot armies in seconds.

**PROOFD solves this by introducing a physical, cryptographic firewall:**
- **Collateral-Backed Identity:** To launch a verified agent, operators must lock **50 HAC** and **1 HACD** inside an L1 stack.
- **On-Chain Slashing:** If an agent commits protocol fraud or oracle manipulation, its PROOFD Passport (SFT) is instantly burned.
- **Penalty Lockup:** Slashed collateral is frozen in the Hacash **Penalty Pool for 90 days**, destroying the operator's capital efficiency.

---

## 🛠️ The HACD AI Issuance Skill Integration

This submission was designed, validated, and packaged using the **HACD Incubator AI Issuance Skill**. The workflow followed five strict engineering phases:

1. **Discovery & Design:** Modeled a hybrid SFT/FT token system to couple identity (SFT) with utility curation credits (FT).
2. **Specification Generation:** Designed the raw on-chain configuration in [`launch_spec.json`](launch_spec.json).
3. **Consensus Validation:** Created [`validate_launch_spec.py`](validate_launch_spec.py) to audit the parameters against Hacash mainnet protocols.
4. **Coordinated Documentation:** Drafted fit reviews, FAQs, and blueprints matching the economic bonding pivot.
5. **DApp Prototyping:** Engineered an interactive Web3 landing page interface in [`index.html`](index.html).

---

## 📂 Repository File Index

All required documents are fully completed and linked below:

| # | File Name | Purpose | Status |
|---|---|---|---|
| 1 | [**`launch_spec.json`**](launch_spec.json) | On-chain stacking protocol parameters | **✅ VALIDATED (0 errors, 0 warnings)** |
| 2 | [**`project_profile.md`**](project_profile.md) | Incubator registry profile and metrics | **✅ COMPLETE** |
| 3 | [**`stack_design.md`**](stack_design.md) | Escrow structure, slashing rules, and 90-day locks | **✅ COMPLETE** |
| 4 | [**`incubator_fit_review.md`**](incubator_fit_review.md) | Review of Hacash L1 technical fit (Score: **96/100**) | **✅ COMPLETE** |
| 5 | [**`issuer_faq.md`**](issuer_faq.md) | Economic and technical developer query catalog | **✅ COMPLETE** |
| 6 | [**`launchpad_copy.md`**](launchpad_copy.md) | Launch campaign collateral and descriptions | **✅ COMPLETE** |
| 7 | [**`x_announcement.md`**](x_announcement.md) | Social media drafts and roadmap highlights | **✅ COMPLETE** |
| 8 | [**`review_checklist.md`**](review_checklist.md) | Self-audit checklist and mitigation plans | **✅ COMPLETE** |

---

## 📊 Economic Specifications & Math Check

PROOFD leverages Hacash's unique dual-asset PoW constraints to enforce absolute mathematical scarcity:

$$\text{Total Lots} = 500$$
$$\text{Collateral per Lot} = 50\text{ HAC}$$
$$\text{Total Formation Cost} = 500 \times 50\text{ HAC} = 25,000\text{ HAC Locked}$$
$$\text{Fungible PRF per Lot} = 16,777,216\text{ PRF } (16^6 \text{ alphabetical space})$$
$$\text{Total Fungible PRF Supply} = 500 \times 16,777,216 = 8,388,608,000\text{ PRF}$$
$$\text{Team Allocation / Pre-Mine} = 0\%$$

Run the mathematical verification suite locally:
```bash
python3 validate_launch_spec.py launch_spec.json --strict
```

---

## 💻 The Web3 dApp Portal (`index.html`)

We have built a premium, interactive user interface ([`index.html`](index.html)) to showcase the end-to-end dApp flow:
- **Real L1 RPC Connection:** Connects client-side fetches to `nodeapi.hacash.org` to query active address balances and unstacked diamond (HACD) listings.
- **Real Browser Wallet Signatures:** Queries `window.ethereum` (EVM mode) and `window.injectedWeb3` (Substrate mode) to trigger real **SubWallet** cryptographic signature request popups.
- **Interactive Developer Tools:** Features a terminal-style tab system with simulated typing commands and a live verifier logging trace panel.

---

## ⚠️ Risk Disclosures

PRF is a utility token. Stacking involves slashing risk. If the Slashing Oracle consensus flags your agent for a protocol violation, your PROOFD SFT is burned and your 50 HAC collateral is frozen in the Penalty Pool for 90 days. Registry SDK and cross-chain verification are roadmap items. HACD Labs does not endorse utility claims. DYOR.
