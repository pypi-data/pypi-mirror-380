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
    ) -> tuple[Path, Path, Path | None]:
        """
        Save transcription results in multiple formats.

        Returns:
            Tuple of (json_path, text_path, webvtt_path)
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

            # Save WebVTT subtitle file if enabled and segments available
            webvtt_path = None
            if (TRANSCRIPTION["output"]["generate_vtt"]
                and result.segments
                and len(result.segments) > 0):
                webvtt_path = transcript_dir / f"{base_name}_subtitles.vtt"
                self._write_webvtt_transcript(result, webvtt_path)

            logger.info(f"Transcription saved: {json_path}, {text_path}" +
                       (f", {webvtt_path}" if webvtt_path else ""))
            return json_path, text_path, webvtt_path

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

    def _write_webvtt_transcript(self, result: TranscriptionResult, webvtt_path: Path):
        """Write WebVTT subtitle file for video players."""
        with open(
            webvtt_path, "w", encoding=TRANSCRIPTION["output"]["text_encoding"]
        ) as f:
            # WebVTT header
            f.write("WEBVTT\n")
            f.write(f"NOTE {result.video_path.name} - Generated Subtitles\n\n")

            # Add cues for each segment
            for i, segment in enumerate(result.segments, 1):
                start_time = self._format_webvtt_timestamp(segment["start"])
                end_time = self._format_webvtt_timestamp(segment["end"])

                # Clean text for subtitle display
                text = segment["text"].strip()
                if not text:
                    continue

                # Split long text into multiple lines (max ~40 chars per line)
                lines = self._split_subtitle_text(text)

                # Write WebVTT cue
                f.write(f"{start_time} --> {end_time}\n")
                f.write("\n".join(lines))
                f.write("\n\n")

        self.logger.info(f"WebVTT subtitle file created: {webvtt_path}")

    def _format_webvtt_timestamp(self, seconds: float) -> str:
        """Convert seconds to WebVTT timestamp format (HH:MM:SS.mmm)."""
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{secs:06.3f}"

    def _split_subtitle_text(self, text: str, max_length: int = 40) -> list[str]:
        """Split long text into subtitle-friendly lines."""
        if len(text) <= max_length:
            return [text]

        words = text.split()
        lines = []
        current_line = ""

        for word in words:
            test_line = f"{current_line} {word}".strip()
            if len(test_line) <= max_length:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word

        if current_line:
            lines.append(current_line)

        return lines
