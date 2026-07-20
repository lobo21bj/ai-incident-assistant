class IncidentAnalyzer:

    def analyze(self, title: str, logs: str) -> str:
        return (
            f"Incident '{title}' received.\n\n"
            f"Log length: {len(logs)} characters."
        )