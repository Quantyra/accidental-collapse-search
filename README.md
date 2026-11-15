# Optimal Search with Accidentally Collapsing Measurements

**Published preprint, version 0.2.0.** [DOI 10.5281/zenodo.24255781](https://doi.org/10.5281/zenodo.24255781). Previous published version: [DOI 10.5281/zenodo.24244953](https://doi.org/10.5281/zenodo.24244953). Daniel Fredriksen, Quantyra Inc. [ORCID 0009-0002-9123-7435](https://orcid.org/0009-0002-9123-7435). [Read the PDF](manuscript/main.pdf) or [LaTeX source](manuscript/main.tex).

We study a hypothetical Born sampler that independently projects the sampled register with probability epsilon and otherwise leaves the global state intact. Sampler outcomes and collapse flags may immediately control later operations on the same continuing state. With a noiseless search oracle, the optimal constant-success unique-item search cost is

\[
T_*(N,\varepsilon)=\Theta(N^{1/3}+\sqrt{\varepsilon N}).
\]

The cost charges every oracle call, sampler call, fresh attempt and ordinary measurement/reset. The lower bound covers arbitrary entangled workspace and partial-register measurements: Q^2(P+1) >= N/32 and Q^2 ceil(1/epsilon) >= N/32 for N >= 12 (the second for epsilon > 0). Each whole-register readout counts as one call. The construction separately pays gates, space, O(P log N) transcript bits and precision; the theorem is stated for N >= 2.

The revision extends the fixed/decreasing-power comparisons to immediate feedback through complete-history finite-tree induction and query-frontier alignment. At epsilon=0 this covers the cited persistent CQP search model. The matched exponent and upper algorithm are unchanged. ABFL supplies the algorithmic template; Miloschewsky--Podder supplies the ideal endpoint and conditional-copy/fidelity precedent; Abbas et al. supplies prior imperfect-readout robustness. [Source comparison and provenance](SOURCES.md) distinguish these contributions from noisy-oracle models. The theorem is not a physical noise result, a full noisy-PDQP classification, or an ordinary BPP/BQP advance.

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

The author authorized this revision after the immediate-feedback proof, with fresh review and versioned archival publication. v0.2.0 is published and verified: [version DOI](https://doi.org/10.5281/zenodo.24255781), [concept DOI](https://doi.org/10.5281/zenodo.24244952), [public receipt](publication/zenodo-v0.2.0-verification.json). All 83 archived files and the release PDF match the frozen tag. Citation/receipt changes are post-release records. The prior release remains: The existing Zenodo release integration has been verified. Version v0.1.0 is published and verified: [version DOI](https://doi.org/10.5281/zenodo.24244953), [concept DOI](https://doi.org/10.5281/zenodo.24244952). All 54 archive files and the release PDF match the frozen tag. The DOI-bearing metadata and public receipt were added after release and are not claimed to be inside the immutable archive. Lean certification is separate and is not claimed.

Original archive materials are licensed under [CC BY 4.0](LICENSE). Cited third-party works retain their own licenses. OpenAI Codex assisted derivation, literature comparison, drafting and internal checking. No independent peer review or formal certification is claimed.
