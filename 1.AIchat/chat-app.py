import os
from dotenv import load_dotenv
from openai import AzureOpenAI


def main(): 

    # Clear the console
    os.system('cls' if os.name=='nt' else 'clear')
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        """
        model_deployment =  os.getenv("MODEL_DEPLOYMENT")
        azure_openai_key = os.getenv("AZURE_OPENAI_KEY")
        azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        api_version = os.getenv("OPENAI_API_VERSION")
        """
        model_deployment =  os.getenv("MODEL_DEPLOYMENT_NAME")
        
        azure_openai_key = os.getenv("AZURE_OPENAI_KEY")
        azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

        azure_openai_key = os.getenv("AZURE_PROJECT_KEY")
        azure_openai_resource_endpoint = os.getenv("AZURE_OPEN_AI_RESOURCE_ENDPOINT")
        #api_version = os.getenv("OPENAI_API_VERSION")

        # Initialize the project client
        openai_client = AzureOpenAI(
            api_key=azure_openai_key,
            azure_endpoint=azure_openai_resource_endpoint,
            #api_version=api_version
        )
        
        # Initialize prompt with system message
        prompt = [ {"role": "system", "content": "You are a helpful AI assistant that answers questions."}]
         

        # Loop until the user types 'quit'
        while True:
            # Get input text
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue
            
            # Get a chat completion
            prompt.append({"role": "user", "content": input_text})
            response = openai_client.chat.completions.create(
                model=model_deployment,messages=prompt)
            completion = response.choices[0].message.content
            print(completion)
            prompt.append({"role": "assistant", "content": completion})
            

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()

