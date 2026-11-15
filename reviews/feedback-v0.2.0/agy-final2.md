# Independent Review Report: Non-Claims and Attribution Lens (v0.2.0 Final2)

**Source SHA-256**: `47384ca46a9b823927da5784ea9d67a1cb14b18d10cfd8a958efb21e56e6e1d3`  
**Review Scope**: Final manuscript revision v0.2.0 (`packet.txt`)  
**Lens**: Non-claims, attribution, persistent adaptive CQP correspondence, distinction from stateless oracle adaptivity, novelty limitations, physical/BPP/BQP non-claims, and AI assistance disclosures.

---

## 1. Executive Summary and Final Recommendation

### Recommendation: **GO**

The manuscript source (`47384ca46a9b823927da5784ea9d67a1cb14b18d10cfd8a958efb21e56e6e1d3`) thoroughly satisfies all requirements of the non-claims and attribution lens. 

The single delta from the previous revision (`e0be2b107ef234bedd9c64961e393657b38164c1d55ef0bcd8e5ddb563487aa9`)—defining $Q, P, R, M$ as the *smallest* worst-case caps over valid marked inputs and complete branches (explicitly the corresponding branch maxima)—rigorously resolves the factor-four sandwich issue identified in Claude Final Finding 1 without compromising any proof step, operational truncation argument, or resource accounting.

The theoretical boundaries of the result are delineated with exemplary rigor:
- **Correspondence with persistent adaptive CQP** (ABFL) is precisely mapped under the declared charged-call convention, with clear operational simulation mappings ($U_i, M_i$, and individual sampler calls) and explicit disclaimers against query-only models with unlimited free samples or exact elementary-gate runtime parity.
- **Distinction from stateless oracle adaptivity** (Morimae–Shirakawa–Yamakawa 2025) is cleanly maintained: persistent state continuation is properly distinguished from independent re-invocations from fresh states.
- **Attribution to prior literature** (ABFL, Miloschewsky–Podder, Abbas et al., Regev–Schiff, Rosmanis, Fiorentino–Weigert, Gilchrist–Langford–Nielsen) is comprehensive, generous, and meticulously candid regarding what is inherited versus what is new.
- **Non-claims** concerning physical realizability, NISQ hardware relevance, complexity class collapses ($\text{BPP}$ vs $\text{BQP}$), unphysical operations (cloning, rewinding, postselection), and unbounded stopping times are explicit, unambiguous, and pervasive.
- **AI and evidence disclosures** adhere to scholarly transparency standards, candidly acknowledging assistance from OpenAI Codex and provider CLI AI reviews while explicitly disclaiming human peer review or formal certification.

---

## 2. Audit of the Final2 Delta Clarification

### 2.1 The Specific Text Modification (Lines 236–239)
```latex
Let $Q,P,R,M$ be the smallest worst-case caps over valid marked inputs
and complete branches on oracle calls, sampler calls, fresh attempt
preparations and ordinary projective measurement/reset calls, respectively.
Thus these caps are the corresponding branch maxima. We charge
\begin{equation}\label{eq:cost}
 T=Q+P+R+M.
\end{equation}
```

### 2.2 Assessment of the Resolution
- **Prior Finding Addressed**: In the prior text, $Q, P, R, M$ were referred to as "separate worst-case caps over complete branches." If an algorithm designer were free to declare arbitrary loose upper bounds (e.g., setting $Q = 10^9$ when the algorithm uses 10 queries), the assertion that $T = Q + P + R + M$ lies between the worst-case summed call count and four times that count would not hold.
- **Validity of the Mathematical Sandwich**: By defining $Q, P, R, M$ as the *smallest* worst-case caps over valid marked inputs and complete branches, they are identical to the actual branch maxima:
  $$Q = \max_{\text{branch}} q, \quad P = \max_{\text{branch}} p, \quad R = \max_{\text{branch}} r, \quad M = \max_{\text{branch}} m.$$
  For any branch, the summed call count is $C_{\text{branch}} = q + p + r + m$. The worst-case summed call count over all branches is $C_{\max} = \max_{\text{branch}} (q + p + r + m)$. By elementary inequalities:
  $$C_{\max} \le Q + P + R + M \le 4 C_{\max}.$$
  The factor-four sandwich is therefore mathematically exact and robust.
