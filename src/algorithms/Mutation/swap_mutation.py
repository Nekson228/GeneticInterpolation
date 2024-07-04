from src.algorithms.Mutation.mutation_strategy import MutationStrategy

import numpy as np


class SwapMutation(MutationStrategy):
    def mutate(self, individual: np.ndarray, search_space: tuple[float, float]) -> np.ndarray:
        indices = np.arange(len(individual))
        id1 = np.random.choice(indices)
        id2 = np.random.choice(np.delete(indices, id1))
        individual[[id1, id2]] = individual[[id2, id1]]
        return individual
