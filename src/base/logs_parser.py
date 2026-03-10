from datetime import datetime
from dataclasses import dataclass

from src.core.interfaces import ILogsParser, ParsedLogObject
from apachelogs import LogParser


class ApacheLogsParser(ILogsParser):
    def __init__(self):
        self.logs_format = '%h %l %u %t "%r" %>s %b "%{Referer}i" "%{User-Agent}i"'
        self.parser = LogParser(self.logs_format)

    def parse(self, raw_logs: list[str]) -> list[ParsedLogObject]:
        """
        Parse the raw logs using the apachelogs library and return a list of ParsedLogObject.
        :param raw_logs:
        :return:
        """
        parsed_lines = []
        for line in raw_logs:
            try:
                parsed_line = self.parser.parse(line)
                parsed_lines.append(ApacheParsedLog(
                    remote_host=parsed_line.remote_host,
                    remote_logname=parsed_line.remote_logname,
                    remote_user=parsed_line.remote_user,
                    request_line=parsed_line.request_line,
                    status=parsed_line.final_status,
                    bytes_sent=parsed_line.bytes_sent,
                    referer=parsed_line.headers_in.get("Referer", ""),
                    user_agent=parsed_line.headers_in.get("User-Agent", "")
                ))
            except Exception as e:
                print(f"Error parsing line: {line}. Error: {e}")
        return parsed_lines


@dataclass
class ApacheParsedLog(ParsedLogObject):
    remote_host: str
    remote_logname: str
    remote_user: str
    request_line: str
    status: int
    bytes_sent: int
    referer: str
    user_agent: str
