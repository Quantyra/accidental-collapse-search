### Review Packet Audit: Non-Claims and Attribution Lens

**Source SHA-256:** `b7cecc45d2958fa77e2add9670cb632e8aa3018dc0a6afe5ce05a967b8b07714`  
**Inspected Version:** Manuscript v0.2.0 (November 15, 2026 revision)  
**Evaluation Lens:** Non-Claims, Attribution, Model Scope, and Disclosures  

---

### 1. Executive Summary & Recommendation

**Recommendation: GO** (with minor documentation notes)

The manuscript revision v0.2.0 rigorously adheres to scholarly attribution standards and maintains disciplined boundary demarcations. It carefully distinguishes its search query complexity results from broad complexity-class statements, properly segregates persistent-state adaptive feedback from stateless circuit-sampling oracle models, explicitly credits earlier templates and lower-bound techniques to their respective authors (ABFL, Miloschewsky–Podder, Abbas et al., Regev–Schiff, Rosmanis, Fiorentino–Weigert, and Gilchrist–Langford–Nielsen), and preserves absolute non-claims regarding physical feasibility, hardware noise, and ordinary BPP vs. BQP consequences. AI tool assistance (OpenAI Codex, CLI multi-model review) and the non-peer-reviewed/informal nature of the proof are prominently disclosed in the text and metadata.

---

### 2. Detailed Audit by Evaluation Area

#### A. Theorem Scope & Persistent Adaptive CQP Correspondence
* **Exact Locations:** LaTeX Lines 80–100 (Theorem 1), Lines 126–136 (Section 1.1), Lines 579–593 (Corollary 3); Primary Comparison Lines 727–734; Metadata Line 737.
* **Findings:**
  1. *Model Scope:* Theorem 1 defines the worst-case query, readout, preparation, and reset call caps ($Q, P, R, M$) for unique unstructured search on $N \ge 2$ items under an independent accidental-collapse Born sampler with immediate classical feedback. Total cost $T = Q + P + R + M$ accounts for every pre-scheduled or adaptive branch attempt.
  2. *CQP Correspondence:* The connection to Aaronson et al. (ABFL author-hosted manuscript \cite{abflcqp}) is strictly characterized as *search-model inclusion* rather than complexity class equality:
     > *"This is search-model inclusion, not equality of entire complexity classes."* (LaTeX Lines 132–133)
  3. *Immediate-Feedback Resolution:* Corollary 3 explicitly restricts the resolution of the persistent feedback question to the declared finite-capped unstructured search setting under charged-call conventions, avoiding unwarranted extrapolation to decision languages or generic postquantum circuits.

#### B. Distinction from Stateless Oracle Adaptivity
* **Exact Locations:** LaTeX Lines 133–136; Primary Comparison Lines 731–732.
* **Findings:**
  - The manuscript explicitly contrasts its persistent continuing quantum register with the *stateless* adaptive circuit-sampling oracle analyzed by Morimae, Shirakawa, and Yamakawa (MSY \cite{msy}):
    > *"Adaptive calls to a stateless circuit-sampling oracle in [footnote 6, Section 5]{msy} start independent invocations; their sampling-hardness equivalence does not supply this persistent-state bound."* (LaTeX Lines 133–136)
  - This is a vital technical distinction: in MSY, adaptive oracle queries invoke separate independent sampling instances (each initializing or consuming state independently), whereas persistent CQP retains an entangled quantum register after non-collapsing or collapsing readout. The manuscript avoids conflating these distinct models.

#### C. Prior Work Attribution and Novelty Boundaries
* **Exact Locations:** LaTeX Lines 56–79, 102–125, 137–163; Primary Comparison Lines 705–725.
* **Findings:**
  - **ABFL (\cite{abfl}, \cite{abflcqp}):** Fully credited for the initial PDQP framework, the partial-Grover plus repeated-sampling search algorithm template, and the persistent CQP formulation.
  - **Miloschewsky & Podder (\cite{mp}):** Fully credited for the ideal cube-root lower bound ($\Theta(N^{1/3})$ at $\eps=0$), the root-fidelity potential, and the use of conditional copies. The text clearly explains why MP's decreasing exponent $\kappa(h) = P + 1 - p(h)$ cannot handle an unbounded number of noisy readouts, thereby isolating the exact novelty of the author's fixed-exponent comparison $k = \lceil 1/\eps \rceil$.
  - **Abbas et al. (\cite{abbas}):** Properly acknowledged for establishing that gentle imperfect measurements support cube-root search via multiple copies ($O(\log N)$ copies, $1/N$-gentleness). The manuscript clearly delineates small continuous disturbance across multiple copies from rare, discrete order-one projection on a single persistent register.
  - **Regev–Schiff (\cite{rs}) & Rosmanis (\cite{rosmanis}):** Accurately cited for noisy-oracle lower bounds, while explaining that oracle calls in this manuscript remain strictly noiseless, shifting noise solely to the postquantum readout instrument.
  - **Fiorentino–Weigert (\cite{fw}) & Gilchrist–Langford–Nielsen (\cite{gln}):** Accurately cited for passive measurement comparisons and foundational root-fidelity/Bures metric properties.
  - **Inherited Proof Machinery:** Jensen's inequality, weighted AM–GM, Cauchy–Schwarz, and the Bures triangle inequality are explicitly disclaimed as inherited standard tools.

