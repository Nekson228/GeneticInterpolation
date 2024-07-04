import os

from PyQt5.QtWidgets import QDockWidget
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSignal

from src.gui.ControlPanelDock.control_panel_dock_ui import Ui_ControlPanelDock

from src.constants import IMAGES_DIR


class ControlPanelDock(QDockWidget, Ui_ControlPanelDock):
    PLAY_ICON_PATH = os.path.join(IMAGES_DIR, 'play-50.png')
    PAUSE_ICON_PATH = os.path.join(IMAGES_DIR, 'pause-50.png')

    playButtonClicked = pyqtSignal(bool, name='playButtonClicked')
    nextButtonClicked = pyqtSignal(name='nextButtonClicked')
    ffButtonClicked = pyqtSignal(name='ffButtonClicked')

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.PLAY_ICON = QtGui.QIcon(ControlPanelDock.PLAY_ICON_PATH)
        self.PAUSE_ICON = QtGui.QIcon(ControlPanelDock.PAUSE_ICON_PATH)

        self.playButton.clicked.connect(self.play)
        self.nextButton.clicked.connect(self.next)
        self.ffButton.clicked.connect(self.fast_forward)

        self.is_playing = False
        self.controls_enabled = False

    @property
    def refresh_rate(self):
        return self.refreshSpinBox.value()

    def toggle_play_button(self, is_playing: bool):
        self.playButton.setIcon(self.PLAY_ICON if is_playing else self.PAUSE_ICON)
        self.is_playing = not is_playing

    def toggle_controls(self, enable_controls: bool, toggle_play: bool = True):
        if toggle_play:
            self.playButton.setEnabled(enable_controls)
        if self.controls_enabled == enable_controls:
            return
        self.nextButton.setEnabled(enable_controls)
        self.ffButton.setEnabled(enable_controls)
        self.refreshSpinBox.setEnabled(enable_controls)
        self.controls_enabled = enable_controls

    def play(self):
        self.toggle_play_button(self.is_playing)
        self.toggle_controls(not self.is_playing, toggle_play=False)
        self.playButtonClicked.emit(not self.is_playing)

    def next(self):
        self.nextButtonClicked.emit()

    def fast_forward(self):
        self.ffButtonClicked.emit()
