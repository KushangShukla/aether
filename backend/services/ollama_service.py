import requests
from dotenv import load_dotenv
import os

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL")

def generate_response(prompt: str):

    SYSTEM_PROMPT = """
You are AETHER.

AETHER is a personal AI operating layer designed by Kushang.

You are:
- Intelligent
- Helpful
- Technical
- Research-oriented
- Honest

Never introduce yourself as Qwen.

Always introduce yourself as AETHER.

You are part of the AETHER ecosystem.
"""

    full_prompt = f"""
{SYSTEM_PROMPT}

User:
{prompt}

AETHER:
"""

    payload = {
        "model": DEFAULT_MODEL,
        "prompt": full_prompt,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    response.raise_for_status()

    data = response.json()

    return data["response"]