The source SHA-256 is `9fb7efb8a19ffcdaedb5b8bd286f51c8802b4f0b80a684151cbf6a768872d1d0`. The verdict is **GO**.

This is an AI review of the frozen packet only. It is not human peer review or formal certification. Earlier review outcomes were not treated as clearance. No files were modified and no external sources were opened. The proof was checked as self-contained. Citations were not re-fetched.

No correctness blockers and no optional-exposition defects were found. No repair is proposed.

## New theorem

Theorem `thm:adversary` and Section "Positive adversaries with feedback" support

\[
QK_\varepsilon(P)\ge c_*\operatorname{Adv}_+(f)\ge\operatorname{Adv}_+(f)/36,
\]

with \(c_*=(1-2\sqrt2/3)/2=(3-2\sqrt2)/6=1/(18+12\sqrt2)>1/36\), and with \(K_\varepsilon(P)=P+1\) at \(\varepsilon=0\) and \(\min\{P+1,\lceil1/\varepsilon\rceil\}\) otherwise. The abstract, README, `.zenodo.json`, and `SOURCES.md` state the weaker \(1/36\) form and the \(\varepsilon=0\) special case. They do not overstate the theorem.

The checked steps are these.

- The nonnegative unit maximizer exists without irreducibility. For a real symmetric entrywise-nonnegative \(\Gamma\), if \(\Gamma u=\lambda u\) and \(|\lambda|=\|\Gamma\|\), then \(v=|u|\) satisfies \(v^T\Gamma v\ge|u^T\Gamma u|\) and hence equals \(\|\Gamma\|\). A symmetric Rayleigh maximizer is an eigenvector, so the proof never divides by an entry of \(v\).
- Both potentials are monotone on nonquery forests. Fixed \(k=\lceil1/\varepsilon\rceil\) uses Lemma `lem:fixed`. The decreasing rule \(\kappa(h)=P+1-p(h)\) uses the displayed estimate \((1-\varepsilon)Ar^{k-1}+\varepsilon C_{k-1}\ge r^k\), including \(\varepsilon=0\). Before a sampler call the cap forces the exponent to be at least 2. Entrywise \(\Gamma_{xy}\ge0\) preserves the pair bounds. Equal histories select equal operations, so immediate feedback stays inside the induction.
- One query layer drops \(\Phi\) by at most \(2K\Lambda_\Gamma\). The identity \(O_x^\dagger O_y=I-2\sum_{i:x_i\neq y_i}\Pi_{h,i}\) gives the factor 2. For overlaps in \([0,1]\), \(|r^k-r'^k|\le k|r-r'|\). Replacing the history exponent by \(K\in\{\lceil1/\varepsilon\rceil,P+1\}\) is valid because every summand is nonnegative. The same bound does not extend to signed weights, as the text says.
- There is no branch-count factor. With \(a_x^{h,i}=v_x\sqrt{p_x(h)}\|\Pi_{h,i}\psi_{x,h}\|\),

\[
\sum_{h,i}\|a^{h,i}\|_2^2
=\sum_x v_x^2\sum_h p_x(h)\sum_i\|\Pi_{h,i}\psi_{x,h}\|^2
\le1.
\]

Halted leaves, unequal sample counts, and history-selected registers are included at their actual probabilities. Identity padding adds no calls and no query mass.

- Terminal separation matches the stated constant. Success \(2/3\) on opposite outputs gives total variation at least \(1/3\) in the half-\(L_1\) convention already used for search. Affinity is at most \(2\sqrt2/3\). Thus \(\Phi_{\mathrm{final}}\le\beta\|\Gamma\|\). Chaining this with nonquery monotonicity produces \(c_*\), and \(2\sqrt2/3<17/18\) produces \(1/36\).
- The two applications are independent, so the minimum is legitimate: each of \(Q(P+1)\) and, for \(\varepsilon>0\), \(Q\lceil1/\varepsilon\rceil\) is at least \(c_*\operatorname{Adv}_+(f)\).

The one-bit stopping check is numerically consistent. For \(\Gamma=\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\), \(v=(1,1)/\sqrt2\), and one sample of an input-independent \(\lvert++\rangle\), post-sampler \(\Phi=1\), the query moves \(\Phi\) to \(1/4\), the query mass is \((3/4)(1/2)=3/8\), and the exponent-one charge is \(2(3/8)=3/4\). Splitting by the collapse flag or by \(t\) unused fair bits does not change that charge. Success is 1 on \(x=0\) and \(3/4\) on \(x=1\), with caps \(Q=P=1\).

