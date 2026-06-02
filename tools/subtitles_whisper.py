"""Subtitle generation using faster-whisper."""
import os
from faster_whisper import WhisperModel


def generate_srt(audio_path: str, output_srt: str, language: str = "ru") -> str:
    """Transcribe audio and write SRT subtitle file."""
    model = WhisperModel("small", device="cpu", compute_type="int8")
    segments, _ = model.transcribe(audio_path, language=language, word_timestamps=True)

    lines = []
    idx = 1
    for seg in segments:
        start = _fmt(seg.start)
        end = _fmt(seg.end)
        lines.append(f"{idx}\n{start} --> {end}\n{seg.text.strip()}\n")
        idx += 1

    with open(output_srt, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    assert os.path.exists(output_srt), f"FAILED: {output_srt} not created"
    print(f"OK: subtitles saved to {output_srt} ({idx-1} segments)")
    return output_srt


def _fmt(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds % 1) * 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"
