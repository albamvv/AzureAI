# 💬 Chat Application with Azure AI Foundry (GPT-4o)

This project demonstrates how to deploy a **GPT-4o model** using **Azure AI Foundry** and create a simple **Python client application** that chats with the deployed model.

---

## 🧩 Overview

In this exercise, you will:

1. Deploy the **GPT-4o model** in Azure AI Foundry.  
2. Configure a project and model deployment.  
3. Build a **Python chat client** using the **Azure AI Foundry** and **Azure OpenAI SDKs**.  
4. Interact with your model through a command-line chat interface.  

## Activar entorno

```bash
source labenv/Scripts/activate
```

## ⚙️ Prerequisites

Before you start, ensure you have:

- An active **Azure subscription** (`CS-SUB-0417` or equivalent)
- Access to **Azure AI Foundry** and **Azure Portal**
- Basic familiarity with **Python** and **Azure Cloud Shell**
- **Git** and **PowerShell** (if running locally)
- Access to Azure AI Foundry: https://ai.azure.com
- Credentials provided by the instructor
- Permissions to create hubs, projects, and model deployments

##  Set Up the Environment

Create a virtual environment and install dependencies:

```bash
python -m venv labenv
.\labenv\Scripts\activate
pip install azure-identity azure-ai-projects openai
```

## Architecture Notes: Azure AI Foundry + Connected AI Resource

Azure AI Foundry is responsible for orchestration:
- project configuration
- model deployment workflows
- evaluation pipelines
- UI and management experience

The Connected AI Resource (Azure OpenAI) provides:
- model hosting and runtime execution
- inference endpoints and API keys
- quota and throughput limits
- safety filters and enterprise access controls

In this architecture:
- **Foundry** = control plane  
- **Connected AI Resource** = data plane  
Both layers work together to support end-to-end generative AI development.

## Understanding Azure AI Foundry and the Connected AI Resource

Below is a simplified view of how both components work together:

                 ┌───────────────────────────────┐
                 │       Azure AI Foundry        │
                 │  • UI / Workspace             │
                 │  • Project orchestration      │
                 │  • Evaluations & pipelines    │
                 │  • Management & monitoring    │
                 └───────────────┬───────────────┘
                                 │ orchestrates
                                 ▼
                 ┌───────────────────────────────┐
                 │   Connected AI Resource       │
                 │   (Azure OpenAI backend)      │
                 │  • Model hosting              │
                 │  • Inference runtime          │
                 │  • Quotas & throughput        │
                 │  • Safety filters & policies  │
                 └───────────────────────────────┘

Summary:
- Foundry = orchestration layer (control plane)
- Connected AI Resource = execution layer (data plane)






