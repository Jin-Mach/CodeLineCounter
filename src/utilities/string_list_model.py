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

    def new_file(self, file: str) -> None:
        row = self.rowCount()
        self.insertRow(row)
        index = self.index(row, 0)
        self.setData(index, file)

    def delete_file(self, row: int) -> None:
        self.removeRow(row)

    def clear_model(self) -> None:
        self.removeRows(0, self.rowCount())

    def file_exists_in_model(self, file: str) -> bool:
        return file in self.stringList()