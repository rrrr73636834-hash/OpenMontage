#!/usr/bin/env python3
"""
Documentary Factory — полный пайплайн.
Footage качаем напрямую с Pexels/Pixabay API.
Usage: python documentary.py "Ancient Egypt" --duration 25
"""
import argparse
import asyncio
import os
import re
import subprocess
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

PEXELS_KEY = os.getenv("PEXELS_API_KEY", "")
PIXABAY_KEY = os.getenv("PIXABAY_API_KEY", "")
OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY", "")
GEMINI_KEY = os.getenv("GEMINI_API_KEY", "")
GOOGLE_KEY = os.getenv("GOOGLE_API_KEY", "")
TTS_VOICE = "en-US-GuyNeural"
FALLBACK_MODELS = [
    "meta-llama/llama-3.3-70b-instruct:free",
    "deepseek/deepseek-r1:free",
    "qwen/qwen3-235b-a22b:free",
]
BLACKLIST_TOKENS = {
    "modern", "office", "car", "phone", "computer", "soviet", "concrete",
    "neon", "tourist", "2020", "2021", "2022", "2023", "2024", "2025",
}


def ok(path: str, label: str, min_kb: int = 10):
    p = Path(path)
    if not p.exists() or p.stat().st_size < min_kb * 1024:
        print(f"\n❌ FATAL: {label} → {path} missing or too small")
        sys.exit(1)
    print(f"✅ {label} ({p.stat().st_size // 1024} KB)")


def ffprobe_duration(path: str) -> float:
    result = subprocess.run(
        [
            "ffprobe", "-v", "quiet", "-show_entries", "format=duration",
            "-of", "csv=p=0", path,
        ],
        capture_output=True,
        text=True,
    )
    try:
        return float(result.stdout.strip())
    except Exception:
        return 0.0


def is_blacklisted(text: str) -> bool:
    text_lower = text.lower()
    return any(token in text_lower for token in BLACKLIST_TOKENS)


def gen_script(topic: str, minutes: int, lang: str = "en") -> str:
    words = minutes * 130
    lang_instruction = (
        "Write in Russian language, BBC style, authoritative tone." 
        if lang == "ru" else
        "Write in English language, BBC documentary style, authoritative cinematic tone."
    )
    prompt = (
        f"Write a {minutes}-minute documentary narration script about: {topic}. "
        f"Length: {words} words. {lang_instruction} "
        f"Plain narration text only, no headers, no stage directions."
    )

    if not OPENROUTER_KEY:
        raise SystemExit("❌ OPENROUTER_API_KEY не задан. Проверь .env")

    models = []
    try:
        response = requests.get(
            "https://openrouter.ai/api/v1/models",
            headers={"Authorization": f"Bearer {OPENROUTER_KEY}"},
            timeout=15,
        )
        data = response.json().get("data", [])
        free_models = [
            m["id"]
            for m in data
            if str(m.get("pricing", {}).get("prompt", "1")) == "0"
        ]
        free_models = sorted(
            free_models,
            key=lambda mid: next(
                (m.get("context_length", 0) for m in data if m.get("id") == mid),
                0,
            ),
            reverse=True,
        )
        models.extend(free_models)
        print(f"  🔍 Найдено бесплатных моделей: {len(free_models)}")
    except Exception as exc:
        print(f"  ⚠️ Не удалось получить список моделей: {exc}")

    for fallback in FALLBACK_MODELS:
        if fallback not in models:
            models.append(fallback)

    for model in models:
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENROUTER_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 4000,
                    "temperature": 0.3,
                },
                timeout=60,
            )
            payload = response.json()
            choices = payload.get("choices", [])
            content = ""
            if choices:
                content = choices[0].get("message", {}).get("content", "").strip()
            if content:
                print(f"  ✅ Использована модель: {model}")
                return content
            print(f"  ⚠️ {model}: пустой ответ")
        except Exception as exc:
            print(f"  ⚠️ {model}: {exc}")

    raise SystemExit("❌ Не удалось получить скрипт из OpenRouter. Проверь ключ и сеть.")


