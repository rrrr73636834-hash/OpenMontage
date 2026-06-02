#!/usr/bin/env python3
import argparse, os, subprocess, sys, requests
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

def enhance_with_pedalboard(input_path: str, output_path: str) -> bool:
    """Apply pedalboard reverb+compressor+lowpass chain."""
    try:
        import pedalboard as pb
        import soundfile as sf
        import numpy as np
        
        # Load audio
        audio, sr = sf.read(input_path)
        if len(audio.shape) == 1:
            audio = np.stack([audio, audio])
        elif audio.shape[0] > audio.shape[1]:
            audio = audio.T
        
        # Apply pedalboard chain
        board = pb.Pedalboard([
            pb.Reverb(room_size=0.3, wet_level=0.15),
            pb.Compressor(threshold_db=-20, ratio=3),
            pb.LowpassFilter(cutoff_hz=8000),
        ])
        enhanced = board(audio, sr)
        sf.write(output_path, enhanced.T if enhanced.shape[0] == 2 else enhanced, sr)
        return True
    except Exception as e:
        print(f"    ⚠️ Pedalboard failed: {e}")
        return False

PIXABAY_KEY = os.getenv("PIXABAY_API_KEY", "")

SOURCES = {
    "rain":   "anoisesrc=c=brown:r=44100",
    "forest": "anoisesrc=c=pink:r=44100",
    "ocean":  "anoisesrc=c=brown:r=44100",
    "fire":   "anoisesrc=c=brown:r=44100",
    "space":  "anoisesrc=c=white:r=44100",
    "cafe":   "anoisesrc=c=pink:r=44100",
}
FILTERS = {
    "rain":   "equalizer=f=200:width_type=h:width=400:g=10,equalizer=f=4000:width_type=h:width=2000:g=-8,acompressor=threshold=-15dB:ratio=2:attack=5:release=200,loudnorm=I=-20:TP=-2:LRA=9",
    "forest": "equalizer=f=1000:width_type=h:width=2000:g=-4,loudnorm=I=-20:TP=-2:LRA=9",
    "ocean":  "equalizer=f=100:width_type=h:width=200:g=14,equalizer=f=3000:width_type=h:width=2000:g=-10,loudnorm=I=-20:TP=-2:LRA=9",
    "fire":   "equalizer=f=300:width_type=h:width=600:g=8,equalizer=f=6000:width_type=h:width=4000:g=-12,loudnorm=I=-20:TP=-2:LRA=9",
    "space":  "equalizer=f=60:width_type=h:width=120:g=6,equalizer=f=8000:width_type=h:width=8000:g=-20,loudnorm=I=-23:TP=-3:LRA=5",
    "cafe":   "equalizer=f=500:width_type=h:width=1000:g=4,loudnorm=I=-18:TP=-2:LRA=11",
}
IMAGE_PROMPTS = {
    "rain":   "dark misty forest midnight, faint moonlight through clouds, indigo blue atmosphere, rain falling, no bright light sources, cinematic 4K",
    "forest": "dark enchanted forest night, deep blue shadows, misty ground fog, ultra detailed 4K, no bright highlights",
    "ocean":  "dark ocean at night, moonlit waves, deep blue sea, calm water, cinematic moody 4K",
    "fire":   "cozy dark room fireplace, warm amber embers, no bright flames, dark walls, 4K cinematic",
    "space":  "deep space nebula dark indigo purple, distant stars, cosmic mist, 4K",
    "cafe":   "dark cozy cafe rainy night, warm amber lamp only, rain on window, cinematic 4K",
}

def ok(path, label):
    p = Path(path)
    if not p.exists() or p.stat().st_size < 1000:
        print(f"❌ FATAL: {label}"); sys.exit(1)
    print(f"✅ {label} ({p.stat().st_size//1024}KB)")

def ffprobe_dur(path):
    r = subprocess.run(["ffprobe","-v","quiet","-show_entries","format=duration","-of","csv=p=0",path],capture_output=True,text=True)
    try: return float(r.stdout.strip())
    except: return 0.0

