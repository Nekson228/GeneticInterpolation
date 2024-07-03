import numpy as np

from src.algorithms.Genetic.genetic_hyper_initializer import GeneticHyperInitializer
from src.algorithms.Genetic.genetic_session_initializer import GeneticSessionInitializer

from src.algorithms.Quality.QualityFunction import QualityFunction
from src.algorithms.Quality.MeanStepDistance import MeanStepDistance

from src.constants import NUMBER_OF_FUNCTION_POINTS


class GeneticAlgorithm:
    def __init__(self, hyper_initializer: GeneticHyperInitializer, session_initializer: GeneticSessionInitializer):
        self.population_size = hyper_initializer.population_size
        self.mutation_rate = hyper_initializer.mutation_rate
        self.crossover_rate = hyper_initializer.crossover_rate
        self.max_generations = hyper_initializer.max_generations

        self.crossover_strategy = hyper_initializer.crossover_strategy
        self.mutation_strategy = hyper_initializer.mutation_strategy
        self.selection_strategy = hyper_initializer.selection_strategy

        self.chromosome_length = session_initializer.steps_amount
        self.function = session_initializer.function
        self.left_bound = session_initializer.left_bound
        self.right_bound = session_initializer.right_bound
        self.search_range = session_initializer.search_space

        self.quality_function: QualityFunction = MeanStepDistance(self.left_bound, self.right_bound,
                                                                  self.function, self.chromosome_length)

        self.current_generation = 0

        self.points_per_step = NUMBER_OF_FUNCTION_POINTS // self.chromosome_length

        self.current_population = np.random.uniform(self.search_range[0], self.search_range[1],
                                                    size=(self.population_size, self.chromosome_length))
        self.current_quality_function_values = self.quality_function.calculate(self.current_population)

        self.best_quality_function_values: np.ndarray = np.zeros(self.max_generations, dtype=float)
        self.best_quality_function_values[0] = self.current_quality_function_values.min()

    def step(self) -> bool:
        """
        Perform one iteration of the algorithm.
        :return: True if the algorithm should continue, False otherwise.
        """
        self.current_generation += 1
        if self.current_generation == self.max_generations:
            return False

        new_population = []
        while len(new_population) < self.population_size:
            parents = self.selection_strategy.select(self.current_population,
                                                     self.current_quality_function_values)
            offsprings = self.crossover_strategy.crossover(*parents) \
                if np.random.random() < self.crossover_rate else parents
            if np.random.random() < self.mutation_rate:
                offsprings = (self.mutation_strategy.mutate(offsprings[0], self.search_range),
                              self.mutation_strategy.mutate(offsprings[1], self.search_range))
            new_population.extend(offsprings)

        if len(new_population) > self.population_size:
            new_population = new_population[:self.population_size]

        self.current_population = np.array(new_population)
        self.current_quality_function_values = self.quality_function.calculate(self.current_population)
        self.best_quality_function_values[self.current_generation] = self.current_quality_function_values.min()

        return True if self.current_generation != self.max_generations else False

    def run(self) -> None:
        """
        Run the algorithm until reaching the maximum iteration amount.
        :return:
        """
        while self.current_generation != self.max_generations:
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
        return self.best_quality_function_values[:self.current_generation]
