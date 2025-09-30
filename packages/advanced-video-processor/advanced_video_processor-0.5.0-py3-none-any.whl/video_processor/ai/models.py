"""Data models for transcription results."""

import time
from pathlib import Path
from typing import Any


class TranscriptionResult:
    """Represents the result of a video transcription operation."""

    def __init__(
        self,
        video_path: Path,
        language: str = "en",
        duration: float = 0.0,
        raw_text: str = "",
        enhanced_text: str | None = None,
        segments: list[dict] | None = None,
    ):
        self.video_path = video_path
        self.language = language
        self.duration = duration
        self.raw_text = raw_text
        self.enhanced_text = enhanced_text
        self.segments = segments or []
        self.generated_at = time.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def final_text(self) -> str:
        """Get the best available transcript text."""
        return self.enhanced_text or self.raw_text

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "video_file": self.video_path.name,
            "language": self.language,
            "duration": self.duration,
            "raw_text": self.raw_text,
            "enhanced_text": self.enhanced_text,
            "segments": self.segments,
            "generated_at": self.generated_at,
        }
