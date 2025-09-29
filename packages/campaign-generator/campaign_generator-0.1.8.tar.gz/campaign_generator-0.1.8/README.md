# Campaign Generator

Campaign Generator is a Python FastAPI application for creating content based on competitor research and user-generated audio. It provides a web interface for generating questions, summarizing text, transcribing audio, and fetching the latest news. The app uses local LLMs via Ollama and supports both Mac and Linux environments.

## Features

- **Audio Transcription:** Upload or record audio and transcribe it using Whisper (macOS: whisper-mps, Linux: faster-whisper).
- **Text Summarization:** Summarize any text using local LLMs (Gemma 3 1B, GPT-OSS 20B) via Ollama.
- **Question Generation:** Generate questions from text using LLMs.
- **Latest News:** Fetch recent news on any topic.
- **Modern Web UI:** Beautiful interface built with Tailwind CSS.
- **OS-aware:** Automatically selects the best transcription backend and Ollama API endpoint for your platform.

## Prerequisites

- Python 3.10+
- [Homebrew](https://brew.sh/) (for macOS)
- [pipx](https://pipxproject.github.io/pipx/)
- [ffmpeg](https://ffmpeg.org/) (for audio conversion)
- [Ollama](https://ollama.com/) installed and running with required models (`gemma3:1b`, `gpt-oss:20b`)

### Install system dependencies (macOS)

```sh
brew install pipx
brew install ffmpeg
pipx ensurepath
source ~/.zshrc  # or restart your terminal
```

### Install with pipx

```sh
pipx install campaign-generator
```

## Usage

Set your ClickUp API key and team ID in your environment variables:

```sh
export CLICKUP_API_KEY=your_clickup_api_key
export CLICKUP_TEAM_ID=your_clickup_team_id

env | grep CLICKUP # to verify they are set
```

When you start the app for the first time, the following folders will be created in the directory you run the command from:
- `research output/`: Stores research results generated from RSS feeds.
- `question output/`: Stores generated questions.
- `audio output/`: Stores uploaded audio files.
- `transcripts output/`: Stores transcriptions of audio files.
- `content generation output/`: Stores generated content.
- `review output/`: Stores reviewed content.
- `challenge output/`: Stores any challenges encountered.

Because of this behavior, it's recommended to run the app from a dedicated project directory.

Start the app with:

```sh
campaign-generator
```

By default, the API will run on [http://localhost:8080](http://localhost:8080).

Open your browser and navigate to `/frontend` to use the web interface:

```
http://localhost:8080/frontend
http://localhost:8080/frontend/chat # for RAG chat interface
http://localhost:8080/docs # for API docs
http://localhost:8080/graph-viewer # for visualization of the RAG graph
```

## How It Works

- **Transcription:** Uses `whisper-mps` on macOS and `faster-whisper` on Linux for audio transcription.
- **LLM Integration:** Connects to Ollama API for text summarization and question generation. The API endpoint is chosen automatically based on your OS.
- **Templates:** The web UI is served from `templates/home.html`.

## Development

- All source code is in the root and `routers/` directory.
- The entrypoint is `main.py`, which runs the FastAPI app.
- You can also run with Docker or Docker Compose (see `Dockerfile` and `docker-compose.yml`).

### Build and Publish to PyPI

1. Upgrade build and twine:
   ```sh
   python -m pip install --upgrade build twine
   ```
2. Build your package:
   ```sh
   python -m build
   ```
3. (Optional) Check your package:
   ```sh
   python -m twine check dist/*
   ```
4. Upload to PyPI:
   ```sh
   python -m twine upload dist/*
   ```

After publishing, you (and others) can install globally with pipx:
```sh
pipx install campaign-generator
```

## Troubleshooting

- If you see errors about missing templates, ensure you installed with pipx after running `pipx ensurepath` and that your terminal session is up to date.
- Make sure Ollama is running and the required models are pulled.
- If you see errors about ffmpeg, make sure it is installed and available in your PATH.

## License

MIT
