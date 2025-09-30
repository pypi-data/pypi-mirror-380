"""360° video frame extraction utilities."""

import logging
from pathlib import Path

import ffmpeg

from ...config import ProcessorConfig
from ...exceptions import EncodingError, FFmpegError

logger = logging.getLogger(__name__)


class Frame360Extractor:
    """Handles extraction of equirectangular frames from 360° videos."""

    def __init__(self, config: ProcessorConfig) -> None:
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.config = config

    def extract_equirectangular_frame(
        self, video_path: Path, timestamp: int, output_dir: Path, video_id: str
    ) -> Path:
        """Extract a full equirectangular frame from the 360° video."""
        temp_frame = output_dir / f"{video_id}_temp_equirect_{timestamp}.jpg"

        try:
            # Get video info
            probe = ffmpeg.probe(str(video_path))
            video_stream = next(
                stream for stream in probe["streams"] if stream["codec_type"] == "video"
            )

            width = video_stream["width"]
            height = video_stream["height"]
            duration = float(video_stream.get("duration", 0))

            # Adjust timestamp if beyond video duration
            if timestamp >= duration:
                timestamp = max(1, int(duration // 2))

            # Extract full resolution frame
            (
                ffmpeg.input(str(video_path), ss=timestamp)
                .filter("scale", width, height)
                .output(str(temp_frame), vframes=1, q=2)  # High quality
                .overwrite_output()
                .run(capture_stdout=True, capture_stderr=True, quiet=True)
            )

        except ffmpeg.Error as e:
            error_msg = e.stderr.decode() if e.stderr else "Unknown FFmpeg error"
            raise FFmpegError(f"Frame extraction failed: {error_msg}") from e

        if not temp_frame.exists():
            raise EncodingError("Frame extraction failed - output file not created")

        return temp_frame

    def get_video_info(self, video_path: Path) -> dict:
        """Get video metadata for processing."""
        try:
            probe = ffmpeg.probe(str(video_path))
            video_stream = next(
                stream for stream in probe["streams"] if stream["codec_type"] == "video"
            )

            return {
                "width": video_stream["width"],
                "height": video_stream["height"],
                "duration": float(video_stream.get("duration", 0)),
                "fps": eval(video_stream.get("r_frame_rate", "30/1")),
            }

        except (ffmpeg.Error, StopIteration) as e:
            self.logger.error(f"Failed to get video info: {e}")
            raise EncodingError(f"Failed to analyze video: {e}") from e
