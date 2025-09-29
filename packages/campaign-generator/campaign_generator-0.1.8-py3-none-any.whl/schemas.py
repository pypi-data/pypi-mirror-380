from pydantic import BaseModel

class InitializeRagRequest(BaseModel):
    chat_model: str = "gemma3:1b"
    embedding_model: str = "nomic-embed-text:latest"

class TextRequest(BaseModel):
    text: str
    task_id: str | None = None
    chat_model: str = "gemma3:1b"
    embedding_model: str = "nomic-embed-text:latest"


class RagRequest(BaseModel):
    chat_model: str = "gemma3:1b"
    embedding_model: str = "nomic-embed-text:latest"
    question: str
    mode: str = "local"
    top_k: int = 5
    similarity_threshold: float = 0.0
    max_tokens: int = 2048