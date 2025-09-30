"""Core 360° video processor - Refactored orchestrator."""

import logging
from pathlib import Path

from ..config import ProcessorConfig
from .metadata_detector import MetadataDetector
from .models import (
    ProjectionType,
    SphericalMetadata,
    StereoMode,
    Video360Analysis,
    Video360ProcessingResult,
    ViewportConfig,
)
from .projection_converter import ProjectionConverter
from .quality_analyzer import QualityAnalyzer
from .stereo_processor import StereoProcessor
from .viewport_extractor import ViewportExtractor

logger = logging.getLogger(__name__)


class Video360Processor:
    """
    Core 360° video processing engine.

    Orchestrates specialized components for projection conversion, viewport extraction,
    stereoscopic processing, and quality analysis of 360° videos.
    """

    def __init__(self, config: ProcessorConfig):
        self.config = config

        # Initialize specialized processors
        self.metadata_detector = MetadataDetector(config)
        self.projection_converter = ProjectionConverter(config)
        self.viewport_extractor = ViewportExtractor(config)
        self.quality_analyzer = QualityAnalyzer(config)
        self.stereo_processor = StereoProcessor(config)

        logger.info(
            f"Video360Processor initialized with {len(self._get_processors())} specialized processors"
        )

    def _get_processors(self) -> list:
        """Get list of specialized processors for monitoring."""
        return [
            self.metadata_detector,
            self.projection_converter,
            self.viewport_extractor,
            self.quality_analyzer,
            self.stereo_processor,
        ]

    # Metadata operations
    async def extract_spherical_metadata(self, video_path: Path) -> SphericalMetadata:
        """Extract spherical metadata from video file."""
        return await self.metadata_detector.extract_spherical_metadata(video_path)

    # Projection operations
    async def convert_projection(
        self,
        input_path: Path,
        output_path: Path,
        target_projection: ProjectionType,
        output_resolution: tuple | None = None,
        source_projection: ProjectionType | None = None,
    ) -> Video360ProcessingResult:
        """Convert between different 360° projections."""
        return await self.projection_converter.convert_projection(
            input_path=input_path,
            output_path=output_path,
            target_projection=target_projection,
            output_resolution=output_resolution,
            source_projection=source_projection,
        )

    # Viewport operations
    async def extract_viewport(
        self, input_path: Path, output_path: Path, viewport_config: ViewportConfig
    ) -> Video360ProcessingResult:
        """Extract flat viewport from 360° video."""
        return await self.viewport_extractor.extract_viewport(
            input_path=input_path,
            output_path=output_path,
            viewport_config=viewport_config,
        )

    async def extract_animated_viewport(
        self,
        input_path: Path,
        output_path: Path,
        viewport_function,
    ) -> Video360ProcessingResult:
        """Extract animated viewport with camera movement."""
        return await self.viewport_extractor.extract_animated_viewport(
            input_path=input_path,
            output_path=output_path,
            viewport_function=viewport_function,
        )

    # Stereoscopic operations
    async def stereo_to_mono(
        self, input_path: Path, output_path: Path, eye: str = "left"
    ) -> Video360ProcessingResult:
        """Convert stereoscopic 360° video to monoscopic."""
        return await self.stereo_processor.stereo_to_mono(
            input_path=input_path, output_path=output_path, eye=eye
        )

    async def convert_stereo_mode(
        self, input_path: Path, output_path: Path, target_mode: StereoMode
    ) -> Video360ProcessingResult:
        """Convert between stereoscopic modes."""
        return await self.stereo_processor.convert_stereo_mode(
            input_path=input_path, output_path=output_path, target_mode=target_mode
        )

    # Quality analysis operations
    async def analyze_360_content(self, video_path: Path) -> Video360Analysis:
        """Analyze 360° video content for optimization recommendations."""
        # First extract metadata
        metadata = await self.extract_spherical_metadata(video_path)

        # Then perform quality analysis
        return await self.quality_analyzer.analyze_360_content(
            video_path=video_path, metadata=metadata
        )

    # Helper methods for backward compatibility and convenience
    def get_optimal_projections(self, metadata: SphericalMetadata) -> list[ProjectionType]:
        """Get optimal projection recommendations based on metadata."""
        # Create dummy quality for compatibility
        from .models import Video360Quality
        dummy_quality = Video360Quality()
        return self.quality_analyzer._recommend_projections(metadata, dummy_quality)

    def generate_recommended_viewports(self, metadata: SphericalMetadata) -> list[ViewportConfig]:
        """Generate recommended viewports for thumbnail generation."""
        return self.quality_analyzer._recommend_viewports(metadata)
