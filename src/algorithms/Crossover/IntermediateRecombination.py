from src.algorithms.Crossover.CrossoverStrategy import CrossoverStrategy

import numpy as np


class IntermediateRecombination(CrossoverStrategy):
    def __init__(self, d: float = 0.25):
        """
        :param d: non-negative parameter for intermediate recombination (0.25 preferred).
        """
        self._d = d

    def _generate_alpha(self) -> float:
        return np.random.uniform(-self._d, 1 + self._d)

    def crossover(self, parent1: np.ndarray, parent2: np.ndarray) -> np.ndarray:
        pass
