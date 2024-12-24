from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

from src.ui.widgets.list_view import ListView
from src.utilities.excenption_handler import ExceptionHandler
from src.utilities.dialog_manager import DialogManager
from src.utilities.string_list_model import StringListModel


# noinspection PyUnresolvedReferences
class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Code line counter")
        self.setFixedSize(500, 400)
        self.string_model = StringListModel()
        self.list_view = ListView(self.string_model, self)
        self.create_gui()

    def create_gui(self) -> None:
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        list_view = self.list_view
        file_count_layout = QHBoxLayout()
        self.file_count_label = QLabel("files: 0")
        file_count_layout.addStretch()
        file_count_layout.addWidget(self.file_count_label)
        file_buttons_layout = QHBoxLayout()
        add_file_button = QPushButton("Add file")
        add_file_button.clicked.connect(self.add_new_file)
        delete_file_button = QPushButton("Delete file")
        delete_file_button.clicked.connect(self.delete_file)
        delete_all_files = QPushButton("Delete all files")
        delete_all_files.clicked.connect(self.delete_all_files)
        count_layout = QHBoxLayout()
        count_button = QPushButton("Start")
        count_layout.addStretch()
        count_layout.addWidget(count_button)
        count_layout.addStretch()
        file_buttons_layout.addWidget(add_file_button)
        file_buttons_layout.addWidget(delete_file_button)
        file_buttons_layout.addWidget(delete_all_files)
        main_layout.addWidget(list_view)
        main_layout.addLayout(file_count_layout)
        main_layout.addLayout(file_buttons_layout)
        main_layout.addLayout(count_layout)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def add_new_file(self) -> None:
        try:
            file = DialogManager.get_file_path_dialog(self)
            if not self.string_model.file_exists_in_model(file):
                self.string_model.new_file(file)
                self.file_count_label.setText(f"files: {self.string_model.rowCount()}")
            else:
                DialogManager.existing_file_messagebox(file, self)
        except Exception as e:
            ExceptionHandler.exception_handler(e)

    def delete_file(self) -> None:
        try:
            index = self.list_view.currentIndex().row()
            if index >= 0:
                self.string_model.delete_file(index)
                self.file_count_label.setText(f"files: {self.string_model.rowCount()}")
        except Exception as e:
            ExceptionHandler.exception_handler(e)

    def delete_all_files(self) -> None:
        try:
            if DialogManager.delete_files_dialog(self):
                self.string_model.clear_model()
                self.file_count_label.setText(f"files: {self.string_model.rowCount()}")
        except Exception as e:
            ExceptionHandler.exception_handler(e)