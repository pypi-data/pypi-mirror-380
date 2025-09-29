import time
from typing import Dict, List
from .utils_nvml import sample_gpu

class MetricSink:
    def __init__(self, gpu_index: int = 0):
        self.gpu_index = gpu_index
        self.samples: List[Dict] = []
        self.t0 = None

    def start(self):
        self.t0 = time.perf_counter()

    def tick(self):
        s = sample_gpu(self.gpu_index) or {}
        s["t"] = time.perf_counter()
        self.samples.append(s)

    def stop(self):
        return {
            "wall_time_s": time.perf_counter() - self.t0 if self.t0 else None,
            "gpu_samples": self.samples
        }