def generate_audio(mood, hours, output):
    seconds = hours * 3600
    if PIXABAY_KEY:
        queries = {"rain":["rain on leaves forest","heavy rain night"],"forest":["forest nature ambience"],"ocean":["ocean waves relaxing"],"fire":["fireplace crackling"],"space":["space ambient"],"cafe":["cafe ambience"]}
        for q in queries.get(mood, [mood]):
            try:
                r = requests.get("https://pixabay.com/api/videos/music/",params={"key":PIXABAY_KEY,"q":q,"per_page":5},timeout=15)
                hits = r.json().get("hits",[]) if r.text.strip() else []
                for hit in hits:
                    url = hit.get("audio",{}).get("url","")
                    if not url: continue
                    raw = output+".raw.mp3"
                    Path(raw).write_bytes(requests.get(url,timeout=60).content)
                    subprocess.run(["ffmpeg","-y","-stream_loop","-1","-i",raw,"-t",str(seconds),"-c","copy",output],capture_output=True)
                    if Path(output).exists() and Path(output).stat().st_size>100000:
                        os.unlink(raw)
                        print(f"  ✅ Audio: Pixabay ({q})")
                        return
            except Exception as e:
                print(f"  ⚠️ {q}: {e}")
    print(f"  🎵 Generating {mood}...")
    subprocess.run(["ffmpeg","-y","-f","lavfi","-i",SOURCES.get(mood,SOURCES["rain"]),"-t",str(seconds),"-af",FILTERS.get(mood,FILTERS["rain"]),"-q:a","0","-acodec","libmp3lame",output],check=True)
    
    # Apply pedalboard enhancement
    temp_wav = output + ".wav"
    if subprocess.run(["ffmpeg","-y","-i",output,"-acodec","pcm_s16le",temp_wav],capture_output=True).returncode == 0:
        if enhance_with_pedalboard(temp_wav, temp_wav):
            subprocess.run(["ffmpeg","-y","-i",temp_wav,"-q:a","0","-acodec","libmp3lame",output],capture_output=True)
        os.unlink(temp_wav)
    
    print(f"  ✅ Audio generated with enhancement")

def get_background(mood, output):
    prompt = IMAGE_PROMPTS.get(mood, IMAGE_PROMPTS["rain"])
    try:
        Path(output).write_bytes(requests.get(f"https://image.pollinations.ai/prompt/{requests.utils.quote(prompt)}?width=1920&height=1080&nologo=true&seed=42",timeout=60).content)
        print(f"  ✅ Image: Pollinations.ai")
    except:
        subprocess.run(["ffmpeg","-y","-f","lavfi","-i","color=c=black:size=1920x1080:duration=1","-vframes","1",output],capture_output=True)

def assemble(image, audio, output):
    dur = int(ffprobe_dur(audio))
    vf = ",".join([
        f"zoompan=z='min(zoom+0.00005,1.08)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={dur}:s=1920x1080:fps=2",
        "curves=r='0/0 0.5/0.42 1/0.75':g='0/0 0.5/0.44 1/0.77':b='0/0.04 0.5/0.50 1/0.90'",
        "eq=brightness=-0.08:saturation=0.7:contrast=1.1",
        "vignette=PI/3.5",
    ])
    subprocess.run(["ffmpeg","-y","-loop","1","-i",image,"-i",audio,"-vf",vf,"-c:v","libx264","-preset","slow","-r","2","-crf","26","-c:a","aac","-b:a","192k","-pix_fmt","yuv420p","-movflags","+faststart","-shortest",output],check=True)
    print(f"  ✅ Final: {Path(output).stat().st_size//1024//1024}MB")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("title")
    ap.add_argument("--mood",default="rain",choices=list(SOURCES.keys()))
    ap.add_argument("--hours",type=int,default=8)
    a = ap.parse_args()
    slug = a.title.lower().replace(" ","_")[:30]
    out = Path(f"soundscapes/{slug}"); out.mkdir(parents=True,exist_ok=True)
    audio = str(out/"audio.mp3"); image = str(out/"bg.jpg"); final = str(out/"final.mp4")
    print(f"\n{'═'*42}\n  🌙 {a.title}\n  {a.mood} | {a.hours}h\n{'═'*42}")
    print("\n── 1/3  AUDIO")
    if not Path(audio).exists(): generate_audio(a.mood,a.hours,audio)
    ok(audio,"Audio")
    print("\n── 2/3  IMAGE")
    if not Path(image).exists(): get_background(a.mood,image)
    ok(image,"Image")
    print("\n── 3/3  ASSEMBLY")
    assemble(image,audio,final)
    ok(final,"Final")
    dur = int(ffprobe_dur(final))
    print(f"\n✅ ГОТОВО: {final}\n   {dur//3600}h {(dur%3600)//60}m | {Path(final).stat().st_size//1024//1024}MB\n")

if __name__=="__main__": main()
