from agents.llm_client import (
    generate_assessment
)


class AssessmentAgent:

    def create_assessment(
        self,
        certification,
        learning_path,
        knowledge
    ):

        return generate_assessment(
            certification,
            learning_path,
            knowledge
        )