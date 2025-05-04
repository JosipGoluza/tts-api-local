import os
from pathlib import Path
from random import random

import torch
from TTS.api import TTS

from app.tts_interface.tts_interface import TTSInterface


class CoquiTTS(TTSInterface):

    def __init__(self, coqui_model_name):
        self.coqui_model_name = coqui_model_name
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tts_model = TTS(coqui_model_name).to(self.device)

    def synthesize(self, text: str, output_dir: Path) -> str:
        file_hash = abs(hash(text + str(random())))
        output_filename = f"{file_hash}.wav"
        output_path = os.path.join(output_dir, output_filename)

        if self.coqui_model_name == "tts_models/multilingual/multi-dataset/xtts_v2":
            self.tts_model.tts_to_file(
                text=text,
                file_path=output_filename,
                speaker="Tanja Adelina",
                language="en",
            )
        else:
            self.tts_model.tts_to_file(
                text=text,
                file_path=output_filename
            )

        # save from default location to output folder
        if os.path.exists(output_filename):
            os.replace(output_filename, output_path)

        return str(file_hash)