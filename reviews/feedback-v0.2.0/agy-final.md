# Independent Review Report: Non-Claims and Attribution Lens (v0.2.0)

**Source SHA-256**: `e0be2b107ef234bedd9c64961e393657b38164c1d55ef0bcd8e5ddb563487aa9`  
**Review Scope**: Final manuscript revision v0.2.0 (`packet.txt`)  
**Lens**: Non-claims, attribution, persistent adaptive CQP correspondence, stateless oracle adaptivity distinction, novelty limits, physical/BPP/BQP non-claims, and AI assistance disclosures.

---

## 1. Recommendation: GO

The v0.2.0 final source completely and rigorously delineates its theoretical scope, mathematical attributions, and non-claims. The correspondence with persistent adaptive CQP (ABFL) is accurately formulated under the explicit charged-call convention, with clear operational simulation mappings and explicit disclaimers regarding query-only free-sample models or exact elementary-gate overheads. Stateless oracle adaptivity (Morimae–Shirakawa–Yamakawa 2025) is cleanly distinguished from persistent-state continuation. The prior findings from Claude F1 (explicit operational capping on the reference oracle $O_0$) and Claude F2 (finite-support classical randomness) have been cleanly integrated. All attributions to primary literature (ABFL, Miloschewsky–Podder, Abbas et al., Regev–Schiff, Rosmanis, Fiorentino–Weigert, Gilchrist–Langford–Nielsen) are accurate, candid, and properly circumscribed. Physical feasibility, complexity-class collapse, and formal certification are unequivocally disclaimed.

---

## 2. Audit of Theorem Scope and Persistent Adaptive CQP Correspondence

### 2.1 Model Scope and Inclusion Mapping
- **Scope Definition (Lines 32–55, 165–256)**: The manuscript studies unstructured search on $N \ge 2$ items with a noiseless oracle $O_w$ and an idealized postquantum Born sampler that independently projects the sampled register with probability $\eps$. The controller operates on the continuing global state with immediate classical feedback from sampler outcomes and collapse flags.
- **Persistent CQP Mapping (Lines 127–133, 585–606, Corollary 4)**:
  - In the ABFL author-hosted CQP manuscript (theory.stanford.edu, Sections 3, 6, 8), computation proceeds in stages: each stage applies a unitary $U_i$ and an ordinary partial measurement $M_i$, followed by sampling the full-register Born distribution without modifying the quantum state. The classical controller then selects subsequent stages on the *same continuing quantum state*.
  - The manuscript's simulation map (lines 591–606) maps each stage directly: $U_i$ is implemented directly; $M_i$ is executed as an allowed ordinary projective measurement (charged in $M$); each Born sample is executed via a sampler call at $\eps = 0$ ($c=0$ identically, state intact), charged in $P$; and oracle queries inside $U_i$ are charged in $Q$.
  - This establishes an exact step-by-step simulation without state replication or rewinding.
- **Charged-Call vs. Query-Only Distinctions (Lines 597–606)**:
  - The text explicitly notes: *"Each returned sample is charged separately, not a free transcript for one circuit-oracle call. This preserves search-query and sample counts and adds at most one ordinary-measurement charge per sampled stage, without copies or replay... No bound on oracle queries alone with unlimited free samples is asserted."*
  - This is an essential and precise non-claim: it prevents any misinterpretation that the theorem lower-bounds a hypothetical model where an algorithm makes few queries and takes unbounded free non-collapsing samples of the resulting state.
  - The distinction between query complexity and charged-call complexity ($T = Q + P + R + M$) is rigorously preserved throughout the paper.

---

## 3. Distinction from Stateless Oracle Adaptivity

