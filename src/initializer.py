from src.base.logs_input import LogsInput


class Facade:
    def __init__(self):
        self.logs_input = LogsInput(logs_file_path="src/data/apache_log.txt")
        pass
    def start(self):
        pass