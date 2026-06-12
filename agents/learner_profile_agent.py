import pandas as pd


class LearnerProfileAgent:

    def __init__(self):

        self.workload_data = pd.read_csv(
            "data/workload.csv"
        )

        self.learners_data = pd.read_csv(
            "data/learners.csv"
        )

    # --------------------------------------------------
    # Employee Workflow Analysis
    # --------------------------------------------------

    def analyze(
        self,
        role,
        certification,
        meeting_hours,
        focus_hours
    ):

        readiness_score = 100

        reasoning = []

        if meeting_hours > 20:

            readiness_score -= 20

            reasoning.append(
                "High meeting load reduces study capacity."
            )

        if focus_hours < 15:

            readiness_score -= 15

            reasoning.append(
                "Low focus hours impact learning effectiveness."
            )

        if certification == "AZ-204":

            readiness_score -= 5

            reasoning.append(
                "Certification requires strong hands-on practice."
            )

        readiness_score = max(
            0,
            min(
                100,
                readiness_score
            )
        )

        if readiness_score >= 80:

            risk = "Low"

        elif readiness_score >= 60:

            risk = "Medium"

        else:

            risk = "High"

        return {

            "role": role,

            "certification": certification,

            "risk": risk,

            "readiness_score": readiness_score,

            "recommended_hours": max(
                20,
                int(
                    (100 - readiness_score) * 0.5 + 20
                )
            ),

            "reasoning": reasoning
        }

    # --------------------------------------------------
    # Manager Dashboard Analysis
    # --------------------------------------------------

    def analyze_employee(
        self,
        role,
        certification,
        practice_score,
        study_hours
    ):

        readiness_score = practice_score

        reasoning = []

        if study_hours < 15:

            readiness_score -= 10

            reasoning.append(
                "Insufficient study hours."
            )

        elif study_hours > 25:

            readiness_score += 5

            reasoning.append(
                "Strong study commitment detected."
            )

        if certification == "AZ-204":

            readiness_score -= 5

            reasoning.append(
                "AZ-204 requires additional practical experience."
            )

        readiness_score = max(
            0,
            min(
                100,
                readiness_score
            )
        )

        if readiness_score >= 80:

            risk = "Low"

        elif readiness_score >= 60:

            risk = "Medium"

        else:

            risk = "High"

        pass_probability = min(
            95,
            max(
                20,
                readiness_score
            )
        )

        return {

            "readiness_score": readiness_score,

            "risk": risk,

            "pass_probability": pass_probability,

            "reasoning": reasoning,

            "recommended_hours": max(
                20,
                int(
                    (100 - readiness_score) * 0.5 + 20
                )
            )
        }