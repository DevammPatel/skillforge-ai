# frontend/pages/manager_dashboard.py

import sys
import os
import pandas as pd
import streamlit as st
import plotly.express as px

# --------------------------------------------------
# Project Path Setup
# --------------------------------------------------

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../.."
    )
)

sys.path.append(project_root)

# --------------------------------------------------
# Imports
# --------------------------------------------------

from agents.learner_profile_agent import (
    LearnerProfileAgent
)

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Manager Dashboard",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# Load Learner Data
# --------------------------------------------------

csv_path = os.path.join(
    project_root,
    "data",
    "learners.csv"
)

raw_df = pd.read_csv(csv_path)

# --------------------------------------------------
# Generate Agent-Based Insights
# --------------------------------------------------

agent = LearnerProfileAgent()

results = []

for _, row in raw_df.iterrows():

    profile = agent.analyze_employee(
        role=row["role"],
        certification=row["certification"],
        practice_score=row["practice_score"],
        study_hours=row["hours_studied"]
    )

    results.append(
        {
            "Employee": row["learner_id"],
            "Role": row["role"],
            "Certification": row["certification"],
            "Readiness": profile["readiness_score"],
            "Risk": profile["risk"],
            "Recommended Hours": profile["recommended_hours"],
            "Study Hours": row["hours_studied"],
            "Exam Outcome": row["exam_outcome"]
        }
    )

df = pd.DataFrame(results)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("📊 Manager Readiness Dashboard")

st.markdown(
    """
Monitor certification readiness across the workforce,
identify risks early, and take proactive action using
AI-generated workforce intelligence.
"""
)

st.divider()

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Average Readiness",
        f"{df['Readiness'].mean():.0f}%"
    )

with col2:
    st.metric(
        "High Risk Learners",
        len(df[df["Risk"] == "High"])
    )

with col3:
    st.metric(
        "Certification Candidates",
        len(df)
    )

with col4:
    st.metric(
        "Average Study Hours",
        f"{df['Study Hours'].mean():.0f}"
    )

st.divider()

# --------------------------------------------------
# Charts Row
# --------------------------------------------------

left_col, right_col = st.columns(2)

with left_col:

    fig = px.bar(
        df,
        x="Employee",
        y="Readiness",
        color="Risk",
        title="Employee Readiness Scores",
        text="Readiness"
    )

    fig.update_layout(
        xaxis_title="Employee",
        yaxis_title="Readiness Score"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right_col:

    fig2 = px.pie(
        df,
        names="Risk",
        title="Risk Distribution"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

st.divider()

# --------------------------------------------------
# Certification Breakdown
# --------------------------------------------------

st.subheader("📚 Certification Risk Distribution")

fig3 = px.histogram(
    df,
    x="Certification",
    color="Risk",
    title="Certification Risk Breakdown",
    barmode="group"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# Team Table
# --------------------------------------------------

st.subheader("👥 Team Readiness Overview")

st.dataframe(
    df,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# AI Workforce Insights
# --------------------------------------------------

st.subheader("🤖 Agent Generated Workforce Insights")

high_risk = df[df["Risk"] == "High"]

avg_score = df["Readiness"].mean()

if avg_score < 75:

    st.warning(
        "Average team readiness is below the target threshold."
    )

else:

    st.success(
        "Average team readiness is within acceptable limits."
    )

# --------------------------------------------------
# High Risk Learners
# --------------------------------------------------

if len(high_risk) > 0:

    st.error(
        f"{len(high_risk)} high-risk learner(s) detected."
    )

    st.markdown("### High-Risk Learners")

    st.dataframe(
        high_risk,
        use_container_width=True
    )

    st.markdown(
        """
### Recommended Manager Actions

- Reduce meeting load for high-risk learners.
- Allocate dedicated study time.
- Assign certification mentors.
- Schedule weekly readiness reviews.
- Monitor progress through targeted assessments.
"""
    )

else:

    st.success(
        "No high-risk learners detected."
    )

# --------------------------------------------------
# Certification Forecast
# --------------------------------------------------

st.markdown("### 📈 Certification Forecast")

expected_pass_rate = (
    len(df[df["Readiness"] >= 60])
    / len(df)
) * 100

st.info(
    f"Estimated Certification Pass Rate: {expected_pass_rate:.0f}%"
)

# --------------------------------------------------
# Executive Summary
# --------------------------------------------------

st.markdown("### 📋 Executive Summary")

st.markdown(
    f"""
- Total Learners Evaluated: **{len(df)}**
- Average Readiness: **{avg_score:.0f}%**
- High Risk Learners: **{len(high_risk)}**
- Estimated Pass Rate: **{expected_pass_rate:.0f}%**

SkillForge AI recommends prioritizing interventions
for high-risk learners while maintaining momentum
for candidates already on track for certification.
"""
)