- **Impact on Proof and Resource Steps**:
  - *Reference World $O_0$ Truncation (Lines 244–247)*: The operational truncation rule dictates that the controller on $O_0$ halts if any counter would exceed $Q, P, R,$ or $M$. Because $Q, P, R, M$ are the branch maxima on valid marked inputs, this truncation never terminates a valid marked-input execution prematurely. The execution tree on $O_0$ remains strictly finite and prefix-free, with branch depths capped by $Q, P, R, M$.
  - *Query Frontiers and Distance Bound*: The number of query frontiers remains at most $Q$.
  - *Upper Bound Construction*: The matching algorithm pre-schedules all attempts, with deterministic call counts $Q = B(t+1)$, $P = Br$, $R = B$, $M = 0$ on all branches, identically matching the branch maxima.
- **Verdict on Delta**: The modification cleanly and completely resolves the finding without invalidating any mathematical or resource step, and introduces no new ambiguities or blockers.

---

## 3. Comprehensive Audit: Non-Claims and Attribution Lens

### 3.1 Theorem Scope and Persistent Adaptive CQP Correspondence
- **Model Definition (Lines 34–56, 166–258)**:
  - Considers unique-item search on $N \ge 2$ with a noiseless phase oracle $O_w$ and a postquantum Born sampler on register $S$ that projects with probability $\eps$ and leaves the global entangled state undisturbed with probability $1 - \eps$.
  - Sampler outcomes $y$ and collapse flags $c$ are delivered immediately to the classical controller to direct subsequent operations on the *same continuing quantum state*.
  - Cost is strictly charged-call: $T = Q + P + R + M$.
- **Persistent CQP Mapping (Lines 128–138, 587–608, Corollary 4)**:
  - In the ABFL author-hosted manuscript (\cite{abflcqp}, Sections 3, 6, 8), adaptive CQP is defined as sequential stages $(U_i, M_i)$ followed by full-register Born samples on the continuing state.
  - The manuscript's mapping (Lines 593–601) simulates each stage directly: $U_i$ is executed directly (oracle queries charged in $Q$); $M_i$ is executed as an allowed ordinary measurement (charged in $M$); each full-register Born sample is executed as a sampler call at $\eps = 0$ (charged in $P$).
  - *Critical Scope Restriction & Non-Claim*: Lines 599–608 explicitly emphasize:
    > *"Each returned sample is charged separately, not a free transcript for one circuit-oracle call. This preserves search-query and sample counts and adds at most one ordinary-measurement charge per sampled stage, without copies or replay... Thus the exact $\Theta$ law uses the charged-call convention here; elementary-gate runtime carries the stated logarithmic and parameter-processing overhead. No bound on oracle queries alone with unlimited free samples is asserted."*
  - This prevents any invalid claims that the lower bound applies to models where sampling is an unmetered, free side-effect of a single query.

### 3.2 Distinction from Stateless Oracle Adaptivity
- **Primary Citation**: Morimae, Shirakawa, and Yamakawa (MSY 2025, arXiv:2510.04448v1).
- **Audit of Distinction (Lines 134–138, 748–750)**:
  - In MSY (footnote 6, Section 5), the model considers adaptive queries to a *stateless* circuit-sampling oracle. In that framework, each query submits a circuit description $C$ and receives a sample from $C\ket{0}^{\otimes n}$; each invocation begins anew from the vacuum state.
  - In persistent adaptive CQP and the present model, the quantum state is persistent across gates and readouts, preserving entanglement and coherence across rounds.
  - The manuscript explicitly notes:
    > *"Adaptive calls to a stateless circuit-sampling oracle in \cite[footnote 6, Section 5]{msy} start independent invocations; their sampling-hardness equivalence does not supply this persistent-state bound. This is search-model inclusion, not equality of entire complexity classes."*
  - This distinction is accurate, necessary, and prevents erroneous conflation of circuit-oracle sampling hardness with persistent-state query lower bounds.

