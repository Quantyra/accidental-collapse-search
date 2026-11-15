# P011 v0.3.0 proof-adversarial review

**Source SHA-256:** `9fb7efb8a19ffcdaedb5b8bd286f51c8802b4f0b80a684151cbf6a768872d1d0`. This is copied from the packet. I did not recompute it, because the brief forbids running commands.

**Verdict: GO-WITH-NOTES.** I found no correctness blockers. All findings below are optional exposition or metadata hygiene.

This is an AI review of the frozen packet only. It is not human peer review or formal certification. I did not check any external source, so the cited theorem and section numbers in ABFL, MP, ŠS, Abbas et al. and MSY are unverified.

---

## 1. New positive-adversary theorem (Theorem 2, Section 5)

I attempted each requested refutation. None succeeded.

| Attack | Result |
|---|---|
| **Normalization with arbitrary entangled workspace** (eqs. `adv-query-charge`, `adv-history-normalization`) | Holds. `O_x^*O_y = (I−2P_x)(I−2P_y) = I − 2Σ_{x_i≠y_i}Π_{h,i}`, because `P_xP_y = Σ_{x_i=y_i=1}Π_{h,i}`. Each `Π_{h,i}` acts on the history-selected address and control register tensored with the identity on all workspace and environment. So `Σ_i‖Π_{h,i}ψ‖² ≤ 1` holds per history. With `Σ_{h∈H} p_x(h) = 1` on a prefix-free cut and `‖v‖ = 1`, the total query mass is at most 1. There is no branch-count factor. |
| **Feedback-selected query registers** | Holds. `Π_{h,i}` depends only on `h`, which is common to both worlds. The bound in `adv-query-pair` is applied per history before summing. |
| **Resets** | Holds. An environment reset is an isometry on the retained purification. A measurement reset is a projective comparison (Lemma 3) followed by a known preparation. Both leave each pair's contribution nondecreasing at fixed or decreasing exponent. |
| **Zero-probability histories** | Holds. Every term carries the factor `√(p_x(h)p_y(h))`. Lemma 3 justifies omitting `p_yq_y = 0` outcomes, since Cauchy–Schwarz forces `⟨u|Π_y|v⟩ = 0` there. Arbitrary filling of undefined states is harmless. |
| **Unequal stopping and sampling** | Holds. A frontier node is "just before the jth query, or halted after all remaining nonquery operations". This gives a prefix-free cut with at most `Q` layers. Halted nodes get `Π = 0` and contribute zero mass. In the decreasing argument, `κ(h) = P+1−p(h)` is history-determined, at least 2 before any sampler call by the cap, and at least 1 after. Bounding by `K = P+1` is valid because each summand in `adv-query-pair` is nonnegative and multiplied by `κ(h) ≤ K` through `|r^k − r'^k| ≤ k|r−r'|`. |
| **Fixed vs. decreasing powers mixed?** | No. They are two separate potentials, each closed under its own nonquery comparison: Lemma 4 with `εk ≥ 1`, and eq. `decreasing`. The min in `K_ε(P)` is taken only after both scalar bounds are proved. |
| **Certificate / Perron normalization** | Holds. For `|u|` with `u` an extremal eigenvector, `|u|ᵀΓ|u| ≥ |uᵀΓu| = ‖Γ‖ ≥ λ_max ≥ |u|ᵀΓ|u|`. Only `Φ_root = vᵀΓv = ‖Γ‖` is used, and the eigen-equation is never needed. `Γ_xx = 0` and `Λ_Γ > 0` follow as stated. |
| **Output separation** | Holds. `F_κ ≤ Σ_h√(p_xp_y) ≤ Σ_b√(Pr_x[b]Pr_y[b]) ≤ 2√2/3`. This gives `Φ_final ≤ β‖Γ‖`, using that `Γ` is supported only on `f(x) ≠ f(y)`. |
| **Constants and endpoints** | Holds. `QK ≥ (1−β)/2 · ‖Γ‖/Λ_Γ`. Since `2√2/3 ≈ 0.94281 < 17/18 ≈ 0.94444`, we get `c_* > 1/36`. At `ε = 1` or `P = 0`, `K = 1`, recovering the ordinary positive adversary bound. At `ε = 0` only the `P+1` branch applies. The failure-`η` variant `(1−2√(η(1−η)))/2` is correct for binary output. |
| **`adv-total`** | Holds. `Q(P+1) ≤ W(W+1) ≤ 2W²` needs `W ≥ 1`, which follows from `QK ≥ c_* > 0` for nonconstant `f`. `⌈1/ε⌉ ≤ 2/ε` gives the `εAdv₊` term. |
| **Parity** | Holds. The hypercube `Γ` has `‖Γ‖ = n`, and each `Γ∘D_i` is a perfect matching with norm 1. Together these give `Q ≥ n/(36⌈1/ε⌉)`. |
| **Stopping check** | Holds. I recomputed the example exactly: `Φ` goes from 1 to 1/4, the query mass is `(3/4)(1/2) = 3/8`, and the charge `2·1·3/8 = 3/4` is tight. Success probabilities are 1 and 3/4. |

## 2. Integration of the inherited search results

