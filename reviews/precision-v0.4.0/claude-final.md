# Review of P011 v0.4.0 (revised): proof-adversarial check, focused on Section 6

**Source SHA-256 (as supplied):** `6542fb4a8bcfd1a84982b0cc2cc14cd4c5a49bdc71b903c1fcc39cd787c33e6d`. I did not recompute it. I ran no commands and read only the supplied packet. This is an AI review. It is not human peer review or kernel/formal validation. I re-derived the revised source independently rather than relying on my earlier report on `af58f74b…`.

**Verdict: GO-WITH-NOTES.** I found no error in Theorem `thm:precision`, its proof, the rare-branch calculation, the rate coupling, or the success transfer. The remaining notes concern one compilation-contract inconsistency (Low) and optional exposition.

---

## 1. Verification of the delta (Section 6)

### Common-cut phase metric (§6.2)
For X = ⊕√p_h u_h^{⊗κ(h)} and the analogous Y:
- ‖X − diag(z)Y‖² = 2 − 2Σ√(p_h q_h) Re(z̄_h⟨u_h,v_h⟩^κ).
- Optimal block phases give 2 − 2F_κ. This uses Σp_h = Σq_h = 1, which holds because halted leaves are retained.
- Composing the optimal phase maps and applying the Euclidean triangle inequality gives the triangle inequality on one cut with identical block spaces.

The paper restricts triangles to a single cut and uses scalar monotonicity across cuts. That restriction is necessary, and it is respected throughout.

### Gate charge (`eq:gate-charge`) and insertion (`eq:gate-insertion`)
- 2(1 − s_h) ≤ 2 − 2Re⟨Uu,Vu⟩ = ‖Uu − Vu‖² ≤ δ_j².
- 1 − s^k ≤ k(1 − s).
- A^U and A^V share the probabilities p_h, so d² = 2Σ_active p_h(1 − s_h^κ) ≤ Kδ_j².
- Halted leaves have s_h = 1.
- A gate does not change p(h), so κ is unchanged across it.
- Applying V_h^{⊗κ} on both sides is a common blockwise isometry, so d(A^V, B^V) = d(A, B).

The `\mathrm{active}` repair is purely typographic.

### Nonquery steps between gates
`lem:projection`, `lem:fixed` and `eq:decreasing` are pairwise statements for arbitrary normalized u, v under common projectors. They therefore apply to A versus B under the same exact oracle. Exact queries are common unitaries in this comparison, so they preserve F_κ exactly and incur no query charge.

The decreasing-power argument needs κ ≥ 1 on every formal branch. The contract imposes the cap P on formal extensions of zero-probability histories in both implementations, which supplies this.

### Terminal transfer
TV ≤ √(1 − A_T²) ≤ √(2 − 2A_T) ≤ d_κ, using F_κ ≤ A_T and (1 + A_T) ≤ 2. Projecting to the visible record cannot increase TV. The constant is 1.

### Rare-branch calculation (`eq:rare-precision`), re-derived
- The all-zero probability on the 1-branch is t^L. Per flag sequence, the perturbed mass is q·t^L = a²t^{L−1} ≤ a².
- The halt mass satisfies c²cos²φ ≤ c².
- Therefore TV equals the perturbed mass on transcripts containing a sampled one.
- The tail identity 1 − E t^L = (1 − t)Σ_{j<m}(1 − ε)^j t^j holds because Pr[L > 0] = 1. Combined with q(1 − t) = b², this gives the displayed sum exactly.
- The sum is at most min{m, 1/ε} ≤ K_ε(m).
- b² ≤ sin²φ = d²cos²(φ/2) ≤ d².
- min{1, Kd²} ≤ √K·d holds in both cases.

### Rate coupling (`eq:rate-precision`, `eq:combined-precision`)
- The per-call conditional mismatch is |ε − ε̂| ≤ τ under maximal coupling, whatever the adaptivity.
- Sequential conditioning over at most P calls gives Pr[no mismatch] ≥ (1 − τ)^P.
- Born draws have the same distribution for either flag value, so the states and actions coincide until the first mismatch.
- The combined bound is the triangle inequality through B at rate ε, with K evaluated at A's rate. This is correct.

### Budget and success
- 2^{−b_g} ≤ (ζ/2G)·2^{−H} ≤ ζ/(2G√K), since 2^H ≥ 2^{J/2} ≥ √K. For K = 1, J = H = 0.
- Using a certified lower bound ε_low gives k = ⌈1/ε_low⌉ ≥ ⌈1/ε⌉, which still satisfies εk ≥ 1, so it is valid.
- 3/4 − 1/12 = 2/3.
- Hoeffding: exp(−2·27·(1/6)²) = e^{−1.5} ≈ 0.223 < 1/4. The repeated ideal success is therefore at least 0.777 ≥ 3/4, so the chain closes.
- Majority failure requires at most 13 correct runs out of 27, a deviation of 5/27 > 1/6. This holds for search labels as well as for Boolean outputs.

### Revised compilation paragraph (former F3)
- Complex-modulus entry error δ/(4d_loc) gives operator norm ≤ Frobenius norm ≤ δ/4.
- Real and imaginary parts at δ/(8d_loc) give modulus ≤ √2·δ/(8d_loc) < δ/(4d_loc).
- 2^{−c_d} ≤ 1/(8d_loc).
- By Weyl's inequality, the singular values of W are within δ/4 of 1, so ‖U_pol − W‖ = max|σ_i − 1| ≤ δ/4. Hence ‖U_pol − U‖ ≤ δ/2.

