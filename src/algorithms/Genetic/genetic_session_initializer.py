from json import load

import numpy as np

from src.data_structures.settings_data import SettingsData

from src.constants import NUMBER_OF_FUNCTION_POINTS


class GeneticSessionInitializer:
    def __init__(self, settings: SettingsData):
        self.function = np.polynomial.Polynomial(settings['f(x)'][::-1])
        self.right_bound = settings['right_bound']
        self.left_bound = settings['left_bound']
        self.steps_amount = settings['steps_amount']
        self.search_space = self._get_search_space()

    def _get_search_space(self) -> tuple[float, float]:
        x = np.linspace(self.left_bound, self.right_bound, NUMBER_OF_FUNCTION_POINTS)
        y = self.function(x)
        return np.min(y), np.max(y)

    @classmethod
    def from_json(cls, path: str):
        with open(path) as file:
            data: SettingsData = load(file)
        return cls(data)
