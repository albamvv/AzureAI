# 🧪 Lab: Use a custom function in an AI agent

Este laboratorio guía el desarrollo de un **AI Agent** capaz de analizar datos y generar visualizaciones utilizando **Azure AI Agent Service** y el **Code Interpreter Tool**.  
El agente ejecutará código Python de forma dinámica para procesar datos y responder a consultas del usuario.

---

## 1. Create an Azure AI Foundry project

1. Open a web browser and navigate to the Azure AI Foundry portal at https://ai.azure.com.
2. In the home page, select **Create an agent**. 

<p align="left"><img src="./images/create_agent.png" height="280px"></p> 

3. When prompted to create a project, enter a valid name for your project and expand Advanced options.
4. Confirm the following settings for your project:

* Some Azure AI resources are constrained by regional model quotas. In the event of a quota limit being exceeded later in the exercise, there's a possibility you may need to create another resource in a different region.
   - **Azure AI Foundry resource:** A valid name for your Azure AI Foundry resource 
   - **Subscription:** Tu suscripción del laboratorio , CS-SUB-0417
   - **Resource group:** AI-102  
   - **Region:** Select any AI Foundry recommended*

<p align="left"><img src="./images/create_project.png" height="280px"></p> 

5. If prompted, deploy a **gpt-4o** model using either the Global Standard or Standard deployment option (depending on your quota availability).

<div style="display: flex; gap: 10px;">
  <img src="./images/deploy_model.png" height="280px">
  <img src="./images/deploy_model2.png" height="280px">
</div>

<p align="left"><img src="./images/deploy_model3.png" height="280px"></p> 

6. When your project is created, the Agents playground will be opened.

<div style="display: flex; gap: 10px;">
  <img src="./images/agents_playground.png" height="250px">
  <img src="./images/agents_playground.png" height="250px">
</div>


7. In the navigation pane on the left, select Overview to see the main page for your project; which looks like this:

<p align="left"><img src="./images/overview.png" height="280px"></p> 

8. Copy the Azure AI Foundry project endpoint values to a notepad, as you'll use them to connect to your project in a client application


## 2. Develop an agent that uses function tools

### Clone the repo containing the application code

1. Open a new browser tab (keeping the Azure AI Foundry portal open in the existing tab). Then in the new tab, browse to the **Azure portal** at https://portal.azure.com; signing in with your Azure credentials if prompted.
2. Abre **Azure Cloud Shell** (PowerShell).  Use the [>_] button to the right of the search bar at the top of the page to create a new Cloud Shell in the Azure portal, selecting a PowerShell environment with no storage in your subscription.
3. In the cloud shell pane, enter the following commands to clone the GitHub repo containing the code files for this exercise (type the command, or copy it to the clipboard and then right-click in the command line and paste as plain text):

```bash
rm -r ai-agents -f
git clone https://github.com/MicrosoftLearning/mslearn-ai-agents ai-agents
```
### Configure the application settings

1. In the cloud shell command-line pane, enter the following command to install the libraries you'll use:

```bash
python -m venv labenv
./labenv/bin/Activate.ps1
pip install -r requirements.txt azure-ai-projects
```

2. Enter the following command to edit the configuration file that has been provided:

```bash
code .env
```

<p align="left"><img src="./images/env.png" height="380px"></p> 

3. Define a custom function

Enter the following command to edit the code file that has been provided for your function code:

```bash
code user_functions.py
```
### Write code to implement an agent that can use your function

- Review the code, using the comments to understand how it:

  - Adds your set of custom functions to a toolset
  - Creates an agent that uses the toolset.
  - Runs a thread with a prompt message from the user.
  - Checks the status of the run in case there's a failure
  - Retrieves the messages from the completed thread and displays the last one sent by the agent.
  - Displays the conversation history
  - Deletes the agent and thread when they're no longer required.

### Sign into Azure and run the app

1. Run az login 

```bash
az login
```

<p align="left"><img src="./images/azlogin.png" height="380px"></p> 

2. After you have signed in, enter the following command to run the application:

3. When prompted, enter a prompt such as:

I have a technical problem

<p align="left"><img src="./images/technical_problem.png" height="380px"></p> 

