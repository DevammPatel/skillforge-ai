import streamlit as st
from orchestrator.demo_trace import generate_trace
from frontend.ui import (
    apply_theme,
    hero,
    readiness_bar,
    section,
    stat_grid,
    workflow_timeline,
)

st.set_page_config(
    page_title="Execution Trace",
    page_icon="⚡",
    layout="wide"
)

apply_theme()

result = generate_trace()

hero(
    "Traceability",
    "Live Multi-Agent Execution Trace",
    "Inspect each agent handoff from learner input through final workforce insight.",
    pills=[
        ("Run mode", "demo trace"),
        ("Agents", "6"),
        ("Status", "complete"),
    ],
)

# =====================================================
# INPUT
# =====================================================

section("Input")

input_data = result["input"]

stat_grid(
    [
        {
            "label": "Role",
            "value": input_data["role"],
            "caption": "Learner persona",
            "tone": "blue",
        },
        {
            "label": "Certification",
            "value": input_data["certification"],
            "caption": "Target credential",
            "tone": "teal",
        },
        {
            "label": "Meetings",
            "value": input_data["meeting_hours"],
            "caption": "Weekly meeting hours",
            "tone": "amber",
        },
        {
            "label": "Focus",
            "value": input_data["focus_hours"],
            "caption": "Weekly focus hours",
            "tone": "green",
        },
    ]
)

# =====================================================
# AGENT 1
# =====================================================

section("Agent 1 - Learner Profile Agent")

stat_grid(
    [
        {
            "label": "Readiness",
            "value": f"{result['profile']['readiness_score']}%",
            "caption": "Profile-derived readiness signal",
            "tone": "teal",
        },
        {
            "label": "Risk",
            "value": result["profile"]["risk"],
            "caption": "Intervention priority for the learner",
            "tone": "amber",
        },
        {
            "label": "Hours",
            "value": result["profile"]["recommended_hours"],
            "caption": "Recommended weekly study effort",
            "tone": "blue",
        },
    ]
)

readiness_bar(result["profile"]["readiness_score"], "Learner readiness")

with st.expander(
    "View Detailed Analysis",
    expanded=True
):
    st.markdown(result["analysis"])

st.markdown('<div class="sf-flow">↓</div>', unsafe_allow_html=True)

# =====================================================
# AGENT 2
# =====================================================

section("Agent 2 - Learning Curator Agent")

with st.expander(
    "Generated Learning Path"
):
    st.markdown(
        result["learning_path"]
    )

st.markdown('<div class="sf-flow">↓</div>', unsafe_allow_html=True)

# =====================================================
# AGENT 3
# =====================================================

section("Agent 3 - Study Planner Agent")

with st.expander(
    "Generated Study Plan"
):
    st.markdown(
        result["study_plan"]
    )

st.markdown('<div class="sf-flow">↓</div>', unsafe_allow_html=True)

# =====================================================
# AGENT 4
# =====================================================

section("Agent 4 - Engagement Agent")

with st.expander(
    "Generated Engagement Plan"
):
    st.markdown(
        result["engagement_plan"]
    )

st.markdown('<div class="sf-flow">↓</div>', unsafe_allow_html=True)

# =====================================================
# AGENT 5
# =====================================================

section("Agent 5 - Assessment Agent")

with st.expander(
    "Generated Assessment"
):
    st.markdown(
        result["assessment"]
    )

st.markdown('<div class="sf-flow">↓</div>', unsafe_allow_html=True)

# =====================================================
# AGENT 6
# =====================================================

section("Agent 6 - Manager Insights Agent")

with st.expander(
    "Generated Manager Recommendations",
    expanded=True
):
    st.markdown(
        result["manager_insights"]
    )

# =====================================================
# EXECUTION SUMMARY
# =====================================================

section("Agent Collaboration Summary")

for step in result["execution_trace"]:

    st.success(
        f"{step['agent']} → {step['output']}"
    )

workflow_timeline(
    [
        (step["agent"], step["output"])
        for step in result["execution_trace"]
    ]
)

# =====================================================
# FINAL OUTCOME
# =====================================================

section("Final Outcome")

st.success("""
SkillForge AI successfully coordinated 6 specialized agents
to analyze learner readiness, generate a personalized learning
path, build an adaptive study schedule, define engagement timing,
assess certification preparedness, and produce manager-level workforce insights.
""")
