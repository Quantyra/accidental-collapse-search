The supplied packet was reviewed as version 0.4.0, source SHA-256 `af58f74bbc841d7d3e5769f4545919652a2c24272a160e369814c846ced8f6de`. That hash was taken from the review brief and was not recomputed. No files, commands, prior reviews, or external sources were used.

**Verdict: GO-WITH-NOTES.** Theorem 6’s transcript bound holds under its stated isometry contract. The fixed-power and decreasing-power lemmas, ordinal frontiers, and normalized history mass support it. Query, sample, preparation, measurement, repetition, failure, and transcript charges stay polynomial in the stated sense. One explicit bit-budget constant is short, and two exposition points are optional.

## What was checked

Section 6 compares two executions of one finite capped controller and one exact oracle. At each ordinal gate frontier the contract is \(\|U_h-V_h\|_{\mathrm{op}}\le\delta_j\) on a common padded space, tensored with the identity on untouched registers. History probabilities are normalized, so a rare branch does not enter as \(1/p_h\). Halted leaves are carried and receive no gate charge. The same \(V_h\) is a block isometry, so it preserves root fidelity. Between frontiers, exact queries, measurements, sampler calls, and the stated resets use the Section 3 scalar comparisons; exponents are not mixed inside one distance.

The gate algebra is sharp at exponent 1. If \(s=|\langle Uu|Vu\rangle|\) is real and nonnegative, then \(\|Uu-Vu\|^2=2(1-s)\). With \(1-s^k\le k(1-s)\) and \(1-s\le\delta_j^2/2\),
\[
d^2=2\sum_h p_h(1-s_h^{\kappa(h)})\le K\delta_j^2,
\]
so each frontier adds at most \(\sqrt K\,\delta_j\). Thus \(\mathrm{TV}\le\min\{1,\sqrt{K_\varepsilon(P)}\sum_j\delta_j\}\). The prefactor is 1 and does not grow with dimension or with the number of histories. \(K_\varepsilon(P)=\min\{P+1,\lceil 1/\varepsilon\rceil\}\), with the value \(P+1\) at \(\varepsilon=0\), is the same quantity as in the adversary theorem.

