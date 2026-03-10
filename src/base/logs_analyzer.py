from src.core.interfaces import ILogsAnalyzer, AnalyzedLogObject, ConvertedLogObject


class LogsAnalyzer(ILogsAnalyzer):
    """
    The LogsAnalyzer class is responsible for analyzing the logs and providing insights based on the parsed and converted log data.
    It can be extended to include various analysis methods such as traffic analysis, error analysis, etc.
    """

    def __init__(self):
        # Initialize any necessary attributes for analysis
        self.countries_counters = {}
        self.browsers_counters = {}
        self.operating_systems_counters = {}


    def add_to_analysis(self, converted_logs: list[ConvertedLogObject]) -> None:
        for log in converted_logs:
            country = log.country
            browser = log.browser
            operating_system = log.operating_system

            if country in self.countries_counters:
                self.countries_counters[country] += 1
            else:
                self.countries_counters[country] = 1

            if browser in self.browsers_counters:
                self.browsers_counters[browser] += 1
            else:
                self.browsers_counters[browser] = 1

            if operating_system in self.operating_systems_counters:
                self.operating_systems_counters[operating_system] += 1
            else:
                self.operating_systems_counters[operating_system] = 1

    def get_analysis(self) -> AnalyzedLogObject:
        pass
