from abc import ABC, abstractmethod

import numpy as np
from typing import Tuple


class CrossoverStrategy(ABC):
    @abstractmethod
    def crossover(self, parent1: np.ndarray, parent2: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Combines two parents to create a child.
        :param parent1: first parent.
        :param parent2: second parent.
        :return: 2 child.
        """
        pass
