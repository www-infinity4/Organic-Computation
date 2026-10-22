"""Simple software-only associative memory. No biological materials or external packages."""
from __future__ import annotations
import random

PATTERNS = ((1, 1, -1, -1, 1, -1), (-1, 1, -1, 1, -1, 1))

def train(patterns=PATTERNS):
    size = len(patterns[0])
    if not patterns or any(len(p) != size or any(v not in (-1, 1) for v in p) for p in patterns):
        raise ValueError("Binary, equally sized patterns required")
    return [[0 if i == j else sum(p[i] * p[j] for p in patterns)
             for j in range(size)] for i in range(size)]

def recall(state, weights, rounds=12):
    state = list(state)
    for _ in range(rounds):
        previous = state[:]
        for i, row in enumerate(weights):
            score = sum(w * x for w, x in zip(row, state))
            if score != 0:
                state[i] = 1 if score > 0 else -1
        if state == previous:
            break
    return tuple(state)

def experiment(seed=111, flips=1, trials=100):
    rng = random.Random(seed)
    weights = train()
    success = 0
    for _ in range(trials):
        target = rng.choice(PATTERNS)
        state = list(target)
        for index in rng.sample(range(len(state)), flips):
            state[index] *= -1
        success += recall(state, weights) == target
    return success / trials

if __name__ == "__main__":
    for flipped in (0, 1, 2):
        print(f"noise flips={flipped}: recall accuracy={experiment(flips=flipped):.3f}")
