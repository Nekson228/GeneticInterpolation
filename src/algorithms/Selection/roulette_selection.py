from src.algorithms.Selection.selection_strategy import SelectionStrategy

import numpy as np


class RouletteSelection(SelectionStrategy):
    def select(self, population: np.ndarray, quality_function_values: np.ndarray) -> np.ndarray:
        if len(population) != len(quality_function_values):
            raise ValueError("Population and quality function values must have the same length.")

        invert_quality_val = 1 / quality_function_values
        probabilities = invert_quality_val / invert_quality_val.sum()
        selected_indices = np.random.choice(len(quality_function_values), size=2, p=probabilities, replace=False)
        return population[selected_indices]
