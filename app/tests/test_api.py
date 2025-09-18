# -*- coding: utf-8 -*-
"""
Created on Sep 18 08:49:26 2025

@author: Jerome Yutai Shen

"""
import io
import wave
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def _dummy_wav() -> bytes:
    """tiny valid wav header with silence"""
    buf = io.BytesIO()
    with wave.open(buf, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(8000)
        w.writeframes(b"\x00\x00" * 100)
    return buf.getvalue()


def test_stt_ok():
    files = {"file": ("hello_world.wav", _dummy_wav(), "audio/wav")}
    r = client.post("/stt", files=files)
    assert r.status_code == 200
    assert "SIMULATED TRANSCRIPT" in r.json()["text"]


def test_tts_ok():
    r = client.post("/tts", json={"text": "hello"})
    assert r.status_code == 200
    assert r.headers["content-type"].startswith("audio/wav")


def test_stt_bad_type():
    files = {"file": ("note.txt", b"oops", "text/plain")}
    r = client.post("/stt", files=files)
    assert r.status_code == 415