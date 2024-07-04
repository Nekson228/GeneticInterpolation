from PyQt5.QtWidgets import QFileDialog, QWidget

from src.constants import JSON_FILE_FILTER, SESSIONS_DIR, SAVE_FILE_CAPTION, OPEN_FILE_CAPTION


class FileDialogManager:
    def __init__(self, parent: QWidget):
        self.parent = parent

    def save_file_dialog(self) -> tuple[str, str]:
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        return QFileDialog.getSaveFileName(self.parent, SAVE_FILE_CAPTION, SESSIONS_DIR, JSON_FILE_FILTER,
                                           options=options)

    def load_file_dialog(self) -> tuple[str, str]:
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        return QFileDialog.getOpenFileName(self.parent, OPEN_FILE_CAPTION, SESSIONS_DIR, JSON_FILE_FILTER,
                                           options=options)
