# Proof-adversarial recheck: Optimal Search with Accidentally Collapsing Measurements

**Source SHA-256 reviewed:** `617e873d184ece9c3b51c0a98b1669cc74c2d36a52396a7a35e75e684349885e` (`manuscript/main.tex`, revised source; original candidate `b791bd13ec9046a161dfd6afa49f06fef1f8b6e9`)

**Scope:** I worked only from the supplied text and diff. I ran no commands, made no external requests and edited nothing. I did not consult the cited papers or the archive's `REVIEW.md`. So I assess neither attribution nor novelty, and I have not checked the disclosure's claims about archive contents. The remit can be completed for the mathematics.

## Independent recheck of the revised arguments

**Variable-exponent block spaces (§3.1).**
- `Σ_a^(κ)` lives on `⊕_h H^{⊗κ(h)}`. This space is the same in both worlds because `κ` is a function of `h` alone.
- On that space, root fidelity of block-diagonal states is `Σ_h √(p_a p_b)·|⟨ψ_{a,h}|ψ_{b,h}⟩|^{κ(h)}`, and Bures distance is a genuine metric there.
- The proof uses the metric (triangle inequality) only *within* a fixed cut, at a query. Between cuts it uses only fidelity monotonicity, so no metric on a varying space is needed. This is sound.

**Subtree refinement (§3.4).**
- `F_κ` is additive over leaves of the history tree. The next operation at leaf `h` depends only on `h`: ordinary outcomes and seed, and sampler records under the deferral rule. It is therefore identical in both worlds.
- Each nonquery step replaces one leaf's contribution by a sum that is at least as large:
  - unitaries and isometries give equality;
  - ordinary measurements give `C_κ ≥ r^κ` (Lemma 2);
  - fixed-power sampler calls are covered by Lemma 3;
  - decreasing-power sampler calls are covered by eq. (decreasing).
- Leaves with zero weight in one world contribute zero before and after.
- Hence refining any finite set of leaves, in any order, is monotone. Worst-case caps make the subtrees finite.
- The cut "just before each leaf's j-th query" refines the cut "just after the (j−1)-th query". The argument is correct.

**Query sensitivity with max κ.**
- At frontier `j`, the comparison unitary is `U = ⊕_h O_{w,reg(h)}^{⊗κ(h)}`, with padded leaves using control bit 0. In world `w` this is exactly the actual step.
- This gives `1−F(Σ_0, UΣ_0U†) = Σ_h p_0(h)(1−|1−2a_{0,h}|^{κ(h)}) ≤ 2K·a_0(w)`, so `d ≤ 2√(K a_0(w))`.
- The triangle step and the componentwise Minkowski step give `D' ≤ D + 2√K`.
- There are at most `Q` frontiers, because `Q` is the worst-case per-branch count. With `K ≤ P+1` or `K = ⌈1/ε⌉`, both bounds in (two-lower) follow.
- The bound in my original Finding 2 (a `√L` blow-up from misaligned global slots) is avoided.

**No operational rescheduling.**
- The frontiers are cuts in the history tree of the unchanged process.
- Branch updates are defined on conditional pure states and do not depend on wall-clock position.
- The cut location is `h`-measurable and does not depend on `w`.
- No step requires sampler records to be available for control. The padded identity queries are analytical and uncharged, which is correct.

**Decreasing exponent.**
- Before a call, `p(h) ≤ P−1`, so `κ ≥ 2`.
- `(1−ε)A r^{κ−1} ≥ (1−ε)r^κ` uses `A ≥ r`.
- `εC_{κ−1} ≥ εr^{κ−1} ≥ εr^κ` uses `κ−1 ≥ 1`.
- Ordinary steps keep `κ`. At the output, `F_κ ≤` the history affinity `≤ A_out`. All correct.

**N ≥ 2 repair.**
- With `Q = 0`, the global state, and hence the output law, is independent of `w` even with sampler calls. Some `w` succeeds with probability at most `1/N ≤ 1/2 < 2/3`, so `T ≥ 1`.
- For `N ≤ 11`, `N^{1/3}+√(εN) ≤ 11^{1/3}+√11 ≈ 5.54 < 6`.
- For `N ≥ 12`, `T ≥ max(N^{1/3}/4, √(εN)/8) ≥ (N^{1/3}+√(εN))/16`.
- The upper fallback for `N' < 256` is constant cost, and `N^{1/3} ≥ 2^{1/3}`. The uniform constants hold for `N ≥ 2`, and excluding `N = 1` is correct.

