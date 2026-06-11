from orchestrator.workflow import (
    SkillForgeWorkflow
)

workflow = SkillForgeWorkflow()

result = workflow.run(
    role="Cloud Engineer",
    certification="AZ-204",
    meeting_hours=22,
    focus_hours=10
)

print(result["profile"])

print("\n")
print(result["analysis"])

print("\n")
print(result["learning_path"])

print("\nSTUDY PLAN\n")

print(result["study_plan"])

print("\nASSESSMENT\n")
print(result["assessment"])

print("\nMANAGER INSIGHTS\n")
print(result["manager_insights"])