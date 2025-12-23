# AI Ethics Checker (Prototype)

**Scores range from 0–10.**  
**Penalties reflect heuristic risk severity.**  
**This tool is intended as a prototype, not a legal compliance engine.**

---

## Overview

The **AI Ethics Checker** is a lightweight, rule-based prototype that evaluates datasets and metadata for potential ethical risks in AI systems.  
It focuses on three key dimensions:  

1. **Fairness** – Checks for imbalance across sensitive attributes (e.g., gender, age, race, caste).  
2. **Transparency** – Verifies availability of essential documentation for model interpretability.  
3. **Accountability** – Assesses responsibility attribution and operational traceability.  

> This tool is meant for **educational and early-stage auditing purposes**.

---

## Folder Structure

ai-ethics-checker/
├── src/
│ └── ai_ethics_checker.py # Main code
├── results/
│ └── sample_output.json # Sample output from running the code
└── README.md # Project description

---

## How to Run

1. **Install dependencies** (only pandas is required):
```bash
pip install pandas
python src/ai_ethics_checker.py
```
---

## View the output

The report will be printed in the console.

A sample output is also available in results/sample_output.json.

---

## Sample Output

{
  "Fairness": {
    "score": 4,
    "flags": ["Potential distribution skew in age", "Imbalance detected in gender"],
    "explanation": "Evaluates imbalance across sensitive attributes using distribution-based heuristics."
  },
  "Transparency": {
    "score": 7,
    "missing": ["model_description", "intended_use"],
    "explanation": "Checks availability of essential documentation for model interpretability."
  },
  "Accountability": {
    "score": 5,
    "missing": ["logging"],
    "explanation": "Assesses responsibility attribution and operational traceability."
  },
  "Overall Score": 5.333333333333333,
  "Meta": {
    "tool_version": "0.1",
    "evaluation_type": "Rule-based prototype",
    "intended_audience": "Educational and early-stage auditing"
  }
}

---

## Notes

The project is self-contained, so no external dataset is required.
The scores are heuristic-based, meant for demonstration and educational purposes.
Future improvements could include:
1. Real datasets in a data/ folder
2. More detailed fairness checks
3. Visualization of results
