"""360° video thumbnail generation - compatibility layer."""

import logging
from pathlib import Path

from ..config import ProcessorConfig
from .thumbnail_360 import Thumbnail360Orchestrator, ViewingAngle

# Optional dependency handling
try:
    from ..utils.video_360 import ProjectionType
except ImportError:
    # Fallback types when dependencies not available
    ProjectionType = str

# Re-export for backward compatibility
__all__ = ["Thumbnail360Generator", "ViewingAngle"]

logger = logging.getLogger(__name__)


class Thumbnail360Generator:
    """Compatibility wrapper for 360° thumbnail generation."""

    def __init__(self, config: ProcessorConfig) -> None:
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

        # Delegate to new orchestrator
        self._orchestrator = Thumbnail360Orchestrator(config)

        # Expose config for backward compatibility
        self.config = config

        self.logger.info("360° thumbnail generator initialized (compatibility layer)")

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
        # Delegate to orchestrator
        return self._orchestrator.generate_360_thumbnails(
            video_path=video_path,
            output_dir=output_dir,
            timestamp=timestamp,
            video_id=video_id,
            projection_type=projection_type,
            viewing_angles=viewing_angles,
        )


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
        # Delegate to orchestrator
        return self._orchestrator.generate_360_sprite_thumbnails(
            video_path=video_path,
            output_dir=output_dir,
            video_id=video_id,
            projection_type=projection_type,
            viewing_angle=viewing_angle,
        )
