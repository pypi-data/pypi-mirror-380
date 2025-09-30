"""360° sprite sheet generation for video scrubbing."""

import logging
import math
from pathlib import Path
from typing import Literal

import ffmpeg

from ...config import ProcessorConfig
from ...constants import THUMBNAILS
from ...exceptions import EncodingError

# Optional dependency handling
try:
    import cv2
    import numpy as np

    HAS_OPENCV = True
except ImportError:
    HAS_OPENCV = False

# Type imports
try:
    from ...utils.video_360 import ProjectionType
except ImportError:
    ProjectionType = str

ViewingAngle = Literal["front", "back", "left", "right", "up", "down", "stereographic"]

logger = logging.getLogger(__name__)


class Sprite360Generator:
    """Handles 360° sprite sheet generation for video scrubbing."""

    def __init__(self, config: ProcessorConfig) -> None:
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.config = config

        if not HAS_OPENCV:
            raise ImportError(
                "Sprite generation requires opencv-python. "
                "Install with: uv add opencv-python"
            )

    def generate_360_sprite_thumbnails(
        self,
        video_path: Path,
        output_dir: Path,
        video_id: str,
        projection_type: ProjectionType = "equirectangular",
        viewing_angle: ViewingAngle = "front",
        thumbnail_generator=None,  # Will be injected to avoid circular imports
    ) -> tuple[Path, Path]:
        """
        Generate 360° sprite sheet for a specific viewing angle.

        Args:
            video_path: Path to 360° video file
            output_dir: Output directory
            video_id: Unique video identifier
            projection_type: Type of 360° projection
            viewing_angle: Viewing angle for sprite generation
            thumbnail_generator: Thumbnail360Generator instance for generating frames

        Returns:
            Tuple of (sprite_file_path, webvtt_file_path)
        """
        sprite_file = output_dir / f"{video_id}_360_{viewing_angle}_sprite.jpg"
        webvtt_file = output_dir / f"{video_id}_360_{viewing_angle}_sprite.webvtt"
        frames_dir = output_dir / "frames_360"

        # Create frames directory
        frames_dir.mkdir(exist_ok=True)

        try:
            # Get video duration
            probe = ffmpeg.probe(str(video_path))
            duration = float(probe["format"]["duration"])

            # Generate frames at specified intervals
            interval = self.config.sprite_interval
            timestamps = list(range(0, int(duration), interval))

            frame_paths = []
            for i, timestamp in enumerate(timestamps):
                # Generate 360° thumbnail for this timestamp
                if thumbnail_generator:
                    thumbnails = thumbnail_generator.generate_360_thumbnails(
                        video_path,
                        frames_dir,
                        timestamp,
                        f"{video_id}_frame_{i}",
                        projection_type,
                        [viewing_angle],
                    )

                    if viewing_angle in thumbnails:
                        frame_paths.append(thumbnails[viewing_angle])

            # Create sprite sheet from frames
            if frame_paths:
                self.create_sprite_sheet(
                    frame_paths, sprite_file, timestamps, webvtt_file
                )

            return sprite_file, webvtt_file

        finally:
            # Clean up frame files
            if frames_dir.exists():
                for frame_file in frames_dir.glob("*"):
                    if frame_file.is_file():
                        frame_file.unlink()
                frames_dir.rmdir()

    def create_sprite_sheet(
        self,
        frame_paths: list[Path],
        sprite_file: Path,
        timestamps: list[int],
        webvtt_file: Path,
    ) -> None:
        """Create sprite sheet from individual frames."""
        if not frame_paths:
            raise EncodingError("No frames available for sprite sheet creation")

        # Load first frame to get dimensions
        first_frame = cv2.imread(str(frame_paths[0]))
        if first_frame is None:
            raise EncodingError(f"Failed to load first frame: {frame_paths[0]}")

        frame_height, frame_width = first_frame.shape[:2]

        # Calculate sprite sheet layout
        cols = THUMBNAILS["sprite_columns"]  # From constants
        rows = math.ceil(len(frame_paths) / cols)

        sprite_width = cols * frame_width
        sprite_height = rows * frame_height

        # Create sprite sheet
        sprite_img = np.zeros((sprite_height, sprite_width, 3), dtype=np.uint8)

        # Create WebVTT content
        webvtt_content = ["WEBVTT", ""]

        # Place frames in sprite sheet and create WebVTT entries
        for i, (frame_path, timestamp) in enumerate(
            zip(frame_paths, timestamps, strict=False)
        ):
            frame = cv2.imread(str(frame_path))
            if frame is None:
                continue

            # Calculate position in sprite
            col = i % cols
            row = i // cols

            x_start = col * frame_width
            y_start = row * frame_height
            x_end = x_start + frame_width
            y_end = y_start + frame_height

            # Place frame in sprite
            sprite_img[y_start:y_end, x_start:x_end] = frame

            # Create WebVTT entry
            start_time = f"{timestamp // 3600:02d}:{(timestamp % 3600) // 60:02d}:{timestamp % 60:02d}.000"
            end_time = f"{(timestamp + 1) // 3600:02d}:{((timestamp + 1) % 3600) // 60:02d}:{(timestamp + 1) % 60:02d}.000"

            webvtt_content.extend(
                [
                    f"{start_time} --> {end_time}",
                    f"{sprite_file.name}#xywh={x_start},{y_start},{frame_width},{frame_height}",
                    "",
                ]
            )

        # Save sprite sheet
        cv2.imwrite(
            str(sprite_file),
            sprite_img,
            [cv2.IMWRITE_JPEG_QUALITY, THUMBNAILS["quality"]]
        )

        # Save WebVTT file
        with open(webvtt_file, "w") as f:
            f.write("\n".join(webvtt_content))

        self.logger.info(f"Created sprite sheet: {sprite_file} ({len(frame_paths)} frames)")
        self.logger.info(f"Created WebVTT file: {webvtt_file}")
