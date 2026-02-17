import pandas as pd

# Load data
use_cases = pd.read_csv("data/sample_use_cases.csv")
risk_matrix = pd.read_csv("data/risk_scoring_matrix.csv")


def calculate_risk_score(lifecycle_stage, data_type, automation_level):
    score = 0

    # Base risk from data type
    if data_type in ["Personal Data", "Financial Data"]:
        score += 3
    else:
        score += 2

    # Automation impact
    if automation_level == "High":
        score += 2
    elif automation_level == "Medium":
        score += 1

    # Lifecycle adjustment
    if lifecycle_stage == "Deployed":
        score += 2
    elif lifecycle_stage == "In Development":
        score += 1

    return score


# Apply risk scoring
use_cases["calculated_risk_score"] = use_cases.apply(
    lambda row: calculate_risk_score(
        row["lifecycle_stage"],
        row["data_type"],
        row["automation_level"]
    ),
    axis=1
)

print(use_cases[["use_case_id", "calculated_risk_score"]])
