# Proof-adversarial review: Optimal Search with Accidentally Collapsing Measurements

**Source SHA-256 reviewed:** `c8c3465e0ec9cddb825b47935efead06bba0c4ad292c1afe81898aa2c755a2fa` (`manuscript/main.tex`, candidate commit `b791bd1`).

**Scope:** I worked only from the source text you supplied. I ran no commands, made no external requests and edited no files. I did not consult Miloschewsky–Podder, ABFL or the other cited works, so attribution and novelty are not assessed. Absence of known prior results is not evidence of novelty.

## Independent analysis of the universal steps

**Model semantics (§2).** The sampler is defined on conditional global pure states. The flag `c` and outcome `y` are classical history labels, even when hidden from the output map. Hidden flags are therefore never treated as a decohered quantum environment fed into later samplers. Branch probabilities are `p_a(h)(1−ε)p_y` for `c=0` and `p_a(h)ε p_y` for `c=1`. These give root-affinity coefficients of exactly `(1−ε)√(p_y q_y)` and `ε√(p_y q_y)`. The ensemble-versus-purification ambiguity of a nonlinear rule is fixed by convention: classical choices go in the history, quantum mixedness is purified. The lower bound holds under either representation. Unitaries and isometries preserve `F_k`, and ordinary measurements increase it.

**`F_k` as a root fidelity.** For block-diagonal states, root fidelity is `Σ_h √(p_a q_b) F(ρ_h,σ_h)`. For k-fold pure products it is `|⟨ψ|φ⟩|^k`. So eq. (potential) is a genuine root fidelity. The Bures triangle sketch is correct: Uhlmann's theorem holds with one purification fixed, and `‖ψ_ρ−ψ_σ‖² ≥ 2−2F`.

**Lemma 2 (`lem:projection`).**
- Terms with `p_y q_y = 0` satisfy `|⟨u|Π_y|v⟩| ≤ √(p_y q_y) = 0`, so omitting them leaves `B_0 ≥ r` intact.
- `B_0 ≤ A` follows termwise from Cauchy–Schwarz.
- Jensen applies because `x^k` is convex on `[0,∞)` for `k ≥ 1`, with weights `√(p_y q_y)/A`. This gives `C_k ≥ A(B_0/A)^k ≥ r^k A^{1−k} ≥ r^k`.
- The `A = 0 ⇒ r = 0` case is correct.

**Lemma 3 (`lem:fixed`).**
- `(1−ε)A + εA^{1−k} ≥ A^{1−ε}·A^{ε(1−k)} = A^{1−εk}` by weighted AM–GM, which needs `A > 0`. Then `A^{1−εk} ≥ 1` follows from `A ≤ 1` and `εk ≥ 1`.
- At ε=1 the inequality is an equality chain, which is fine.
- The zero branch is fine because `A = 0` forces `r = 0`.
- Branches with zero weight in one world contribute 0 before and after.

**Decreasing exponent (eq. `decreasing`).**
- `(1−ε)A r^{k−1} ≥ (1−ε)r^k` uses `A ≥ r`.
- `C_{k−1} ≥ r^{k−1} ≥ r^k` needs `k−1 ≥ 1`, which holds.
- This is valid at ε=0.
- Dummy readouts of a known basis register give `A = 1` and `r_y = r`, so they are harmless.

**Query sensitivity (§3.4).**
- `⟨ψ|O_w|ψ⟩ = 1 − 2a_{0,h}(w)`, so `d² = 2(1−F) ≤ 4k·a_0(w)`.
- Eq. (self) holds: Bernoulli's inequality covers `a ≤ 1/2`, and the trivial bound covers `a ≥ 1/2`.
- The triangle step uses blockwise-unitary invariance with the same history labels in all three states.
- Minkowski gives an increase of at most `2√k·√(Σ_w a_0(w)) ≤ 2√k`.

**Output distance (§3.5).**
- At most 5 labels have `z_w > 1/6`.
- `TV ≥ 2/3 − 1/6 = 1/2`.
- Le Cam's bound gives `A_out ≤ √3/2`.
- `F_k ≤` history affinity `≤` output affinity, by coarse-graining over inaccessible parts and data processing.
- So `d_w² ≥ 2−√3 > 1/4`, and `(N−6)/4 ≥ N/8` holds for `N ≥ 12`.
- From `D ≤ 2Q√k`, `Q²k ≥ N/32` follows.
- The bounds `⌈1/ε⌉ ≤ 2/ε`, `Q ≥ √(εN)/8`, `P+1 ≤ 2(Q+P)` and `Q+P ≥ N^{1/3}/4` all check out.

**Upper bound (§4).**
- Eq. (success) is exact. A collapse on an unmarked draw kills the attempt, and the closed form and endpoints are right.
- The parameter claims hold: `m ≥ 7`, `m ≤ √N'`, `2t+1 ≥ m/4`, `(2t+1)θ ≤ 1.125 < π/2`, `p ≥ m²/(4π²N')`, `ε ≤ 40p` and `rp ≥ 1/40`.
- `s ≥ (1−e^{−1/40})/41 ≥ 1/3280`, and `(1−1/3280)^{13120} ≤ e^{−4}`.
- Attempts are product states with independent coins, so they are independent.
- The resources are `Q = O(m)` and `P = O(N'^{1/3})`.
- The `ε̄` substitution preserves `ε ≤ 40p` and `m ≤ √N'`.
- The matched law is confirmed.

