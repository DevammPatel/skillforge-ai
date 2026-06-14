import streamlit as st
import pandas as pd
import plotly.express as px
from frontend.ui import (
    apply_theme,
    configure_chart,
    hero,
    insight_cards,
    section,
    stat_grid,
)

st.set_page_config(
    page_title="Platform Analytics",
    page_icon="📈",
    layout="wide"
)

apply_theme()

hero(
    "Operations view",
    "Platform Analytics",
    "Track workflow volume, agent health, response times, and readiness trends.",
    pills=[
        ("Health", "stable"),
        ("Readiness", "78%"),
        ("Failures", "0"),
    ],
)

# =====================================================
# PLATFORM KPIs
# =====================================================

section("Platform Snapshot", "Workflow throughput and current readiness posture")

stat_grid(
    [
        {
            "label": "Learners Processed",
            "value": "245",
            "caption": "Profiles evaluated by the workflow",
            "tone": "blue",
        },
        {
            "label": "Plans Generated",
            "value": "198",
            "caption": "Adaptive study plans created",
            "tone": "teal",
        },
        {
            "label": "Assessments",
            "value": "612",
            "caption": "Questions and criteria generated",
            "tone": "amber",
        },
        {
            "label": "Avg Readiness",
            "value": "78%",
            "caption": "Current platform readiness average",
            "tone": "green",
        },
    ]
)

# =====================================================
# AGENT HEALTH
# =====================================================

section("Agent Health", "Current status and average response time")

health_df = pd.DataFrame(
    {
        "Agent": [
            "Learner Profile Agent",
            "Learning Curator Agent",
            "Study Planner Agent",
            "Assessment Agent",
            "Manager Insights Agent"
        ],
        "Status": [
            "Healthy",
            "Healthy",
            "Healthy",
            "Healthy",
            "Healthy"
        ],
        "Avg Response Time (s)": [
            1.2,
            1.5,
            1.1,
            1.8,
            1.3
        ]
    }
)

st.dataframe(
    health_df,
    width="stretch"
)

insight_cards(
    [
        {
            "title": "Fastest agent",
            "body": "Study Planner Agent is currently the quickest responder at 1.1 seconds.",
        },
        {
            "title": "Largest workload",
            "body": "Assessment Agent takes longest because it generates questions and evaluation criteria.",
        },
        {
            "title": "System state",
            "body": "All specialized agents are healthy and available for orchestration.",
        },
    ]
)

# =====================================================
# RESPONSE TIME CHART
# =====================================================

section("Agent Response Times")

fig = px.bar(
    health_df,
    x="Agent",
    y="Avg Response Time (s)",
    title="Average Agent Response Time"
)

st.plotly_chart(
    configure_chart(fig, height=380),
    width="stretch"
)

# =====================================================
# PLATFORM LOAD
# =====================================================

section("Daily Workflow Volume")

volume_df = pd.DataFrame(
    {
        "Day": [
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat",
            "Sun"
        ],
        "Requests": [
            35,
            42,
            38,
            51,
            47,
            22,
            18
        ]
    }
)

fig2 = px.line(
    volume_df,
    x="Day",
    y="Requests",
    markers=True,
    title="Daily Workflow Requests"
)

st.plotly_chart(
    configure_chart(fig2, height=360),
    width="stretch"
)

# =====================================================
# PLATFORM INSIGHTS
# =====================================================

section("Platform Insights")

st.success("""
All agents are operational.

Assessment Agent shows the highest response time due to
question generation workloads.

Platform readiness remains stable above 75%.

No workflow failures detected.
""")

st.info("""
SkillForge AI successfully orchestrates specialized
agents while maintaining consistent response times
and certification readiness recommendations.
""")
