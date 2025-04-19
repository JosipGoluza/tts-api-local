from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Local TTS API. Use /docs for API documentation."}

@app.post("/synthesize")
async def synthesize_speech():
    # TODO: Implement TTS synthesis logic
    raise HTTPException(status_code=501, detail="Not Implemented Yet")
