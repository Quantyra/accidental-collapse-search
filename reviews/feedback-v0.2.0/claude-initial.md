# Proof-adversarial review: v0.2.0

**Source SHA-256 (as supplied):** `b7cecc45d2958fa77e2add9670cb632e8aa3018dc0a6afe5ce05a967b8b07714`
I did not recompute this hash, because the packet forbids tools. The review covers the LaTeX text in the packet, the SOURCES comparison and the metadata, read once and with no external access. Cited works were not consulted, so claims about their contents are unverified here. This is an AI review, not human or formal (kernel) validation.

**Verdict: GO-WITH-NOTES.** I re-derived every lower-bound step and every upper-bound constant and found no error that breaks the theorem. The findings below are gaps in stated hypotheses or scope, not broken inequalities.

---

## Substantive findings

### F1. Minor: caps and finiteness are not stated for the reference world O₀
**Locations:** §2, "Let Q,P,R,M be separate worst-case caps over complete branches"; §3.3, "The worst-case cap p(h)≤P ensures…"; §3.4, "at most Q query frontiers" and "always satisfies 1≤κ(h)≤P+1".

- The caps are quantified over complete branches but never tied to a set of inputs.
- O₀ is not a valid input ("No success requirement is imposed").
- On histories that have zero weight in every world O_w, the controller under O₀ may exceed Q or P, or even run without bound.
- The proof uses the caps on world-0 histories in three places:
  - κ(h) = P+1−p(h) ≥ 1 needs p(h) ≤ P.
  - The count of at most Q frontiers needs the query cap.
  - The "finite execution tree" claim needs finiteness under O₀.

**Why it is not fatal:**
- For each pair (0,w), only histories with positive weight in world w contribute to F(0,w), and those histories obey the caps.
- Overcounting a₀(w) is harmless.
- Frontiers beyond Q touch only histories with zero contribution, so they leave D unchanged.

**Fix:** add one sentence saying that, without loss of generality, the controller halts once any count would exceed its cap. Those histories have zero probability under every O_w, so success is unchanged, and the O₀ tree becomes finite with 1 ≤ κ ≤ P+1.

### F2. Minor: classical randomness must be finitely supported
**Locations:** §2, "Fresh classical random choices…"; §3.1, sums over h; §3.4, "finite-tree induction".

- The proof sums over a finite tree.
- Continuous or unbounded randomness would turn those sums into integrals and break the "finite tree" wording.

**Fix:** state that random choices are finitely supported. "Finite capped controller" arguably implies this, but it should be explicit.

### F3. Minor (scope): the claims about prior open questions cannot be checked from the packet
**Locations:** §1.1, "answers that search question under the explicit charged-call convention"; Corollary (persistent adaptive ideal search).

- The packet does not show that the CQP model of [abflcqp] (Sections 3, 6, 8) is contained in this model, or that the question in [mp, §1.5] is the same question.
- Particular points to confirm:
  - whether CQP's sampler and update rule match eq. (instrument) at ε=0;
  - whether CQP grants any free resource not charged in eq. (cost), such as unbounded samples per step or uncharged full-history sampling;
  - whether the cited question is about query lower bounds or about class containment.
- The manuscript already hedges with "search-model inclusion". I would soften "answers" to "addresses, under the stated inclusion", unless the inclusion is spelled out against the cited definitions.

### F4. Low: encoding damage in SOURCES.md
**Location:** the SOURCES table and prose, e.g. "?just above?", "Miloschewsky?Podder", "Sections 3?4", "Regev?Schiff", "Fiorentino?Weigert", "Gilchrist?Langford?Nielsen".

- Quotes and en dashes appear as "?" throughout.
- This may be an artifact of the review packet, but the committed file should be checked.

### F5. Low (presentation): κ is stated for all histories without qualification
**Location:** §3.4, "always satisfies 1≤κ(h)≤P+1".

This is true only on cap-respecting histories. It is resolved by F1's truncation sentence.

### F6. Informational: the fixed exponent threshold is tight
**Location:** §3.2.

- For k = 1 and ε < 1, the factor (1−ε)A + ε is below 1 whenever A < 1.
- More generally, A^{1−εk} < 1 when εk < 1 and A < 1, so the condition εk ≥ 1 is necessary for this local inequality. The §4.4 negative control (g₁ < r) is a concrete instance.
- A one-line remark would show that the inequality chain does not rely on a loose step.

---

## Steps independently re-derived (all hold)

### Lemma 2 (projection comparison)
- r ≤ B₀ ≤ A ≤ 1 holds.
- Weighted Jensen with convex x^k on weights √(p_y q_y)/A gives C_k ≥ A(B₀/A)^k ≥ r^k/A^{k−1}.
- The case A = 0 is handled correctly.
- Outcomes with p_y q_y = 0 carry ⟨u|Π_y|v⟩ = 0, so omitting them is justified.

### Lemma 3 (fixed power)
- The coefficients are (1−ε) on each unchanged branch and ε on each projected branch.
- Weighted AM–GM gives (1−ε)A + εA^{1−k} ≥ A^{1−εk}.
- With A ≤ 1 and εk ≥ 1, the right side is at least 1.

### Decreasing exponent (eq. decreasing)
- The step needs k−1 ≥ 1, which holds because the cap guarantees κ ≥ 2 before any sampler call (subject to F1).
- C₁ = B₀ ≥ r covers the boundary case.
- The step is valid at ε = 0.

