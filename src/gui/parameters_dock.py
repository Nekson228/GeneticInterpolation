from typing import TypedDict
from json import dump, load
from random import randint

from PyQt5.QtWidgets import QDockWidget, QMessageBox, QFileDialog
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

        self.saveButton.clicked.connect(self.save_settings)
        self.loadButton.clicked.connect(self.load_settings)
        self.randomButton.clicked.connect(self.random_settings)

    def validate_input(self) -> bool:
        function_text = self.functionLineEdit.text()

        if not function_text:
            QMessageBox.critical(self, "Error", "All fields must be filled.")
            return False

        try:
            function_data = list(map(float, function_text.split(FUNCTION_COEFFICIENTS_SPLITTER)))
        except ValueError:
            QMessageBox.critical(self, "Error", "Invalid data entered for function.")
            return False

        if len(function_data) > 9:
            QMessageBox.critical(self, "Error", "Polynomial degree must be not greater than 8.")
            return False

        if self.leftBoundDoubleSpinBox.value() >= self.rightBoundDoubleSpinBox.value():
            QMessageBox.critical(self, "Error", "Left bound must be less than right bound.")
            return False

        if self.stepsAmountSpinBox.value() < 2:
            QMessageBox.critical(self, "Error", "Amount of steps must be greater than 1.")
            return False

        return True

    def emit_go_button_clicked(self):
        if not self.validate_input():
            return
        self.goButtonClicked.emit(self.get_settings())

    def get_settings(self) -> SettingsData:
        return {
            'f(x)': list(map(float, self.functionLineEdit.text().split(FUNCTION_COEFFICIENTS_SPLITTER))),
            'steps_amount': self.stepsAmountSpinBox.value(),
            'left_bound': self.leftBoundDoubleSpinBox.value(),
            'right_bound': self.rightBoundDoubleSpinBox.value(),
        }

    def set_settings(self, settings: SettingsData) -> None:
        self.functionLineEdit.setText(FUNCTION_COEFFICIENTS_SPLITTER.join(map(str, settings['f(x)'])))
        self.stepsAmountSpinBox.setValue(settings['steps_amount'])
        self.leftBoundDoubleSpinBox.setValue(settings['left_bound'])
        self.rightBoundDoubleSpinBox.setValue(settings['right_bound'])

    def save_file_dialog(self) -> tuple[str, str]:
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        return QFileDialog.getSaveFileName(self, "Save File", "", "JSON Files (*.json)", options=options)

    def load_file_dialog(self) -> tuple[str, str]:
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        return QFileDialog.getOpenFileName(self, "Open File", "", "JSON Files (*.json)", options=options)

    def save_settings(self) -> None:
        filename, _ = self.save_file_dialog()
        if not filename:
            return
        with open(filename, 'w') as file:
            dump(self.get_settings(), file)

    def load_settings(self) -> None:
        filename, _ = self.load_file_dialog()
        if not filename:
            return
        with open(filename, 'r') as file:
            settings = load(file)
        self.set_settings(settings)
        self.emit_go_button_clicked()

    def random_settings(self) -> None:
        self.set_settings({
            'f(x)': [randint(-10, 10) for _ in range(randint(3, 9))],
            'steps_amount': randint(30, 100),
            'left_bound': randint(-30, 0),
            'right_bound': randint(1, 30)
        })
        self.emit_go_button_clicked()
