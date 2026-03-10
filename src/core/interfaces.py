from abc import ABC, abstractmethod


class IAnalysisController(ABC):
    @abstractmethod
    def __init__(self, logs_input: ILogsInput, logs_parser: ILogsParser, logs_converter: ILogsConverter,
                 logs_analyzer: ILogsAnalyzer, analysis_output: IAnalysisOutput):
        pass
    @abstractmethod
    def start(self) -> None:
        pass


class ILogsInput(ABC):
    @abstractmethod
    def read_next(self, num_of_lines: int) -> list[str]:
        pass

    @abstractmethod
    def is_finished(self) -> bool:
        pass


class ILogsParser(ABC):
    @abstractmethod
    def parse(self, raw_logs: list[str]) -> list[ParsedLogObject]:
        pass


class ILogsConverter(ABC):
    @abstractmethod
    def convert(self, parsed_logs: list[ParsedLogObject]) -> list[ConvertedLogObject]:
        pass


class ILogsAnalyzer(ABC):
    @abstractmethod
    def add_to_analysis(self, converted_logs: list[ConvertedLogObject]) -> None:
        pass

    @abstractmethod
    def get_analysis(self) -> AnalyzedLogObject:
        pass


class IAnalysisOutput(ABC):
    @abstractmethod
    def submit(self, analysis: AnalyzedLogObject) -> None:
        pass


class ParsedLogObject(ABC):
    pass


class ConvertedLogObject(ABC):
    pass


class AnalyzedLogObject(ABC):
    pass
