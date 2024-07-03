import numpy as np

from src.algorithms.Quality.QualityFunction import QualityFunction

from src.algorithms.step_function import StepFunction

from src.constants import NUMBER_OF_FUNCTION_POINTS


class MeanStepDistance(QualityFunction):
    """
    Quality function that calculates the mean distance between the function, and the step function.
    """
    def __init__(self, left_bound: float, right_bound: float, function: np.polynomial.Polynomial,
                 chromosome_length: int):
        super().__init__(left_bound, right_bound, function, chromosome_length)
        self._step_function = StepFunction(chromosome_length, left_bound, right_bound)
        self._points_per_step = NUMBER_OF_FUNCTION_POINTS // self._chromosome_length

        self._x_points = [np.linspace(start, stop, self._points_per_step) for _, (start, stop) in self._step_function]
        self._y_points = [self._function(x_points) for x_points in self._x_points]

    def calculate(self, population: np.ndarray) -> np.ndarray:
        """
        Calculate quality function values for the entire population.
        :param population: 2D-array where each row is an individual.
        :return: 1D array of quality function values for every individual.
        """
        quality_values = np.zeros(population.shape[0], dtype=float)
        for idx, individual in enumerate(population):
            self._step_function.step_heights = individual
            res = np.zeros(self._chromosome_length)
            for i, height in enumerate(self._step_function.step_heights):
                y_points = self._y_points[i]
                res[i] = np.abs(y_points - height).sum()
            quality_values[idx] = res.sum() / NUMBER_OF_FUNCTION_POINTS
        return quality_values
