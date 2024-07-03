import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import numpy as np

from typing import Callable
from enum import Enum

from src.algorithms.step_function import StepFunction

matplotlib.use('Qt5Agg')


class PlotType(Enum):
    MAIN_FUNCTION = 0
    QUALITY_FUNCTION = 1


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width: int = 8, height: int = 4, dpi: int = 100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.subplots(1, 2)
        super(MplCanvas, self).__init__(fig)
        self.setParent(parent)

    def plot_function(self, f: Callable[[float], float], left_bound: float, right_bound: float, fmt: str = 'b-'):
        x = np.linspace(left_bound, right_bound, int(self.figure.get_dpi() * self.figure.get_figwidth()))
        y = np.vectorize(f)(x)
        self.axes[PlotType.MAIN_FUNCTION].plot(x, y, fmt)

    def plot_step_function(self, step_f: StepFunction, fmt: str = 'r-'):
        for height, interval in step_f:
            self.axes[PlotType.MAIN_FUNCTION].plot(interval, (height, height), fmt)

    def plot_quality_function(self, values: np.ndarray, n: int, fmt: str = 'r-'):
        x = np.arange(1, n + 1)
        self.axes[PlotType.QUALITY_FUNCTION].plot(x, values, fmt)

    def clear(self, plot_type: PlotType = PlotType.MAIN_FUNCTION):
        self.axes[plot_type.value].clear()

    def clear_all(self):
        for ax in self.axes:
            ax.clear()

    def render(self):
        self.draw()
        self.flush_events()
