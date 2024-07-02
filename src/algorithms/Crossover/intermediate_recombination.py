from src.algorithms.Crossover.crossover_strategy import CrossoverStrategy

import numpy as np

class IntermediateRecombination(CrossoverStrategy):
    def __init__(self, d: float = 0.25):
        """
        :param d: non-negative parameter for intermediate recombination (0.25 preferred).
        """
        self._d = d

    def _generate_alpha(self, size: int) -> np.ndarray:
        """
        Generate an array of alpha values.

        :param size: The size of the array to generate.
        :return: An array of alpha values.
        """
        return np.random.uniform(-self._d, 1 + self._d, size)

    def crossover(self, parent1: np.ndarray, parent2: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """
        Perform intermediate recombination crossover.

        :param parent1: The first parent array.
        :param parent2: The second parent array.
        :return: A tuple containing two offspring arrays.
        """
        size = len(parent1)
        alpha = self._generate_alpha(size), self._generate_alpha(size)
        offspring1 = parent1 + alpha[0] * (parent2 - parent1)
        offspring2 = parent1 + alpha[1] * (parent2 - parent1)
        return offspring1, offspring2
