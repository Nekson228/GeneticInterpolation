import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'images')
PARAMETERS_DIR = os.path.join(ASSETS_DIR, 'parameters')

FUNCTION_COEFFICIENTS_SPLITTER = ' '

MAX_POLYNOMIAL_COEFFICIENT_AMOUNT = 9

NUMBER_OF_FUNCTION_POINTS = 10_000
