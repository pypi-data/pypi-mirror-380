import requests

from settings import ClickUpSettings


def fetch_clickup_spaces() -> list[dict]:
    """Fetch ClickUp spaces for the configured team."""
    response = requests.get(
        "https://api.clickup.com/api/v2/team/{team_id}/space".format(
            team_id=ClickUpSettings().clickup_team_id
        ),
        headers={"Authorization": ClickUpSettings().clickup_api_key},
    )
    if response.status_code == 200:
        spaces = response.json().get("spaces", [])
        if not spaces:
            return {"error": "No spaces found"}
        return [{"id": s.get("id"), "name": s.get("name")} for s in spaces]
    else:
        return {"error": "Failed to retrieve space ID"}


def fetch_clickup_folder_ids(space_id: int) -> list[dict]:
    """Fetch ClickUp folder IDs for a given space."""
    # get folders
    response = requests.get(
        "https://api.clickup.com/api/v2/space/{space_id}/folder".format(
            space_id=space_id
        ),
        headers={"Authorization": ClickUpSettings().clickup_api_key},
    )
    if response.status_code == 200:
        folders = response.json().get("folders", [])
        if not folders:
            return {"error": "No folders found"}
        return [{"id": f.get("id"), "name": f.get("name")} for f in folders]
    else:
        return {"error": "Failed to retrieve folder ID"}


def fetch_clickup_list_ids(folder_id: int) -> list[dict]:
    """Fetch ClickUp list IDs for a given folder."""
    response = requests.get(
        "https://api.clickup.com/api/v2/folder/{folder_id}/list".format(
            folder_id=folder_id
        ),
        headers={"Authorization": ClickUpSettings().clickup_api_key},
    )
    if response.status_code == 200:
        lists = response.json().get("lists", [])
        if not lists:
            return {"error": "No lists found"}
        return [{"id": l.get("id"), "name": l.get("name")} for l in lists]
    else:
        return {"error": "Failed to retrieve list ID"}


def fetch_clickup_tasks(list_id: int | str) -> list[dict]:
    """Fetch ClickUp tasks for a given list."""
    response = requests.get(
        "https://api.clickup.com/api/v2/list/{list_id}/task".format(list_id=list_id),
        headers={"Authorization": ClickUpSettings().clickup_api_key},
    )
    # print(response.status_code, response.json())
    if response.status_code == 200:
        return response.json()

def fetch_clickup_task(task_id: str) -> dict:
    """Fetch a specific ClickUp task by ID."""
    response = requests.get(
        "https://api.clickup.com/api/v2/task/{task_id}".format(task_id=task_id),
        headers={"Authorization": ClickUpSettings().clickup_api_key},
    )
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to retrieve task"}

def update_clickup_task(task_id: str, description: str, status: str) -> dict:
    """Update the status of a ClickUp task."""
    response = requests.put(
        "https://api.clickup.com/api/v2/task/{task_id}".format(task_id=task_id),
        headers={
            "Authorization": ClickUpSettings().clickup_api_key,
            "Content-Type": "application/json",
        },
        json={"status": status, "description": description},
    )
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to update task status"}


def add_attachment_to_task(task_id: str, file_path: str) -> dict:
    """Add an attachment to a ClickUp task."""
    with open(file_path, 'rb') as file:
        files = {'attachment': file}
        response = requests.post(
            f"https://api.clickup.com/api/v2/task/{task_id}/attachment",
            headers={"Authorization": ClickUpSettings().clickup_api_key},
            files=files
        )
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to add attachment to task"}