
# Explore AI Agent Development

This project demonstrates how to build, configure, and test an AI Agent using the Azure AI Agent service in Azure AI Foundry. The agent assists employees with corporate expense claims by grounding its responses in a policy document and generating claim files through the code interpreter.

> **Note:** Some features used in this exercise are in preview or evolving. You may encounter errors or unexpected behavior.

---

## 1. Create an Azure AI Foundry Project and Agent

## Create the Project
1. Open https://ai.azure.com and sign in 
2. On the home page, select **Create an agent**.

<p align="left"><img src="./images/create_agent.png" height="200px"></p>

3. Enter a valid project name.
4. Expand **Advanced options** and configure:
   - **Azure AI Foundry resource:** choose a valid name  
   - **Subscription:** `CS-SUB-0429`
   - **Resource group:** `AI-102`
   - **Region:** any recommended region  

<p align="left"><img src="./images/crear_proyecto.png" height="350px"></p>

5. Select **Create**.

### Automatic Resource Creation When Creating an Agent

When you create an AI Agent for the first time in Azure AI Foundry, the platform automatically provisions the required infrastructure if it does not already exist.

If you click **Create an agent** and no project or Azure OpenAI resource is available yet, Azure will automatically create:

- **A new Project**  
  This serves as the workspace that stores agents, models, vector stores, evaluations, and configuration.

- **A new Azure OpenAI Resource**  
  This is the backend service where the model is hosted, deployed, and executed.

- **A Base Model Deployment (gpt-4o or gpt-4o-mini)**  
  Azure deploys a default model so the agent has a working LLM available immediately.

This automation ensures that first-time users can start building agents without manually creating or configuring backend resources. Once the project is created, all future agents and deployments will reuse the connected Azure OpenAI resource unless specified otherwise.

6. If prompted to deploy the `gpt-4o` model:
   - Deployment type: **Standard**
   - Tokens per minute: **5K** (or the maximum available)

A `gpt-4o` model deployment is created automatically when you create your first agent.

The **Agents Playground** will open automatically.

---

## 2. Create the Agent

## Download the Knowledge Document
Download the expenses policy document:

**https://raw.githubusercontent.com/MicrosoftLearning/mslearn-ai-agents/main/Labfiles/01-agent-fundamentals/Expenses_Policy.docx**

Save it locally.

## Configure the Agent
In the **Agents Playground**, open the **Setup** panel.

- **Agent name:** `ExpensesAgent`
- **Model:** ensure the GPT-4o deployment is selected
- **Instructions:**

