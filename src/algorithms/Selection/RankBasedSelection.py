from src.algorithms.Selection.SelectionStrategy import SelectionStrategy

import numpy as np


class RankBasedSelection(SelectionStrategy):
    def select(self, population: np.ndarray, quality_function_values: np.ndarray) -> np.ndarray:
        pass
