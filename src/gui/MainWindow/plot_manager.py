import numpy as np

from src.gui.MplCanvas.mpl_canvas import MplCanvas

from src.algorithms.Genetic.genetic import GeneticAlgorithm
from src.algorithms.step_function import StepFunction

from src.data_structures.settings_data import SettingsData


class PlotManager:
    TOP3_FMT = ['yellow', 'orange', 'red']

    def __init__(self, canvas: MplCanvas):
        self.canvas = canvas

    def update_population_plots(self, genetic: GeneticAlgorithm, step_function: StepFunction) -> None:
        self.canvas.clear_step_lines()
        top3_best = reversed(genetic.get_top_individuals(3))
        for i, individual in enumerate(top3_best):
            step_function.step_heights = individual
            self.canvas.plot_step_function(step_function, self.TOP3_FMT[i])

        best_quality = genetic.get_best_quality_function_values()
        self.canvas.plot_quality_function(best_quality, genetic.current_generation)
        self.canvas.render()

    def update_session_plots(self, settings: SettingsData) -> None:
        polynomial = np.polynomial.Polynomial(settings['f(x)'][::-1])
        self.canvas.clear_all()
        self.canvas.plot_function(polynomial, settings['left_bound'], settings['right_bound'])
        self.canvas.render()
