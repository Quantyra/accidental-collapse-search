# Review of P011 v0.4.0: proof-adversarial check, focused on Section 6

**Source SHA-256 (as supplied):** `af58f74bbc841d7d3e5769f4545919652a2c24272a160e369814c846ced8f6de`
I did not recompute this hash. Per the packet constraints I ran no commands and read only the supplied material. This is an AI review. It is not human peer review or kernel/formal validation.

**Verdict: GO-WITH-NOTES.** I found no error in the theorem, its proof, or its constants. The notes below are about typesetting, notation, compilation bookkeeping, and optional exposition.

---

## 1. Section 6 core: gate insertion, metric, powers

**Common-cut phase metric (§6.2).** I checked the identity d_κ(A,B) = min_{|z_h|=1} ‖X − diag(z_h)Y‖₂.
- Expanding gives Σ(p_h+q_h) − 2Σ√(p_h q_h)|⟨u_h,v_h⟩|^{κ(h)} at the optimal phases, which equals 2 − 2F_κ because both distributions are normalized.
- Composing the two optimal phase maps and applying the Euclidean triangle inequality gives the metric triangle inequality.
- It is only a pseudometric modulo block phases. That is all the proof uses, and the paper correctly restricts triangles to one cut with identical block spaces.

**Gate charge (`eq:gate-charge`).** All steps hold:
- 2(1−s_h) = 2 − 2|⟨Uu,Vu⟩| ≤ 2 − 2Re⟨Uu,Vu⟩ = ‖Uu−Vu‖² ≤ δ_j².
- 1 − s^k ≤ k(1−s).
- Halted leaves have s_h = 1.
- Therefore d² = 2Σ_active p_h(1−s_h^{κ}) ≤ Kδ_j² Σ_active p_h ≤ Kδ_j².
- The normalized-mass point is correct and essential. With unweighted per-history charges, the bound would scale with the number of histories.

**Insertion (`eq:gate-insertion`).** The chain is d(A^U,B^V) ≤ d(A^U,A^V) + d(A^V,B^V). The last term equals d(A,B) because V_h^{⊗κ} is a common blockwise isometry. A gate does not change p(h), so κ is the same before and after it. Correct.

**Fixed and decreasing powers.** Both are reused from `lem:fixed` and `eq:decreasing`. Those lemmas are pairwise statements for arbitrary normalized u, v under common projectors, so they apply to the A-vs-B comparison (same oracle, same controller) as well as the oracle-vs-oracle comparison. The exact queries are common unitaries. The two potentials are kept separate, and I found no step that mixes exponents.

**Terminal transfer.** The chain TV ≤ √(1−A_T²) ≤ √(2−2A_T) ≤ d_κ holds, using (1−A)(1+A) ≤ 2(1−A). Projecting to the visible record can only decrease TV. **Correct, constant one.**

**Falsifiers attempted (none succeeded):**
1. *Single-qubit leak, ε=0.* Rotation θ followed by P samples gives TV ≈ min(1, Pθ²). This stays below √(P+1)·θ throughout and saturates near θ ~ 1/√P. This is consistent with the theorem, and the √K threshold is sharp.
2. *Protected-register leak with ε>0.* The perturbation is stored in D. Each round weakly couples D→S at angle β, samples S, and uncomputes. A collapse on S=0 damps D's leak amplitude only by cos β. Summing gives detection ≈ θ² sin²β / (1−cos^{2ε}β) → θ²/ε. This matches K = ⌈1/ε⌉ exactly in the quadratic regime and does not exceed the bound. This was my strongest attempt to exploit "collapse ≠ reset" (Remark), and the fixed power absorbs it.
3. *Coherent accumulation over G gates, then P samples.* TV ≈ P(Gδ)², which is below √(P+1)·Gδ while small.
4. *Unequal stopping and feedback.* Alignment is by ordinal gate count. Matching histories select identical operations, and halted leaves are carried with s = 1. I found no double counting or missing mass.

## 2. Rare-branch exact calculation (`eq:rare-precision`)

I verified this independently.
- v = c cos φ|00⟩ + a|10⟩ + c sin φ|11⟩, and ‖R_φ − I‖ = |e^{iφ}−1| = 2 sin(φ/2).
- With L ∈ {1,…,m} and Pr[L>j] = (1−ε)^j, the all-zero mass is q t^L = a² t^{L−1} ≤ a² for each flag sequence.
- The halt mass satisfies c² cos²φ ≤ c², and total perturbed mass is 1.
- The tail identity 1 − E t^L = (1−t) Σ_{j<m} Pr[L>j] t^j and q(1−t) = b² give the displayed formula exactly.
- Bound: the sum is ≤ min{m, 1/ε} ≤ K_ε(m), and b² ≤ sin²φ = d² cos²(φ/2) ≤ d². Finally, min{1, Kd²} ≤ √K·d holds in both cases.
- At a = 0 the formula gives b², which matches direct computation.

**Optional exposition:** With t → 1 and ε = 0, this family gives TV ≈ m c² sin²φ ≈ K·d². So it also shows that the K factor is attained in the quadratic regime, which makes the √K constant-TV threshold sharp. The paper presents the family only as a no-inverse-probability diagnostic. A single sentence noting the sharpness would strengthen it. Nonblocking.

