import pathlib

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QLabel, QDialog, QVBoxLayout, QPushButton

from src.utilities.excenption_handler import ExceptionHandler


# noinspection PyUnresolvedReferences
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
        message.setDefaultButton(QMessageBox.StandardButton.No)
        result = message.exec()
        if result == QMessageBox.StandardButton.Yes:
            return True
        return False

    @staticmethod
    def show_row_count_dialog(row_count: int, parent=None) -> None:
        dialog = QDialog(parent)
        dialog.setWindowTitle("Row count")
        layout = QVBoxLayout()
        dialog_text = QLabel("Total rows in your project:")
        dialog_text.setFont(QFont("Arial", 12))
        dialog_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        row_count_text = QLabel(f"{row_count}")
        row_count_text.setFont(QFont("Arial", 15))
        row_count_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ok_button = QPushButton("Ok")
        ok_button.clicked.connect(dialog.accept)
        layout.addWidget(dialog_text)
        layout.addWidget(row_count_text)
        layout.addWidget(ok_button)
        dialog.setLayout(layout)
        dialog.exec()