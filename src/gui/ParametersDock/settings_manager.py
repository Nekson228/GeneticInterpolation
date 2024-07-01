from json import dump, load
from random import randint
from typing import Optional

from PyQt5.QtWidgets import QWidget

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

    def set_settings(self, settings: SettingsData) -> None:
        self.widgets.functionLineEdit.setText(FUNCTION_COEFFICIENTS_SPLITTER.join(map(str, settings['f(x)'])))
        self.widgets.stepsAmountSpinBox.setValue(settings['steps_amount'])
        self.widgets.leftBoundDoubleSpinBox.setValue(settings['left_bound'])
        self.widgets.rightBoundDoubleSpinBox.setValue(settings['right_bound'])

    def save_settings(self) -> None:
        filename, _ = self.file_dialog_manager.save_file_dialog()
        if not filename:
            return
        with open(filename, 'w') as file:
            dump(self.get_settings(), file)

    def load_settings(self) -> None:
        filename, _ = self.file_dialog_manager.load_file_dialog()
        if not filename:
            return
        with open(filename, 'r') as file:
            self.set_settings(load(file))

    def random_settings(self) -> None:
        self.set_settings({
            'f(x)': [randint(-10, 10) for _ in range(randint(3, 9))],
            'steps_amount': randint(30, 100),
            'left_bound': randint(-30, 0),
            'right_bound': randint(1, 30)
        })
