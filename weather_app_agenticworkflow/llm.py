import os
from langchain_openai import AzureChatOpenAI

def getLLM():
    return AzureChatOpenAI(
    openai_api_version=os.environ.get("AZURE_OPENAI_VERSION", "VERSION"),
    azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT", "MODEL"),
    azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT", "BASE_PATH"),
    api_key=os.environ.get("KEY")
)
