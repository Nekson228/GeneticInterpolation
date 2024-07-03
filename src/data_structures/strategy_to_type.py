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
