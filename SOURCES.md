# Sources, attribution and provenance

The manuscript is self-contained. Its analytic source was frozen at commit `761389cae990d8fdd70458239d137ec9db2b2275` and its focused novelty comparison at `dd6eb45cd2be4d0e4a556394ff2abaad04f4288e` in the author's technical research repository. [Provenance](evidence/provenance.json) retains original source hashes and byte-identical own diagnostic evidence. These commit identifiers are provenance, not a requirement for reader access to a separate repository.

## Closest primary results

| Source and inspected version | What is inherited or distinguished |
| --- | --- |
| [Aaronson, Bouland, Fitzsimons, Lee, *The space ?just above? BQP*, arXiv:1412.6507v1](https://arxiv.org/html/1412.6507v1), 2014 preprint / ITCS 2016; Sections 2, 4 and Appendix E | Non-collapsing computation and the partial-Grover/repeated-sampling algorithm template. Not a new template here. |
| [Miloschewsky?Podder, *New Lower-bounds for Quantum Computation with Non-Collapsing Measurements*, arXiv:2411.04085v3](https://arxiv.org/html/2411.04085v3), September 2025; Sections 3?4 and Section 1.5; [CCC 2025 publication](https://doi.org/10.4230/LIPIcs.CCC.2025.12) | Ideal cube-root lower bound and conditional-copy/fidelity precedent. Their broader noisy-computation question motivates this specific model. A readout-dependent exponent cannot simply be replaced by a mean collapse waiting time. |
| [Amira Abbas et al., *On quantum backpropagation, information reuse, and cheating measurement collapse*](https://proceedings.neurips.cc/paper_files/paper/2023/file/8c3caae2f725c8e2a55ecd600563d172-Paper-Conference.pdf), NeurIPS 2023, Appendix E.4, Proposition 28 | Prior cube-root upper bound under gentle imperfect measurements on multiple copies; the cited proof uses O(log N) copies and 1/N-gentleness. Small conditional disturbance is not independent rare projection; no matching all-rate lower bound for this sampler follows. |
| [Regev?Schiff, *Impossibility of a Quantum Speed-up with a Faulty Oracle*](https://arxiv.org/html/1202.1027v1), ICALP 2008 / 2012 arXiv upload; Theorem 1 | Faults occur at oracle calls. This theorem keeps the oracle noiseless and adds nondisturbing sampled information. |
| [Rosmanis, *Quantum Search with Noisy Oracle*, arXiv:2309.14944v1](https://arxiv.org/html/2309.14944v1), 2023; model, Theorem 1, Sections 3?6 and 8 | Closest inspected partial-register/flag comparison, but its ordinary oracle-noise instrument lacks the nondisturbing Born record. Matching discarded-record marginals do not equate operations. |
| [Fiorentino?Weigert, *A Quantum Theory with Non-Collapsing Measurements*, arXiv:2303.13411v2](https://arxiv.org/html/2303.13411v2), 2025; Sections II, V.2?3 and VI.2 | Passive-measurement composition and single-copy state reconstruction have a different measurement-cost and state-update contract. |
| [Gilchrist?Langford?Nielsen, *Distance measures to compare real and ideal quantum processes*, quant-ph/0408063v2](https://arxiv.org/html/quant-ph/0408063v2), PRA 71 (2005); Section III | Standard fidelity/Bures facts, converting squared fidelity to the root-fidelity convention used here. |

The retained contribution is the fixed conditional-history exponent k = ceil(1/epsilon), its noisy-readout monotonicity, the square-root query sensitivity, and the matched fully charged search law. Jensen, AM?GM, the Bures metric, the ideal endpoint and diagnostic counts are not separate new results.

## Search limits

The November 14, 2026 comparison searched variants of non-collapsing/noncollapsing with noise, imperfect, accidental, probabilistic, partial collapse, robustness, fidelity/Bures and search, plus PDQP noise and recent follow-ups. The named transfer questions were whether gentle-copy robustness, faulty/noisy-oracle bounds, the ideal copy method, or passive reconstruction already imply this exact instrument and cost contract. The compared statements do not directly do so; no identical theorem was found. Absence of a search hit is not exhaustive priority certification.

Additional abstracts only were screened: [Cakan et al. 2510.05055v1](https://arxiv.org/abs/2510.05055v1), [Morimae, Shirakawa and Yamakawa 2510.04448v1](https://arxiv.org/abs/2510.04448v1), and [Lolck, Mancinska and Paraashar 2411.04931v1](https://arxiv.org/abs/2411.04931v1). These were not full-proof audits and carry no theorem-level novelty conclusion here. No author contact, unpublished-work check, independent expert review or exhaustive citation crawl occurred.

[Primary-source pins](evidence/primary-source-pins.json) identify the inspected files without redistributing full third-party texts. The manuscript bibliography links directly to the primary sources. Original results, the protected-workspace counterexample and the earlier weaker signed-score estimate remain in the source history; the paper centers the final matched theorem.
