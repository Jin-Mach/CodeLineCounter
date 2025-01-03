from typing import Any

from PyQt6.QtCore import QStringListModel, Qt
from PyQt6.QtGui import QFont


class StringListModel(QStringListModel):
    def __init__(self) -> None:
        super().__init__()

    def data(self, index, role=Qt.ItemDataRole.DisplayRole) -> Any:
        if role == Qt.ItemDataRole.FontRole:
            return QFont("Arial", 11)
        return super().data(index, role)

    def add_file(self, file: str) -> None:
        self.insertRow(self.rowCount())
        self.setData(self.index(self.rowCount() - 1), file)

    def delete_file(self, row: int) -> None:
        self.removeRow(row)

    def clear_model(self) -> None:
        self.removeRows(0, self.rowCount())