from fastapi import APIRouter, HTTPException
from lightrag import QueryParam
import os

# local imports
from clickup_utils import fetch_clickup_task, update_clickup_task
from utils import upload_file_from_bytes
from rag_utils import initialize_rag
from schemas import InitializeRagRequest, RagRequest, TextRequest
from settings import LocalSettings

router = APIRouter(prefix="/rag", tags=["rag"])


@router.post("/initialize")
async def initialize_rag_endpoint(request: InitializeRagRequest):
    try:
        rag = await initialize_rag(
            chat_model=request.chat_model, embed_model=request.embedding_model
        )
        return {"message": "RAG initialized successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/query")
async def query_rag_endpoint(request: RagRequest):
    """Query the RAG system with a question and return the answer."""
    try:
        rag = await initialize_rag(
            chat_model=request.chat_model or "gemma3:1b",
            embed_model=request.embedding_model or "nomic-embed-text:latest",
        )
        response = await rag.aquery(
            query=request.question,
            param=QueryParam(mode=request.mode, top_k=request.top_k),
        )
        print("RAG response:", response)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/questions")
async def question_rag_endpoint(request: TextRequest):
    """Query the RAG system with a question and return the answer."""
    try:
        task = fetch_clickup_task(task_id="869ak7hj3")
        system_prompt = task.get("text_content", "") if task else ""
    except Exception as e:
        system_prompt = ""
        print(f"Warning: Failed to fetch ClickUp task {request.task_id}: {e}")

    try:
        rag = await initialize_rag(
            chat_model=request.chat_model or "gemma3:1b",
            embed_model=request.embedding_model or "nomic-embed-text:latest",
        )
        response = await rag.aquery(
            query=request.text,
            param=QueryParam(mode="hybrid", top_k=5),
            system_prompt=system_prompt,
        )
        filename = f"{request.task_id or 'unknown_task'}.txt"
        upload_file_from_bytes(
            filename=filename,
            data=response.encode("utf-8"),
            output_dir=LocalSettings().question_output_dir,
        )
        if request.task_id:
            update_clickup_task(
                task_id=request.task_id,
                status="phase 4. interview",
                description=response,
            )
        return {"detail": f"Question generated and saved for task {request.task_id}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/reload")
async def reload_rag_endpoint(request: InitializeRagRequest):
    """Scan the RAG working directory, enqueue new text files and process the pipeline."""
    try:
        # initialize RAG and storages
        rag = await initialize_rag(
            chat_model=request.chat_model, embed_model=request.embedding_model
        )

        # determine working dir
        working_dir = getattr(rag, "working_dir", LocalSettings().research_output_dir)

        docs = []
        paths = []
        for root, _, files in os.walk(working_dir):
            for fn in files:
                if fn.lower().endswith((".txt", ".md", ".html", ".htm")):
                    full = os.path.join(root, fn)
                    try:
                        with open(full, "r", encoding="utf-8", errors="ignore") as fh:
                            content = fh.read()
                            if content and content.strip():
                                docs.append(content)
                                paths.append(full)
                    except Exception:
                        continue

        if not docs:
            return {
                "message": "RAG reloaded: no text files found in working_dir",
                "working_dir": working_dir,
            }

        track_id = await rag.apipeline_enqueue_documents(input=docs, file_paths=paths)
        await rag.apipeline_process_enqueue_documents()

        return {
            "message": "RAG reloaded and files enqueued/processed",
            "track_id": track_id,
            "files": len(docs),
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
