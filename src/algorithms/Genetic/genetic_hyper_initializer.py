from json import load

from src.data_structures.strategy_to_type import crossover_strategies, mutation_strategies, selection_strategies
from src.data_structures.hyperparameters_data import HyperparametersData


class GeneticHyperInitializer:
    def __init__(self, hyperparameters_data: HyperparametersData):
        self.mutation_rate = hyperparameters_data['mutation_rate']
        self.crossover_rate = hyperparameters_data['crossover_rate']
        self.population_size = hyperparameters_data['population_size']
        self.max_generations = hyperparameters_data['max_generations']

        self.selection_strategy = selection_strategies[hyperparameters_data['selection_strategy']]()
        self.crossover_strategy = crossover_strategies[hyperparameters_data['crossover_strategy']]()
        self.mutation_strategy = mutation_strategies[hyperparameters_data['mutation_strategy']]()

    @classmethod
    def from_json(cls, path: str):
        with open(path) as file:
            data: HyperparametersData = load(file)
        return cls(data)