This is correct and no longer assumes the rounded matrix is unitary.

## 2. Dependencies (Sections 3–5)

I rechecked the following, and all are correct:
- **Section 3:** 2 − √3 > 1/4; (N − 6)/4 ≥ N/8 for N ≥ 12; N/32; Q ≥ √(εN)/8; N^{1/3}/4; small-N range < 6.
- **Section 4:** 4π² ≤ 40; 1/3280; e^{−4} < 1/12; Brη ≤ 1/24.
- **Section 4 branching check:** 18/25, 82/125, 412/625, 84/125.
- **Section 5:** c_* ≈ 0.0286 > 1/36; spectral normalization; stopping check 1 → 1/4 with charge 3/4.
- **η-replacement:** TV ≥ 1 − 2η gives affinity ≤ √(1 − (1 − 2η)²) = 2√(η(1 − η)).

## 3. Attempted falsifiers (none broke the theorem)

1. **Protected-register leak, ε > 0.** A perturbation is stored in D, weakly coupled to S at angle β per round, sampled, then uncomputed. Detection ≈ θ²sin²β/(1 − cos^{2ε}β) → θ²/ε. This matches ⌈1/ε⌉ in the quadratic regime and stays below √K·θ. Collapse ≠ reset is absorbed by the fixed power.
2. **ε = 0, rotation then P samples.** TV ≈ min(1, Pθ²) ≤ √(P+1)·θ.
3. **G coherent gate errors, then P samples.** TV ≈ P(Gδ)² ≤ √K·Gδ while the error is small.
4. **Unequal stopping and history-selected registers.** Branches are aligned by ordinal gate count, halted leaves carry s = 1, and the normalized active mass prevents any branch-count factor.
5. **Zero-probability branch in one implementation only.** Its block contributes √(p·0) = 0, and formal caps keep κ ≥ 1.
6. **Rare-branch limit a/b → 0 with d → 0.** The conditional states become nearly orthogonal, yet TV ≤ d² holds with no 1/a² factor. This matches the paper's claim.
7. **Polar boundary.** ‖W − U‖ ≤ δ/4 < 1 needs only δ < 4, so it is always satisfied.
8. **SU(d) phase.** This attempt broke the literal compilation contract but not the theorem. See F-A below.

## 4. Findings

| # | Severity | Location | Finding |
|---|---|---|---|
| F-A | **Low (contract consistency)** | `eq:gate-contract` vs §6.4 "Fix overall phase representatives when synthesizing in SU(d_loc)" and "The complete synthesized word must satisfy `eq:gate-contract`" | The contract is a strict operator-norm bound with no phase freedom. SU(d) synthesis produces e^{−iθ/d}U up to δ. Example: U = S = diag(1, i), det = i, d = 2. The SU(2) representative is e^{−iπ/4}S, and ‖e^{−iπ/4}S − S‖ = \|1 − e^{iπ/4}\| ≈ 0.765. A word approximating it violates the stated contract by an order-one amount even when δ is tiny. The theorem itself is unaffected. The proof uses only s_h = \|⟨U_h u, V_h u⟩\| and the common isometry V_h, and a scalar phase e^{iα_h} on the entire history-selected operator (padded, including its controls) leaves both invariant. **Fix (one sentence):** state that the contract may hold modulo a scalar phase of the whole history-selected operator, with the existing remark that relative phases of controlled gates must be preserved. This is narrower than the declined F4 and needs no averaged-error contract. |
| F-B | Nonblocking (bookkeeping clarity) | §6.4 "leaving total error at most δ/2 for this finite-arithmetic allowance and gate synthesis"; ledger S(b_g) | Rounding plus exact polarization uses δ/2. Numerical polar error and synthesis must then share the remaining δ/2. If δ = 2^{−b_g}, synthesis "at b_g bits" alone would use the full δ. The text covers this with "constant precision allowances included" in S(b). Stating an explicit split, for example δ/4 + δ/4 at b_g + 2 bits, would make the ledger self-evident. |
| F-C | Optional (notation) | `eq:rare-precision` | In §6.3, d = ‖R_φ − I‖, while d_κ is the Bures distance in §6.2. Both are local and unambiguous in context. |
| — | Declined items | F4 (averaged contract), F5 (sharpness) | The declines are acceptable. Neither is needed for the theorem as stated, and the paper makes no optimality claim. F-A is a minimal subset of F4 that is needed only for consistency with SU(d) compilation. |

Former findings are resolved:
- **F1:** `\mathrm{active}` is fixed.
- **F2:** B_tr and d_loc are introduced.
- **F3:** complex-modulus and real/imaginary accuracy and polar unitarization are now explicit and correct.
- **F6:** README archiving language is scoped to v0.3.0, and the header says the v0.4.0 review is in progress.

Claim scope is consistent across the abstract, `thm:precision`, SOURCES, README and metadata. Each presents the result as an auxiliary consequence with no first-continuity, optimality, physical-noise or BPP/BQP claim. ABFL Appendix D, Çakan et al. Claim 8.3 and Dawson–Nielsen are acknowledged. I did not verify the external citations and introduced no references.

**Recommendation: GO-WITH-NOTES.** Apply F-A, the one-sentence phase clarification. F-B and F-C are optional.
