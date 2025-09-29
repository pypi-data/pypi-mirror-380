from fastapi import APIRouter, Response, Query
import os

from settings import LocalSettings

router = APIRouter(prefix="/frontend", tags=["frontend"])


@router.get("")
async def serve_frontend():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "templates", "home.html"
    )
    try:
        with open(template_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        return Response(content=html_content, media_type="text/html")
    except Exception as e:
        return Response(
            content=f"Error loading template: {e}",
            media_type="text/plain",
            status_code=500,
        )


@router.get("/chat")
async def serve_chat():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "templates", "chat.html"
    )
    try:
        with open(template_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        return Response(content=html_content, media_type="text/html")
    except Exception as e:
        return Response(
            content=f"Error loading template: {e}",
            media_type="text/plain",
            status_code=500,
        )


@router.get("/graph-viewer")
async def serve_graph():
    template_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "templates", "graph_viewer.html"
    )
    try:
        with open(template_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        return Response(content=html_content, media_type="text/html")
    except Exception as e:
        return Response(
            content=f"Error loading template: {e}",
            media_type="text/plain",
            status_code=500,
        )


@router.get("/graphml")
async def serve_graphml():
    try:
        with open(
            f"{LocalSettings().research_output_dir}/graph_chunk_entity_relation.graphml",
            "r",
            encoding="utf-8",
        ) as f:
            graphml_content = f.read()
        return Response(content=graphml_content, media_type="application/xml")
    except Exception as e:
        return Response(
            content=f"Error loading GraphML file: {e}",
            media_type="text/plain",
            status_code=500,
        )


@router.get("/redirect")
async def redirect_page(
    target: str = Query(..., description="Target URL to redirect to")
):
    html = f"""
    <!DOCTYPE html>
    <html lang='en'>
    <head>
        <meta http-equiv='refresh' content='0; url={target}' />
        <title>Redirecting...</title>
    </head>
    <body>
        <p>Redirecting to <a href='{target}'>{target}</a>...</p>
    </body>
    </html>
    """
    return Response(content=html, media_type="text/html")
