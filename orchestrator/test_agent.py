from agents.learner_profile_agent import (
    LearnerProfileAgent
)

from agents.llm_client import (
    generate_reasoning
)

agent = LearnerProfileAgent()

profile = agent.analyze(
    role="Cloud Engineer",
    certification="AZ-204",
    meeting_hours=22,
    focus_hours=10
)

print(profile)

print("\nLLM ANALYSIS\n")

print(generate_reasoning(profile))