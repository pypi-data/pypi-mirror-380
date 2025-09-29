import json, os, time
from typing import Dict

def write_jsonl(path: str, record: Dict):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

def stamp() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S")
