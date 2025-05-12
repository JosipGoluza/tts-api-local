import subprocess
from pathlib import Path
from random import random

from app.tts_interface.tts_interface import TTSInterface


class PiperTTS(TTSInterface):
    def __init__(self, model_name: str):
        self.model_name = model_name

    def synthesize(self, text: str, output_dir: Path, voices_dir: Path) -> str:
        file_hash = abs(hash(text + str(random())))
        output_filename = f"{file_hash}.wav"
        output_path = output_dir / output_filename

        try:
            process = subprocess.Popen(
                [
                    "piper",
                    "--model", self.model_name,
                    "--output_file", str(output_path),
                    "--data_dir", voices_dir,
                    "--download_dir", voices_dir,
                ],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding = 'utf-8', # kako bi prihvaćao hrvatska slova
            )

            stdout, stderr = process.communicate(input=text)

            if process.returncode != 0:
                raise RuntimeError(f"Piper TTS failed: {stderr}")

            return str(file_hash)

        except Exception as e:
            raise RuntimeError(f"Failed to synthesize speech using Piper: {str(e)}")