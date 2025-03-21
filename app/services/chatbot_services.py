import asyncio
import os
from ..config import LLAMA_PATH, MODEL_PATH, LLAMA_ENV_PATH

async def run_llama_stream(prompt: str, max_tokens: int = 200):
    os.environ["DYLD_LIBRARY_PATH"] = LLAMA_ENV_PATH

    if not os.path.exists(LLAMA_PATH):
        raise FileNotFoundError(f"Llama.cpp binary not found at {LLAMA_PATH}")
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

    command = [
        LLAMA_PATH,
        "-m", MODEL_PATH,
        "-p", prompt,
        "-n", str(max_tokens),
        "--ctx_size", "8192",
        "--no-display-prompt"
    ]

    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    while True:
        line = await process.stdout.readline()
        if not line:
            break
        yield line.decode().strip() + "\n"
