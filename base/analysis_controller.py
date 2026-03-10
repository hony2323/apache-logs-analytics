from core.interfaces import IAnalysisController, ILogsInput, ILogsParser, ILogsConverter, ILogsAnalyzer, IAnalysisOutput


class AnalysisController(IAnalysisController):
    def __init__(self, logs_input: ILogsInput, logs_parser: ILogsParser, logs_converter: ILogsConverter,
                 logs_analyzer: ILogsAnalyzer, analysis_output: IAnalysisOutput):
        self.logs_input = logs_input
        self.logs_parser = logs_parser
        self.logs_converter = logs_converter
        self.logs_analyzer = logs_analyzer
        self.analysis_output = analysis_output

    def start(self) -> None:
        while not self.logs_input.is_finished():
            raw_logs = self.logs_input.read_next(100)
            parsed_logs = self.logs_parser.parse(raw_logs)
            converted_logs = self.logs_converter.convert(parsed_logs)
            self.logs_analyzer.add_to_analysis(converted_logs)
        analysis = self.logs_analyzer.get_analysis()
        self.analysis_output.submit(analysis)
