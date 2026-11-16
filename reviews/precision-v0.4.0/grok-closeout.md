The packet’s closing lines are the only unread part of the supplied review. I’ll read those and then audit Section 6 against the stated resource contracts.**Verdict: GO.** The revised Section 6 contracts close the earlier bit-budget and workspace gaps. No material finding remains under the stated hypotheses.

**Source SHA-256:** `42f8f7b25ee045d3412440095c3c8719dc380c627aa687b976f03142eec87769`. This is the hash supplied with the packet. It was not recomputed. No files were edited, no citations were opened, and no human, kernel, or numerical validation is claimed.

## Findings

None at blocker or revise severity. The eight listed repairs match the manuscript and the inequalities they are meant to support.

## What was rechecked

The gate contract in Section 6 allows one scalar phase on the whole history-selected operator, controls included, chosen before the operator-norm test. Absolute overlaps are unchanged. A coherent control is part of that operator, so no relative phase inside the gate is discarded. For a unit vector and the phased representative,

\[
2(1-s)\le\|Uu-Vu\|^2\le\delta_j^2,\qquad 1-s^k\le k(1-s),
\]

with \(s=|\langle Uu|Vu\rangle|\). Summing only normalized active mass gives

\[
d_\kappa(A^U,A^V)^2=2\sum_{h\,\mathrm{active}}p_h(1-s_h^{\kappa(h)})\le K\delta_j^2.
\]

Each ordinal frontier therefore adds at most \(\sqrt K\,\delta_j\). Both active-history subscripts are `\mathrm{active}`. Halted leaves are carried and uncharged. The same \(V_h\) is a common block isometry. Fixed power \(k=\lceil 1/\varepsilon\rceil\) and decreasing power \(\kappa(h)=P+1-p(h)\) are applied as separate distances, then the minimum is taken. That is \(K_\varepsilon(P)\), including \(P+1\) at \(\varepsilon=0\). The prefactor is 1 and does not grow with dimension, history count, or inverse branch probability.

The rate term is a different coupling. With the policy and the implemented gates frozen, flag mismatch has probability at most \(1-(1-\tau)^P\le P\tau\). Triangle inequality gives

\[
\mathrm{TV}\le\min\bigl\{1,\sqrt{K_\varepsilon(P)}\textstyle\sum_j\delta_j+P\tau\bigr\}.
\]

A rounded rate that changes a threshold, schedule, or cap is explicitly outside \(P\tau\).

The compilation split adds to \(\delta=2^{-b_g}\). Entrywise complex-modulus error at most \(\delta/(4d_{\mathrm{loc}})\) contributes at most \(\delta/4\) in operator norm through the Frobenius bound \(\|E\|_{\mathrm{op}}\le d_{\mathrm{loc}}\max|E_{ij}|\). Real and imaginary errors \(\delta/(8d_{\mathrm{loc}})\) give modulus at most \(\sqrt2\,\delta/(8d_{\mathrm{loc}})<\delta/(4d_{\mathrm{loc}})\). With \(c_d=\lceil\log_2(8d_{\mathrm{loc}})\rceil\), absolute accuracy \(2^{-(b_g+c_d)}\) meets that entry tolerance. The rounded matrix is not treated as unitary. For \(\|W-U\|\le\delta/4<1\), singular values lie within \(\delta/4\) of 1, so the polar unitary satisfies \(\|U_{\mathrm{pol}}-W\|\le\delta/4\) and \(\|U_{\mathrm{pol}}-U\|\le\delta/2\). Numerical polar and synthesis each receive \(\delta/4\), and \(b_{\mathrm{syn}}=b_g+2\) appears in every synthesis time, length, ancilla, and workspace term. Matrix evaluation stays at \(b_g+c_d\). The four pieces sum to \(\delta\), so the synthesized word can meet \(\|U_h-V_h\|_{\mathrm{op}}\le\delta_j\). Preparation isometries are routed through an effective fixed-dimensional unitary dilation whose description and ancillas are charged. Ancillas are reused serially and returned clean, with cleanup and certified finite arithmetic inside \(S(b)\), \(L(b)\), \(M_S(b)\), and \(a(b)\). The width ledger is \(w+a(b_{\mathrm{syn}})\) once. Unused zero-cap bit budgets are set to zero. \(B_{\mathrm{tr}}\) and \(d_{\mathrm{loc}}\) are the Section 6.4 names.

