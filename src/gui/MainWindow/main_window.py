import os
from typing import Optional

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui, Qt, QtCore
from PyQt5.QtCore import QTime, QTimer

import numpy as np

from src.gui.MainWindow.main_window_ui import Ui_MainWindow

from src.gui.ParametersDock.parameters_dock import ParametersDock

from src.gui.MplCanvas.mpl_canvas import MplCanvas

from src.constants import IMAGES_DIR, PARAMETERS_DIR

from src.data_structures.settings_data import SettingsData

from src.algorithms.Genetic.genetic import GeneticAlgorithm
from src.algorithms.Genetic.genetic_session_initializer import GeneticSessionInitializer
from src.algorithms.Genetic.genetic_hyper_initializer import GeneticHyperInitializer

from src.algorithms.step_function import StepFunction


class MainWindow(QMainWindow, Ui_MainWindow):
    PLAY_ICON_PATH = os.path.join(IMAGES_DIR, 'play-50.png')
    PAUSE_ICON_PATH = os.path.join(IMAGES_DIR, 'pause-50.png')
    HYPERPARAMETERS_PATH = os.path.join(PARAMETERS_DIR, 'hyperparameters.json')

    TOP3_FMT = ['red', 'orange', 'yellow']

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.play_icon = QtGui.QIcon(MainWindow.PLAY_ICON_PATH)
        self.pause_icon = QtGui.QIcon(MainWindow.PAUSE_ICON_PATH)

        self.parametersDock = ParametersDock()
        self.addDockWidget(Qt.Qt.LeftDockWidgetArea, self.parametersDock)

        self.canvas = MplCanvas(self.canvas)

        self.playButton.clicked.connect(self.play)
        self.nextButton.clicked.connect(self.next)

        self.parametersDock.goButtonClicked.connect(self.update_session)

        self.is_playing = False
        self.is_controls_disabled = False

        self.genetic: Optional[GeneticAlgorithm] = None
        self.step_function: Optional[StepFunction] = None

    def play(self):
        if self.is_playing:
            self.is_playing = False
            self.playButton.setIcon(self.play_icon)
            print('Pause')
        else:
            self.is_playing = True
            self.playButton.setIcon(self.pause_icon)
            print('Play')

    def next(self):
        print('Next')

    def toggle_controls(self, enable: bool) -> None:
        self.playButton.setEnabled(enable)
        self.nextButton.setEnabled(enable)
        self.parametersDock.setEnabled(enable)

    def _update_genetic(self, settings: SettingsData) -> None:
        session_init = GeneticSessionInitializer(settings)
        hyper_init = GeneticHyperInitializer.from_json(MainWindow.HYPERPARAMETERS_PATH)
        self.genetic = GeneticAlgorithm(hyper_init, session_init)

    def _update_population_plots(self) -> None:
        top3_best = self.genetic.get_top_individuals(3)
        for i, individual in enumerate(top3_best):
            self.step_function.step_heights = individual
            self.canvas.plot_step_function(self.step_function, MainWindow.TOP3_FMT[i])

        best_quality = self.genetic.get_best_quality_function_values()
        self.canvas.plot_quality_function(best_quality, self.genetic.current_generation)
        self.canvas.render()

    def update_session(self, settings: SettingsData) -> None:
        polynomial = np.polynomial.Polynomial(settings['f(x)'][::-1])
        self.canvas.clear_all()
        self.canvas.plot_function(polynomial, settings['left_bound'], settings['right_bound'])
        self.canvas.render()

        if self.is_controls_disabled:
            self.toggle_controls(True)
            self.is_controls_disabled = False

        self.step_function = StepFunction(settings['steps_amount'], settings['left_bound'], settings['right_bound'])
        self._update_genetic(settings)
