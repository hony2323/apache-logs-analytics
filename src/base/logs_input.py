from src.core.interfaces import ILogsInput


class LogsInput(ILogsInput):
    def __init__(self, logs_file_path: str):
        self.logs_file_path = logs_file_path
        self.logs_file = open(logs_file_path, "r")
        self._finished = False

    def read_next(self, num_of_lines: int) -> list[str]:
        """
        read the next num_of_lines lines from the logs file and return them as a list of strings.
         If the end of the file is reached, set the finished flag to True.
        :param num_of_lines:
        :return:
        """
        lines = []

        for _ in range(num_of_lines):
            line = self.logs_file.readline()

            if not line:
                self._finished = True
                self.logs_file.close()
                break

            lines.append(line.rstrip("\n"))

        return lines

    def is_finished(self) -> bool:
        return self._finished
