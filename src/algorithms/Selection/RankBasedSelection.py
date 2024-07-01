from src.algorithms.Selection.SelectionStrategy import SelectionStrategy

import numpy as np


class RankBasedSelection(SelectionStrategy):
    def select(self, population: np.ndarray, quality_function_values: np.ndarray) -> np.ndarray:
        ranks = np.argsort(quality_function_values)[::-1]
        selection_probs = ranks / np.sum(ranks)
        selection_id = np.random.choice(np.arange(len(population)), size=2, p=selection_probs, replace=False)

        return population[selection_id]



