from PyQt5.QtWidgets import QDockWidget
from PyQt5.QtCore import pyqtSignal

from src.gui.ParametersDock.parameters_dock_ui import Ui_ParametersDock

from src.gui.ParametersDock.parameters_validator import ParametersValidator
from src.gui.ParametersDock.settings_manager import SettingsManager


class ParametersDock(QDockWidget, Ui_ParametersDock):
    goButtonClicked = pyqtSignal(dict, name='goButtonClicked')

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.goButton.clicked.connect(self.emit_go_button_clicked)

        self.validator = ParametersValidator(self)
        self.settings_manager = SettingsManager(self)

        self.saveButton.clicked.connect(self.save_settings)
        self.loadButton.clicked.connect(self.load_settings)
        self.randomButton.clicked.connect(self.random_settings)

    def validate_input(self) -> bool:
        return self.validator.validate(
            self.functionLineEdit.text(),
            self.leftBoundDoubleSpinBox.value(),
            self.rightBoundDoubleSpinBox.value(),
            self.stepsAmountSpinBox.value()
        )

    def emit_go_button_clicked(self):
        if not self.validate_input():
            return
        self.goButtonClicked.emit(self.settings_manager.get_settings())

    def random_settings(self):
        self.settings_manager.random_settings()
        self.emit_go_button_clicked()

    def save_settings(self):
        self.settings_manager.save_settings()

    def load_settings(self):
        self.settings_manager.load_settings()
        self.emit_go_button_clicked()
