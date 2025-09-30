import os
from pathlib import Path
from dotenv import load_dotenv
from llama_parse import LlamaParse, ResultType

class LlamaMarkdownParser:
    def __init__(self, name: str, config: dict) -> None:
        load_dotenv()
        self.api_key = os.getenv(name)
        if not self.api_key:
            raise EnvironmentError("Missing CLAIMS-RAG-TOKEN in environment variables.")

        self.parser = LlamaParse(
            api_key=self.api_key,
            result_type=ResultType.MD,
            premium_mode=config["llama_parser"]["premium_mode"]
        )

    def parse_file(self, file_path: Path) -> str:
        documents = self.parser.load_data(str(file_path))
        return "\n".join([f"{doc.text} <--PAGE_NUMBER {page + 1}-->\n" for page, doc in enumerate(documents)])