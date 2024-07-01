from typing import NamedTuple

from PyQt5.QtWidgets import QLineEdit, QDoubleSpinBox, QSpinBox


class SettingsWidgets(NamedTuple):
    functionLineEdit: QLineEdit
    leftBoundDoubleSpinBox: QDoubleSpinBox
    rightBoundDoubleSpinBox: QDoubleSpinBox
    stepsAmountSpinBox: QSpinBox
