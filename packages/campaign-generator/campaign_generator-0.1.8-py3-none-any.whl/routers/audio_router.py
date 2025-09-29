from fastapi import APIRouter, UploadFile, File, HTTPException, Query
import shutil
import os

# local imports
from clickup_utils import add_attachment_to_task, update_clickup_task
from settings import LocalSettings
from utils import convert_webm_to_mp3, transcribe_audio

router = APIRouter(prefix="/audio", tags=["audio"])

@router.post("/transcribe")
async def transcribe(
    file: UploadFile = File(...),
    save_dir: str = Query(
        default=LocalSettings().transcripts_output_dir,
        description="Directory to save the transcript file",
    ),
):
    temp_file_path = f"/tmp/{file.filename}"
    try:
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        # Call the transcribe_audio function from utils
        content = transcribe_audio(temp_file_path)
    except Exception as e:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
        raise HTTPException(status_code=500, detail=str(e))
    if os.path.exists(temp_file_path):
        os.remove(temp_file_path)

    if save_dir:
        save_dir = os.path.expanduser(save_dir)
        os.makedirs(save_dir, exist_ok=True)
        transcript_filename = os.path.splitext(file.filename)[0] + ".txt"
        transcript_path = os.path.join(save_dir, transcript_filename)
        try:
            with open(transcript_path, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to save transcript: {e}")

    task_id = file.filename.split('_')[-1].split('.')[0] if '_' in file.filename else None
    if task_id:
        try:
            update_clickup_task(
                task_id=task_id,
                status="phase 5. transcript",
                description=content
            )
        except Exception as e:
            print(f"Warning: Failed to update ClickUp task {task_id}: {e}")

    return {"content": content}


@router.post("/record")
async def record_audio(
    file: UploadFile = File(...),
    save_dir: str = Query(
        default=LocalSettings().audio_output_dir,
        description="Directory to save the audio file",
    ),
):
    save_dir = os.path.expanduser(save_dir)
    os.makedirs(save_dir, exist_ok=True)
    webm_path = os.path.join(save_dir, file.filename)
    mp3_filename = os.path.splitext(file.filename)[0] + ".mp3"
    mp3_path = os.path.join(save_dir, mp3_filename)
    try:
        with open(webm_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        # Convert WebM to MP3
        convert_webm_to_mp3(webm_path, mp3_path)
        # Optionally, remove the original WebM file
        os.remove(webm_path)
        try:
            task_id = file.filename.split('_')[-1].split('.')[0] if '_' in file.filename else None
            if task_id:
                add_attachment_to_task(task_id=task_id, file_path=mp3_path)
        except Exception as e:
            print(f"Warning: Failed to add attachment to ClickUp task {task_id}: {e}")
        return {
            "message": "Audio recorded and converted to MP3 successfully",
            "file_path": mp3_path,
        }
    except Exception as e:
        if os.path.exists(webm_path):
            os.remove(webm_path)
        if os.path.exists(mp3_path):
            os.remove(mp3_path)
        raise HTTPException(status_code=500, detail=str(e))
