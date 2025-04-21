from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

from app.tts_interface.tts_client import TTSClient

AUDIO_OUTPUT_DIR = Path("./output")
AUDIO_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    # Add more origins as needed.
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

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


@app.get("/stream/{hash_id}")
async def stream_audio(hash_id: str):
    try:
        file_path = AUDIO_OUTPUT_DIR / f"{hash_id}.wav"
        print(f"Attempting to stream file: {file_path}")

        if not file_path.is_file():
            raise HTTPException(status_code=404, detail=f"Audio file '{hash_id}.wav' not found.")

        return FileResponse(
            path=file_path,
            media_type='audio/wav',  # Explicitly set the MIME type
            filename=f"{hash_id}.wav"  # Suggest a filename for download
        )

    except HTTPException as http_exc:
        raise http_exc
