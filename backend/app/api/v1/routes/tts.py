from fastapi import APIRouter, Query
from fastapi.responses import StreamingResponse
from app.services.tts_service import generate_speech
import io

router = APIRouter()

@router.get("/tts")
def get_tts(text: str = Query(...)):
    result = generate_speech(text)
    audio_data = result["audio"]
    timings = result["timings"]
    
    # Return audio stream
    return StreamingResponse(
        io.BytesIO(audio_data),
        media_type="audio/wav",
        headers={"X-Timings": str(timings)} if timings else {}
    )