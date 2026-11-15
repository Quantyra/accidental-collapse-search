# Proof-adversarial review: v0.2.0 final source

**Source SHA-256 (as supplied):** `e0be2b107ef234bedd9c64961e393657b38164c1d55ef0bcd8e5ddb563487aa9`

I followed the no-tools instruction, so I did not recompute this hash. It is the identifier given in the packet. This report covers only the LaTeX, SOURCES text and metadata supplied above. I checked the arithmetic by hand. Nothing here is human, kernel or formal validation. I cannot independently check the cited CQP definition (\cite{abflcqp}).

## Verdict: **GO-WITH-NOTES**

I found no fatal or major gap. Every lower-bound step I tried to break held. The changes made after F1/F2 close the gaps they target. The remaining notes are minor or about clarity.

## Step-by-step verification

**Lemma `lem:projection` (`eq:jensen`)**
- The chain r ≤ B₀ ≤ A ≤ 1 is correct: completeness, then the triangle inequality, then Cauchy–Schwarz.
- The Jensen weights √(p_y q_y)/A average r_y to exactly B₀/A, so C_k ≥ A(B₀/A)^k ≥ r^k/A^{k−1}.
- Omitting terms with p_y q_y = 0 is justified.
- At k = 1, C₁ = B₀ ≥ r, as required.

**Lemma `lem:fixed` (`eq:fixed`)**
- The c=0 histories (h,y,0) carry weights (1−ε)p_y and (1−ε)q_y, and their states are unchanged. That gives (1−ε)Ar^k.
- The c=1 histories give εC_k.
- Weighted AM–GM gives the exponent (1−ε)·1 + ε(1−k) = 1−εk. With A ≤ 1 and εk ≥ 1, A^{1−εk} ≥ 1.
- The step is correct, and nothing in it depends on how many readouts occur.

**Decreasing exponent (`eq:decreasing`)**
- Before a real call the cap gives p(h) ≤ P−1, so κ ≥ 2; after the call κ ≥ 1.
- (1−ε)Ar^{k−1} ≥ (1−ε)r^k uses A ≥ r. εC_{k−1} ≥ εr^{k−1} ≥ εr^k.
- This holds at ε = 0 and ε = 1.

**Query sensitivity (`eq:self`, `eq:D`)**
- The reference world is O₀, so the reference history distribution does not depend on w. This is what makes Σ_w a₀(w) ≤ 1 hold at every frontier. It is correct.
- 1−|1−2a|^κ ≤ 2κa gives d² ≤ 4K·a₀(w).
- The triangle step through O_w^{⊗κ}Σ₀ uses unitary invariance at one common cut and block space.
- Minkowski then bounds the increment by 2√K.

**Bures triangle sketch**
- Fix a purification of the middle state, then choose Uhlmann-optimal, phase-aligned purifications of the endpoints. The Euclidean triangle inequality plus minimisation over purifications gives the result. Correct.
- Block-diagonal root fidelity factorises as Σ√(p q)·|⟨·⟩|^κ. Correct.

**Frontier induction**
- Nodes "immediately before the j-th query, or halted with fewer than j queries" form a prefix-free cut fixed by the history.
- The decision rule is the same in every world at equal histories, and the random choices are recorded in the history. So the same h reaches the same node in all worlds.
- Classical random splits preserve each contribution exactly.
- Each nonquery expansion is local: unitary, projective measurement, sampler, isometric preparation, environment reset, or measurement reset.
- Padding with control-zero queries gives a = 0. There is no loss from branch counting.

**Success to distance**
- At most 5 labels have z_w > 1/6, so "N−6" is conservative. TV ≥ 1/2.
- TV ≤ √(1−BC²) gives A_out ≤ √3/2. Then F ≤ history affinity ≤ A_out, so d² ≥ 2−√3 > 1/4.
- At N = 12, (N−6)/4 = N/8 exactly.
- 4Q²K ≥ N/8 gives Q²K ≥ N/32. Q ≥ √(εN)/8 holds.
- Q²(P+1) ≤ 2(Q+P)³ needs 2Q+P ≥ 1, which holds because Q ≥ 1.
- For N < 12: a zero-query transcript is independent of w, so min_w success ≤ 1/N. Also 11^{1/3}+√11 ≈ 5.54 < 6.

**Upper bound**
- For N′ ≥ 256: m ≥ 7, m ≤ √N′, and 2t+1 ≥ m/2 − 1/2 ≥ m/4.
- (2t+1)θ ≤ (m/2+1)(2/√N′) ≤ 1.125 < π/2.
- 4π² ≈ 39.5 ≤ 40. ε ≤ 40p follows from m² ≥ εN′, and rp ≥ 1/40.
- The closed form for s matches the first-success decomposition. A collapse on an unmarked draw correctly fails.
- 1−e^{−1/40} ≥ 1/80, so s ≥ 1/3280. With B = 4·3280, the failure probability is ≤ e^{−4} < 1/12.
- P = B⌈N′/m²⌉ ≤ B(N′^{1/3}+1).
- Approximation: Brη ≤ 1/24 leaves success ≥ 21/24.
- The ε̄ substitution keeps ε ≤ ε̄ ≤ 40p.

