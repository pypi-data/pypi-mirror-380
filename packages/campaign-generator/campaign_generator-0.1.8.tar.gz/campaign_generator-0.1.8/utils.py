import os
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai import AsyncWebCrawler, BrowserConfig, CacheMode, CrawlerRunConfig
import subprocess
import requests
from datetime import date, datetime, timedelta
import platform
import asyncio
from playwright.async_api import async_playwright

from settings import ClickUpSettings, LocalSettings

if platform.system() == "Darwin":
    # macOS: use whisper-mps
    from whisper_mps.whisper.transcribe import transcribe as whisper_transcribe

    def transcribe_audio(file_path: str):
        """Transcribe audio file to text using whisper_mps."""
        result = whisper_transcribe(file_path, model="small")
        return result["text"]

else:
    # Linux/other: use faster-whisper
    from faster_whisper import WhisperModel

    def transcribe_audio(file_path: str):
        """Transcribe audio file to text using faster-whisper."""
        model = WhisperModel("small")
        segments, info = model.transcribe(file_path)
        # Concatenate all segments
        return " ".join([segment.text for segment in segments])


fit_md_generator = DefaultMarkdownGenerator(
    content_source="fit_html", options={"ignore_links": True}
)


def get_ollama_host():
    if platform.system() == "Darwin":
        print("Using localhost for Ollama API")
        return "http://localhost:11434"
    else:
        print("Using Docker container for Ollama API")
        return "http://ollama:11434"

def get_ollama_models():
    """Fetch available models from Ollama API."""
    url = f"{get_ollama_host()}/api/tags"
    response = requests.get(url)
    response.raise_for_status()
    return response.json().get("models", [])

def get_ollama_questions(text: str, model: str = "gemma3:1b"):
    """Generate a list of questions based on the prompt text using Ollama API."""
    url = f"{get_ollama_host()}/v1/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": f"""
                You are an interviewer tasked with creating thoughtful, reusable interview questions on the topic of Dungeons and dragons. 
                Your questions must follow these five parameters:
                1. Breadth - Cover the six journalist anchors (Who, What, When, Where, Why, How).
                2. Creator-Centric - Include process, behind-the-scenes, origin/inspiration, and insights/lessons learned.
                3. Relevance - Keep every question tied to the overarching topic, so answers are useful across multiple content formats (blog, posts, newsletter, Patreon, VIP).
                4. Tangibility - Each question should have a mirrored version that asks, "So what? What's in it for the reader, client, fan, or peer?"
                5. Business Transferability - Include at least one variant of each question that shifts the focus from "Here's my journey" to "Here's a lesson others could apply in their own business or creative practice."
                Output your questions organised by category (Who, What, When, Where, Why, How). For each question, include:
                •  The creator-centric version
                •  The tangible/client-centric version
                •  The business transferability version.
                """,
            },
            {
                "role": "system",
                "content": "Return a list of questions in formatted markdown.",
            },
            {
                "role": "system",
                "content": "Only respond with the markdown content, no explanations.",
            },
            {"role": "user", "content": text},
        ],
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    generated_text = response.json()["choices"][0]["message"]["content"]

    # Remove markdown code block markers if present
    if generated_text.startswith("```html"):
        generated_text = generated_text[len("```html") :].strip()
    if generated_text.endswith("```"):
        generated_text = generated_text[:-3].strip()
    return generated_text


def get_ollama_summary(text: str, model: str = "gemma3:1b"):
    """Get a summary of the text using Ollama API."""
    url = f"{get_ollama_host()}/v1/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant that summarizes text.",
            },
            {
                "role": "system",
                "content": "Please return the output in formatted html.",
            },
            {
                "role": "system",
                "content": "Use HTML tags like <p>, <b>, <i>, <ul>, <li> for formatting.",
            },
            {"role": "system", "content": "Use nice css styles to make it look cool."},
            {
                "role": "system",
                "content": "Only respond with the HTML content, no explanations.",
            },
            {"role": "user", "content": text},
        ],
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    generated_text = response.json()["choices"][0]["message"]["content"]

    # Remove markdown code block markers if present
    if generated_text.startswith("```html"):
        generated_text = generated_text[len("```html") :].strip()
    if generated_text.endswith("```"):
        generated_text = generated_text[:-3].strip()
    return generated_text


