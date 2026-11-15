# Focused delta check: v0.2.0 final2 source

**Source SHA-256 (as supplied):** `47384ca46a9b823927da5784ea9d67a1cb14b18d10cfd8a958efb21e56e6e1d3`

I used no tools, so I have not recomputed this hash. The packet supplies it, and I bind the verdict to it. This check covers only the stated one-paragraph delta from `e0be2b10…`, against my completed full review of that source. It is not human, kernel or formal validation.

## Verdict: **GO**

## Does the delta close prior Finding 1?

Yes. Q, P, R and M are now the smallest caps over valid marked inputs and complete branches, which means each is the branch maximum of its call type. For any valid input and branch, write that branch's total as q + p + r + m.

- **Lower side of the sandwich:** each term is at most its cap, so the largest branch total is at most Q + P + R + M.
- **Upper side of the sandwich:** each cap is attained by some branch whose total is at least that cap. So each of the four caps is at most the largest branch total, and their sum is at most four times it.

The factor-four sandwich is therefore valid. On a finite capped tree the minimum exists, so T is now uniquely defined for each algorithm.

## Does it invalidate any proof or resource step?

I found nothing it breaks.

1. **Caps now defined over valid inputs only, versus O₀.**
   - The lower bound needs every O₀ branch to have at most Q queries (for the frontier count) and p(h) ≤ P (so that κ = P+1−p(h) ≥ 1).
   - The retained truncation clause ("halt before a cap would be exceeded") provides both. It depends only on the history's call counts, so the decision rule stays common across worlds at equal histories.
   - Because Q and P are maxima over valid executions, the truncation never fires on valid inputs, so those executions are unchanged, as the text states.
   - Histories that are positive only in O₀ contribute zero to F(0,w).
2. **Smallest versus arbitrary caps in the lower bound.** The inequalities Q²(P+1) ≥ N/32 and Q²⌈1/ε⌉ ≥ N/32 hold for any valid caps, so they hold for the smallest ones. The N < 12 step still gives Q ≥ 1, because a zero-query law cannot succeed.
3. **Upper construction.** Every branch makes exactly B(t+1) queries (the padding check is inside each query), Br sampler calls, B preparations and no measurements. The branch maxima therefore equal the values in eq. (resources). The N′ < 256 fallback has constant maxima.
4. **Corollary 1 and the consistency of Theorem 1's wording** ("worst-case oracle and sampler call caps") are unaffected.

## Attempted counterexample to the new wording

I tried an algorithm whose O₀ executions exceed the valid-input maxima, for example by looping on a "no mark seen" history. Truncation at the valid-input caps covers this case. The truncated algorithm is identical on all valid inputs, so neither success nor cost changes, and the lower bound applies to it. No break.

## Remaining notes

Earlier Findings 2–5 (optional circuit-size remark, frontier-paragraph redundancy, N−6 versus N−5, wording of the related-work claim) are editorial or optional. None is a blocker. The delta introduces no new substantive issue.