### 3.3 Prior-Work Attribution
The manuscript provides clear attributions for every component:
1. **ABFL (\cite{abfl}, arXiv:1412.6507v1 / ITCS 2016)** (Lines 59–61, 119, 656–661): Credited for establishing the non-collapsing measurement framework (PDQP) and the foundational partial-Grover plus repeated-sampling search algorithm. Explicitly distinguished from the author-hosted CQP manuscript (\cite{abflcqp}).
2. **Miloschewsky and Podder (\cite{mp}, CCC 2025 / arXiv:2411.04085v3)** (Lines 62–64, 119–127, 674–681): Credited for the ideal cube-root $\Omega(N^{1/3})$ lower bound, the conditional-copy framework, and the root-fidelity potential method. The manuscript candidly states:
   > *"We reconstruct the ideal inequality and extend its control scope; neither the deferred endpoint nor the use of conditional copies is a separate contribution."* (Lines 121–123).
   The open feedback question from MP Section 1.5 is cited as direct motivation.
3. **Abbas et al. (\cite{abbas}, NeurIPS 2023)** (Lines 139–148, 682–689): Credited for proving that gentle imperfect measurements can support cube-root search (Proposition 28). Accurately distinguished: Abbas et al. require multi-copy states ($O(\log N)$ copies) and uniform $1/N$-gentleness on every measurement ($\|\mathcal{E}(\rho) - \rho\|_1 \le 1/N$). In contrast, accidental collapse is a rare event that causes $O(1)$ disturbance upon projection. The manuscript disclaims novelty for the general concept of imperfect readout robustness, isolating its claim to the exact all-$\eps$ tradeoff for independent projections.
4. **Regev and Schiff (\cite{rs}, ICALP 2008 / arXiv:1202.1027v1)** (Lines 75–77, 149–153, 690–695): Credited for lower bounds on faulty oracle calls; distinguished by noise location (oracle calls remain noiseless here).
5. **Rosmanis (\cite{rosmanis}, arXiv:2309.14944v1)** (Lines 77–78, 150–154, 221–235, 696–700): Credited for search under noisy oracles with recorded error flags. Distinguished by the non-CPTP character of record-retaining Born instruments (equation \eqref{eq:record}) compared to standard dephasing channels.
6. **Fiorentino and Weigert (\cite{fw}, PLA 2025 / arXiv:2303.13411v2)** (Lines 155–159, 701–706): Credited for passive-measurement theory; distinguished by composition rules and absence of the charged independent-collapse tradeoff.
7. **Gilchrist, Langford, and Nielsen (\cite{gln}, PRA 2005 / quant-ph/0408063v2)** (Lines 163–164, 281–286, 707–712): Credited for standard root-fidelity and Bures metric triangle inequalities.