The displayed budgets match the success split. \(2^H\ge\sqrt K\) and \(b_g=\lceil\log_2(2G/\zeta)\rceil+H\) give \(2^{-b_g}\le\zeta/(2G\sqrt K)\). Likewise \(2^{-b_\varepsilon}\le\zeta/(2P)\). Ideal success at least \(3/4\) and \(\zeta\le 1/12\) remain at least \(2/3\). For ideal success \(2/3\), 27 charged repetitions and majority have failure at most \(\exp(-2\cdot 27\cdot(1/6)^2)=\exp(-27/18)<1/4\). Budgets are recomputed on the enlarged caps.

Under fixed local dimension, uniform effective descriptions from the public input and the realized history, phase-fixed \(\mathrm{SU}(d_{\mathrm{loc}})\) targets, and compiler bounds polynomial in the accuracy length, the compiled cost stays polynomial in the original resources. Bit length is \(O(\log(GPK/\zeta)+\log d_{\mathrm{loc}})\). Descriptions are evaluated only on the realized history. Powers and purifications are proof objects. Dawson–Nielsen polynomiality was not re-audited. It remains a hypothesis of the manuscript.

The search and adversary dependencies still support the theorem. For \(N\ge 12\), \(d_w^2\ge 2-\sqrt3>1/4\) and \((N-6)/4\ge N/8\) give \(Q^2 K\ge N/32\). The construction constants still give \(p\ge m^2/(40N')\), \(s\ge 1/3280\), and failure at most \(e^{-4}<1/12\) over \(B=13120\) charged attempts. The adversary factor obeys \(2\sqrt2/3<17/18\), so \(c_*>1/36\). The README marks 0.4.0 review as in progress and attaches the completed archive claims to 0.3.0.

## Attempted falsifiers

- Misaligned global phase: \(2(1-s)\le\|Uu-e^{i\theta}Vu\|^2\) for every \(\theta\), with equality at the aligned representative. A \(d\)-th-root residual changes the unphased operator norm by \(\Theta(1)\) and is removed by that representative. It is not a counterexample once the representative is fixed. A phase that depends on the control state is still forbidden, and the text forbids it.
- Rare-branch diagnostic: \(b^2\le d^2\) and \(\sum_{j<m}((1-\varepsilon)t)^j\le\min(m,1/\varepsilon)\le K_\varepsilon(m)\), so \(\mathrm{TV}\le K d^2\le\sqrt K\,d\). No \(1/q\) factor appears. The theorem’s linear form is valid and, for tiny \(d\), weaker than this quadratic example.
- Polar budget: \(\delta/4\) (entries) plus \(\delta/4\) (polar-to-rounded gap) plus \(\delta/4\) (numerical polar) plus \(\delta/4\) (synthesis) equals \(\delta\). The condition \(\delta/4<1\) holds for the certified choice \(\delta=2^{-b_g}\le 1\).
- Real/imaginary grid: modulus \(\sqrt2\,\delta/(8d_{\mathrm{loc}})\) is about \(0.707\) of the complex-modulus allowance \(\delta/(4d_{\mathrm{loc}})\). The inequality is strict.
- Rate-policy split: a schedule that moves with the rounded rate can change the transcript by \(\Theta(1)\). The manuscript excludes that case from \(P\tau\).
- Frontier bookkeeping: the same classical history halts in both executions. Exponents depend on the history label, not on mixing the two power arguments inside one distance.
- Zero caps: \(G=0\) leaves the executions identical, and \(P=0\) or \(\varepsilon=1\) forces \(K=1\). The positive-cap formulas are not applied to a zero denominator.
- Section 4 numeric check, unchanged by Section 6: at \(p=1/5\), \(q=4/5\), \(\varepsilon=1/2\), \(g_1=18/25<4/5\), \(g_2=82/125\ge 16/25\), and the two frontiers are \(412/625\ge r^2\) and \(84/125\ge r^3\).

## Nonblocking optional exposition

These do not affect the contracts or the verdict. In Section 6, \(n\) in \(E(n,b)\) and \(M_E(n,b)\) is not given a local definition. It reads as the length of the public classical input. When the rate is exact, the prose allows dropping the factor two in the gate bit budget, while the displayed \(b_g\) keeps \(2G\). That displayed choice remains sufficient.
