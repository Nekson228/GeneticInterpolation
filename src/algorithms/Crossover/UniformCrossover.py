from src.algorithms.Crossover.CrossoverStrategy import CrossoverStrategy

import numpy as np
from typing import Tuple


class UniformCrossover(CrossoverStrategy):
    def crossover(self, parent1: np.ndarray, parent2: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        size = len(parent1)
        offspring1 = np.zeros(size)
        offspring2 = np.zeros(size)
        for i in range(size):
            p = np.random.uniform()
            offspring1[i] = parent1[i] if p < 0.5 else parent2[i]
            offspring2[i] = parent2[i] if p < 0.5 else parent1[i]

        return offspring1, offspring2
