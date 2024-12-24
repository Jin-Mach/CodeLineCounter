from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

from src.ui.widgets.list_view import ListView


class MainWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Code line counter")
        self.setFixedSize(500, 400)
        self.list_view = ListView(self)
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
        delete_file_button = QPushButton("Delete file")
        delete_all_files = QPushButton("Delete all files")
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