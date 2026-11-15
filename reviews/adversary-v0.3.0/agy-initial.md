### Independent Provider Review: Non-Claims and Attribution Lens (v0.3.0)

**Source SHA-256:** `9fb7efb8a19ffcdaedb5b8bd286f51c8802b4f0b80a684151cbf6a768872d1d0`  
**Review Focus:** Audit of scientific claims, non-claims boundaries, attribution of prior work, metadata alignment, and verification of the new general positive-adversary extension (Theorem 2) against the supplied primary-source evidence.  
**Verdict:** **GO-WITH-NOTES**

---

### 1. Executive Summary & Core Verdict

The v0.3.0 manuscript and its public metadata files ([`README.md`](initial-agy-packet.txt#L984), [`.zenodo.json`](initial-agy-packet.txt#L955), and [`SOURCES.md`](initial-agy-packet.txt#L1028)) cleanly delineate the scope of the theoretical results. 

The primary addition in v0.3.0 is **Theorem 2** ([lines 134–148](initial-agy-packet.txt#L134-L148)), which establishes a positive-adversary query bound:
$$Q \min\{P+1, \lceil 1/\eps \rceil\} \ge c_* \operatorname{Adv}_+(f) \ge \operatorname{Adv}_+(f)/36$$
for every finite Boolean promise problem $f$, evaluated under the persistent-feedback, independent-collapse model.

The audit confirms:
1. **Positive vs. Signed Adversary:** The manuscript explicitly and repeatedly restricts the theorem to the entrywise-nonnegative spectral adversary $\operatorname{Adv}_+(f)$ and emphasizes that the proof does not extend to signed-weight general adversary methods.
2. **Attribution:** Foundational adversary frameworks, the equivalence of positive spectral and positive weighted schemes, Perron-Frobenius eigenvector weighting, and standard certificates (such as hypercube parity) are properly credited to Miloschewsky--Podder \cite{mp} and \v{S}palek--Szegedy \cite{ss}.
3. **Hierarchy of Lower Bounds:** The text preserves the distinction between general Boolean promise bounds and search: it explicitly emphasizes that the search bound from Theorem 1 ($\Theta(N^{1/3} + \sqrt{\eps N})$) remains strictly sharper than the adversary bound on unstructured search.
4. **Non-Claims Integrity:** The work explicitly refrains from claiming physical feasibility, realization on physical noisy quantum hardware, ordinary $\mathsf{BPP}$ vs. $\mathsf{BQP}$ separation/collapse, efficient certificate discovery, or formal verification.
5. **Finite Demonstrations:** Numerical and symbolic examples (such as Section 4.4 and Section 5.4) are labeled as checks, bookkeeping illustrations, or negative controls, not as mathematical proofs.

There are **no correctness blockers**. Several minor expository observations are recorded below under **GO-WITH-NOTES**.

---

### 2. Detailed Audit by Review Dimensions

#### A. Distinction Between General Positive Adversary and Signed Adversary
- **Verification:**
  - In [lines 134–148](initial-agy-packet.txt#L134-L148) (Theorem 2) and [lines 647–658](initial-agy-packet.txt#L647-L658), $\Gamma$ is defined as a non-zero, real symmetric, **entrywise-nonnegative** matrix with $\Gamma_{xy} = 0$ whenever $f(x) = f(y)$.
  - In [line 658](initial-agy-packet.txt#L658), the author states: *"This is the positive spectral convention of \cite{ss}, not the signed-weight general adversary."*
  - In [lines 731–732](initial-agy-packet.txt#L731-L732): *"Using $K=P+1$ for varying exponents is valid because all summands in the pairwise bound are nonnegative. This reasoning does not justify a signed-weight extension."*
  - In [lines 813–814](initial-agy-packet.txt#L813-L814): *"No efficient certificate discovery, signed adversary theorem, physical realization or general classical simulator follows from this result."*
  - In [`README.md` (line 987)](initial-agy-packet.txt#L987) and [`SOURCES.md` (line 1033)](initial-agy-packet.txt#L1033): identical explicit distinctions are made.
- **Finding:** The boundary between the positive adversary method and the signed (Høyer–Lee–\v{S}palek / Reichardt) general adversary is maintained with complete mathematical accuracy.

#### B. Attribution of Prior Adversary Work and Parity Certificate
- **Verification:**
  - **Miloschewsky & Podder (2025):** Properly credited in [lines 166–168](initial-agy-packet.txt#L166-L168) for proving the ideal PDQP positive weighted bound $QP = \Omega(1/v_{\max})$ (\cite[Lemma 4.3]{mp}), as well as the initial open question regarding noise and outcome feedback (\cite[Section 1.5]{mp}).
  - **\v{S}palek & Szegedy (2006):** Properly credited in [lines 168–174](initial-agy-packet.txt#L168-L174) and [lines 657–658](initial-agy-packet.txt#L657-L658) for the standard nonnegative spectral adversary definition and the equivalence between positive weighted and spectral adversary methods (\cite[Theorem 3.1]{ss}).
  - **Parity Certificate:** In [lines 777–789](initial-agy-packet.txt#L777-L789) (Corollary 3), the hypercube adjacency certificate for $n$-bit parity ($\|\Gamma\|=n$, $\|\Gamma \circ D_i\|=1$) is explicitly marked: *"This is an application of a standard certificate."*
  - **Other Works:** Abbas et al. \cite{abbas} (gentle measurement robustness on multiple copies), Regev–Schiff \cite{rs} / Rosmanis \cite{rosmanis} (oracle-noise models), and Fiorentino–Weigert \cite{fw} (passive measurements) are accurately differentiated in Section 1.1 and [`SOURCES.md`](initial-agy-packet.txt#L1042-L1053).
- **Finding:** Attribution is transparent and thorough.

#### C. Search Bound Sharpness vs. General Adversary Bound
- **Verification:**
  - For unstructured search, the positive adversary gives $\operatorname{Adv}_+(f) = \Theta(\sqrt{N})$. Applying Theorem 2 would only yield $Q \min\{P+1, \lceil 1/\eps \rceil\} = \Omega(\sqrt{N})$ (or $Q+P = \Omega(N^{1/4})$ in the ideal case), which is known to be loose compared to the optimal cube-root scaling.
  - The manuscript makes this distinction clear:
    - [Lines 152–154](initial-agy-packet.txt#L152-L154): *"The sharper search bound in Theorem~\ref{thm:main} is retained."*
    - [Lines 788–789](initial-agy-packet.txt#L788-L789): *"For search, the stronger bound of Theorem~\ref{thm:main} remains the appropriate guarantee."*
    - [`README.md` (line 987)](initial-agy-packet.txt#L987) and [`.zenodo.json` (line 958)](initial-agy-packet.txt#L958): repeated verbatim.
- **Finding:** The work avoids claiming that the general adversary subsumes or matches the specialized root-fidelity search bound.

#### D. Non-Claims on Physics, BPP/BQP, and Efficient Discovery
- **Verification:**
  - **Physical Feasibility / Hardware:** Disclaimed in [lines 60–61](initial-agy-packet.txt#L60-L61), [lines 78–79](initial-agy-packet.txt#L78-L79), [lines 813–815](initial-agy-packet.txt#L813-L815), and [lines 859–864](initial-agy-packet.txt#L859-L864).
  - **$\mathsf{BPP}$ vs. $\mathsf{BQP}$ Complexity:** Explicitly noted in [line 61](initial-agy-packet.txt#L61) and [line 864](initial-agy-packet.txt#L864) (*"The interpolation is an oracle-model result, with the ordinary BPP/BQP question left open."*).
  - **Efficient Certificate Discovery:** Acknowledged in [lines 150–152](initial-agy-packet.txt#L150-L152) and [lines 773–775](initial-agy-packet.txt#L773-L775) (*"Matrices, eigenvectors and complete histories may be exponentially large analytical certificates. The controller is not given their amplitudes or an efficient way to find them."*).
- **Finding:** All non-claims boundaries are cleanly articulated.

#### E. Epistemic Status of Finite Demonstrations and Diagnostics
- **Verification:**
  - Section 4.4 ([lines 626–642](initial-agy-packet.txt#L626-L642)): Explicitly designated as a *"symbolic check and negative control"*, noting that *"The quantified local inequalities and finite-tree induction prove the general claim."*
  - Section 5.4 ([lines 791–805](initial-agy-packet.txt#L791-L805)): Designated as a *"symbolic family [that] checks the stopping bookkeeping; the arbitrary-tree proof, not small-case agreement, establishes the theorem."*
  - Evidence Disclosure ([lines 867–877](initial-agy-packet.txt#L867-L877)): Clarifies that the archive's finite diagnostic receipts predate the extensions and do not establish universal mathematical claims.
- **Finding:** Diagnostic demonstrations are not conflated with general analytic proofs.

#### F. Metadata and Synchronous Versioning
- **Verification:**
  - **Title:** Identical across LaTeX ([line 30](initial-agy-packet.txt#L30)), [`.zenodo.json` (line 957)](initial-agy-packet.txt#L957), and [`README.md` (line 985)](initial-agy-packet.txt#L985).
  - **Version & Date:** Consistent across all documents (`0.3.0`, `November 15, 2026`).
  - **Author & ORCID:** Consistent (`Daniel Fredriksen`, `Quantyra Inc.`, `0009-0002-9123-7435`).
  - **Abstract / Description:** Both describe the updated dual theorems (search cost $\Theta(N^{1/3}+\sqrt{\eps N})$ and adversary bound $QK_\eps(P) \ge \operatorname{Adv}_+(f)/36$).
- **Finding:** Metadata synchronization is exact.

---

### 3. Findings and Notes

| ID | Location | Severity | Category | Description | Proposed Action |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **N-01** | [`manuscript/main.tex#L767-L770`](initial-agy-packet.txt#L767-L770) | Low / Exposition | Derivation Clarity | Equation (26) combines two separate lower bounds: $W = \Omega(\sqrt{\operatorname{Adv}_+(f)})$ (from $Q(P+1)$) and $W = \Omega(\eps \operatorname{Adv}_+(f))$ (from $Q \lceil 1/\eps \rceil \le 2Q/\eps$). The text states the resulting sum without briefly reminding the reader that this is the combination of the two independent cases (similar to [lines 513–514](initial-agy-packet.txt#L513-L514) for search). | Optional: Add a brief phrase stating *"Combining the maximum of the two bounds gives..."* |
| **N-02** | [`manuscript/main.tex#L777-L781`](initial-agy-packet.txt#L777-L781) | Low / Exposition | Boundary Clarification | Corollary 3 states that for $n$-bit parity at any fixed $\eps > 0$, $\Omega(n)$ queries are required *"irrespective of the sampler cap"*. This is correct because $\lceil 1/\eps \rceil = O(1)$ renders $P$ irrelevant in the bound. However, at $\eps = 0$, $Q(P+1) = \Omega(n)$ allows sublinear queries if $P$ is large. | Optional: Add a brief note explicitly contrasting this with the $\eps = 0$ case where unbounded sampling can reduce query counts, highlighting the fragility of parity query speedups to non-zero collapse rates. |
| **N-03** | [`SOURCES.md#L1033-L1070`](initial-agy-packet.txt#L1033-L1070) | Informational | Attribution Scope | Specific external commit identifiers (`3781d76b...`, `9c51e117...`) and proof SHA-256 hashes are cited for internal provenance. | None needed; the manuscript notes these are self-contained archive records and not external dependencies. |

---

### 4. Verification Boundaries & Remaining Limitations

1. **Supplied Evidence vs. Independent Literature Verification:**  
   Per the review constraints, this evaluation was performed solely against the frozen review packet without external web access, live repository fetching, or author correspondence. Citations to external literature (such as \v{S}palek--Szegedy 2006, Miloschewsky--Podder 2025, Aaronson et al. 2016, and Abbas et al. 2023) were audited based on the excerpts, mathematical formulas, and contextual arguments reproduced within the packet.
2. **AI Review Status:**  
   This evaluation constitutes an automated, independent non-claims and attribution audit. As stated in the manuscript disclosure, it is distinct from human peer review or formal mathematical machine certification (e.g., Lean).

---

### 5. Final Recommendation

**GO-WITH-NOTES.** The revision satisfies all attribution, non-claims, and metadata criteria required for v0.3.0 release readiness. The minor notes (N-01 and N-02) are optional expository polish and do not impede progression.
