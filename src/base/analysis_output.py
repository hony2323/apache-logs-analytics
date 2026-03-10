from src.core.interfaces import IAnalysisOutput, AnalyzedLogObject


class AnalysisOutput(IAnalysisOutput):
    def submit(self, analysis: AnalyzedLogObject) -> None:
        """"""
        print("County:")
        AnalysisOutput._print_descending(analysis.countries_percentage)
        print("OS:")
        AnalysisOutput._print_descending(analysis.operating_systems_percentage)
        print("Browser:")
        AnalysisOutput._print_descending(analysis.browsers_percentage)

    @staticmethod
    def _print_descending(data: dict[str, float]) -> None:
        for key, value in sorted(data.items(), key=lambda x: x[1], reverse=True):
            print(f"{key}: {value:.2f}%")