### 3.4 Novelty Limitations and Literature Search Disclosures
- **Search Boundaries (Lines 160–162, 736–743)**: The manuscript explicitly documents its search history (conducted November 14 and 15, 2026), listing exact queries and candidate papers screened at the abstract level ([Cakan et al. 2510.05055v1](https://arxiv.org/abs/2510.05055v1), [Morimae et al. 2510.04448v1](https://arxiv.org/abs/2510.04448v1), [Lolck et al. 2411.04931v1](https://arxiv.org/abs/2411.04931v1)).
- **Candid Limitations**: The author explicitly records:
  > *"This is a bounded literature comparison, not an assertion of exhaustive priority... No author contact, unpublished-work check, independent expert review or exhaustive citation crawl occurred."* (Lines 161–162, 740–741).
- **Core Novelty Confined**: The text narrows its specific contributions to:
  1. The fixed-power potential comparison with copy exponent $k = \lceil 1/\eps \rceil$ that maintains monotonicity through arbitrarily many readouts;
  2. The extension of both lower-bound arguments to immediate adaptive feedback on persistent states via finite-tree induction and query-frontier alignment;
  3. The fully charged matching construction proving tightness across all $0 \le \eps \le 1$.

### 3.5 Physical, Complexity-Class, and Algorithmic Non-Claims
The manuscript enforces strict conceptual safeguards:
1. **No Physical Implementation Claims (Lines 54–55, 71–74, 628–634)**: Explicitly disclaims physical realizability on noisy quantum devices, characterizing the primitive strictly as an idealized postquantum information resource.
2. **No Complexity Class Collapses (Lines 54–55, 632–634)**: Explicitly disclaims implications for ordinary $\text{BPP}$ vs $\text{BQP}$, noting that the interpolation is an oracle-model result.
3. **No Unrealistic Postquantum Capabilities (Lines 197–200, 205–207)**: Disclaims unknown-state readout, physical state cloning, state rewinding, chosen-outcome projection, free postselection, or nonlinear maps on reduced density matrices.
4. **No Free Restarts or Unbounded Stopping Times (Lines 248–251)**: All attempts are pre-scheduled and charged ($B = 13120$); no expected-cost or unbounded stopping-time theorem is asserted.
5. **No Practical Asymptotic Overstatement (Lines 536–538)**: Explicitly notes that constant factors certify an asymptotic scaling law, not practical running times.

### 3.6 AI and Evidence Disclosures
- **AI Tooling Disclosure (Lines 642–646)**: Fully and transparently discloses that OpenAI Codex assisted with derivation, literature comparison, drafting, and internal checking. Discloses that separate provider CLI AI reviews were conducted, with model identities, scopes, findings, and dispositions preserved in repository logs.
- **Status of Evidence (Lines 636–642, 645–647)**: Emphasizes that the manuscript contains an informal analytic proof and internal checks, explicitly disclaiming human peer review or formal kernel certification. Clarifies that preserved diagnostic numerical runs illustrate algebraic identities but do not establish universal theorems by finite verification.
- **Open Availability (Lines 648–652)**: Complete LaTeX, reproducibility records, and citation metadata are identified at [https://github.com/Quantyra/accidental-collapse-search](https://github.com/Quantyra/accidental-collapse-search) under a CC BY 4.0 license.

---

## 4. Attempted Counterexamples and Adversarial Stress Tests

### Stress Test 1: Bypassing Lower Bounds via Unbounded Free Sampling in Adaptive CQP
- *Adversarial Hypothesis*: In persistent adaptive CQP, an algorithm performs $O(1)$ Grover queries to create an overlap of $O(1/\sqrt{N})$, and then applies $P = \Theta(N)$ non-collapsing Born samples at $\eps = 0$ on the continuing state. If sampling is free, search succeeds in $O(1)$ oracle queries, which is $o(N^{1/3})$.
- *Defense in Text*: Corollary 4 (lines 599–608) and Theorem 1 (lines 83–94, 240–243) explicitly evaluate total cost under the charged-call convention $T = Q + P + R + M$, wherein every sampler call is charged in $P$. The text explicitly notes: *"No bound on oracle queries alone with unlimited free samples is asserted."*
- *Result*: Defeated; the non-claim is explicit, exact, and structurally sound.

### Stress Test 2: Transferring MSY (2025) Sampling Hardness to Persistent CQP
- *Adversarial Hypothesis*: Since Morimae, Shirakawa, and Yamakawa (2025) proved equivalence between sampling hardness and quantum cryptography under adaptive non-collapsing measurements, one might argue that persistent CQP search lower bounds follow automatically from their equivalence.
- *Defense in Text*: Lines 134–138 explicitly refute this transfer: MSY's equivalence concerns *stateless* circuit-sampling oracles where each query resets to $\ket{0}^{\otimes n}$, whereas persistent CQP allows operations on the *same continuing quantum state*. The text notes: *"Adaptive calls to a stateless circuit-sampling oracle in \cite[footnote 6, Section 5]{msy} start independent invocations; their sampling-hardness equivalence does not supply this persistent-state bound."*
- *Result*: Defeated; the conceptual distinction is rigorously maintained.

### Stress Test 3: Exploiting Uncapped Reference Executions on $O_0$
- *Adversarial Hypothesis*: Consider an algorithm that stops only upon measuring the marked item $w$. On valid marked inputs $w \in [N]$, it halts within caps $Q, P, R, M$. On the all-zero reference oracle $O_0 = I$, no marked item exists, so it loops indefinitely, preventing the definition of a finite prefix-free cut for the potential comparison.
- *Defense in Text*: Lines 244–247 mandate operational truncation: *"The finite controller and caps apply on every execution, including the reference oracle $O_0$. Enforce them by halting before a cap would be exceeded; if initially promised only on marked inputs, this truncation leaves every valid-input execution unchanged."*
- *Result*: Defeated; execution trees on $O_0$ are finite and prefix-free by operational mandate.

### Stress Test 4: Conflating Accidental Collapse with Gentle Measurements (Abbas et al.)
- *Adversarial Hypothesis*: Abbas et al. (2023) established that cube-root search is robust to $1/N$-gentle measurements. One could argue that an accidental collapse probability of $\eps = 1/\sqrt{N}$ is "gentle on average" and should achieve $O(N^{1/3})$, contradicting Theorem 1's prediction of $\Theta(N^{1/3} + \sqrt{\eps N}) = \Theta(N^{1/3} + N^{1/4}) = \Theta(N^{1/3})$ or fixed $\eps > 0$ yielding $\Theta(\sqrt{N})$.
- *Defense in Text*: Lines 142–148 explain that Abbas et al. require gentle disturbance on *every* measurement outcome ($\|\mathcal{E}(\rho) - \rho\|_1 \le 1/N$). Accidental collapse is an independent rare event with order-one disturbance on the conditional state when it occurs ($c=1$). For any fixed $\eps > 0$, the channel has $\Theta(1)$ conditional disturbance.
- *Result*: Defeated; the physical regimes and mathematical models are properly distinguished.

### Stress Test 5: Inconsistency in the Factor-Four Cost Sandwich
- *Adversarial Hypothesis*: If $Q, P, R, M$ are arbitrary user-specified caps, then $T = Q + P + R + M$ could exceed four times the actual worst-case branch call count $C_{\max}$.
- *Defense in Text*: Lines 236–239 in Final2 explicitly define $Q, P, R, M$ as the *smallest* worst-case caps over valid marked inputs and complete branches, explicitly identifying them as branch maxima. Thus $C_{\max} \le T \le 4 C_{\max}$ holds unconditionally.
- *Result*: Defeated; the Final2 delta closes the issue rigorously.

---

## 5. Substantive Findings Summary Table

| ID | Location | Severity | Description | Disposition |
|---|---|---|---|---|
| **F-01** | Lines 236–239 | Resolved / Minor | Definition of $Q,P,R,M$ as smallest worst-case caps (branch maxima) to validate the factor-four sandwich. | Fully resolved in Final2 delta; sandwich $C_{\max} \le T \le 4 C_{\max}$ is mathematically exact. |
| **F-02** | Lines 244–247 | Resolved / Minor | Enforcement of caps on reference oracle $O_0$ via operational truncation. | Fully resolved; ensures finite prefix-free cuts on $O_0$ without affecting valid executions. |
| **F-03** | Line 195 | Resolved / Minor | Classical randomness measure support. | Fully resolved; explicit restriction to finite-support classical randomness. |
| **F-04** | Lines 593–608 | Resolved / Minor | Syntax mapping and query-only free-sample disclaimers for persistent CQP. | Fully resolved; explicit simulation mapping and charged-call convention disclaim free-sample models. |
| **F-05** | Lines 134–138 | Verified / Note | Distinction between persistent CQP and stateless circuit-oracle adaptivity (MSY). | Accurate, clear, and prevents invalid literature transfers. |
| **F-06** | Lines 636–647 | Verified / Note | AI assistance and evidence disclosures. | Transparent, comprehensive, and accurately distinguishes informal proofs from formal certification. |

---

## 6. Final Audit Verdict

The manuscript revision v0.2.0 (SHA-256: `47384ca46a9b823927da5784ea9d67a1cb14b18d10cfd8a958efb21e56e6e1d3`) is fully self-consistent, mathematically sound in its cost definitions, accurate in its attributions to primary literature, and rigorous in its disclaimers and non-claims.

**Final Determination**: **GO**
