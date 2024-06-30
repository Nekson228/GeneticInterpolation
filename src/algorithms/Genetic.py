import numpy as np
import numpy.polynomial as np_poly

from src.data_structures.SettingsData import SettingsData

from src.algorithms.Crossover.CrossoverStrategy import CrossoverStrategy
from src.algorithms.Selection.SelectionStrategy import SelectionStrategy
from src.algorithms.Mutation.MutationStrategy import MutationStrategy


class GeneticAlgorithm:
    def __init__(self, population_size: int, mutation_rate: float, crossover_rate: float,
                 max_iterations: int, session_settings: SettingsData,
                 crossover_strategy: CrossoverStrategy, mutation_strategy: MutationStrategy,
                 selection_strategy: SelectionStrategy):
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
        pass

    def step(self) -> None:
        """
        Perform one iteration of the algorithm.
        :return: None
        """
        pass

    def run(self) -> None:
        """
        Run the algorithm until reaching the maximum iteration amount.
        :return:
        """
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

