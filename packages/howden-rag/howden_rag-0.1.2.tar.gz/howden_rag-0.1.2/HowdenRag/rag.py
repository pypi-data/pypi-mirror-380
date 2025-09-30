from typing import List
import os
from llama_index.core.node_parser import SentenceSplitter
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from dotenv import load_dotenv
from howden_rag.utils import make_safe_id
from pathlib import Path
load_dotenv()
from openai import OpenAI


def make_safe_id(filepath: Path) -> str:
    return filepath.stem.replace(" ", "_").lower()


class DocumentChunk:
    """Represents a single chunk of text with its embedding and metadata."""

    def __init__(self, idx: int, text: str, embedding: list[float], filepath: Path):
        self.id = f"{idx}_{make_safe_id(filepath)}"
        self.content = text
        self.content_vector = embedding
        self.filepath = filepath

    def to_dict(self) -> dict:
        """Convert to a dictionary suitable for uploading."""
        return {
            "id": self.id,
            "content": self.content,
            "content_vector": self.content_vector,
        }

    def to_markdown(self) -> str:
        """Convert chunk into markdown format for documentation."""
        return (
            f"### Chunk {self.id}\n\n"
            f"**File:** `{self.filepath.name}`\n\n"
            f"**Content:**\n\n{self.content}\n\n"
            f"---\n"
        )


class RAG:
    def __init__(self,
                 model: str,
                 chunk_size,
                 chunk_overlap: int,
                 name:str,
                 build_database: bool):
        self.model = model
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.name = name

        self._build_database = build_database
        self._all_chunks: List[DocumentChunk] = []

        self._search_client: SearchClient= SearchClient(endpoint=os.getenv("ENDPOINT"),
                                                        index_name=os.getenv("index_name"),
                                                        credential=AzureKeyCredential(os.getenv("AZURE_API_KEY")))

        self._embed_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def __call__(self,filepath: Path) -> str:
        return self.run(filepath)

    def run(self, filepath: Path):
        if self._build_database:
            self.index_database()

        text = filepath.read_text(encoding="utf-8")
        chunks = self.chunk_text(text)

        doc_chunks = self.embed_chunks(chunks, filepath)
        self._all_chunks.extend(doc_chunks)  # keep for later

        self.upload_document(doc_chunks)

        return "\n".join(c.to_markdown() for c in self._all_chunks)

    def save_all_chunks_to_md(self, output_path: Path):
        """Dump all collected chunks into one markdown file."""
        with output_path.open("w", encoding="utf-8") as f:
            f.write("# Document Chunks Export\n\n")
            for chunk in self._all_chunks:
                f.write(chunk.to_markdown())
        print(f"✅ Saved {len(self._all_chunks)} chunks to {output_path}")

    def index_database(self):
        from howden_rag.handler_create_index import create_index  # adjust to your actual import
        create_index(
            os.getenv("ENDPOINT"),
            os.getenv("AZURE_API_KEY"),
            os.getenv("index_name"),
            delete_if_exists=True,
        )
        self._build_database = False

    def chunk_text(self, text: str) -> List[str]:
        splitter = SentenceSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
        return splitter.split_text(text)

    def embed_chunks(self, chunks: List[str], filepath: Path) -> List[DocumentChunk]:
        doc_chunks = []
        for idx, txt in enumerate(chunks):
            response = self._embed_client.embeddings.create(model=self.model, input=txt)
            embedding = response.data[0].embedding
            doc_chunks.append(DocumentChunk(idx, txt, embedding, filepath))
        return doc_chunks

    def upload_document(self, doc_chunks: List[DocumentChunk]):
        print("Uploading documents...")
        docs = [chunk.to_dict() for chunk in doc_chunks]
        self._search_client.upload_documents(docs)
