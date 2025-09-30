import os
from openai import OpenAI
from src.clients.base_client import BaseClient

class OpenAIClient(BaseClient):
    def __init__(self, model: str):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model: str = model