#### D. Physical Feasibility, BPP, and BQP Non-Claims
* **Exact Locations:** LaTeX Lines 52–53, 70–71, 194–196, 612–618; Metadata Line 737.
* **Findings:**
  - The manuscript consistently disclaims physical implementation:
    > *"This is a particular noisy extension of a hypothetical information resource. It does not assert a physical implementation of non-collapsing measurement."* (LaTeX Lines 70–71)
    > *"There is no unknown-state description, physical cloning, rewinding, chosen-outcome projection or free postselection."* (LaTeX Lines 194–196)
  - Complexity-theoretic non-claims are unambiguous:
    > *"The result concerns this specified postquantum access model, not physical noisy quantum hardware or ordinary BPP versus BQP."* (Abstract Lines 52–53)
    > *"The interpolation is an oracle-model result, with the ordinary BPP/BQP question left open."* (LaTeX Lines 617–618)

#### E. Evidence, Diagnostic Runs, and AI Assistance Disclosures
* **Exact Locations:** LaTeX Lines 619–631; Primary Comparison Lines 703, 729, 733; Metadata Line 737.
* **Findings:**
  - *Proof Status:* Explicitly states the proof is an informal analytic theorem, without claiming formal kernel verification or independent human peer review.
  - *Diagnostic Receipts:* Clarifies that preserved diagnostic runs are illustrative finite checks that do not constitute universal empirical proofs.
  - *AI Disclosure:* Fully and transparently discloses assistance by OpenAI Codex (derivation, literature check, drafting) and independent provider CLI reviews, noting that model identities, scopes, findings, and dispositions are logged in the repository.

---

### 3. Substantive Findings & Notes

| ID | Location | Severity | Category | Description & Disposition |
|---|---|---|---|---|
| **N-01** | LaTeX L646–650 (`\bibitem{abflcqp}`) | Low / Note | Bibliographic Precision | The citation points to the undated author-hosted 28-page PDF (`cqp.pdf`). The primary comparison file anchors this with SHA-256 `b3692abc5d78d23e88871dea8ed17b4648b84a8f423fd3354aa3f694b1d488de`. This provides complete reproducibility without redistributing third-party text. |
| **N-02** | LaTeX L504–507 | Low / Note | Scope Consistency | For $N' < 256$, the algorithm falls back to exhaustive query without sampler invocation. The lower bound treats $2 \le N < 12$ by zero-query success bounds and excludes $N=1$. Scope boundaries are consistently closed across all regimes. |
| **N-03** | LaTeX L539–558 | Low / Note | Non-Claims Boundary | The approximate-preparation section explicitly clarifies that its trace-distance coupling is a specific construction property for this no-intervening-operation schedule, not a general trace-distance contraction theorem for nonlinear samplers. Excellent preservation of negative boundaries. |

---

### 4. Attempted Counterexamples & Stress Tests

1. **Attempted Overclaim of CQP Complexity Equality:**
   - *Test:* Does Corollary 3 or Section 1.1 imply that $\text{CQP} \neq \text{BQP}$ or characterize the full language class CQP?
   - *Result:* Passed. The text explicitly limits the result to query complexity of unique search within the declared finite-capped access model, explicitly disclaiming full complexity-class equality (Lines 132–133).
2. **Attempted Conflation with Stateless Adaptive Oracles (MSY):**
   - *Test:* Can the lower bound be circumvented by viewing the sampler as a stateless circuit oracle query in the sense of MSY?
   - *Result:* Passed. A stateless oracle re-prepares states from scratch upon each query, destroying entanglement with workspace. Persistent CQP preserves the post-readout state across subsequent operations. The manuscript correctly maintains this distinction.
3. **Attempted Prior Art Infringement against Abbas et al. (2023):**
   - *Test:* Does the upper bound claim novelty over gentle measurement search?
   - *Result:* Passed. Abbas et al. relies on $1/N$-gentle measurements across $O(\log N)$ parallel copies. The present work addresses an independent discrete-projection channel on a single persistent register with an all-$\eps$ matching bound $\Theta(N^{1/3} + \sqrt{\eps N})$. The attribution to Abbas et al. is prominent and explicit.
4. **Attempted Equivalence to Noisy-Oracle Bounds (Rosmanis):**
   - *Test:* Can the lower bound be trivially deduced from dephased or faulty oracle models?
   - *Result:* Passed. Rosmanis and Regev–Schiff apply noise to the oracle itself. Here the oracle is noiseless, and the sampler provides nondisturbing Born records on $c=0$. The text proves why discarded-record marginal equivalence does not imply operation equivalence for retained classical records (Lines 228–232).

---

### 5. Conclusion

The manuscript exhibits rigorous scholarship regarding prior work attribution, precisely defines the novelty and technical limits of its contributions, and strictly maintains all physical and complexity-theoretic non-claims. No blocking defects were found under the non-claims and attribution lens.
