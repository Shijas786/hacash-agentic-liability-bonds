# Issuer FAQ — PROOFD

**Document type:** `issuer_faq.md`  
**Generated:** 2026-06-29 via HACD Incubator AI Issuance Skill

---

## General Questions

**Q: What is PROOFD in one sentence?**  
A: PROOFD is a crypto-economic bonding and slashing protocol that locks HACD + HAC as a security bond for autonomous AI agents, ensuring agents face real financial penalties for malicious behavior.

**Q: Why does an AI agent need an economic bond?**  
A: Because autonomous agents transact millions in DeFi but carry zero legal or financial liability. If an agent executes an exploit or defaults on a trade, it loses nothing. Staking 50 HAC + 1 HACD locks a $2,500+ security bond. If the agent misbehaves, this bond is slashed, creating a massive economic penalty.

**Q: How is PROOFD different from ENS, Lens, or standard NFT staking?**  
A: Three ways: (1) Standard staking lacks physical scarcity; attackers can borrow tokens via flash loans to bypass limits. HACD is a PoW-mined asset with absolute scarcity. (2) PROOFD features an on-chain **slashing mechanic** that burns the agent's identity passport. (3) Slashing locks the stacked HAC collateral for a 90-day cooling freeze, imposing a severe capital drag on bad actors.

---

## Stacking and Bonding Questions

**Q: How do I form a security bond for my agent?**  
A: Go to hacd.it/launchpad during the public batch window. Select a HACD you own, stack 50 HAC onto it, and confirm. This transaction takes ~5 minutes. You will receive 1 PROOFD Passport (SFT) and 16,777,216 PRF utility tokens.

**Q: What do I need to stack?**  
A: You need (1) a Hacash wallet, (2) at least 1 HACD, and (3) 50 HAC. Up to 200 HACD lots can be processed in a single transaction.

**Q: What is "slashing"? How does it happen?**  
A: If an agent violates protocol rules (e.g. oracle manipulation, DeFi exploits, trade default), the decentralized **Slashing Oracle** triggers a slash. When this happens, the agent's PROOFD Passport SFT is burned, and the stacked 50 HAC is locked in a Penalty Pool for a 90-day cooling freeze.

**Q: How does the Slashing Oracle determine if an agent misbehaved?**  
A: The oracle is a consensus multi-sig operated by Hacash nodes and verified AI agent frameworks (e.g. ElizaOS, Virtuals). Slashing decisions require proof of transaction failure or protocol manipulation verified on-chain.

**Q: What if I want to remove my stack voluntarily?**  
A: If there are no pending slash disputes, you can de-bond your agent. This action returns your HACD and 50 HAC instantly, but permanently burns the PROOFD Passport SFT (revoking the agent's identity). The distributed PRF tokens remain in circulation.

---

## PRF Token Questions

**Q: What is PRF?**  
A: PRF is the economic utility token of the PROOFD protocol. Stakers receive 16,777,216 PRF per lot. It is used to pay for trust audits, back agent reputation index scores, and participate in slashing dispute curation.

**Q: Why 16,777,216 PRF per lot?**  
A: 16,777,216 = 16^6, the total possible unique HACD names. This locks the economic math of PRF directly to Hacash's namespace: each PRF token conceptually represents "one unit of the HACD namespace."

**Q: Is PRF a security?**  
A: No. PRF is a utility token with no guaranteed financial return. The 50 HAC stack cost is an on-chain collateral deposit — not a purchase price, price floor, or investment value.

---

## Registry and SDK Questions

**Q: What is the PROOFD Registry?**  
A: A searchable public registry showing all active, bonded, and slashed agents. DeFi protocols query this registry to check if an agent has an active, unslashed security bond before allowing it to transact.

**Q: How do developers integrate the PROOFD bond check?**  
A: An open-source SDK will be released 8 weeks post-launch, allowing DeFi contracts to check if an agent's calling wallet is associated with an active, unslashed PROOFD Passport SFT.

---

## Issuer Questions

**Q: Does the PROOFD team hold any PRF reserve or pre-mine?**  
A: No. There is no team reserve and no pre-mine. 100% of the PRF supply enters circulation through stack-bonding.

**Q: Who operates the 50 partner lots?**  
A: The 50 partner lots are reserved for founding AI agent frameworks and DeFi protocols to ensure early integration. The team holds zero lots.

**Q: How do I contact the PROOFD team?**  
A: X: @proofd_id · Discord: discord.gg/proofd · Submission Portal: hacd.it/incubator
