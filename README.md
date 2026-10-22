# Organic Computation

A research and software-simulation project prepared through the Bubbles AI signed research-and-build pipeline. The repository studies neural-tissue computing, molecular information processing, energy measurement, and ethical issues — not a working biological processor.

## Scientific anchor
- DARPA's **O-Circuit** (2026) explores neural-tissue-driven biological processing units for low-energy learning and inference. This is a research **goal**, not proof of a practical replacement for silicon. [DARPA O-Circuit](https://www.darpa.mil/events/2026/o-circuit-proposers-day)
- DARPA's completed **Molecular Informatics** program studied molecular approaches to encode and process information. [Program page](https://www.darpa.mil/research/programs/molecular-informatics)
- DARPA **Living Foundries** studies programmable metabolic processes for biomanufacturing, a related but distinct field. [Program page](https://www.darpa.mil/research/programs/living-foundries)

## Workstreams
1. Literature and evidence: distinguish results, plans, proposals, and simulations.
2. Software-only experiments: associative memory and noisy inputs with standard Python.
3. Measurement model: learning accuracy, repeatability, response latency, and total system energy including support equipment.
4. Ethics: donor consent, biological safety, oversight and uncertainty about sentience.
5. Theories: a separate, clearly speculative track for user-proposed hydrogen/electron/energy connections, with explicit falsifiable predictions and tests.

## Run

```sh
python3 -m unittest discover -s tests -v
python3 simulations/associative_memory.py
python3 -m simulations.benchmark --seed 111 --trials 250 --noise 0 1 2 3
```

**Benchmark upgrade:** the new command returns JSON accuracy, counts and confidence intervals for a fixed Hopfield-style associative-memory model and two baselines (stored nearest-template and unchanged noisy input). The same examples are evaluated by every method. A simpler method can outperform the neural-inspired model; this is a scientific comparison, not proof of biological efficiency.

Read [the evidence map](research/evidence-map.md) for which DARPA claims are supported. Bubbles now has a [proposed read-only tool contract](bubbles/README.md); the Python benchmark is tested, but the live Bubbles tool adapter is **not yet deployed**.

Nothing in this repository grows biological tissue, enables drone control, supplies wet-lab protocols, or establishes a commercial product. No DARPA affiliation or funding is claimed.

Start with [research overview](research/overview.md), [Bubbles preliminary notes](research/bubbles-analysis.md), [hypotheses](research/hypotheses.md), and [sources](research/sources.json).
