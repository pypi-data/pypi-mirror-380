from abc import ABC, abstractmethod
from .config import BenchConfig

class BenchRunner(ABC):
    def __init__(self, cfg: BenchConfig, gpu_index: int = 0):
        self.cfg = cfg
        self.gpu_index = gpu_index

    @abstractmethod
    def run(self) -> dict:
        ...
