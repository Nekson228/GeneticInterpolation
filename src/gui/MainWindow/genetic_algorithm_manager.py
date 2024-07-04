from typing import Optional

from src.algorithms.Genetic.genetic import GeneticAlgorithm
from src.algorithms.Genetic.genetic_hyper_initializer import GeneticHyperInitializer
from src.algorithms.Genetic.genetic_session_initializer import GeneticSessionInitializer

from src.data_structures.settings_data import SettingsData

from src.constants import HYPERPARAMETERS_PATH


class GeneticAlgorithmManager:
    def __init__(self):
        self.genetic: Optional[GeneticAlgorithm] = None

    def initialize_genetic(self, settings: SettingsData) -> None:
        session_init = GeneticSessionInitializer(settings)
        hyper_init = GeneticHyperInitializer.from_json(HYPERPARAMETERS_PATH)
        self.genetic = GeneticAlgorithm(hyper_init, session_init)
