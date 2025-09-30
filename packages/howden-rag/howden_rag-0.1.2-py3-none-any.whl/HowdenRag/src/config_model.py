import toml
import dataclasses
import json
import hashlib

class ConfigValidationError(Exception):
    pass


from dataclasses import dataclass
from typing import Literal, get_args, Any
from pathlib import Path


@dataclass(frozen=True)
class InputConfig:
    pdf_path: str
    split: bool


@dataclass(frozen=True)
class LlamaParserConfig:
    premium_mode: bool


@dataclass(frozen=True)
class EmbeddingConfig:
    model: str
    chunk_size: int
    chunk_overlap: int


@dataclass(frozen=True)
class CompletionConfig:
    model: Literal["gpt-3.5-turbo", "gpt-4", "gpt-4o"]


@dataclass(frozen=True)
class ChromaConfig:
    method: Literal["cosine_similarity", "none"]
    threshold: float

    def __post_init__(self):
        allowed_methods = get_args(self.__annotations__["method"])
        if self.method not in allowed_methods:
            raise ValueError(
                f"method must be one of {allowed_methods!r}, got {self.method!r}"
            )

@dataclass(frozen=True)
class QueryConfig:
    model: str
    improve_query: bool
    max_tokens: int
    flag_model: str
    reranker: Literal["bge", "llm"] = "llm"


@dataclass(frozen=True)
class Config:
    input: InputConfig
    llama_parser: LlamaParserConfig
    embedding: EmbeddingConfig
    chroma: ChromaConfig
    query: QueryConfig

    def write_to_json_file(self, file_path: str) -> None:
        data: dict[str, Any] = dataclasses.asdict(self)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)



def stable_config_hash(config: Config) -> str:
    data = dataclasses.asdict(config)  # ✅ Works because config is a dataclass
    json_repr = json.dumps(data, sort_keys=True, default=str)
    return hashlib.sha256(json_repr.encode("utf-8")).hexdigest()

def load_and_validate_config(path: str) -> Config:
    model_token_limits = {
        "gpt-3.5-turbo": 4096,
        "gpt-4": 8192,
        "gpt-4-32k": 32768,
        "gpt-4o": 128000,
    }

    try:
        raw = toml.load(path)

        query_model = raw["query"]["model"]
        max_tokens = model_token_limits.get(query_model)

        if max_tokens is None:
            raise ConfigValidationError(f"Unsupported query model: {query_model}")

        return Config(
            input=InputConfig(
                pdf_path=raw["input"]["pdf_path"],
                split = raw["input"]["split"]
            ),
            llama_parser=LlamaParserConfig(
                premium_mode=raw["llama_parser"]["premium_mode"]
            ),
            embedding=EmbeddingConfig(
                model=raw["embedding"]["model"],
                chunk_size=raw["embedding"]["chunk_size"],
                chunk_overlap=raw["embedding"]["chunk_overlap"]
            ),
            chroma=ChromaConfig(
                method=raw["chroma"]["method"],
                threshold=raw["chroma"]["threshold"]
            ),
            query=QueryConfig(
                model=query_model,
                improve_query=raw["query"]["improve_query"],
                max_tokens=max_tokens, 
                flag_model=raw["query"]["flag_model"],
                reranker=raw["query"]["reranker"]
            )
        )

    except KeyError as e:
        raise ConfigValidationError(f"Missing required config key: {e}")
    except TypeError as e:
        raise ConfigValidationError(f"Invalid value in config: {e}")
