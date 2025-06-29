from PyQt6.QtWidgets import QLabel

from src.utilities.dialog_manager import DialogManager
from src.utilities.string_list_model import StringListModel


class FileController:

    @staticmethod
    def add_files(files: list[str], model: StringListModel, dialog: DialogManager, text_label: QLabel) -> None:
        for file in files:
            if file in model.stringList():
                if dialog.show_duplicate_file_dialog(file):
                    model.add_file(file)
            else:
                model.add_file(file)
        text_label.setText(f"files: {model.rowCount()}")

    @staticmethod
    def delete_file(index: int, model: StringListModel, dialog: DialogManager, text_label: QLabel) -> None:
        if index >= 0:
            model.delete_file(index)
            text_label.setText(f"files: {model.rowCount()}")
        else:
            dialog.show_delete_file_messagebox()

    @staticmethod
    def delete_all_files(model: StringListModel, dialog: DialogManager, text_label: QLabel, parent=None) -> None:
        if model.rowCount() > 0:
            if dialog.show_delete_files_dialog(parent):
                model.clear_model()
                text_label.setText(f"files: {model.rowCount()}")