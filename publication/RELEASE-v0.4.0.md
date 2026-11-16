# P011 v0.4.0: adaptive implementation-error guarantees

This revision closes the manuscript's general ideal-to-implemented accuracy-transfer gap. For the same finite capped controller and exact input oracle, the full visible transcript changes by at most

TV <= min{1, sqrt(K) sum_j delta_j + P tau},

where K=min{P+1,ceil(1/epsilon)} (P+1 at epsilon=0), delta_j uniformly bounds ordinary-gate operator-norm error at the jth gate and tau bounds a separately coupled collapse-rate error for the same frozen policy.

The proof preserves arbitrary workspace and purification, partial measurements, immediate feedback and unequal stopping without dimension, history-count or inverse-probability losses. Explicit precision, success, repetition, gate-description evaluation, certified polar rounding/dilation/synthesis, memory and transcript costs are included. The sharp search law and general positive-adversary theorem remain.

The precision theorem is an auxiliary consequence of existing power comparisons. ABFL gate-set independence, Cakan et al. conditional-copy continuity and Dawson--Nielsen synthesis are attributed. No new framework, first-continuity, physical-noise or ordinary BPP/BQP claim is made.

Fresh actual Claude, Grok and AGY reviews and final-source rechecks are archived with findings and dispositions. No unresolved blocker remains. The 18-page PDF, metadata, preserved evidence and clean rebuild are verified. AI review is not human peer review or formal certification; full PaperMill certification remains separately queued.

The existing Zenodo integration creates a new version in the same DOI family. Its actual DOI and archive verification will be recorded after publication. Previous versions remain immutable. Original archive materials: CC BY 4.0. Daniel Fredriksen, Quantyra Inc., ORCID 0009-0002-9123-7435.
