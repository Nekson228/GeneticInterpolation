from typing import TypedDict

from PyQt5.QtWidgets import QDockWidget, QMessageBox
from PyQt5.QtCore import pyqtSignal

from src.gui.parameters_dock_ui import Ui_ParametersDock

from src.constants import FUNCTION_COEFFICIENTS_SPLITTER

SettingsData = TypedDict('SettingsData', {
    'f(x)': list[float],
    'steps_amount': int,
    'left_bound': float,
    'right_bound': float,
})


class ParametersDock(QDockWidget, Ui_ParametersDock):
    goButtonClicked = pyqtSignal(dict, name='goButtonClicked')

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.goButton.clicked.connect(self.emit_go_button_clicked)

    def verify_input(self) -> bool:
        function_text = self.functionLineEdit.text()

        if not function_text:
            QMessageBox.critical(self, "Error", "All fields must be filled.")
            return False

        try:
            list(map(float, function_text.split(FUNCTION_COEFFICIENTS_SPLITTER)))
        except ValueError:
            QMessageBox.critical(self, "Error", "Invalid data entered for function.")
            return False

        if self.leftBoundDoubleSpinBox.value() >= self.rightBoundDoubleSpinBox.value():
            QMessageBox.critical(self, "Error", "Left bound must be less than right bound.")
            return False

        if self.stepsAmountSpinBox.value() < 2:
            QMessageBox.critical(self, "Error", "Amount of steps must be greater than 1.")
            return False

        return True

    def emit_go_button_clicked(self):
        if not self.verify_input():
            return
        self.goButtonClicked.emit(self.get_settings())

    def get_settings(self) -> SettingsData:
        return {
            'f(x)': list(map(float, self.functionLineEdit.text().split(FUNCTION_COEFFICIENTS_SPLITTER))),
            'steps_amount': self.stepsAmountSpinBox.value(),
            'left_bound': self.leftBoundDoubleSpinBox.value(),
            'right_bound': self.rightBoundDoubleSpinBox.value(),
        }
