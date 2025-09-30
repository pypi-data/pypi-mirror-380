"""360° video quality analysis and assessment."""

import logging
from pathlib import Path

from ..config import ProcessorConfig
from ..constants import VIDEO_360
from .models import (
    ProjectionType,
    SphericalMetadata,
    Video360Analysis,
    Video360Quality,
    ViewportConfig,
)

logger = logging.getLogger(__name__)


class QualityAnalyzer:
    """Analyzes 360° video quality and provides optimization recommendations."""

    def __init__(self, config: ProcessorConfig):
        self.config = config

    async def analyze_360_content(self, video_path: Path, metadata: SphericalMetadata) -> Video360Analysis:
        """
        Analyze 360° video content for optimization recommendations.

        Args:
            video_path: Path to 360° video
            metadata: Pre-extracted spherical metadata

        Returns:
            Video360Analysis with detailed analysis results
        """
        try:
            # Initialize quality assessment
            quality = Video360Quality()

            # Analyze projection-specific characteristics
            quality = self._assess_projection_quality(metadata, quality)

            # Generate recommendations
            analysis = Video360Analysis(metadata=metadata, quality=quality)

            # Recommend optimal projections based on content
            analysis.optimal_projections = self._recommend_projections(metadata, quality)

            # Recommend viewports for thumbnail generation
            analysis.recommended_viewports = self._recommend_viewports(metadata)

            # Streaming recommendations based on video characteristics
            analysis.supports_viewport_adaptive = self._assess_viewport_adaptive_support(metadata, quality)
            analysis.supports_tiled_encoding = self._assess_tiled_encoding_support(metadata)

            return analysis

        except Exception as e:
            logger.error(f"360° content analysis failed: {e}")
            from ..exceptions import VideoProcessorError
            raise VideoProcessorError(f"Content analysis failed: {e}") from e

    def _assess_projection_quality(self, metadata: SphericalMetadata, quality: Video360Quality) -> Video360Quality:
        """Assess quality characteristics of the current projection."""
        # Get base quality from constants for projection type
        quality.projection_quality = VIDEO_360["projection_quality"].get(
            metadata.projection.value, VIDEO_360["quality_thresholds"]["default_fallback_quality"]
        )

        # Analyze projection-specific characteristics
        if metadata.projection == ProjectionType.EQUIRECTANGULAR:
            quality.pole_distortion = self._analyze_pole_distortion(metadata)
            quality.seam_quality = VIDEO_360["quality_thresholds"]["good_seam"]  # Equirectangular has good seam continuity

        elif metadata.projection == ProjectionType.CUBEMAP:
            quality.pole_distortion = 0.0  # No pole distortion in cubemap
            quality.seam_quality = VIDEO_360["quality_thresholds"]["acceptable_seam"]  # Potential seams at cube edges

        elif metadata.projection == ProjectionType.EAC:
            quality.pole_distortion = VIDEO_360["quality_thresholds"]["low_pole_distortion"]  # Minimal distortion
            quality.seam_quality = VIDEO_360["quality_thresholds"]["excellent_seam"]  # Excellent seam quality

        else:
            # Default values for other projections
            quality.pole_distortion = VIDEO_360["quality_thresholds"]["moderate_pole_distortion"]
            quality.seam_quality = VIDEO_360["quality_thresholds"]["default_good_quality"]

        # Set default viewport quality based on projection
        quality.viewport_quality = quality.projection_quality * VIDEO_360["quality_thresholds"]["high_viewport_quality"]

        return quality

    def _analyze_pole_distortion(self, metadata: SphericalMetadata) -> float:
        """Analyze pole distortion for equirectangular projection."""
        if metadata.projection != ProjectionType.EQUIRECTANGULAR:
            return 0.0

        # Distortion increases with resolution height for equirectangular
        # Higher resolutions have more pronounced pole stretching
        if hasattr(metadata, 'height') and metadata.height:
            # Normalize to common resolutions and calculate distortion factor
            height_factor = min(metadata.height / VIDEO_360["distortion"]["height_normalization"], VIDEO_360["distortion"]["max_height_multiplier"])  # Normalize to 4K height
            distortion = height_factor * VIDEO_360["distortion"]["height_distortion_factor"]  # Max 25% distortion at very high res
        else:
            # Default moderate distortion when height unknown
            distortion = VIDEO_360["distortion"]["moderate_distortion"]

        return min(distortion, VIDEO_360["quality_thresholds"]["max_pole_distortion"])  # Cap at 30% max distortion

    def _recommend_projections(
        self, metadata: SphericalMetadata, quality: Video360Quality
    ) -> list[ProjectionType]:
        """Recommend optimal projections based on content analysis."""
        recommendations = []

        # Always include source projection first
        recommendations.append(metadata.projection)

        # Add complementary projections based on source
        if metadata.projection == ProjectionType.EQUIRECTANGULAR:
            # EAC is excellent for high-quality viewing
            recommendations.extend([ProjectionType.EAC, ProjectionType.CUBEMAP])
        elif metadata.projection == ProjectionType.CUBEMAP:
            # Cubemap converts well to equirectangular and EAC
            recommendations.extend([ProjectionType.EQUIRECTANGULAR, ProjectionType.EAC])
        elif metadata.projection == ProjectionType.EAC:
            # EAC maintains quality when converting
            recommendations.extend([ProjectionType.CUBEMAP, ProjectionType.EQUIRECTANGULAR])
        else:
            # For other projections, recommend standard options
            recommendations.extend([ProjectionType.EQUIRECTANGULAR, ProjectionType.CUBEMAP])

        # Add flat viewport extraction for all content
        # This is useful for creating traditional video previews
        recommendations.append(ProjectionType.FLAT)

        # Remove duplicates while preserving order
        seen = set()
        unique_recommendations = []
        for proj in recommendations:
            if proj not in seen:
                seen.add(proj)
                unique_recommendations.append(proj)

        return unique_recommendations[:4]  # Limit to top 4 recommendations

    def _recommend_viewports(self, metadata: SphericalMetadata) -> list[ViewportConfig]:
        """Recommend viewports for thumbnail generation and preview extraction."""
        viewports = []

        # Standard cardinal directions for comprehensive coverage
        standard_views = [
            ViewportConfig(yaw=0, pitch=0, fov=90, width=1920, height=1080),    # Front
            ViewportConfig(yaw=90, pitch=0, fov=90, width=1920, height=1080),   # Right
            ViewportConfig(yaw=180, pitch=0, fov=90, width=1920, height=1080),  # Back
            ViewportConfig(yaw=270, pitch=0, fov=90, width=1920, height=1080),  # Left
            ViewportConfig(yaw=0, pitch=45, fov=90, width=1920, height=1080),   # Up-Front
            ViewportConfig(yaw=0, pitch=-45, fov=90, width=1920, height=1080),  # Down-Front
        ]

        viewports.extend(standard_views)

        # Add initial view from metadata if it differs from front view
        if (hasattr(metadata, 'initial_view_heading') and
            hasattr(metadata, 'initial_view_pitch') and
            (metadata.initial_view_heading != 0 or metadata.initial_view_pitch != 0)):

            viewports.append(
                ViewportConfig(
                    yaw=metadata.initial_view_heading,
                    pitch=metadata.initial_view_pitch,
                    roll=getattr(metadata, 'initial_view_roll', 0),
                    fov=90,
                    width=1920,
                    height=1080
                )
            )

        return viewports

    def _assess_viewport_adaptive_support(self, metadata: SphericalMetadata, quality: Video360Quality) -> bool:
        """Determine if content supports viewport-adaptive streaming."""
        # Viewport-adaptive streaming works best with certain projections
        projection_supported = metadata.projection in [
            ProjectionType.EQUIRECTANGULAR,
            ProjectionType.CUBEMAP,
            ProjectionType.EAC
        ]

        # Quality should be reasonable for adaptive streaming
        quality_adequate = quality.projection_quality > VIDEO_360["quality_thresholds"]["medium_confidence"]

        # Check if we can determine motion characteristics
        motion_suitable = True
        if hasattr(quality, 'motion_intensity') and quality.motion_intensity:
            # Lower motion content is better for viewport adaptation
            motion_suitable = quality.motion_intensity < VIDEO_360["quality_thresholds"]["motion_suitable_threshold"]

        return projection_supported and quality_adequate and motion_suitable

    def _assess_tiled_encoding_support(self, metadata: SphericalMetadata) -> bool:
        """Determine if content supports tiled encoding optimization."""
        # Tiled encoding requires minimum resolution for benefits
        resolution_adequate = (
            hasattr(metadata, 'width') and
            metadata.width and
            metadata.width >= 3840  # Minimum 4K width
        )

        # Only certain projections benefit from tiling
        projection_supported = metadata.projection in [
            ProjectionType.EQUIRECTANGULAR,
            ProjectionType.EAC,
            ProjectionType.CUBEMAP
        ]

        return resolution_adequate and projection_supported
