import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'images')
PARAMETERS_DIR = os.path.join(ASSETS_DIR, 'parameters')
SESSIONS_DIR = os.path.join(BASE_DIR, 'sessions')

JSON_FILE_FILTER = "JSON Files (*.json)"

SAVE_FILE_CAPTION = "Save File"
OPEN_FILE_CAPTION = "Open File"

FUNCTION_COEFFICIENTS_SPLITTER = ' '

MAX_POLYNOMIAL_COEFFICIENT_AMOUNT = 9

NUMBER_OF_FUNCTION_POINTS = 10_000
