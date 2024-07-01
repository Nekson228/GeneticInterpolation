import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets', 'images')

FUNCTION_COEFFICIENTS_SPLITTER = ' '

MAX_POLYNOMIAL_DEGREE = 8
MIN_STEPS_AMOUNT = 2