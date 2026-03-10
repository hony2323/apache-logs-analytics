from src.base.analysis_output import AnalysisOutput
from src.base.logs_analyzer import LogsAnalyzer
from src.base.logs_converter import GeoLite2FileLogsConverter
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
        self.logs_converter = GeoLite2FileLogsConverter("src/data/GeoLite2-Country.mmdb")
        self.logs_analyzer = LogsAnalyzer()
        self.analysis_output = AnalysisOutput()

    def start(self):
        logs = self.logs_input.read_next(115)  # Todo: make the number of lines configurable
        parsed_logs = self.logs_parser.parse(logs)
        converted_logs = self.logs_converter.convert(parsed_logs)
        self.logs_analyzer.add_to_analysis(converted_logs)
        self.analysis_output.submit(self.logs_analyzer.get_analysis())