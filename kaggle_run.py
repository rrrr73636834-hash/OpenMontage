#!/usr/bin/env python3
import argparse,json,os,sys,time,zipfile
from pathlib import Path
import requests

KAGGLE_USER=os.environ.get("KAGGLE_USERNAME","")
KAGGLE_KEY=os.environ.get("KAGGLE_KEY","")
KAGGLE_AUTH=(KAGGLE_USER,KAGGLE_KEY)
KAGGLE_BASE="https://www.kaggle.com/api/v1"
KERNEL_SLUG=f"{KAGGLE_USER}/forts-video-pipeline"

def push_kernel(nb_path,niche,topic,duration,lang):
    nb=json.loads(nb_path.read_text("utf-8"))
    inject={"cell_type":"code","metadata":{},"outputs":[],"execution_count":None,"source":
        f'''import os
os.environ["TOPIC"]="""{topic}"""
os.environ["NICHE"]="""{niche}"""
os.environ["DURATION"]="""{duration}"""
os.environ["LANG"]="""{lang}"""
os.environ["OPENROUTER_API_KEY"]=os.environ.get("OPENROUTER_API_KEY","")
'''}
    nb["cells"].insert(0,inject)
    r=requests.post(f"{KAGGLE_BASE}/kernels/push",auth=KAGGLE_AUTH,
        headers={"Content-Type":"application/json"},
        json={"id":KERNEL_SLUG,"title":"FORTS Video Pipeline","code":json.dumps(nb),
              "language":"python","kernel_type":"notebook","is_private":True,
              "enable_gpu":True,"enable_internet":True,
              "dataset_sources":[],"competition_sources":[],"kernel_sources":[]},
        timeout=60)
    r.raise_for_status()
    print(f"pushed: {KERNEL_SLUG}")
    return KERNEL_SLUG

def wait_kernel(slug,timeout_min=90):
    deadline=time.time()+timeout_min*60
    last=""
    while time.time()<deadline:
        r=requests.get(f"{KAGGLE_BASE}/kernels/{slug}",auth=KAGGLE_AUTH,timeout=30)
        r.raise_for_status()
        status=r.json().get("status","unknown")
        if status!=last:
            print(f"status: {status}"); last=status
        if status=="complete": return True
        if status in("error","cancel"):
            print("kernel failed"); return False
        time.sleep(30)
    print("timeout"); return False

def download_output(slug,output_dir):
    output_dir.mkdir(parents=True,exist_ok=True)
    r=requests.get(f"{KAGGLE_BASE}/kernels/{slug}/output",
        auth=KAGGLE_AUTH,stream=True,timeout=120)
    r.raise_for_status()
    zp=output_dir/"out.zip"
    with open(zp,"wb") as f:
        for chunk in r.iter_content(65536):
            if chunk: f.write(chunk)
    with zipfile.ZipFile(zp,"r") as z: z.extractall(output_dir)
    zp.unlink(missing_ok=True)
    final=next(output_dir.rglob("final.mp4"),None)
    if not final: raise FileNotFoundError("final.mp4 not found")
    print(f"done: {final}")
    return final

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--niche",required=True)
    ap.add_argument("--topic",required=True)
    ap.add_argument("--duration",type=int,default=10)
    ap.add_argument("--lang",default="en")
    ap.add_argument("--output",default="./kaggle_output")
    ap.add_argument("--notebook",default="kaggle_pipeline.ipynb")
    a=ap.parse_args()
    if not KAGGLE_USER or not KAGGLE_KEY: sys.exit("KAGGLE creds missing")
    nb=Path(a.notebook)
    if not nb.exists(): sys.exit(f"notebook not found: {nb}")
    slug=push_kernel(nb,a.niche,a.topic,a.duration,a.lang)
    if not wait_kernel(slug): sys.exit(1)
    download_output(slug,Path(a.output))

if __name__=="__main__": main()
