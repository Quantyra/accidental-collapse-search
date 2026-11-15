# Independent Review: Non-Claims and Attribution Lens (Revised Source)

**Review Lens:** Non-claims / Attribution  
**Provider Assignment:** agy  
**Candidate Commit:** `b791bd13ec9046a161dfd6afa49f06fef1f8b6e9`  
**Source SHA-256:** `617e873d184ece9c3b51c0a98b1669cc74c2d36a52396a7a35e75e684349885e`  
**Evaluation Date:** 2026-11-15  

---

## 1. Executive Summary and Remit Scope

This independent review evaluates the revised draft manuscript *"Optimal Search with Accidentally Collapsing Measurements"* (version `0.1.0-dev`) and its accompanying public-facing repository files (`README.md`, `SOURCES.md`, `.zenodo.json`, `CITATION.cff`, and `publication/README.md`) under the assigned **Non-Claims and Attribution** lens.

The evaluation was performed strictly against the self-contained review packet provided. In strict adherence to instructions, no repository edits, commands, delegation, external requests, or additional file reads were executed.

### Core Scientific Claim Evaluated
The manuscript establishes that in unstructured search on $N \ge 2$ items with a noiseless oracle and an independent Born sampler that projects the sampled register with probability $\eps$ (with all sampler outcomes and collapse flags deferred until circuit termination), the optimal worst-case total cost for constant-success unique-item identification is:
$$T_*(N,\eps) = \Theta\bigl(N^{1/3} + \sqrt{\eps N}\bigr), \qquad 0 \le \eps \le 1.$$
Total cost accounts for every oracle query $Q$, sampler call $P$, predetermined fresh preparation attempt $R$, and ordinary measurement/reset call $M$ ($T = Q + P + R + M$).

---

## 2. Disposition and Retraction of Initial Findings

### Finding 01 (Previous Finding 01 — LOW): Wide-Register Readout Unit Cost vs. Bit-Length Accounting
* **Initial Status:** Noted that treating wide-register readout $P$ as a unit-cost call in the Abstract and README could obscure bit-level transcript accounting.
* **Revision Disposition:** Fully **RESOLVED**. The revised Abstract (lines 49–50), Introduction (lines 99–103), Section 2 (lines 231–232), Section 4.3 (line 496), and `README.md` (lines 636–637) explicitly clarify that each whole-register readout counts as one call, while transcript storage is accounted separately as $O(P \log N)$ bits.

### Finding 02 (Previous Finding 02 — LOW): Pre-Review Disclaimer Transition upon Completion
* **Initial Status:** Recommended transitioning the pre-review disclaimer ("no separate external-model or human review is represented as completed") once provider CLI reviews were performed.
* **Revision Disposition:** Fully **RESOLVED**. The revised manuscript (Section 5, lines 562–565), `README.md` (lines 642, 664), `.zenodo.json` (line 700), `CITATION.cff` (line 752), and `publication/README.md` (lines 764, 766) accurately disclose that separate CLI AI reviews were conducted, identify that actual scopes, findings, and dispositions are archived in `REVIEW.md`, and reiterate that AI review is neither independent human peer review nor formal certification.

### Finding 03 (Previous Finding 03 — LOW): Abbas et al. Attribution and Formal Retraction
* **Initial Status:** Initial Finding 03 asserted that Abbas et al. (Appendix E.4, Proposition 28) analyzed a single-copy sequential gentleness result with perturbation $\delta \le O(N^{-2/3})$.
* **Coordinator Inspection:** The coordinator inspected the primary proceedings PDF (page 28) and confirmed that Proposition 28 explicitly employs $O(\log N)$ copies and $1/N$-gentleness; the proposed single-copy statement was not present in that proof.
* **Formal Retraction:** This reviewer **formally retracts** the assertion in initial Finding 03 regarding a single-copy $N^{-2/3}$-gentleness result in Abbas et al. Proposition 28. That proposed statement was unsupported by the pinned primary source.
* **Revision Disposition:** Fully **RESOLVED**. The revised manuscript text (Section 1.1, lines 129–131) and `SOURCES.md` (line 679) accurately cite the exact parameters of the primary proof:
  > *"Their construction uses multiple copies with a gentleness assumption on the resulting state: the cited proof uses $O(\log N)$ copies and $1/N$-gentleness."*
  This attribution is now exact, faithful to the primary proceedings, and cleanly distinguishes gentle multi-copy disturbance from independent, rare, order-one projection.

