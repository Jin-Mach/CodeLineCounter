import pathlib

from PyQt6.QtWidgets import QFileDialog, QMessageBox

from src.utilities.excenption_handler import ExceptionHandler


class DialogManager:

    @staticmethod
    def get_file_path_dialog(parent=None) -> str:
        try:
            dialog_path = pathlib.Path(__file__).parts[0]
            file_path, _ = QFileDialog.getOpenFileName(parent, "", dialog_path, "Python Files (*.py)")
            return file_path
        except Exception as e:
            ExceptionHandler.exception_handler(e, parent)

    @staticmethod
    def existing_file_messagebox(file: str, parent=None) -> None:
        message = QMessageBox(parent)
        message.setWindowTitle("Existing file")
        message.setText(f"You have already added this file:\n{file}")
        message.exec()

    @staticmethod
    def delete_files_dialog(parent=None) -> bool:
        message = QMessageBox(parent)
        message.setWindowTitle("Delete all files")
        message.setText("Delete all files?\nYes/No")
        message.addButton(QMessageBox.StandardButton.Yes)
        message.addButton(QMessageBox.StandardButton.No)
        result = message.exec()
        if result == QMessageBox.StandardButton.Yes:
            return True
        return False