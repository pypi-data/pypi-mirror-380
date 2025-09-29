from typing import Optional, List
from pydantic import BaseModel, ConfigDict

class BenchConfig(BaseModel):
    model_config = ConfigDict(protected_namespaces=())

    # core
    task: str = "textgen"                # "textgen"
    backend: str = "openai"              # "openai"
    model_id: Optional[str] = None

    # benchmark settings
    warmup_steps: int = 5
    steps: int = 30
    batch_size: int = 1
    seq_in: int = 0                      # not used for OpenAI; kept for compatibility
    seq_out: int = 128                   # maps to max_tokens
    prompt: Optional[str] = None
    system: Optional[str] = None
    seed: int = 123

    # HTTP/OpenAI (vLLM) connection
    base_url: Optional[str] = None       # e.g. http://host:3000/v1
    api_key: Optional[str] = None
    timeout_s: int = 120
    endpoint: Optional[str] = None       # explicit endpoint override

    # generation params (optional)
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    stream: bool = False                 # we set it but do not consume stream in bench
    stop: Optional[List[str]] = None
    json_mode: bool = False              # response_format={"type":"json_object"} if True
