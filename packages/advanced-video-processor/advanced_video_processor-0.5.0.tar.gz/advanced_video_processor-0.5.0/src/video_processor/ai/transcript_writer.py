"""Transcript file writing utilities."""

import json
import logging
from pathlib import Path

from ..constants import TRANSCRIPTION
from .models import TranscriptionResult

logger = logging.getLogger(__name__)


class TranscriptWriter:
    """Handles saving transcription results in multiple formats."""

    def __init__(self) -> None:
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    def save_transcription_results(
        self, result: TranscriptionResult, output_dir: Path
    ) -> tuple[Path, Path]:
        """
        Save transcription results in multiple formats.

        Returns:
            Tuple of (json_path, text_path)
        """
        try:
            base_name = result.video_path.stem
            transcript_dir = output_dir / "transcripts"
            transcript_dir.mkdir(exist_ok=True)

            # Save detailed JSON with timestamps
            json_path = transcript_dir / f"{base_name}_transcript.json"
            with open(
                json_path, "w", encoding=TRANSCRIPTION["output"]["text_encoding"]
            ) as f:
                json.dump(
                    result.to_dict(),
                    f,
                    indent=TRANSCRIPTION["output"]["json_indent"],
                    ensure_ascii=False,
                )

            # Save clean text file
            text_path = transcript_dir / f"{base_name}_transcript.txt"
            self._write_text_transcript(result, text_path)

            logger.info(f"Transcription saved: {json_path}, {text_path}")
            return json_path, text_path

        except Exception as e:
            logger.error(f"Failed to save transcription results: {e}")
            raise

    def _write_text_transcript(self, result: TranscriptionResult, text_path: Path):
        """Write the formatted text transcript."""
        with open(
            text_path, "w", encoding=TRANSCRIPTION["output"]["text_encoding"]
        ) as f:
            f.write(f"# {result.video_path.name} - Transcript\n\n")
            f.write(f"Duration: {result.duration:.1f} seconds\n")
            f.write(f"Language: {result.language}\n\n")
            f.write(
                "## Enhanced Transcript\n\n"
                if result.enhanced_text
                else "## Raw Transcript\n\n"
            )
            f.write(result.final_text)
            f.write("\n\n---\n\n")

            # Add segment breakdown
            f.write("## Segment Breakdown\n\n")
            for i, segment in enumerate(result.segments, 1):
                start_time = f"{int(segment['start']//60):02d}:{int(segment['start']%60):02d}"
                end_time = f"{int(segment['end']//60):02d}:{int(segment['end']%60):02d}"
                f.write(f"**{start_time}-{end_time}**: {segment['text']}\n\n")
