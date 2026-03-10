import geoip2.database

from src.base.logs_parser import ApacheParsedLog
from src.core.interfaces import ILogsConverter, ConvertedLogObject


class GeoLite2FileLogsConverter(ILogsConverter):
    def __init__(self, geo_lite_2_file_path: str):
        self.geo_lite_2_file_path = geo_lite_2_file_path
        self.reader = geoip2.database.Reader(self.geo_lite_2_file_path)

    def convert(self, parsed_logs: list[ApacheParsedLog]) -> list[ConvertedLogObject]:
        converted_logs = []
        for log in parsed_logs:
            try:
                response = self.reader.country(log.remote_host)
                country = response.country.name
            except Exception as e:
                print(f"Error converting log: {log}. Error: {e}")
                country = "Unknown"
            converted_logs.append(GeoLite2ConvertedLog(parsed_log=log, country=country))
        return converted_logs


class GeoLite2ConvertedLog(ConvertedLogObject):
    def __init__(self, parsed_log: ApacheParsedLog, country: str):
        self.remote_host = parsed_log.remote_host
        self.remote_logname = parsed_log.remote_logname
        self.remote_user = parsed_log.remote_user
        self.request_line = parsed_log.request_line
        self.status = parsed_log.status
        self.bytes_sent = parsed_log.bytes_sent
        self.referer = parsed_log.referer
        self.user_agent = parsed_log.user_agent
        self.country = country

    def __str__(self):
        return (f"Remote Host: {self.remote_host},"
                f" Country: {self.country},"
                f"User Agent: {self.user_agent}"
                )
