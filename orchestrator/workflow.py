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

        # --------------------------------------------------
        # Agent 1: Learner Profile Agent
        # --------------------------------------------------

        profile = self.profile_agent.analyze(
            role,
            certification,
            meeting_hours,
            focus_hours
        )

        profile_analysis = (
            generate_reasoning(profile)
        )

        # --------------------------------------------------
        # Agent 2: Learning Curator Agent
        # --------------------------------------------------

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

        # --------------------------------------------------
        # Agent 3: Study Planner Agent
        # --------------------------------------------------

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

        # --------------------------------------------------
        # Agent 4: Assessment Agent
        # --------------------------------------------------

        assessment = (
            self.assessment_agent
            .create_assessment(
                certification,
                learning_path,
                knowledge
            )
        )

        # --------------------------------------------------
        # Agent 5: Manager Insights Agent
        # --------------------------------------------------

        manager_insights = (
            self.manager_agent.generate(
                profile,
                study_plan
            )
        )

        # --------------------------------------------------
        # Execution Trace
        # --------------------------------------------------

        execution_trace = [

            {
                "agent": "Learner Profile Agent",
                "status": "Completed",
                "output": (
                    f"Readiness Score: "
                    f"{profile['readiness_score']}, "
                    f"Risk: {profile['risk']}"
                )
            },

            {
                "agent": "Learning Curator Agent",
                "status": "Completed",
                "output": (
                    "Generated personalized learning path"
                )
            },

            {
                "agent": "Study Planner Agent",
                "status": "Completed",
                "output": (
                    "Generated adaptive study schedule"
                )
            },

            {
                "agent": "Assessment Agent",
                "status": "Completed",
                "output": (
                    "Generated certification assessment"
                )
            },

            {
                "agent": "Manager Insights Agent",
                "status": "Completed",
                "output": (
                    "Generated workforce recommendations"
                )
            }

        ]

        # --------------------------------------------------
        # Final Workflow Output
        # --------------------------------------------------

        return {

            "input": {

                "role": role,

                "certification": certification,

                "meeting_hours": meeting_hours,

                "focus_hours": focus_hours
            },

            "profile": profile,

            "analysis": profile_analysis,

            "learning_path": learning_path,

            "study_plan": study_plan,

            "assessment": assessment,

            "manager_insights": manager_insights,

            "execution_trace": execution_trace
        }