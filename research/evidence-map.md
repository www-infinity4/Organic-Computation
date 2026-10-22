# Evidence map: DARPA research versus our software experiments

**Checked:** 2026-10-22. This document separates agency program goals from demonstrable results. A DARPA solicitation is not evidence that the goals have been achieved.

| Source | What it supports | What it does **not** establish |
| --- | --- | --- |
| [DARPA O-Circuit program](https://www.darpa.mil/events/2026/o-circuit-proposers-day) | DARPA is exploring neural-tissue-driven biological processing units with learning/inference and low-power ambitions | That a practical general-purpose organic computer exists, or that our simulator measures tissue |
| [O-Circuit solicitation DARPA-PS-26-28, May 1, 2026](https://sam.gov/opp/6d28dbf9da1f4fe09c58d5ad7896fe9c/view) | Program aims to improve learning, inference and computational memory; solicitation describes existing capability limits | Successful final demonstrations or verified energy performance |
| [O-Circuit prior notice DARPA-SN-26-48, March 3, 2026](https://sam.gov/opp/f8fd222be5f046b887fb4759b2d7d123/view) | Early program announcement and research objectives | Results from an awarded performer |
| [DARPA Molecular Informatics](https://www.darpa.mil/research/programs/molecular-informatics) | DARPA explored encoding/processing information with molecules; this program is completed | That a molecular device has replaced silicon or works like neural tissue |
| [DARPA Living Foundries](https://www.darpa.mil/research/programs/living-foundries) | Programmable biomanufacturing research | Direct evidence about neural-computation performance |

## Digital experiment: paired baseline comparison

Code: [`simulations/benchmark.py`](../simulations/benchmark.py). All three methods receive the *same* corrupted test examples: a fixed-weight Hopfield-like recall function; the nearest stored-template comparator; and an identity/no-correction baseline.

The fixed dataset has **two six-bit prototype patterns**, so successful retrieval from those same known patterns is **not** evidence of general intelligence or a biological learning mechanism. Nearest-template is permitted to store those prototypes, matching the experiment's training information. Randomness uses a fixed seed and is deterministic on Python 3.12.

The script reports exact counts, accuracy and approximate Wilson 95% intervals for each noise level. Compare algorithms using identical trials and show counterexamples where a simpler comparator performs better. Do not infer electrical wattage, organoid efficiency, consciousness, or DARPA performance outcomes from CPU instruction counts.

### Repeat the experiment

```sh
python3 -m unittest discover -s tests -v
python3 -m simulations.benchmark --seed 111 --trials 250 --noise 0 1 2 3
```

`--trials` is bounded to 1–10,000. `--noise` contains distinct integers 0–6. Output is JSON suitable for an **authorized, read-only** Bubbles research card. The CLI does not contact any external service or require an account.

## Separate speculative track

The user's proposed hydrogen/electron-position and resonance/time-link ideas remain hypotheses. They are **not** DARPA findings. Before representing a mechanism as tested, specify measurable physical variables and units, a control, reproducible observations, and a falsifier. No physical or time-travel demonstration is present in this repository.
