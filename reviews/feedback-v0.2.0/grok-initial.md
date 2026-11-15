**GO-WITH-NOTES.** No substantive break found in the charged-call theorem. The supplied packet is the v0.2.0 source identified as SHA-256 `b7cecc45d2958fa77e2add9670cb632e8aa3018dc0a6afe5ce05a967b8b07714`. That digest was not recomputed from bytes. Cited PDFs were not opened. No human or machine-formal validation is claimed.

The uniform claim \(T_*(N,\varepsilon)=\Theta(N^{1/3}+\sqrt{\varepsilon N})\) for worst-case \(T=Q+P+R+M\), constant success \(2/3\), and immediate feedback holds on the arguments as written, for \(N\ge 2\) and \(0\le\varepsilon\le 1\).

## Findings

**Minor — transcript bits are an implementation upper bound, not part of \(T_*\).** Abstract; Theorem 1; §Gate, space, and precision costs. Retaining every readout costs \(O(P\log N)\) bits. The decision rule only needs one marked address, so the same query/sampler/preparation schedule can overwrite samples and keep \(O(\log N)\) classical workspace. That does not change \(Q,P,R,M\) or the \(\Theta\) law. The paper’s wording (“uses”, “charged separately”) matches the retain-all schedule.

**Minor — pigeonhole is one label weaker than necessary.** §Success requires distance. At most five labels can have \(z_w>1/6\), so at least \(N-5\) labels have \(z_w\le 1/6\). The text uses \(N-6\). For \(N\ge 12\), \((N-6)/4\ge N/8\) still holds, and \(Q^2\lceil 1/\varepsilon\rceil\ge N/32\), \(Q^2(P+1)\ge N/32\) follow. The constant does not need a repair.

No other cost, precision, cap, or adaptive-history defect rose to a correction of the theorem.

## What was checked

Fixed-power step (Lemma Fixed-power monotonicity, display (eq:fixed)): for integer \(k\) with \(\varepsilon k\ge 1\),
\[
(1-\varepsilon)Ar^k+\varepsilon C_k\ge r^k\bigl((1-\varepsilon)A+\varepsilon A^{1-k}\bigr)\ge r^k A^{1-\varepsilon k}\ge r^k,
\]
using \(C_k\ge r^k/A^{k-1}\), weighted AM–GM, and \(A\le 1\). The exponent \(\lceil 1/\varepsilon\rceil\) stays fixed for every later readout. These copies are only inside the potential.

Decreasing exponent (display (eq:decreasing)): before a call the exponent is at least 2 because \(p(h)\le P\). The scalar
\[
(1-\varepsilon)Ar^{k-1}+\varepsilon C_{k-1}\ge(1-\varepsilon)r^k+\varepsilon r^{k-1}\ge r^k
\]
is monotone for every \(\varepsilon\in[0,1]\), including ideal readouts. History-dependent \(\kappa\) is compared as a number. Bures geometry is used only inside one cut.

Query frontiers: on a prefix-free cut, \(\sum_w a_0(w)\le 1\). Each real query increases \(D=(\sum_w d_w^2)^{1/2}\) by at most \(2\sqrt{K}\), with \(K=\lceil 1/\varepsilon\rceil\) or \(K=P+1\). Identity padding on halted branches adds no \(a_0\) mass and no charged calls. Nonquery steps do not increase \(D\). Final \(D\le 2Q\sqrt{K}\).

Success-to-distance: standard total variation is at least \(1/2\), root affinity at most \(\sqrt{3}/2\), and \(d_w^2\ge 2-\sqrt{3}>1/4\). With \(D^2\ge N/8\) this is exactly \(N/32\). Then \(\lceil 1/\varepsilon\rceil\le 2/\varepsilon\) gives \(Q\ge\sqrt{\varepsilon N}/8\), and \(Q^2(P+1)\le(Q+P)^3\) gives \(Q+P\ge N^{1/3}/4\). Sum-of-caps \(T\) and worst-branch total \(W\) satisfy \(W\le T\le 4W\), so both are \(\Theta(N^{1/3}+\sqrt{\varepsilon N})\). For \(2\le N<12\), zero-query outputs are independent of \(w\), so \(T\ge 1\) while \(N^{1/3}+\sqrt{\varepsilon N}<6\).

Upper schedule (displays (eq:parameters)–(eq:resources)): \(p\ge m^2/(4\pi^2 N')\ge m^2/(40N')\), \(\varepsilon\le 40p\), \(rp\ge 1/40\), and \(s\ge 1/3280\). With \(B=13120\), failure is at most \(e^{-4}<1/12\). Here \(4\pi^2<40\) and \(1-e^{-x}\ge x/2\) on \([0,1]\) both hold. \(N'/m^2\le m+O(1)\), so \(Q\), \(P\), and \(R=B\) are all \(O(N^{1/3}+\sqrt{\varepsilon N})\). An additive \(1/N'\) upper estimate on \(\varepsilon\) only changes constants. For trace distance \(\eta\le 1/(24Br)\) on each attempt’s pure state before readout, the coupling loss is at most \(1/24\), and success stays above \(2/3\). That coupling uses the unchanged state on non-collapse; it is not a general nonlinear contraction.

The branching check recomputes exactly: \(g_1=18/25<4/5\), \(g_2=82/125\ge 16/25\), fixed-power frontier \(412/625\ge r^2\), decreasing frontier \(84/125\ge r^3\).

## Attempted counterexamples

- Split caps: one branch holds all queries, another holds all samples. Global \(P\) still sets \(\kappa\le P+1\) on every branch, and \(T\le 4W\). The product bound still forces both the cap sum and the worst branch.
- Early abort, flag-triggered restart, or a geometric number of attempts. Worst-case branches still pay the full cap. Expected and unbounded stopping are outside the stated claim.
- One wide readout of many copies, or \(P=O(1)\). Then \(Q^2(P+1)=\Omega(N)\) forces \(Q=\Omega(\sqrt N)\).
- Bitwise sampling. That only increases \(P\). The matching upper bound is allowed to read the address and mark bit in one call.
- Collapse confined to an ancilla, with the query register left intact. Ordinary and sampler steps stay monotone on the global conditional state, so this does not undercut \(D\).
- Discarded-record dephasing, reduced-state nonlinear updates, free unknown-\(\varepsilon\) calibration, and noisy oracle calls. These are different contracts; the paper excludes them rather than deriving them.
- Unpowered potential \(k=1\) at \(\varepsilon=1/2\). The paper’s own point \(g_1<r\) is a genuine failure of that comparator; \(k=\lceil 1/\varepsilon\rceil\) is doing necessary work.
- Coherent preparation error only on an averaged reduced state. That does not control this sampler’s transcript. The stated pure-state, per-attempt hypothesis does.

External search-model sentences (persistent CQP, the MP feedback question, stateless circuit sampling) are used only as the manuscript states them. They are not re-established here.
