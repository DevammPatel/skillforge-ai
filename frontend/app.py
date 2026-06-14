import sys
import os

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.append(project_root)

import streamlit as st
import plotly.graph_objects as go

from orchestrator.workflow import SkillForgeWorkflow
from frontend.ui import (
    agent_list,
    apply_theme,
    callout,
    configure_chart,
    hero,
    insight_cards,
    readiness_bar,
    section,
    sidebar_brand,
    stat_grid,
)


# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="SkillForge AI",
    page_icon="🚀",
    layout="wide"
)

apply_theme()

# --------------------------------------------------
# Header
# --------------------------------------------------

hero(
    "Azure AI Foundry multi-agent platform",
    "SkillForge AI",
    (
        "Turn certification goals, workload constraints, and knowledge sources "
        "into personalized study plans, assessments, and manager-ready insights."
    ),
    pills=[
        ("Planner", "adaptive"),
        ("Assessment", "generated"),
        ("Insights", "manager-ready"),
    ],
)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    sidebar_brand()

    st.header("Learner Profile")

    role = st.selectbox(
        "Role",
        [
            "Cloud Engineer",
            "DevOps Engineer",
            "Data Engineer",
            "Security Engineer"
        ]
    )

    certification = st.selectbox(
        "Certification",
        [
            "AZ-204",
            "AZ-400",
            "DP-203",
            "AZ-500"
        ]
    )

    meeting_hours = st.slider(
        "Meeting Hours",
        0,
        40,
        20
    )

    focus_hours = st.slider(
        "Focus Hours",
        0,
        30,
        15
    )

    run_button = st.button(
        "Generate Plan",
        width="stretch"
    )

    st.divider()

    st.subheader("Agent Workflow")

    agent_list(
        [
            ("Learner Profile Agent", "Readiness and risk analysis"),
            ("Learning Curator Agent", "Knowledge-grounded pathing"),
            ("Study Planner Agent", "Workload-aware scheduling"),
            ("Engagement Agent", "Work-rhythm reminders"),
            ("Assessment Agent", "Practice questions and criteria"),
            ("Manager Insights Agent", "Workforce recommendations"),
        ]
    )

# --------------------------------------------------
# Run Workflow
# --------------------------------------------------

if run_button:

    workflow = SkillForgeWorkflow()

    with st.spinner(
        "Running multi-agent workflow..."
    ):

        result = workflow.run(
            role=role,
            certification=certification,
            meeting_hours=meeting_hours,
            focus_hours=focus_hours
        )

    # ----------------------------------------------
    # KPI Row
    # ----------------------------------------------

    section(
        "Certification Snapshot",
        f"{role} pursuing {certification}"
    )

    risk = result["profile"]["risk"]
    score = result["profile"]["readiness_score"]

    stat_grid(
        [
            {
                "label": "Readiness Score",
                "value": f"{score}%",
                "caption": "Current certification preparedness",
                "tone": "teal",
            },
            {
                "label": "Risk Level",
                "value": risk,
                "caption": "Based on workload and study capacity",
                "tone": "rose" if risk == "High" else "amber" if risk == "Medium" else "green",
            },
            {
                "label": "Recommended Hours",
                "value": result["profile"]["recommended_hours"],
                "caption": "Suggested weekly learning investment",
                "tone": "blue",
            },
        ]
    )

    readiness_bar(score)

    # ----------------------------------------------
    # Gauge Chart
    # ----------------------------------------------

    section(
        "Readiness Signal",
        "Score combines workload, focus capacity, and certification context"
    )

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={
                "text": "Certification Readiness"
            },
            gauge={
                "axis": {
                    "range": [0, 100],
                    "tickwidth": 1,
                    "tickcolor": "#64748b",
                },
                "bar": {"color": "#2563eb"},
                "bgcolor": "white",
                "borderwidth": 1,
                "bordercolor": "#dbe3ef",
                "steps": [
                    {"range": [0, 50], "color": "#fee2e2"},
                    {"range": [50, 80], "color": "#fef3c7"},
                    {"range": [80, 100], "color": "#dcfce7"},
                ],
                "threshold": {
                    "line": {"color": "#0f766e", "width": 4},
                    "thickness": 0.78,
                    "value": 80,
                },
            }
        )
    )

    fig = configure_chart(fig, height=340)

    st.plotly_chart(
        fig,
        width="stretch"
    )

    # ----------------------------------------------
    # Main Content Layout
    # ----------------------------------------------

    section("Learning Path", "Knowledge-grounded skills and sequencing")

    st.markdown(
        result["learning_path"]
    )

    col_left, col_right = st.columns(2)

    with col_left:

        section("Study Plan")

        st.markdown(
            result["study_plan"]
        )

    with col_right:

        section("Engagement")

        st.markdown(
            result["engagement_plan"]
        )

    section("Assessment", "Grounded practice questions and readiness criteria")

    st.markdown(
        result["assessment"]
    )

    section("Manager Insights", "Recommended interventions and success signals")

    st.markdown(
        result["manager_insights"]
    )
else:
    section("Launch A Plan", "Choose a learner profile in the sidebar")

    callout(
        "Ready when you are",
        (
            "Pick a role, certification, meeting load, and focus capacity. "
            "SkillForge will coordinate the agent workflow and return a full readiness plan."
        ),
    )

    insight_cards(
        [
            {
                "title": "Profile first",
                "body": "The learner profile agent turns workload and focus capacity into a readiness signal.",
            },
            {
                "title": "Plan with constraints",
                "body": "The study planner adapts learning time around meetings and available focus hours.",
            },
            {
                "title": "Manager-ready output",
                "body": "The final response includes interventions, assessment content, and workforce guidance.",
            },
        ]
    )
