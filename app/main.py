from fastapi import FastAPI
from pathlib import Path

from app.tts_interface.tts_client import TTSClient

AUDIO_OUTPUT_DIR = Path("./output")
AUDIO_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Local TTS API. Use /docs for API documentation."}

@app.post("/synthesize")
async def synthesize_speech(request: SynthesisRequest):
    try:
        tts_coqui = TTSClient(model_name="coqui_tts")
        coqui_audio = tts_coqui.generate_speech(
            text=request.text,
            output_dir=AUDIO_OUTPUT_DIR,
        )
        return {"message": coqui_audio}
    except Exception as e:
        print(f"\nAn error occurred during Coqui TTS generation: {e}")
        return None
