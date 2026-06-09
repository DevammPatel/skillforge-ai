import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.learning_curator_agent import (
    LearningCuratorAgent
)

from agents.llm_client import (
    generate_learning_path
)

agent = LearningCuratorAgent()

knowledge = agent.get_learning_material()

result = generate_learning_path(
    "Cloud Engineer",
    "AZ-204",
    knowledge
)

print(result)