from fastapi import FastAPI

from app.tts_interface.tts_client import TTSClient

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Local TTS API. Use /docs for API documentation."}

@app.post("/synthesize")
async def synthesize_speech():
    my_text = "Bok svijete. Ovo je probni tekst za testiranje ljepote i točnosti modela."
    try:
        tts_coqui = TTSClient(model_name="coqui_tts")
        coqui_audio = tts_coqui.generate_speech(
            text=my_text,
        )
        return {"message": coqui_audio}
    except Exception as e:
        print(f"\nAn error occurred during Coqui TTS generation: {e}")
        return None
