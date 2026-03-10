from user_agents import parse

import geoip2.database

from src.core.interfaces import ILogsConverter, ConvertedLogObject, ParsedLogObject


class GeoLite2FileLogsConverter(ILogsConverter):
    def __init__(self, geo_lite_2_file_path: str):
        self.geo_lite_2_file_path = geo_lite_2_file_path
        self.reader = geoip2.database.Reader(self.geo_lite_2_file_path)

    def convert(self, parsed_logs: list[ParsedLogObject]) -> list[ConvertedLogObject]:
        converted_logs = []
        for log in parsed_logs:
            try:
                response = self.reader.country(log.remote_host)
                country = response.country.name
            except Exception as e:
                print(f"Error converting log: {log}. Error: {e}")
                country = "Unknown"
            try:
                user_agent = parse(log.user_agent)
                browser = user_agent.browser.family
                operating_system = user_agent.os.family
            except Exception as e:
                print(f"Error parsing user agent: {log.user_agent}. Error: {e}")
                browser = "Unknown"
                operating_system = "Unknown"
            converted_logs.append(ConvertedLogObject(
                remote_host=log.remote_host,
                remote_logname=log.remote_logname,
                remote_user=log.remote_user,
                request_line=log.request_line,
                status=log.status,
                bytes_sent=log.bytes_sent,
                referer=log.referer,
                user_agent=log.user_agent,
                country=country,
                operating_system=operating_system,
                browser=browser
            ))
        return converted_logs
