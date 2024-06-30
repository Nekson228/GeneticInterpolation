from abc import ABC, abstractmethod

import numpy as np


class SelectionStrategy(ABC):
    @abstractmethod
    def select(self, population: np.ndarray, quality_function_values: np.ndarray) -> np.ndarray:
        """
        Selects individuals from the population based on their quality function values.
        :param population: array of individuals.
        :param quality_function_values: array of quality function values.
        :return: selected individuals.
        """
        pass
