from abc import ABC, abstractmethod

import numpy as np


class QualityFunction(ABC):
    def __init__(self, left_bound: float, right_bound: float, function: np.polynomial.Polynomial,
                 chromosome_length: int):
        self._left_bound = left_bound
        self._right_bound = right_bound
        self._function = function
        self._chromosome_length = chromosome_length

    @abstractmethod
    def calculate(self, population: np.ndarray) -> np.ndarray:
        """
        Calculate quality function values for the entire population.
        :param population: 2D-array where each row is an individual.
        :return: 1D array of quality function values for every individual.
        """
        pass
