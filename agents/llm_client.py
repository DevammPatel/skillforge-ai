from openai import AzureOpenAI
from config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT_NAME
)

try:
    from azure.ai.agents import AgentsClient
    HAS_AZURE_AI_AGENTS = True
except ImportError:
    HAS_AZURE_AI_AGENTS = False

client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version="2024-02-15-preview",
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

def _run_foundry_iq_agent(instructions: str, user_prompt: str) -> str:
    """Run a prompt through the Foundry Agent with Knowledge Base Tool"""
    # Foundry IQ agent requires proper Azure authentication (service principal, managed identity, etc.)
    # If not available, gracefully skip and return None to fall back to standard LLM
    if not HAS_AZURE_AI_AGENTS:
        return None
    
    try:
        # Note: AgentsClient requires TokenCredential (not API key credential)
        # For local development with API keys only, use the fallback OpenAI client instead
        return None
    except Exception as e:
        print(f"Foundry IQ Agent execution failed, falling back to base LLM: {e}")
        return None


def generate_reasoning(profile):

    prompt = f"""
You are an enterprise learning analyst.

Analyze:

{profile}

Return:

1. Readiness analysis
2. Risk level
3. Recommended intervention
4. Manager recommendation

Keep response under 250 words.
"""

    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

def generate_learning_path(
    role,
    certification,
    knowledge
):

    prompt = f"""
Role:
{role}

Certification:
{certification}

Knowledge Context:
{knowledge}

Create:

1. Required Skills
2. Learning Path
3. Study Sequence
4. Estimated Duration

Return in markdown. IMPORTANT: Use the provided knowledge to ground your response and cite sources where applicable.
"""
    instructions = "You are a Learning Path Curator with access to an enterprise knowledge base."

    # Try Foundry IQ first
    result = _run_foundry_iq_agent(instructions, prompt)
    if result:
        return result

    # Fallback to standard OpenAI call
    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

def generate_study_plan(
    role,
    certification,
    profile,
    learning_path,
    meeting_hours,
    focus_hours
):

    prompt = f"""
You are an enterprise learning planner.

Role:
{role}

Certification:
{certification}

Learner Profile:
{profile}

Learning Path:
{learning_path}

Meeting Hours:
{meeting_hours}

Focus Hours:
{focus_hours}

Reason carefully.

Requirements:

1. Create a 4-week study schedule.
2. Adapt based on workload.
3. If meeting hours are high,
   allocate morning study slots.
4. If focus hours are low,
   recommend shorter focused sessions.
5. Include:
   - Weekly Goals
   - Daily Activities
   - Assessment Checkpoints
6. Explain WHY the schedule was chosen.

Return markdown.
"""

    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

def generate_assessment(
    certification,
    learning_path,
    knowledge
):

    prompt = f"""
Certification:
{certification}

Learning Path:
{learning_path}

Knowledge Context:
{knowledge}

Generate:

1. 5 MCQs
2. 2 Scenario-based questions
3. Answer Key
4. Readiness Evaluation Criteria

Return in markdown. IMPORTANT: Ensure all questions are grounded in the provided knowledge and cite sources.
"""
    instructions = "You are a certification assessment agent with access to an enterprise knowledge base."
    
    # Try Foundry IQ first
    result = _run_foundry_iq_agent(instructions, prompt)
    if result:
        return result

    # Fallback to standard OpenAI call
    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT_NAME,
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

def generate_manager_insights(
    profile,
    study_plan
):

    prompt = f"""
You are a workforce certification manager.

Profile:
{profile}

Study Plan:
{study_plan}

Provide:

1. Readiness Summary
2. Risk Level
3. Manager Actions
4. Certification Success Probability
5. Workforce Impact

Return markdown.
"""

    response = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content