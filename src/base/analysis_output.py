from src.core.interfaces import IAnalysisOutput, AnalyzedLogObject


class AnalysisOutput(IAnalysisOutput):
    def submit(self, analysis: AnalyzedLogObject) -> None:
        print("Countries percentage:")
        for country, percentage in analysis.countries_percentage.items():
            print(f"{country}: {percentage:.2f}%")
        print("Browsers percentage:")
        for browser, percentage in analysis.browsers_percentage.items():
            print(f"{browser}: {percentage:.2f}%")
        print("Operating systems percentage:")
        for operating_system, percentage in analysis.operating_systems_percentage.items():
            print(f"{operating_system}: {percentage:.2f}%")
