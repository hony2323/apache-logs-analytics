from src.base.logs_input import LogsInput
from src.base.logs_parser import ApacheLogsParser


class Facade:
    """
    The Facade class provides a simplified interface to the complex subsystem of log processing.
    It initializes the necessary components and provides a method to start the log processing workflow.
    """

    def __init__(self):
        self.logs_input = LogsInput(
            logs_file_path="src/data/apache_log.txt")  # Todo: make the file path configurable
        self.logs_parser = ApacheLogsParser()
        pass

    def start(self):
        logs = self.logs_input.read_next(5)  # Todo: make the number of lines configurable
        parsed_logs = self.logs_parser.parse(logs)
        for lo in parsed_logs:
            print(lo)
