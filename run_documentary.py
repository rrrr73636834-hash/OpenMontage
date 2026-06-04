#!/usr/bin/env python3
"""
Run full documentary pipeline independently.
Usage: python run_documentary.py "Ancient Egypt" --duration 25 --lang ru
"""
import argparse, os, sys, subprocess
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def check(path: str, label: str):
    if not os.path.exists(path) or os.path.getsize(path) < 100:
        print(f"FATAL: {label} failed — {path} missing or empty")
        sys.exit(1)
    print(f"✓ {label}: {path}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("topic", help="Documentary topic")
    ap.add_argument("--duration", type=int, default=25)
    ap.add_argument("--lang", default="ru")
    args = ap.parse_args()

    slug = args.topic.lower().replace(" ", "_")[:20]
    out = Path(f"projects/{slug}")
    out.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*50}")
    print(f"TOPIC: {args.topic}")
    print(f"OUTPUT: {out}/final.mp4")
    print(f"{'='*50}\n")

    # Stage 1: OpenMontage footage
    raw = str(out / "raw.mp4")
    if not os.path.exists(raw):
        print("=== Stage 1: Generating footage via OpenMontage ===")
        subprocess.run([
            "python", "-c",
            f"""
import sys; sys.path.insert(0, '.')
from tools.tool_registry import registry
registry.discover()
# Run documentary montage pipeline
exec(open('.agents/skills/documentary_montage.md').read())
"""
        ], check=False)
        # Fallback: run via make if available
        if not os.path.exists(raw):
            print("Trying direct pipeline run...")
            subprocess.run(
                f'python -m tools.run_pipeline --pipeline documentary_montage '
                f'--topic "{args.topic}" --duration {args.duration} --output {raw}',
                shell=True
            )
    else:
        print(f"✓ Stage 1: Using existing {raw}")
    check(raw, "Raw footage")

    # Stage 2: Script
    script_path = str(out / "script.txt")
    if not os.path.exists(script_path):
        print("\n=== Stage 2: Generating narration script ===")
        script = generate_script(args.topic, args.duration, args.lang)
        Path(script_path).write_text(script, encoding="utf-8")
    check(script_path, "Script")

    # Stage 3: TTS narration
    narr = str(out / "narration.mp3")
    if not os.path.exists(narr):
        print("\n=== Stage 3: Generating narration (edge-tts) ===")
        from tools.tts_edge import generate_narration
        generate_narration(script_path, narr)
    check(narr, "Narration")

    # Stage 4: Subtitles
    srt = str(out / "subtitles.srt")
    if not os.path.exists(srt):
        print("\n=== Stage 4: Generating subtitles (Whisper) ===")
        from tools.subtitles_whisper import generate_srt
        generate_srt(narr, srt, language=args.lang)
    check(srt, "Subtitles")

    # Stage 5: Music
    music = str(out / "music.mp3")
    if not os.path.exists(music):
        print("\n=== Stage 5: Downloading music (Pixabay) ===")
        from tools.music_pixabay import download_music
        download_music(music, mood="cinematic documentary",
                      api_key=os.getenv("PIXABAY_API_KEY", ""))
    check(music, "Music")

    # Stage 6: Final assembly
    final = str(out / "final.mp4")
    print("\n=== Stage 6: Final assembly (FFmpeg) ===")
    from tools.assemble_final import assemble
    assemble(raw, narr, srt, music, final)
    check(final, "Final video")

    print(f"\n{'='*50}")
    print(f"DONE: {final}")
    print(f"{'='*50}")

def generate_script(topic: str, duration: int, lang: str) -> str:
    """Generate narration script. Uses Gemini free API or fallback template."""
    api_key = os.getenv("GOOGLE_API_KEY", "")
    if api_key:
        import requests
        prompt = (
            f"Write a {duration}-minute documentary narration script about: {topic}. "
            f"Language: {lang}. Style: BBC documentary, authoritative, educational. "
            f"No headers, no stage directions. Plain continuous narration text only."
        )
        resp = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/"
            f"gemini-2.0-flash:generateContent?key={api_key}",
            json={"contents": [{"parts": [{"text": prompt}]}]},
            timeout=30
        )
        text = resp.json()["candidates"][0]["content"]["parts"][0]["text"]
        return text
    # Fallback
    return (
        f"Добро пожаловать в документальный фильм о теме: {topic}. "
        f"В этом видео мы изучим историю, факты и значение данной темы. "
        f"Приготовьтесь к увлекательному путешествию в мир знаний."
    )

if __name__ == "__main__":
    main()
