from PyQt6.QtCore import QStringListModel, pyqtSignal, QObject

from src.utilities.excenption_handler import ExceptionHandler


# noinspection PyUnresolvedReferences
class Counter(QObject):
    count_signal = pyqtSignal(int)

    @staticmethod
    def count_lines_in_file(file_path: str) -> int | None:
        try:
            in_comment = False
            lines = 0
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    stripped_line = line.strip()
                    if not stripped_line or stripped_line.startswith("#"):
                        continue
                    if stripped_line.startswith(("'''", '"""')) and stripped_line.endswith(("'''", '"""')):
                        continue
                    if not in_comment and (stripped_line.startswith("'''") or stripped_line.startswith('"""')):
                        if stripped_line.endswith("'''") or stripped_line.endswith('"""'):
                            if len(stripped_line) > 3:
                                continue
                        else:
                            in_comment = True
                        continue
                    if in_comment and (stripped_line.endswith("'''") or stripped_line.endswith('"""')):
                        in_comment = False
                        continue
                    if in_comment:
                        continue
                    lines += 1
            return lines
        except Exception as e:
            ExceptionHandler.exception_handler(e)
            return None

    def line_counter(self, model: QStringListModel) -> None:
        try:
            total_lines = 0
            for line in model.stringList():
                file_path = line.strip()
                if not file_path:
                    continue
                total_lines += self.count_lines_in_file(file_path)
            self.count_signal.emit(total_lines)
        except Exception as e:
            ExceptionHandler.exception_handler(e)