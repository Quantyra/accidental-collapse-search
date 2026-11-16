### Source Identification
- **Review Target**: P011 v0.4.0 Review Packet
- **Source SHA-256**: `af58f74bbc841d7d3e5769f4545919652a2c24272a160e369814c846ced8f6de`
- **Review Lens**: Attribution / Non-Claims / Provenance
- **Recommendation**: **GO-WITH-NOTES**

---

### Executive Summary

An independent attribution and non-claims audit of the complete v0.4.0 manuscript source (`main.tex`), provenance record (`SOURCES.md`), public `README.md`, and archival metadata was conducted against the supplied review packet.

The core addition in version 0.4.0—Section 6 ("Implementation error for complete adaptive histories") and Theorem 4 (`thm:precision`)—is presented scrupulously as an **auxiliary consequence** of P011's existing complete-history power-comparison machinery rather than a novel foundational lower-bound or independent complexity framework. Prior work by Aaronson, Bouland, Fitzsimons, and Lee (ABFL), Çakan et al., and Dawson and Nielsen is accurately cited, precisely bounded, and not subordinated or obscured. 

The non-claims boundaries—distinguishing the hypothetical postquantum instrument from physical noise/fault tolerance, clarifying that mathematical conditional copies are proof devices rather than quantum resources, and separating informal analytic proofs from human peer review or formal Lean certification—are maintained consistently across the manuscript, documentation, and archival metadata.

---

### 1. Attribution & Prior-Art Analysis

#### 1.1 Auxiliary Status of Section 6
- **Manuscript Position**: The manuscript uniformly characterizes Section 6 as a supporting derivation:
  - *Abstract* (lines 56–60): Introduces the gate-error bound as an *"auxiliary consequence"*.
  - *Introduction* (lines 156–161): Explicitly clarifies that Section 6 *"converts the retained local power comparisons into a bound on complete adaptive transcript distributions... This is an auxiliary consequence of the existing machinery, not a new lower-bound framework."*
  - *Section 6 Introduction* (lines 843–846): Notes that the power comparisons *"also give an auxiliary precision theorem. This section compares two implementations of the same controller, with the same exact input oracle, rather than two different oracle inputs."*
  - *SOURCES.md* (lines 1248–1249) & *Archive Metadata* (line 1350): Restate that this is an attributed consequence of existing machinery, closing the paper's explicit general implementation-transfer caveat without claiming a new adversary or continuity framework.
- **Assessment**: The characterization is mathematically and methodologically accurate. Theorem 4 inserts an isometric perturbation into the existing Bures distance direct-sum potential $d_\kappa$, utilizing the normalized active history mass $\sum_{h\text{ active}} p_h \le 1$ to bound aggregate error without altering the underlying potential functions.

#### 1.2 ABFL Gate-Set Independence
- **Context & Citation**: ABFL (2014/2016, arXiv:1412.6507v1, Appendix D; author-hosted CQP manuscript, Appendix D) established gate-set independence for ideal, non-adaptive PDQP circuits by showing that gate approximation to error $2^{-O(n)}$ requires only polynomial precision bits.
- **Manuscript Treatment**:
  - Section 1.1 (lines 215–218) explicitly acknowledges: *"ABFL already proves gate-set independence for ideal PDQP \cite[Appendix D]{abfl}. Its dimension-dependent estimate requires exponentially small numerical error but only polynomially many accuracy bits; efficient gate-set independence is not new here."*
- **Assessment**: Overstatement is avoided. The manuscript cleanly isolates ABFL's priority on the principle of gate-set independence in non-collapsing computation, while noting that Theorem 4's contribution is a dimension-independent operator-norm transfer bound ($\sqrt{K_\eps(P)} \sum \delta_j$) for persistent adaptive feedback with accidental collapse.

#### 1.3 Çakan et al. Conditional-Copy Continuity
- **Context & Citation**: Çakan, Khurana, Morimae, Shirakawa, Tomer, and Yamakawa (arXiv:2510.05055v1, Oct 2025, Section 8.2, Claim 8.3) proved that the trace distance between conditional-copy states satisfies $\operatorname{TD}(\tilde{A}, \tilde{B}) \le 3 \operatorname{TD}(A, B)$ in a two-time, fixed-circuit setting.
- **Manuscript Treatment**:
  - Section 1.1 (lines 219–225) explicitly attributes: *"\c{C}akan et al. already prove a dimension-independent conditional-copy trace-distance comparison with factor three \cite[Section 8.2, Claim 8.3]{cakan}. Their inspected statement treats two-time states in a fixed ideal circuit and does not itself state our collapse-sensitive square-root budget for persistent feedback. Theorem~\ref{thm:precision} is presented as a quantitative auxiliary consequence, with no first-continuity or exhaustive novelty claim."*
  - *SOURCES.md* (lines 1246–1247) records that the intermediate-state comparisons of Claim 8.3 were directly inspected.
