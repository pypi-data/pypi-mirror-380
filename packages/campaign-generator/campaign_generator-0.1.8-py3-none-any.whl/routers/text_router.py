from fastapi import APIRouter, HTTPException
from datetime import datetime

# local imports
from clickup_utils import fetch_clickup_task, update_clickup_task
from schemas import TextRequest
from settings import LocalSettings
from utils import (
    get_ollama_content_generation,
    get_ollama_models,
    get_ollama_summary,
    get_ollama_questions,
    get_ollama_transcript_cleanup,
    scrape_website_content,
    upload_file_from_bytes,
)

router = APIRouter(prefix="/text", tags=["text"])

@router.get("/models")
async def get_models():
    try:
        models = get_ollama_models()
        return {"models": [model.get("name") for model in models]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/summarize")
async def summarize_text(request: TextRequest):
    try:
        summary = get_ollama_summary(text=request.text, model=request.chat_model)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/transcript-cleanup")
async def cleanup_transcript(request: TextRequest):
    try:
        task = fetch_clickup_task(task_id="869akcv3p")
        system_prompt = task.get("text_content", "") if task else ""
    except Exception as e:
        system_prompt = ""
        print(f"Warning: Failed to fetch system prompt from ClickUp task: {e}")
    try:
        print(f"Chosen model: {request.chat_model}")
        cleaned_text = get_ollama_transcript_cleanup(
            text=request.text, model=request.chat_model, system_prompt=system_prompt
        )
        if request.task_id:
            try:
                update_clickup_task(
                    task_id=request.task_id,
                    status="phase 6. transcript clean",
                    description=cleaned_text,
                )
            except Exception as e:
                print(f"Warning: Failed to update ClickUp task {request.task_id}: {e}")

            try:
                file_name = f"cleaned_{request.task_id or 'unknown_task'}.txt"
                upload_file_from_bytes(
                    filename=file_name,
                    data=cleaned_text.encode("utf-8"),
                    output_dir=LocalSettings().transcripts_output_dir,
                )
            except Exception as e:
                print(
                    f"Warning: Failed to upload cleaned transcript for task {request.task_id}: {e}"
                )
        return {"cleaned_text": cleaned_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/challenge-ideas")
async def generate_challenge_ideas(request: TextRequest):
    try:
        task = fetch_clickup_task(task_id="869akcv6d")
        system_prompt = task.get("text_content", "") if task else ""
    except Exception as e:
        system_prompt = ""
        print(f"Warning: Failed to fetch system prompt from ClickUp task: {e}")

    try:
        print(f"Chosen model: {request.chat_model}")
        content = get_ollama_content_generation(
            prompt=request.text, model=request.chat_model, system_prompt=system_prompt
        )

        if request.task_id:
            try:
                update_clickup_task(
                    task_id=request.task_id,
                    status="phase 7. challenge",
                    description=content,
                )
            except Exception as e:
                print(f"Warning: Failed to update ClickUp task {request.task_id}: {e}")

            try:
                file_name = f"challenge_ideas_{request.task_id or 'unknown_task'}.txt"
                upload_file_from_bytes(
                    filename=file_name,
                    data=content.encode("utf-8"),
                    output_dir=LocalSettings().content_generation_dir,
                )
            except Exception as e:
                print(
                    f"Warning: Failed to upload generated content for task {request.task_id}: {e}"
                )

        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/generate-content")
async def generate_content(request: TextRequest):
    try:
        prompt_task = fetch_clickup_task(task_id="869ak6tvx")
        prompt = prompt_task.get("text_content", "") if prompt_task else ""
        style_task = fetch_clickup_task(task_id="869akjejr")
        style = style_task.get("text_content", "") if style_task else ""
        system_prompt = f"{prompt}\n\nStyle Guidelines:\n{style}"
    except Exception as e:
        system_prompt = ""
        print(f"Warning: Failed to fetch system prompt from ClickUp task: {e}")

    try:
        print(f"Chosen model: {request.chat_model}")
        content = get_ollama_content_generation(
            prompt=request.text, model=request.chat_model, system_prompt=system_prompt
        )

        if request.task_id:
            try:
                update_clickup_task(
                    task_id=request.task_id,
                    status="phase 8. draft channel",
                    description=content,
                )
            except Exception as e:
                print(f"Warning: Failed to update ClickUp task {request.task_id}: {e}")

            try:
                file_name = f"{request.task_id or 'unknown_task'}.txt"
                upload_file_from_bytes(
                    filename=file_name,
                    data=content.encode("utf-8"),
                    output_dir=LocalSettings().content_generation_dir,
                )
            except Exception as e:
                print(
                    f"Warning: Failed to upload generated content for task {request.task_id}: {e}"
                )

        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/review")
async def review_content(request: TextRequest):
    try:
        prompt_task = fetch_clickup_task(task_id="869ak6h10")
        prompt = prompt_task.get("text_content", "") if prompt_task else ""
        style_task = fetch_clickup_task(task_id="869akjejr")
        style = style_task.get("text_content", "") if style_task else ""
        system_prompt = f"{prompt}\n\nStyle Guidelines:\n{style}"
    except Exception as e:
        system_prompt = ""
        print(f"Warning: Failed to fetch system prompt from ClickUp task: {e}")

    try:
        print(f"Chosen model: {request.chat_model}")
        content = get_ollama_content_generation(
            prompt=request.text, model=request.chat_model, system_prompt=system_prompt
        )

        if request.task_id:
            try:
                update_clickup_task(
                    task_id=request.task_id,
                    status="phase 9. review interlink",
                    description=content,
                )
            except Exception as e:
                print(f"Warning: Failed to update ClickUp task {request.task_id}: {e}")

            try:
                file_name = f"{request.task_id or 'unknown_task'}.txt"
                upload_file_from_bytes(
                    filename=file_name,
                    data=content.encode("utf-8"),
                    output_dir=LocalSettings().review_output_dir,
                )
            except Exception as e:
                print(
                    f"Warning: Failed to upload generated content for task {request.task_id}: {e}"
                )

        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))