# ── STAGE 2: FOOTAGE ─────────────────────────────────────
def search_terms(script: str, n: int) -> list[str]:
    tokens = [w.strip(".,;:!?()[]«»\"'") for w in script.split() if len(w) > 3]
    chunk = max(1, len(tokens) // n)
    terms = []
    for i in range(n):
        segment = tokens[i * chunk : (i + 1) * chunk]
        keywords = [w for w in segment if len(w) > 4][:3]
        terms.append(" ".join(keywords) if keywords else "documentary footage")
    return terms


def download_file(url: str, path: str) -> bool:
    try:
        with requests.get(url, timeout=60, stream=True) as response:
            response.raise_for_status()
            with open(path, "wb") as handle:
                for chunk in response.iter_content(65536):
                    if chunk:
                        handle.write(chunk)
        return True
    except Exception:
        return False


def download_clip_from_pexels(query: str, path: str) -> bool:
    if not PEXELS_KEY:
        return False
    try:
        response = requests.get(
            "https://api.pexels.com/videos/search",
            headers={"Authorization": PEXELS_KEY},
            params={"query": query, "per_page": 10, "orientation": "landscape"},
            timeout=15,
        )
        for video in response.json().get("videos", []):
            metadata = " ".join(
                [
                    str(video.get("url", "")),
                    str(video.get("user", {}).get("name", "")),
                    str(video.get("tags", "")),
                ]
            )
            if is_blacklisted(metadata):
                continue
            files = sorted(
                [
                    f
                    for f in video.get("video_files", [])
                    if f.get("quality") in {"hd", "sd"}
                ],
                key=lambda f: f.get("width", 0),
                reverse=True,
            )
            if not files:
                continue
            if download_file(files[0].get("link", ""), path):
                return ffprobe_duration(path) > 3
    except Exception:
        pass
    return False


def download_clip_from_pixabay(query: str, path: str) -> bool:
    if not PIXABAY_KEY:
        return False
    try:
        response = requests.get(
            "https://pixabay.com/api/videos/",
            params={"key": PIXABAY_KEY, "q": query, "per_page": 10},
            timeout=15,
        )
        for hit in response.json().get("hits", []):
            metadata = " ".join([str(hit.get("tags", "")), str(hit.get("pageURL", ""))])
            if is_blacklisted(metadata):
                continue
            video_info = hit.get("videos", {})
            url = (video_info.get("large") or video_info.get("medium") or {}).get("url", "")
            if not url:
                continue
            if download_file(url, path):
                return ffprobe_duration(path) > 3
    except Exception:
        pass
    return False


def download_clip_from_ytdlp(query: str, path: str) -> bool:
    """Download documentary footage from YouTube using yt-dlp."""
    try:
        import yt_dlp
        search_query = f"ytsearch3:{query} documentary footage no copyright"
        opts = {
            'format': 'best[ext=mp4][filesize<50M]',
            'quiet': True,
            'no_warnings': True,
            'socket_timeout': 30,
        }
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(search_query, download=False)
            if info and isinstance(info, dict) and 'entries' in info:
                for entry in info.get('entries', []):
                    if entry and 'url' in entry:
                        opts['outtmpl'] = path.rsplit('.', 1)[0]
                        with yt_dlp.YoutubeDL(opts) as ydl_dl:
                            ydl_dl.download([entry['url']])
                        if Path(path).exists():
                            return ffprobe_duration(path) > 3
    except Exception:
        pass
    return False

def download_clip(query: str, path: str) -> bool:
    if download_clip_from_ytdlp(query, path):
        return True
    if download_clip_from_pexels(query, path):
        return True
    if download_clip_from_pixabay(query, path):
        return True
    return False


def normalize_clip(raw_path: str, output_path: str, duration: int) -> bool:
    cmd = [
        "ffmpeg", "-y", "-i", raw_path,
        "-t", str(duration),
        "-vf", "scale=1920:1080:force_original_aspect_ratio=decrease," +
               "pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1",
        "-c:v", "libx264", "-preset", "fast", "-an", output_path,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0 and Path(output_path).exists()


def collect_footage(terms: list[str], clips_dir: Path, clip_sec: int) -> list[str]:
    clips = []
    for index, term in enumerate(terms, start=1):
        raw_path = clips_dir / f"raw_{index:03d}.mp4"
        clip_path = clips_dir / f"clip_{index:03d}.mp4"
        if clip_path.exists() and ffprobe_duration(str(clip_path)) > 2:
            print(f"  ♻️  [{index}/{len(terms)}] reuse: {term}")
            clips.append(str(clip_path))
            continue
        print(f"  📥 [{index}/{len(terms)}] {term}")
        if download_clip(term, str(raw_path)) and normalize_clip(str(raw_path), str(clip_path), clip_sec):
            clips.append(str(clip_path))
            continue
        print(f"  ⚠️ [{index}/{len(terms)}] placeholder black pad")
        subprocess.run([
            "ffmpeg", "-y", "-f", "lavfi",
            "-i", f"color=c=black:size=1920x1080:duration={clip_sec}:rate=24",
            "-c:v", "libx264", str(clip_path),
        ], capture_output=True)
        clips.append(str(clip_path))
    return clips


def concat_clips(clips: list[str], output: str):
    manifest = output + ".txt"
    with open(manifest, "w", encoding="utf-8") as f:
        for clip in clips:
            f.write(f"file '{os.path.abspath(clip)}'\n")
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", manifest, "-c", "copy", output,
    ], check=True, capture_output=True)
    os.remove(manifest)


