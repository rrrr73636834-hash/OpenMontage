#!/usr/bin/env python3
import argparse,json,os,sys,time,zipfile,subprocess,tempfile,shutil
from pathlib import Path

KAGGLE_USER=os.environ.get("KAGGLE_USERNAME","")
KAGGLE_KEY=os.environ.get("KAGGLE_KEY","")

def setup_kaggle_creds():
    """Записываем kaggle.json для CLI."""
    kaggle_dir = Path.home()/".kaggle"
    kaggle_dir.mkdir(exist_ok=True)
    creds = {"username":KAGGLE_USER,"key":KAGGLE_KEY}
    (kaggle_dir/"kaggle.json").write_text(json.dumps(creds))
    (kaggle_dir/"kaggle.json").chmod(0o600)

def push_kernel(nb_path,niche,topic,duration,lang):
    """Пушим через kaggle CLI."""
    import requests
    # Читаем notebook и инжектируем конфиг
    nb = json.loads(nb_path.read_text("utf-8"))
    inject = {
        "cell_type":"code","metadata":{},"outputs":[],"execution_count":None,
        "source":[
            "import os\n",
            f'os.environ[\"TOPIC\"] = {json.dumps(topic)}\n',
            f'os.environ[\"NICHE\"] = {json.dumps(niche)}\n',
            f'os.environ[\"DURATION\"] = \"{duration}\"\n',
            f'os.environ[\"LANG\"] = {json.dumps(lang)}\n',
            f'os.environ[\"OPENROUTER_API_KEY\"] = {json.dumps(os.environ.get("OPENROUTER_API_KEY",""))}\n',
        ]
    }
    nb["cells"].insert(0, inject)

    # Создаём временную папку с kernel
    tmpdir = Path(tempfile.mkdtemp())
    nb_file = tmpdir/"kernel.ipynb"
    nb_file.write_text(json.dumps(nb), encoding="utf-8")

    slug = f"forts-{niche.replace('_','-')}"
    meta = {
        "id": f"{KAGGLE_USER}/{slug}",
        "title": f"FORTS {niche}",
        "code_file": "kernel.ipynb",
        "language": "python",
        "kernel_type": "notebook",
        "is_private": True,
        "enable_gpu": True,
        "enable_internet": True,
        "dataset_sources": [],
        "competition_sources": [],
        "kernel_sources": [],
    }
    (tmpdir/"kernel-metadata.json").write_text(json.dumps(meta))

    result = subprocess.run(
        ["kaggle","kernels","push","-p",str(tmpdir)],
        capture_output=True, text=True
    )
    shutil.rmtree(tmpdir)

    if result.returncode != 0:
        print(result.stderr)
        raise RuntimeError(f"Push failed: {result.stderr}")
    print(f"pushed: {KAGGLE_USER}/{slug}")
    return f"{KAGGLE_USER}/{slug}"

def wait_kernel(slug, timeout_min=90):
    deadline = time.time()+timeout_min*60
    last = ""
    while time.time()<deadline:
        r = subprocess.run(
            ["kaggle","kernels","status",slug],
            capture_output=True, text=True
        )
        out = r.stdout.strip()
        if out != last:
            print(f"status: {out}"); last=out
        if "complete" in out.lower(): return True
        if "error" in out.lower() or "cancel" in out.lower():
            print("kernel failed"); return False
        time.sleep(30)
    print("timeout"); return False

def download_output(slug, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        ["kaggle","kernels","output", slug, "-p", str(output_dir)],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(f"Download failed: {result.stderr}")
    final = next(output_dir.rglob("final.mp4"), None)
    if not final:
        raise FileNotFoundError("final.mp4 not found")
    print(f"done: {final}")
    return final

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--niche",required=True)
    ap.add_argument("--topic",required=True)
    ap.add_argument("--duration",type=int,default=10)
    ap.add_argument("--lang",default="en")
    ap.add_argument("--output",default="./kaggle_output")
    ap.add_argument("--notebook",default="kaggle_pipeline.ipynb")
    a = ap.parse_args()
    if not KAGGLE_USER or not KAGGLE_KEY: sys.exit("KAGGLE creds missing")
    setup_kaggle_creds()
    nb = Path(a.notebook)
    if not nb.exists(): sys.exit(f"notebook not found: {nb}")
    slug = push_kernel(nb, a.niche, a.topic, a.duration, a.lang)
    if not wait_kernel(slug): sys.exit(1)
    download_output(slug, Path(a.output))

if __name__=="__main__": main()
