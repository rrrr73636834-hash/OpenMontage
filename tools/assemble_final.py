"""FFmpeg final video assembly with narration, subtitles, and music."""
import os
import subprocess


def assemble(
    video_path: str,
    narration_path: str,
    subtitles_path: str,
    music_path: str,
    output_path: str,
) -> str:
    """Combine footage + narration + subtitles + music into final MP4."""
    subtitle_style = (
        "FontName=Arial,FontSize=22,PrimaryColour=&Hffffff&,"
        "OutlineColour=&H000000&,Outline=2,Shadow=1,"
        "Alignment=2,MarginV=30"
    )
    cmd = [
        "ffmpeg", "-y",
        "-i", video_path,
        "-i", narration_path,
        "-i", music_path,
        "-vf", f"subtitles={subtitles_path}:force_style='{subtitle_style}'",
        "-filter_complex",
        "[1:a]volume=1.0[narr];[2:a]volume=0.12[mus];[narr][mus]amix=inputs=2:duration=first[audio]",
        "-map", "0:v",
        "-map", "[audio]",
        "-c:v", "libx264", "-preset", "fast", "-crf", "20",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        output_path,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"FFmpeg failed:\n{result.stderr[-2000:]}")

    size_mb = os.path.getsize(output_path) / 1024 / 1024
    assert size_mb > 10, f"FAILED: output too small ({size_mb:.1f} MB)"
    print(f"OK: final video saved to {output_path} ({size_mb:.1f} MB)")
    return output_path
