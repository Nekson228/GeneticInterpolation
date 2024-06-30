import os

from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui, Qt

import numpy as np

from src.gui.main_window_ui import Ui_MainWindow
from src.gui.parameters_dock import ParametersDock, SettingsData
from src.constants import ASSETS_DIR
from src.gui.mpl_canvas import MplCanvas

class MainWindow(QMainWindow, Ui_MainWindow):
    PLAY_ICON_PATH = os.path.join(ASSETS_DIR, 'play-50.png')
    PAUSE_ICON_PATH = os.path.join(ASSETS_DIR, 'pause-50.png')

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.parametersDock = ParametersDock()
        self.addDockWidget(Qt.Qt.LeftDockWidgetArea, self.parametersDock)

        MainWindow.PLAY_ICON = QtGui.QIcon(MainWindow.PLAY_ICON_PATH)
        MainWindow.PAUSE_ICON = QtGui.QIcon(MainWindow.PAUSE_ICON_PATH)

        self.canvas = MplCanvas(self.canvas)

        self.playButton.clicked.connect(self.play)
        self.nextButton.clicked.connect(self.next)

        self.parametersDock.goButtonClicked.connect(self.update_session)

        self.isPlaying = False

    def play(self):
        if self.isPlaying:
            self.isPlaying = False
            self.playButton.setIcon(MainWindow.PLAY_ICON)
            print('Pause')
        else:
            self.isPlaying = True
            self.playButton.setIcon(MainWindow.PAUSE_ICON)
            print('Play')

    def next(self):
        print('Next')

    def update_session(self, settings: SettingsData) -> None:
        polynomial = np.polynomial.Polynomial(settings['f(x)'][::-1])
        self.canvas.clear_all()
        self.canvas.plot_function(polynomial, settings['left_bound'], settings['right_bound'])
        self.canvas.render()