- **Primary Reference**: Morimae, Shirakawa, and Yamakawa (MSY 2025, arXiv:2510.04448v1).
- **Audit of Distinction (Lines 134–137, 746–748)**:
  - In MSY (footnote 6, Section 5), adaptive queries are made to a *stateless* circuit-sampling oracle: each query supplies a description of a circuit $C$ and receives a sample from $C\ket{0}$. Crucially, each such call is an independent invocation from a fresh state; the underlying physical state does not persist across queries.
  - In persistent adaptive CQP and the present model, the controller maintains and continues the *same uncollapsed entangled state* across successive operations and measurements.
  - The manuscript explicitly clarifies: *"Adaptive calls to a stateless circuit-sampling oracle in \cite[footnote 6, Section 5]{msy} start independent invocations; their sampling-hardness equivalence does not supply this persistent-state bound. This is search-model inclusion, not equality of entire complexity classes."*
  - This distinction is mathematically exact and prevents invalid transfers of sampling-hardness equivalences to persistent-state query lower bounds.

---

## 4. Attribution and Prior-Work Delineation

The manuscript's attribution structure is thorough, accurate, and carefully delineated:

1. **Aaronson, Bouland, Fitzsimons, and Lee (ABFL, arXiv:1412.6507v1 / ITCS 2016)** (Lines 58–61, 118, 654–658):
   - Correctly credited for introducing the non-collapsing measurement framework (PDQP) and the algorithmic template of partial Grover evolution followed by repeated readouts.
   - Pinned arXiv version is correctly distinguished from the author-hosted CQP manuscript (theory.stanford.edu, \cite{abflcqp}) which defines persistent adaptive continuation.
2. **Miloschewsky and Podder (MP, CCC 2025 / arXiv:2411.04085v3)** (Lines 61–63, 119–126, 672–679):
   - Correctly credited for the ideal $\Omega(N^{1/3})$ lower bound, the conditional-copy construction, and the root-fidelity potential technique.
   - Explicit non-claim of priority: *"We reconstruct the ideal inequality and extend its control scope; neither the deferred endpoint nor the use of conditional copies is a separate contribution."* (Lines 120–122).
   - Accurately notes that MP Section 1.5 formulated noisy non-collapsing computation and adaptive feedback as open problems.
3. **Abbas, King, Huang, Huggins, Movassagh, Gilboa, and McClean (NeurIPS 2023)** (Lines 138–146, 680–687):
   - Accurately credited for demonstrating that gentle imperfect measurements support cube-root search (Appendix E.4, Proposition 28).
   - Accurately distinguished: Abbas et al. rely on multiple copies ($O(\log N)$) and a global $1/N$-gentleness assumption on every measurement. In contrast, an accidental collapse is an independent rare event with order-one disturbance on the conditional state when it occurs. The manuscript claims no priority for the general idea of imperfect readout robustness, but specifically for the matched, all-$\eps$ bound under the explicit independent-collapse instrument.
4. **Regev and Schiff (ICALP 2008 / arXiv:1202.1027v1)** (Lines 74–76, 148–153, 688–693):
   - Accurately credited for bounds on faulty oracle calls (where the oracle acts as identity with error probability).
   - Distinguished by noise location: the search oracle here is noiseless; noise resides strictly in the auxiliary readout mechanism.
5. **Rosmanis (arXiv:2309.14944v1, 2023)** (Lines 74–76, 148–154, 220–234, 694–697):
   - Accurately credited for search under noisy oracles with recorded noise flags.
   - Accurately distinguished: discarding records in equation \eqref{eq:record} gives an ordinary dephasing channel, but retaining the nondisturbing Born record yields a non-CPTP nonlinear instrument. Equal discarded-record marginals do not justify transferring oracle-noise theorems.
6. **Fiorentino and Weigert (PLA 2025 / arXiv:2303.13411v2)** (Lines 154–158, 699–704):
   - Accurately credited for passive measurement theory; correctly noted that their composition rules and state-reconstruction do not provide the charged independent-collapse tradeoff.
