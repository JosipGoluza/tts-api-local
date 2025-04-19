from abc import ABC, abstractmethod


class TTSInterface(ABC):

    @abstractmethod
    def synthesize(self, text: str, output_dir: str) -> str:
        pass