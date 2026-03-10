from src.core.interfaces import ILogsInput


class LogsInput(ILogsInput):
    def __init__(self, logs_file_path: str):
        self.logs_file_path = logs_file_path
        self.logs_file = open(logs_file_path, "r")
        self._finished = False

    def read_next(self, num_of_lines: int) -> list[str]:
        lines = []

        for _ in range(num_of_lines):
            line = self.logs_file.readline()

            if not line:
                self._finished = True
                break

            lines.append(line.rstrip("\n"))

        return lines

    def is_finished(self) -> bool:
        return self._finished
