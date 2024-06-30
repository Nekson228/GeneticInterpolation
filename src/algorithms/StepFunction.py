import numpy as np

from typing import Iterator


class StepFunction:
    """
    Class to represent a step function (g(x)) to draw.
    """
    def __init__(self, number_of_steps: int, left_bound: float, right_bound: float, steps_heights: np.ndarray):
        """
        Initialize the step-function.
        :param number_of_steps: Amount steps in the function.
        :param left_bound: Left bound of the function.
        :param right_bound: Right bound of the function.
        :param steps_heights: np.ndarray with the float heights of the steps.
        """
        self.number_of_steps = number_of_steps
        self.steps_heights = steps_heights
        self.step_intervals = np.linspace(left_bound, right_bound, number_of_steps + 1, endpoint=True)

    def __iter__(self) -> Iterator[tuple[float, np.ndarray[2, float]]]:
        for i in range(self.number_of_steps):
            yield self.steps_heights[i], self.step_intervals[i:i + 2]
