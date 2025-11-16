# 💬 Chat Application with Azure AI Foundry (GPT-4o)

This project demonstrates how to deploy a **GPT-4o model** using **Azure AI Foundry** and create a simple **Python client application** that chats with the deployed model.

---

## 🧩 Overview

In this exercise, you will:

1. Deploy the **GPT-4o model** in Azure AI Foundry.  
2. Configure a project and model deployment.  
3. Build a **Python chat client** using the **Azure AI Foundry** and **Azure OpenAI SDKs**.  
4. Interact with your model through a command-line chat interface.  

## ⚙️ Activar entorno

```bash
source .venv/bin/activate
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

## 📦 Set Up the Environment

Create a virtual environment and install dependencies:

```bash
python -m venv labenv
.\labenv\Scripts\activate
pip install azure-identity azure-ai-projects openai
```

## 🧱 Architecture Notes: Azure AI Foundry + Connected AI Resource

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

### Azure AI Foundry

There are two types of projects in Azure AI Foundry.

<p align="left"><img src="./images/azure_projects.png" height="380px"></p> 

1. **Foundry projects**

Foundry projects are associated with an Azure AI Foundry resource in an Azure subscription. Foundry projects provide support for Azure AI Foundry models (including OpenAI models), Azure AI Foundry Agent Service, Azure AI services, and tools for evaluation and responsible AI development.

An Azure AI Foundry resource supports the most common AI development tasks to develop generative AI chat apps and agents. In most cases, using a Foundry project provides the right level of resource centralization and capabilities with a minimal amount of administrative resource management. You can use Azure AI Foundry portal to work in projects that are based in Azure AI Foundry resources, making it easy to add connected resources and manage model and agent deployments.

2. **Hub-based projects**

Hub-based projects are associated with an Azure AI hub resource in an Azure subscription. Hub-based projects include an Azure AI Foundry resource, as well as managed compute, support for Prompt Flow development, and connected Azure storage and Azure key vault resources for secure data storage.

Azure AI hub resources support advanced AI development scenarios, like developing Prompt Flow based applications or fine-tuning models. You can also use Azure AI hub resources in both Azure AI Foundry portal and Azure Machine learning portal, making it easier to work on collaborative projects that involve data scientists and machine learning specialists as well as developers and AI software engineers






