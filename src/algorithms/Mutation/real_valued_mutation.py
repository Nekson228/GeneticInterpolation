from src.algorithms.Mutation.mutation_strategy import MutationStrategy

import numpy as np


class RealValuedMutation(MutationStrategy):
    def __init__(self, m: int = 20):
        self._m = m

    def _calculate_delta(self, size: int) -> float:
        a = np.array(np.random.rand(size, self._m) < 1 / self._m, dtype=float)
        delta = np.sum(a * (2. ** (-np.arange(1, self._m + 1))),
                       axis=1)
        return delta

    def mutate(self, individual: np.ndarray, search_space: tuple[float, float]) -> np.ndarray:
        alpha = 0.5 * (search_space[1] - search_space[0])
        delta = self._calculate_delta(len(individual))
        sign = np.random.choice([-1, 1], size=len(individual))
        mutated_individual = individual + sign * alpha * delta
        return mutated_individual
