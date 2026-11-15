# Preserved finite diagnostics

These files are unchanged research evidence from the analytic development, not new runs performed during manuscript preparation. `provenance.json` records exact source commits and SHA-256 identities. The first run passed 1,094 exact assertions in 6.921573 seconds; a separately preregistered supplemental run for the stronger power potential passed 374 in 4.457189 seconds. Aggregate recorded time: 11.378762 seconds within the original 120-second cap.

The scripts cover the success recurrence, explicit constants, protected workspace, scalar identities and fixed projector examples. The first includes an earlier valid but weaker signed-score bound; the manuscript uses the stronger power potential. Finite fixtures do not establish the universal theorem and are not independent or formal certification.

To reproduce, copy the two scripts and two preregistration JSON files into a fresh scratch directory with `scripts/` and `artifacts/` subdirectories, preserving their filenames. Install SymPy 1.14.0 in a separate Python environment. Run `scripts/s261_exact_diagnostic.py`, then `scripts/s261_power_potential_diagnostic.py`. Each script refuses to overwrite an existing receipt, and the second reads the first receipt and charges its runtime. Do not copy the original result JSON files into that scratch `artifacts/` directory. These are historical bounded diagnostics, not a benchmark or a parameter sweep. A reproduction must preserve any failure and must not overwrite the original evidence here.

Original records use UTC timestamps; manuscript date is November 14, 2026 Hawaii. Third-party full texts, private planning and unrelated technical history are not included.
