from PyQt6.QtWidgets import QMessageBox

from src.utilities.logger import setup_logger


class ExceptionHandler:

    @staticmethod
    def exception_handler(exception: Exception, parent=None):
        logger = setup_logger()
        logger.error("An error occurred: %s", exception, exc_info=True)
        message = QMessageBox(parent)
        message.setWindowTitle("Error")
        message.setIcon(QMessageBox.Icon.Critical)
        message.setText(f"Error: {exception}")
        message.exec()