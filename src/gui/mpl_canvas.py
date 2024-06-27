import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import numpy as np

from typing import Callable

matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width: int = 8, height: int = 4, dpi: int = 100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot()
        super(MplCanvas, self).__init__(fig)
        self.setParent(parent)

    def plot_function(self, f: Callable[[float], float], left_bound: float, right_bound: float, fmt: str = 'b-'):
        x = np.linspace(left_bound, right_bound, int(self.figure.get_dpi() * self.figure.get_figwidth()))
        y = np.vectorize(f)(x)
        self.axes.plot(x, y, fmt)
        self.draw()

    def clear(self):
        self.axes.clear()
        self.draw()

