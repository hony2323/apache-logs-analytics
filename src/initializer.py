from src.base.analysis_controller import AnalysisController
from src.base.analysis_output import AnalysisOutput
from src.base.logs_analyzer import LogsAnalyzer
from src.base.logs_converter import GeoLite2FileLogsConverter
from src.base.logs_input import LogsInput
from src.base.logs_parser import ApacheLogsParser

from src.config.general_config import LOGS_FILE_PATH, GEO2_DB_FILE_PATH, NUM_OF_LINES_TO_READ
class Facade:
    """
    The Facade class provides a simplified interface to the complex subsystem of log processing.
    It initializes the necessary components and provides a method to start the log processing workflow.
    """

    def __init__(self):
        self.logs_input = LogsInput(
            logs_file_path=LOGS_FILE_PATH)  # Todo: make the file path configurable
        self.logs_parser = ApacheLogsParser()
        self.logs_converter = GeoLite2FileLogsConverter(GEO2_DB_FILE_PATH)
        self.logs_analyzer = LogsAnalyzer()
        self.analysis_output = AnalysisOutput()
        self.controller = AnalysisController(
            logs_input=self.logs_input,
            logs_parser=self.logs_parser,
            logs_converter=self.logs_converter,
            logs_analyzer=self.logs_analyzer,
            analysis_output=self.analysis_output,
            num_of_lines_to_read=NUM_OF_LINES_TO_READ
        )

    def start(self):
        self.controller.start()
