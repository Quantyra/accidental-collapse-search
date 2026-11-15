# v0.2.0: Immediate-feedback search

This revision extends the matching search law Theta(N^(1/3)+sqrt(epsilon N)) to finite capped controllers that immediately use sampler outcomes and collapse flags to select later operations on the same surviving state. Deferred feedback remains a special case. Both N/32 lower bounds and the paid upper construction remain.

The expanded proof handles unequal sampling and stopping through complete-history finite-tree induction and branchwise query frontiers. The ideal endpoint covers the cited persistent adaptive CQP search procedures with individually charged samples. All attempts and additional gate, classical parameter, space, transcript and precision costs are explicit; no query-only free-sample or exact elementary-runtime claim is made.

Fresh Claude, Grok and AGY AI reviews and final-source checks are archived with dispositions. Stopping caps, finite-support randomness, the branch-maxima convention and source-model accounting were clarified. This is an informal research preprint, without independent human peer review or Lean certification. No physical implementation or ordinary BPP/BQP result is claimed.

Author: Daniel Fredriksen, Quantyra Inc., ORCID 0009-0002-9123-7435. License: CC BY 4.0. The v0.1.0 archive and DOI remain unchanged. Zenodo assigns this release a new version DOI under the existing concept DOI.
