"""Main orchestrator for 360° thumbnail generation."""

import logging
from pathlib import Path
from typing import Literal

from ...config import ProcessorConfig
from ...exceptions import EncodingError
from .frame_extractor import Frame360Extractor
from .projection_processor import ProjectionProcessor
from .sprite_generator import Sprite360Generator

# Optional dependency handling
try:
    import cv2

    from ...utils.video_360 import HAS_360_SUPPORT, ProjectionType
except ImportError:
    # Fallback types when dependencies not available
    ProjectionType = str
    HAS_360_SUPPORT = False

ViewingAngle = Literal["front", "back", "left", "right", "up", "down", "stereographic"]

logger = logging.getLogger(__name__)


class Thumbnail360Orchestrator:
    """
    Main orchestrator for 360° thumbnail generation that coordinates
    frame extraction, projection processing, and sprite generation.
    """

    def __init__(self, config: ProcessorConfig) -> None:
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.config = config

        if not HAS_360_SUPPORT:
            raise ImportError(
                "360° thumbnail generation requires optional dependencies. "
                "Install with: uv add 'video-processor[video-360]'"
            )

        # Initialize component processors
        self.frame_extractor = Frame360Extractor(config)
        self.projection_processor = ProjectionProcessor(config)
        self.sprite_generator = Sprite360Generator(config)

        self.logger.info("360° thumbnail orchestrator initialized")

    def generate_360_thumbnails(
        self,
        video_path: Path,
        output_dir: Path,
        timestamp: int,
        video_id: str,
        projection_type: ProjectionType = "equirectangular",
        viewing_angles: list[ViewingAngle] | None = None,
    ) -> dict[str, Path]:
        """
        Generate 360° thumbnails for different viewing angles.

        Args:
            video_path: Path to 360° video file
            output_dir: Output directory
            timestamp: Time in seconds to extract thumbnail
            video_id: Unique video identifier
            projection_type: Type of 360° projection
            viewing_angles: List of viewing angles to generate

        Returns:
            Dictionary mapping viewing angles to thumbnail paths
        """
        if viewing_angles is None:
            viewing_angles = self.config.thumbnail_360_projections

        self.logger.info(
            f"Generating 360° thumbnails for {len(viewing_angles)} angles at {timestamp}s"
        )

        thumbnails = {}

        # First extract a full equirectangular frame
        equirect_frame = self.frame_extractor.extract_equirectangular_frame(
            video_path, timestamp, output_dir, video_id
        )

        try:
            # Load the equirectangular image
            equirect_img = cv2.imread(str(equirect_frame))
            if equirect_img is None:
                raise EncodingError(
                    f"Failed to load equirectangular frame: {equirect_frame}"
                )

            # Generate thumbnails for each viewing angle
            for angle in viewing_angles:
                thumbnail_path = self.projection_processor.generate_angle_thumbnail(
                    equirect_img, angle, output_dir, video_id, timestamp
                )
                thumbnails[angle] = thumbnail_path
                self.logger.debug(f"Generated {angle} thumbnail: {thumbnail_path}")

        finally:
            # Clean up temporary equirectangular frame
            if equirect_frame.exists():
                equirect_frame.unlink()

        self.logger.info(f"Generated {len(thumbnails)} 360° thumbnails")
        return thumbnails

    def generate_360_sprite_thumbnails(
        self,
        video_path: Path,
        output_dir: Path,
        video_id: str,
        projection_type: ProjectionType = "equirectangular",
        viewing_angle: ViewingAngle = "front",
    ) -> tuple[Path, Path]:
        """
        Generate 360° sprite sheet for a specific viewing angle.

        Args:
            video_path: Path to 360° video file
            output_dir: Output directory
            video_id: Unique video identifier
            projection_type: Type of 360° projection
            viewing_angle: Viewing angle for sprite generation

        Returns:
            Tuple of (sprite_file_path, webvtt_file_path)
        """
        self.logger.info(f"Generating 360° sprite sheet for {viewing_angle} angle")

        # Pass self as thumbnail_generator to avoid circular imports
        return self.sprite_generator.generate_360_sprite_thumbnails(
            video_path=video_path,
            output_dir=output_dir,
            video_id=video_id,
            projection_type=projection_type,
            viewing_angle=viewing_angle,
            thumbnail_generator=self,
        )

    def get_video_info(self, video_path: Path) -> dict:
        """Get video metadata for processing."""
        return self.frame_extractor.get_video_info(video_path)

    def get_capabilities(self) -> dict[str, bool]:
        """Get information about available 360° processing capabilities."""
        return {
            "frame_extraction": True,
            "perspective_projection": True,
            "stereographic_projection": True,
            "sprite_generation": True,
            "webvtt_support": True,
            "multi_angle_support": True,
        }
