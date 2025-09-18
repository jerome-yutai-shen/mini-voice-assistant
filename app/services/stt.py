# -*- coding: utf-8 -*-
"""
Created on Sep 18 08:48:16 2025

@author: Jerome Yutai Shen

"""
from fastapi import UploadFile, HTTPException
from pathlib import Path

ALLOWED_AUDIO_EXTS = {".wav", ".mp3"}
ALLOWED_CONTENT_TYPES = {"audio/wav", "audio/x-wav", "audio/mpeg", "audio/mp3"}


async def sim_stt(file: UploadFile) -> str:
    if Path(file.filename or "").suffix.lower() not in ALLOWED_AUDIO_EXTS:
        raise HTTPException(status_code=415, detail="Unsupported file extension")

    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(status_code=415, detail=f"Unsupported content type: {file.content_type}")


    chunk = await file.read(1024 ** 2)
    if not chunk:
        raise HTTPException(status_code = 400, detail = "Empty audio")

    base = (file.filename or "audio").rsplit(".", 1)[0]
    return f"SIMULATED TRANSCRIPT {base}"