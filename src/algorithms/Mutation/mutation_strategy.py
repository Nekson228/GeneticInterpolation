from abc import ABC, abstractmethod

import numpy as np


class MutationStrategy(ABC):
    @abstractmethod
    def mutate(self, individual: np.ndarray, search_range: tuple[float, float]) -> np.ndarray:
        """
        Mutates an individual.
        :param individual: individual for mutation.
        :param search_range: range of possible gene values (start, end).
        :return: mutated individual.
        """
        pass
