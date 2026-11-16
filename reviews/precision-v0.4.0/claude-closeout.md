# Re-review of P011 v0.4.0: proof-adversarial closeout, focused on Section 6

**Source SHA-256 (as supplied):** `42f8f7b25ee045d3412440095c3c8719dc380c627aa687b976f03142eec87769`

I did not recompute this hash. I ran no commands, read nothing outside the packet and edited nothing. This is an AI review only. It is not human peer review and not kernel or formal validation.

**Verdict: GO-WITH-NOTES.** Coordinator changes 1–8 meet the mathematical and resource contracts. I found no Medium or High issue. The three remaining notes are Low or optional and do not block release.

---

## 1. Verification of the coordinator changes

**Changes 1–2 (typesetting and notation).**
- `eq:gate-charge` now uses `\mathrm{active}` in both subscripts.
- §6.4 uses `B_{\mathrm{tr}}` and `d_{\mathrm{loc}}`. These no longer clash with B=13120 in §4.2 or with d in `eq:rare-precision`.
- Resolved.

**Change 6 (whole-operator scalar phase), `eq:gate-contract`.** I checked every place the contract is used.
- *Gate charge.* If ‖U_h − e^{iθ_h}V_h‖ ≤ δ_j, then ‖U_h u − e^{iθ_h}V_h u‖² ≥ 2(1 − |⟨U_h u, V_h u⟩|). The bound on s_h therefore holds with the actual V_h.
- *Insertion.* Applying V_h or e^{iθ_h}V_h on both sides changes each block by a phase. d_κ minimizes over block phases, so `eq:gate-insertion` is unchanged.
- *History dependence.* Choosing θ_h separately for each history is legitimate. Each block is a separate conditional pure state, and no coherent superposition across histories exists in Σ.
- *Controlled gates.* Requiring the phase to be global on the full history-selected operator, including its controls, is the correct restriction. A relative phase between control sectors changes s_h and would not be harmless.
- *SU(d) synthesis.* The paper's sentence on synthesizing in SU(d_loc) is consistent with this. A phase on the local factor tensored with the identity is a global phase of the whole step operator, because each index j is one gate step.
- Resolved.

**Changes 3 and 7 (entry accuracy, polar step, bit split).** I rechecked each constant.
- *Real/imaginary split.* Accuracy δ/(8d_loc) on each part gives complex modulus ≤ √2·δ/(8d_loc) < δ/(4d_loc).
- *Entrywise to operator norm.* ‖·‖_op ≤ ‖·‖_F ≤ d_loc · max-entry, which gives ≤ δ/4.
- *Bits for the matrix entries.* 2^{−(b_g+c_d)} = δ·2^{−c_d} ≤ δ/(8d_loc) because c_d = ⌈log₂(8d_loc)⌉.
- *Polar step.* By Weyl, |σ_i(W) − 1| ≤ ‖W − U‖ ≤ δ/4. Then ‖U_pol − W‖ = max_i |σ_i − 1| ≤ δ/4, so ‖U_pol − U‖ ≤ δ/2.
- *Polar precondition.* The condition δ/4 < 1 holds because b_g ≥ 1 whenever G ≥ 1 and ζ < 1, so δ ≤ 1/2.
- *Remaining budget.* Numerical polar error δ/4 plus synthesis error δ/4 complete δ. Setting b_syn = b_g + 2 gives exactly 2^{−b_syn} = δ/4.
- *Ledger.* Every compiler term (L, S, M_S, a) uses b_syn. The evaluation terms use b_g + c_d. This is consistent.
- Resolved.

**Change 8 (ancilla reuse).** Synthesis ancillas are reused serially, returned clean, and cleanup is included in S, L and a. The quantum-space term w + a(b_syn) is therefore valid. A clean ancilla is a known zero preparation and a common isometry, so it is covered by the nonquery comparisons in §3.1. Resolved.

**Zero-cap convention.** With G=0, the theorem gives TV=0 and b_g is set to 0. With P=0, K=1, so J=H=0 and b_ε=0. With exact rate, the gate allocation can be ζ/(G√K). All consistent.

## 2. Attempted falsifiers (none succeeded)

1. **History-dependent phase representative used to hide a relative control phase.** Take a controlled-V where only the target branch carries e^{iθ}. Choosing the representative per history cannot cancel this, because the phase is not scalar on the whole operator. The contract then correctly forces δ_j ≳ |e^{iθ} − 1|. Rejected as a loophole.
2. **Rounded matrix nearly singular.** This would need ‖W − U‖ ≥ 1, but the budget gives at most 1/8. The polar step is well defined.
3. **Real/imaginary rounding against a complex-modulus contract.** The √2 factor is absorbed by the 8 versus 4 in the denominators, as computed above.
4. **Charging ancilla space per gate.** Serial clean reuse gives a(b_syn), not G·a(b_syn). A dirty-ancilla variant would break the common-isometry argument, and the paper excludes it.
5. **Rate coupling, fixed/decreasing powers, rare-branch formula, terminal TV ≤ d_κ, budget and the 27-repetition Hoeffding bound.** These are unchanged from my initial report and recheck as before. In particular b²Σ_{j<m}((1−ε)t)^j ≤ min{1, K_ε(m)d²} ≤ √K·d, and exp(−27/18) ≈ 0.223 < 1/4.

Sections 3–5 are unchanged in substance. Their constants still hold: 2 − √3 > 1/4, N/32, 1/3280, e^{−4} < 1/12, and c_* ≈ 0.0286 > 1/36.

## 3. Remaining findings

| # | Severity | Location | Finding |
|---|---|---|---|
| N1 | Low (exposition) | §6.4, "Allow at most δ/4 for numerical polar approximation…" | The synthesis target must be an exact unitary, but the numerical polar output is only approximately unitary. The proof is fine if the two δ/4 allowances are read as one end-to-end certificate: ‖word − U_pol‖ ≤ δ/2, measured against the exact polar unitary. One clause stating this would remove the ambiguity. The ledger does not show the polar computation as a separate term. Saying it is included in S(b_syn) and M_S(b_syn) would match "charging both computations". |
| N2 | Low (resource) | §6.4, preparation-isometry dilation | The fixed-dimensional dilation ancillas belong to the codomain of the preparation isometry. Unlike synthesis ancillas, they are not returned clean. They should be counted in w, or stated as already counted there, rather than in a(b_syn). This changes space by at most O(1) per preparation register, so it is not a quantitative concern. |
| N3 | Optional | `eq:rare-precision` | Same as my earlier F5. This family also attains the K·d² scale, which shows the √K threshold is sharp. The coordinator deferred this deliberately, and I agree it is not needed. |

Earlier findings F1, F2, F3 and F6 are resolved. F4 is partially adopted as the whole-operator phase; mass-averaged history-dependent errors remain deferred, which is acceptable. I did not verify the external citations, and I introduced no new references.

**Recommendation: GO-WITH-NOTES.** N1 and N2 are one-sentence clarifications. N3 is optional.
