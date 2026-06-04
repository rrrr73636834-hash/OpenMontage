#!/usr/bin/env python3
"""Unified launcher for niche video production.

Run with: python3 make_video.py <niche> <topic> <duration> [--use-kaggle]
"""
import argparse
import os
import subprocess
import sys
from pathlib import Path

from documentary import (
    concat_clips,
    download_clip,
    ffprobe_duration,
    gen_narration,
    gen_script,
    gen_subtitles,
    get_background,
    normalize_clip,
    ok,
)
from niche_presets import NICHES
from soundscape import generate_audio


def verify_exists(path: Path, label: str):
    if not path.exists() or path.stat().st_size < 1024:
        raise FileNotFoundError(f"Stage failed: {label} missing or invalid: {path}")
    print(f"✅ Verified {label}: {path}")


def build_image_slideshow(images: list[Path], output_video: Path, clip_length: int = 6):
    workdir = output_video.parent / "slides"
    workdir.mkdir(parents=True, exist_ok=True)
    clip_paths = []
    for index, image in enumerate(images, start=1):
        clip_path = workdir / f"slide_{index:03d}.mp4"
        zoom = f"zoompan=z='min(zoom+0.0005,1.08)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={clip_length*25}:s=1920x1080:fps=25"
        subprocess.run([
            "ffmpeg", "-y", "-loop", "1", "-i", str(image),
            "-vf", zoom,
            "-t", str(clip_length),
            "-c:v", "libx264", "-preset", "slow", "-crf", "24",
            "-pix_fmt", "yuv420p", str(clip_path),
        ], check=True)
        clip_paths.append(clip_path)
    manifest = workdir / "video_list.txt"
    with manifest.open("w", encoding="utf-8") as handle:
        for clip_path in clip_paths:
            handle.write(f"file '{clip_path.resolve()}'\n")
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", str(manifest), "-c", "copy", str(output_video)], check=True)
    return output_video


def create_visuals(niche: str, preset: dict, output_dir: Path, use_kaggle: bool) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    slideshow = output_dir / "visuals.mp4"
    if use_kaggle:
        kaggle_dir = Path("kaggle_output") / niche
        images = sorted(kaggle_dir.glob("*.png")) if kaggle_dir.exists() else []
        if images:
            print(f"Using {len(images)} Kaggle images for {niche}")
            build_image_slideshow(images[:6], slideshow)
            verify_exists(slideshow, "Kaggle slideshow")
            return slideshow
        print("No Kaggle images found, falling back to footage")

    terms = preset.get("search_terms", [])
    clips_dir = output_dir / "clips"
    clips_dir.mkdir(parents=True, exist_ok=True)
    clips = []
    clip_sec = max(4, int(30 / max(1, len(terms))))
    for idx, term in enumerate(terms, start=1):
        raw_path = clips_dir / f"raw_{idx:03d}.mp4"
        clip_path = clips_dir / f"clip_{idx:03d}.mp4"
        print(f"Downloading footage for: {term}")
        if download_clip(term, str(raw_path)) and normalize_clip(str(raw_path), str(clip_path), clip_sec):
            clips.append(str(clip_path))
            continue
        get_background(niche, str(clip_path))
        clips.append(str(clip_path))
    concat_clips(clips, str(slideshow))
    verify_exists(slideshow, "Visuals")
    return slideshow


def mix_audio(narration: Path, music: Path, output: Path) -> Path:
    temp = output.with_suffix(".mixed.mp3")
    subprocess.run([
        "ffmpeg", "-y",
        "-i", str(narration),
        "-i", str(music),
        "-filter_complex",
        "[1:a]volume=0.25[a1];[0:a][a1]amix=inputs=2:dropout_transition=3",
        "-c:a", "libmp3lame", "-q:a", "2", str(temp)
    ], check=True)
    verify_exists(temp, "Mixed audio")
    return temp


def assemble_video(visuals: Path, audio: Path, subtitles: Path, output: Path):
    cmd = [
        "ffmpeg", "-y", "-i", str(visuals), "-i", str(audio),
        "-c:v", "libx264", "-preset", "medium", "-crf", "22",
        "-c:a", "aac", "-b:a", "192k", "-pix_fmt", "yuv420p",
        "-shortest",
    ]
    if subtitles.exists():
        cmd.extend(["-vf", f"subtitles={str(subtitles)}"])
    cmd.append(str(output))
    subprocess.run(cmd, check=True)
    verify_exists(output, "Final video")
    return output


def main():
    parser = argparse.ArgumentParser(description="Produce a niche YouTube video from topic and duration.")
    parser.add_argument("niche", choices=NICHES.keys())
    parser.add_argument("topic")
    parser.add_argument("duration", type=int)
    parser.add_argument("--use-kaggle", action="store_true")
    args = parser.parse_args()

    preset = NICHES[args.niche]
    project = Path("productions") / args.niche / args.topic.replace(" ", "_")[:40]
    project.mkdir(parents=True, exist_ok=True)
    script_path = project / "script.txt"
    visuals_path = project / "visuals.mp4"
    narration_path = project / "narration.mp3"
    subtitles_path = project / "subtitles.srt"
    music_path = project / "music.mp3"
    mixed_audio_path = project / "mixed_audio.mp3"
    final_path = project / "final.mp4"

    if not script_path.exists():
        script = gen_script(args.topic, args.duration, lang="en")
        script_path.write_text(script, encoding="utf-8")
    verify_exists(script_path, "Script")

    visuals_path = create_visuals(args.niche, preset, project, args.use_kaggle)

    if not narration_path.exists():
        gen_narration(str(script_path), str(narration_path), lang="en")
    verify_exists(narration_path, "Narration")

    if not subtitles_path.exists():
        gen_subtitles(str(narration_path), str(subtitles_path), lang="en")
    verify_exists(subtitles_path, "Subtitles")

    if not music_path.exists():
        generate_audio(preset["music_mood"], args.duration, str(music_path))
    verify_exists(music_path, "Music")

    mixed_audio = mix_audio(narration_path, music_path, mixed_audio_path)
    assemble_video(visuals_path, mixed_audio, subtitles_path, final_path)

    print(f"\nFinal video created: {final_path}")


if __name__ == "__main__":
    main()
