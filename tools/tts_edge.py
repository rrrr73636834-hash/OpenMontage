"""Edge-TTS narration tool for OpenMontage Documentary pipeline."""
import asyncio
import edge_tts
import os
from pathlib import Path

VOICE = "ru-RU-DmitryNeural"


async def _generate(text: str, output_path: str) -> None:
    communicate = edge_tts.Communicate(text, VOICE, rate="-5%", volume="+0%")
    await communicate.save(output_path)


def generate_narration(script_path: str, output_path: str) -> str:
    """Generate narration from script file using edge-tts."""
    text = Path(script_path).read_text(encoding="utf-8")
    asyncio.run(_generate(text, output_path))
    assert os.path.exists(output_path), f"FAILED: {output_path} not created"
    size = os.path.getsize(output_path)
    assert size > 1000, f"FAILED: {output_path} too small ({size} bytes)"
    print(f"OK: narration saved to {output_path} ({size} bytes)")
    return output_path
