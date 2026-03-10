from core.interfaces import ILogsInput


class LogsInput(ILogsInput):
    def __init__(self):
        pass

    def read_next(self, num_of_lines: int) -> list[str]:
        return []

    def is_finished(self) -> bool:
        return True
