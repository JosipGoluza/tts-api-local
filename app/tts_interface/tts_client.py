from app.tts_interface.models.coqui_tts import CoquiTTS
from app.tts_interface.tts_interface import TTSInterface


class TTSClient:
    _available_models = {
        "coqui_tts": CoquiTTS,
    }

    def __init__(self, model_name: str):
        if model_name not in self._available_models:
            raise ValueError(
                f"Unknown TTS model: '{model_name}'. "
                f"Available models: {list(self._available_models.keys())}"
            )

        model_class = self._available_models[model_name]
        self._model: TTSInterface = model_class()

    def generate_speech(self, text: str, output_dir: str = "./output") -> str:
        audio_file_id = self._model.synthesize(text, output_dir)
        return audio_file_id