7. **Gilchrist, Langford, and Nielsen (PRA 2005 / quant-ph/0408063v2)** (Lines 162–163, 279–284, 705–710):
   - Accurately credited as the source for standard root-fidelity, Bures metric, and triangle inequality tools.

---

## 5. Novelty Limitations and Disclaimers

- **Bounded Literature Search (Lines 159–161, 734–740)**:
  - The manuscript explicitly characterizes its literature review as a *focused, bounded comparison* rather than an assertion of exhaustive priority.
  - The search boundaries, screening dates (November 14 and 15, 2026), specific search terms, and abstract screenings (Cakan et al., Morimae et al., Lolck et al.) are documented with complete transparency.
  - Explicitly states: *"No author contact, unpublished-work check, independent expert review or exhaustive citation crawl occurred."*
- **What is New vs. What is Inherited (Lines 103–116, 732–733)**:
  - *Inherited*: Algorithmic template (ABFL), conditional copies and fidelity potential (MP), gentle measurement robustness concept (Abbas et al.), Bures metric and distance inequalities (GLN), AM–GM, Jensen.
  - *New Contribution*: The fixed-power potential comparison with copy exponent $k = \lceil 1/\eps \rceil$, which remains non-decreasing across arbitrarily many readouts; finite-tree induction and query-frontier alignment extending lower bounds to immediate adaptive feedback on persistent state; the exact matching upper-bound analysis charging every attempt; and the uniform interpolation $\Theta(N^{1/3} + \sqrt{\eps N})$ across all $0 \le \eps \le 1$.

---

## 6. Physical, Complexity-Class, and Algorithmic Non-Claims

The manuscript maintains strict, unambiguous boundaries:
1. **No Physical Implementation Claims (Lines 53–54, 70–72, 626–632)**:
   - *"This is a particular noisy extension of a hypothetical information resource. It does not assert a physical implementation of non-collapsing measurement."*
   - *"The result concerns this specified postquantum access model, not physical noisy quantum hardware or ordinary BPP versus BQP."*
2. **No Complexity-Class Collapses (Lines 53–54, 626–632)**:
   - The theorem is strictly an oracle-model query/readout complexity result. It explicitly states that the ordinary BPP vs. BQP question is left completely open.
3. **No Unrealistic Postquantum Primitives (Lines 196–198, 205–206)**:
   - Explicitly disclaims unknown-state description, physical cloning, state rewinding, chosen-outcome projection, free postselection, or ensemble-independent nonlinear maps on reduced density matrices.
4. **No Unbounded Stopping Times or Free Restarts (Lines 246–249)**:
   - All actual attempts are charged, including failed trials and restarts.
   - The upper bound pre-schedules all $B = 13120$ attempts; no expected-cost or unbounded stopping-time theorem is asserted.
5. **No Practical Asymptotic Overstatement (Lines 534–535)**:
   - *"The constants above certify an asymptotic law and are not a practical performance estimate."*

---

## 7. AI and Evidence Disclosures

- **Assistance Disclosure (Lines 633–644)**:
  - Discloses that the manuscript has an informal analytic proof and internal checks, and explicitly states that it does not constitute formal certification or independent peer review.
  - Discloses that historical finite exact numerical runs illustrate algebraic comparisons and do not establish universal claims by finite agreement.
  - Fully discloses that OpenAI Codex assisted with derivation, literature comparison, drafting, and internal checking.
  - Fully discloses that separate AI reviews were conducted through provider CLIs, with actual model identities, review scopes, findings, and dispositions recorded in the archive.
  - Explicitly states: *"These reviews are not independent human peer review or formal certification."*
- **Availability and Licensing (Lines 646–650)**:
  - Repository URL, CC BY 4.0 license, and citation metadata are explicitly provided.

---

## 8. Evaluation of Final-Source Modifications

