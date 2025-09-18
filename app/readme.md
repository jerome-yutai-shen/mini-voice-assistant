# Mini Voice Assistant API

A simple **FastAPI** application that simulates:

- **STT (Speech-to-Text)** → accepts an audio file and returns dummy transcribed text.  
- **TTS (Text-to-Speech)** → accepts JSON text and returns a generated `.wav` file.  

This is **not real STT/TTS**, only a mock implementation for demo and testing purposes.

---
## File structure
```bash
app
├── __init__.py
├── api
│    ├── __init__.py
│    └── routes.py
├── main.py
├── readme.md
├── schemas.py
├── services
│    ├── stt.py
│    └── tts.py
├── tests
│    └── test_api.py
├── utils
│    └── audio.py
├── Dockerfile
├── requirements.txt
└── sample_wav.wav
```

## Run Locally (without Docker)

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate

2. Install dependencies:
   ```bash
    pip install -r requirements.txt

3. Start the app:
   ```bash
   uvicorn app.main:app --reload --port 8000

4. Open Swagger UI in your browser:
    http://127.0.0.1:8000/docs

## Run with Docker
1. Build the image (from project root):
   ```bash
   docker build -t mini-voice-assistant .
   
2. Run the container:
   ```bash
   docker run --rm -p 8000:8000 mini-voice-assistant
   
3. Open Swagger UI in your browser:
    http://127.0.0.1:8000/docs

### Note: 
inside the container the app binds to 0.0.0.0:8000 (all interfaces).
On your host machine, always use http://127.0.0.1:8000.

## Example Usage

1. STT (Speech-to-Text)
```bash
curl -X POST "http://127.0.0.1:8000/stt" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@sample_wav.wav"
   ```
You can use the sample_wav.wav in the **project root directory**. 

Response   
```json
    {
      "text": "SIMULATED TRANSCRIPT sample_wav"
    }
```
2. TTS (Text-to-Speech)
```bash
curl -X POST "http://127.0.0.1:8000/tts" \
  -H "accept: audio/wav" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello world", "speed": 1.0, "voice": "test"}' \
  --output speech.wav
```
It creates a download url, click to download it.

## Unit test
To run tests, make sure you are in the **project root directory** (where `Dockerfile` and `requirements.txt` are located, not inside the `app/` folder):
```bash
python -m pytest app -q
```