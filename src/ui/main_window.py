from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

from src.ui.widgets.list_view import ListView
from src.utilities.excenption_handler import ExceptionHandler
from src.utilities.dialog_manager import DialogManager
from src.utilities.file_controler import FileControler
from src.utilities.line_counter import Counter
from src.utilities.string_list_model import StringListModel


# noinspection PyUnresolvedReferences
class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Code line counter")
        self.setFixedSize(600, 400)
        self.dialog_manager = DialogManager()
        self.string_model = StringListModel()
        self.list_view = ListView(self.string_model, self)
        self.file_controler = FileControler()
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
        count_button.clicked.connect(self.start_count)
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
            files = DialogManager.get_file_path_dialog(self)
            if files:
                self.file_controler.add_files(files, self.string_model, self.dialog_manager, self.file_count_label)
        except Exception as e:
            ExceptionHandler.exception_handler(e)

    def delete_file(self) -> None:
        try:
            index = self.list_view.currentIndex().row()
            self.file_controler.delete_file(index, self.string_model, self.dialog_manager, self.file_count_label)
        except Exception as e:
            ExceptionHandler.exception_handler(e)

    def delete_all_files(self) -> None:
        try:
            self.file_controler.delete_all_files(self.string_model, self.dialog_manager, self.file_count_label, self)
        except Exception as e:
            ExceptionHandler.exception_handler(e)

    def start_count(self) -> None:
        try:
            if self.string_model.rowCount() > 0:
                counter = Counter()
                counter.count_signal.connect(self.show_lines_count)
                counter.line_counter(self.string_model)
            else:
                DialogManager.show_no_files_messagebox()
        except Exception as e:
            ExceptionHandler.exception_handler(e)

    def show_lines_count(self, lines: int) -> None:
        DialogManager.show_row_count_dialog(lines, self)