---

## 3. Audit of Non-Claims, Model Boundaries, and Attribution

### 3.1 Non-Claims and Perimeter Demarcation
1. **Postquantum Primitive vs. Physical Quantum Mechanics:**  
   The manuscript unambiguously identifies the Born sampler as a postquantum thought experiment and an information-theoretic primitive (Section 1, lines 71–77; Section 2, lines 206–220). Section 2 rigorously details that retaining the classical record $(y, c=0)$ while leaving the global state undisturbed yields an unnormalized state $\omega_{0,y}(\rho) = (1-\eps)\Tr(\Pi_y \rho)\rho$ that depends quadratically on $\rho$, demonstrating why the retained-record operation cannot be described by an ordinary linear CPTP quantum instrument for $\eps < 1$. Discarding the record yields ordinary dephasing, but retaining it does not.
2. **Physical Hardware Disclaimers:**  
   The Abstract (lines 58–59), Section 1 (lines 76–77), Section 5 (lines 549–554), `README.md`, and `.zenodo.json` consistently disclaim any assertion of physical realizability or fault-tolerant quantum hardware relevance.
3. **Complexity Class Implications (BPP vs. BQP):**  
   The manuscript and public metadata clearly state that this is an oracle-relative query complexity theorem; it leaves the relation between standard classical BPP and quantum BQP completely open (lines 553–554).
4. **Algorithmic Constraints and No-Feedback Rule:**  
   The access model explicitly forbids using deferred sampler outcomes or collapse flags to dynamically steer later gates, queries, preparations, or restarts (lines 178–182). All attempts are predetermined and charged regardless of intermediate success (lines 226–227).

### 3.2 Model Refinements and Mathematical Soundness
1. **$N \ge 2$ Domain and Bounded-$N$ Lower Bound:**  
   The revision explicitly establishes the domain $N \ge 2$ across the Abstract, Theorem 1, and Section 3.5. For $2 \le N < 12$, any zero-query algorithm has an output distribution independent of $w$ and must fail with probability at least $1 - 1/N \ge 1/2 > 1/3$ for some item. Thus $Q \ge 1$, which matches $\Theta(N^{1/3} + \sqrt{\eps N})$ because $N^{1/3} + \sqrt{\eps N} < 6$ in this range. The trivial case $N=1$ is explicitly excluded as requiring no oracle access (lines 423–425).
2. **Distinct Reset Implementations (Measurement vs. Environment):**  
   Section 2 (lines 194–205) and Section 3.1 (lines 296–300) carefully distinguish between *measurement reset* (which performs an ordinary projective measurement and records the classical outcome) and *environment reset* (which swaps to an ancilla and retains the register in an inaccessible quantum purification). Because nonlinear conditional operations can distinguish these implementations, the manuscript does not conflate them, proves that both satisfy the lower-bound potential comparison, and explicitly notes that the main upper-bound construction uses neither.
3. **History-Dependent Exponents and $j$-th Query Frontier Alignment:**  
   To accommodate ordinary-control branches with differing numbers of readouts or query timings, the lower bound uses a history-dependent exponent $\kappa(h) = P + 1 - p(h)$ and aligns branches at the frontier immediately preceding each branch's $j$-th oracle query (lines 367–387). The text explicitly qualifies these frontiers as *analytical observation points* for evaluating the mathematical potential across branches, rather than physical rescheduling or algorithmic feedback.
4. **Conditional Pure-State Approximation Contract:**  
   Section 4.3 (lines 509–528) establishes that approximation bounds must hold on conditional global pure states rather than averaged reduced density matrices, couples the error through the no-intervening-operation transcript, and explicitly disclaims any general contractivity property for nonlinear samplers.

