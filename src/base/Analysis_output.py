from src.core.interfaces import IAnalysisOutput, AnalyzedLogObject


class AnalysisOutput(IAnalysisOutput):
    def submit(self, analysis: AnalyzedLogObject) -> None:
        pass