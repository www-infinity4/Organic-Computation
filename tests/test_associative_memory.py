import unittest
from simulations.associative_memory import PATTERNS, train, recall, experiment

class SimulationTests(unittest.TestCase):
    def test_diagonal_zero(self):
        weights = train()
        self.assertTrue(all(weights[i][i] == 0 for i in range(len(weights))))
    def test_patterns_stable(self):
        weights = train()
        for pattern in PATTERNS:
            self.assertEqual(recall(pattern, weights), pattern)
    def test_reproducible(self):
        self.assertEqual(experiment(seed=22), experiment(seed=22))
    def test_accuracy_range(self):
        self.assertGreaterEqual(experiment(), 0)
        self.assertLessEqual(experiment(), 1)

if __name__ == "__main__":
    unittest.main()
