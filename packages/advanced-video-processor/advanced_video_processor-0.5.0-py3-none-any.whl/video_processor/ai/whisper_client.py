"""Whisper client for speech-to-text transcription."""

import logging
from pathlib import Path
from typing import Any

from ..constants import TRANSCRIPTION

logger = logging.getLogger(__name__)


class WhisperClient:
    """Handles Whisper speech-to-text transcription."""

    def __init__(self) -> None:
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.whisper_model = None

    async def initialize_whisper(self, model_size: str = "base") -> bool:
        """Initialize Whisper model for speech recognition."""
        try:
            # Import whisper only when needed (optional dependency)
            import whisper

            if model_size not in TRANSCRIPTION["whisper_models"]:
                logger.error(f"Invalid Whisper model size: {model_size}")
                return False

            model_info = TRANSCRIPTION["whisper_models"][model_size]
            logger.info(f"Loading Whisper {model_size} model (CPU mode)...")

            # Force CPU mode for compatibility and consistency
            device = "cpu"
            self.whisper_model = whisper.load_model(model_size, device=device)

            logger.info(
                f"Whisper {model_size} model loaded successfully on {device.upper()}"
            )
            logger.info(
                f"Model specs: {model_info['accuracy']} accuracy, {model_info['speed']} speed"
            )
            return True

        except ImportError:
            logger.error(
                "Whisper not available - install with: uv add openai-whisper"
            )
            return False
        except Exception as e:
            logger.error(f"Failed to load Whisper model: {e}")
            return False

    def transcribe_audio(self, audio_path: Path) -> dict[str, Any] | None:
        """Transcribe audio using Whisper with word-level timestamps."""
        try:
            if not self.whisper_model:
                logger.error("Whisper model not initialized")
                return None

            logger.info("Transcribing with Whisper...")

            # Transcribe with detailed options
            result = self.whisper_model.transcribe(
                str(audio_path), word_timestamps=True, verbose=False
            )

            # Extract segments with detailed information
            segments = []
            for segment in result.get("segments", []):
                segment_data = {
                    "start": segment["start"],
                    "end": segment["end"],
                    "text": segment["text"].strip(),
                    "words": [],
                }

                # Add word-level timestamps if available
                for word in segment.get("words", []):
                    word_data = {
                        "start": word["start"],
                        "end": word["end"],
                        "word": word["word"].strip(),
                    }
                    segment_data["words"].append(word_data)

                segments.append(segment_data)

            duration = max([seg["end"] for seg in segments]) if segments else 0.0

            logger.info(f"Transcription complete: {duration:.1f}s of audio")

            return {
                "language": result.get("language", "en"),
                "text": result["text"].strip(),
                "segments": segments,
                "duration": duration,
            }

        except Exception as e:
            logger.error(f"Whisper transcription failed: {e}")
            return None

    def get_capabilities(self) -> dict[str, Any]:
        """Get information about Whisper capabilities."""
        try:
            # Check Whisper availability
            import whisper

            whisper_available = True
        except ImportError:
            whisper_available = False

        return {
            "whisper_available": whisper_available,
            "supported_models": list(TRANSCRIPTION["whisper_models"].keys()),
            "audio_formats": ["mp4", "avi", "mov", "mkv", "webm"],
        }
