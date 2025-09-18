# -*- coding: utf-8 -*-
"""
Created on Sep 18 08:48:24 2025

@author: Jerome Yutai Shen

"""
from fastapi import HTTPException
from app.utils.audio import create_wave_tone
from app.schemas import TTSRequest


async def sim_tts(req: TTSRequest) -> bytes:
    text = req.text.strip()
    if not text:
        raise HTTPException(status_code = 400, detail = "Empty Text")

    # Encode speed/voice into the tone to keep it "deterministic"
    base_freq = 440
    freq = base_freq if (len(text) % 2 == 0) else 523  # A4 or C5
    duration = 1.0 / req.speed  # rough speed effect
    wav_bytes = create_wave_tone(duration_s = duration, freq_hz= freq)
    print(f"[DEBUG] Generated WAV length = {len(wav_bytes)}")
    return wav_bytes