## Checklist

- Caps are worst-case branch maxima over promised inputs. Finite controllers are truncated at those caps. The reference and off-promise strings carry no success requirement. The adversary frontiers use at most \(Q\) layers.
- Failed trials, feedback restarts, query-dependent preparations, both specified reset implementations, and ordinary partial measurements are inside \(W\) and \(T=Q+P+R+M\), with \(Q,P,R,M\le W\le T\le4W\). No expected-cost or unbounded stopping-time claim is made. The search construction pays all \(B=13120\) predetermined attempts.
- A whole-register readout is one sampler call. Transcript storage is separate, at \(O(P\log N)\) bits. Quantum space is \(O(\log N)\) because the attempt count is an absolute constant. Gates and scheduling are \(O((T+1)\log N)\), with \(\operatorname{poly}(\log N)\) parameter arithmetic. Output bits are not free.
- The known-rate contract is an upper estimate \(\bar\varepsilon\in[\varepsilon,\min(1,\varepsilon+1/N')]\), with integer binary search. The preparation coupling is only for the no-intervening-operation search circuit: trace distance \(\eta\le1/(24Br)\) on each conditional global pure state. An averaged reduced state is explicitly not enough. The adversary section does not import that coupling. A hypothetical whole-history failure \(\eta<1/2\) replaces \(c_*\) by \((1-2\sqrt{\eta(1-\eta)})/2\), which correctly recovers \(c_*\) at \(\eta=1/3\).
- Parity is correct for fixed \(\varepsilon>0\). The hypercube adjacency matrix has norm \(n\), and each \(\Gamma\circ D_i\) is a perfect matching of norm 1, so \(\operatorname{Adv}_+\ge n\). The fixed-power bound gives \(\Omega(n)\) queries for any sampler cap. Reading every bit is an \(O(n)\) query upper bound and pays its measurements. Search keeps the sharper \(Q^2K\ge N/32\) law rather than the weaker positive-adversary consequence.
- The total-call display \(W=\Omega(\sqrt{\operatorname{Adv}_+(f)}+\varepsilon\operatorname{Adv}_+(f))\) follows from \(Q(P+1)\le W(W+1)\le2W^2\) and \(\lceil1/\varepsilon\rceil\le2/\varepsilon\). It is a uniform lower bound, not a bit-runtime or matching upper bound. The manuscript says so.
- Certificate discovery is not described as efficient. The manuscript, README, Zenodo record, and `SOURCES.md` all say that matrices, eigenvectors, and complete histories may be exponentially large analytical certificates.
- Feedback and unequal stopping remain in the model. Frontiers align each branch at its own next query. The controller may use outcomes and flags immediately. Hiding flags is stated only as a search-cost invariance, and the upper search algorithm does not read them.

The inherited search arithmetic also matches the text: \(D\le2Q\sqrt K\), \(D^2\ge N/8\) for \(N\ge12\), hence \(N/32\); the parameter bounds give success at least \(1/3280\) per attempt; \(B=13120\) leaves failure at most \(e^{-4}<1/12\). The branching negative control evaluates to the printed fractions \(18/25\), \(82/125\), \(412/625\), and \(84/125\).

## Remaining limitations

These are limits of the stated model, not defects.

- The result concerns this noiseless-oracle, independent-collapse sampler. It does not give a physical implementation, a classification of all noisy PDQP or adaptive CQP, or an ordinary BPP versus BQP consequence.
- Only the positive spectral adversary is proved. Signed weights, efficient certificate finding, and a general classical simulator are not obtained.
- The factor \(1/36\) and the search factors \(32\) and \(8\) are sufficient absolute constants, not optimal constants. Search remains stronger than substituting \(\operatorname{Adv}_+=\Theta(\sqrt N)\) into the new product bound.
- \(T\) does not include gate, transcript, space, or precision cost. Unknown-\(\varepsilon\) calibration and extra oracle or gate noise are outside the contract.
- The \(\Omega(\sqrt{\operatorname{Adv}_+}+\varepsilon\operatorname{Adv}_+)\) form is what holds uniformly. On a particular algorithm with \(P=0\) it is weaker than the direct bound \(Q=\Omega(\operatorname{Adv}_+)\).
- The literature comparison is a bounded primary-source comparison, not an exhaustive priority claim.
- The preserved finite diagnostics predate the feedback and adversary arguments and are not a universal proof.
