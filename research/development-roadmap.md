# Organic Computation Phi — research and development roadmap

**Created:** October 22, 2026  
**Focus:** software simulations informed by DARPA O-Circuit research, not wet-lab procedures or a claim of an operational biological processor.

## What DARPA is actually studying

O-Circuit (Organoid Cytomorphic Intelligence Resulting from Convergent Understanding and Information Transfer) explores biological processing units using neural tissue for learning, inference, computational memory, and lower-power sense-compute-act behavior. These are proposed research capabilities. The May 1, 2026 solicitation describes project goals, not evidence that this repository's Python model behaves like living brain tissue.

Primary references: [DARPA program](https://www.darpa.mil/events/2026/o-circuit-proposers-day), [DARPA-PS-26-28](https://sam.gov/opp/6d28dbf9da1f4fe09c58d5ad7896fe9c/view), and [DARPA-SN-26-48](https://sam.gov/opp/f8fd222be5f046b887fb4759b2d7d123/view).

Molecular Informatics and Living Foundries are related DARPA programs, but neither is interchangeable with O-Circuit.

## Stage 1: Baseline reproducibility

Run the included associative-memory experiment and repeat with the same random seed. Record training patterns, flips per input, number of trials, accuracy and expected failure cases. The current simulator is a toy recurrent model. Compare with a no-learning or nearest-pattern baseline on precisely the same inputs.

## Stage 2: Learning and memory

Add a bounded plasticity model and a non-learning control. Quantify:
- acquisition over training examples, including previously unseen patterns
- retention after delays; forgetting and interference across competing memories
- error rates under varying noise levels and across multiple random seeds
- execution time, CPU/RAM overhead and complexity, marked as software metrics

A software process's runtime is not direct evidence for the milliwatt-hour energy usage of a biological processing unit.

## Stage 3: Bubbles / Robot Brain interface

Design a read-only research tool whose result includes `model_type`, `seed`, `task`, `input_source`, `metrics`, `baseline`, `limitations`, and `research_citations`. Do not connect the model to privileged GitHub writes, wallets, an Android device or third-party accounts simply because an experiment passed. Those abilities remain behind existing owner authorization.

## Stage 4: Scientific and theoretical cross-connections

Study the user's hydrogen, electron-position, resonance and temporal concepts as explicitly unverified hypotheses alongside the organic-computation work, not as known mechanisms. Write a prediction, units, instrumentation assumptions, possible confounders and falsifying observations for each before making causal claims.

## Acceptance for future changes

Every model change must have a test and an actual passing CI run. A repository commit is not a validated experiment; a search result is not a paper read; a published program goal is not a measured scientific finding. Keep Bubbles' tool receipts separate from the research conclusions.
