from src.algorithms.Crossover.UniformCrossover import UniformCrossover
from src.algorithms.Crossover.IntermediateRecombination import IntermediateRecombination

import numpy as np


def test_uniform_crossover_produces_valid_offspring():
    parent1 = np.array([1, 2, 3], dtype=float)
    parent2 = np.array([4, 5, 6], dtype=float)
    crossover = UniformCrossover()
    offspring1, offspring2 = crossover.crossover(parent1, parent2)
    assert offspring1.shape == parent1.shape
    assert offspring2.shape == parent2.shape
    assert offspring1.dtype == float
    assert offspring2.dtype == float


def test_uniform_crossover_handles_empty_parents():
    parent1 = np.array([], dtype=float)
    parent2 = np.array([], dtype=float)
    crossover = UniformCrossover()
    offspring1, offspring2 = crossover.crossover(parent1, parent2)
    assert offspring1.shape == parent1.shape
    assert offspring2.shape == parent2.shape


def test_uniform_crossover_handles_single_element_parents():
    parent1 = np.array([1], dtype=float)
    parent2 = np.array([2], dtype=float)
    crossover = UniformCrossover()
    offspring1, offspring2 = crossover.crossover(parent1, parent2)
    assert offspring1.shape == parent1.shape
    assert offspring2.shape == parent2.shape
    assert offspring1.dtype == float
    assert offspring2.dtype == float


def test_uniform_crossover_offspring_contains_parent_genes():
    parent1 = np.array([1, 2, 3], dtype=float)
    parent2 = np.array([4, 5, 6], dtype=float)
    crossover = UniformCrossover()
    offspring1, offspring2 = crossover.crossover(parent1, parent2)
    assert all(elem in parent1 or elem in parent2 for elem in offspring1)
    assert all(elem in parent1 or elem in parent2 for elem in offspring2)


def test_intermediate_recombination_crossover_produces_valid_offspring():
    parent1 = np.array([1, 2, 3], dtype=float)
    parent2 = np.array([4, 5, 6], dtype=float)
    crossover = IntermediateRecombination()
    offspring1, offspring2 = crossover.crossover(parent1, parent2)
    assert offspring1.shape == parent1.shape
    assert offspring2.shape == parent2.shape
    assert offspring1.dtype == float
    assert offspring2.dtype == float


def test_intermediate_recombination_crossover_handles_empty_parents():
    parent1 = np.array([], dtype=float)
    parent2 = np.array([], dtype=float)
    crossover = IntermediateRecombination()
    offspring1, offspring2 = crossover.crossover(parent1, parent2)
    assert offspring1.shape == parent1.shape
    assert offspring2.shape == parent2.shape


def test_intermediate_recombination_crossover_handles_single_element_parents():
    parent1 = np.array([1], dtype=float)
    parent2 = np.array([2], dtype=float)
    crossover = IntermediateRecombination()
    offspring1, offspring2 = crossover.crossover(parent1, parent2)
    assert offspring1.shape == parent1.shape
    assert offspring2.shape == parent2.shape
    assert offspring1.dtype == float
    assert offspring2.dtype == float


def test_intermediate_recombination_crossover_handles_different_d_values():
    parent1 = np.array([1, 2, 3], dtype=float)
    parent2 = np.array([4, 5, 6], dtype=float)
    for d in [0, 0.25, 0.5, 1]:
        crossover = IntermediateRecombination(d)
        offspring1, offspring2 = crossover.crossover(parent1, parent2)
        assert offspring1.shape == parent1.shape
        assert offspring2.shape == parent2.shape
        assert offspring1.dtype == float
        assert offspring2.dtype == float
