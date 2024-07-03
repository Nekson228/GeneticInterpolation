import numpy as np

from typing import Iterator


class StepFunction:
    """
    Class to represent a step function (g(x)) to draw.
    """
    def __init__(self, number_of_steps: int, left_bound: float, right_bound: float, steps_heights: np.ndarray = None):
        """
        Initialize the step-function.
        :param number_of_steps: steps amount in the function.
        :param left_bound: left bound of the function.
        :param right_bound: right bound of the function.
        :param steps_heights: np.ndarray with the float heights of the steps.
        """
        self._number_of_steps = number_of_steps
        self._steps_heights = steps_heights if steps_heights is not None else np.zeros(number_of_steps)
        self._step_intervals = np.linspace(left_bound, right_bound, number_of_steps + 1, endpoint=True)

    def __iter__(self) -> Iterator[tuple[float, np.ndarray[2, float]]]:
        for i in range(self._number_of_steps):
            yield self._steps_heights[i], self._step_intervals[i:i + 2]

    @property
    def step_heights(self):
        return self._steps_heights

    @step_heights.setter
    def step_heights(self, new_heights: np.ndarray):
        self._steps_heights = new_heights
