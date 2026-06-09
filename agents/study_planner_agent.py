from agents.llm_client import (
    generate_study_plan
)


class StudyPlannerAgent:

    def create_plan(
        self,
        role,
        certification,
        profile,
        learning_path,
        meeting_hours,
        focus_hours
    ):

        return generate_study_plan(
            role,
            certification,
            profile,
            learning_path,
            meeting_hours,
            focus_hours
        )