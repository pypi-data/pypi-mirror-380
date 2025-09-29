import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# local imports
from routers import (
    audio_router,
    cron_router,
    text_router,
    frontend_router,
    clickup_router,
    rag_router,
)
from settings import LocalSettings

async def lifespan(app: FastAPI):
    # on startup check if output directories exist, if not create them
    output_dirs = [
        LocalSettings().research_output_dir,
        LocalSettings().question_output_dir,
        LocalSettings().audio_output_dir,
        LocalSettings().transcripts_output_dir,
        LocalSettings().content_generation_dir,
        LocalSettings().challenge_output_dir,
        LocalSettings().review_output_dir,
    ]

    for dir in output_dirs:
        os.makedirs(os.path.expanduser(dir), exist_ok=True)

    yield
    # Shutdown code can go here if needed

app = FastAPI(
    title="campaign-generator-api",
    version="0.0.1",
    description="General API for the campaign generator.",
    contact={
        "email": "contact@jamestwose.com",
    },
    lifespan=lifespan,
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(audio_router.router)
app.include_router(clickup_router.router)
app.include_router(cron_router.router)
app.include_router(frontend_router.router)
app.include_router(rag_router.router)
app.include_router(text_router.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the Campaign Generator API!"}