- **Assessment**: The acknowledgment is accurate, specific to the exact claim index, and explicitly disclaims first-continuity priority.

#### 1.4 Dawson–Nielsen Gate Synthesis
- **Context & Citation**: Dawson and Nielsen (quant-ph/0505030v2, QIC 2006) provide the standard Solovay–Kitaev algorithm for approximating unitaries in fixed dimensions using a finite universal gate set.
- **Manuscript Treatment**:
  - Section 1.1 (line 226) and Section 6.4 (line 1058) cite \cite{dn} for standard fixed-dimensional synthesis.
  - Section 6.4 (lines 1049–1087) provides an explicit, conservative accounting ledger incorporating description evaluation $E(n, b_g + c_d)$, compiler time $S(b_g)$, word length $L(b_g)$, classical workspace $M_E, M_S$, and ancillas $a(b_g)$.
  - Explicit limitation (lines 1084–1086): *"Arbitrary growing-width matrices, uncomputable real descriptions and general ambient noise do not acquire an efficient implementation from this theorem."*
- **Assessment**: Dawson–Nielsen is credited as standard inherited machinery. Synthesis is properly restricted to fixed local dimension $d$, relative phase preservation in $\operatorname{SU}(d)$ is explicitly accounted for, and no unwarranted claims of scalable multi-qubit compilation are made.

---

### 2. Non-Claims & Boundary Demarcation

The manuscript maintains rigorous boundaries against unwarranted extrapolations:

1. **Hypothetical Sampler vs. Physical Hardware Noise**:
   - The paper repeatedly emphasizes that the independent-collapse sampler is a postquantum mathematical access model, not a physical error model for faulty hardware:
     - Lines 77–79: *"This is a particular noisy extension of a hypothetical information resource. It does not assert a physical implementation of non-collapsing measurement."*
     - Lines 309–311: Clarifies that retaining the Born record ($c=0$) is non-linear and not equivalent to ordinary dephasing or a noisy oracle channel.
     - Lines 1131–1136: Confirms that the results do not classify all noisy PDQP/CQP computations, establish physical realizability, or resolve general ambient noise.
2. **Postquantum Bounds vs. BPP / BQP**:
   - Lines 60–62, 1135–1136, and 1258 explicitly state that all bounds are relative to the specified oracle access model, leaving the ordinary BPP versus BQP relationship unaffected.
3. **Proof Device vs. Algorithmic Resource**:
   - Lines 116–117, 363–365, 432–435, and 1081–1082 explicitly state that mathematical powers $(\ket{\psi}\bra{\psi})^{\otimes k}$ and purified reference environments are purely analytical bounding devices, not physical registers or algorithmic memory.
4. **Informal Analytic Derivations vs. Certification**:
   - Lines 1139–1149 (*Evidence and assistance disclosure*), *README.md* (lines 1316–1317, 1344), and metadata explicitly declare:
     - The preprint is an informal analytic derivation.
     - Preserved numerical runs are illustrative checks on finite cases, not general inductive proofs.
     - OpenAI Codex and CLI AI reviews are disclosed, with an explicit statement that AI reviews do not constitute independent human peer review or formal certification.
     - No Zenodo DOI is claimed for v0.4.0 prior to publication readiness.

---

### 3. Attempted Falsifiers & Stress Tests

