from typing import Optional

from src.gui.MainWindow.plot_manager import PlotManager
from src.gui.MainWindow.genetic_algorithm_manager import GeneticAlgorithmManager

from src.data_structures.settings_data import SettingsData

from src.algorithms.step_function import StepFunction


class SessionManager:
    def __init__(self, plot_manager: PlotManager, genetic_manager: GeneticAlgorithmManager):
        self.plot_manager = plot_manager
        self.genetic_manager = genetic_manager
        self.settings: Optional[SettingsData] = None

    def update_session(self, settings: SettingsData) -> StepFunction:
        self.plot_manager.update_session_plots(settings)
        step_function = StepFunction(settings['steps_amount'], settings['left_bound'], settings['right_bound'])
        self.genetic_manager.initialize_genetic(settings)
        self.plot_manager.update_population_plots(self.genetic_manager.genetic, step_function)
        self.settings = settings
        return step_function