# ── STAGE 3: TTS ─────────────────────────────────────────
async def _tts_edge(text: str, path: str, voice: str = TTS_VOICE):
    import edge_tts
    await edge_tts.Communicate(text, voice, rate="-8%").save(path)


def gen_narration(script_path: str, output_path: str, lang: str = "ru"):
    """
    Auto-selects best available TTS by language and availability.
    Priority: Google TTS > Kokoro (English only) > edge-tts
    Then applies audio enhancement for broadcast quality.
    """
    from tools.audio import tts_google, tts_kokoro

    text = Path(script_path).read_text("utf-8")
    raw_audio = output_path + ".raw.mp3"

    # Route by language and availability
    if False:  # Google TTS disabled - requires OAuth2
        pass

    elif lang == "en" and tts_kokoro.is_available():
        print("  🎙 Using: Kokoro-82M (English) — voice: am_michael")
        tts_kokoro.generate(text, raw_audio, voice="am_michael", speed=0.88)

    elif lang == "en":
        # Try to install and use Kokoro
        tts_kokoro.install()
        if tts_kokoro.is_available():
            print("  🎙 Using: Kokoro-82M (English) — voice: am_michael")
            tts_kokoro.generate(text, raw_audio, voice="am_michael", speed=0.88)
        else:
            # Fallback to edge-tts English
            print("  🎙 Fallback: edge-tts (English)")
            asyncio.run(_tts_edge(text, raw_audio, voice="en-US-GuyNeural"))

    else:
        # Default: edge-tts
        print("  🎙 Using: edge-tts")
        asyncio.run(_tts_edge(text, raw_audio, TTS_VOICE))

    # Always enhance audio quality
    from tools.audio.audio_enhance import enhance_voice
    enhance_voice(raw_audio, output_path)
    if os.path.exists(raw_audio):
        os.unlink(raw_audio)


# ── STAGE 4: SUBTITLES ───────────────────────────────────
from faster_whisper import WhisperModel


def fmt_timestamp(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds % 1) * 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


def gen_subtitles(audio: str, srt: str, lang: str = "ru"):
    model = WhisperModel("small", device="cpu", compute_type="int8")
    segments, _ = model.transcribe(audio, language=lang, word_timestamps=True)
    lines = []
    for idx, seg in enumerate(segments, start=1):
        lines.append(
            f"{idx}\n{fmt_timestamp(seg.start)} --> {fmt_timestamp(seg.end)}\n{seg.text.strip()}\n"
        )
    Path(srt).write_text("\n".join(lines), encoding="utf-8")


# ── STAGE 5: MUSIC ───────────────────────────────────────
def get_music(out: str, duration: int):
    if PIXABAY_KEY:
        try:
            response = requests.get(
                "https://pixabay.com/api/videos/music/",
                params={
                    "key": PIXABAY_KEY,
                    "q": "cinematic documentary orchestral epic",
                    "per_page": 10,
                },
                timeout=15,
            )
            for hit in response.json().get("hits", []):
                url = hit.get("audio", {}).get("url", "")
                if not url:
                    continue
                tmp_path = out + ".tmp.mp3"
                if not download_file(url, tmp_path):
                    continue
                result = subprocess.run([
                    "ffmpeg", "-y", "-stream_loop", "-1",
                    "-i", tmp_path, "-t", str(duration), "-c", "copy", out,
                ], capture_output=True)
                Path(tmp_path).unlink(missing_ok=True)
                if result.returncode == 0 and Path(out).exists():
                    return
        except Exception:
            pass
    subprocess.run([
        "ffmpeg", "-y", "-f", "lavfi",
        "-i", "anullsrc=r=44100:cl=stereo",
        "-t", str(duration), "-q:a", "9", "-acodec", "libmp3lame", out,
    ], capture_output=True)


