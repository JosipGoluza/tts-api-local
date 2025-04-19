import os
import tempfile

import torch
from TTS.api import TTS

from app.tts_interface.tts_interface import TTSInterface


class CoquiTTS(TTSInterface):

    def __init__(self, model_name="tts_models/hr/cv/vits"):
        print(f"Initializing Coqui TTS model: {model_name}...")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tts_model = TTS(model_name).to(self.device)
        print(f"Coqui TTS initialized on device: {self.device}")

    def synthesize(self, text: str, output_dir: str) -> str:
        print(f"Synthesizing with Coqui TTS: '{text[:50]}...'")

        if output_dir is None:
            output_dir = tempfile.gettempdir()
        os.makedirs(output_dir, exist_ok=True)

        file_hash = abs(hash(text))
        output_filename = f"{file_hash}.wav"
        output_path = os.path.join(output_dir, output_filename)

        self.tts_model.tts_to_file(
            text=text,
            file_path=output_path
        )

        print(f"Audio saved by Coqui TTS to: {output_path}")
        return output_filename