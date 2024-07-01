import numpy as np
import numpy.polynomial as np_poly
from typing import Callable

from src.data_structures.SettingsData import SettingsData

from src.algorithms.Crossover.CrossoverStrategy import CrossoverStrategy
from src.algorithms.Selection.SelectionStrategy import SelectionStrategy
from src.algorithms.Mutation.MutationStrategy import MutationStrategy


class GeneticAlgorithm:
    def __init__(self, population_size: int, mutation_rate: float, crossover_rate: float,
                 max_iterations: int, session_settings: SettingsData,
                 crossover_strategy: Callable, mutation_strategy: Callable,
                 selection_strategy: Callable):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate

        self.chromosome_length = session_settings['steps_amount']
        self.function = np_poly.Polynomial(session_settings['f(x)'][::-1])
        self.left_bound = session_settings['left_bound']
        self.right_bound = session_settings['right_bound']

        self.current_population = None  # TODO: Implement population initialization

        self.max_iterations = max_iterations
        self.current_iteration = 0

        self.best_quality_function_values: np.ndarray = np.zeros(max_iterations, dtype=float)

        self.crossover_strategy = crossover_strategy
        self.mutation_strategy = mutation_strategy
        self.selection_strategy = selection_strategy

        # add another fields if needed

    def quality_function(self, individual: np.ndarray) -> float:
        """
        Calculate quality function value for the individual.
        :param individual: individual to calculate quality function value for.
        :return: quality function value.
        """
        res = []
        lst = np.linspace(self.left_bound, self.right_bound, self.chromosome_lenght)
        for i in range(len(lst) - 1):
            x_points = np.linspace(lst[i], lst[i + 1], 1000)
            y_points = np.polyval(self.function[::-1], x_points)
            dist = np.mean(abs(y_points - individual[i]))
            res.append(dist)
        return np.mean(res)

    def step(self) -> None:
        """
        Perform one iteration of the algorithm.
        :return: None
        """
        new_population = [] #what
        while(len(new_population) != self.population_size):
            parents = self.selection_strategy(self.current_population)
            offspings = self.crossover_strategy(parents)
            mutations = tuple((self.mutation_rate(offspings[0]), self.mutation_rate(offspings[1])))
            new_population.append(mutations[0])
            new_population.append(mutations[1])
        self.current_population = new_population
        pass

    def run(self) -> None:
        """
        Run the algorithm until reaching the maximum iteration amount.
        :return:
        """
        while(self.current_iteration != self.max_iterations):
            self.step()
        pass

    def get_top_individuals(self, n: int) -> np.ndarray:
        """
        Get the best individuals from the current population.
        :param n: individuals amount to return.
        :return: array of the best individuals.
        """
        pass

    def get_best_individual(self) -> np.ndarray:
        """
        Get the best individual from the current population.
        :return: the best individual.
        """
        pass

    def get_best_quality_function_value(self) -> float:
        """
        Get the best quality function value from the current population.
        :return: the best quality function value.
        """
        pass

    def get_best_quality_function_values(self) -> np.ndarray:
        """
        Get the best quality function values from the current population.
        :return: array of the best quality function values.
        """
        pass

