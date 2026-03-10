import dataclasses
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


@dataclasses.dataclass
class ParsedLogObject:
    remote_host: str
    remote_logname: str
    remote_user: str
    request_line: str
    status: int
    bytes_sent: int
    referer: str
    user_agent: str


@dataclasses.dataclass
class ConvertedLogObject:
    remote_host: str
    remote_logname: str
    remote_user: str
    request_line: str
    status: int
    bytes_sent: int
    referer: str
    user_agent: str
    country: str

    def __str__(self):
        return (f"Remote Host: {self.remote_host},"
                f" Country: {self.country},"
                f"User Agent: {self.user_agent}"
                )


@dataclasses.dataclass
class AnalyzedLogObject:
    pass
