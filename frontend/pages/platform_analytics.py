import streamlit as st
import pandas as pd
import plotly.express as px
import random

st.set_page_config(
    page_title="Platform Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Platform Analytics")

st.markdown("""
Operational visibility into SkillForge AI's multi-agent platform.
""")

st.divider()

# =====================================================
# PLATFORM KPIs
# =====================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Learners Processed",
        "245"
    )

with col2:
    st.metric(
        "Learning Plans Generated",
        "198"
    )

with col3:
    st.metric(
        "Assessments Generated",
        "612"
    )

with col4:
    st.metric(
        "Average Readiness",
        "78%"
    )

st.divider()

# =====================================================
# AGENT HEALTH
# =====================================================

st.header("🤖 Agent Health")

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
    use_container_width=True
)

st.divider()

# =====================================================
# RESPONSE TIME CHART
# =====================================================

st.header("⚡ Agent Response Times")

fig = px.bar(
    health_df,
    x="Agent",
    y="Avg Response Time (s)",
    title="Average Agent Response Time"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# =====================================================
# PLATFORM LOAD
# =====================================================

st.header("📊 Daily Workflow Volume")

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
    fig2,
    use_container_width=True
)

st.divider()

# =====================================================
# PLATFORM INSIGHTS
# =====================================================

st.header("🧠 Platform Insights")

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