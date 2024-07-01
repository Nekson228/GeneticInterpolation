from src.algorithms.Mutation.RealNumberMutation import RealNumberMutation

import numpy as np


def test_mutate():
    individual = np.array([1, 2, 3], dtype=float)
    mutation = RealNumberMutation(0.5)
    mutated = mutation.mutate(individual)
    assert mutated.shape == (3,)
    assert mutated.dtype == float
    assert np.all(np.abs(mutated - individual) <= 0.5)
