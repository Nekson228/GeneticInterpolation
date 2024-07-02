import numpy as np
import numpy.polynomial as np_poly

from src.data_structures.settings_data import SettingsData

from src.algorithms.Crossover.crossover_strategy import CrossoverStrategy
from src.algorithms.Selection.selection_strategy import SelectionStrategy
from src.algorithms.Mutation.mutation_strategy import MutationStrategy

from src.algorithms.step_function import StepFunction


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

        self.points_per_step = GeneticAlgorithm.NUMBER_OF_POINTS // self.chromosome_length

        self.current_population = np.random.uniform(search_space[0], search_space[1],
                                                    size=(population_size, self.chromosome_length))
        self.current_quality_function_values = self.quality_function_vectorized(self.current_population)

        self.max_iterations = max_iterations
        self.current_iteration = 0

        self.best_quality_function_values: np.ndarray = np.zeros(max_iterations, dtype=float)
        self.best_quality_function_values[0] = self.current_quality_function_values.min()

        self.crossover_strategy = crossover_strategy
        self.mutation_strategy = mutation_strategy
        self.selection_strategy = selection_strategy

    def quality_function_vectorized(self, population: np.ndarray) -> np.ndarray:
        """
        Calculate quality function values for the entire population.

        :param population: 2D-array where each row is an individual.
        :return: 1D array of quality function values for each individual.
        """
        # TODO: Move this to a separate class.
        # TODO: optimize this function.
        quality_values = np.zeros(self.population_size, dtype=float)
        for idx, individual in enumerate(population):
            step_function = StepFunction(self.chromosome_length, self.left_bound, self.right_bound, individual)
            res = np.zeros(self.chromosome_length)
            for i, (height, (start, stop)) in enumerate(step_function):
                x_points = np.linspace(start, stop, self.points_per_step)
                y_points = self.function(x_points)
                res[i] = np.abs(y_points - height).sum()
            quality_values[idx] = res.sum() / GeneticAlgorithm.NUMBER_OF_POINTS
        return quality_values

    def step(self) -> bool:
        """
        Perform one iteration of the algorithm.
        :return: True if the algorithm should continue, False otherwise.
        """
        self.current_iteration += 1
        if self.current_iteration == self.max_iterations:
            return False

        new_population = []
        while len(new_population) < self.population_size:
            parents = self.selection_strategy.select(self.current_population,
                                                     self.current_quality_function_values)
            offsprings = self.crossover_strategy.crossover(*parents) \
                if np.random.random() < self.crossover_rate else parents
            if np.random.random() < self.mutation_rate:
                offsprings = (self.mutation_strategy.mutate(offsprings[0]),
                              self.mutation_strategy.mutate(offsprings[1]))
            new_population.extend(offsprings)

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


def main():
    from src.algorithms.Crossover.intermediate_recombination import IntermediateRecombination
    from src.algorithms.Mutation.real_valued_mutation import RealValuedMutation
    from src.algorithms.Selection.rank_based_selection import RankBasedSelection
    settings: SettingsData = {
        'steps_amount': 50,
        'f(x)': [1, 0, 0],
        'left_bound': -1,
        'right_bound': 1
    }
    crossover_strategy = IntermediateRecombination()
    mutation_strategy = RealValuedMutation(1)
    selection_strategy = RankBasedSelection()
    genetic_algorithm = GeneticAlgorithm(population_size=10, mutation_rate=0.1, crossover_rate=0.7,
                                         max_iterations=1000, search_space=(0, 1), session_settings=settings,
                                         crossover_strategy=crossover_strategy, mutation_strategy=mutation_strategy,
                                         selection_strategy=selection_strategy)
    genetic_algorithm.run()
    best = genetic_algorithm.get_top_individuals(1)
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 2, sharey=False)
    x = np.linspace(-1, 1, 1000)
    y = np.polyval(settings['f(x)'], x)
    ax[0].plot(x, y)
    step_function = StepFunction(settings['steps_amount'], settings['left_bound'], settings['right_bound'], best[0])
    for height, (start, stop) in step_function:
        x = np.linspace(start, stop, 100)
        y = np.polyval(settings['f(x)'], x)
        ax[0].plot(x, np.full_like(x, height), 'r')
        ax[1].plot(x, y)
    ax[1].plot(genetic_algorithm.get_best_quality_function_values())
    plt.show()


if __name__ == '__main__':
    main()
