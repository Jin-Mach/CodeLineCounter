import pathlib

from PyQt6.QtWidgets import QFileDialog

from src.utilities.excenption_handler import ExceptionHandler

def get_file_path(parent=None) -> str:
    try:
        dialog_path = pathlib.Path(__file__).parts[0]
        file_path, _ = QFileDialog.getOpenFileName(parent, "", dialog_path, "Python Files (*.py)")
        return file_path
    except Exception as e:
        ExceptionHandler.exception_handler(e, parent)