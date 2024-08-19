from dotenv import load_dotenv  
import os
from os.path import dirname
import semantic_kernel as sk
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

current_dir = dirname(os.path.abspath(__file__))
root_dir = dirname(dirname(current_dir))
env_file = os.path.join(root_dir, '.env')

async def main():
    #Load the environment variables
    load_dotenv(dotenv_path=env_file)
    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
    endpoint_url = os.getenv("AZURE_OPENAI_ENDPOINT")
    azure_key = os.getenv("AZURE_OPENAI_API_KEY")

    kernel = sk.Kernel()

    # Add Azure OpenAI chat completion
    kernel.add_service("dv", AzureChatCompletion(
        deployment_name=deployment_name,
        api_key=azure_key,
        base_url=endpoint_url
    ))
    
    #kernel.add_service("dv", azure_chat_completion)

    # Define the prompt
    prompt = kernel.create_semantic_function("What are the differences between Azure Machine Learning and Azure AI services?")

    print("Prompt:", prompt)

    
    print(response)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
