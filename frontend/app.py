import sys
import os

project_root = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.append(project_root)

import streamlit as st
import plotly.graph_objects as go

from orchestrator.workflow import SkillForgeWorkflow


# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="SkillForge AI",
    page_icon="🚀",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown("""
# 🚀 SkillForge AI

### Enterprise Certification Intelligence Platform

*Powered by Azure AI Foundry Multi-Agent Architecture*
""")

st.divider()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.header("Learner Details")

    role = st.selectbox(
        "Role",
        [
            "Cloud Engineer",
            "DevOps Engineer",
            "Data Engineer"
        ]
    )

    certification = st.selectbox(
        "Certification",
        [
            "AZ-204",
            "AZ-400",
            "DP-203"
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
        use_container_width=True
    )

    st.divider()

    st.subheader("🤖 Multi-Agent Workflow")

    st.markdown("""
✅ Learner Profile Agent

✅ Learning Curator Agent

✅ Study Planner Agent

✅ Assessment Agent

✅ Manager Insights Agent
""")

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

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Readiness Score",
            result["profile"]["readiness_score"]
        )

    with col2:

        risk = result["profile"]["risk"]

        emoji = {
            "Low": "🟢",
            "Medium": "🟡",
            "High": "🔴"
        }

        st.metric(
            "Risk Level",
            f"{emoji.get(risk, '')} {risk}"
        )

    with col3:
        st.metric(
            "Recommended Hours",
            result["profile"]["recommended_hours"]
        )

    st.divider()

    # ----------------------------------------------
    # Gauge Chart
    # ----------------------------------------------

    score = result["profile"]["readiness_score"]

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            title={
                "text": "Certification Readiness"
            },
            gauge={
                "axis": {
                    "range": [0, 100]
                },
                "steps": [
                    {"range": [0, 50]},
                    {"range": [50, 80]},
                    {"range": [80, 100]}
                ]
            }
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    # ----------------------------------------------
    # Main Content Layout
    # ----------------------------------------------

    st.subheader("📚 Learning Path")

    st.markdown(
        result["learning_path"]
    )

    st.divider()

    col_left, col_right = st.columns(2)

    with col_left:

        st.subheader("📅 Study Plan")

        st.markdown(
            result["study_plan"]
        )

    with col_right:

        st.subheader("📝 Assessment")

        st.markdown(
            result["assessment"]
        )

    st.divider()

    st.subheader("📊 Manager Insights")

    st.markdown(
        result["manager_insights"]
    )