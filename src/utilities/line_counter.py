from PyQt6.QtCore import QStringListModel

from src.utilities.excenption_handler import ExceptionHandler

def count_lines_in_file(file_path: str) -> int:
    try:
        in_coment = False
        lines = 0
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                stripped_line = line.strip()
                if not stripped_line or stripped_line.startswith("#"):
                    continue
                if stripped_line.startswith(("'''", '"""')) and stripped_line.endswith(("'''", '"""')):
                    continue
                if not in_coment and (stripped_line.startswith("'''") or stripped_line.startswith('"""')):
                    if stripped_line.endswith("'''") or stripped_line.endswith('"""'):
                        if len(stripped_line) > 3:
                            continue
                    else:
                        in_coment = True
                    continue
                if in_coment and (stripped_line.endswith("'''") or stripped_line.endswith('"""')):
                    in_coment = False
                    continue
                if in_coment:
                    continue
                lines += 1
        return lines
    except Exception as e:
        ExceptionHandler.exception_handler(e)

def line_counter(model: QStringListModel) -> int:
    try:
        total_lines = 0
        for line in model.stringList():
            file_path = line.strip()
            if not file_path:
                continue
            total_lines += count_lines_in_file(file_path)
        return total_lines
    except Exception as e:
        ExceptionHandler.exception_handler(e)