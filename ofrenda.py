#!/usr/bin/env python3
"""Ofrenda.exe: turn a memory into a small, private digital ofrenda."""
import argparse
import json
import sys
import urllib.error
import urllib.request


OLLAMA_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "gemma3:1b"


def fallback(name, memory):
    """A graceful offline demo when Ollama is not running."""
    return (
        f"🕯️ OFRENDA FOR {name.upper()}\n\n"
        f"The machine remembers this: {memory}\n\n"
        "May the marigold path stay bright, and may this memory never be lost."
    )


def remember(name, memory, model=DEFAULT_MODEL, offline=False):
    prompt = f"""You are a gentle digital ofrenda keeper.
Write a short, poetic remembrance card for Día de los Muertos.
Honor the person without inventing facts. Use warm imagery, one tiny title,
and 3-5 sentences. Do not mention AI, prompts, or that you are a machine.
Name: {name}
Memory: {memory}"""
    if offline:
        return fallback(name, memory)
    payload = json.dumps({"model": model, "prompt": prompt, "stream": False}).encode()
    request = urllib.request.Request(
        OLLAMA_URL, data=payload, headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            return json.loads(response.read())['response'].strip()
    except (urllib.error.URLError, TimeoutError, KeyError, json.JSONDecodeError):
        print("⚠️  Ollama is unavailable; using the offline candlelight mode.\n", file=sys.stderr)
        return fallback(name, memory)


def main():
    parser = argparse.ArgumentParser(description="Create a private digital ofrenda with local AI.")
    parser.add_argument("name", help="the person, pet, place, or project being remembered")
    parser.add_argument("memory", help="one sentence to place on the ofrenda")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="local Ollama model")
    parser.add_argument("--offline", action="store_true", help="use the deterministic demo")
    args = parser.parse_args()
    print("\n" + remember(args.name, args.memory, args.model, args.offline) + "\n")


if __name__ == "__main__":
    main()
