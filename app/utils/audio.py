# -*- coding: utf-8 -*-
"""
Created on Sep 18 08:48:44 2025

@author: Jerome Yutai Shen

"""
import io
import wave
import math


def create_wave_tone(duration_s: float = 1.0,
                     sample_rate: int = 16000,
                     freq_hz: float = 440,
                     wave_type: str = "tone"
                    ) -> bytes:
    num_samples = int(duration_s * sample_rate)
    buf = io.BytesIO()
    with wave.open(buf, 'wb') as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2) # 16 bit
        wav.setframerate(sample_rate)
        frames = bytearray()
        for idx in range(num_samples):
            if wave_type.lower() == "tone":
                values = int(32767 * 0.2 * math.sin(2 * math.pi * freq_hz * (idx / sample_rate)))
            else:
                values = 0
            frames += int(values).to_bytes(2, byteorder = "little", signed=True)
        wav.writeframes(bytes(frames))
    return buf.getvalue()