# ── STAGE 6: ASSEMBLY ────────────────────────────────────
def assemble(video: str, narr: str, srt: str, music: str, output: str):
    dur = int(ffprobe_duration(narr))
    fade_out = max(0, dur - 4)
    subtitle_style = (
        "FontName=Arial,FontSize=24,Bold=1,"
        "PrimaryColour=&Hffffff&,OutlineColour=&H000000&,"
        "Outline=2,Shadow=1,Alignment=2,MarginV=35"
    )
    vf_chain = ",".join([
        "crop=iw:ih*0.88:0:ih*0.06",
        "scale=1920:1080:force_original_aspect_ratio=decrease",
        "pad=1920:1080:(ow-iw)/2:(oh-ih)/2",
        "curves=r='0/0 0.2/0.08 0.8/0.62 1/0.82':g='0/0 0.2/0.10 0.8/0.63 1/0.82':b='0/0.06 0.5/0.40 1/0.78'",
        "eq=contrast=1.4:brightness=-0.10:saturation=0.60",
        "noise=alls=8:allf=t+u",
        "vignette=PI/4",
        "unsharp=5:5:0.8:3:3:0.4",
        f"fade=t=in:st=0:d=0.5,fade=t=out:st={fade_out}:d=1.0",
        f"subtitles={srt}:force_style='{subtitle_style}'",
    ])
    audio_filter = (
        f"[1:a]volume=1.0,afade=t=in:d=0.5,afade=t=out:st={fade_out}:d=1.5[narr];"
        f"[2:a]volume=0.12,afade=t=in:d=3,afade=t=out:st={fade_out}:d=3[mus];"
        "[narr][mus]amix=inputs=2:duration=first[audio]"
    )
    subprocess.run([
        "ffmpeg", "-y",
        "-i", video, "-i", narr, "-i", music,
        "-vf", vf_chain,
        "-filter_complex", audio_filter,
        "-map", "0:v", "-map", "[audio]",
        "-c:v", "libx264", "-preset", "fast", "-crf", "20",
        "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        output,
    ], check=True)


# ── MAIN ─────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("topic")
    ap.add_argument("--duration", type=int, default=25)
    ap.add_argument("--lang", default="ru")
    ap.add_argument("--clips", type=int, default=None)
    a = ap.parse_args()

    slug = re.sub(r"[^\w]", "_", a.topic.lower())[:25]
    out = Path(f"projects/{slug}")
    out.mkdir(parents=True, exist_ok=True)
    clips_dir = out / "clips"
    clips_dir.mkdir(exist_ok=True)

    n_clips = a.clips or a.duration * 2
    clip_sec = (a.duration * 60) // n_clips + 3

    print(
        f"\n{'═'*48}\n  📽  DOCUMENTARY FACTORY\n"
        f"  Тема: {a.topic}\n  Длина: {a.duration} мин\n{'═'*48}"
    )

    script_path = str(out / "script.txt")
    if not Path(script_path).exists():
        Path(script_path).write_text(gen_script(a.topic, a.duration), encoding="utf-8")
    ok(script_path, "Script", 1)

    raw_path = str(out / "raw.mp4")
    if not Path(raw_path).exists() or ffprobe_duration(raw_path) < 30:
        terms = search_terms(Path(script_path).read_text(encoding="utf-8"), n_clips)
        clips = collect_footage(terms, clips_dir, clip_sec)
        concat_clips(clips, raw_path)
    ok(raw_path, "Raw footage", 100)

    narration_path = str(out / "narration.mp3")
    if not Path(narration_path).exists():
        gen_narration(script_path, narration_path)
    ok(narration_path, "Narration", 10)

    subtitles_path = str(out / "subtitles.srt")
    if not Path(subtitles_path).exists():
        gen_subtitles(narration_path, subtitles_path, a.lang)
    ok(subtitles_path, "Subtitles", 1)

    music_path = str(out / "music.mp3")
    if not Path(music_path).exists():
        get_music(music_path, int(ffprobe_duration(narration_path)))
    ok(music_path, "Music", 1)

    final_path = str(out / "final.mp4")
    assemble(raw_path, narration_path, subtitles_path, music_path, final_path)
    ok(final_path, "Final", 1000)

    final_duration = int(ffprobe_duration(final_path))
    final_size_mb = Path(final_path).stat().st_size // 1024 // 1024
    print(
        f"\n{'═'*48}\n  ✅ ГОТОВО: {final_path}\n"
        f"  Длина: {final_duration//60}:{final_duration%60:02d}\n"
        f"  Размер: {final_size_mb} MB\n{'═'*48}\n"
    )


if __name__ == "__main__":
    main()
