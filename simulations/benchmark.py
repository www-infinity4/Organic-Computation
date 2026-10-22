"""Reproducible software-only associative-memory benchmark (not an organoid)."""
from __future__ import annotations
import argparse
import json
import math
import random
from simulations.associative_memory import PATTERNS, recall, train

SCHEMA_VERSION = 1
METHODS = ("hopfield", "nearest_template", "identity")

def hamming(a: tuple[int, ...], b: tuple[int, ...]) -> int:
    if len(a) != len(b):
        raise ValueError("Different pattern lengths")
    return sum(x != y for x, y in zip(a, b))

def nearest_template(state: tuple[int, ...],
                     patterns: tuple[tuple[int, ...], ...] = PATTERNS) -> tuple[int, ...]:
    """Stored-prototype comparator; earliest prototype wins a distance tie."""
    if not patterns:
        raise ValueError("At least one template required")
    return min(patterns, key=lambda p: hamming(state, p))

def wilson_interval(successes: int, trials: int, z: float = 1.96) -> tuple[float, float]:
    """Approximate 95% binomial interval for this artificial task only."""
    if trials < 1 or not 0 <= successes <= trials:
        raise ValueError("Invalid binomial counts")
    p = successes / trials
    d = 1 + z * z / trials
    center = (p + z * z / (2 * trials)) / d
    half = z / d * math.sqrt(p * (1 - p) / trials + z * z / (4 * trials * trials))
    return (0.0 if successes == 0 else max(0.0, center - half),
            1.0 if successes == trials else min(1.0, center + half))

def run_benchmark(seed: int = 111, trials: int = 250,
                  noise_levels: tuple[int, ...] = (0, 1, 2, 3)) -> dict:
    """Identical generated inputs for each method; pure Python and deterministic."""
    if type(seed) is not int or not 0 <= seed <= 2**32 - 1:
        raise ValueError("Seed must be a 32-bit unsigned integer")
    if type(trials) is not int or not 1 <= trials <= 10000:
        raise ValueError("Trials must be an integer between 1 and 10000")
    if not noise_levels or len(set(noise_levels)) != len(noise_levels):
        raise ValueError("Noise levels must be unique and nonempty")
    if any(type(level) is not int or level < 0 or level > len(PATTERNS[0]) for level in noise_levels):
        raise ValueError("Invalid noise level")
    weights = train(PATTERNS)
    rng = random.Random(seed)
    rows = []
    for flips in noise_levels:
        counts = dict.fromkeys(METHODS, 0)
        for _ in range(trials):
            target = rng.choice(PATTERNS)
            corrupted = list(target)
            for pos in rng.sample(range(len(target)), flips):
                corrupted[pos] = -corrupted[pos]
            observed = tuple(corrupted)
            predicted = {
                "hopfield": recall(observed, weights),
                "nearest_template": nearest_template(observed),
                "identity": observed,
            }
            for method, prediction in predicted.items():
                counts[method] += prediction == target
        results = {}
        for method, successes in counts.items():
            low, high = wilson_interval(successes, trials)
            results[method] = {
                "correct": successes, "total": trials,
                "accuracy": round(successes / trials, 6),
                "wilson95": [round(low, 6), round(high, 6)],
            }
        rows.append({"flipped_bits": flips, "results": results})
    return {
        "schema_version": SCHEMA_VERSION,
        "model_type": "toy_binary_associative_memory",
        "task": "recall_original_pattern_after_bit_flips",
        "seed": seed,
        "trials_per_noise_level": trials,
        "pattern_count": len(PATTERNS),
        "pattern_length_bits": len(PATTERNS[0]),
        "methods": list(METHODS),
        "metrics": rows,
        "baseline": "identity retains corrupted bits; nearest_template stores the same patterns",
        "limitations": [
            "Fully digital toy model, not neural tissue, an organoid, or general intelligence",
            "Training and evaluation reuse two fixed prototypes; no out-of-distribution validation",
            "Wilson intervals describe sampling uncertainty on this artificial task only",
            "No biological energy or hardware efficiency measurements",
        ],
        "research_citations": [
            "https://www.darpa.mil/events/2026/o-circuit-proposers-day",
            "https://sam.gov/opp/6d28dbf9da1f4fe09c58d5ad7896fe9c/view",
        ],
    }

def main() -> None:
    parser = argparse.ArgumentParser(description="Digital-only associative-memory benchmark")
    parser.add_argument("--seed", type=int, default=111)
    parser.add_argument("--trials", type=int, default=250)
    parser.add_argument("--noise", type=int, nargs="+", default=[0, 1, 2, 3])
    args = parser.parse_args()
    try:
        result = run_benchmark(args.seed, args.trials, tuple(args.noise))
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
