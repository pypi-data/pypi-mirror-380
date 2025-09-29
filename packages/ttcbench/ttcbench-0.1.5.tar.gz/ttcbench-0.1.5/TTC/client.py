# TTC/client.py
import os
from typing import Any, Dict, List, Optional, Tuple
import requests

from .config import DEFAULT_BASE_URL, DEFAULT_MODEL_ID

def _env(n: str, d: Optional[str] = None) -> Optional[str]:
    return os.getenv(n, d)

def _headers(api_key: Optional[str]) -> Dict[str, str]:
    h = {"Content-Type": "application/json"}
    if api_key:
        h["Authorization"] = f"Bearer {api_key}"
    return h

def _get_json(session: requests.Session, url: str, headers: Dict[str, str], timeout: int) -> Dict[str, Any]:
    r = session.get(url, headers=headers, timeout=timeout)
    r.raise_for_status()
    return r.json()

def _post_json(session: requests.Session, url: str, headers: Dict[str, str], body: Dict[str, Any], timeout: int) -> Dict[str, Any]:
    r = session.post(url, headers=headers, json=body, timeout=timeout)
    r.raise_for_status()
    return r.json()

def _resolve_base_and_model(base_url: Optional[str], model: Optional[str], timeout: int, api_key: Optional[str]) -> Tuple[str, str]:
    """base_url/model: cfg/ENV/DEFAULT + резолв короткого имени через /v1/models."""
    base = (base_url or _env("MODEL_BASE_URL") or DEFAULT_BASE_URL).rstrip("/")
    want = model or _env("DEFAULT_MODEL") or DEFAULT_MODEL_ID

    sess = requests.Session()
    hdrs = _headers(api_key or _env("MODEL_API_KEY"))

    data = _get_json(sess, base + "/models", hdrs, timeout).get("data", [])
    # точное совпадение
    for m in data:
        if m.get("id") == want:
            return base, want
    # по суффиксу /wanted
    cand = [m.get("id") for m in data if str(m.get("id","")).endswith("/"+want)]
    if cand:
        return base, cand[0]
    # по basename
    def base_name(s: str) -> str: return s.rstrip("/").split("/")[-1]
    cand2 = [m.get("id") for m in data if base_name(str(m.get("id",""))) == want]
    if cand2:
        return base, cand2[0]
    raise RuntimeError(f"Model '{want}' not found at {base}/models. Available: {[m.get('id') for m in data]}")

def chat(
    prompt: str,
    *,
    model: Optional[str] = None,
    system: Optional[str] = None,
    temperature: Optional[float] = None,
    top_p: Optional[float] = None,
    max_tokens: int = 256,
    stop: Optional[List[str]] = None,
    json_mode: bool = False,
    stream: bool = False,
    timeout_s: int = 120,
    api_key: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Отправляет один запрос в vLLM OpenAI /v1/chat/completions.
    Юзер указывает ТОЛЬКО текст и опциональные параметры модели.

    Возвращает dict: {
        "text": <ответ ассистента>,
        "raw": <полный ответ сервера>,
        "model_id": <итоговый id модели>,
        "endpoint": <использованный URL>
    }
    """
    base, model_id = _resolve_base_and_model(None, model, timeout_s, api_key)
    url = base + "/chat/completions"
    sess = requests.Session()
    hdrs = _headers(api_key or _env("MODEL_API_KEY"))

    body: Dict[str, Any] = {
        "model": model_id,
        "messages": [],
        "max_tokens": max_tokens,
    }
    if system:
        body["messages"].append({"role": "system", "content": system})
    body["messages"].append({"role": "user", "content": prompt})

    if temperature is not None: body["temperature"] = temperature
    if top_p is not None:       body["top_p"] = top_p
    if stream:                  body["stream"] = True
    if stop:                    body["stop"] = stop
    if json_mode:               body["response_format"] = {"type": "json_object"}

    resp = _post_json(sess, url, hdrs, body, timeout_s)

    # вытащим текст (первый choice)
    text = None
    try:
        text = resp["choices"][0]["message"]["content"]
    except Exception:
        pass

    return {
        "text": text,
        "raw": resp,
        "model_id": model_id,
        "endpoint": url,
    }
