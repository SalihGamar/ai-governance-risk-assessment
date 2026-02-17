import pandas as pd

# Load data
use_cases = pd.read_csv("data/sample_use_cases.csv")


def classify_ai_capability(description):
    description = description.lower()

    if "resume" in description or "chatbot" in description:
        return "NLP"
    elif "forecast" in description or "fraud" in description:
        return "Prediction"
    elif "anomaly" in description:
        return "Anomaly Detection"
    else:
        return "Other"


def calculate_risk_score(lifecycle_stage, data_type, automation_level):
    score = 0

    # Data sensitivity
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


# Apply AI classification
use_cases["classified_capability"] = use_cases["ai_description"].apply(
    classify_ai_capability
)

# Apply risk scoring
use_cases["calculated_risk_score"] = use_cases.apply(
    lambda row: calculate_risk_score(
        row["lifecycle_stage"],
        row["data_type"],
        row["automation_level"]
    ),
    axis=1
)

print(use_cases[[
    "use_case_id",
    "classified_capability",
    "calculated_risk_score"
]])
