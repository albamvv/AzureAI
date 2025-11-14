
# Explore AI Agent Development

This project demonstrates how to build, configure, and test an AI Agent using the Azure AI Agent service in Azure AI Foundry. The agent assists employees with corporate expense claims by grounding its responses in a policy document and generating claim files through the code interpreter.

> **Note:** Some features used in this exercise are in preview or evolving. You may encounter errors or unexpected behavior.

---

# 1. Create an Azure AI Foundry Project and Agent

## Sign in
1. Open https://ai.azure.com  
2. Sign in 
3. Generate and enter the authentication code within 60 seconds.
4. Close any onboarding dialogs and navigate to the home page.

## Create the Project
1. On the home page, select **Create an agent**.

<p align="left"><img src="./images/create_agent.png" height="280px"></p>

2. Enter a valid project name.
3. Expand **Advanced options** and configure:
   - **Azure AI Foundry resource:** choose a valid name  
   - **Subscription:** `CS-SUB-0429`
   - **Resource group:** `AI-102`
   - **Region:** any recommended region  

> Some regions may have quota limits. If deployment fails later, repeat in a different region.

4. Select **Create**.
5. If prompted to deploy the `gpt-4o` model:
   - Deployment type: **Standard**
   - Tokens per minute: **5K** (or the maximum available)

A `gpt-4o` model deployment is created automatically when you create your first agent.

The **Agents Playground** will open automatically.

---

# 2. Create the Agent

## Download the Knowledge Document
Download the expenses policy document:

**https://raw.githubusercontent.com/MicrosoftLearning/mslearn-ai-agents/main/Labfiles/01-agent-fundamentals/Expenses_Policy.docx**

Save it locally.

## Configure the Agent
In the **Agents Playground**, open the **Setup** panel.

- **Agent name:** `ExpensesAgent`
- **Model:** ensure the GPT-4o deployment is selected
- **Instructions:**