def internal_get_ollama_summary(text: str, model: str = "gemma3:1b"):
    """Get a summary of the text using Ollama API."""
    url = f"{get_ollama_host()}/v1/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant that summarizes text.",
            },
            {
                "role": "system",
                "content": "Please return max 10 sentences summary in plain text.",
            },
            {
                "role": "system",
                "content": "Only summarize, do not add comments, or flavor text.",
            },
            {"role": "user", "content": text},
        ],
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    generated_text = response.json()["choices"][0]["message"]["content"]

    return generated_text


def get_ollama_transcript_cleanup(text: str, model: str = "gemma3:1b", system_prompt: str = ""):
    """Clean up a transcript using Ollama API."""
    url = f"{get_ollama_host()}/v1/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": system_prompt or "You are a helpful assistant that cleans up transcripts.",
            },
            {"role": "user", "content": text},
        ],
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    generated_text = response.json()["choices"][0]["message"]["content"]

    return generated_text


def get_ollama_content_generation(prompt: str, model: str = "gemma3:1b", system_prompt: str = "") -> str:
    """Generate content based on a prompt using Ollama API."""
    url = f"{get_ollama_host()}/v1/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": system_prompt or "You are a helpful assistant that generates content.",
            },
            {"role": "user", "content": prompt},
        ],
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    generated_text = response.json()["choices"][0]["message"]["content"]

    # Remove markdown code block markers if present
    if generated_text.startswith("```markdown"):
        generated_text = generated_text[len("```markdown") :].strip()
    if generated_text.endswith("```"):
        generated_text = generated_text[:-3].strip()
    return generated_text


def convert_webm_to_mp3(webm_path, mp3_path):
    subprocess.run(["ffmpeg", "-y", "-i", webm_path, mp3_path], check=True)


async def get_real_article_url_with_consent(google_news_url):
    """Use Playwright to navigate to the URL and handle consent pages."""

    # get everything after the continue=
    continue_url = google_news_url.split("continue=")[-1]
    print(f"Continue URL: {continue_url}")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, slow_mo=3000)
        page = await browser.new_page()
        await page.goto(continue_url, wait_until="domcontentloaded")
        # If consent page appears, click "Accept all" or "Reject all"
        if "consent.google.com" in page.url:
            try:
                # Try to click "Accept all" button
                await page.click("button:has-text('Accept all')")
            except Exception:
                # Try to click "Reject all" if "Accept all" not found
                try:
                    await page.click("button:has-text('Reject all')")
                except Exception:
                    pass
            # Wait for redirect
            await page.wait_for_load_state("domcontentloaded")
        final_url = page.url
        await browser.close()
        return final_url


async def scrape_website_content(url: str) -> str:
    """Scrape website content using crawl4ai."""
    final_url = await get_real_article_url_with_consent(url)
    print(f"Final URL after consent: {final_url}")
    # Use crawl4ai to extract content
    try:
        async with AsyncWebCrawler(
            config=BrowserConfig(
                headless=True,
                enable_stealth=True,  # Enables stealth mode
                user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/116.0.0.0 Safari/537.36",
            )
        ) as crawler:
            result = await crawler.arun(
                url=final_url,
                config=CrawlerRunConfig(
                    wait_until="domcontentloaded",
                    page_timeout=60000,
                    cache_mode=CacheMode.BYPASS,
                    markdown_generator=fit_md_generator,
                ),
            )
            content = result.markdown
            print(f"Scraped content: {content[:500]}...")  # Print first 500 chars
            # return content
            summarized_content = internal_get_ollama_summary(
                text=content, model="granite3.1-moe:1b"
            )
            return summarized_content, final_url
    except Exception as e:
        print(f"Error fetching {url}: {e}")


def upload_file_from_bytes(filename: str, data: bytes, output_dir: str) -> str:
    """Write bytes to a local file under LocalSettings.research_output_dir.

    Args:
        filename: Name of the file to write.
        data: Bytes content to write.
        mime_type: Optional MIME type (ignored).
        folder_id: Optional folder id (ignored).

    Returns:
        The path to the written file.
    """
    # sanitize filename a bit
    safe_name = filename.replace("/", "_").replace("\\", "_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = os.path.join(output_dir, f"{timestamp}_{safe_name}")

    with open(out_path, "wb") as fh:
        fh.write(data)

    return out_path