### 3.3 Prior-Work Attribution and Provenance
1. **Algorithmic Template:** Fully and prominently attributed to Aaronson, Bouland, Fitzsimons, and Lee (ABFL, 2016) in Section 1.1, `README.md`, `SOURCES.md`, and `.zenodo.json`.
2. **Ideal Cube-Root Endpoint and Conditional-Copy Device:** Explicitly credited to Miloschewsky and Podder (CCC 2025). The author explicitly disclaims the ideal endpoint and the use of conditional copies as independent contributions (lines 120–122).
3. **Gentle Imperfect Readout Robustness:** Credited to Abbas et al. (NeurIPS 2023, Proposition 28), with exact parameters ($O(\log N)$ copies, $1/N$-gentleness).
4. **Noisy/Faulty Oracle Models:** Regev–Schiff (2008) and Rosmanis (2023) are cited and accurately distinguished based on noise location (oracle noise vs. postquantum readout channel noise).
5. **Passive Measurement Theory:** Fiorentino and Weigert (2025) is cited and distinguished by its composition rules and state-reconstruction cost model.
6. **Mathematical and Distance Tools:** Gilchrist, Langford, and Nielsen (2005) is credited for root fidelity and Bures distance properties.
7. **Perimeter of Literature Claims:** In Section 1.1 (lines 148–151) and `SOURCES.md` (lines 688–693), the author explicitly notes that the literature search was focused rather than exhaustive, documents that recent preprints (Cakan et al., Morimae et al., Lolck et al.) were screened at the abstract level only, and disclaims any exhaustive priority certification.

### 3.4 Verification and Publication Status Hygiene
* **Version Uniformity:** Version `0.1.0-dev` is maintained consistently across `manuscript/main.tex`, `README.md`, `CITATION.cff`, `.zenodo.json`, and `publication/README.md`.
* **Archival and DOI Hygiene:** No DOI is invented or claimed. Zenodo integration is identified strictly as repository setup, without implying that an archival release or formal publication has occurred.

---

## 4. Audit Findings

No **HIGH** or **MEDIUM** findings remain. All three previous low-severity items have been resolved and dispositioned. Only one minor operational observation is noted for future release management:

### FINDING-01 (LOW / Informational)
* **Location:** `publication/README.md`: lines 766–768; `manuscript/main.tex`: line 37; `.zenodo.json`: line 701; `CITATION.cff`: line 730
* **Issue / Scope Context:** Version strings are currently pinned to development draft status (`0.1.0-dev`). While this is entirely truthful and appropriate for the current pre-release archive, transitioning to an archival release (if authorized in the future) will require updating all version fields consistently to a non-dev release tag.
* **Theorem / Publication Blocker:** **No**. Does not block the mathematical theorem or draft archive preparation.
* **Concrete Proposed Action:** When future release authorization is granted, verify that all version strings across the manuscript, CFF metadata, `.zenodo.json`, and package verification records are updated in a single atomic commit as already specified in `publication/README.md`.

---

## 5. Explicit Disclaimers

In accordance with review protocols:
1. This review does **not** certify universal mathematical correctness or formal machine-checked proof (e.g., Lean/Coq).
2. This review does **not** certify absolute scientific novelty or exhaustive priority over unindexed or non-compared literature.
3. This review does **not** certify physical realizability or experimental feasibility.
4. This AI-based review through provider CLIs does **not** constitute independent human peer review or formal certification.

---

## 6. Final Verdict

**Verdict:** **GO**

### Justification:
The revised manuscript and public claims rigorously adhere to all non-claims boundaries and attribution requirements. The scope of the postquantum access model is cleanly demarcated, physical hardware realizations and unconditioned BPP/BQP claims are explicitly disclaimed, prior work (ABFL, Miloschewsky–Podder, Abbas et al., Regev–Schiff, Rosmanis) is credited with exact parameters, and the previous unsupported assertion regarding a single-copy result in Abbas Proposition 28 has been formally retracted and corrected. The public metadata and version disclosures are transparent, truthful, and free of blockers.
