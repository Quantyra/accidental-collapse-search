# Three-lens findings and disposition

Date: 2026-11-15. Status: COMPLETE. All three revised-source lenses completed; there is no unresolved blocking finding. The original Grok attempt timed out without a report and remains excluded from clearance. This is informal AI review, not human peer review or formal certification. Immutable initial packets identify the original candidate and full source. Reports are reviewer statements; the coordinator adjudicates them against the mathematics and primary evidence.

## Initial findings

| ID | Lens / severity | Disposition |
| --- | --- | --- |
| C1 | Proof-adversarial / MEDIUM | Accept explicit domain repair: state N >= 2 and prove the bounded 2 <= N < 12 lower bound by zero-query input independence. N=1 requires no input access. The asymptotic rate is unchanged. |
| C2 | Proof-adversarial / LOW | Accept alignment clarification: compare the j-th-query frontiers, using history exponent kappa(h)=P+1-p(h) for actual branch readouts. Intermediate nonquery subtrees are monotone; query sensitivity uses max kappa <= P+1. This is an analytical alignment, with no operational rescheduling or deferred-record access. Claude and Grok final-source checks explicitly validate the construction. |
| C3 | Proof-adversarial / LOW | Accept error-contract clarification: require trace-distance control on each actual conditional global pure preparation branch, with independent within-attempt preparation. A bound only on an averaged reduced state is not asserted. Exact-gate main theorem unchanged. |
| C4 | Proof-adversarial / LOW | Accept separate reset conventions: measurement-and-reprepare creates a classical history outcome; swap-to-environment is an isometry with no fictitious conditioned outcome. Both obey their respective lower-bound comparison. The attaining main construction uses M=0. |
| C5 | Proof-adversarial / LOW | Retain declared deferred-outcome scope. The reviewer suggests a possible adaptive extension; no such extension, novelty claim or successor investigation is selected. |
| C6 | Proof-adversarial / expository note | Add the Cauchy--Schwarz justification that a zero-probability overlap term vanishes. |
| A1 | Non-claims / LOW | Accept explicit abstract/README statement that a whole-register readout is one call and the construction separately charges O(P log N) transcript bits. |
| A2 | Non-claims / LOW | Update all post-review disclosures to reflect actual separate CLI AI review as completed; keep human/formal certification and release status distinct. AGY final-source check confirms the wording. |
| A3 | Non-claims / LOW | Reject the proposed attribution change as unsupported by its cited proposition. The primary proof of Abbas et al., Appendix E.4, Proposition 28, uses O(log N) copies and 1/N-gentleness. The reviewer asserted a single-copy N^(-2/3) statement that is not present there. Retain multiple-copy attribution and add the explicit source parameters. AGY explicitly withdrew its assertion in the revised-source report. This does not rule out a different single-copy argument; none was supplied. |

Primary evidence for A3: [NeurIPS 2023 proceedings PDF, page 28](https://proceedings.neurips.cc/paper_files/paper/2023/file/8c3caae2f725c8e2a55ecd600563d172-Paper-Conference.pdf), SHA-256 `7e6e144f88aeabb8c8f93a02127ff74a1e93c9c83e52c14a5f546f09b688d829`, already pinned in the archive. This was a named source check of a reviewer claim, not a new broad novelty search. Some report line numbers refer to combined packets, and AGY calls the reset counterexample Remark 4; its manuscript location is Section 5, Remark 5. Exact section/equation references govern the dispositions.

Review completion is specific to source `617e873d184ece9c3b51c0a98b1669cc74c2d36a52396a7a35e75e684349885e`. No archival release or DOI is created by this review.

## Revised-source checks received

Claude reviewed source `617e873d184ece9c3b51c0a98b1669cc74c2d36a52396a7a35e75e684349885e` and returned GO-WITH-NOTES, with no HIGH/MEDIUM finding or declared-model gap. Initial C1-C4 are explicitly resolved. Two remaining LOW suggestions concern making the larger ordinary-control class and fixed-cut use of the metric even more explicit. These are accepted as nonblocking explanatory notes, with no further source change required: the declared theorem retains its fixed sampler schedule; the lower proof supplies the more general frontier comparison; metric triangle comparisons occur within a common history cut, and comparisons across cuts use only the scalar fidelity inequality. The per-history query sum is bounded by its maximum exponent exactly as stated. These notes do not authorize a broader sampler-feedback theorem. Claude's metadata-verification limit is respected: the coordinator, not that reviewer, verifies the archive record.

AGY returned GO for the same source, confirmed the unit-cost/disclosure changes, and withdrew A3. Its only remaining observation is future release-version consistency, which is release packaging outside this review request. AGY did not independently inspect the primary source; its retraction follows the coordinator's source check, which is documented above. Available/configured AGY model is Gemini 3.8 Flash High; its returned JSON does not attest model identity. No legacy Gemini Pro formal-certification result is claimed.


Grok completed its revised-source full resource review in 1,152.46 seconds with returned model `grok-4.7-build` and verdict GO. It found no manuscript defect or unpaid resource. The earlier 1,200.19-second noncompletion remains a separate operational exclusion; the prepared alternative-provider packet was never launched and is not counted as a review.

One minor error in the Grok report is not adopted: its prose writes r <= (N')^(1/3), dropping a ceiling. The exact safe bound is r <= N'/m^2 + 1 <= (N')^(1/3) + 1. The manuscript already defines r with the ceiling and only asserts N'/m^2 <= (N')^(1/3), so its O-bound is unaffected and no paper change is needed. Likewise the report's broad statements of non-applicability outside the model are read as scope limits, not proofs that extensions fail. Neither the reviewer nor this record certifies novelty or the impossibility of other models.

## Final lens table

| Lens | Actual final-source result | Disposition |
| --- | --- | --- |
| Proof-adversarial / Claude Code | GO-WITH-NOTES | Initial domain, alignment, approximation and reset items resolved; remaining LOW exposition notes accepted as nonblocking. |
| Complexity/resource / Grok | GO | Complete revised-source review; paid query/readout/preparation/reset, gate, transcript, space and precision costs supported. Reviewer ceiling shorthand corrected in this disposition. |
| Non-claims/attribution / AGY | GO | Unit-cost and AI-review disclosures accepted; unsupported initial source assertion withdrawn. |

All three final reports identify the same source hash. The [manifest](manifest.json) binds provider/model evidence, packet hashes, reports, completion markers and this disposition. Claude and Grok returned model identities; AGY's model is a configured identity only. These are separate AI reviews, not human peer review, an independent serving audit or formal certification. No new general complexity bound or successor investigation follows. Release versioning and the first archival release remain separate from the completed review request.
