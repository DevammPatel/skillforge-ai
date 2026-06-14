# SkillForge AI

Enterprise certification intelligence powered by Azure AI Foundry, Azure OpenAI, and a coordinated multi-agent workflow.

SkillForge AI helps employees and managers turn certification goals into readiness scores, learning paths, adaptive study plans, generated assessments, and workforce-level insights. The app now includes a polished multi-page Streamlit interface with shared visual styling, dashboard cards, tuned Plotly charts, and traceable agent output.

## What Changed

- Added a shared Streamlit UI layer in `frontend/ui.py` for theming, hero sections, section headers, agent lists, and Plotly defaults.
- Polished the learner planner in `frontend/app.py` with a stronger product layout, styled sidebar workflow, KPI row, readiness gauge, and cleaner output sections.
- Refined manager and analytics dashboards with consistent cards, chart colors, table framing, and executive sections.
- Updated architecture and execution trace pages so the whole Streamlit experience feels cohesive.
- Refreshed this README to match the current project structure and run flow.

## Core Features

- Learner readiness scoring based on role, certification target, meeting load, and focus capacity.
- Knowledge-grounded learning path generation for Azure certification goals.
- Workload-aware study plan creation.
- Work-rhythm engagement plan for reminder cadence and escalation rules.
- AI-generated practice assessment content and readiness criteria.
- Manager dashboard for team readiness, risk distribution, pass-rate forecasting, and recommended actions.
- Platform analytics for agent health, workflow volume, and response-time visibility.
- Execution trace page showing each agent handoff and final output.

## Microsoft IQ Alignment

This project targets the Microsoft Agents League Reasoning Agents track and uses synthetic enterprise learning data only.

- **Foundry IQ pattern:** `knowledge_base/*.md` acts as the approved knowledge layer for learning-path and assessment generation. The prompts require grounded answers and source citations from the synthetic certification guide, workload report, and team report. When Azure credentials are available, Azure OpenAI is used for generation; if not, deterministic grounded demo responses keep the app runnable for judges.
- **Work IQ pattern:** `data/workload.csv` provides synthetic work signals such as meeting hours, focus hours, and preferred learning slot. These signals influence readiness scoring and workload-aware study planning.
- **Fabric IQ pattern:** `data/certifications.json` represents a small semantic model of certifications, skills, and recommended study hours. The manager dashboard and planning flow use this role/certification structure for decision support.

All learner IDs, work signals, certification outcomes, and knowledge documents are fabricated for demonstration. No customer data, employee names, email addresses, PII, credentials, or confidential records are included.

## Application Pages

| Page | File | Purpose |
| --- | --- | --- |
| Learner Planner | `frontend/app.py` | Runs the full multi-agent workflow for an individual learner. |
| Manager Dashboard | `frontend/pages/manager_dashboard.py` | Aggregates learner readiness, risk, and workforce recommendations. |
| Platform Analytics | `frontend/pages/platform_analytics.py` | Shows operational metrics for workflows and agent health. |
| Execution Trace | `frontend/pages/execution_trace.py` | Displays a live trace of the multi-agent workflow. |
| Architecture | `frontend/pages/architecture.py` | Explains the system design, agents, and data flow. |

## Architecture

```text
Employee / Manager
        |
        v
Streamlit Experience
        |
        v
Workflow Orchestrator
        |
        +-- Learner Profile Agent
        +-- Learning Curator Agent
        +-- Study Planner Agent
        +-- Engagement Agent
        +-- Assessment Agent
        +-- Manager Insights Agent
        |
        v
Azure OpenAI / Azure AI Foundry
        |
        v
Knowledge Base + Learner Data
```

## Multi-Agent Workflow

1. Learner Profile Agent analyzes readiness, risk, and recommended study effort.
2. Learning Curator Agent retrieves knowledge and builds a certification learning path.
3. Study Planner Agent creates an adaptive schedule using workload constraints.
4. Engagement Agent recommends reminder cadence and follow-up rules from workload signals.
5. Assessment Agent generates MCQs, scenario questions, and evaluation criteria.
6. Manager Insights Agent turns the profile and plan into workforce-level guidance.

The orchestrator in `orchestrator/workflow.py` coordinates these agents and returns a single structured result for the UI.

## Tech Stack

- Python
- Streamlit
- Plotly
- Pandas and NumPy
- Azure OpenAI
- Azure AI Agents SDK
- python-dotenv

## Project Structure

```text
SkillForge-AI/
├── agents/
│   ├── assessment_agent.py
│   ├── engagement_agent.py
│   ├── learner_profile_agent.py
│   ├── learning_curator_agent.py
│   ├── llm_client.py
│   ├── manager_insights_agent.py
│   └── study_planner_agent.py
├── data/
│   ├── certifications.json
│   ├── learners.csv
│   └── workload.csv
├── frontend/
│   ├── app.py
│   ├── ui.py
│   └── pages/
│       ├── architecture.py
│       ├── execution_trace.py
│       ├── manager_dashboard.py
│       └── platform_analytics.py
├── knowledge_base/
│   ├── certification_guide.md
│   ├── team_report.md
│   └── workload_report.md
├── orchestrator/
│   ├── demo_trace.py
│   └── workflow.py
├── config.py
├── requirements.txt
└── run_workflow.py
```

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
AZURE_OPENAI_ENDPOINT=your_endpoint
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_DEPLOYMENT_NAME=your_deployment_name
AZURE_AI_PROJECT_ENDPOINT=your_project_endpoint_optional
AZURE_SEARCH_CONNECTION_NAME=your_search_connection_optional
```

The app can still run in demo mode without these variables. In that case, Azure calls fall back to deterministic responses grounded in the synthetic local knowledge base.

Run the Streamlit app:

```bash
streamlit run frontend/app.py
```

Open the local Streamlit URL and use the sidebar to generate a learner plan. Streamlit will expose the additional pages from the `frontend/pages` directory.

## CLI Demo

You can also run the workflow from the terminal:

```bash
python run_workflow.py
```

## Data Sources

- `data/learners.csv` drives the manager dashboard.
- `data/workload.csv` contains workload context.
- `data/certifications.json` stores certification metadata.
- `knowledge_base/*.md` grounds learning path and assessment generation.

## Hackathon Context

SkillForge AI was built for the Microsoft Agents League Hackathon to demonstrate collaborative AI agents for enterprise learning, certification readiness, and workforce planning.
