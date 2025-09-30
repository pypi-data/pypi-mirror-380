from pathlib import Path
from HowdenConfig import Config
import os

def wrapper(path: Path, model, text: str, client):
    folder_path = path.parent
    if not folder_path.exists():
        hash_value = parameter.hash_value
        os.mkdir(str(folder_path / hash_value))
        embed_text(text, client, parameter)







def embed_text(text: str, client, model: str  ) -> list[float]:

    response = client.embeddings.create(
        model=model,
        input=text
    )
    return response.data[0].embedding

