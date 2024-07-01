from src.algorithms.Selection.SelectionStrategy import SelectionStrategy

import numpy as np


class RankBasedSelection(SelectionStrategy):
    def select(self, population: np.ndarray, quality_function_values: np.ndarray) -> np.ndarray:
        if len(population) != len(quality_function_values):
            raise ValueError("Population and quality function values must have the same length.")
        ranks = np.argsort(quality_function_values[::-1]) + 1
        probabilities = np.arange(1, len(ranks) + 1) / ranks.sum()
        selected_indices = np.random.choice(ranks - 1, size=2, p=probabilities, replace=False)
        return population[selected_indices]
