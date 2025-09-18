# -*- coding: utf-8 -*-
"""
Created on Sep 18 08:46:18 2025

@author: Jerome Yutai Shen

"""
from pydantic import BaseModel, Field


class TTSRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=2000)
    speed: float = Field(1.0, ge = 0.5, le = 2.0, description = "Playback speed hint")
    voice: str | None = Field(None, description = "Mock voice id")