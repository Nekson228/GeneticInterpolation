from src.algorithms.Mutation.mutation_strategy import MutationStrategy

import numpy as np


class SwapMutation(MutationStrategy):
    def __init__(self, p: 0.1):
        self._p = p

    def mutate(self, individual: np.ndarray, search_space: tuple[float, float]) -> np.ndarray:
        if np.random.rand() < self._p:
            indices = np.arange(len(individual))
            id1 = np.random.choice(indices)
            id2 = np.random.choice(indices, replace=False)
            individual[[id1, id2]] = individual[[id2, id1]]
        return individual
