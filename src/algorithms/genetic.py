import numpy as np
import numpy.polynomial as np_poly

from src.data_structures.settings_data import SettingsData

from src.algorithms.Crossover.CrossoverStrategy import CrossoverStrategy
from src.algorithms.Selection.SelectionStrategy import SelectionStrategy
from src.algorithms.Mutation.MutationStrategy import MutationStrategy

from src.algorithms.StepFunction import StepFunction


class GeneticAlgorithm:
    NUMBER_OF_POINTS = 10_000

    def __init__(self, population_size: int, mutation_rate: float, crossover_rate: float,
                 max_iterations: int, search_space: tuple[float, float],
                 session_settings: SettingsData,
                 crossover_strategy: CrossoverStrategy, mutation_strategy: MutationStrategy,
                 selection_strategy: SelectionStrategy):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate

        self.chromosome_length = session_settings['steps_amount']
        self.function = np_poly.Polynomial(session_settings['f(x)'][::-1])
        self.left_bound = session_settings['left_bound']
        self.right_bound = session_settings['right_bound']

        self.current_population = np.random.uniform(search_space[0], search_space[1],
                                                    size=(population_size, self.chromosome_length))
        self.current_quality_function_values = self.quality_function_vectorized(self.current_population)

        self.max_iterations = max_iterations
        self.current_iteration = 0

        self.best_quality_function_values: np.ndarray = np.zeros(max_iterations, dtype=float)

        self.crossover_strategy = crossover_strategy
        self.mutation_strategy = mutation_strategy
        self.selection_strategy = selection_strategy

        self.points_per_step = GeneticAlgorithm.NUMBER_OF_POINTS // self.chromosome_length

    def quality_function_vectorized(self, population: np.ndarray) -> np.ndarray:
        """
        Calculate quality function values for the entire population.

        :param population: 2D-array where each row is an individual.
        :return: 1D array of quality function values for each individual.
        """
        step_function = StepFunction(self.chromosome_length, self.left_bound, self.right_bound, population)

        heights, starts, stops = np.array([[height, start, stop] for height, start, stop in step_function]).T

        x_points = np.linspace(starts, stops, self.points_per_step)
        y_points = self.function(x_points)

        dist = np.abs(y_points.T - heights)
        return dist.sum(axis=1) / GeneticAlgorithm.NUMBER_OF_POINTS

    def step(self) -> bool:
        """
        Perform one iteration of the algorithm.
        :return: True if the algorithm should continue, False otherwise.
        """
        if self.current_iteration == self.max_iterations:
            return False
        self.current_iteration += 1

        new_population = []
        while len(new_population) < self.population_size:
            parents = self.selection_strategy.select(self.current_population,
                                                     self.current_quality_function_values)
            offsprings = self.crossover_strategy.crossover(*parents)
            mutations = (self.mutation_strategy.mutate(offsprings[0]),
                         self.mutation_strategy.mutate(offsprings[1]))
            new_population.extend(mutations)

        if len(new_population) > self.population_size:
            new_population = new_population[:self.population_size]

        self.current_population = np.array(new_population)
        self.current_quality_function_values = self.quality_function_vectorized(self.current_population)
        self.best_quality_function_values[self.current_iteration] = self.current_quality_function_values.min()

        return True if self.current_iteration != self.max_iterations else False

    def run(self) -> None:
        """
        Run the algorithm until reaching the maximum iteration amount.
        :return:
        """
        while self.current_iteration != self.max_iterations:
            self.step()

    def get_top_individuals(self, n: int) -> np.ndarray:
        """
        Get the best individuals from the current population.
        :param n: individuals amount to return.
        :return: array of the best individuals.
        """
        return self.current_population[self.current_quality_function_values.argsort()[:n]]

    def get_best_quality_function_values(self) -> np.ndarray:
        """
        Get the best quality function values from the current population.
        :return: array of the best quality function values.
        """
        return self.best_quality_function_values[:self.current_iteration]
