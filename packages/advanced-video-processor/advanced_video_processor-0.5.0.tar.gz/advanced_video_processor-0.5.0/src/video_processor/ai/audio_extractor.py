"""Audio extraction utilities for speech recognition."""

import logging
import subprocess
import tempfile
from pathlib import Path

from ..constants import TRANSCRIPTION

logger = logging.getLogger(__name__)


class AudioExtractor:
    """Handles audio extraction from video files for speech recognition."""

    def __init__(self) -> None:
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.temp_dir = Path(tempfile.gettempdir()) / "video_transcription"
        self.temp_dir.mkdir(exist_ok=True)

    def extract_audio(self, video_path: Path) -> Path | None:
        """Extract audio from video file using FFmpeg with optimal settings for speech recognition."""
        try:
            audio_path = self.temp_dir / f"{video_path.stem}_audio.wav"

            # Audio extraction settings from constants
            settings = TRANSCRIPTION["audio_extraction"]

            cmd = [
                "ffmpeg",
                "-y",
                "-i",
                str(video_path),
                "-vn",  # No video
                "-acodec",
                settings["codec"],  # PCM format for whisper
                "-ar",
                str(settings["sample_rate"]),  # 16kHz sample rate
                "-ac",
                str(settings["channels"]),  # Mono channel
                str(audio_path),
            ]

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=settings["timeout_seconds"],
            )

            if result.returncode != 0:
                logger.error(f"FFmpeg audio extraction failed: {result.stderr}")
                return None

            if not audio_path.exists():
                logger.error("Audio file not created")
                return None

            logger.info(f"Audio extracted: {audio_path}")
            return audio_path

        except subprocess.TimeoutExpired:
            logger.error("Audio extraction timeout")
            return None
        except Exception as e:
            logger.error(f"Audio extraction failed: {e}")
            return None

    def cleanup_temp_files(self):
        """Clean up temporary audio files."""
        try:
            if TRANSCRIPTION["processing"]["temp_cleanup"]:
                for audio_file in self.temp_dir.glob("*_audio.wav"):
                    audio_file.unlink(missing_ok=True)
        except Exception as e:
            logger.warning(f"Cleanup warning: {e}")
