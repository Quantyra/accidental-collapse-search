# P011 v0.3.0 final-source proof-adversarial recheck

**Source SHA-256:** `88bcf523f4fccac8422273bb65a02995304f6a68bc911b20e7b8383de03a44c6`. I copied this from the packet and did not recompute it, since commands are forbidden. It identifies the bytes reviewed; it is not mathematical verification.

**Verdict: GO-WITH-NOTES.** There are no blockers. My initial analysis still clears the full final source.

This is an AI review of the packet only. It is not human peer review or formal certification, and external citations remain unverified.

## 1. Each change checked against the original finding

| Finding | Change | Check | Status |
|---|---|---|---|
| **N1** Rayleigh normalization | §5 now asks for a nonnegative unit `v` with `vᵀΓv = ‖Γ‖`, with no eigen-equation claimed. | The absolute values of an extremal real eigenvector give a Rayleigh quotient of at least the extremal eigenvalue magnitude, which is `‖Γ‖`, and at most `λ_max ≤ ‖Γ‖`. So the quotient equals `‖Γ‖`. Only `Φ_root = vᵀΓv` is used later, and `‖v‖ = 1` is still what fixes the normalization in `adv-history-normalization`. | Resolved, scope unchanged |
| **N2** Classical branching | One sentence added after Lemma 3. | Each child has weight `p_a(h)π(c\|h)` with the state unchanged, and `π` is input-independent given `h` by the model. So `√(p_x p_y)` scales by `π(c\|h)`, and summing over `c` gives exact preservation. This holds blockwise at any exponent, so both potentials and `Φ` are covered. | Resolved |
| **N3** `A = 0` | Added at eq. `decreasing`. | `A = 0` gives `r = 0`, so the old contribution is 0 and the new one is nonnegative. | Resolved |
| **N4** ε-dependence for parity | The proof now states `Q ≥ n/(36⌈1/ε⌉)`, plus `Q(P+1) ≥ n/36` at ε = 0. | From Theorem 2 with `‖Γ‖ = n` and `Λ_Γ = 1`: `Q⌈1/ε⌉ ≥ QK ≥ c_* n > n/36`. At ε = 0, `K = P+1`. This is a direct specialization and adds no new algorithmic claim. | Resolved |
| **N5** Version-history tense | Now reads "Since version 0.2.0, …". | Exposition only. | Resolved |
| **N6** README / `.zenodo.json` | Archiving section rewritten by version; the garbled sentence is gone. | v0.3.0 is marked as a pending candidate with no DOI claimed. v0.2.0 and v0.1.0 are listed with their DOIs and receipts. The Zenodo description is coherent. | Resolved (minor residue in note 1 below) |
| **N7** Attempt-boundary definition | Deferred. | I accept the deferral. Both lower bounds use only `Q` and `P`. The upper construction explicitly defines and charges all `B` attempts (`R = B`). Ancillas are paid in gate and space accounting. | Acceptable |
| **AGY N-01** max/sum | `adv-total` now derives separate bounds. | From `Q(P+1) ≤ 2W²`: `W ≥ √(c_* Adv/2)`. From `⌈1/ε⌉ ≤ 2/ε` and `W ≥ Q`: `W ≥ c_* ε Adv/2`. Taking `max ≥ ½·sum` gives the stated Ω. At ε = 0 the linear term vanishes and the bound stays consistent. | Correct |
| **AGY N-02** ideal parity tradeoff | One sentence added. | This is the ε = 0 specialization of Theorem 2 and is proved. | Correct |

**On the "sharper" wording.** For search, `Q²K ≥ N/32` implies `QK ≥ √(N/32)·√K`, so Theorem 1 implies the adversary specialization uniformly.

Comparing total cost:
- Theorem 2 gives `Ω(N^{1/4} + ε√N)`.
- Theorem 1 gives `Θ(N^{1/3} + √(εN))`.

At ε = 1 both are `√N`, so "sharper/stronger" correctly means a uniformly stronger law, not a strict improvement at every fixed rate. The manuscript's wording ("sharper", "stronger … appropriate guarantee") matches that reading.

## 2. Full-source recheck

- **Unchanged and still verified:** Lemmas 3–4, eq. `decreasing`, query sensitivity, query-frontier induction, success-distance constants, the upper-construction arithmetic, the §4.4 exact values, the spectral charge, normalization, terminal separation, the bound `c_* > 1/36`, and the stopping check.
- **No regressions:** None of the edits touch a quantified inequality or a theorem statement. The abstract and both theorem statements are unchanged.

## 3. Remaining notes (non-blocking)

1. **README presentation.** The opening paragraph says "The revision adds…" before the version line identifies which revision. The status line also says "Previous published version: DOI …24244953" without labelling it v0.1.0. The Archiving list below is correct. Optional fix: label it v0.1.0 and lead with the version line.
2. **N7 is deferred, not resolved.** "Fresh attempt preparation" remains informal in §2. This is harmless for the stated results.
3. **Limitations carried over from my initial review:**
   - External citation locations are unverified.
   - The CQP inclusion depends on the cited definition matching the conditioned-on-actual-outcomes convention.
   - The sampler convention for hidden or unreported records is a modeling choice.
   - The hashes in SOURCES.md are unverified.
   - Coverage is the positive adversary only.
