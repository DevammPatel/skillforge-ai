import streamlit as st
from orchestrator.demo_trace import generate_trace

st.set_page_config(
    page_title="Execution Trace",
    page_icon="⚡",
    layout="wide"
)

result = generate_trace()

st.title("⚡ Live Multi-Agent Execution Trace")

st.markdown("""
This page demonstrates how SkillForge AI orchestrates
multiple specialized AI agents to generate certification intelligence.
""")

st.divider()

# =====================================================
# INPUT
# =====================================================

st.header("🎯 Input")

input_data = result["input"]

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Role", input_data["role"])

with c2:
    st.metric(
        "Certification",
        input_data["certification"]
    )

with c3:
    st.metric(
        "Meeting Hours",
        input_data["meeting_hours"]
    )

with c4:
    st.metric(
        "Focus Hours",
        input_data["focus_hours"]
    )

st.divider()

# =====================================================
# AGENT 1
# =====================================================

st.subheader("👤 Agent 1 — Learner Profile Agent")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Readiness Score",
        result["profile"]["readiness_score"]
    )

with col2:
    st.metric(
        "Risk",
        result["profile"]["risk"]
    )

with col3:
    st.metric(
        "Recommended Hours",
        result["profile"]["recommended_hours"]
    )

with st.expander(
    "View Detailed Analysis",
    expanded=True
):
    st.markdown(result["analysis"])

st.markdown("⬇️")

# =====================================================
# AGENT 2
# =====================================================

st.subheader("📚 Agent 2 — Learning Curator Agent")

with st.expander(
    "Generated Learning Path"
):
    st.markdown(
        result["learning_path"]
    )

st.markdown("⬇️")

# =====================================================
# AGENT 3
# =====================================================

st.subheader("📅 Agent 3 — Study Planner Agent")

with st.expander(
    "Generated Study Plan"
):
    st.markdown(
        result["study_plan"]
    )

st.markdown("⬇️")

# =====================================================
# AGENT 4
# =====================================================

st.subheader("📝 Agent 4 — Assessment Agent")

with st.expander(
    "Generated Assessment"
):
    st.markdown(
        result["assessment"]
    )

st.markdown("⬇️")

# =====================================================
# AGENT 5
# =====================================================

st.subheader("📊 Agent 5 — Manager Insights Agent")

with st.expander(
    "Generated Manager Recommendations",
    expanded=True
):
    st.markdown(
        result["manager_insights"]
    )

st.divider()

# =====================================================
# EXECUTION SUMMARY
# =====================================================

st.header("🤖 Agent Collaboration Summary")

for step in result["execution_trace"]:

    st.success(
        f"{step['agent']} → {step['output']}"
    )

st.divider()

# =====================================================
# FINAL OUTCOME
# =====================================================

st.header("🏁 Final Outcome")

st.success("""
SkillForge AI successfully coordinated 5 specialized agents
to analyze learner readiness, generate a personalized learning
path, build an adaptive study schedule, assess certification
preparedness, and produce manager-level workforce insights.
""")