| Target Claim / Scenario | Falsification Test Description | Outcome | Result |
| :--- | :--- | :--- | :--- |
| **Falsifier 1**: Rare-branch error blowup in Theorem 4 | Attempted to construct a policy where a gate error occurs on an exponentially rare history branch ($p_h \ll 1$), testing whether $\operatorname{TV}$ explodes by $O(\delta / p_h)$ or $O(\delta / \sqrt{p_h})$. | Checked Eq. (912)–(916). The perturbation is weighted by the unconditional active branch probability $p_h$: $d_\kappa^2 \le K \delta_j^2 \sum_{h\text{ active}} p_h \le K \delta_j^2$. Verified against the diagnostic family in Eq. (991)–(995) where $a \to 0$: $\operatorname{TV} \le \sqrt{K} d$, confirming no inverse probability factor. | **Passed (Falsification failed)** |
| **Falsifier 2**: Rate-coupling $\tau$ under adaptive thresholding | Tested whether the rate-coupling bound $\operatorname{TV} \le P\tau$ holds if the classical controller branches on threshold comparisons of $\eps$. | Checked Section 6.3 (lines 1003–1018). The manuscript explicitly restricts the coupling to a *frozen policy* and explicitly warns in lines 1017–1018: *"Rounding a rate and then changing a branch threshold, schedule or cap is not covered by $P\tau$ alone. Such a policy change needs its own argument."* | **Passed (Falsification failed)** |
| **Falsifier 3**: Subsumption by Çakan et al. Claim 8.3 | Tested whether Çakan et al. (arXiv:2510.05055v1) already implies Theorem 4. | Çakan et al. Claim 8.3 establishes $\operatorname{TD}(\tilde{A}, \tilde{B}) \le 3 \operatorname{TD}(A, B)$ for fixed ideal circuits at $\eps=0$. It does not provide the collapse-sensitive exponent $K_\eps(P)$, adaptive persistent-state query frontiers, or gate-compilation transfers. Manuscript attribution is strictly accurate. | **Passed (Falsification failed)** |
| **Falsifier 4**: Subsumption by ABFL Appendix D | Tested whether ABFL (arXiv:1412.6507v1) already yields Theorem 4's precision bound. | ABFL's simulation is dimension-dependent (requiring $2^{-O(n)}$ gate precision) and non-adaptive. Theorem 4's bound is dimension-independent with constant 1. The manuscript explicitly notes this distinction while acknowledging ABFL's priority for ideal gate-set independence. | **Passed (Falsification failed)** |
| **Falsifier 5**: Solovay–Kitaev dimension scaling | Tested whether Theorem 4 overclaims gate compilation for arbitrary multi-qubit unitaries. | Checked Section 6.4 (line 1052, 1084–1086). Compilation is explicitly restricted to fixed local dimension $d$, and arbitrary growing-width matrices are explicitly excluded from efficient implementation claims. | **Passed (Falsification failed)** |
| **Falsifier 6**: Cross-document consistency | Audited consistency of Theorem 4 and rate error claims across LaTeX source, `SOURCES.md`, `README.md`, and metadata. | The formula $\operatorname{TV} \le \min\{1, \sqrt{K_\eps(P)}\sum \delta_j + P\tau\}$ with $K_\eps(P) = \min\{P+1, \lceil 1/\eps \rceil\}$ matches identically across lines 876/1014, 1244, 1297, and 1350. | **Passed (Falsification failed)** |

---

### 4. Findings & Specific Observations

#### Finding 1 (Nonblocking Exposition / Minor Typo): Subscript Whitespace Artifact
- **Severity**: Minor / Nonblocking Exposition
- **Source Location**: `manuscript/main.tex`, lines 912–915 (Equation 912):
  ```latex
  d_\kappa(A^U,A^V)^2
  &=2\sum_{h\ {
  m active}}p_h(1-s_h^{\kappa(h)})\\
  &\le K\delta_j^2\sum_{h\ {
  m active}}p_h
  \le K\delta_j^2.
  ```
- **Description**: A linebreak split `h\ {\rm active}` into `h\ {` followed by `\rm active}` across lines 912–913 and 914–915. While standard TeX engines handle this without a fatal parse error, it represents a minor formatting artifact in the LaTeX source.
- **Disposition**: Nonblocking cosmetic fix for future source polishing.

#### Finding 2 (Nonblocking Exposition): Combined Rate Formula Presentation
- **Severity**: Informational / Nonblocking Exposition
- **Source Location**: `manuscript/main.tex`, Section 6.1 (line 876) vs. Section 6.3 (line 1014), compared with `README.md` (line 1297).
- **Description**: Theorem 4 in Section 6.1 is formally stated for gate errors at identical collapse rate $\eps$: $\operatorname{TV}(\mathcal{T}_A, \mathcal{T}_B) \le \min\{1, \sqrt{K_\eps(P)}\sum \delta_j\}$. The rate error coupling $+ P\tau$ is derived subsequently in Section 6.3 (Equation 1014). The summary documents (`README.md`, `SOURCES.md`, and archival metadata) present the combined formula $\min\{1, \sqrt{K}\sum \delta_j + P\tau\}$ directly.
- **Disposition**: Nonblocking. The documentation accurately reflects the total combined bound established across Sections 6.1 and 6.3, and Section 6.3 explicitly documents the separate nature of the rate coupling.

---

### Final Recommendation

**GO-WITH-NOTES**

The v0.4.0 delta is fully sound under the attribution, non-claims, and provenance lens:
1. Section 6 is properly presented as an auxiliary consequence of the core P011 power-comparison machinery.
2. ABFL, Çakan et al., and Dawson–Nielsen are rigorously credited with appropriate boundaries.
3. Non-claims regarding physical noise, BPP/BQP, formal verification, and human peer review are transparent and consistent across all manuscript texts, documentation, and archival metadata.
4. Source hash `af58f74bbc841d7d3e5769f4545919652a2c24272a160e369814c846ced8f6de` is verified.
