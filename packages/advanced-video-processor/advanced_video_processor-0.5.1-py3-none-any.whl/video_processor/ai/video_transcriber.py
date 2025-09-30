"""Main video transcription orchestrator."""

import logging
from pathlib import Path
from typing import Any

from ..exceptions import VideoProcessorError
from .audio_extractor import AudioExtractor
from .models import TranscriptionResult
from .ollama_client import OllamaClient
from .transcript_writer import TranscriptWriter
from .whisper_client import WhisperClient

logger = logging.getLogger(__name__)


class VideoTranscriber:
    """
    Main transcription class that orchestrates the speech-to-text pipeline.

    Integrates Whisper for speech recognition with optional Ollama enhancement
    for improved transcript quality and formatting.
    """

    def __init__(self, ollama_host: str = None, ollama_port: int = None) -> None:
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.ollama_client = OllamaClient(ollama_host, ollama_port)
        self.whisper_client = WhisperClient()
        self.audio_extractor = AudioExtractor()
        self.transcript_writer = TranscriptWriter()

    async def transcribe_video(
        self,
        video_path: Path,
        whisper_model: str = "base",
        enhance_with_ollama: bool = True,
        domain_context: str = "general",
    ) -> TranscriptionResult | None:
        """
        Complete video transcription pipeline.

        Args:
            video_path: Path to video file
            whisper_model: Whisper model size to use
            enhance_with_ollama: Whether to enhance with Ollama
            domain_context: Context for enhancement (general, technical, educational)

        Returns:
            TranscriptionResult or None if failed
        """
        try:
            logger.info(f"Processing video: {video_path.name}")

            # Initialize Whisper if needed
            if not self.whisper_client.whisper_model:
                if not await self.whisper_client.initialize_whisper(whisper_model):
                    raise VideoProcessorError("Failed to initialize Whisper model")

            # Step 1: Extract audio
            logger.info("Extracting audio...")
            audio_path = self.audio_extractor.extract_audio(video_path)
            if not audio_path:
                raise VideoProcessorError("Audio extraction failed")

            # Step 2: Transcribe with Whisper
            transcript_data = self.whisper_client.transcribe_audio(audio_path)
            if not transcript_data:
                raise VideoProcessorError("Whisper transcription failed")

            # Step 3: Enhance with Ollama if requested and available
            enhanced_text = None
            if enhance_with_ollama:
                enhanced_text = await self._enhance_with_ollama(
                    transcript_data["text"], domain_context
                )

            # Create result
            result = TranscriptionResult(
                video_path=video_path,
                language=transcript_data["language"],
                duration=transcript_data["duration"],
                raw_text=transcript_data["text"],
                enhanced_text=enhanced_text,
                segments=transcript_data["segments"],
            )

            # Cleanup temporary files
            self.audio_extractor.cleanup_temp_files()

            logger.info(f"Transcription pipeline complete for {video_path.name}")
            return result

        except Exception as e:
            logger.error(f"Transcription pipeline failed: {e}")
            self.audio_extractor.cleanup_temp_files()
            raise VideoProcessorError(f"Transcription failed: {e}") from e

    async def _enhance_with_ollama(
        self, raw_text: str, domain_context: str
    ) -> str | None:
        """Enhance transcript using Ollama if available."""
        ollama_status = await self.ollama_client.check_connection()
        if not (ollama_status["connected"] and ollama_status["selected_model"]):
            return None

        logger.info(f"Enhancing transcript with {ollama_status['selected_model']}...")
        enhanced_text = await self.ollama_client.enhance_transcript(
            raw_text,
            ollama_status["selected_model"],
            domain_context,
        )

        if enhanced_text and enhanced_text != raw_text:
            logger.info("Transcript enhanced successfully")
            return enhanced_text
        else:
            logger.warning("Enhancement failed, using raw transcript")
            return None

    def save_transcription_results(
        self, result: TranscriptionResult, output_dir: Path
    ) -> tuple[Path, Path, Path | None]:
        """Save transcription results in multiple formats."""
        return self.transcript_writer.save_transcription_results(result, output_dir)

    def get_transcription_capabilities(self) -> dict[str, Any]:
        """Get information about available transcription capabilities."""
        try:
            # Check httpx for Ollama integration
            import httpx

            ollama_support = True
        except ImportError:
            ollama_support = False

        whisper_capabilities = self.whisper_client.get_capabilities()

        return {
            **whisper_capabilities,
            "ollama_support": ollama_support,
            "output_formats": ["json", "txt"],
            "domain_contexts": ["general", "technical", "educational"],
        }
