import pathlib

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QLabel, QDialog, QVBoxLayout, QPushButton, QHBoxLayout


# noinspection PyUnresolvedReferences
class DialogManager:

    @staticmethod
    def get_file_path_dialog(parent=None) -> list:
        dialog_path = pathlib.Path(__file__).parts[0]
        file_paths, _ = QFileDialog.getOpenFileNames(parent, "", dialog_path, "Python Files (*.py)")
        if file_paths:
            return file_paths

    @staticmethod
    def show_delete_file_messagebox(parent=None) -> None:
        message = QMessageBox(parent)
        message.setWindowTitle("Select file")
        message.setText("Select the file you want to delete.")
        message.exec()

    @staticmethod
    def show_delete_files_dialog(parent=None) -> bool:
        dialog = QDialog(parent)
        dialog.setWindowTitle("Deleting files..")
        layout = QVBoxLayout()
        text_label = QLabel("Delete all files?")
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        question_label = QLabel("Yes/No")
        question_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        buttons_layout = QHBoxLayout()
        yes_button = QPushButton("Yes")
        yes_button.clicked.connect(dialog.accept)
        no_button = QPushButton("No")
        no_button.setDefault(True)
        no_button.clicked.connect(dialog.reject)
        buttons_layout.addStretch()
        buttons_layout.addWidget(yes_button)
        buttons_layout.addWidget(no_button)
        layout.addWidget(text_label)
        layout.addWidget(question_label)
        layout.addLayout(buttons_layout)
        dialog.setLayout(layout)
        result = dialog.exec()
        return result == QDialog.DialogCode.Accepted

    @staticmethod
    def show_no_files_messagebox(parent=None) -> None:
        message = QMessageBox(parent)
        message.setWindowTitle("No Files Selected")
        message.setText("Please select one or more files to count the lines of code.")
        message.exec()

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

    @staticmethod
    def show_duplicate_file_dialog(file: str, parent=None) -> bool:
        dialog = QDialog(parent)
        dialog.setWindowTitle("Duplicate file")
        layout = QVBoxLayout()
        dialog_text = QLabel(f"File is in your list:\n{file}\nAdd file?")
        dialog_text.setFont(QFont("Arial", 12))
        dialog_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        buttons_layout = QHBoxLayout()
        add_button = QPushButton("Add file")
        add_button.clicked.connect(dialog.accept)
        skip_button = QPushButton("Skip")
        skip_button.clicked.connect(dialog.reject)
        buttons_layout.addStretch()
        buttons_layout.addWidget(add_button)
        buttons_layout.addWidget(skip_button)
        layout.addWidget(dialog_text)
        layout.addLayout(buttons_layout)
        dialog.setLayout(layout)
        result = dialog.exec()
        return result == dialog.DialogCode.Accepted