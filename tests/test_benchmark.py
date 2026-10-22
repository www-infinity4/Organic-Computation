import json
import subprocess
import sys
import unittest

from simulations.associative_memory import PATTERNS, train, recall
from simulations.benchmark import hamming, nearest_template, run_benchmark, wilson_interval

class BenchmarkTests(unittest.TestCase):
    def test_repeatable_and_no_fake_energy(self):
        a = run_benchmark(seed=111, trials=120, noise_levels=(0, 1, 3))
        self.assertEqual(a, run_benchmark(seed=111, trials=120, noise_levels=(0, 1, 3)))
        self.assertEqual(a["model_type"], "toy_binary_associative_memory")
        self.assertNotIn("energy_mwh", a)
        self.assertEqual(len(a["metrics"]), 3)

    def test_zero_noise(self):
        result = run_benchmark(trials=90, noise_levels=(0,))
        for row in result["metrics"][0]["results"].values():
            self.assertEqual(row["correct"], 90)
            self.assertEqual(row["accuracy"], 1.0)

    def test_identity_fails_after_flips(self):
        result = run_benchmark(trials=50, noise_levels=(1, 2, 3))
        self.assertTrue(all(x["results"]["identity"]["correct"] == 0 for x in result["metrics"]))

    def test_nearest_tie_is_deterministic(self):
        templates = ((1, 1), (1, -1))
        self.assertEqual(nearest_template((-1, 1), templates), templates[0])
        self.assertEqual(hamming((1, 1), (-1, 1)), 1)

    def test_ranges_and_ci(self):
        self.assertEqual(wilson_interval(100, 100)[1], 1.0)
        self.assertLess(wilson_interval(0, 100)[1], 0.05)
        for n in (-1, True, 10001):
            with self.assertRaises(ValueError):
                run_benchmark(trials=n)
        for levels in ((), (1, 1), (7,), (-1,)):
            with self.assertRaises(ValueError):
                run_benchmark(noise_levels=levels)

    def test_training_patterns(self):
        self.assertEqual(len(train()), len(PATTERNS[0]))
        for p in PATTERNS:
            self.assertEqual(recall(p, train()), p)

    def test_cli_json_contract(self):
        result = subprocess.run([sys.executable, "-m", "simulations.benchmark", "--seed", "22",
                                 "--trials", "20", "--noise", "0", "1"],
                                capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        self.assertEqual(data["seed"], 22)
        self.assertEqual([x["flipped_bits"] for x in data["metrics"]], [0, 1])

if __name__ == "__main__":
    unittest.main()