1. **Claude F1 Resolution (Explicitly Capped Reference World $O_0$, Lines 242–245)**:
   - *Previous Gap*: Concern that an algorithm promised to respect caps only on valid marked inputs $w \in [N]$ might run indefinitely on $O_0 = I$.
   - *Resolution*: Lines 242–245 state: *"The finite controller and caps apply on every execution, including the reference oracle $O_0$. Enforce them by halting before a cap would be exceeded; if initially promised only on marked inputs, this truncation leaves every valid-input execution unchanged."*
   - *Assessment*: This operational truncation guarantees that the execution tree on $O_0$ is finite, prefix-free, and contained within the exact same caps, without modifying any execution on valid inputs. The gap is completely closed.
2. **Claude F2 Resolution (Finite-Support Randomness, Line 194)**:
   - *Previous Gap*: Continuous or infinite-support classical randomness could create measure-theoretic complications for discrete direct sums and finite-tree induction.
   - *Resolution*: Line 194 explicitly requires: *"Fresh classical random choices have finite support and are input-independent given the history."*
   - *Assessment*: This ensures that every node in the execution tree has discrete probability weight and every prefix-free cut is finite. The gap is completely closed.
3. **Corollary 4 Scope and Syntax Inclusion (Lines 591–606)**:
   - *Previous Gap*: Ambiguity regarding whether persistent CQP allows free samples or whether elementary gate runtime matches query counts.
   - *Resolution*: The proof of Corollary 4 maps $U_i, M_i$ directly, charges each sample call individually, explicitly states the logarithmic and parameter-processing runtime overheads, and expressly disclaims oracle-query bounds with unlimited free samples.
   - *Assessment*: Completely resolved.
4. **Layout and SOURCES Formatting (Lines 651–653, 715–750)**:
   - Bibliography font is reduced (`\small`, `\raggedright`) to preserve clean layout; punctuation in primary comparisons and provenance files is clean and accurate.
5. **No Optional Exponent-Threshold Tightness Theorem Added**:
   - Confirmed: the paper appropriately maintains focus on the core interpolation $\Theta(N^{1/3} + \sqrt{\eps N})$ and $\max\{1/3, (1-\alpha)/2\}$ without introducing unvetted secondary claims.

---

## 9. Attempted Counterexamples and Adversarial Stress Tests

### Attempt 1: Exploiting "Free" Samples in Persistent CQP
- *Construct*: Suppose an algorithm executes $Q = O(1)$ queries to create a state with $O(1/\sqrt{N})$ overlap on the marked item, and then takes $P = \Theta(N)$ non-collapsing samples of that state at $\eps = 0$. If samples are free, the total query cost is $O(1)$, which is $o(N^{1/3})$.
- *Defense in Text*: The manuscript explicitly charges every sample call in $T = Q + P + R + M$ (equation \eqref{eq:cost}) and specifically disclaims query-only free-sample bounds in Corollary 4 (lines 604–605): *"No bound on oracle queries alone with unlimited free samples is asserted."*
- *Result*: Counterexample defeated; model scope is explicitly charged-call.

### Attempt 2: Transferring MSY (2025) Hardness to Circumvent the Lower Bound
- *Construct*: Argue that because MSY showed quantum cryptography and sampling hardness equivalence under adaptive non-collapsing measurements, persistent-state search lower bounds follow immediately from their equivalence.
- *Defense in Text*: In MSY (footnote 6 / Section 5), queries are made to a *stateless* circuit-sampling oracle where each query restarts from a fresh state $\ket{0}$. Persistent CQP allows unitaries and measurements on the *same continuing quantum state*. The manuscript explicitly notes this distinction in lines 134–137, refuting any conflation.
- *Result*: Counterexample defeated; distinction is sound.

### Attempt 3: Violating Finite Cuts via Pathological Stopping Rules on $O_0$
- *Construct*: Design a controller that only halts when it observes a marked item. On $O_0$, no marked item exists, so the algorithm loops indefinitely, preventing the definition of a finite prefix-free cut.
- *Defense in Text*: Lines 242–245 mandate that the algorithm is operationally truncated by halting whenever $Q, P, R,$ or $M$ would exceed its worst-case cap. Because the caps are finite, the tree on $O_0$ is strictly finite and prefix-free.
- *Result*: Counterexample defeated; operational truncation guarantees well-defined cuts.

