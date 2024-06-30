from abc import ABC, abstractmethod

import numpy as np


class MutationStrategy(ABC):
    @abstractmethod
    def mutate(self, individual: np.ndarray) -> np.ndarray:
        """
        Mutates an individual.
        :param individual: individual for mutation.
        :return: mutated individual.
        """
        pass
