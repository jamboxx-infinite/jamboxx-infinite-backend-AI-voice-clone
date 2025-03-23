import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LLAMA_PATH = os.path.join(BASE_DIR, "build/bin/llama-cli")
MODEL_PATH = os.path.join(BASE_DIR, "models/mistral-7b-instruct-v0.2.Q4_K_M.gguf")
LLAMA_ENV_PATH = os.path.join(BASE_DIR, "build/bin")
