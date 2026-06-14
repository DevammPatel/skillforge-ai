import streamlit as st
from frontend.ui import (
    apply_theme,
    hero,
    insight_cards,
    section,
    stat_grid,
    workflow_timeline,
)

st.set_page_config(
    page_title="Architecture",
    page_icon="🏗️",
    layout="wide"
)

apply_theme()

# --------------------------------------------------
# Header
# --------------------------------------------------

hero(
    "Azure AI Foundry architecture",
    "SkillForge AI Architecture",
    "A focused multi-agent system for certification planning, assessment, and workforce insight.",
    pills=[
        ("Agents", "6"),
        ("Frontend", "Streamlit"),
        ("Grounding", "knowledge base"),
    ],
)

# --------------------------------------------------
# Overview
# --------------------------------------------------

section("Solution Overview")

st.markdown("""

SkillForge AI is a multi-agent enterprise certification intelligence platform designed to help organizations improve workforce certification readiness.

The platform uses specialized AI agents to analyze learner readiness, curate learning resources, generate adaptive study plans, assess certification preparedness, and provide workforce-level insights to managers.

Each agent performs a focused responsibility while a central orchestrator coordinates the workflow.
""")

# --------------------------------------------------
# High-Level Architecture
# --------------------------------------------------

section("System Architecture")

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

# --------------------------------------------------
# Agent Layer
# --------------------------------------------------

section("Multi-Agent Layer")

insight_cards(
    [
        {
            "title": "Separation of concerns",
            "body": "Each agent owns one certification-intelligence task, keeping outputs focused and inspectable.",
        },
        {
            "title": "Context passing",
            "body": "The orchestrator passes profile, learning path, plan, and assessment context through the workflow.",
        },
        {
            "title": "Dashboard delivery",
            "body": "Outputs are shaped for both learner action and manager intervention.",
        },
    ]
)

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

    st.success("""
### 🔔 Engagement Agent

**Responsibility**
- Adapt reminders to work rhythm
- Respect focus windows
- Define escalation thresholds

**Output**
- Reminder Cadence
- Best Reminder Window
- Privacy-Aware Follow-Up
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

# --------------------------------------------------
# Azure AI Foundry
# --------------------------------------------------

section("Azure AI Foundry Integration")

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

# --------------------------------------------------
# Data Flow
# --------------------------------------------------

section("Workflow Execution")

workflow_timeline(
    [
        (
            "Employee input",
            "The learner submits a certification goal and workload details.",
        ),
        (
            "Readiness analysis",
            "The Learner Profile Agent evaluates readiness and risk.",
        ),
        (
            "Learning path",
            "The Learning Curator Agent generates a grounded study sequence.",
        ),
        (
            "Adaptive plan",
            "The Study Planner Agent creates a workload-aware schedule.",
        ),
        (
            "Assessment",
            "The Assessment Agent generates readiness checks and criteria.",
        ),
        (
            "Manager insight",
            "The Manager Insights Agent produces workforce recommendations.",
        ),
        (
            "Dashboard delivery",
            "Results appear in learner, manager, trace, and analytics pages.",
        ),
    ]
)

# --------------------------------------------------
# Project Highlights
# --------------------------------------------------

section("Why SkillForge AI?")

stat_grid(
    [
        {
            "label": "AI Agents",
            "value": "6",
            "caption": "Specialized reasoning roles",
            "tone": "blue",
        },
        {
            "label": "Dashboards",
            "value": "4",
            "caption": "Learner, manager, trace, and operations views",
            "tone": "teal",
        },
        {
            "label": "Azure Layer",
            "value": "Foundry",
            "caption": "Azure OpenAI-backed intelligence",
            "tone": "amber",
        },
        {
            "label": "Pattern",
            "value": "Multi-agent",
            "caption": "Coordinated orchestration",
            "tone": "green",
        },
    ]
)

# --------------------------------------------------
# Business Impact
# --------------------------------------------------

section("Business Impact")

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
