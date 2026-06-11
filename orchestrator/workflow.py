from agents.learner_profile_agent import (
    LearnerProfileAgent
)

from agents.learning_curator_agent import (
    LearningCuratorAgent
)

from agents.study_planner_agent import (
    StudyPlannerAgent
)

from agents.assessment_agent import (
    AssessmentAgent
)

from agents.manager_insights_agent import (
    ManagerInsightsAgent
)

from agents.llm_client import (
    generate_reasoning,
    generate_learning_path
)

class SkillForgeWorkflow:

    def __init__(self):

        self.profile_agent = (
            LearnerProfileAgent()
        )

        self.curator_agent = (
            LearningCuratorAgent()
        )

        self.study_planner = (
            StudyPlannerAgent()
        )

        self.assessment_agent = (
            AssessmentAgent()
        )

        self.manager_agent = (
            ManagerInsightsAgent()
        )

    def run(
        self,
        role,
        certification,
        meeting_hours,
        focus_hours
    ):

        profile = self.profile_agent.analyze(
            role,
            certification,
            meeting_hours,
            focus_hours
        )

        profile_analysis = (
            generate_reasoning(profile)
        )

        knowledge = (
            self.curator_agent
            .get_learning_material()
        )

        learning_path = (
            generate_learning_path(
                role,
                certification,
                knowledge
            )
        )

        study_plan = (
            self.study_planner.create_plan(
                role,
                certification,
                profile,
                learning_path,
                meeting_hours,
                focus_hours
            )
        )       

        assessment = (
            self.assessment_agent
                .create_assessment(
                certification,
                learning_path,
                knowledge
            )
        )

        manager_insights = (
            self.manager_agent.generate(
            profile,
            study_plan
            )
        )

        return {
            "profile": profile,
            "analysis": profile_analysis,
            "learning_path": learning_path,
            "study_plan": study_plan,
            "assessment": assessment,
            "manager_insights": manager_insights
        }