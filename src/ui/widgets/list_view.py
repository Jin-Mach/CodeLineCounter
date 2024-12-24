from PyQt6.QtCore import QStringListModel
from PyQt6.QtWidgets import QListView


class ListView(QListView):
    def __init__(self, model: QStringListModel, parent=None) -> None:
        super().__init__(parent)
        self.setModel(model)
        self.setEditTriggers(QListView.EditTrigger.NoEditTriggers)