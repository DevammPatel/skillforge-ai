import streamlit as st

st.set_page_config(
    page_title="Architecture",
    page_icon="🏗️",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown("""
# 🏗️ SkillForge AI Architecture

### Enterprise Certification Intelligence Platform

*Powered by Azure AI Foundry and Multi-Agent Reasoning*
""")

st.divider()

# --------------------------------------------------
# Overview
# --------------------------------------------------

st.markdown("""
## 🎯 Solution Overview

SkillForge AI is a multi-agent enterprise certification intelligence platform designed to help organizations improve workforce certification readiness.

The platform uses specialized AI agents to analyze learner readiness, curate learning resources, generate adaptive study plans, assess certification preparedness, and provide workforce-level insights to managers.

Each agent performs a focused responsibility while a central orchestrator coordinates the workflow.
""")

st.divider()

# --------------------------------------------------
# High-Level Architecture
# --------------------------------------------------

st.header("🌐 System Architecture")

st.code("""
                     ┌─────────────────────┐
                     │      End User       │
                     │ Employee / Manager  │
                     └──────────┬──────────┘
                                │
                                ▼
                 ┌──────────────────────────────┐
                 │     Workflow Orchestrator    │
                 └──────────┬───────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼

┌────────────────┐  ┌────────────────┐  ┌────────────────┐
│ Learner Profile│  │ Learning       │  │ Study Planner  │
│ Agent          │  │ Curator Agent  │  │ Agent          │
└───────┬────────┘  └───────┬────────┘  └───────┬────────┘
        │                   │                   │
        └───────────┬───────┴───────────┬───────┘
                    ▼                   ▼

         ┌───────────────────────────────┐
         │      Azure AI Foundry         │
         │      Azure OpenAI Models      │
         └──────────────┬────────────────┘
                        │
                        ▼

              ┌───────────────────┐
              │ Knowledge Sources │
              │ • Certification   │
              │ • Team Reports    │
              │ • Workload Data   │
              └───────────────────┘

                        │
                        ▼

┌────────────────┐  ┌────────────────┐
│ Assessment     │  │ Manager        │
│ Agent          │  │ Insights Agent │
└────────────────┘  └────────────────┘
""", language="text")

st.divider()

# --------------------------------------------------
# Agent Layer
# --------------------------------------------------

st.header("🤖 Multi-Agent Layer")

col1, col2 = st.columns(2)

with col1:

    st.success("""
### 👤 Learner Profile Agent

**Responsibility**
- Analyze learner readiness
- Identify certification risks
- Estimate study effort
- Generate readiness scores

**Output**
- Risk Level
- Readiness Score
- Recommended Hours
""")

    st.success("""
### 📚 Learning Curator Agent

**Responsibility**
- Retrieve learning resources
- Recommend certification paths
- Identify required skills

**Output**
- Learning Path
- Skill Roadmap
- Study Sequence
""")

    st.success("""
### 📅 Study Planner Agent

**Responsibility**
- Generate adaptive schedules
- Account for workload constraints
- Optimize study allocation

**Output**
- Weekly Plan
- Daily Tasks
- Milestones
""")

with col2:

    st.success("""
### 📝 Assessment Agent

**Responsibility**
- Generate certification questions
- Evaluate preparedness
- Simulate assessments

**Output**
- MCQs
- Scenario Questions
- Readiness Evaluation
""")

    st.success("""
### 📊 Manager Insights Agent

**Responsibility**
- Workforce intelligence
- Team readiness tracking
- Risk detection

**Output**
- Team Analytics
- Risk Reports
- Manager Actions
""")

st.divider()

# --------------------------------------------------
# Azure AI Foundry
# --------------------------------------------------

st.header("☁️ Azure AI Foundry Integration")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
### Azure OpenAI

- GPT Model Deployment
- Reasoning Generation
- Assessment Creation
- Learning Recommendations
""")

with col2:
    st.info("""
### Knowledge Grounding

- Certification Guides
- Team Reports
- Workload Reports
- Enterprise Data
""")

with col3:
    st.info("""
### Agent Orchestration

- Multi-Agent Workflow
- Context Passing
- Output Aggregation
- Decision Support
""")

st.divider()

# --------------------------------------------------
# Data Flow
# --------------------------------------------------

st.header("🔄 Workflow Execution")

st.markdown("""
### Step 1
Employee submits certification goal and workload details.

⬇️

### Step 2
Learner Profile Agent evaluates readiness and identifies risks.

⬇️

### Step 3
Learning Curator Agent generates a personalized learning path.

⬇️

### Step 4
Study Planner Agent creates an adaptive certification schedule.

⬇️

### Step 5
Assessment Agent generates readiness evaluations.

⬇️

### Step 6
Manager Insights Agent produces workforce recommendations.

⬇️

### Step 7
Results are presented through Employee and Manager Dashboards.
""")

st.divider()

# --------------------------------------------------
# Project Highlights
# --------------------------------------------------

st.header("🏆 Why SkillForge AI?")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "AI Agents",
        "5"
    )

with c2:
    st.metric(
        "Dashboards",
        "2"
    )

with c3:
    st.metric(
        "Azure Services",
        "AI Foundry"
    )

with c4:
    st.metric(
        "Architecture",
        "Multi-Agent"
    )

st.divider()

# --------------------------------------------------
# Business Impact
# --------------------------------------------------

st.header("📈 Business Impact")

st.markdown("""
### For Employees
- Personalized certification guidance
- Adaptive learning schedules
- Improved exam readiness

### For Managers
- Workforce readiness visibility
- Early risk identification
- Better learning resource allocation

### For Organizations
- Increased certification success rates
- Reduced learning inefficiencies
- Data-driven workforce development
""")

st.success(
    "SkillForge AI transforms workforce certification readiness through collaborative AI agents, enterprise knowledge grounding, and intelligent decision support."
)