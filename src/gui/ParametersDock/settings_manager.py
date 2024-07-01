from json import dump, load
from random import randint

from src.gui.ParametersDock.parameters_dock import ParametersDock
from src.gui.ParametersDock.file_dialog_manager import FileDialogManager

from src.data_structures.settings_data import SettingsData

from src.constants import FUNCTION_COEFFICIENTS_SPLITTER


class SettingsManager:
    def __init__(self, parent: ParametersDock):
        self.parent = parent
        self.file_dialog_manager = FileDialogManager(parent)

    def get_settings(self) -> SettingsData:
        return {
            'f(x)': list(map(float, self.parent.functionLineEdit.text().split(FUNCTION_COEFFICIENTS_SPLITTER))),
            'steps_amount': self.parent.stepsAmountSpinBox.value(),
            'left_bound': self.parent.leftBoundDoubleSpinBox.value(),
            'right_bound': self.parent.rightBoundDoubleSpinBox.value(),
        }

    def set_settings(self, settings: SettingsData) -> None:
        self.parent.functionLineEdit.setText(FUNCTION_COEFFICIENTS_SPLITTER.join(map(str, settings['f(x)'])))
        self.parent.stepsAmountSpinBox.setValue(settings['steps_amount'])
        self.parent.leftBoundDoubleSpinBox.setValue(settings['left_bound'])
        self.parent.rightBoundDoubleSpinBox.setValue(settings['right_bound'])

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
        self.parent.emit_go_button_clicked()

    def random_settings(self) -> None:
        self.set_settings({
            'f(x)': [randint(-10, 10) for _ in range(randint(3, 9))],
            'steps_amount': randint(30, 100),
            'left_bound': randint(-30, 0),
            'right_bound': randint(1, 30)
        })
        self.parent.emit_go_button_clicked()
