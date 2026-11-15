# Review record

Status: internal manuscript preparation; no separate external-model review, independent human peer review or formal certification. This record does not claim that research diagnostics establish the theorem by finite agreement.

## Scope and disposition

The manuscript transcribes the retained analytic proof of the uniform independent-collapse search law. Internal checking covers the following specific obligations:

| Obligation | Argument and current disposition |
| --- | --- |
| State update with entangled reference | Projectors act on the sampled register and identity on all workspace/reference; histories carry global conditional pure states. Mixed preparation semantics are explicit, with no unspecified reduced-density extension. |
| Complete histories | Copy powers occur inside the history sum; outputs and flags are retained jointly. No independent-snapshot premise is used. |
| Fixed exponent | Weighted Jensen gives C_k >= r^k/A^(k-1); weighted AM-GM makes (1-epsilon)A+epsilon A^(1-k) >= 1 when epsilon k >= 1. Zero branches handled separately. |
| Query cost | The auxiliary reference query and Bures triangle inequality give 2 sqrt(k a_0(w)); summing squared distances costs 2 sqrt(k), not k. |
| Success comparison | The zero-oracle input needs no success guarantee. At least N-6 labels give output variation >= 1/2 and D^2 >= N/8. |
| Construction and failure costs | Mark bits are appended coherently before readout. All 13,120 attempts run; no feedback verification or free restart. Small instances have a bounded exhaustive fallback. |
| Precision and computation | Power-of-four padding uses a controlled oracle; exact gates are available. Approximate preparation uses a construction-specific coupling, not general nonlinear contractivity. Parameter selection uses integer comparisons. |
| Literature and claims | Credits ABFL, Abbas et al. and Miloschewsky--Podder; distinguishes noisy oracle, gentleness and retained-record access. No broad priority, physical or BPP/BQP claim. |

The published manuscript is not yet a release: source/PDF hashes, compiler checks, actual all-page inspection and metadata consistency are recorded in `verification/`. The two original finite diagnostic runs are preserved without rerunning or overwriting them. Their 1,468 exact assertions support local sanity checks, while the general argument is analytic.

## Recommended focus for a subsequent adversarial review

Inspect complete-history conditioning and purification semantics; the auxiliary-state triangle-inequality step; no-feedback legality; and the exact prior-work boundary. Any selected review must preserve actual provider/model identity, input hashes, raw findings and dispositions. No reviewer verdict is manufactured here. No mandatory human-review prerequisite is introduced. Formal Lean certification, if selected, is a separate project.
