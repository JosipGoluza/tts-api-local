from abc import ABC, abstractmethod
from pathlib import Path


class TTSInterface(ABC):

    @abstractmethod
    def synthesize(self, text: str, output_dir: Path) -> str:
        pass