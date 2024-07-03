from src.algorithms.Genetic.genetic_session_initializer import GeneticSessionInitializer


def test_genetic_session_initializer():
    settings = {
        'steps_amount': 10,
        'f(x)': [1, 0],
        'left_bound': -1,
        'right_bound': 1
    }
    genetic_session_initializer = GeneticSessionInitializer(settings)
    assert genetic_session_initializer.search_space == (-1, 1)