from src.algorithms.Crossover.CrossoverStrategy import CrossoverStrategy

import numpy as np
from typing import Tuple


class IntermediateRecombination(CrossoverStrategy):
    def __init__(self, d: float = 0.25):
        """
        :param d: non-negative parameter for intermediate recombination (0.25 preferred).
        """
        self._d = d

    def _generate_alpha(self) -> float:
        return np.random.uniform(-self._d, 1 + self._d)

    def crossover(self, parent1: np.ndarray, parent2: np.ndarray) -> Turple[np.ndarray, np.ndarray]:
        size = len(parent1)
        offspring1 = np.zeros(size)
        offspring2 = np.zeros(size)
        for i in range(size):
            alpha1 = self._generate_alpha()
            alpha2 = self._generate_alpha()
            offspring1[i] = parent1[i] + alpha1 * (parent2[i] - parent1[i])
            offspring2[i] = parent1[i] + alpha2 * (parent2[i] - parent1[i])

        return offspring1, offspring2