- **Lemma 3 (Jensen):** `C_k ≥ A(B₀/A)^k ≥ r^k/A^{k−1}`, and `r ≤ B₀ ≤ A ≤ 1`. Correct.
- **Lemma 4 (fixed power):** By weighted AM–GM, `(1−ε)A + εA^{1−k} ≥ A^{1−εk} ≥ 1` when `A ≤ 1` and `εk ≥ 1`. Correct.
- **Eq. `decreasing`:** `(1−ε)Ar^{k−1} + εC_{k−1} ≥ (1−ε)r^k + εr^{k−1} ≥ r^k`. Correct, including at `ε = 0`.
- **Query sensitivity:** The hybrid goes through `O_wΣ_0`. We get `d(Σ_0, O_wΣ_0)² = 2Σ_h p_0(h)(1−|1−2a|^κ) ≤ 4Ka_0(w)`. Minkowski then gives an increment of at most `2√K` per frontier. Correct, including history-dependent `κ`.
- **Cap enforcement on `O_0`:** Truncation is history-determined and leaves valid executions unchanged. Correct.
- **Success distance:** `A_out ≤ √3/2` and `2−√3 > 1/4`, so `D² ≥ (N−6)/4 ≥ N/8` for `N ≥ 12`. This gives `Q²k ≥ N/32`, `Q ≥ √(εN)/8`, and `Q+P ≥ N^{1/3}/4`. The `N < 12` case uses `12^{1/3} + √12 < 6`. All correct.
- **Upper bound:** I checked:
  - `4 ≤ m ≤ √N'`.
  - `2t+1 ≥ m/4`.
  - `(2t+1)θ ≤ 1+2/√N' < π/2`.
  - `p ≥ m²/(4π²N')` with `4π² < 40`.
  - `ε ≤ 40p` and `rp ≥ 1/40`.
  - `s ≥ (1−e^{−1/40})/41 ≥ 1/3280`.
  - `(1−1/3280)^{13120} ≤ e^{−4} < 1/12`.
  - The success formula's first-success decomposition is correct, because a marked draw succeeds whether or not it collapses.
  - With approximation, `Brη ≤ 1/24` still leaves success at least 7/8.
- **Section 4.4 check:** I recomputed `g₁ = 18/25`, `g₂ = 82/125`, and the frontier values `412/625 ≥ 400/625` and `84/125 ≥ 64/125`. All exact.
- **Regression check:** The adversary section reuses Lemmas 3–4 and eq. `decreasing` unchanged. Theorem 1, eq. `two-lower` and the upper construction are unchanged. I found no integration regression.

## 3. Findings

There are no correctness blockers. Everything below is optional.

| # | Severity | Location (`manuscript/main.tex`) | Issue | Proposed repair |
|---|---|---|---|---|
| N1 | Minor exposition | §5, the paragraph after eq. `adv-definition` ("Choose a nonnegative unit vector…") | The step from "Rayleigh quotient equals ‖Γ‖" to `Γv = ‖Γ‖v` silently uses the fact that a Rayleigh maximizer of a symmetric matrix is an eigenvector. The eigen-equation is never used anyway. | State "nonnegative unit `v` with `vᵀΓv = ‖Γ‖`", or add the one-line maximizer argument. |
| N2 | Minor exposition | §3.1, the paragraph after Lemma 3 | Fresh classical random branching is not listed among the nonquery comparisons. It is trivially an equality, since the probabilities are input-independent and the states are unchanged. | Add one sentence. |
| N3 | Minor exposition | §3.3, eq. `decreasing` | The `A = 0` case is not mentioned. It is trivial: `r = 0`, so the old contribution is 0. | Add "if `A = 0`, the old contribution is zero." |
| N4 | Minor clarity | Parity corollary | "Ω(n) … irrespective of the sampler cap" hides the dependence on ε. | State the bound explicitly as `Q ≥ n/(36⌈1/ε⌉)`. |
| N5 | Exposition | §1, paragraph after Theorem 1 ("Version 0.2.0 extends both comparisons…") | The version history reads as current-version claims inside the v0.3.0 text. | Rephrase as "Since version 0.2.0…" or move it to a revision note. |
| N6 | Metadata hygiene | `README.md` Archiving paragraph; `.zenodo.json` description | The README has a garbled sentence: "The prior release remains: The existing Zenodo release integration has been verified." Both files mix v0.2.0 "the revision extends…" prose with the v0.3.0 additions. | Reorder by version and fix the sentence. |
| N7 | Exposition | §2, definition of `R` | What counts as a "fresh attempt preparation", as opposed to an ancilla preparation, is informal. It does not affect the lower bounds, which ignore `R`. | Optionally define it. |

## 4. Remaining limitations, not defects

- **External citations unverified.** The attributions to MP Lemma 4.3, ŠS Theorem 3.1, ABFL CQP Sections 3/6/8, Abbas et al. Proposition 28 and MSY footnote 6 are not checked here.
- **CQP inclusion depends on CQP's definition.** The persistent-CQP corollary relies on CQP's sampler acting on states conditioned on the actual outcomes of the ordinary measurements `M_i`. The model fixes this convention, but whether it matches the cited definition is unverified.
- **Model choice for hidden flags and unreported outcomes.** The sampler acts on states conditioned on all actual classical records, including hidden flags and unreported outcomes. The proofs are consistent with this convention, but it is a modeling choice. A different ensemble convention for the nonlinear sampler would define a different model.
- **Unverified hashes.** I did not verify the research-commit or proof hashes in `SOURCES.md` (e.g. `9776b0…`). They differ from the packet hash by design, since they identify the research source rather than this manuscript.
- **Scope.** The argument covers the positive adversary only. It makes no claims about a signed-adversary extension, efficient certificate discovery, or physical realization, and the paper correctly disclaims these.
