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
from frontend.ui import (
    apply_theme,
    configure_chart,
    hero,
    insight_cards,
    readiness_bar,
    section,
    stat_grid,
)

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Manager Dashboard",
    page_icon="📊",
    layout="wide"
)

apply_theme()

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

hero(
    "Workforce certification intelligence",
    "Manager Readiness Dashboard",
    (
        "Monitor readiness, risk, study effort, and forecasted pass rates "
        "across the certification pipeline."
    ),
    pills=[
        ("Learners", len(df)),
        ("Avg readiness", f"{df['Readiness'].mean():.0f}%"),
        ("High risk", len(df[df["Risk"] == "High"])),
    ],
)

# --------------------------------------------------
# KPI Cards
# --------------------------------------------------

section("Team Snapshot", "Generated from learner profiles and readiness analysis")

avg_score = df["Readiness"].mean()
high_risk = df[df["Risk"] == "High"]

stat_grid(
    [
        {
            "label": "Average Readiness",
            "value": f"{avg_score:.0f}%",
            "caption": "Across active certification candidates",
            "tone": "teal",
        },
        {
            "label": "High Risk Learners",
            "value": len(high_risk),
            "caption": "Require intervention this sprint",
            "tone": "rose" if len(high_risk) else "green",
        },
        {
            "label": "Candidates",
            "value": len(df),
            "caption": "Learners in this readiness cohort",
            "tone": "blue",
        },
        {
            "label": "Avg Study Hours",
            "value": f"{df['Study Hours'].mean():.0f}",
            "caption": "Reported preparation hours",
            "tone": "amber",
        },
    ]
)

readiness_bar(avg_score, "Team readiness")

# --------------------------------------------------
# Charts Row
# --------------------------------------------------

section("Readiness And Risk", "Compare individuals and overall exposure")

left_col, right_col = st.columns(2)

with left_col:

    fig = px.bar(
        df,
        x="Employee",
        y="Readiness",
        color="Risk",
        title="Employee Readiness Scores",
        text="Readiness",
        color_discrete_map={
            "Low": "#16a34a",
            "Medium": "#d97706",
            "High": "#e11d48",
        },
    )

    fig.update_layout(
        xaxis_title="Employee",
        yaxis_title="Readiness Score"
    )
    fig.update_traces(texttemplate="%{text}%", textposition="outside")
    fig.update_yaxes(range=[0, 105])

    st.plotly_chart(
        configure_chart(fig, height=390),
        width="stretch"
    )

with right_col:

    fig2 = px.pie(
        df,
        names="Risk",
        title="Risk Distribution",
        hole=0.54,
        color="Risk",
        color_discrete_map={
            "Low": "#16a34a",
            "Medium": "#d97706",
            "High": "#e11d48",
        },
    )

    st.plotly_chart(
        configure_chart(fig2, height=390),
        width="stretch"
    )

# --------------------------------------------------
# Certification Breakdown
# --------------------------------------------------

section("Certification Breakdown", "Risk grouped by target credential")

fig3 = px.histogram(
    df,
    x="Certification",
    color="Risk",
    title="Certification Risk Breakdown",
    barmode="group",
    color_discrete_map={
        "Low": "#16a34a",
        "Medium": "#d97706",
        "High": "#e11d48",
    },
)

st.plotly_chart(
    configure_chart(fig3, height=360),
    width="stretch"
)

# --------------------------------------------------
# Team Table
# --------------------------------------------------

section("Team Readiness Overview")

st.dataframe(
    df,
    width="stretch"
)

# --------------------------------------------------
# AI Workforce Insights
# --------------------------------------------------

section("Agent Generated Workforce Insights")

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

    section("High-Risk Learners")

    st.dataframe(
        high_risk,
        width="stretch"
    )

    st.markdown(
        "### Recommended Manager Actions"
    )

    insight_cards(
        [
            {
                "title": "Protect focus time",
                "body": "Reduce meeting load and reserve dedicated certification blocks for high-risk learners.",
            },
            {
                "title": "Add accountability",
                "body": "Assign mentors and schedule weekly readiness reviews until risk drops.",
            },
            {
                "title": "Use targeted checks",
                "body": "Monitor progress with focused assessments tied to the learner's weakest skills.",
            },
        ]
    )

else:

    st.success(
        "No high-risk learners detected."
    )

# --------------------------------------------------
# Certification Forecast
# --------------------------------------------------

section("Certification Forecast")

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

section("Executive Summary")

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
