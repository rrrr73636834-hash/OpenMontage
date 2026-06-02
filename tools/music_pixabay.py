"""Download cinematic background music from Pixabay free API."""
import os
import requests
from pathlib import Path


def download_music(output_path: str, mood: str = "cinematic", api_key: str = "") -> str:
    """Download royalty-free music. Falls back to silence if no key."""
    if not api_key:
        api_key = os.getenv("PIXABAY_API_KEY", "")

    if api_key:
        url = "https://pixabay.com/api/videos/music/"
        params = {"key": api_key, "q": mood, "per_page": 5}
        resp = requests.get(url, params=params, timeout=15)
        hits = resp.json().get("hits", [])
        if hits:
            track_url = hits[0]["audio"]["url"]
            audio = requests.get(track_url, timeout=30).content
            Path(output_path).write_bytes(audio)
            print(f"OK: music downloaded to {output_path}")
            return output_path

    # Fallback: generate 1800s silence via ffmpeg
    os.system(f'ffmpeg -f lavfi -i anullsrc=r=44100:cl=stereo -t 1800 -q:a 9 -acodec libmp3lame {output_path} -y')
    print(f"OK: silence fallback saved to {output_path}")
    return output_path