## 3. Rate coupling and budgets (`eq:rate-precision` – `eq:precision-budget`)

- **Rate coupling.** Flags are coupled maximally, with per-call mismatch ≤ |ε−ε̂| ≤ τ regardless of adaptivity, over at most P calls. Born draws and actions agree until the first mismatch. The bound 1 − (1−τ)^P ≤ Pτ is correct.
- **Combined bound.** The triangle through B_ε correctly uses K_ε(P) at A's rate.
- **Budget.** √K·G·δ ≤ ζ/2 and Pτ ≤ ζ/2. Also 2^H ≥ 2^{J/2} ≥ √K, so 2^{−b_g} ≤ ζ/(2G√K). Correct.
- **Success.** 3/4 − 1/12 = 2/3. Hoeffding gives exp(−2·27·(1/6)²) = e^{−1.5} ≈ 0.223 < 1/4, and a failed majority requires ≤ 13/27 < 1/2 correct. Correct.

## 4. Dependencies rechecked (Sections 3–5)

All constants check out:
- **Section 3.** 2 − √3 ≈ 0.268 > 1/4. (N−6)/4 ≥ N/8 for N ≥ 12. 4Q²k ≥ N/8 gives N/32. Q ≥ √(εN)/8. Q²(P+1) ≤ 2(Q+P)³ gives N^{1/3}/4. For small N, 12^{1/3} + √12 ≈ 5.75 < 6.
- **Section 4.** 4π² ≤ 40. 2t+1 ≥ m/4. (2t+1)θ ≤ 1 + 2/√N' < π/2. 1/3280 and e^{−4} < 1/12. Br·η ≤ 1/24.
- **Section 4.4 branching check.** g₁ = 18/25, g₂ = 82/125, 412/625 ≥ 400/625, 84/125 ≥ 64/125. I re-derived the frontier formulas from the instrument.
- **Section 5.** The spectral charge and the normalization `eq:adv-history-normalization` hold. c_* ≈ 0.02860 > 1/36 ≈ 0.02778, and 2√2/3 < 17/18. The stopping check values (1 → 1/4, mass 3/8, charge 3/4) are exact. The η-replacement of c_* is (1 − 2√(η(1−η)))/2, which recovers β at η = 1/3.

## 5. Findings

| # | Severity | Location | Finding |
|---|---|---|---|
| F1 | Low (typesetting; verify) | `eq:gate-charge`, both `\sum_{h\ {…m active}}` | The packet shows a line break where `\rm` is expected (`{` newline `m active}`). This is consistent with `\r` being turned into a carriage return. If the source really contains this, TeX renders italic "mactive". Other `\r…` macros (`\rangle`, `\rvert`, `\raggedright`) look intact, so this may be a packet artifact. Check the PDF and the byte-level source. |
| F2 | Low (notation) | §6 vs `lem:projection`, §4.2, §6.4 ledger | **A, B** denote implementations in §6. Elsewhere, A is the affinity in the Lemma, B = 13120 attempts in §4.2, and B is the transcript-length bound in the §6.4 ledger. **d** denotes the Bures distance, the rotation norm in `eq:rare-precision`, and the local dimension in §6.4. Each is locally defined, but renaming (e.g. 𝒜, ℬ; ℓ for transcript length) would help. |
| F3 | Low (compilation bookkeeping) | §6.4, "entry accuracy δ/(4d) contributes at most δ/4" | The Frobenius bound gives d·δ/(4d) only if "entry accuracy" means the complex modulus. If it means real and imaginary parts separately, the bound becomes √2·δ/4. Also, the rounded matrix is not unitary. Polar unitarization costs at most another δ/4 (since ‖W−Ũ‖ ≤ ‖U−Ũ‖), which leaves ≤ δ/2 for synthesis. That fits within the "remaining" 3δ/4, but the paper should state it explicitly. |
| F4 | Optional (strengthening) | `eq:gate-contract`, `eq:gate-charge` | The proof uses only s_h = \|⟨U_h u, V_h u⟩\|, so the contract can be weakened to min_θ ‖U_h − e^{iθ}V_h‖. A history-selected gate acts on the whole conditional state, so its global phase is harmless. The existing SU(d) caution about controlled gates remains correct. Similarly, d² ≤ Σ_h p_h κ(h) δ_h² permits history-dependent, mass-averaged errors. Nonblocking. |
| F5 | Optional (exposition) | `eq:rare-precision` | Note that this family also attains the Kd² scale (§2 above). Nonblocking. |
| F6 | Low (public README, not manuscript) | README "Archiving" | The sentence "Fresh three-provider AI review has no unresolved blocker; document, metadata and clean-build checks pass" follows the v0.4.0 plan. It can be read as a v0.4.0 claim, which would conflict with the header's "fresh review in progress". Scope it explicitly to v0.3.0. |

I found no Medium or High findings. Claim scope is consistent across the abstract, Theorem `thm:precision`, SOURCES, and the metadata: auxiliary consequence, no first-continuity claim, no physical-noise claim, and the cited ABFL Appendix D, Çakan et al. Claim 8.3, and Dawson–Nielsen are acknowledged. I did not verify the external citations. I did not use or invent any references.

**Recommendation: GO-WITH-NOTES.** Fix F1 if it is real and F6. F2 and F3 are advisable. F4 and F5 are optional.
