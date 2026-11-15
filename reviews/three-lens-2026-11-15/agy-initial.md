# Independent Review: Non-Claims and Attribution Lens

**Review Lens:** Non-claims / Attribution  
**Provider Assignment:** agy  
**Candidate Commit:** `b791bd13ec9046a161dfd6afa49f06fef1f8b6e9`  
**Source SHA-256:** `c8c3465e0ec9cddb825b47935efead06bba0c4ad292c1afe81898aa2c755a2fa`  
**Evaluation Date:** 2026-11-15  

---

## 1. Executive Summary & Model/Proof Analysis

The review packet evaluates the draft manuscript *"Optimal Search with Accidentally Collapsing Measurements"* (v0.1.0-dev) along with its accompanying repository files (`README.md`, `SOURCES.md`, `.zenodo.json`, `CITATION.cff`, and `publication/README.md`).

The core scientific contribution is an informal analytic theorem establishing that in an unstructured search setting with a noiseless oracle and a hypothetical Born sampler that independently collapses the sampled register with probability $\eps$ (with outcomes and flags deferred until the circuit terminates), the optimal constant-success query/readout cost is:
$$T_*(N,\eps) = \Theta\bigl(N^{1/3} + \sqrt{\eps N}\bigr), \qquad 0 \le \eps \le 1.$$

### Mathematical and Proof Architecture Audit
1. **Access Model and Record-Retaining Semantics:**  
   The sampler operates on conditional global pure states $\psi$ in an arbitrary Hilbert space $\mathcal{H}_S \otimes \mathcal{H}_W \otimes \mathcal{H}_R$ (sampled register, workspace, inaccessible reference/environment). With probability $1-\eps$, the state remains $\psi$ while recording the Born outcome $y$; with probability $\eps$, the state projects to $\frac{\Pi_y \psi}{\sqrt{p_y}}$.  
   The manuscript rigorously identifies in Section 2 (lines 193–207) that conditioned on classical outcomes, the unnormalized state on the non-collapsing branch is $\omega_{0,y}(\rho) = (1-\eps)\Tr(\Pi_y \rho)\rho$. Because this depends quadratically on $\rho$, retaining the classical record $(y, c=0)$ is *not* an ordinary linear CPTP quantum instrument for $\eps < 1$. Thus, standard quantum channel theorems for noisy oracles or dephasing cannot be transferred directly.
2. **Fixed-Power Conditional-History Potential:**  
   The lower bound constructs a mathematical potential on the complete conditional classical history $h$:
   $$\Sigma_a^{(k)} = \bigoplus_h p_a(h) \bigl(\ket{\psi_{a,h}}\bra{\psi_{a,h}}\bigr)^{\otimes k}, \qquad F_k(a,b) = \sum_h \sqrt{p_a(h)p_b(h)} \, |\ip{\psi_{a,h}}{\psi_{b,h}}|^k.$$
   In Lemma 3, using weighted AM–GM with weights $1-\eps$ and $\eps$, the non-decrease of $F_k$ under sampler calls requires:
   $$(1-\eps)A + \eps A^{1-k} \ge A^{1-\eps k} \ge 1 \quad \text{for } A \le 1 \text{ and } \eps k \ge 1.$$
   Setting $k = \lceil 1/\eps \rceil$ keeps the potential monotonically non-decreasing under *arbitrarily many* sampler readouts.
3. **Query Sensitivity and Bures Hybrid Bound:**  
   Under a query $O_w$, the overlap of the reference state with its perturbed copy is bounded by $1 - |1 - 2a|^k \le 2ka$. By Minkowski's inequality, the root sum-of-squares Bures distance $D = (\sum_w d_w^2)^{1/2}$ increases by at most $2\sqrt{k}$ per oracle call. Requiring constant-success distinguishing from an uninformative reference requires $D^2 \ge N/8$ for $N \ge 12$, yielding $4Q^2 k \ge N/8 \implies Q^2 \lceil 1/\eps \rceil \ge N/32$.
