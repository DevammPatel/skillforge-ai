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

client = None

if (
    AZURE_OPENAI_ENDPOINT
    and AZURE_OPENAI_API_KEY
    and AZURE_OPENAI_DEPLOYMENT_NAME
):
    client = AzureOpenAI(
        api_key=AZURE_OPENAI_API_KEY,
        api_version="2024-02-15-preview",
        azure_endpoint=AZURE_OPENAI_ENDPOINT
    )


def _chat_completion(messages):
    if client is None:
        return None

    try:
        response = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT_NAME,
            messages=messages
        )
        return response.choices[0].message.content

    except Exception as exc:
        print(
            "Azure OpenAI call failed; using deterministic demo fallback: "
            f"{exc}"
        )
        return None

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

    response = _chat_completion(
        [
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    if response:
        return response

    reasons = profile.get("reasoning") or [
        "The learner profile was evaluated using workload and certification context."
    ]

    return f"""
1. **Readiness analysis:** The learner has a readiness score of **{profile['readiness_score']}%** for **{profile['certification']}**.
2. **Risk level:** Current risk is **{profile['risk']}**.
3. **Recommended intervention:** {' '.join(reasons)}
4. **Manager recommendation:** Protect focus time and track weekly assessment checkpoints until readiness improves.
"""

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
    response = _chat_completion(
        [
            {"role": "system", "content": instructions},
            {"role": "user", "content": prompt}
        ]
    )

    if response:
        return response

    return f"""
## Required Skills
- Review the role-aligned certification skills for **{role}** and **{certification}**.
- Focus on implementation practice, service configuration, monitoring, and exam-style scenario analysis.

## Learning Path
1. Read the synthetic Engineering Certification Enablement Guide.
2. Study the certification-specific skill areas from the approved knowledge base.
3. Complete weekly practice checkpoints and review weak areas.
4. Take a final mock assessment 3 days before the exam.

## Study Sequence
- **Week 1:** Certification overview, core services, and role mapping.
- **Week 2:** Hands-on labs and applied service configuration.
- **Week 3:** Scenario practice and troubleshooting drills.
- **Week 4:** Mock exam, revision, and readiness review.

## Estimated Duration
Use the recommended study hours from the certification guide and adjust based on workload.

**Sources:** Engineering Certification Enablement Guide (Synthetic), Workload and Learning Correlation, Quarterly Learning Report.
"""

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

    response = _chat_completion(
        [
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    if response:
        return response

    session_length = (
        "45-minute focused sessions"
        if focus_hours < 15
        else "60-90 minute focused sessions"
    )
    preferred_slot = (
        "morning"
        if meeting_hours > 20
        else "the learner's highest-focus window"
    )

    return f"""
## 4-Week Study Plan

**Why this schedule:** The learner has **{meeting_hours} meeting hours** and **{focus_hours} focus hours**, so the plan uses {session_length} in {preferred_slot} blocks.

### Week 1
- Confirm exam objectives for **{certification}**.
- Complete baseline review and identify weak skill areas.
- Schedule 3 study blocks and 1 checkpoint.

### Week 2
- Complete hands-on labs for the highest-priority skills.
- Use short recall checks after each session.
- Review missed practice questions.

### Week 3
- Practice scenario-based questions.
- Run a timed mini-assessment.
- Rebalance study time toward weak areas.

### Week 4
- Complete a final mock exam.
- Review incorrect answers.
- Prepare exam-day checklist and next-step recommendation.
"""

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
    response = _chat_completion(
        [
            {"role": "system", "content": instructions},
            {"role": "user", "content": prompt}
        ]
    )

    if response:
        return response

    return f"""
## Grounded Practice Assessment

### MCQs
1. Which study pattern is recommended for certification readiness?
   - A. One long session only
   - B. 1-2 hours of focused daily study
   - C. No practice assessments
   - D. Final review only

2. What practice score threshold should learners target before attempting the exam?
   - A. Below 50%
   - B. Around 60%
   - C. At least 75% or role-specific threshold
   - D. Score is not relevant

3. What workload signal can reduce study completion?
   - A. More than 20 meeting hours per week
   - B. At least 15 focus hours
   - C. Weekly checkpoints
   - D. Final mock exam

4. What should the learner do before moving forward?
   - A. Ignore weak areas
   - B. Review weak areas
   - C. Skip assessments
   - D. Stop studying after week one

5. What improves certification success according to the team report?
   - A. More than 20 study hours and practice score above 75
   - B. No study plan
   - C. High meeting load
   - D. Random scheduling

### Scenario Questions
1. A learner has 25 meeting hours and 8 focus hours. Recommend a study adjustment.
2. A learner scores 68% on practice checks. Explain whether they should take the exam or loop back into preparation.

### Answer Key
1. B
2. C
3. A
4. B
5. A

### Readiness Evaluation Criteria
- Ready: practice score meets the target threshold and weak areas are reviewed.
- Needs preparation: high meeting load, low focus time, or practice score below threshold.

**Sources:** Engineering Certification Enablement Guide (Synthetic), Workload and Learning Correlation, Quarterly Learning Report.
"""

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

    response = _chat_completion(
        [
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    if response:
        return response

    return f"""
## Readiness Summary
The learner is currently marked **{profile['risk']} risk** with a readiness score of **{profile['readiness_score']}%**.

## Manager Actions
- Protect recurring focus blocks for certification study.
- Review progress weekly using practice checkpoints.
- Assign mentor support if readiness remains below target.

## Certification Success Probability
Estimated success probability is aligned to the readiness score and should improve as weak areas are remediated.

## Workforce Impact
Reducing meeting pressure and using targeted study windows can improve certification throughput without disrupting delivery work.
"""
