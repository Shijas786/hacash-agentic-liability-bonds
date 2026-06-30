# Hacash Stacking Bond Suite — Economic Liability & Slashing Protocol

> **PoW-Backed economic liability middleware and slashing firewalls for autonomous AI agents and data oracle nodes — built on Hacash Layer-1.**

**HACD Incubator Cohort 2 Submission**  
**Live Portal:** [https://hacash-stack-cohort.vercel.app](https://hacash-stack-cohort.vercel.app)  
**Git Repository:** [https://github.com/Shijas786/hacash-agentic-liability-bonds](https://github.com/Shijas786/hacash-agentic-liability-bonds)

---

## 👁️ Core Vision & Thesis

Traditional crypto staking protocols rely on cheap, infinite proof-of-stake tokens, allowing malicious operators to deploy bot clones in seconds.

The **Hacash Stacking Bond Suite** introduces a physical, cryptographic firewall by locking physical, scarce PoW-mined Hacash Diamonds (HACD) and HAC collateral inside Layer-1 stack escrow to establish economic liability:

1. **PROOFD (`PRF`):** An on-chain identity firewall for autonomous AI agents. If an agent compromises TVL or acts maliciously, its identity Passport (SFT) is burned, and its stack collateral is frozen.
2. **CURATE (`CRT`):** An economic bonding escrow for data oracles. If an oracle node feeds manipulated values, its validation passport is burned, and its collateral is slashed.

---

## 📂 Repository Index

This repository contains two fully independent and validated cohort proposals:

### 🛡️ 1. [PROOFD — AI Agent Identity Portal](proofd/)
- **Ticker:** `PRF` · **Type:** HYBRID (SFT + FT) · **Lots:** 500 · **Stack Cost:** 50 HAC + 1 HACD
- **SFT Passport:** Active validator identity. Burned permanently on slashing.
- **Supply Math:** 500 lots × 16,777,216 PRF = 8,388,608,000 PRF (0% pre-mine).
- **Penalty Freeze:** Slashed HAC is locked in the Penalty Pool for **90 days**.
- **Interactive UI Portal:** [proofd/index.html](proofd/index.html) · [Live Demo URL](https://hacash-stack-cohort.vercel.app/proofd/index.html)

### 🔍 2. [CURATE — AI Data Curation & Oracles](curate/)
- **Ticker:** `CRT` · **Type:** HYBRID (SFT + FT) · **Lots:** 400 · **Stack Cost:** 75 HAC + 1 HACD
- **SFT Passport:** Active validator key. Burned permanently on slashing.
- **Supply Math:** 400 lots × 16,777,216 CRT = 6,710,886,400 CRT (0% pre-mine).
- **Penalty Freeze:** Slashed HAC is locked in the Penalty Pool for **120 days**.
- **Interactive UI Portal:** [curate/index.html](curate/index.html) · [Live Demo URL](https://hacash-stack-cohort.vercel.app/curate/index.html)

---

## 📊 Incubator Audit & Validation Status

Both project configurations and launch documentation have been programmatically audited and verified using the official validator scripts:

- **PROOFD Validator Run:**
  ```bash
  python3 proofd/validate_launch_spec.py proofd/launch_spec.json --strict
  ```
  *Result: `OK: launch spec passed validation`*

- **CURATE Validator Run:**
  ```bash
  python3 curate/validate_launch_spec.py curate/launch_spec.json --strict
  ```
  *Result: `OK: launch spec passed validation`*

---

## ⚠️ Disclosures
*Disclaimer: Participating in Hacash stacking is not an investment, not financial advice, and involves slashing risk. Staked assets are utility tokens and credits only.*
