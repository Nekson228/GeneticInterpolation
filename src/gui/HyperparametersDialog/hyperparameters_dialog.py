from json import load, dump

from PyQt5.QtWidgets import QDialog

from src.gui.HyperparametersDialog.hyperparameters_dialog_ui import Ui_HyperparametersDialog

from src.data_structures.hyperparameters_data import (HyperparametersData,
                                                      crossover_strategy_keys, mutation_strategy_keys,
                                                      selection_strategy_keys)


class HyperparametersDialog(QDialog, Ui_HyperparametersDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.selectionComboBox.addItems(selection_strategy_keys)
        self.crossoverComboBox.addItems(crossover_strategy_keys)
        self.mutationComboBox.addItems(mutation_strategy_keys)

        self._load_hyperparameters()

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def _load_hyperparameters(self):
        with open('assets/parameters/hyperparameters.json') as file:
            data: HyperparametersData = load(file)
        self.mutationRateDoubleSpinBox.setValue(data['mutation_rate'])
        self.crossoverRateDoubleSpinBox.setValue(data['crossover_rate'])
        self.populationSizeSpinBox.setValue(data['population_size'])
        self.maxGenerationsAmountSpinBox.setValue(data['max_generations'])
        self.selectionComboBox.setCurrentText(data['selection_strategy'])
        self.crossoverComboBox.setCurrentText(data['crossover_strategy'])
        self.mutationComboBox.setCurrentText(data['mutation_strategy'])

    def _save_hyperparameters(self):
        data: HyperparametersData = {
            'mutation_rate': self.mutationRateDoubleSpinBox.value(),
            'crossover_rate': self.crossoverRateDoubleSpinBox.value(),
            'population_size': self.populationSizeSpinBox.value(),
            'max_generations': self.maxGenerationsAmountSpinBox.value(),
            'selection_strategy': self.selectionComboBox.currentText(),
            'crossover_strategy': self.crossoverComboBox.currentText(),
            'mutation_strategy': self.mutationComboBox.currentText()
        }
        with open('assets/parameters/hyperparameters.json', 'w') as file:
            dump(data, file)

    def accept(self):
        self._save_hyperparameters()
        super().accept()

    def reject(self):
        super().reject()
