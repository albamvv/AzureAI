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


##  Set Up the Environment

Create a virtual environment and install dependencies:

```bash
python -m venv labenv
.\labenv\Scripts\activate
pip install azure-identity azure-ai-projects openai
```


### 4. variables de entorno

1. MODEL_DEPLOYMENT

![MODEL_DEPLOYMENT](./images/MODEL_DEPLOYMENT.png)

2. OPENAI_API_VERSION

![OPENAI_API_VERSION](./images/OPENAI_API_VERSION.png)

## RESOURCE DATA

3. AZURE_OPENAI_KEY

![AZURE_OPENAI_KEY](./images/AZURE_OPENAI_KEY.png)

4. AZURE_OPENAI_ENDPOINT

![AZURE_OPENAI_ENDPOINT](./images/AZURE_OPENAI_ENDPOINT.png)




