"""
Audio post-processing: normalize, compress, EQ for documentary voice.
Makes any TTS sound more professional and broadcast-ready.
"""
import subprocess
import os


def enhance_voice(input_path: str, output_path: str) -> str:
    """
    Apply broadcast-standard voice processing chain:
    1. Normalize to -3dB LUFS
    2. High-pass filter (cut below 80Hz — removes rumble)
    3. De-ess (reduce sibilance)
    4. Dynamic compression (makes voice consistent)
    5. Slight warmth EQ boost at 3kHz (presence)
    """
    filters = ",".join([
        "highpass=f=80",
        "equalizer=f=3000:width_type=h:width=2000:g=2",
        "equalizer=f=8000:width_type=h:width=4000:g=-1.5",
        "acompressor=threshold=-20dB:ratio=3:attack=5:release=50:makeup=2dB",
        "loudnorm=I=-16:TP=-1.5:LRA=11",
    ])

    subprocess.run([
        "ffmpeg", "-y", "-i", input_path,
        "-af", filters,
        "-c:a", "libmp3lame", "-q:a", "2",
        output_path
    ], check=True, capture_output=True)

    print(f"  ✅ Audio enhanced: {output_path}")
    return output_path
