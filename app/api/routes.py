# -*- coding: utf-8 -*-
"""
Created on Sep 18 08:47:43 2025

@author: Jerome Yutai Shen

"""
import io
from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse, StreamingResponse
from app.schemas import TTSRequest
from app.services.stt import sim_stt
from app.services.tts import sim_tts


router = APIRouter()

@router.post("/stt")
async def stt_endpoint(file: UploadFile):
    transcript = await sim_stt(file)
    return JSONResponse({"text": transcript})

@router.post("/tts")
async def tts_endpoint(payload: TTSRequest):
    wav_bytes = await sim_tts(payload)
    return StreamingResponse(
        content = io.BytesIO(wav_bytes),
        media_type = "audio/wav",
        headers = {"Content-Disposition": "attachment; filename = speech.wav"}
    )
