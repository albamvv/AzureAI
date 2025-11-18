# 🧪 Lab: Develop an AI Agent with Azure AI Agent Service

Este laboratorio guía el desarrollo de un **AI Agent** capaz de analizar datos y generar visualizaciones utilizando **Azure AI Agent Service** y el **Code Interpreter Tool**.  
El agente ejecutará código Python de forma dinámica para procesar datos y responder a consultas del usuario.

---

## 1. Crear un proyecto en Azure AI Foundry

1. Accede al portal: https://ai.azure.com  
2. Selecciona **Create an agent**.  
3. Configura el proyecto:
   - **Azure AI Foundry resource:** Selecciona un recurso válido  
   - **Subscription:** Tu suscripción del laboratorio  
   - **Resource group:** AI-102  
   - **Region:** Cualquiera recomendada para Foundry  

4. Crea el proyecto. Si se solicita, despliega un modelo **gpt-4o** con configuración *Standard* (5K TPM).

5. Una vez creado el proyecto:
   - El **Agents playground** se abrirá automáticamente.
   - En **Overview**, copia los valores del **project endpoint**. Los necesitarás para el cliente Python.

---

## 2. Create an agent client app

### Clonar el repositorio de ejemplo

1. Abre https://portal.azure.com en otra pestaña.  
2. Abre **Azure Cloud Shell** (PowerShell).  
3. Ejecuta:

```bash
rm -r ai-agents -f
git clone https://github.com/MicrosoftLearning/mslearn-ai-agents ai-agents
```

## 3. Pruebas


When prompted, view the data that the app has loaded from the data.txt text file. Then enter a prompt such as:

```bash
What's the category with the highest cost?
```


View the response. Then enter another prompt, this time requesting a visualization:

```bash
Create a text-based bar chart showing cost by category
```

View the response. Then enter another prompt, this time requesting a statistical metric:

```bash
What's the standard deviation of cost?
```


## 🧠 CONCEPTO CLAVE

El SDK Azure AI Agent Service (lib azure.ai.agents) permite dos modos de autenticación:

1. DefaultAzureCredential → requiere az login (actualmente lo que usas)

2. API Key → igual que con Azure OpenAI (lo que quieres usar)

Y sí: puedes usar API Key también para agentes.