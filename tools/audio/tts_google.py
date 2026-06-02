"""
Google Cloud TTS — best quality for Russian.
Free tier: 1M Neural2 characters/month, 4M Standard/month.
Uses GOOGLE_API_KEY from .env (same key as Gemini).
"""
import os
import requests
import base64
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

GOOGLE_KEY = os.getenv("GOOGLE_API_KEY", "")

VOICES = {
    "ru": {"name": "ru-RU-Neural2-B", "lang": "ru-RU"},  # deep male Russian
    "en": {"name": "en-US-Neural2-D", "lang": "en-US"},  # deep male English
    "ru_female": {"name": "ru-RU-Neural2-A", "lang": "ru-RU"},
    "en_female": {"name": "en-US-Neural2-F", "lang": "en-US"},
}


def is_available() -> bool:
    return bool(GOOGLE_KEY)


def generate(text: str, output_path: str,
             lang: str = "ru",
             speaking_rate: float = 0.85,
             pitch: float = -2.0) -> str:
    """
    Generate narration via Google Cloud TTS Neural2.
    speaking_rate: 0.75=slow, 0.85=documentary, 1.0=normal
    pitch: -4=deep, 0=normal, +4=high
    Chunks text to handle 5000 char API limit.
    """
    if not GOOGLE_KEY:
        raise RuntimeError("GOOGLE_API_KEY not set in .env")

    voice_cfg = VOICES.get(lang, VOICES["en"])
    url = f"https://texttospeech.googleapis.com/v1/text:synthesize?key={GOOGLE_KEY}"

    # Chunk text into 4500 char pieces
    chunks = [text[i:i+4500] for i in range(0, len(text), 4500)]
    audio_parts = []

    for j, chunk in enumerate(chunks):
        payload = {
            "input": {"text": chunk},
            "voice": {"languageCode": voice_cfg["lang"],
                      "name": voice_cfg["name"]},
            "audioConfig": {
                "audioEncoding": "MP3",
                "speakingRate": speaking_rate,
                "pitch": pitch,
                "effectsProfileId": ["large-home-entertainment-class-device"]
            }
        }

        resp = requests.post(url, json=payload, timeout=30)
        data = resp.json()

        if "audioContent" not in data:
            raise RuntimeError(f"Google TTS error: {data.get('error', data)}")

        audio_parts.append(base64.b64decode(data["audioContent"]))
        print(f"  🔊 Google TTS chunk {j+1}/{len(chunks)}")

    # Concatenate all parts
    combined = b"".join(audio_parts)
    Path(output_path).write_bytes(combined)

    size_kb = Path(output_path).stat().st_size // 1024
    print(f"  ✅ Google TTS: {output_path} ({size_kb}KB)")
    return output_path
