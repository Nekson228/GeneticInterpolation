import json.decoder
from json import dump, load
from random import randint
from typing import Optional

from PyQt5.QtWidgets import QWidget, QMessageBox

from src.gui.ParametersDock.file_dialog_manager import FileDialogManager

from src.data_structures.settings_data import SettingsData
from src.data_structures.setting_widgets import SettingsWidgets

from src.constants import FUNCTION_COEFFICIENTS_SPLITTER


class SettingsManager:
    def __init__(self, widgets: SettingsWidgets, parent: Optional[QWidget] = None):
        self.widgets = widgets
        self.file_dialog_manager = FileDialogManager(parent)

    def get_settings(self) -> SettingsData:
        return {
            'f(x)': list(map(float, self.widgets.functionLineEdit.text().split(FUNCTION_COEFFICIENTS_SPLITTER))),
            'steps_amount': self.widgets.stepsAmountSpinBox.value(),
            'left_bound': self.widgets.leftBoundDoubleSpinBox.value(),
            'right_bound': self.widgets.rightBoundDoubleSpinBox.value(),
        }

    def set_settings(self, settings: SettingsData) -> bool:
        try:
            function = settings['f(x)']
            left_bound = settings['left_bound']
            right_bound = settings['right_bound']
            steps_amount = settings['steps_amount']
        except KeyError as e:
            QMessageBox.critical(None, "Error", f"JSON file does not contain field {e.args}")
            return False
        self.widgets.functionLineEdit.setText(FUNCTION_COEFFICIENTS_SPLITTER.join(map(str, function)))
        self.widgets.leftBoundDoubleSpinBox.setValue(left_bound)
        self.widgets.rightBoundDoubleSpinBox.setValue(right_bound)
        self.widgets.stepsAmountSpinBox.setValue(steps_amount)
        return True

    def save_settings(self) -> None:
        filename, _ = self.file_dialog_manager.save_file_dialog()
        if not filename:
            return
        with open(filename, 'w') as file:
            dump(self.get_settings(), file)

    def load_settings(self) -> bool:
        filename, _ = self.file_dialog_manager.load_file_dialog()
        if not filename:
            return False
        try:
            with open(filename, 'r') as file:
                return self.set_settings(load(file))
        except json.decoder.JSONDecodeError:
            QMessageBox.critical(None, "Error", "JSON file is invalid.")
            return False

    def random_settings(self) -> None:
        self.set_settings({
            'f(x)': [randint(-10, 10) for _ in range(randint(3, 9))],
            'steps_amount': randint(30, 100),
            'left_bound': randint(-30, 0),
            'right_bound': randint(1, 30)
        })
