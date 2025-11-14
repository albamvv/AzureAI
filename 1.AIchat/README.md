# 💬 Chat Application with Azure AI Foundry (GPT-4o)

This project demonstrates how to deploy a **GPT-4o model** using **Azure AI Foundry** and create a simple **Python client application** that chats with the deployed model.

---

## 🧩 Overview

In this exercise, you will:

1. Deploy the **GPT-4o model** in Azure AI Foundry.  
2. Configure a project and model deployment.  
3. Build a **Python chat client** using the **Azure AI Foundry** and **Azure OpenAI SDKs**.  
4. Interact with your model through a command-line chat interface.  

## 1. Deploy a model in an Azure AI Foundry project
Let's start by deploying a model in an Azure AI Foundry project.

1. Open a web browser and navigate to the Azure AI Foundry portal at https://ai.azure.com and sign in
2. In the home page, in the Explore models and capabilities section, search for the **gpt-4o model**; which we'll use in our project.
3. In the search results, select the gpt-4o model to see its details, and then at the top of the page for the model, select Use this model. When prompted to create a project, enter a valid name for your project and expand Advanced options.

<p align="left"><img src="./images/gpt-4o_model.png" height="380px"></p> 



After selecting **Customize**, specify the following settings for your project:

- **Azure AI Foundry resource:**  
  Provide a valid name for your Azure AI Foundry resource.
- **Subscription:**  
  `CS-SUB-0445`
- **Resource group:**  
  Create or select an existing resource group.
- **Region:**  
  Select any *AI Foundry recommended* region.

> **Note:** Some Azure AI resources are limited by regional model quotas.  
> If you encounter quota limitations later in the exercise, you may need to create the resource again in a different region.

4. Select Create and wait for your project to be created. If prompted, deploy the gpt-4o model using the Standard deployment type and customize the deployment details to set a Tokens per minute rate limit of 5K.

> **Note:**  Reducing the TPM helps avoid over-using the quota available in the subscription you are using. 5,000 TPM should be sufficient for the data used in this exercise. If your available quota is lower than this, you will be able to complete the exercise but you may experience errors if the rate limit is exceeded.

5. When your project is created, the chat playground will be opened automatically so you can test your model:
6. In the Setup pane, note the name of your model deployment; which should be gpt-4o. You can confirm this by viewing the deployment in the Models and endpoints page (just open that page in the navigation pane on the left).
7. In the navigation pane on the left, select Overview to see the main page for your project; which looks like this:

## 2. Create a client application to chat with the model

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




