from urllib import response
from fastapi import APIRouter, HTTPException
from typing import Optional
import threading
import time
import traceback
import asyncio

import feedparser

from clickup_utils import fetch_clickup_tasks
from settings import LocalSettings
from utils import scrape_website_content, upload_file_from_bytes

router = APIRouter(prefix="/cron", tags=["cron"])


# Simple in-process scheduler state
_cron_thread: Optional[threading.Thread] = None
_cron_stop_event: Optional[threading.Event] = None
_cron_lock = threading.Lock()
_cron_interval_seconds = 60


async def _cron_job_once():
    """The actual job to run periodically. Keep light and idempotent."""
    response = fetch_clickup_tasks(list_id=901212713796)
    tasks = [
        {"id": t.get("id"), "name": t.get("name")} for t in response.get("tasks", [])
    ]

    feed_urls = [t.get("name") for t in tasks]

    for feed_url in feed_urls:
        print(f"[cron_job_once] Processing feed: {feed_url}")
        if "https" not in feed_url:
            update_url = "https://" + feed_url
            print(f"  - updating feed URL to: {update_url}")
            feed_url = update_url
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[0:3]:  # process only first 3 entries
            try:
                content, final_url = await scrape_website_content(entry.link)
                content_to_upload = f"Source URL: {final_url}\n\n{content}"
                chosen_filename = f"{final_url.split('//')[-1].replace('/', '_')}.txt"
                upload_file_from_bytes(
                    filename=chosen_filename,
                    data=content_to_upload.encode("utf-8"),
                    output_dir=LocalSettings().research_output_dir,
                )
            except Exception as e:
                print(f"[cron_job_once] error: {e}")


def _cron_worker(stop_event: threading.Event, interval: int):
    try:
        while not stop_event.is_set():
            start = time.time()
            try:
                # run the async job from the background thread
                asyncio.run(_cron_job_once())
            except Exception:
                # keep worker alive on errors
                traceback.print_exc()
            elapsed = time.time() - start
            to_wait = max(0, interval - elapsed)
            # wait in small increments so stop_event can interrupt quickly
            stop_event.wait(to_wait)
    finally:
        print("[cron_worker] exiting")


@router.get("/run_once")
async def run_cron_once():
    """Run the cron job once immediately."""
    try:
        await _cron_job_once()
        return {"status": "completed"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/start")
async def start_cron(interval_seconds: int = _cron_interval_seconds):
    """Start the background cron-like worker. Returns status."""
    global _cron_thread, _cron_stop_event, _cron_interval_seconds
    with _cron_lock:
        if _cron_thread and _cron_thread.is_alive():
            return {
                "status": "already_running",
                "interval_seconds": _cron_interval_seconds,
            }

        _cron_interval_seconds = int(interval_seconds)
        _cron_stop_event = threading.Event()
        _cron_thread = threading.Thread(
            target=_cron_worker,
            args=(_cron_stop_event, _cron_interval_seconds),
            daemon=True,
        )
        _cron_thread.start()
        return {"status": "started", "interval_seconds": _cron_interval_seconds}


@router.post("/stop")
async def stop_cron():
    """Stop the background cron-like worker if running."""
    global _cron_thread, _cron_stop_event
    with _cron_lock:
        if not _cron_thread or not _cron_thread.is_alive():
            return {"status": "not_running"}

        _cron_stop_event.set()
        # wait briefly for thread to exit
        _cron_thread.join(timeout=5)
        alive = _cron_thread.is_alive()
        if alive:
            return {"status": "stop_timeout", "still_alive": True}

        # cleanup
        _cron_thread = None
        _cron_stop_event = None
        return {"status": "stopped"}


@router.get("/status")
async def cron_status():
    """Return whether the cron worker is running and the configured interval."""
    global _cron_thread, _cron_interval_seconds
    running = bool(_cron_thread and _cron_thread.is_alive())
    return {"running": running, "interval_seconds": _cron_interval_seconds}
