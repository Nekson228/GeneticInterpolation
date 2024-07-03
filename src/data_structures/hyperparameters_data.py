from typing import TypedDict, Literal, get_args

SelectionStr = Literal['rank_based']
CrossoverStr = Literal['uniform', 'intermediate']
MutationStr = Literal['real_valued']

selection_strategy_keys = get_args(SelectionStr)
crossover_strategy_keys = get_args(CrossoverStr)
mutation_strategy_keys = get_args(MutationStr)

HyperparametersData = TypedDict('HyperparametersData', {
    "mutation_rate": float,
    "crossover_rate": float,
    "population_size": int,
    "max_generations": int,
    "selection_strategy": SelectionStr,
    "crossover_strategy": CrossoverStr,
    "mutation_strategy": MutationStr
})
