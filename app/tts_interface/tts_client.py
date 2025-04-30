from pathlib import Path

from app.tts_interface.models.coqui_tts import CoquiTTS
from app.tts_interface.tts_interface import TTSInterface


class TTSClient:
    _available_models = {
        "coqui_tts": CoquiTTS("tts_models/hr/cv/vits"),
        "coqui_xtts_v2": CoquiTTS("tts_models/multilingual/multi-dataset/xtts_v2"),
        "coqui_bark": CoquiTTS("tts_models/multilingual/multi-dataset/bark"),
    }

    def __init__(self, model_name: str):
        if model_name not in self._available_models:
            raise ValueError(
                f"Unknown TTS model: '{model_name}'. "
                f"Available models: {list(self._available_models.keys())}"
            )

        self._model: TTSInterface = self._available_models[model_name]

    def generate_speech(self, text: str, output_dir: Path) -> str:
        audio_file_id = self._model.synthesize(text, output_dir)
        return audio_file_id

    @classmethod
    def get_available_models(cls) -> list[str]:
        return list(cls._available_models.keys())