**Negative control**
- a = b = 2/5 and r = 4/5.
- g₁ = 18/25 < 4/5, while g₂ = 82/125 ≥ 80/125.
- The fixed-power frontier value is 250/625 + 80/625 + 82/625 = 412/625 ≥ 400/625.
- The decreasing-power value is 50/125 + 16/125 + 18/125 = 84/125 ≥ 64/125.
- All of these match the manuscript.

## Attempted counterexamples (all failed to break the proof)

1. **Tiny ε with very many readouts (P ≫ 1/ε).** The fixed exponent ⌈1/ε⌉ is unaffected by the number of readouts. The manuscript correctly avoids substituting the mean waiting time.
2. **Fixed power below threshold (εk < 1).** This fails locally, as the paper's own k=1 control shows. The threshold εk ≥ 1 is exactly what AM–GM needs, and the lemma states it.
3. **Protected workspace (sampler on an unentangled |0⟩_S).** A = 1 with a single outcome, so the contribution is unchanged. The potential survives, consistent with the Remark.
4. **Rank > 1 partial projectors or history-chosen sampled registers.** The lemma is stated for general projectors, and histories are common across worlds.
5. **Outcome-dependent stopping or restarts that differ between O₀ and O_w.** Zero-weight branches contribute zero. Frontier padding is analytical. A restart is an environment reset plus preparation, which is isometric.
6. **Laundering query information into a discarded or environment register, then sampling.** The environment stays in the global pure state. Overlaps include it, and there is no fictitious record.
7. **One query followed by about N ideal samples.** Q²(P+1) ≈ N, which is consistent and tight.
8. **Hidden flags.** Lower-bound histories record the flags, while the controller acts on a coarser history. Operations remain common at each fine history, so the result holds.
9. **Reference world running past the caps.** This was handled by the explicit capping and truncation of O₀ (former F1). Histories that are positive only in O₀ contribute zero to each F(0,w), so truncation is harmless.

## Do the post-F1/F2 changes address the actual gaps?

- **F1 (explicit capped O₀): yes.** Both the frontier count and the κ ≥ 1 requirement need caps on every O₀ branch. Section 2 now enforces the caps by truncation, and the truncation provably leaves valid-input executions unchanged.
- **F2 (finite-support randomness): yes.** It makes the execution tree finite, so the induction is genuinely finite. Countable support would also work through convergent sums, but finite support is clean.
- **CQP mapping (Corollary 1): adequate as scoped.** It charges each sample separately, adds at most one M-charge per stage, and explicitly disclaims query-only, unlimited-free-sample bounds. That disclaimer is necessary: with free samples, one query plus N samples finds the item. I cannot verify the cited CQP syntax from the packet, so Corollary 1's applicability rests on the coordinator's recheck.

## Findings

| # | Severity | Location | Finding |
|---|---|---|---|
| 1 | Minor | Sec. 2, paragraph after `eq:cost` ("This sum of caps lies between…") | The 1×–4× sandwich holds only if Q,P,R,M are the *tight* maxima over branches. If "caps" are just upper bounds, the upper side fails. Suggested fix: "the smallest such caps, i.e., the branch maxima". |
| 2 | Minor (optional strengthening) | Corollary 1 proof | Suppose each CQP stage has at least one circuit step. Then Q, P and M are each at most the circuit size, so the charged-call lower bound also implies an Ω(N^{1/3}) circuit-size lower bound. Consider stating this only if the cited syntax guarantees nonempty stages; I cannot confirm it does. |
| 3 | Editorial | Sec. 3.4, frontier paragraphs | The same points are repeated: padding, no rescheduling, finite-tree induction, common spaces. Condensing would make the argument easier to read. |
| 4 | Editorial | Sec. 3.5 ("at least N−6") | N−5 is exact. N−6 is conservative and correct; no change needed. |
| 5 | Note | Intro, related-work paragraph ("answers that search question") | Correctly qualified by "under the explicit charged-call convention". The claim depends on the cited cost measure matching (see #2); the current wording is acceptable. |

## Consistency checks
- SOURCES.md and the metadata agree with the manuscript on scope: search-model inclusion, not class equality; no human review; inherited tools attributed.
- The ⌈1/ε⌉ contribution statement is consistent across all three documents.
- The bibliography and dates are internally consistent (inspection date = manuscript date = November 15, 2026). I did not check any reference against its primary source.

**Recommendation: GO-WITH-NOTES.** Finding #1 is a one-phrase fix. The others are optional.
