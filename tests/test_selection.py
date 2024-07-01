from src.algorithms.Selection.RankBasedSelection import RankBasedSelection

import numpy as np


def test_select():
    population = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=float)
    quality_function_values = np.array([1, 2, 3], dtype=float)
    selection = RankBasedSelection()
    selected = selection.select(population, quality_function_values)
    assert selected.shape == (2, 3)
    assert selected.dtype == float
    assert np.all(np.isin(selected, population))