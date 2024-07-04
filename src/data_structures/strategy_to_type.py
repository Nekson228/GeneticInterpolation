from src.algorithms.Crossover.crossover_strategy import CrossoverStrategy
from src.algorithms.Crossover.uniform_crossover import UniformCrossover
from src.algorithms.Crossover.intermediate_recombination import IntermediateRecombination

from src.algorithms.Mutation.mutation_strategy import MutationStrategy
from src.algorithms.Mutation.real_valued_mutation import RealValuedMutation
from src.algorithms.Mutation.swap_mutation import SwapMutation

from src.algorithms.Selection.selection_strategy import SelectionStrategy
from src.algorithms.Selection.rank_based_selection import RankBasedSelection
from src.algorithms.Selection.roulette_selection import RouletteSelection

crossover_strategies: dict[str, type[CrossoverStrategy]] = {
    'uniform': UniformCrossover,
    'intermediate': IntermediateRecombination,
}

mutation_strategies: dict[str, type[MutationStrategy]] = {
    'real_valued': RealValuedMutation,
    'swap': SwapMutation,
}

selection_strategies: dict[str, type[SelectionStrategy]] = {
    'rank_based': RankBasedSelection,
    'roulette': RouletteSelection,
}
