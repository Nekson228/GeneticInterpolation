from typing import Optional

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import Qt, QtCore
from PyQt5.QtCore import QTime, QTimer

from src.gui.MainWindow.main_window_ui import Ui_MainWindow
from src.gui.MainWindow.plot_manager import PlotManager
from src.gui.MainWindow.genetic_algorithm_manager import GeneticAlgorithmManager
from src.gui.MainWindow.session_manager import SessionManager

from src.gui.ParametersDock.parameters_dock import ParametersDock
from src.gui.ControlPanelDock.control_panel_dock import ControlPanelDock

from src.gui.MplCanvas.mpl_canvas import MplCanvas

from src.data_structures.settings_data import SettingsData

from src.algorithms.step_function import StepFunction


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.controlPanelDock = ControlPanelDock()
        self.addDockWidget(Qt.Qt.BottomDockWidgetArea, self.controlPanelDock)

        self.parametersDock = ParametersDock()
        self.addDockWidget(Qt.Qt.LeftDockWidgetArea, self.parametersDock)

        self.setCorner(Qt.Qt.BottomLeftCorner, Qt.Qt.LeftDockWidgetArea)
        self.setCorner(Qt.Qt.TopLeftCorner, Qt.Qt.LeftDockWidgetArea)

        self.setCorner(Qt.Qt.BottomRightCorner, Qt.Qt.RightDockWidgetArea)
        self.setCorner(Qt.Qt.TopRightCorner, Qt.Qt.RightDockWidgetArea)

        self.parametersDock.goButtonClicked.connect(self.update_session)

        self.controlPanelDock.playButtonClicked.connect(self.play)
        self.controlPanelDock.nextButtonClicked.connect(self.next)
        self.controlPanelDock.ffButtonClicked.connect(self.fast_forward)

        self.refresh_timer = QTimer(self)
        self.refresh_timer.timeout.connect(self.next)

        self.plotManager = PlotManager(MplCanvas(self.canvas))
        self.geneticManager = GeneticAlgorithmManager()
        self.sessionManager = SessionManager(self.plotManager, self.geneticManager)

        self.step_function: Optional[StepFunction] = None

    def play(self, is_playing: bool):
        if is_playing:
            self.refresh_timer.stop()
        else:
            self.refresh_timer.start(self.controlPanelDock.refresh_rate)

    def next(self):
        proceed = self.geneticManager.genetic.step()
        if not proceed:
            if self.refresh_timer.isActive():
                self.refresh_timer.stop()
                self.controlPanelDock.toggle_play_button(True)
            self.controlPanelDock.toggle_controls(False)
        self.plotManager.update_population_plots(self.geneticManager.genetic, self.step_function)

    def fast_forward(self):
        self.geneticManager.genetic.run()
        self.controlPanelDock.toggle_controls(False)
        self.plotManager.update_population_plots(self.geneticManager.genetic, self.step_function)

    def update_session(self, settings: SettingsData) -> None:
        self.plotManager.update_session_plots(settings)
        self.controlPanelDock.toggle_controls(True)
        self.step_function = self.sessionManager.update_session(settings)
