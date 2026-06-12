from orchestrator.workflow import SkillForgeWorkflow


def generate_trace():

    workflow = SkillForgeWorkflow()

    result = workflow.run(
        role="Cloud Engineer",
        certification="AZ-204",
        meeting_hours=22,
        focus_hours=10
    )

    return result