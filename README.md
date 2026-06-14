# 🚀 SkillForge AI

### Enterprise Certification Intelligence Platform powered by Azure AI Foundry

SkillForge AI is an enterprise learning and certification readiness platform that helps employees and managers accelerate certification success through AI-powered recommendations, grounded learning paths, adaptive study plans, readiness assessments, and workforce intelligence.

Built for the **Microsoft Agents League Hackathon**, SkillForge combines Azure AI Foundry Agents, Azure AI Search, Azure OpenAI, Knowledge Bases, and a coordinated multi-agent architecture to deliver personalized certification guidance grounded in official Microsoft certification content.

## 🌐 Live Demo

https://skillforge-ai-egcwzshcnjb9uv2wvyspkh.streamlit.app/

---

## 🎯 Problem Statement

Organizations invest heavily in employee certifications, but often struggle to answer:

* Which certification should an employee pursue?
* Is the employee ready for certification?
* What learning path should they follow?
* How much study effort is required?
* Which employees are at risk of failing?
* What workforce interventions are needed?

SkillForge AI addresses these challenges using AI agents that transform certification goals into actionable learning plans and workforce insights.

---

## 🤖 Multi-Agent Architecture

SkillForge AI uses a coordinated multi-agent workflow where each agent performs a specialized responsibility.

### 1. Learner Profile Agent

Analyzes:

* Role
* Certification target
* Meeting load
* Focus hours

Produces:

* Readiness score
* Risk classification
* Recommended study effort

---

### 2. Learning Curator Agent

Retrieves certification knowledge and generates:

* Required skills
* Learning roadmap
* Study sequence
* Certification preparation strategy

---

### 3. Study Planner Agent

Creates:

* Personalized study plans
* Workload-aware schedules
* Weekly goals
* Assessment checkpoints

---

### 4. Assessment Agent

Generates:

* Certification practice questions
* Scenario-based challenges
* Answer keys
* Readiness evaluation criteria

---

### 5. Manager Insights Agent

Provides:

* Workforce readiness visibility
* Risk forecasting
* Intervention recommendations
* Certification success projections

---

## 🧠 Azure AI Foundry Integration

SkillForge AI leverages Azure AI Foundry to provide grounded and explainable certification guidance.

### Components Used

✅ Azure AI Foundry Project

✅ Azure AI Foundry Agent

✅ Azure AI Search

✅ Azure OpenAI

✅ Knowledge Base

✅ Managed Identities

✅ MCP (Model Context Protocol)

### Knowledge Base

The platform uses an Azure AI Foundry Knowledge Base containing Microsoft certification learning materials and certification guidance.

Examples:

* AZ-204
* AZ-400
* DP-203
* AI-102
* Azure learning resources

The AI agent retrieves relevant knowledge before generating recommendations, ensuring responses are grounded in certification documentation rather than relying solely on model knowledge.

---

## 🏗 System Architecture

Employee / Manager

↓

Streamlit Frontend

↓

Workflow Orchestrator

↓

Learner Profile Agent

↓

Learning Curator Agent

↓

Study Planner Agent

↓

Assessment Agent

↓

Manager Insights Agent

↓

Azure AI Foundry Agent

↓

Azure AI Search

↓

Knowledge Base

↓

Azure OpenAI

---

## 📊 Key Features

### Individual Learner Planning

* Readiness scoring
* Risk assessment
* Learning path generation
* Adaptive study plans
* Certification preparation guidance

### Workforce Intelligence

* Team readiness dashboard
* Risk distribution analysis
* Certification forecasting
* Manager recommendations

### Platform Analytics

* Agent execution visibility
* Workflow traceability
* Readiness trends
* Operational insights

### Explainable AI

* Agent execution traces
* Grounded responses
* Knowledge-backed recommendations

---

## 🖥 Application Pages

| Page               | Purpose                             |
| ------------------ | ----------------------------------- |
| Learner Planner    | Personalized certification planning |
| Manager Dashboard  | Workforce readiness intelligence    |
| Platform Analytics | Operational and agent metrics       |
| Execution Trace    | Multi-agent workflow visibility     |
| Architecture       | System architecture visualization   |

---

## 🛠 Tech Stack

### Frontend

* Streamlit
* Plotly

### Backend

* Python
* Pandas

### AI & Agentic Layer

* Azure AI Foundry
* Azure OpenAI
* Azure AI Search
* Azure AI Foundry Knowledge Base
* MCP (Model Context Protocol)

### Cloud

* Microsoft Azure

---

## 📂 Project Structure

SkillForge-AI/

├── agents/

├── data/

├── frontend/

├── orchestrator/

├── config.py

├── requirements.txt

├── run_workflow.py

└── README.md

---

## 🚀 Local Setup

Clone the repository:

```bash
git clone <repository-url>
cd SkillForge-AI
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure environment variables:

```env
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_DEPLOYMENT_NAME=
```

Run the application:

```bash
streamlit run frontend/app.py
```

---

## 🏆 Microsoft Agents League Alignment

SkillForge AI demonstrates:

* Multi-Agent Reasoning
* Knowledge-Grounded AI
* Azure AI Foundry Integration
* Enterprise Workforce Intelligence
* Retrieval-Augmented Generation (RAG)
* Agent Orchestration
* Explainable AI Workflows

The project showcases how organizations can leverage AI agents to improve certification readiness, workforce upskilling, and employee development at scale.

---

## 👨‍💻 Author

Devamm Patel

Built for the Microsoft Agents League Hackathon 2026.
