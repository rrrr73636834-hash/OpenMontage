#!/usr/bin/env python3
"""
Documentary Factory — гибрид Codespace + Kaggle.
Codespace: скрипт, TTS, субтитры, стоки, музыка, сборка.
Kaggle: только FLUX картинки (GPU).
"""
import argparse, asyncio, json, os, re, subprocess, sys, time
from pathlib import Path
import requests
from dotenv import load_dotenv

load_dotenv()

PEXELS_KEY      = os.getenv("PEXELS_API_KEY","")
PIXABAY_KEY     = os.getenv("PIXABAY_API_KEY","")
OPENROUTER_KEY  = os.getenv("OPENROUTER_API_KEY","")
KAGGLE_USER     = os.getenv("KAGGLE_USERNAME","")
KAGGLE_KEY      = os.getenv("KAGGLE_KEY","")

FALLBACK_MODELS = [
    "google/gemma-4-26b-a4b-it:free",
    "moonshotai/kimi-k2.6:free",
    "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
    "meta-llama/llama-3.3-70b-instruct:free",
    "deepseek/deepseek-r1:free",
]

# ── 1. SCRIPT ──────────────────────────────────────────────────────────────

def gen_script(topic: str, minutes: int, lang: str = "en") -> str:
    words = minutes * 130
    instr = ("BBC documentary style, authoritative cinematic tone."
             if lang == "en" else "BBC стиль, авторитетный тон.")
    prompt = (f"Write a {minutes}-minute documentary narration about: {topic}. "
              f"Length: {words} words. {instr} "
              f"Plain narration only, no headers, no stage directions.")
    for model in FALLBACK_MODELS:
        try:
            r = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={"Authorization": f"Bearer {OPENROUTER_KEY}",
                         "Content-Type": "application/json"},
                json={"model": model, "messages": [{"role":"user","content":prompt}],
                      "max_tokens": 4000, "temperature": 0.3},
                timeout=90)
            content = r.json()["choices"][0]["message"]["content"].strip()
            if len(content) > 200:
                print(f"✅ Script: {model} ({len(content.split())} words)")
                return content
        except Exception as e:
            print(f"⚠️  {model}: {e}")
    raise RuntimeError("❌ Script generation failed")

# ── 2. TTS — Kokoro ────────────────────────────────────────────────────────

def gen_narration(script_path: str, output_path: str, voice: str = "bm_lewis") -> None:
    import soundfile as sf
    import numpy as np
    from kokoro import KPipeline
    text = Path(script_path).read_text("utf-8")
    lang_code = "b" if voice.startswith("b") else "a"
    pipeline = KPipeline(lang_code=lang_code)
    chunks = []
    for _, _, audio in pipeline(text, voice=voice, speed=0.88,
                                split_pattern=r"(?<=[.!?])\s+"):
        chunks.append(audio)
    if not chunks:
        raise RuntimeError("Kokoro empty output")
    combined = np.concatenate(chunks)
    wav = Path(output_path).with_suffix(".wav")
    sf.write(str(wav), combined, 24000)
    subprocess.run(["ffmpeg","-y","-i",str(wav),
                    "-c:a","libmp3lame","-q:a","2",output_path],
                   check=True, capture_output=True)
    wav.unlink(missing_ok=True)
    print(f"✅ Narration: {Path(output_path).stat().st_size//1024} KB")

# ── 3. SUBTITLES — Whisper CPU ─────────────────────────────────────────────

