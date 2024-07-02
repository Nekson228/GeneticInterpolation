from json import load

from src.algorithms.Crossover.crossover_strategy import CrossoverStrategy
from src.algorithms.Crossover.uniform_crossover import UniformCrossover
from src.algorithms.Crossover.intermediate_recombination import IntermediateRecombination

from src.algorithms.Mutation.mutation_strategy import MutationStrategy
from src.algorithms.Mutation.real_valued_mutation import RealValuedMutation

from src.algorithms.Selection.selection_strategy import SelectionStrategy
from src.algorithms.Selection.rank_based_selection import RankBasedSelection

crossover_strategies: dict[str, type[CrossoverStrategy]] = {
    'uniform': UniformCrossover,
    'intermediate': IntermediateRecombination
}

mutation_strategies: dict[str, type[MutationStrategy]] = {
    'real_valued': RealValuedMutation
}

selection_strategies: dict[str, type[SelectionStrategy]] = {
    'rank_based': RankBasedSelection
}


class GeneticHyperInitializer:
    def __init__(self, mutation_rate: float, crossover_rate: float, population_size: int, max_iterations: int,
                 selection_strategy: SelectionStrategy, crossover_strategy: CrossoverStrategy,
                 mutation_strategy: MutationStrategy):
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.population_size = population_size
        self.max_iterations = max_iterations

        self.selection_strategy = selection_strategy
        self.crossover_strategy = crossover_strategy
        self.mutation_strategy = mutation_strategy


    @classmethod
    def from_json(cls, path: str):
        with open(path) as file:
            data = load(file)
        return cls(data['mutation_rate'], data['crossover_rate'], data['population_size'], data['max_iterations'],
                   selection_strategies[data['selection_strategy']](),
                   crossover_strategies[data['crossover_strategy']](),
                   mutation_strategies[data['mutation_strategy']]())
