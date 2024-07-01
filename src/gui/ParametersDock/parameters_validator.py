from typing import Optional

from PyQt5.QtWidgets import QMessageBox, QWidget

from src.constants import MIN_STEPS_AMOUNT, MAX_POLYNOMIAL_COEFF_AMOUNT, FUNCTION_COEFFICIENTS_SPLITTER


class ParametersValidator:
    def __init__(self, parent: Optional[QWidget] = None):
        self.parent = parent

    def validate(self, function_text: str, left_bound: float, right_bound: float, steps_amount: int) -> bool:
        if not function_text:
            QMessageBox.critical(self.parent, "Error", "All fields must be filled.")
            return False

        try:
            function_data = list(map(float, function_text.split(FUNCTION_COEFFICIENTS_SPLITTER)))
        except ValueError:
            QMessageBox.critical(self.parent, "Error", "Invalid data entered for function.")
            return False

        if len(function_data) > MAX_POLYNOMIAL_COEFF_AMOUNT:
            QMessageBox.critical(self.parent, "Error",
                                 f"Polynomial degree must be not greater than {MAX_POLYNOMIAL_COEFF_AMOUNT - 1}.")
            return Falsere

        if left_bound >= right_bound:
            QMessageBox.critical(self.parent, "Error", "Left bound must be less than right bound.")
            return False

        if steps_amount < MIN_STEPS_AMOUNT:
            QMessageBox.critical(self.parent, "Error", f"Amount of steps must be greater than {MIN_STEPS_AMOUNT - 1}.")
            return False

        return True