### Attempt 4: Contradicting Abbas et al. (NeurIPS 2023) Robustness
- *Construct*: Argue that because Abbas et al. proved that $O(1/N)$-gentle measurements preserve $O(N^{1/3})$ search, an accidental collapse probability $\eps = 1/\sqrt{N}$ should also yield $O(N^{1/3})$ search, contradicting $T = \Theta(N^{1/3} + \sqrt{\eps N}) = \Theta(N^{1/3} + N^{1/4}) = \Theta(N^{1/3})$ or fixed $\eps > 0$ yielding $\Theta(\sqrt{N})$.
- *Defense in Text*: Abbas et al. require gentleness on *every* measurement outcome ($\| \mathcal{E}(\rho) - \rho \|_1 \le 1/N$). In the accidental collapse model, with probability $\eps$, the state undergoes a full projective collapse onto a basis state $\ket{y}$, producing a trace-distance disturbance of order 1. For any fixed $\eps > 0$, the channel has $\Theta(1)$ disturbance, completely violating gentleness.
- *Result*: Counterexample defeated; physical mechanisms and mathematical regimes are distinct.

### Attempt 5: Asserting Physical Realizability or BPP/BQP Collapse
- *Construct*: Interpret Theorem 1 as demonstrating a physical algorithm that speeds up search on NISQ or faulty quantum computers.
- *Defense in Text*: Lines 53–54, 70–72, and 626–632 unequivocally state that the primitive is a hypothetical postquantum information resource, not physical noisy quantum hardware, and that ordinary BPP vs. BQP remains completely unaffected.
- *Result*: Counterexample defeated; non-claims are pervasive and explicit.

---

## 10. Substantive Findings Summary

| ID | Location | Severity | Description | Disposition |
|---|---|---|---|---|
| **F-01** | Lines 242–245 | Resolved / Minor | Prior Claude F1: Cap enforcement on reference oracle $O_0$. | Fully resolved by operational truncation rule; execution tree on $O_0$ is strictly finite. |
| **F-02** | Line 194 | Resolved / Minor | Prior Claude F2: Classical randomness measure support. | Fully resolved by explicit requirement of finite support. |
| **F-03** | Lines 591–606 | Resolved / Minor | Syntax mapping and query-only disclaimers for persistent CQP. | Fully resolved: $U_i, M_i$ mapped directly, individual sample charges explicit, free-sample models disclaimed. |
| **F-04** | Lines 134–137 | Verified / Note | Distinction between stateless oracle adaptivity (MSY) and persistent CQP. | Accurate, rigorously stated, and prevents invalid literature transfers. |
| **F-05** | Lines 633–644 | Verified / Note | AI and evidence disclosures. | Candid, transparent, and accurately distinguishes informal proofs/AI review from formal peer review. |

---

## 11. Final Assessment

The manuscript revision v0.2.0 meets all criteria under the non-claims and attribution lens:
- **Theorem Scope & Persistent CQP**: Mapped with precision under explicit charged-call accounting; query-only free-sample models are explicitly disclaimed.
- **Stateless Oracle Adaptivity**: Cleanly and accurately distinguished from persistent-state continuation.
- **Attributions**: Rigorous, transparent, and accurate across all primary literature (ABFL, MP, Abbas et al., Regev–Schiff, Rosmanis, Fiorentino–Weigert, GLN).
- **Novelty Limits**: Fully delineated with documented search bounds and screening limits.
- **Non-Claims**: Pervasive and robust against physical overinterpretation, complexity-class collapse, or unrealistic postquantum operations.
- **AI Disclosures**: Transparent and compliant with scholarly integrity standards.

**Final Determination**: **GO**
