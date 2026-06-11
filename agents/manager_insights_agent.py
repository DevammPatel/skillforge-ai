from agents.llm_client import (
    generate_manager_insights
)


class ManagerInsightsAgent:

    def generate(
        self,
        profile,
        study_plan
    ):

        return generate_manager_insights(
            profile,
            study_plan
        )