4. **Matching Construction and Resource Accounting:**  
   The upper bound executes $B = 13120$ pre-scheduled independent attempts of $t = \lfloor m/4 \rfloor$ Grover iterations and $r = \lceil N'/m^2 \rceil$ sampler readouts, where $m = \lceil \max\{(N')^{1/3}, \sqrt{\eps N'}\} \rceil$. The single-attempt success probability is derived exactly as:
   $$s(p, r, \eps) = \frac{p\{1 - [(1-p)(1-\eps)]^r\}}{p + \eps - p\eps} \ge \frac{1}{3280},$$
   ensuring overall failure probability $\le e^{-4} < 1/12$. The resource counts ($Q = B(t+1)$, $P = Br$, $R = B$, $M = 0$) match the lower bound up to absolute constant factors across the entire interval $\eps \in [0, 1]$.

---

## 2. Audit of Non-Claims, Attribution, and Scope Boundaries

### 2.1 Distinction Between Hypothetical Sampler and Ordinary Quantum Instrument
- **Manuscript:** Clearly demarcates that the non-collapsing Born sampler is a postquantum thought experiment and an information-theoretic primitive (Section 1, lines 63–77; Section 2, lines 193–207). It explicitly demonstrates why discarding the classical measurement record yields ordinary dephasing, whereas retaining the non-disturbing classical outcome violates linearity.
- **Supporting Docs (`README.md`, `.zenodo.json`, `publication/README.md`):** Consistently describe the model as a "hypothetical Born sampler" and a "postquantum access model." No claim is made that this primitive is physically realizable with standard quantum gates or open-system Lindbladian dynamics.

### 2.2 Purity, Reference Semantics, and Arbitrary Entangled Workspace
- **Semantics:** The model defines state updates on normalized global pure states $\psi$, representing mixed initial states or environmental interactions via an input-independent global purification.
- **Entangled Workspace:** Remark 4 (lines 487–494) provides a counterexample demonstrating that collapse of the sampled register $S$ does not collapse an unmeasured data register $D$, refuting any naive assumption that noise causes an automatic global reset. The complete-history potential $\Sigma_a^{(k)}$ rigorously accommodates arbitrary workspace entanglement without loss of bound validity.

### 2.3 Physical Claims and BPP/BQP Implications
- **Physical Feasibility:** The manuscript explicitly disclaims physical hardware realizations (Abstract, line 58; Section 1, line 76; Section 5, line 497).
- **Complexity Class Consequences:** The author explicitly states in Section 5 (lines 497–501), `README.md`, and `.zenodo.json` that the result is strictly an oracle-relative query complexity bound and leaves the unconditioned relation between ordinary classical BPP and quantum BQP completely open.

### 2.4 Attribution of Ideal Endpoint, Algorithmic Template, and Proof Techniques
- **Algorithmic Template:** Fully and prominently attributed to Aaronson, Bouland, Fitzsimons, and Lee (ABFL, 2016) in Section 1.1, `README.md`, `SOURCES.md`, and `.zenodo.json`.
- **Ideal Cube-Root Endpoint & Conditional-Copy Precedent:** The $\Omega(N^{1/3})$ lower bound and the initial conditional-copy/fidelity methodology are attributed to Miloschewsky and Podder (CCC 2025). The author explicitly clarifies in Section 1.1 (lines 120–122):
  > *"We explicitly reconstruct the ideal bound inside our history model; we do not claim that endpoint or the use of conditional copies as a separate contribution."*
- **Mathematical Tools:** Standard Bures distance properties, Jensen's inequality, weighted AM–GM, and root-fidelity relations are attributed to Gilchrist, Langford, and Nielsen (2005) and standard analysis.

### 2.5 Abbas et al. Gentle-Readout Comparison
- **Prior Art Distinction:** Abbas et al. (NeurIPS 2023, Appendix E.4, Proposition 28) demonstrated that gentle imperfect measurements (where disturbance per readout is uniformly bounded by a small parameter $\delta$) can support cube-root search.
- **Accidental Collapse vs. Gentle Readout:** The manuscript (Section 1.1, lines 127–135) and `SOURCES.md` accurately contrast a uniform, bounded $O(\sqrt{\delta})$ perturbation across all calls with an independent Bernoulli process that yields zero perturbation with probability $1-\eps$, but an $O(1)$ catastrophic projective disturbance with probability $\eps$. The distinction is technically accurate and fairly characterized.

### 2.6 Noisy-Oracle Distinctions (Regev–Schiff, Rosmanis)
- **Prior Art Distinction:** Regev and Schiff (ICALP 2008) analyze oracles that randomly act as the identity; Rosmanis (2023) analyzes dephasing and depolarizing noise during oracle execution.
- **Noise Location:** The manuscript clearly identifies that here the oracle is noiseless ($O_w$), and noise occurs exclusively in the postquantum readout channel. This architectural difference is clearly stated in Section 1, Section 2, and `SOURCES.md`.

### 2.7 Bounded Novelty Language and Absence of Search Hits
- **Literature Perimeter:** In Section 1.1 (lines 147–151) and `SOURCES.md`, the author explicitly qualifies the literature search as a focused comparison and explicitly disclaims exhaustive priority certification:
  > *"Absence of a search hit is not exhaustive priority certification."*
- **Screened Literature:** `SOURCES.md` transparently documents that recent preprints (Cakan et al., Morimae et al., Lolck et al.) were screened at the abstract level only and disclaims any theorem-level novelty assertion against them.

### 2.8 Review, Verification, and Publication Status
- **Review Disclosures:** The draft across all documents (`manuscript/main.tex`, `README.md`, `CITATION.cff`, `.zenodo.json`, and `publication/README.md`) states version `0.1.0-dev`.
- **Integrity of Claims:** No DOI is invented or claimed. Zenodo integration is identified strictly as repository setup without claiming that a release has occurred or that independent human peer review or formal certification has taken place.

---

## 3. Detailed Audit Findings

| Finding ID | Severity | Location | Issue / Reasoning | Theorem or Publication Blocker? | Concrete Proposed Correction |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **FINDING-01** | **LOW** | `manuscript/main.tex`: lines 48–50; `README.md`: line 581 | **Wide-Register Readout Unit Cost vs. Bit-Length Accounting.** In the Abstract and README, total cost is summarized as $T = Q+P+R+M = \Theta(N^{1/3}+\sqrt{\eps N})$ by treating each sampler readout $P$ as a unit-cost call. While lines 103, 218, and 448 explicitly state that transcript storage is charged separately as $O(P \log N)$ bits, the Abstract could be misread as implying bit-level readout is free. | No (Does not block theorem or publication; purely expository). | In Abstract (line 48) and README, insert a brief parenthetical clarifying that $P$ measures unit calls to the wide register, with $O(P \log N)$ transcript bits accounted separately. |
| **FINDING-02** | **LOW** | `manuscript/main.tex`: lines 509–510; `.zenodo.json`: lines 646; `README.md`: line 609 | **Pre-Review Disclaimer Transition upon Completion.** The frozen pre-review text states: *"no separate external-model or human review is represented as completed."* As noted in packet item 13, this describes the pre-review state. When this independent review suite is completed and dispositioned, retaining verbatim wording that no review occurred would become historically inaccurate. | No (Appropriate for pre-review draft; must be updated prior to archival release). | Update the post-review revision note in the manuscript, `README.md`, and `.zenodo.json` to state: *"Draft updated following independent multi-lens AI review; no independent human peer review or formal machine-checked proof (e.g. Lean) has occurred."* |
| **FINDING-03** | **LOW** | `manuscript/main.tex`: Section 1.1, line 129; `SOURCES.md`: line 624 | **Abbas et al. Copy Structure Clarification.** `SOURCES.md` summarizes Abbas et al. as: *"Prior cube-root upper bound under gentle imperfect measurements on multiple copies."* In Abbas et al. (Appendix E.4, Proposition 28), gentle measurements can also be applied sequentially to a single copy under bounded perturbation $\delta \le O(N^{-2/3})$. | No (Does not affect theorem validity or priority boundary). | Refine `SOURCES.md` and line 129 to state: *"Their construction analyzes gentle measurements (sequential or multi-copy) with bounded conditional disturbance per readout..."* |

---

## 4. Final Verdict

**Verdict:** **GO-WITH-NOTES**

### Justification:
- **No Theorem Gaps:** The mathematical model, lower bound proof (Lemmas 2 and 3, query sensitivity, Bures metric hybrid), and matching upper bound construction are self-contained, mathematically rigorous, and internally consistent.
- **Accurate & Modest Attribution:** The manuscript meticulously credits ABFL for the algorithm template, Miloschewsky–Podder for the ideal cube-root lower bound and conditional-copy foundation, Abbas et al. for gentle-measurement robustness, and Regev–Schiff / Rosmanis for noisy oracle frameworks.
- **Strict Scope Boundaries:** The distinction between hypothetical postquantum samplers and ordinary physical quantum instruments is maintained without exception. Physical hardware realization and ordinary BPP/BQP implications are explicitly disclaimed.
- **Honest Publication/Review Status:** Versioning is uniformly pinned to `0.1.0-dev`, Zenodo status is accurately described as integration setup without a published release or DOI, and evidence hashes are preserved.
- The three noted items are low-severity expository refinements and workflow transitions that do not impede publication readiness.
