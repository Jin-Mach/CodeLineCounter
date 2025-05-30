import sys

from PyQt6.QtWidgets import QApplication

from src.ui.main_window import MainWindow

def run_app() -> None:
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(application.exec())