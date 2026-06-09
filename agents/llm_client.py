from openai import AzureOpenAI
from config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_DEPLOYMENT_NAME
)

client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version="2024-02-15-preview",
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

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
You are a Learning Path Curator.

Role:
{role}

Certification:
{certification}

Knowledge:
{knowledge}

Create:

1. Required Skills
2. Learning Path
3. Study Sequence
4. Estimated Duration

Return in markdown.
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