4. View the response. The agent may ask for your email address and a description of the issue. You can use any email address (for example, alex@contoso.com) and any issue description (for example my computer won't start)


5. You can continue the conversation if you like. The thread is stateful, so it retains the conversation history - meaning that the agent has the full context for each response. Enter quit when you're done.

6. Review the conversation messages that were retrieved from the thread, and the tickets that were generated.
7. The tool should have saved support tickets in the app folder. You can use the ls command to check, and then use the cat command to view the file contents, like this:


cat ticket-<ticket_num>.txt

## ✔️ Conclusiones técnicas

- **Los Azure AI Agents no soportan autenticación por clave.**  
  Solo admiten autenticación mediante **Azure Active Directory (Azure AD)**.

- Por tanto, el código únicamente puede funcionar utilizando:

  **✔️ `DefaultAzureCredential`**  
  Ideal para desarrollo local, especialmente si utilizas `az login`.

  **✔️ `ClientSecretCredential`**  
  Recomendado para entornos de **CI/CD**, servicios backend o despliegues automatizados.

## Run Without AZ LOGIN

### 1. Microsoft Entra ID: AZURE_TENANT_ID


1. En el portal de Azure, ve a Microsoft Entra ID. En el menú de la izquierda selecciona: Microsoft Entra ID



<img src="./images/ms_entra_id.png" height="400px">

<img src="./images/id_inquilino_tenant.png" height="300px">


2. Create the App Registration: AZURE_CLIENT_ID

Microsoft Entra ID → App registrations → New registration

<img src="./images/crear_app.png" height="300px">

3. Rellena:

- Name: por ejemplo bbva-ai-agents-custom-functions.
- Supported account types: normalmente Single tenant (solo vuestro tenant).
- Redirect URI no es necesaria para client credentials (puede quedar vacía).

<img src="./images/registrar_app.png" height="300px">

This is where your **azure_client_id** appears:

<img src="./images/azure_client_id.png" height="270px">

- Once created:
  - The *Application (client) ID* appears at the top.
  - The *Directory (tenant) ID* is also visible here (same as before).

---

### 3. Create the Secret: AZURE_CLIENT_SECRET

1. Vamos a registro de aplicaciones

<p align="left"><img src="./images/registro_apps.png" height="25¡00px"></p> 


2. Vamos a todas las aplicaciones

<img src="./images/todas_apps.png" height="380px">



3. Añadir nuevo cliente

>New client secret → Add → Copy the value

- **Value** is the real secret key Azure AD uses to generate tokens.  
- **Secret ID** only identifies the secret inside Azure; it is *not* used for authentication.

<img src="./images/valor.png" height="300px">



### 4. Assign Permissions (IAM Role) to the App Registration

#### 1. Open the resources

<img src="./images/recursos.png" height="300px">


### Resource Structure in Azure AI Foundry

You have two main resources:


#### 1️⃣ `project-agent-resource`
- **Type:** AI Foundry (Azure AI Services)
- **Description:**  
  This is the *root resource* of Azure AI Foundry.  
  **This is where permissions must be assigned.**

This resource controls critical capabilities:
- Creating Agents  
- Running Agents  
- Calling `/assistants`  
- Creating `/runs`  
- Creating `/threads`  

👉 **This is the resource currently blocking your operations.**

---

#### 2️⃣ `project_agent` (inside `project-agent-resource`)
- **Type:** Azure AI Project  
- **Description:**  
  This contains the specific Foundry project, but **does not control** the core IAM permissions.

📌 **Conclusion:**  
Assign roles directly to **`project-agent-resource` (AI Foundry)** to unlock all Agent and Assistant operations.

---

### 2. Select the Resource

Click on **project-agent-resource** (Type: AI Foundry)

<img src="./images/IAM.png" height="300px">

---

### 3. Exact Steps to Grant Access

- Access control (IAM)
- Click **+ Add**
- Click **Add role assignment**
- Search for the role:
  - **Azure AI Developer** (recommended)
  - **Cognitive Services Contributor**
- Choose **User, group, or service principal**

<img src="./images/asignar_acceso.png" height="300px">

- Search for your App Registration: **agents-client-app**

<img src="./images/miembros.png" height="300px">

- Select it and save

### 4. app empresarial

Portal Azure  
 → Microsoft Entra ID  
   → Aplicaciones empresariales  
     → Todas las aplicaciones  
       → + Nueva aplicación  
         → Examinar la galería de aplicaciones de Microsoft Entra

<img src="./images/app_empresarial.png" height="300px">

