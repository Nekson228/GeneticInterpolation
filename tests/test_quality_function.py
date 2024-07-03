import numpy as np

from src.algorithms.Quality.MeanStepDistance import MeanStepDistance


def test_mean_step_distance():
    function = np.polynomial.Polynomial([0, 1])
    mean_step_distance = MeanStepDistance(-1, 1, function, 3)
    population = np.random.uniform(-1, 1, size=(10, 3))
    quality_values = mean_step_distance.calculate(population)
    assert quality_values.shape == (10,)
    assert quality_values.dtype == float
    assert (quality_values >= 0).all()
    assert (quality_values <= 1).all()
