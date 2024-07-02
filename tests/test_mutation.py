from src.algorithms.Mutation.real_valued_mutation import RealValuedMutation

import numpy as np


def test_mutate():
    individual = np.array([1, 2, 3], dtype=float)
    mutation = RealValuedMutation(0.5)
    mutated = mutation.mutate(individual)
    assert mutated.shape == (3,)
    assert mutated.dtype == float
    assert np.all(np.abs(mutated - individual) <= 0.5)