def gen_subtitles(audio_path: str, srt_path: str, lang: str = "en") -> None:
    from faster_whisper import WhisperModel
    # CPU tiny — быстро; если есть GPU используем large-v3
    try:
        model = WhisperModel("large-v3", device="cuda", compute_type="float16")
        print("✅ Whisper: large-v3 GPU")
    except Exception:
        model = WhisperModel("tiny", device="cpu", compute_type="int8")
        print("⚠️  Whisper: tiny CPU")
    segments, _ = model.transcribe(audio_path, language=lang,
                                   word_timestamps=True, beam_size=5)
    def ts(s):
        h=int(s//3600); m=int((s%3600)//60)
        sec=int(s%60); ms=int((s%1)*1000)
        return f"{h:02}:{m:02}:{sec:02},{ms:03}"
    lines = []
    for i, seg in enumerate(segments, 1):
        lines.append(f"{i}\n{ts(seg.start)} --> {ts(seg.end)}\n{seg.text.strip()}\n")
    Path(srt_path).write_text("\n".join(lines), encoding="utf-8")
    print(f"✅ Subtitles: {len(lines)} segments")

# ── 4. IMAGES — Kaggle FLUX или Pollinations fallback ──────────────────────

def _kaggle_flux_images(script: str, style: str, n: int, out_dir: Path) -> list:
    """Отправляет задачу на Kaggle T4 — только генерация картинок."""
    import tempfile, shutil, zipfile
    from pathlib import Path

    sentences = [s.strip() for s in script.replace("\n"," ").split(".")
                 if len(s.strip()) > 20]
    step = max(1, len(sentences)//n)
    scenes = [" ".join(sentences[i*step:(i+1)*step])[:200] for i in range(n)]

    nb = {
        "nbformat":4,"nbformat_minor":0,
        "metadata":{"kernelspec":{"display_name":"Python 3",
                                  "language":"python","name":"python3"},
                    "kaggle":{"accelerator":"nvidiaTeslaT4"}},
        "cells":[
            {"cell_type":"code","metadata":{},"outputs":[],"execution_count":None,
             "source":[
                f"scenes = {json.dumps(scenes)}\n",
                f"style = {json.dumps(style)}\n",
                "import subprocess, sys\n",
                "subprocess.run([sys.executable,'-m','pip','install','-q',\n",
                "    'diffusers','transformers','accelerate','safetensors','torch'], check=True)\n",
                "from diffusers import FluxPipeline\n",
                "import torch\n",
                "from pathlib import Path\n",
                "out = Path('/kaggle/working')\n",
                "pipe = FluxPipeline.from_pretrained(\n",
                "    'black-forest-labs/FLUX.1-schnell',\n",
                "    torch_dtype=torch.float16)\n",
                "pipe.enable_sequential_cpu_offload()\n",
                "pipe.enable_attention_slicing()\n",
                "for i,scene in enumerate(scenes):\n",
                "    img = pipe(f'{scene}, {style}',\n",
                "        num_inference_steps=4, guidance_scale=0.0,\n",
                "        height=1080, width=1920).images[0]\n",
                "    img.save(str(out/f'img_{i:03d}.png'))\n",
                "    print(f'done {i+1}/{len(scenes)}')\n",
             ]},
        ]
    }

    tmpdir = Path(tempfile.mkdtemp())
    (tmpdir/"kernel.ipynb").write_text(json.dumps(nb))
    slug = f"forts-flux-images"
    meta = {"id":f"{KAGGLE_USER}/{slug}","title":"FORTS FLUX Images",
            "code_file":"kernel.ipynb","language":"python",
            "kernel_type":"notebook","is_private":True,
            "enable_gpu":True,"enable_internet":True,
            "dataset_sources":[],"competition_sources":[],"kernel_sources":[]}
    (tmpdir/"kernel-metadata.json").write_text(json.dumps(meta))

    # Setup kaggle creds
    kdir = Path.home()/".kaggle"
    kdir.mkdir(exist_ok=True)
    (kdir/"kaggle.json").write_text(json.dumps({"username":KAGGLE_USER,"key":KAGGLE_KEY}))
    (kdir/"kaggle.json").chmod(0o600)

    r = subprocess.run(["kaggle","kernels","push","-p",str(tmpdir)],
                       capture_output=True, text=True)
    shutil.rmtree(tmpdir)
    if r.returncode != 0:
        raise RuntimeError(f"Kaggle push failed: {r.stderr}")
    print(f"✅ Kaggle FLUX kernel pushed")

    # Wait
    full_slug = f"{KAGGLE_USER}/{slug}"
    for _ in range(120):
        time.sleep(30)
        s = subprocess.run(["kaggle","kernels","status",full_slug],
                           capture_output=True, text=True).stdout.strip()
        print(f"  Kaggle: {s}")
        if "complete" in s.lower(): break
        if "error" in s.lower(): raise RuntimeError("Kaggle kernel error")

    # Download
    dl_dir = out_dir
    dl_dir.mkdir(exist_ok=True)
    subprocess.run(["kaggle","kernels","output",full_slug,"-p",str(dl_dir)],
                   check=True, capture_output=True)
    paths = sorted(dl_dir.glob("img_*.png"))
    print(f"✅ Kaggle: {len(paths)} images downloaded")
    return paths

def _pollinations_images(script: str, style: str, n: int, out_dir: Path) -> list:
    """Fallback — Pollinations.ai бесплатно без ключа."""
    sentences = [s.strip() for s in script.replace("\n"," ").split(".")
                 if len(s.strip()) > 20]
    step = max(1, len(sentences)//n)
    out_dir.mkdir(exist_ok=True)
    paths = []
    for i in range(n):
        scene = " ".join(sentences[i*step:(i+1)*step])[:150]
        prompt = f"{scene}, {style}"
        url = f"https://image.pollinations.ai/prompt/{requests.utils.quote(prompt)}?width=1920&height=1080&nologo=true"
        for attempt in range(3):
            try:
                r = requests.get(url, timeout=60)
                if r.status_code == 200 and len(r.content) > 10000:
                    p = out_dir/f"img_{i:03d}.png"
                    p.write_bytes(r.content)
                    paths.append(p)
                    print(f"  🎨 [{i+1}/{n}] Pollinations ok")
                    break
            except Exception as e:
                print(f"  ⚠️  attempt {attempt+1}: {e}")
                time.sleep(5)
    return paths

def gen_images(script: str, style: str, n: int, out_dir: Path) -> list:
    """Kaggle FLUX если доступен, иначе Pollinations."""
    if KAGGLE_USER and KAGGLE_KEY:
        try:
            return _kaggle_flux_images(script, style, n, out_dir)
        except Exception as e:
            print(f"⚠️  Kaggle failed: {e} — falling back to Pollinations")
    return _pollinations_images(script, style, n, out_dir)

# ── 5. MUSIC — Pixabay ─────────────────────────────────────────────────────

def get_music(output_path: str, duration_sec: int, mood: str = "cinematic") -> None:
    if PIXABAY_KEY:
        try:
            r = requests.get("https://pixabay.com/api/videos/music/",
                params={"key":PIXABAY_KEY,"q":mood,"per_page":5}, timeout=15)
            for hit in r.json().get("hits",[]):
                url = hit.get("audio",{}).get("url","")
                if not url: continue
                data = requests.get(url, timeout=30)
                tmp = Path(output_path).with_suffix(".tmp.mp3")
                tmp.write_bytes(data.content)
                subprocess.run(["ffmpeg","-y","-stream_loop","-1",
                    "-i",str(tmp),"-t",str(duration_sec),
                    "-c:a","libmp3lame","-q:a","4",output_path],
                    check=True, capture_output=True)
                tmp.unlink(missing_ok=True)
                print(f"✅ Music: {Path(output_path).stat().st_size//1024} KB")
                return
        except Exception as e:
            print(f"⚠️  Pixabay music: {e}")
    # Silent fallback
    subprocess.run(["ffmpeg","-y","-f","lavfi","-i",
        "anullsrc=r=44100:cl=stereo","-t",str(duration_sec),
        "-c:a","libmp3lame","-q:a","9",output_path],
        check=True, capture_output=True)
    print("⚠️  Silent audio fallback")

# ── 6. VISUALS — Ken Burns ─────────────────────────────────────────────────

def build_visuals(image_paths: list, duration_sec: int, output_path: str) -> None:
    n = len(image_paths)
    clip_dur = max(4, duration_sec // n)
    clips_dir = Path(output_path).parent / "clips"
    clips_dir.mkdir(exist_ok=True)
    movements = [
        "zoompan=z='min(zoom+0.0008,1.5)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={d}:s=1920x1080",
        "zoompan=z=1.3:x='if(lte(on,1),0,x+1.2)':y='ih/2-(ih/zoom/2)':d={d}:s=1920x1080",
        "zoompan=z='if(lte(on,1),1.5,max(1,zoom-0.0008))':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={d}:s=1920x1080",
        "zoompan=z=1.3:x='iw/2-(iw/zoom/2)':y='if(lte(on,1),0,y+0.8)':d={d}:s=1920x1080",
    ]
    clip_paths = []
    for i, img in enumerate(image_paths):
        cp = clips_dir/f"clip_{i:03d}.mp4"
        mv = movements[i % len(movements)].format(d=clip_dur*25)
        subprocess.run([
            "ffmpeg","-y","-loop","1","-i",str(img),
            "-vf",f"{mv},scale=1920:1080,setsar=1",
            "-t",str(clip_dur),"-c:v","libx264",
            "-preset","fast","-crf","20","-pix_fmt","yuv420p","-r","25",str(cp)
        ], check=True, capture_output=True)
        clip_paths.append(cp)
        print(f"  🎬 [{i+1}/{n}]")
    manifest = clips_dir/"list.txt"
    manifest.write_text("\n".join(f"file '{p.resolve()}'" for p in clip_paths))
    subprocess.run(["ffmpeg","-y","-f","concat","-safe","0",
                    "-i",str(manifest),"-c","copy",output_path],
                   check=True, capture_output=True)
    print(f"✅ Visuals: {Path(output_path).stat().st_size//1024//1024} MB")

# ── 7. ASSEMBLE ────────────────────────────────────────────────────────────

GRADES = {
    "cold_cyan":     "curves=r=0/0 0.2/0.08 0.8/0.62 1/0.82:g=0/0 0.2/0.10 0.8/0.63 1/0.82:b=0/0.06 0.8/0.8 1/1",
    "warm_gold":     "curves=r=0/0 0.5/0.6 1/1:g=0/0 0.5/0.5 1/0.9:b=0/0 0.5/0.3 1/0.7,eq=saturation=1.2",
    "midnight_blue": "curves=r=0/0 0.5/0.35 1/0.75:g=0/0 0.5/0.4 1/0.8:b=0/0.1 0.5/0.6 1/1,eq=brightness=-0.05",
}

def ffprobe_dur(path: str) -> int:
    r = subprocess.check_output(["ffprobe","-v","quiet",
        "-show_entries","format=duration","-of","csv=p=0",path])
    return int(float(r.decode().strip()))

def assemble(visuals: str, narration: str, music: str,
             subtitles: str, output: str, color_grade: str = "cold_cyan") -> None:
    grade = GRADES.get(color_grade, GRADES["cold_cyan"])
    sub_style = ("FontName=Arial,FontSize=22,Bold=1,"
                 "PrimaryColour=&Hffffff&,OutlineColour=&H000000&,"
                 "Outline=2,Shadow=1,Alignment=2,MarginV=40")
    narr_dur = ffprobe_dur(narration)
    fade_out = max(0, narr_dur - 4)
    vf = ",".join([
        "scale=1920:1080:force_original_aspect_ratio=decrease",
        "pad=1920:1080:(ow-iw)/2:(oh-ih)/2",
        grade, "noise=alls=4:allf=t+u", "vignette=PI/5",
        f"subtitles={subtitles}:force_style='{sub_style}'",
    ])
    af = (f"[1:a]volume=1.0,afade=t=in:d=0.5,afade=t=out:st={fade_out}:d=4[narr];"
          f"[2:a]volume=0.12,afade=t=in:d=3,afade=t=out:st={fade_out}:d=4[mus];"
          f"[narr][mus]amix=inputs=2:duration=first[audio]")
    subprocess.run([
        "ffmpeg","-y",
        "-i",visuals,"-i",narration,"-i",music,
        "-vf",vf,"-filter_complex",af,
        "-map","0:v","-map","[audio]",
        "-c:v","libx264","-profile:v","high","-level:v","4.0",
        "-preset","medium","-crf","18","-r","25",
        "-c:a","aac","-b:a","192k","-ar","44100",
        "-pix_fmt","yuv420p","-movflags","+faststart","-shortest",
        output
    ], check=True)
    dur = ffprobe_dur(output)
    size = Path(output).stat().st_size//1024//1024
    print(f"\n✅ FINAL: {output}")
    print(f"   {dur//60}:{dur%60:02d} | {size} MB")

# ── MAIN ───────────────────────────────────────────────────────────────────

def ok(path: str, label: str, min_kb: int = 10) -> None:
    p = Path(path)
    if not p.exists() or p.stat().st_size < min_kb*1024:
        sys.exit(f"❌ {label}: {path}")
    print(f"✅ {label} ({p.stat().st_size//1024} KB)")

def main():
    from niche_presets import NICHES
    ap = argparse.ArgumentParser()
    ap.add_argument("topic")
    ap.add_argument("--niche", default="financial_crime", choices=list(NICHES.keys()))
    ap.add_argument("--duration", type=int, default=10)
    ap.add_argument("--lang", default="en")
    a = ap.parse_args()

    preset = NICHES[a.niche]
    slug = re.sub(r"[^\w]","_", a.topic.lower())[:30]
    out = Path("productions") / a.niche / slug
    out.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*50}")
    print(f"🎬 {a.niche.upper()} | {a.topic}")
    print(f"{'='*50}\n")

    # 1. Script
    sp = str(out/"script.txt")
    if not Path(sp).exists():
        Path(sp).write_text(gen_script(a.topic, a.duration, a.lang), encoding="utf-8")
    ok(sp, "Script", 1)
    script = Path(sp).read_text("utf-8")

    # 2. Narration
    np_ = str(out/"narration.mp3")
    if not Path(np_).exists():
        gen_narration(sp, np_, preset["voice"])
    ok(np_, "Narration")

    # 3. Subtitles
    srt = str(out/"subtitles.srt")
    if not Path(srt).exists():
        gen_subtitles(np_, srt, a.lang)
    ok(srt, "Subtitles", 1)

    # 4. Images
    img_dir = out/"images"
    existing = list(img_dir.glob("img_*.png")) if img_dir.exists() else []
    if len(existing) < max(6, a.duration):
        n_img = max(6, a.duration)
        image_paths = gen_images(script, preset["image_style"], n_img, img_dir)
    else:
        image_paths = sorted(existing)
    print(f"✅ Images: {len(image_paths)}")

    # 5. Visuals
    vis = str(out/"visuals.mp4")
    if not Path(vis).exists():
        narr_dur = ffprobe_dur(np_)
        build_visuals(image_paths, narr_dur, vis)
    ok(vis, "Visuals")

    # 6. Music
    mus = str(out/"music.mp3")
    if not Path(mus).exists():
        get_music(mus, ffprobe_dur(np_), preset["music_mood"])
    ok(mus, "Music")

    # 7. Final
    final = str(out/"final.mp4")
    assemble(vis, np_, mus, srt, final, preset["color_grade"])
    ok(final, "Final", 100)

if __name__ == "__main__":
    main()
