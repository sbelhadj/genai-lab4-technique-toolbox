"""
Generation Utilities for Lab 4 — Technique Toolbox
"""

import requests
import json


def generate(prompt, model="llama3.2:3b", temperature=0.3, max_tokens=500, timeout=90):
    """Generate a completion using Ollama."""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": model, "prompt": prompt, "stream": False,
                  "options": {"temperature": temperature, "num_predict": max_tokens}},
            timeout=timeout)
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        return f"[Generation failed: {e}]"


def generate_n(prompt, n=5, **kwargs):
    """Generate n completions for the same prompt."""
    return [generate(prompt, **kwargs) for _ in range(n)]


def is_ollama_available():
    try:
        r = requests.get("http://localhost:11434/api/tags", timeout=5)
        return r.status_code == 200
    except Exception:
        return False


def try_parse_json(text):
    """Attempt to parse JSON from model output, handling markdown fences."""
    text = text.strip()
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()
    try:
        return json.loads(text), None
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}") + 1
        if start >= 0 and end > start:
            try:
                return json.loads(text[start:end]), None
            except json.JSONDecodeError as e:
                return None, str(e)
        return None, "No JSON object found"
