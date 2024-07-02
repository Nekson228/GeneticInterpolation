from src.algorithms.Crossover.crossover_strategy import CrossoverStrategy

import numpy as np


class UniformCrossover(CrossoverStrategy):
    def crossover(self, parent1: np.ndarray, parent2: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        mask = np.random.uniform(size=parent1.shape) < 0.5
        offspring1 = np.where(mask, parent1, parent2)
        offspring2 = np.where(mask, parent2, parent1)
        return offspring1, offspring2
