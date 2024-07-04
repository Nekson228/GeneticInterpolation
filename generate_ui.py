import pathlib as pl
import os

from PyQt5 import uic

from src.constants import UI_DIR, GUI_SRC_DIR


def snake_to_camel(snake_str: str) -> str:
    components = snake_str.split('_')
    return ''.join(x.title() for x in components)


def generate_ui():
    ui_files = pl.Path(UI_DIR).rglob('*.ui')
    for ui_file in ui_files:
        ui_filename = ui_file.stem
        py_file = os.path.join(GUI_SRC_DIR, snake_to_camel(ui_filename), f'{ui_filename}_ui.py')
        with open(py_file, 'w') as file:
            uic.compileUi(ui_file, file)


if __name__ == '__main__':
    generate_ui()
