from PyQt5.QtWidgets import QFileDialog, QWidget


class FileDialogManager:
    def __init__(self, parent: QWidget):
        self.parent = parent

    def save_file_dialog(self) -> tuple[str, str]:
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        return QFileDialog.getSaveFileName(self.parent, "Save File", "", "JSON Files (*.json)", options=options)

    def load_file_dialog(self) -> tuple[str, str]:
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        return QFileDialog.getOpenFileName(self.parent, "Open File", "", "JSON Files (*.json)", options=options)
