from fastapi import APIRouter
from clickup_utils import (
    fetch_clickup_spaces,
    fetch_clickup_folder_ids,
    fetch_clickup_list_ids,
    fetch_clickup_tasks,
)

router = APIRouter(prefix="/clickup", tags=["clickup"])

@router.get("/spaces")
async def clickup_spaces():
    try:
        return fetch_clickup_spaces()
    except Exception as e:
        return {"error": str(e)}
    
@router.get("/folders")
async def clickup_folders(space_id: int):
    try:
        return fetch_clickup_folder_ids(space_id=space_id)
    except Exception as e:
        return {"error": str(e)}
    
@router.get("/lists")
async def clickup_lists(folder_id: int):
    try:
        return fetch_clickup_list_ids(folder_id=folder_id)
    except Exception as e:
        return {"error": str(e)}

@router.get("/tasks")
async def clickup_tasks(list_id: int | str):
    # get space id
    try:
        return fetch_clickup_tasks(
            list_id=list_id
        )
    except Exception as e:
        return {"error": str(e)}