**Reset semantics (§2, §3.1).**
- An environment reset is an isometry on the retained purification, identical in both worlds, so it preserves `F`.
- A measurement reset is an ordinary measurement (monotone) followed by a known preparation (isometry).
- Each convention is covered separately. Declining to identify the two is correct, because they lead to different later sampler statistics.

**Conditional-pure preparation error (§4.3).**
- With per-branch pure-state trace distance `≤ η`, address/mark-bit total-variation distance is `≤ η`.
- Before a collapse, draws are i.i.d. from one fixed law in each world. Coupling the coins, and each draw with failure probability `≤ η`, gives a union bound of `rη` per attempt and `Brη` overall.
- With `η ≤ 1/(24Br)`, success is at least `11/12 − 1/24 = 7/8 > 2/3`.
- The gate case holds: unitary approximations keep the branch pure, and pure-state trace distance `≤ ‖ψ−ψ'‖ ≤ Σ` operator-norm errors.
- The added caveat about averaged density matrices is correct and matches my counterexample.

**Unchanged parts.** I rechecked these quickly; nothing changed.
- Lemmas 2–3, eq. (self), and the output-distance step hold.
- The upper bound holds: `p ≥ m²/(4π²N')`, `ε ≤ ε̄ ≤ 40p`, `rp ≥ 1/40`, `s ≥ 1/3280`, and `(1−1/3280)^{13120} ≤ e^{−4} < 1/12`.

## Disposition of initial findings

| # | Initial finding | Status |
|---|---|---|
| 1 | MEDIUM: N=1 is false and N<12 is unproved | **Resolved.** The domain is `N ≥ 2` and the bounded-N argument is correct. |
| 2 | LOW: misaligned padding could give `Σ√π_j > Q` | **Resolved.** The j-th-query frontier and per-history `κ(h)` are exactly the needed fix. |
| 3 | LOW: averaged-state η does not control the nonlinear transcript | **Resolved.** The contract is now on conditional global pure branches, with an explicit caveat. |
| 4 | LOW: reset/discard semantics unspecified | **Resolved.** Both conventions are defined, charged and covered separately. |
| 5 | Observation: the lower bound does not visibly use deferral | **Unchanged, appropriately.** See Finding 3 below; this is an extension, not a gap. |

## Findings on the revised source

No HIGH or MEDIUM findings. No actual gap in the declared model was found.

**1. LOW (exposition): §2 says "The circuit and sampler schedule are fixed before execution"; §3.1/§3.3 introduce `κ(h)` to handle "ordinary-control branches with different numbers of intermediate readouts."**
- If the schedule really is fixed, `p(h)` is the same at every cut and `κ(h)` is unnecessary.
- The variable exponent matters only under the relaxation permitted by §2: "ordinary-history-controlled operations with fixed worst-case caps." That relaxation implicitly includes ordinary-controlled sampler placement.
- **Impact:** none on the theorem. The lower bound covers the larger class, and the upper bound uses the fixed class.
- **Fix:** add one sentence to §2 saying the lower bound permits ordinary outcomes to control gates, queries, resets *and the placement of sampler calls*, subject to worst-case caps `Q` and `P`. Say also that `κ(h)` exists for that case.

**2. LOW (exposition): §3.1, "The associated Bures distance is again a metric," and §3.4, the frontier paragraph.**
- The argument is correct. However, it does not say that the metric is used only at a fixed cut, where block spaces and `κ` are common to the three states compared. Across cuts, only fidelity monotonicity is used.
- A reader may worry that the state spaces differ between frontiers.
- The step `Σ_h p_0(h)·2κ(h)a_{0,h}(w) ≤ 2K·a_0(w)` is described in words but not displayed.
- **Fix:** add one sentence on where the metric is used, and display the bound. It might also be noted that the per-history sum, rather than `K`, is the sharper quantity.

**3. Extension outside the declared model (not a gap): deferral of sampler outcomes.**
- As in my original Finding 5, I still cannot identify a lower-bound step that uses deferral.
- The new frontier argument only needs the next operation to be a function of `h`, which would remain true under sampler-outcome feedback.
- The manuscript correctly disclaims that extension (§5), and nothing in the revision relies on it.
- **Recommendation:** leave the claim narrow. If it is ever broadened, check it against the known adaptive-model literature first.

**4. Outside mathematical remit:** the disclosure paragraph and README now state that the archive records CLI AI-review identities, scopes, findings and dispositions. I was not given `REVIEW.md` and cannot confirm this. The record should include this recheck and its disposition before any readiness decision.

## Limitations
This is a single informal AI review, not human peer review or a formal certificate. It makes no assessment of novelty, priority, physical feasibility or literature accuracy.

**Verdict: GO-WITH-NOTES**
