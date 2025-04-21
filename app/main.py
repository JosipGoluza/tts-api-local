from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

from app.tts_interface.tts_client import TTSClient

AUDIO_OUTPUT_DIR = Path("./output")
AUDIO_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
app = FastAPI()


class SynthesisRequest(BaseModel):
    text: str

@app.get("/models")
async def get_available_models():
    return {"models": TTSClient.get_available_models}

@app.post("/synthesize/{model_name}")
async def synthesize_speech(model_name: str, request: SynthesisRequest):
    try:
        tts_coqui = TTSClient(model_name=model_name)
        coqui_audio = tts_coqui.generate_speech(
            text=request.text,
            output_dir=AUDIO_OUTPUT_DIR,
        )
        return {"message": coqui_audio}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

