"""
Scores range from 0–10.
Penalties reflect heuristic risk severity.
The system is intended as a prototype, not a legal compliance engine.
"""

import pandas as pd

class AIEthicsChecker:
    def __init__(self, dataset, metadata):
        self.dataset = dataset
        self.metadata = metadata
        self.report = {}

    def fairness_check(self):
        sensitive_attrs = ["gender", "age", "race", "caste"]
        found = [col for col in self.dataset.columns if col.lower() in sensitive_attrs]

        score = 10
        flags = []

        if found:
            for attr in found:
                if pd.api.types.is_numeric_dtype(self.dataset[attr]):
                    if self.dataset[attr].std() > 10:
                        score -= 3
                        flags.append(f"Potential distribution skew in {attr}")
                else:
                    ratio = self.dataset[attr].value_counts(normalize=True)
                    if ratio.min() < 0.2:
                        score -= 3
                        flags.append(f"Imbalance detected in {attr}")

        score = max(score, 0)

        self.report["Fairness"] = {
            "score": score,
            "flags": flags,
            "explanation": "Evaluates imbalance across sensitive attributes using distribution-based heuristics."
        }

    def transparency_check(self):
        required_fields = ["model_description", "dataset_source", "intended_use"]
        score = 10
        missing = []

        for field in required_fields:
            if field not in self.metadata:
                score -= 3
                missing.append(field)

        score = max(score, 0)

        self.report["Transparency"] = {
            "score": score,
            "missing": missing,
            "explanation": "Checks availability of essential documentation for model interpretability."
        }

    def accountability_check(self):
        score = 10
        missing = []

        if "owner" not in self.metadata:
            score -= 5
            missing.append("owner")

        if "logging" not in self.metadata:
            score -= 5
            missing.append("logging")

        score = max(score, 0)

        self.report["Accountability"] = {
            "score": score,
            "missing": missing,
            "explanation": "Assesses responsibility attribution and operational traceability."
        }

    def generate_report(self):
        self.fairness_check()
        self.transparency_check()
        self.accountability_check()

        total = sum(section["score"] for section in self.report.values())
        self.report["Overall Score"] = total / 3
        self.report["Meta"] = {
            "tool_version": "0.1",
            "evaluation_type": "Rule-based prototype",
            "intended_audience": "Educational and early-stage auditing"
        }

        return self.report


if __name__ == "__main__":
    data = {
        "gender": ["Male"] * 9 + ["Female"],
        "age": [25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
    }

    df = pd.DataFrame(data)

    metadata = {
        "dataset_source": "Unknown source",
        "owner": "AI Team"
    }

    checker = AIEthicsChecker(df, metadata)
    report = checker.generate_report()

    print(report)

