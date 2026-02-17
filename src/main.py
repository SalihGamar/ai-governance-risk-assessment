import pandas as pd

# Load dataset
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

    if data_type in ["Personal Data", "Financial Data"]:
        score += 3
    else:
        score += 2

    if automation_level == "High":
        score += 2
    elif automation_level == "Medium":
        score += 1

    if lifecycle_stage == "Deployed":
        score += 2
    elif lifecycle_stage == "In Development":
        score += 1

    return score


def governance_decision(score, lifecycle_stage):
    if score >= 6 and lifecycle_stage == "Deployed":
        return "Escalate - Immediate Risk Review Required"
    elif score >= 5:
        return "Review - Governance Controls Needed"
    else:
        return "Approve - Risk Acceptable with Monitoring"


use_cases["classified_capability"] = use_cases["ai_description"].apply(
    classify_ai_capability
)

use_cases["calculated_risk_score"] = use_cases.apply(
    lambda row: calculate_risk_score(
        row["lifecycle_stage"],
        row["data_type"],
        row["automation_level"]
    ),
    axis=1
)

use_cases["governance_decision"] = use_cases.apply(
    lambda row: governance_decision(
        row["calculated_risk_score"],
        row["lifecycle_stage"]
    ),
    axis=1
)

print("\nAI Governance Assessment Results\n")
print("-" * 50)

for index, row in use_cases.iterrows():
    print(f"Use Case: {row['use_case_id']}")
    print(f"Capability: {row['classified_capability']}")
    print(f"Risk Score: {row['calculated_risk_score']}")
    print(f"Decision: {row['governance_decision']}")
    print("-" * 50)

]])
