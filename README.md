# Optimal Search and Positive-Adversary Bounds with Accidentally Collapsing Measurements

**Version 0.4.0: reviewed release candidate; archival publication pending.** The auxiliary implementation-error theorem gives `TV <= min{1,sqrt(K) sum_j delta_j + P tau}` for the same finite capped controller and exact oracle, where K=min{P+1,ceil(1/epsilon)} (P+1 at zero). Uniform ordinary-gate errors and a separately coupled rate error preserve arbitrary workspace, partial measurements, immediate feedback and unequal stopping. Precision, success and full compilation costs are explicit; no physical-noise or first-continuity claim. The existing search and adversary results below remain.

Version 0.3.0 adds a second main theorem: every finite Boolean promise problem in the same model satisfies `Q min{P+1,ceil(1/epsilon)} >= Adv_+(f)/36`, using P+1 at epsilon=0. Here Adv_+ is the positive spectral adversary. Complete-history query probabilities remove any branch-count factor; the proof preserves immediate feedback, partial measurements and unequal stopping. For n-bit parity, fixed positive epsilon requires Omega(n) queries. The original sharper search law is retained. Certificates can be exponential analytical objects; no signed-adversary or efficient-discovery result is claimed.

**Previous version 0.3.0: published and verified.** [DOI 10.5281/zenodo.24261197](https://doi.org/10.5281/zenodo.24261197); [concept DOI 10.5281/zenodo.24244952](https://doi.org/10.5281/zenodo.24244952). Previous published version 0.2.0: [DOI 10.5281/zenodo.24255781](https://doi.org/10.5281/zenodo.24255781). Previous published version 0.1.0: [DOI 10.5281/zenodo.24244953](https://doi.org/10.5281/zenodo.24244953). Daniel Fredriksen, Quantyra Inc. [ORCID 0009-0002-9123-7435](https://orcid.org/0009-0002-9123-7435). [Read the PDF](manuscript/main.pdf) or [LaTeX source](manuscript/main.tex).

We study a hypothetical Born sampler that independently projects the sampled register with probability epsilon and otherwise leaves the global state intact. Sampler outcomes and collapse flags may immediately control later operations on the same continuing state. With a noiseless search oracle, the optimal constant-success unique-item search cost is

\[
T_*(N,\varepsilon)=\Theta(N^{1/3}+\sqrt{\varepsilon N}).
\]

The cost charges every oracle call, sampler call, fresh attempt and ordinary measurement/reset. The lower bound covers arbitrary entangled workspace and partial-register measurements: Q^2(P+1) >= N/32 and Q^2 ceil(1/epsilon) >= N/32 for N >= 12 (the second for epsilon > 0). Each whole-register readout counts as one call. The construction separately pays gates, space, O(P log N) transcript bits and precision; the theorem is stated for N >= 2.

Version 0.2.0 extended the fixed/decreasing-power comparisons to immediate feedback through complete-history finite-tree induction and query-frontier alignment. At epsilon=0 this covers the cited persistent CQP search model. The matched exponent and upper algorithm are unchanged. ABFL supplies the algorithmic template; Miloschewsky--Podder supplies the ideal endpoint and conditional-copy/fidelity precedent; Abbas et al. supplies prior imperfect-readout robustness. [Source comparison and provenance](SOURCES.md) distinguish these contributions from noisy-oracle models. The theorem is not a physical noise result, a full noisy-PDQP classification, or an ordinary BPP/BQP advance.

## Contents and evidence

- [Manuscript](manuscript/main.tex): complete model, proof, construction, resource accounting and references.
- [Review record](REVIEW.md): internal checks, separate CLI AI-review reports and dispositions; no human peer review or formal certification.
- [Preserved diagnostic evidence](evidence/README.md): original scripts, preregistrations and receipts, with hashes. Finite checks do not prove the general theorem.
- [Publication status](publication/README.md): release readiness and archival verification.
- [CITATION.cff](CITATION.cff) and [.zenodo.json](.zenodo.json): author, title, license and archival metadata.

## Build and verify

Use Python 3.13, Tectonic 0.17.0 and the pinned packages in [tools/requirements.txt](tools/requirements.txt). Install these in your own environment. Then run:

```sh
python -m pip install -r tools/requirements.txt
python tools/build.py --tectonic /path/to/tectonic --render
python tools/check_package.py
```

Build outputs and page renders go in ignored `.build/`; the PDF and build receipt are retained. Package validation checks the existing inventory without executing the research diagnostics. After intentional artifact changes and a new visual inspection, `python tools/check_package.py --write` records the revised inventory. Build and package checks are document verification, not mathematical or formal certification. Reproduction of historical diagnostics is described separately in [evidence/README.md](evidence/README.md).

## Archiving

Version 0.4.0 has completed fresh three-provider AI review with all findings dispositioned and no unresolved blocker. Exact release and public archive verification remain pending; the existing Zenodo integration will be reused. For the published version 0.3.0, three-provider AI review had no unresolved blocker and document, metadata and clean-build checks passed. Its [public archive receipt](publication/zenodo-v0.3.0-verification.json) verifies the DOI metadata, all 110 archived files and the release PDF against the frozen tag. Citation and verification records added after publication remain separate from the immutable archive.

Previous publications remain immutable:

- v0.2.0, immediate-feedback search: [version DOI](https://doi.org/10.5281/zenodo.24255781), [archive receipt](publication/zenodo-v0.2.0-verification.json); all 83 archived files and PDF verified.
- v0.1.0, deferred-feedback search: [version DOI](https://doi.org/10.5281/zenodo.24244953), [archive receipt](publication/zenodo-v0.1.0-verification.json); all 54 archived files and PDF verified.

The [concept DOI](https://doi.org/10.5281/zenodo.24244952) identifies the version family. Citation and verification additions after each release are not claimed to be inside its immutable archive. Lean certification remains separate.

Original archive materials are licensed under [CC BY 4.0](LICENSE). Cited third-party works retain their own licenses. OpenAI Codex assisted derivation, literature comparison, drafting and internal checking. No independent peer review or formal certification is claimed.
