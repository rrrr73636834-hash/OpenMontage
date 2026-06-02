"""
Kokoro-82M TTS tool — best free English TTS.
Apache 2.0 license. Local inference, no API key needed.
Voices: af_heart, af_bella, am_adam, am_michael, bf_emma, bm_lewis
"""
import os
import sys
import soundfile as sf
from pathlib import Path


def is_available() -> bool:
    try:
        import kokoro
        return True
    except ImportError:
        return False


def install():
    os.system("pip install kokoro>=0.9.4 soundfile -q")


def generate(text: str, output_path: str,
             voice: str = "am_michael",
             speed: float = 0.9) -> str:
    """
    Generate English narration with Kokoro-82M.
    voice options: am_michael (deep male), af_heart (warm female),
                   bm_lewis (british male), bf_emma (british female)
    speed: 0.8=slow documentary, 1.0=normal, 1.2=fast
    """
    if not is_available():
        print("Installing Kokoro...")
        install()

    from kokoro import KPipeline
    import numpy as np

    pipeline = KPipeline(lang_code="a")  # 'a'=American English, 'b'=British

    audio_chunks = []
    generator = pipeline(text, voice=voice, speed=speed, split_pattern=r'\n+')

    for i, (gs, ps, audio) in enumerate(generator):
        audio_chunks.append(audio)
        print(f"  🔊 Chunk {i+1} synthesized")

    if not audio_chunks:
        raise RuntimeError("Kokoro generated no audio")

    combined = np.concatenate(audio_chunks)

    # Save as WAV then convert to MP3 via ffmpeg
    wav_path = output_path + ".wav"
    sf.write(wav_path, combined, 24000)

    import subprocess
    subprocess.run([
        "ffmpeg", "-y", "-i", wav_path,
        "-q:a", "2", output_path
    ], capture_output=True, check=True)
    os.unlink(wav_path)

    size_kb = Path(output_path).stat().st_size // 1024
    print(f"  ✅ Kokoro narration: {output_path} ({size_kb}KB)")
    return output_path
