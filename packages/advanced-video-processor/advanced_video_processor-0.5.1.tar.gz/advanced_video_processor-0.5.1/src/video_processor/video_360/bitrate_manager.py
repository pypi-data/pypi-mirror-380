"""360° video bitrate ladder management and optimization."""

import logging

from ..config import ProcessorConfig
from ..constants import VIDEO_360
from ..streaming.adaptive import BitrateLevel
from .models import BitrateLevel360, ProjectionType

logger = logging.getLogger(__name__)


class BitrateManager:
    """Manages bitrate ladder generation for 360° video streaming."""

    def __init__(self, config: ProcessorConfig):
        self.config = config
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    async def generate_360_bitrate_ladder(
        self,
        video_path: str,
        projection: ProjectionType,
        target_formats: list[str] | None = None,
    ) -> list[BitrateLevel360]:
        """
        Generate optimized bitrate ladder for 360° video.

        Adjusts standard bitrate levels based on projection type and 360° characteristics.
        """
        try:
            # Get base bitrate levels
            base_levels = self._get_base_bitrate_levels()

            # Apply 360° specific adjustments
            projection_multiplier = self._get_projection_bitrate_multiplier(projection)

            adapted_levels = []
            for level in base_levels:
                # Apply 360° bitrate multiplier
                adapted_bitrate = int(level.bitrate * projection_multiplier)

                # Create 360° specific bitrate level
                level_360 = BitrateLevel360(
                    quality=level.quality,
                    bitrate=adapted_bitrate,
                    resolution=(level.width, level.height),
                    fps=level.fps,
                    projection=projection,
                    is_viewport_optimized=False,
                    tiling_enabled=self._should_enable_tiling(level.width, level.height),
                )

                adapted_levels.append(level_360)

            self.logger.info(f"Generated {len(adapted_levels)} bitrate levels for {projection.value}")
            return adapted_levels

        except Exception as e:
            self.logger.error(f"Failed to generate 360° bitrate ladder: {e}")
            raise

    def _get_base_bitrate_levels(self) -> list[BitrateLevel]:
        """Get base bitrate levels for adaptation."""
        # Standard streaming bitrate levels
        return [
            BitrateLevel("low", 800_000, 854, 480, 24),
            BitrateLevel("medium", 2_000_000, 1280, 720, 30),
            BitrateLevel("high", 5_000_000, 1920, 1080, 30),
            BitrateLevel("ultra", 12_000_000, 3840, 2160, 30),
        ]

    def _get_projection_bitrate_multiplier(self, projection: ProjectionType) -> float:
        """Get bitrate multiplier based on projection type efficiency."""
        return VIDEO_360["bitrate_multipliers"]["projection_efficiency"].get(
            projection.value, VIDEO_360["bitrate_multipliers"]["projection_efficiency"]["default"]
        )

    def _should_enable_tiling(self, width: int, height: int) -> bool:
        """Determine if tiling should be enabled for this resolution."""
        # Enable tiling for 4K and above resolutions
        return width >= 3840 and height >= 2160

    def get_optimal_quality_for_bandwidth(self, available_bandwidth: int) -> str:
        """Get optimal quality level for available bandwidth."""
        if available_bandwidth >= 8_000_000:
            return "ultra"
        elif available_bandwidth >= 3_000_000:
            return "high"
        elif available_bandwidth >= 1_200_000:
            return "medium"
        else:
            return "low"
