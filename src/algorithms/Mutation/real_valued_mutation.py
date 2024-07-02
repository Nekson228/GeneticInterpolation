from src.algorithms.Mutation.mutation_strategy import MutationStrategy

import numpy as np


class RealValuedMutation(MutationStrategy):
    def __init__(self, search_space: float, m: int = 20):
        self._search_space = search_space
        self._m = m

    def _calculate_delta(self, size: int) -> float:
        a = np.array(np.random.rand(size, self._m) < 1 / self._m, dtype=float)
        delta = np.sum(a * (2. ** (-np.arange(1, self._m + 1))),
                       axis=1)
        return delta

    def mutate(self, individual: np.ndarray) -> np.ndarray:
        alpha = 0.5 * self._search_space
        delta = self._calculate_delta(len(individual))
        sign = np.random.choice([-1, 1], size=len(individual))
        mutated_individual = individual + sign * alpha * delta
        return mutated_individual
