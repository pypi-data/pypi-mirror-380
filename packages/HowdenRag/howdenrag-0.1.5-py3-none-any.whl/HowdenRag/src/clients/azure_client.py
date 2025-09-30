import os
from openai import AsyncAzureOpenAI
from src.clients.base_client import BaseClient

class AzureOpenAIClient(BaseClient):
    def __init__(self, model: str):
        self.client = AsyncAzureOpenAI(
            api_key=os.getenv("AZURE-OPENAI-API-KEY"),
            api_version=os.getenv("AZURE-OPENAI-API-VERSION"),
            azure_endpoint=os.getenv("AZURE-OPENAI-ENDPOINT"),
        )
        self.model: str = model
        
   


        