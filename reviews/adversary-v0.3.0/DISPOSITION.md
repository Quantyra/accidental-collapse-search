# v0.3.0 three-provider findings and dispositions

The three lenses ran through their actual provider CLIs on immutable packets. Claude returned `claude-opus-5-5`; Grok returned `grok-4.7-build`; AGY was configured as `gemini-3.8-flash-high`, but its response does not attest a serving model. Binary, packet, source, raw-response and public-report identities are recorded in the manifest. Raw responses remain local; only final reviewer reports are published, with local sandbox links replaced by links to the corresponding archived packet. These substitutions are counted and do not alter findings. No provider-authentication, model-routing or serving-infrastructure assurance is inferred beyond that evidence.

Initial source: `9fb7efb8a19ffcdaedb5b8bd286f51c8802b4f0b80a684151cbf6a768872d1d0`. Final source: `88bcf523f4fccac8422273bb65a02995304f6a68bc911b20e7b8383de03a44c6`. Every final report covers the latter. No manuscript-source substitution follows final review.

## Initial findings

| Reviewer / item | Finding | Disposition |
| --- | --- | --- |
| Claude N1 | Rayleigh-maximizer-to-eigenvector step is implicit and the eigen-equation is unused. | Implemented: use directly the nonnegative unit vector with Rayleigh quotient equal to the spectral norm. This is a presentation simplification; the earlier argument already allowed reducible matrices. |
| Claude N2 | Classical random branching is not explicitly listed among local comparisons. | Implemented: child pair weights multiply by common probabilities summing to one. |
| Claude N3 | The decreasing-power zero-overlap case is implicit. | Implemented: A=0 makes the old contribution zero. |
| Claude N4 | Parity hides the collapse-rate dependence in Omega(n). | Implemented: Q >= n/(36 ceil(1/epsilon)) is explicit; at epsilon=0 give only the proved Q(P+1)>=n/36 tradeoff. |
| Claude N5 | Version-history tense can sound like a current-version claim. | Implemented: since v0.2.0 the comparisons cover immediate feedback. |
| Claude N6 | README archiving prose mixes version histories and contains a malformed sentence. | Implemented: coherent prior-version list and rewritten current metadata. |
| Claude N7 | Fresh-attempt boundaries could be defined more formally. | Deferred as optional exposition: both lower bounds use Q/P only; the upper construction explicitly defines and pays all B attempts. Ancilla initialization remains paid in gate/space work. Final proof recheck accepts this disposition. No altered resource model is introduced. |
| AGY N-01 | Explain the maximum-to-sum inference for total calls. | Implemented: derive the two bounds separately and use max >= half their sum. |
| AGY N-02 | Clarify the ideal parity endpoint. | Implemented as the proved tradeoff only. The manuscript does not infer a faster ideal algorithm from a lower bound. |
| AGY N-03 | Internal research hashes are provenance. | Retained; the manuscript is self-contained and does not depend on private research files. |
| Grok initial | No correctness, resource or optional-exposition defect reported. | GO on the full initial audit; final-source recheck verifies the subsequent limited changes. |

## Final-source coverage and judgment

No unresolved blocking finding remains. The manifest records each actual final verdict and exact reviewed source. The general theorem's positive-weight restriction, two separate powers, history/query normalization, terminal separation, finite feedback/stopping model, parity example and complete cost/precision limits are covered. The sharper search law and construction are retained.

Claude's remaining README layout suggestion is addressed as a public-status edit: explicitly label v0.3.0 in the opening claim and v0.1.0 in the previous-version line. The manuscript source is unchanged. N7 remains an explicitly accepted nonblocking limitation. Publication status and DOI receipt labels change only after actual publication, without a new mathematical claim.

Two reviewer glosses are not adopted as stronger findings. The search law is stronger uniformly; it is not strictly asymptotically stronger at every fixed positive rate. Replacing the unused eigen-equation did not remove an irreducibility assumption: none was present. AGY's broad wording about eliminating that assumption is therefore not treated as a correction of a mathematical defect. Provider equation/corollary numbers sometimes refer to packet lines rather than compiled numbering; named manuscript statements and the source hashes determine scope.

## Trust and preservation

The coordinator separately inspected the pinned primary MP and Spalek--Szegedy statements and preserved the earlier source correspondence. Reviewers were limited to supplied packets and did not independently fetch the literature. Their approvals are not exhaustive novelty clearance, human peer review, formal certification or physical evidence. The theorem remains a positive-adversary result in the specified hypothetical sampler model; no signed-adversary, efficient certificate-discovery or ordinary BPP/BQP conclusion is claimed.

All initial and final reports are preserved, including nonblocking notes. The two historical diagnostic runs and previous publication/review records remain byte-identical; no new research diagnostic was executed. Build, all-page visual inspection, metadata and exact-byte checks are operational assurance, not a kernel proof. Full-manuscript certification remains separately queued with its existing owner.
