**GO-WITH-NOTES.** The new definition makes the factor-four sandwich valid and does not invalidate the charged-call theorem or the prior resource audit. No new substantive blocker.

**Source SHA-256 (packet-supplied, not recomputed here):** `47384ca46a9b823927da5784ea9d67a1cb14b18d10cfd8a958efb21e56e6e1d3`

The changed cost sentence in Section 2 now takes \(Q,P,R,M\) to be the smallest worst-case caps on valid marked inputs and complete branches, and states that these caps are the corresponding branch maxima. If \(W\) is the worst-case sum of those four call counts on one complete marked branch, then \(W\le T\le 4W\): each branch sum is at most \(T\), and each individual maximum is attained on some marked branch, so it is at most \(W\). The same \(\Theta(N^{1/3}+\sqrt{\varepsilon N})\) law therefore holds for both \(T\) and \(W\). The upper schedule still meets those maxima by running every predetermined attempt, so \(Q=B(t+1)\), \(P=Br\), \(R=B\), and \(M=0\) are unchanged.

The same paragraph caps every execution, including the reference oracle \(O_0\), by halting before a cap is exceeded. Marked-input executions are unchanged because those caps are already their branch maxima. The lower-bound tree stays finite, with at most \(Q\) query frontiers and \(p(h)\le P\), so both \(D\le 2Q\sqrt{K}\) comparisons and \(Q^2(P+1)\ge N/32\), \(Q^2\lceil 1/\varepsilon\rceil\ge N/32\) still apply. Finite-support input-independent randomness matches the finite-tree induction. The fixed-power step, decreasing-exponent step, frontier padding, success-to-distance step, parameter bounds, and pure-state coupling are untouched.

The corollary only records the \(U_i/M_i\) inclusion, charges each full-register sample, and disclaims a query-only bound with unlimited free samples and an exact elementary-gate runtime. That narrows the external reading. It does not change \(T_*\). The bibliography size change is layout only.

The two earlier notes stay notes. Transcript bits are a retain-all upper bound outside \(T_*\), and the pigeonhole uses \(N-6\) where \(N-5\) is available. For \(N\ge 12\), \((N-6)/4\ge N/8\) still yields \(N/32\). Neither one breaks the theorem.

Cited PDFs were not opened. No human or machine-formal validation is claimed.
