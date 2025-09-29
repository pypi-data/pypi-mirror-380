import os, time
from typing import Dict, Any, List, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

from .config import BenchConfig
from .runner_base import BenchRunner
from .metrics import MetricSink

def _env(n, d=None): return os.getenv(n, d)

def _headers(api_key: Optional[str]) -> Dict[str,str]:
    h = {"Content-Type": "application/json"}
    if api_key: h["Authorization"] = f"Bearer {api_key}"
    return h

def _get_json(session: requests.Session, url: str, headers: Dict[str,str], timeout: int) -> Dict[str,Any]:
    r = session.get(url, headers=headers, timeout=timeout)
    r.raise_for_status()
    return r.json()

def _post_json(session: requests.Session, url: str, headers: Dict[str,str], body: Dict[str,Any], timeout: int) -> Dict[str,Any]:
    r = session.post(url, headers=headers, json=body, timeout=timeout)
    r.raise_for_status()
    return r.json()

def _mk_payload_chat(cfg: BenchConfig, model_id: str, prompt: str, max_tokens: int) -> Dict[str, Any]:
    body: Dict[str, Any] = {
        "model": model_id,
        "messages": [],
        "max_tokens": max_tokens,
    }
    # system
    if cfg.system:
        body["messages"].append({"role": "system", "content": cfg.system})
    body["messages"].append({"role": "user", "content": prompt})

    # optional params
    if cfg.temperature is not None: body["temperature"] = cfg.temperature
    if cfg.top_p is not None:       body["top_p"] = cfg.top_p
    if cfg.stream:                  body["stream"] = True
    if cfg.stop:                    body["stop"] = cfg.stop
    if cfg.json_mode:               body["response_format"] = {"type": "json_object"}

    return body

def _pick_model_id(session: requests.Session, base_url: str, headers: Dict[str,str], wanted: str, timeout: int) -> str:
    """Resolve short name -> full id using /v1/models."""
    js = _get_json(session, base_url.rstrip("/") + "/models", headers, timeout)
    data = js.get("data", []) if isinstance(js, dict) else []

    # exact
    for m in data:
        mid = m.get("id")
        if mid == wanted:
            return mid

    # suffix match
    cand = [m.get("id") for m in data if isinstance(m, dict) and str(m.get("id","")).endswith("/"+wanted)]
    if cand: return cand[0]

    # basename match
    def base(s: str) -> str: return s.rstrip("/").split("/")[-1]
    cand2 = [m.get("id") for m in data if isinstance(m, dict) and base(str(m.get("id",""))) == wanted]
    if cand2: return cand2[0]

    raise RuntimeError(f"Model '{wanted}' not found on {base_url}/models. Available: {[m.get('id') for m in data]}")

def _extract_total_tokens(resp: Dict[str,Any]) -> Optional[int]:
    if not isinstance(resp, dict): return None
    usage = resp.get("usage")
    if isinstance(usage, dict) and "total_tokens" in usage:
        try: return int(usage["total_tokens"])
        except Exception: return None
    return None

class OpenAITextGenRunner(BenchRunner):
    """Bench for /v1/chat/completions (fallback /v1/completions if needed)."""
    def run(self) -> dict:
        cfg = self.cfg
        base_url = (cfg.base_url or _env("MODEL_BASE_URL") or "").rstrip("/")
        api_key  = cfg.api_key or _env("MODEL_API_KEY", "")
        model_in = cfg.model_id or _env("DEFAULT_MODEL", "")

        if not base_url: raise RuntimeError("MODEL_BASE_URL is required")
        if not model_in: raise RuntimeError("model_id/DEFAULT_MODEL is required")

        session = requests.Session()
        headers = _headers(api_key)

        # resolve model id
        model_id = _pick_model_id(session, base_url, headers, model_in, cfg.timeout_s)

        # choose endpoint
        url = base_url + "/chat/completions"
        if cfg.endpoint:
            ep = cfg.endpoint.lstrip("/")
            if ep.endswith("completions"): url = base_url + "/" + ep

        # warmup
        warm = _mk_payload_chat(cfg, model_id, cfg.prompt or "warmup", max(1, min(8, cfg.seq_out)))
        for _ in range(max(0, cfg.warmup_steps)):
            try: _post_json(session, url, headers, warm, cfg.timeout_s)
            except Exception: pass

        # run
        sink = MetricSink(gpu_index=0)
        latencies: List[float] = []
        total_tokens = 0
        total_requests = 0

        prompt = cfg.prompt or "Напиши короткий ответ на русском одним предложением."
        sink.start()
        t0 = time.perf_counter()

        for _ in range(cfg.steps):
            body = _mk_payload_chat(cfg, model_id, prompt, cfg.seq_out)
            t_step = time.perf_counter()
            futs = []
            with ThreadPoolExecutor(max_workers=cfg.batch_size) as ex:
                for _b in range(cfg.batch_size):
                    futs.append(ex.submit(_post_json, session, url, headers, body, cfg.timeout_s))
                for f in as_completed(futs):
                    dt = time.perf_counter() - t_step
                    latencies.append(dt)
                    total_requests += 1
                    try:
                        resp = f.result()
                        tt = _extract_total_tokens(resp)
                        if tt: total_tokens += int(tt)
                    except Exception:
                        pass
            sink.tick()

        wall = time.perf_counter() - t0
        stats = sink.stop()
        return {
            "task": "textgen",
            "backend": "openai",
            "endpoint": url,
            "model_id": model_id,
            "base_url": base_url,
            "batch_size": cfg.batch_size,
            "seq_out": cfg.seq_out,
            "steps": cfg.steps,
            "requests_total": total_requests,
            "wall_time_s": round(wall, 4),
            "avg_latency_s": round(sum(latencies)/len(latencies), 4) if latencies else None,
            "tokens_total": int(total_tokens),
            "tok_per_s": round(total_tokens/wall, 2) if wall>0 else None,
            **stats
        }
