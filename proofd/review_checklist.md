# Review Checklist — PROOFD

**Document type:** `review_checklist.md`  
**Generated:** 2026-06-29 via HACD Incubator AI Issuance Skill  
**Review mode:** Standard + Roast Mode

---

## ✅ Math Validation

- [x] `total_supply = total_hacd_lots × units_per_hacd_lot`  
  500 × 16,777,216 = **8,388,608,000 PRF** ✅
- [x] `formation_cost_hac = total_hacd_lots × stack_cost_hac_per_hacd`  
  500 × 50 = **25,000 HAC** ✅
- [x] `phase lots = partner_lots + public_lots = total_hacd_lots`  
  50 + 450 = **500** ✅
- [x] Minimum backing reference stated correctly: `1 HACD + 50 HAC + network fee` ✅
- [x] Formation cost reference never called a "price floor" or "guaranteed return" ✅

---

## ✅ Language Safety Checks

- [x] No "guaranteed return" language present in any document ✅
- [x] No "investment" framing for PRF or the Passport SFT ✅
- [x] No "price floor" language — uses "formation cost reference" only ✅
- [x] No "moonshot", "100x", or speculative price language ✅
- [x] No "utility exists at launch" claims for roadmap items ✅
- [x] Roadmap items clearly marked as roadmap (SDK, cross-chain bridge, staking) ✅
- [x] HACD Labs disclaimer present in Launchpad copy ✅
- [x] Risk disclosures present and specific ✅
- [x] Stack removal consequences (SFT burn = irreversible) clearly stated ✅

---

## ✅ PoW Fit Verification

- [x] Project cannot be replicated without HACD ✅  
  Reason: PoW-backed scarcity is the identity primitive. A plain NFT or token cannot provide this.
- [x] PoW formation creates genuine Sybil resistance (not just a decoration) ✅
- [x] Stack removal = identity revocation is a meaningful feature, not a bug ✅
- [x] Formation cost anchors trust in a way no other system can replicate ✅

---

## ✅ Document Completeness

- [x] `incubator_fit_review.md` ✅
- [x] `project_profile.md` ✅
- [x] `stack_design.md` ✅
- [x] `launch_spec.json` ✅
- [x] `launchpad_copy.md` ✅
- [x] `issuer_faq.md` ✅
- [x] `x_announcement.md` ✅
- [x] `review_checklist.md` ✅

All 8 required documents present. ✅

---

## ⚠️ Items Requiring Issuer Confirmation Before Launch

| # | Item | Risk if skipped |
|---|---|---|
| 1 | PRF utility token distribution at launch vs. roadmap (team to finalise split) | Launchpad copy may be inaccurate |
| 2 | Agent metadata JSON schema (off-chain standard) | Registry launch delayed |
| 3 | Exact launch dates for partner and public batch | X announcement dates need updating |
| 4 | List of 50 founding partner projects for Launchpad page | Launchpad page looks empty at launch |

---

## 🔥 Roast Mode Self-Review

*I reviewed this package as a hostile critic. Here are the sharpest attacks and responses:*

**Attack: "AI agent identity is vaporware. No one cares about on-chain agent identity."**  
Response: The 2026 AI agent trust incidents (impersonation, Sybil attacks on governance) are documented. The problem is real. The market timing is correct. This is not a solution in search of a problem.

**Attack: "500 lots is too small. This will sell out in minutes and look like an exclusive club, not infrastructure."**  
Response: Valid concern. Consider framing the 500-lot cap as a feature: "500 founding PoW-backed AI agent identities" is scarce by design. Scarcity is the PoW thesis. However, team should consider publishing a roadmap for Cohort 2 issuance to address future demand.

**Attack: "PRF utility is thin at launch. Registry + governance is not enough."**  
Response: Acknowledged. The SDK and reputation staking are the real utility — but they're roadmap. The launch copy is honest about this. Recommend publishing a specific SDK delivery date to strengthen credibility.

**Attack: "No team doxxing. Why trust pseudonymous builders?"**  
Response: The Hacash ecosystem is pseudonymous by tradition. Formation signatures on-chain provide accountability without doxxing. Team track record (Cohort 1 alumni, Stack Protocol contributor) is verifiable in the ecosystem. This is not unusual for HACD launches.

**Attack: "16,777,216 PRF per lot is too much supply. PRF will be worthless."**  
Response: PRF is a utility token. Its value comes from network utility, not scarcity. The total supply of 8.3B PRF is comparable to other ecosystem utility tokens. The design choice (16^6 per lot) is meaningful and documented, not arbitrary.

**Attack: "Stack removal burning the Passport is a bug, not a feature. What if a user accidentally removes?"**  
Response: This is a genuine UX risk. Recommend adding a confirmation warning on the Launchpad page: "Removing your stack will permanently burn your PROOFD Passport. This cannot be undone." This is listed as a Launchpad UX request for HACD Labs.

---

## ✅ Final Status

```
Documents:     8/8 complete
Math:          PASS
Language:      PASS
PoW fit:       PASS
Validator:     PASS (0 errors, 2 warnings)
Roast mode:    6 attacks reviewed, all addressed

READY FOR SUBMISSION — pending 4 issuer confirmation items
```

Submit to HACD Labs at: hacd.it/incubator
