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
# Build Dashboard Dataset
# --------------------------------------------------

results = []

for _, row in raw_df.iterrows():

    readiness = max(
        40,
        min(
            100,
            int(row["practice_score"])
        )
    )

    risk = (
        "High"
        if readiness < 60
        else "Medium"
        if readiness < 80
        else "Low"
    )

    results.append(
        {
            "Employee": row["learner_id"],
            "Role": row["role"],
            "Certification": row["certification"],
            "Readiness": readiness,
            "Risk": risk,
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
    "Monitor certification readiness across the workforce and identify learners who require intervention."
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
# Charts
# --------------------------------------------------

left_col, right_col = st.columns(2)

with left_col:

    fig = px.bar(
        df,
        x="Employee",
        y="Readiness",
        color="Risk",
        title="Employee Readiness Scores"
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
# Team Table
# --------------------------------------------------

st.subheader("👥 Team Readiness")

st.dataframe(
    df,
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# AI Workforce Recommendations
# --------------------------------------------------

high_risk = df[df["Risk"] == "High"]

st.subheader("🤖 AI Workforce Recommendations")

if len(high_risk) > 0:

    st.warning(
        f"{len(high_risk)} learner(s) require immediate attention."
    )

    st.markdown("### Immediate Actions")

    st.markdown("""
- Reduce meeting load for high-risk learners.
- Schedule weekly certification check-ins.
- Assign mentors to struggling candidates.
- Increase protected study time.
- Track readiness improvement weekly.
""")

    st.markdown("### High-Risk Learners")

    for learner in high_risk["Employee"]:
        st.write(f"• {learner}")

else:

    st.success(
        "No high-risk learners detected."
    )

st.markdown("### Certification Forecast")

expected_pass_rate = (
    len(df[df["Readiness"] >= 60])
    / len(df)
) * 100

st.info(
    f"Estimated Certification Pass Rate: {expected_pass_rate:.0f}%"
)