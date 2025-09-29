import os
from pydantic_settings import BaseSettings

class ClickUpSettings(BaseSettings):
    clickup_api_key: str
    clickup_team_id: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class LocalSettings(BaseSettings):
    research_output_dir: str = "research output"  # phase 2.
    question_output_dir: str = "question output"  # phase 3. -> phase 4.
    audio_output_dir: str = "audio output"  # phase 4. -> phase 5.
    transcripts_output_dir: str = "transcripts output"  # phase 5. -> phase 6.
    challenge_output_dir: str = "challenge output"  # phase 6. -> phase 7.
    content_generation_dir: str = "content generation output"  # phase 7. -> phase 8.
    review_output_dir: str = "review output"  # phase 8. -> phase 9.