I found no legal counterexample to the fixed-exponent monotonicity. I also found no missing hypothesis in Lemmas 2–3 or in the hybrid argument.

## Findings

**1. MEDIUM: Theorem 1, eq. (main), "uniformly for 0≤ε≤1" with "absolute implied constants" is false at N=1, and N<12 is unproved.**
- At N=1, the algorithm "output 1" costs T=0, while `N^{1/3}+√(εN) ≥ 1`. So no positive constant gives the stated lower bound.
- For 2 ≤ N ≤ 11, §3 only proves eq. (two-lower) for N ≥ 12, then asserts the lower half of the theorem.
- This does not block the asymptotic mathematics, but the statement as written must be corrected before release.
- **Fix:** state `N ≥ 2`. Add one line: for N ≥ 2 a zero-query algorithm's output law is independent of w, so some w succeeds with probability at most 1/2. Hence `T ≥ Q ≥ 1 ≥ (N^{1/3}+√(εN))/c` with c≈6 for N ≤ 11.

**2. LOW (exposition with a real pitfall): §3.4 final paragraph, "Ordinary adaptive branches can be padded to fixed caps … The same estimate applies to each common history."**
- D is a global quantity, so how branches are aligned matters.
- Suppose padding embeds all branches into one universal slot pattern, with real queries at different global steps. Then the increment at step j is `2√k·√π_j`, where `π_j` is the mass doing a real query. The sum `Σ_j √π_j` can exceed Q. For example, L branches each making one query at different steps give `√L` instead of 1.
- The correct alignment does exist, so this is not a theorem gap. Monotonicity is per-subtree, so the potential at the frontier "just before each history's j-th query" dominates the frontier after its (j−1)-th query. At frontier j every unfinished history queries, so `Σ_w a_0(w) ≤ 1`.
- **Fix:** state this frontier alignment explicitly, or pad each inter-query segment to a common length. In the decreasing argument, use a per-history exponent `k_h = P+1 − (#sampler calls in h)`. Its bound `k_h ≤ P+1` suffices in eq. (self).

**3. LOW: §4.3, "suppose the joint state of each attempt has trace-distance error at most η … transcript differs with probability at most rη".**
- In this nonlinear model, the density operator does not determine the transcript law. Take `I/2` on S prepared two ways:
  - as a classical mixture of `|0⟩,|1⟩`: all r samples are equal;
  - as half of a Bell pair: the r samples are i.i.d.
- The per-draw coupling is valid only when the attempt is a single conditional global pure state, so that pre-collapse draws are i.i.d. from one η-close law.
- The stated gate-error case (summed operator-norm errors) is pure, so that application is fine. Exact gates make this irrelevant to Theorem 1.
- **Fix:** impose the η bound on every conditional pure branch, or bound the loss by `r·Σ_h p_h η_h`. Note that an averaged-state bound alone yields only `Σ p_h η_h ≤ √η` via Jensen. This does not block the theorem.

**4. LOW (model clarity): §2 and §3.1, "discards can be retained in the inaccessible purification, and resets can be represented by ordinary measurement and preparation".**
- These two representations are not operationally equivalent here.
- Suppose a register is entangled with S and is reset by swap-to-environment. Later samples of S stay i.i.d. If it is reset by measure-and-flip, S is conditioned and later samples repeat.
- The model charges M "reset calls" without fixing which semantics applies. This is precisely an unobserved-environment versus conditioned-outcome distinction.
- The lower bound holds under both: one is an isometry and the other an ordinary measurement plus isometry. The upper bound uses `M=0`. So the theorem is unaffected.
- **Fix:** define reset and discard semantics explicitly, and state that the lower bound covers either convention.

**5. LOW (observation, non-blocking): where the proof uses deferral of sampler outcomes.**
- I could not locate a step of §3 that uses the rule that sampler outcomes "cannot control later gates".
- Every step is per-history, and conditioning operations on `y` keeps them input-independent at a fixed h.
- If that is right, the lower bound covers sampler-outcome feedback, which §5 explicitly disclaims.
- **Recommendation:** either identify the step that uses deferral, or carefully verify the extension against known adaptive-model results before claiming it. The current narrower claim is safe.

## Not findings
- Lemma 2 omits the one-line justification `|⟨u|Π_y|v⟩| ≤ √(p_y q_y)` for dropping the zero terms. It would be worth adding.
- The padded-oracle encoding of out-of-range labels when `b=0` is standard and should be fine.
- After this review, the review-status wording in the manuscript disclosure, README, `.zenodo.json` and publication record will need updating. As you noted, that is outside the mathematics.

## Limitations
This is a single-reviewer informal check, not a formal certificate. I did not compare against the cited papers.

**Verdict: GO-WITH-NOTES**
