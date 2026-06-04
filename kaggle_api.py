#!/usr/bin/env python3
"""Kaggle dataset and kernel automation for scene image generation."""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

KAGGLE_USERNAME = os.getenv("KAGGLE_USERNAME")
KAGGLE_KEY = os.getenv("KAGGLE_KEY")
DATASET_SLUG = "niche-video-scenes"
KERNEL_SLUG = f"{KAGGLE_USERNAME}/niche-sdxl-generator" if KAGGLE_USERNAME else None


def run_command(cmd, cwd=None, check=True):
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and result.returncode != 0:
        raise RuntimeError(
            f"Command failed: {' '.join(cmd)}\n{result.stderr.strip()}"
        )
    return result


def ensure_kaggle_auth():
    if not KAGGLE_USERNAME or not KAGGLE_KEY:
        raise RuntimeError("KAGGLE_USERNAME and KAGGLE_KEY must be set in environment")


def create_dataset_package(scenes_path: str, dataset_dir: str = "kaggle_dataset") -> Path:
    scenes_path = Path(scenes_path)
    if not scenes_path.exists():
        raise FileNotFoundError(f"scenes file missing: {scenes_path}")
    dataset_dir = Path(dataset_dir)
    dataset_dir.mkdir(parents=True, exist_ok=True)
    target = dataset_dir / scenes_path.name
    target.write_bytes(scenes_path.read_bytes())
    metadata = {
        "title": "Niche Video Scenes",
        "id": f"{KAGGLE_USERNAME}/{DATASET_SLUG}",
        "licenses": [{"name": "CC0-1.0"}],
        "resources": [{"path": scenes_path.name}],
    }
    (dataset_dir / "dataset-metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    return dataset_dir


def push_dataset(dataset_dir: str):
    ensure_kaggle_auth()
    run_command(["kaggle", "datasets", "create", "-p", str(dataset_dir), "--dir-mode", "zip"])


def write_kernel_metadata(kernel_dir: str):
    kernel_meta = {
        "id": KERNEL_SLUG,
        "title": "Niche SDXL Image Generator",
        "code_file": "kaggle_generator.ipynb",
        "language": "python",
        "kernel_type": "notebook",
        "is_private": True,
        "enable_gpu": True,
        "enable_internet": True,
    }
    Path(kernel_dir).mkdir(parents=True, exist_ok=True)
    Path(kernel_dir, "kernel-metadata.json").write_text(json.dumps(kernel_meta, indent=2), encoding="utf-8")


def push_notebook(notebook_path: str, kernel_dir: str = "kaggle_kernel"):
    ensure_kaggle_auth()
    notebook = Path(notebook_path)
    if not notebook.exists():
        raise FileNotFoundError(f"Notebook not found: {notebook}")
    write_kernel_metadata(kernel_dir)
    target = Path(kernel_dir) / notebook.name
    target.write_bytes(notebook.read_bytes())
    run_command(["kaggle", "kernels", "push", "-p", str(Path(kernel_dir).resolve())])


def wait_for_kernel(kernel_slug: str, timeout: int = 1800):
    deadline = time.time() + timeout
    while time.time() < deadline:
        result = run_command(["kaggle", "kernels", "status", kernel_slug], check=False)
        status = result.stdout.strip().lower()
        print(f"Kernel status: {status}")
        if "complete" in status or "finished" in status:
            return True
        if "error" in status or "failed" in status:
            raise RuntimeError(f"Kernel failed: {status}")
        time.sleep(15)
    raise TimeoutError(f"Kernel did not complete within {timeout} seconds")


def download_kernel_output(kernel_slug: str, output_dir: str = "kaggle_output") -> Path:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    run_command(["kaggle", "kernels", "output", kernel_slug, "-p", str(output_dir)])
    return output_dir


def main():
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("scenes", help="Path to scenes.json")
    ap.add_argument("--notebook", default="kaggle_generator.ipynb")
    ap.add_argument("--dataset-dir", default="kaggle_dataset")
    ap.add_argument("--kernel-dir", default="kaggle_kernel")
    a = ap.parse_args()

    dataset_dir = create_dataset_package(a.scenes, a.dataset_dir)
    push_dataset(str(dataset_dir))
    push_notebook(a.notebook, a.kernel_dir)
    if KERNEL_SLUG:
        wait_for_kernel(KERNEL_SLUG)
        download_kernel_output(KERNEL_SLUG)
    else:
        raise RuntimeError("KAGGLE_USERNAME not configured for kernel slug")

if __name__ == "__main__":
    main()