### Other nonquery steps
These all preserve or increase the potential:
- common unitaries;
- history-selected gates and history-selected projectors;
- input-independent random branching;
- known-ancilla preparation;
- environment reset (an isometry);
- measurement reset (an ordinary measurement followed by preparation).

### Query sensitivity
- ⟨ψ|O_w|ψ⟩ = 1 − 2a.
- Bernoulli's inequality gives 1 − |1−2a|^k ≤ 2ka, on both ranges of a.
- d² = 2(1−F) ≤ 4K·a₀(w).
- O_w is applied blockwise as the unitary ⊕_h O_w^{⊗κ(h)}, so the Bures triangle is used on one common block space.
- Minkowski's inequality and Σ_w a₀(w) ≤ 1 give an increase of at most 2√K per frontier.
- Between frontiers only scalar monotonicity is used, never a cross-space metric. This is correct.

### Bures triangle sketch
Uhlmann-optimal purifications with real, positive phase alignment, followed by the Euclidean triangle inequality, give the result. This is correct.

### Endpoint
- With TV ≥ 2/3 − 1/6 = 1/2 and TV ≤ √(1−A²), we get A ≤ √3/2.
- Then d² ≥ 2 − √3 > 1/4.
- At least N−6 labels have z_w ≤ 1/6, and (N−6)/4 ≥ N/8 for N ≥ 12.
- From 4Q²k ≥ N/8, Q²k ≥ N/32.

### Lower-bound arithmetic
- ⌈1/ε⌉ ≤ 2/ε gives Q ≥ √(εN)/8.
- P+1 ≤ 2(Q+P) and Q² ≤ (Q+P)² give Q + P ≥ N^{1/3}/4.
- Q = 0 is excluded by the inequality itself.

### Small N
- For 2 ≤ N < 12, a zero-query algorithm succeeds with probability at most 1/N ≤ 1/2.
- The cost expression satisfies 12^{1/3} + √12 ≈ 5.75 < 6.

### Upper bound
- eq. (success) holds, including both limits: 1−(1−p)^r at ε = 0 and p at ε = 1.
- The parameters satisfy m ≥ 7 and m ≤ √N'.
- 2⌊m/4⌋ + 1 ≥ m/4.
- (2t+1)θ ≤ 1 + 2/√N' ≤ 1.125 < π/2.
- p ≥ m²/(4π²N') ≥ m²/(40N'), so ε ≤ 40p and rp ≥ 1/40.
- The success probability is at least (1/80)/41 = 1/3280.
- With B = 4·3280 attempts, the failure probability is at most e^{−4} < 1/12.
- N'/m² ≤ N'^{1/3}.
- Spot checks:
  - N' = 256, ε = 1: m = 16, p ≈ 0.285.
  - N' = 256, ε = 0: m = 7, r = 6, p ≈ 0.035.

### Approximation coupling
- Trace distance between pure states is at most their Euclidean distance, which is at most the sum of per-gate operator-norm errors.
- The TV distance of each attempt's draw law is at most η, and after a collapse the draws repeat, so the transcript differs with probability at most rη.
- The bound η ≤ 1/(24Br) leaves success at least 1 − 1/12 − 1/24 > 2/3.

### §4.4 numerics
All figures are recomputed exactly:
- a = b = 2/5 and r = 4/5;
- g₁ = 18/25 < 20/25;
- g₂ = 82/125 ≥ 80/125;
- frontier values 412/625 ≥ 400/625 and 84/125 ≥ 64/125.

The symbolic frontier expressions match the tree described.

### Cost bracketing
The sum of caps is at most four times the maximum per-branch sum. Correct.

---

## Attempted counterexamples (none broke the proof)

1. **Protected entangled workspace.** A query-dependent register D is kept apart from the sampled register S. The conditional-pure-state potential tracks D, and collapse of S never resets D.
2. **Readout-dependent stopping, gate choice and register choice.** I recomputed the §4.4 tree. The frontier induction applies node by node, and padding with control bit 0 adds a₀ = 0.
3. **Too-small fixed exponent (εk < 1).** The local inequality genuinely fails (F6, and g₁ < r). The theorem uses k = ⌈1/ε⌉, so this is avoided.
4. **Many readouts at small ε.** The fixed exponent does not grow with the number of readouts. Each sampler call is individually non-decreasing, so there is no waiting-time substitution.
5. **Outcomes with positive weight in only one world, or history-selected projectors.** Their contribution is zero. Lemma 2's omission rule and zero-weight inheritance handle them.
6. **Hidden or erased flags.** The histories keep the flags, and the controller's decisions are functions of the coarser history. The potential stays well defined.
7. **Environment reset versus measurement reset.** The first is an isometry; the second is a measurement plus preparation. Both are covered, and their different later sampler statistics are correctly not identified with each other.
8. **Controlled or superposed queries.** The control bit enters a_{0,h}(w), and Σ_w a_{0,h}(w) ≤ 1 still holds.
9. **Reference world exceeding the caps.** This is a gap in statement only (F1). It is harmless because such histories carry zero weight in every valid world.
10. **Boundary rates.** At ε = 1, k = 1 and the potential reduces to ordinary-measurement monotonicity. At ε = 0, the decreasing-exponent argument gives the ideal bound.
11. **Small-N edges and the N' = 256 parameter edges.** Both checked above.

---

## Recommended edits before release

- Add the truncation-to-caps sentence (F1) and the finitely-supported-randomness sentence (F2).
- Optionally add the tightness remark for εk ≥ 1 (F6).
- Soften "answers that search question" unless the CQP inclusion is checked against the cited definitions (F3).
- Fix the character encoding in SOURCES.md (F4).
