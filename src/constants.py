import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
SESSIONS_DIR = os.path.join(BASE_DIR, 'sessions')
UI_DIR = os.path.join(BASE_DIR, 'ui')
SRC_DIR = os.path.join(BASE_DIR, 'src')
IMAGES_DIR = os.path.join(ASSETS_DIR, 'images')
PARAMETERS_DIR = os.path.join(ASSETS_DIR, 'parameters')
GUI_SRC_DIR = os.path.join(SRC_DIR, 'gui')
HYPERPARAMETERS_PATH = os.path.join(PARAMETERS_DIR, 'hyperparameters.json')

JSON_FILE_FILTER = "JSON Files (*.json)"

SAVE_FILE_CAPTION = "Save File"
OPEN_FILE_CAPTION = "Open File"

FUNCTION_COEFFICIENTS_SPLITTER = ' '

MAX_POLYNOMIAL_COEFFICIENT_AMOUNT = 9

NUMBER_OF_FUNCTION_POINTS = 10_000
