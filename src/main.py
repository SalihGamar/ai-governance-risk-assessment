import pandas as pd

# Load sample use cases
use_cases = pd.read_csv("data/sample_use_cases.csv")

# Load risk scoring matrix
risk_matrix = pd.read_csv("data/risk_scoring_matrix.csv")

print("Use Cases Loaded:")
print(use_cases.head())

print("\nRisk Matrix Loaded:")
print(risk_matrix.head())