The rate term is a separate coupling. While the policy and gates are frozen, flags can be coupled so that the first mismatch has probability at most \(1-(1-\tau)^P\le P\tau\). Triangle inequality gives the combined cap \(\min\{1,\sqrt{K_\varepsilon(P)}\sum\delta_j+P\tau\}\). Rounding \(\varepsilon\) and then changing a threshold, schedule, or cap is outside that term. The search construction does not use it for that purpose: a rational upper estimate \(\bar\varepsilon\in[\varepsilon,\min(1,\varepsilon+1/N')]\) is substituted directly into the parameter rule, and \(\sqrt{\bar\varepsilon N'}\le\sqrt{\varepsilon N'+1}\) changes only constants.

## Finding

**Minor — bit formula versus the entry/synthesis split.** Location: the precision-budget display and the compilation paragraphs in Section 6, including \(\delta\le\zeta/(2G\sqrt K)\), \(b_g=\lceil\log_2(2G/\zeta)\rceil+H\), entry accuracy \(\delta/(4d)\), and \(S(b_g)\), \(E(n,b_g+c_d)\).

The identity \(2^H\ge\sqrt K\) is correct, so \(2^{-b_g}\le\zeta/(2G\sqrt K)\) meets the operator-norm budget \(\delta\). The next paragraph spends \(\delta/4\) on matrix entries and assigns the remaining \(3\delta/4\) to synthesis, but the displayed compiler call is still at \(b_g\), whose tolerance is a full \(\delta\). Saturating both written tolerances allows operator norm \(5\delta/4\). Then
\[
\sqrt K\sum_j\delta_j+P\tau\le\frac54\cdot\frac\zeta2+\frac\zeta2=\frac{9\zeta}8.
\]
For ideal success \(3/4\) and \(\zeta=1/12\), the loss allowed by that saturated reading is \(9/96=3/32\), and
\[
\frac34-\frac3{32}=\frac{21}{32}=\frac23-\frac1{96}.
\]
So those particular constants do not quite force implemented success \(2/3\). The TV theorem is unaffected. Repair is one extra synthesis bit, or an explicit split such as entry tolerance \(\delta/4\) and synthesis tolerance \(\delta/2\). Asymptotic degree is unchanged: accuracy length remains \(O(\log(G/\zeta)+\log K)\) with \(K\le P+1\).

The direct repetition route still clears \(2/3\) under this saturated reading. Hoeffding gives failure at most \(\exp(-2\cdot27\cdot(1/6)^2)=\exp(-27/18)\approx0.223\), so success is at least about \(0.777\). Subtracting \(9\zeta/8\) leaves about \(0.683>2/3\). The tight \(3/4\) bridge is the one that misses.

## Attempted falsifiers

- Gate factor: at \(k=1\) and real positive overlap, \(d=\delta_j\) is achieved by the written inequalities. No off-by-two.
- Rare-branch diagnostic: \(b^2\le d^2\) and \(\sum_{j=0}^{m-1}(1-\varepsilon)^j\le K_\varepsilon(m)\), so \(\mathrm{TV}\le\min\{1,K d^2\}\le\sqrt K\,d\). No inverse-probability factor appears. The theorem’s linear \(\sqrt K\,d\) form is valid and, for tiny \(d\), weaker than this quadratic example.
- Decreasing-power step: \((1-\varepsilon)Ar^{k-1}+\varepsilon C_{k-1}\ge r^k\) for \(A\ge r\) and \(k\ge2\). The cap puts the exponent at least 2 before a sampler call and at least 1 after it.
- Fixed power: weighted AM–GM gives \((1-\varepsilon)A+\varepsilon A^{1-k}\ge A^{1-\varepsilon k}\ge1\) when \(\varepsilon k\ge1\) and \(0<A\le1\).
- Branching numbers at \(p=1/5\), \(q=4/5\), \(\varepsilon=1/2\): \(g_1=18/25<4/5\), \(g_2=82/125\ge16/25\), frontiers \(412/625\ge r^2\) and \(84/125\ge r^3\).
- One-bit adversary check: query mass \((3/4)\cdot(1/2)=3/8\), charge \(2\cdot(3/8)=3/4\), and \(\Phi\) falls from 1 to \(1/4\).
- Search constants: \(p\ge m^2/(4\pi^2 N')\), denominator \(\le41p\), \(s\ge1/3280\), and \(B=13120\) gives failure at most \(e^{-4}<1/12\). Also \(N'<4N\), and \((2t+1)\theta\le1+2/\sqrt{N'}<\pi/2\) for \(N'\ge256\).
- A wrong \(d\)th root of unity changes operator norm by \(\Theta(1)\) while the projective gate is unchanged. The \(\mathrm{SU}(d)\) phase sentence is necessary for the contract. It is not a counterexample once representatives are fixed.
- A schedule that changes with a rounded rate can move a transcript by \(\Theta(1)\), which \(P\tau\) does not cover. The manuscript already excludes that case.

## Costs

Under the hypotheses actually written — fixed local dimension, uniform effective descriptions from the public input and the realized history, phase-fixed \(\mathrm{SU}(d)\) targets, and compiler bounds polynomial in the accuracy length — compiled cost stays polynomial in the original caps. Bit length is \(O(\log(GP/\zeta))\). Elementary words multiply \(G\) by a polynomial in that length. Descriptions are evaluated only on the realized history. Powers and purifications are proof objects.

The search upper bound is polynomial overhead on top of the stated query cost, not a \(\mathrm{poly}(\log N)\) algorithm. For \(N'\ge256\), \(B=13120\) is an absolute constant, \(Q=B(t+1)\), \(P=Br\), \(R=B\), and \(M=0\), with \(m=\Theta(N^{1/3}+\sqrt{\varepsilon N})\) and \(N'/m^2=O(m)\). Nonoracle gates and the scan are \(O(T\log N)\). Transcript storage \(O(P\log N)\) is separate, as are \(\mathrm{poly}(\log N)\) integer parameter operations. The exact Hadamard–\(X\)–Toffoli circuit does not pay synthesis. If those gates are approximate, \(O(\log N)\) accuracy bits are enough for the Section 4 coupling \(\eta\le1/(24Br)\). All \(B\) attempts are charged, including failures. The \(N'<256\) fallback is constant. The lower bound \(T=\Omega(N^{1/3}+\sqrt{\varepsilon N})\) matches this accounting up to the absolute factor already displayed: \(Q+P\ge N^{1/3}/4\) and \(Q\ge\sqrt{\varepsilon N}/8\) for \(N\ge12\).

The 27-fold majority recomputes the budget at caps at most \(27G\) and \(27P\), plus preparation gates, and charges every run and the counter. That Hoeffding bound is correct. Dawson–Nielsen synthesis was not re-audited here; polynomiality remains conditional on the manuscript’s compiler hypotheses.

## Nonblocking exposition

- Working precision inside synthesis has to grow with \(b\). The phrase “constant precision allowances included” is acceptable only as “already inside \(S(b)\), \(L(b)\), \(M_S(b)\), and \(a(b)\).” An \(O(1)\)-bit mantissa does not protect an operator-norm target \(2^{-b}\).
- The ledger adds synthesis ancillas once, as \(w+a(b_g)\). That is valid if those ancillas are reused serially and returned clean. The manuscript does not say this in Section 6.
- Phase fixing is required and stated. No separate bit or arithmetic term is given; it has to be part of the compiler bounds that meet \(\|U_h-V_h\|_{\mathrm{op}}\le\delta_j\).

No human, kernel, or citation-library validation is claimed. The notes do not change Theorem 6, the search \(\Theta\) law, or the adversary bound.
