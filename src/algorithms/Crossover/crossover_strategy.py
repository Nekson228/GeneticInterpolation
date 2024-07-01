from abc import ABC, abstractmethod

import numpy as np


class CrossoverStrategy(ABC):
    @abstractmethod
    def crossover(self, parent1: np.ndarray, parent2: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """
        Combines two parents to create two children.
        :param parent1: first parent.
        :param parent2: second parent.
        :return: two children.
        """
        pass
