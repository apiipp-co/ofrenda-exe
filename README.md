# 🕯️ Ofrenda.exe

> **A tiny local AI memory keeper for the Ghost in the Machine challenge.**

Ofrenda.exe turns one small memory into a warm remembrance card inspired by
Día de los Muertos. It is a friendly ghost in your terminal: a machine that
does not resurrect the past, but helps us keep its light visible.

The project uses an open-weight model running locally through [Ollama](https://ollama.com/).
Your names, stories, and family memories stay on your machine. No account,
cloud API key, or upload is required.

## ✨ Quick start

Install Ollama, then download a small open-weight model:

```bash
ollama pull gemma3:1b
ollama serve
```

Run the one-file app:

```bash
python3 ofrenda.py "Abuela Rosa" "She taught me to make sweet bread on rainy Sundays."
```

For a zero-setup demo, use the candlelight fallback:

```bash
python3 ofrenda.py "My first open-source project" "It taught me that unfinished things can still help someone." --offline
```

Use another local model with `--model`, for example `--model llama3.2:3b`.

## 🧠 How it works

1. The CLI accepts a name and a memory.
2. A carefully bounded prompt asks the local model for a short remembrance.
3. Ollama generates the card on-device.
4. If Ollama is asleep, the app still produces a deterministic offline card.

## 🌼 Why open-weight AI?

Memories are intimate. Local inference keeps them private, makes the project
usable without internet, and lets people replace the model instead of being
locked into a disappearing service. The machine becomes an ofrenda: a place
where old stories can safely meet new tools.

## 📜 License

MIT — see [LICENSE](LICENSE).
