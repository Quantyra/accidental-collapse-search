# P011 v0.3.0: general positive-adversary bounds

This revision adds a second main theorem for arbitrary finite Boolean promise problems in the same independent flagged accidental-collapse model:

`Q min{P+1,ceil(1/epsilon)} >= Adv_+(f)/36`, using P+1 at epsilon=0.

The proof covers immediate feedback, arbitrary entangled workspace, partial measurements, permitted resets and unequal stopping. It sums actual query probabilities across complete histories, avoiding a branch-count factor, and applies fixed and decreasing powers separately. A parity application shows that any fixed positive collapse rate requires Omega(n) input queries. The sharper optimal search law `Theta(N^(1/3)+sqrt(epsilon N))` is retained.

All additional computational resources remain paid. Certificates may be exponentially large analytical objects; no efficient discovery, signed-adversary extension, physical implementation or ordinary BPP/BQP result is claimed. Positive adversary methods and other inherited ingredients are explicitly attributed.

Fresh Claude, Grok and AGY provider CLI reviews and final-source rechecks are archived with their findings and dispositions. No unresolved blocker remains. The fourteen-page PDF, metadata, retained evidence and clean rebuild are checked. AI review is not independent human peer review or formal certification; full Lean certification remains separately queued.

The existing Zenodo integration archives this release as a new version in the same DOI family. The version DOI and exact archive verification will be recorded after publication. Previous v0.1.0 and v0.2.0 remain immutable. Original archive materials: CC BY 4.0. Author: Daniel Fredriksen, Quantyra Inc., ORCID 0009-0002-9123-7435.
