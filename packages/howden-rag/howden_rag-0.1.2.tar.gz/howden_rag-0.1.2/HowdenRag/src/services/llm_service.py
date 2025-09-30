from src.clients.base_client import BaseClient
import instructor 
from pydantic import BaseModel



class LLMService:
    def __init__(self, client: BaseClient):
        self.client = client.client
        self.model = client.model
    
    def get_instructor_client(self):
        return instructor.patch(self.client)

    def get_response(self, messages: list[dict], max_retries: int = 3, model: str = None, response_model: BaseModel = None, max_tokens: int = None):

        if response_model is None:
            client = self.client
            return client.chat.completions.create(
                model=model or self.model, 
                messages=messages,
                temperature=0.0, 
                max_tokens=max_tokens)   

        instructor_client = self.get_instructor_client()
        return instructor_client.chat.completions.create(
            model=model or self.model,
            response_model=response_model,
            messages=messages,
            max_retries=max_retries, 
            temperature=0.0)
    

    def get_embeddings(self, text: str, embedding_model: str) -> list[float]: 
        client = self.client
        return client.embeddings.create(model=embedding_model, input=text).data[0].embedding