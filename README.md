# 🚀 SkillForge AI

### Enterprise Certification Intelligence Platform powered by Azure AI Foundry

SkillForge AI is a multi-agent enterprise certification intelligence platform designed to improve workforce certification readiness through intelligent planning, adaptive learning, assessment generation, and workforce-level insights.

Built for the **Microsoft Agents League Hackathon**, SkillForge AI leverages **Azure AI Foundry**, **Azure OpenAI**, and a collaborative **multi-agent architecture** to transform how organizations prepare employees for professional certifications.

---

# 🎯 Problem Statement

Organizations invest heavily in employee certifications, yet many learners struggle due to:

* Heavy meeting schedules
* Lack of personalized study plans
* Poor visibility into readiness levels
* Static learning recommendations
* Limited manager insights

Existing learning systems often provide generic recommendations and fail to adapt to individual workloads and organizational constraints.

---

# 💡 Solution

SkillForge AI uses multiple specialized AI agents that collaborate to:

* Analyze learner readiness
* Curate learning resources
* Generate adaptive study plans
* Create certification assessments
* Provide workforce-level manager insights

The result is a personalized and data-driven certification readiness platform.

---

# 🏗️ Architecture

```text
Employee / Manager
        │
        ▼

Workflow Orchestrator

 ├── Learner Profile Agent
 ├── Learning Curator Agent
 ├── Study Planner Agent
 ├── Assessment Agent
 └── Manager Insights Agent

        │

        ▼

 Azure AI Foundry
 Azure OpenAI Models

        │

        ▼

 Enterprise Knowledge Sources

        │

        ▼

 Employee & Manager Dashboards
```

---

# 🤖 Multi-Agent System

## 1. Learner Profile Agent

Responsibilities:

* Readiness analysis
* Risk identification
* Study effort estimation

Outputs:

* Readiness Score
* Risk Level
* Recommended Study Hours

---

## 2. Learning Curator Agent

Responsibilities:

* Knowledge retrieval
* Learning path generation
* Skill gap identification

Outputs:

* Personalized Learning Path
* Recommended Skills
* Study Sequence

---

## 3. Study Planner Agent

Responsibilities:

* Adaptive schedule generation
* Workload-aware planning
* Milestone creation

Outputs:

* Weekly Study Plan
* Daily Learning Schedule
* Learning Milestones

---

## 4. Assessment Agent

Responsibilities:

* Certification question generation
* Readiness evaluation
* Knowledge validation

Outputs:

* MCQs
* Scenario-Based Questions
* Assessment Criteria

---

## 5. Manager Insights Agent

Responsibilities:

* Workforce intelligence
* Risk detection
* Certification forecasting

Outputs:

* Team Readiness Analytics
* Risk Reports
* Manager Recommendations

---

# ☁️ Azure AI Foundry Integration

SkillForge AI uses Azure AI Foundry for:

* Multi-agent reasoning
* Azure OpenAI model deployment
* Enterprise-grade AI orchestration
* Knowledge-grounded recommendations
* Assessment generation

---

# 📊 Key Features

### Employee Dashboard

* Certification readiness score
* Personalized learning path
* Adaptive study plan
* AI-generated assessments
* Certification guidance

### Manager Dashboard

* Team readiness monitoring
* Risk distribution analysis
* Workforce recommendations
* Certification forecasting
* Resource planning insights

### Execution Trace

* Transparent multi-agent workflow
* Agent-by-agent reasoning visibility
* Workflow traceability

### Platform Analytics

* Agent health monitoring
* Platform performance metrics
* Workflow volume analytics
* Operational visibility

---

# 📈 Business Impact

## For Employees

* Personalized learning journeys
* Better certification readiness
* Adaptive study schedules

## For Managers

* Early risk identification
* Improved workforce planning
* Better resource allocation

## For Organizations

* Higher certification success rates
* Reduced training inefficiencies
* Data-driven workforce development

---

# 🛠️ Technology Stack

### AI & Agents

* Azure AI Foundry
* Azure OpenAI
* Multi-Agent Architecture

### Backend

* Python
* Custom Agent Orchestration

### Frontend

* Streamlit

### Data & Analytics

* Pandas
* Plotly

---

# 📂 Project Structure

```text
SkillForge-AI

├── agents
│   ├── learner_profile_agent.py
│   ├── learning_curator_agent.py
│   ├── study_planner_agent.py
│   ├── assessment_agent.py
│   ├── manager_insights_agent.py
│   └── llm_client.py
│
├── orchestrator
│   ├── workflow.py
│   └── demo_trace.py
│
├── frontend
│   ├── app.py
│   └── pages
│       ├── manager_dashboard.py
│       ├── architecture.py
│       ├── execution_trace.py
│       └── platform_analytics.py
│
├── data
│
├── knowledge_base
│
└── requirements.txt
```

---

# 🚀 Running the Application

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file:

```env
AZURE_OPENAI_ENDPOINT=your_endpoint
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment
```

## Launch Streamlit

```bash
streamlit run frontend/app.py
```

---

# 🎥 Demo Workflow

1. Enter employee profile details.
2. Generate certification readiness analysis.
3. Review personalized learning path.
4. Explore adaptive study plan.
5. Generate certification assessment.
6. Analyze manager insights.
7. Monitor workforce readiness through dashboards.

---

# 🏆 Microsoft Agents League Hackathon

SkillForge AI demonstrates how multiple specialized AI agents can collaborate through Azure AI Foundry to deliver enterprise-grade certification intelligence, workforce analytics, and adaptive learning experiences.

Built with ❤️ for the Microsoft Agents League Hackathon.