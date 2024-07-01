from src.algorithms.Mutation.MutationStrategy import MutationStrategy

import numpy as np


class RealNumberMutation(MutationStrategy):
    def calculate_delta(m: int) -> float:
        delta = 0
        for i in range(1, m + 1):
            a_i = 1 if np.random.rand() < 1 / m else 0
            delta += a_i * 2 ** (-i)

        return delta

    def mutate(self, individual: np.ndarray) -> np.ndarray:
        search_space = 10 # what is value????
        m = 20
        alpha = 0.5 * search_space
        mutated_individual = individual.copy()

        for i in range(len(mutated_individual)):
            delta = calculate_delta(m)
            sign = 1 if np.random.rand() < 0.5 else -1
            mutated_individual[i] += sign * alpha * delta

        return mutated_individual
