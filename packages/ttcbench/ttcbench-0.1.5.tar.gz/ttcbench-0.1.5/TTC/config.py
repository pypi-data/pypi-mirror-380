# TTC/config.py
from typing import Optional, List
from pydantic import BaseModel, ConfigDict

# 🔧 дефолты (подправишь при необходимости)
DEFAULT_BASE_URL = "http://87.255.209.214:3000/v1"
DEFAULT_MODEL_ID = "Qwen2.5-72B-Instruct-GPTQ-Int4"

class BenchConfig(BaseModel):
    model_config = ConfigDict(protected_namespaces=())

    # базовые
    task: str = "textgen"
    backend: str = "openai"

    # значения по умолчанию
    base_url: str = DEFAULT_BASE_URL
    model_id: str = DEFAULT_MODEL_ID

    # внутренние параметры бенча (юзер их не трогает)
    warmup_steps: int = 0
    steps: int = 1
    batch_size: int = 1
    seq_in: int = 0
    seq_out: int = 256
    prompt: Optional[str] = None
    timeout_s: int = 120
    endpoint: Optional[str] = None

    # генерация (все опционально для юзера)
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    stream: bool = False
    json_mode: bool = False
    system: Optional[str] = None
    stop: Optional[List[str]] = None

    # auth
    api_key: Optional[str] = None
