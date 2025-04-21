from app.tts_interface.models.coqui_tts import CoquiTTS
from app.tts_interface.tts_interface import TTSInterface


class TTSClient:
    _available_strategies = {
        "coqui_tts": CoquiTTS,
    }

    def __init__(self, model_name: str):
        if model_name not in self._available_strategies:
            raise ValueError(
                f"Unknown TTS model: '{model_name}'. "
                f"Available models: {list(self._available_strategies.keys())}"
            )

        print(f"\nSelected TTS Model: {model_name}")
        strategy_class = self._available_strategies[model_name]
        self._strategy: TTSInterface = strategy_class()

    def generate_speech(self, text: str, output_dir: str = "./output") -> str:
        audio_file_id = self._strategy.synthesize(text, output_dir)
        return audio_file_id