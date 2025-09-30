"""360° video conversion orchestrator."""

import logging
from pathlib import Path

from ..config import ProcessorConfig
from .batch_converter import BatchConverter
from .conversion_utils import ConversionUtils
from .models import ProjectionType, Video360ProcessingResult
from .preview_generator import PreviewGenerator
from .projection_converter import ProjectionConverter

logger = logging.getLogger(__name__)


class Video360ConversionOrchestrator:
    """
    Orchestrates all 360° video conversion operations.

    This class coordinates between specialized conversion classes:
    - ProjectionConverter: Core projection transformations
    - BatchConverter: Batch processing operations
    - PreviewGenerator: Preview and demo content creation
    - ConversionUtils: Utility functions and estimations
    """

    def __init__(self, config: ProcessorConfig):
        self.config = config
        self.projection_converter = ProjectionConverter(config)
        self.batch_converter = BatchConverter(config)
        self.preview_generator = PreviewGenerator(config)
        self.utils = ConversionUtils()
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    async def convert_projection(
        self,
        input_path: Path,
        output_path: Path,
        target_projection: ProjectionType,
        output_resolution: tuple[int, int] | None = None,
        source_projection: ProjectionType | None = None,
    ) -> Video360ProcessingResult:
        """
        Convert between 360° projections using the projection converter.

        Args:
            input_path: Source video path
            output_path: Output video path
            target_projection: Target projection type
            output_resolution: Optional (width, height) for output
            source_projection: Source projection (auto-detected if None)

        Returns:
            Video360ProcessingResult with conversion details
        """
        return await self.projection_converter.convert_projection(
            input_path, output_path, target_projection, output_resolution, source_projection
        )

    async def batch_convert_projections(
        self,
        input_files: list[Path],
        output_dir: Path,
        target_projection: ProjectionType,
        batch_size: int = 4,
        quality_preset: str = "balanced",
    ) -> list[Video360ProcessingResult]:
        """
        Convert multiple videos to specified projection format using batch converter.

        Args:
            input_files: List of input video files
            output_dir: Output directory for converted files
            target_projection: Target projection format
            batch_size: Number of concurrent conversions
            quality_preset: Quality preset (fast, balanced, quality, archive)

        Returns:
            List of processing results for each file
        """
        return await self.batch_converter.batch_convert_projections(
            input_files, output_dir, target_projection, batch_size, quality_preset
        )

    async def create_cubemap_layouts(
        self,
        input_path: Path,
        output_dir: Path,
        layouts: list[str] | None = None,
    ) -> list[Path]:
        """
        Create multiple cubemap layout variations using batch converter.

        Args:
            input_path: Source equirectangular video
            output_dir: Output directory for cubemap layouts
            layouts: List of layout types (3x2, 2x3, 1x6, etc.)

        Returns:
            List of created cubemap files
        """
        return await self.batch_converter.create_cubemap_layouts(
            input_path, output_dir, layouts
        )

    async def create_projection_preview_grid(
        self,
        input_path: Path,
        output_path: Path,
        source_projection: ProjectionType = ProjectionType.EQUIRECTANGULAR,
        grid_size: tuple[int, int] = (2, 3),
        preview_duration: float = 10.0,
    ) -> Video360ProcessingResult:
        """
        Create a preview grid showing different projections using preview generator.

        Args:
            input_path: Source video
            output_path: Output preview video
            source_projection: Source projection type
            grid_size: Grid dimensions (cols, rows)
            preview_duration: Duration of preview in seconds

        Returns:
            Video360ProcessingResult with preview creation details
        """
        return await self.preview_generator.create_projection_preview_grid(
            input_path, output_path, source_projection, grid_size, preview_duration
        )

    async def create_motion_preview(
        self,
        input_path: Path,
        output_path: Path,
        duration: float = 30.0,
    ) -> Video360ProcessingResult:
        """
        Create a motion preview showing camera movement through 360° space.

        Args:
            input_path: Source 360° video
            output_path: Output motion preview
            duration: Duration of motion preview

        Returns:
            Video360ProcessingResult with motion preview details
        """
        return await self.preview_generator.create_motion_preview(
            input_path, output_path, duration
        )

    def get_supported_projections(self) -> list[ProjectionType]:
        """Get list of supported projection types."""
        return self.utils.get_supported_projections()

    def get_conversion_matrix(self) -> dict[ProjectionType, list[ProjectionType]]:
        """Get matrix of supported conversions between projection types."""
        return self.utils.get_conversion_matrix()

    def estimate_conversion_time(
        self,
        source_projection: ProjectionType,
        target_projection: ProjectionType,
        input_resolution: tuple[int, int],
        duration_seconds: float,
        quality_preset: str = "balanced",
    ) -> dict:
        """
        Estimate conversion time and resource requirements.

        Args:
            source_projection: Source projection
            target_projection: Target projection
            input_resolution: Input video resolution
            duration_seconds: Input video duration
            quality_preset: Quality preset used

        Returns:
            Dictionary with time and resource estimates
        """
        return self.utils.estimate_conversion_time(
            source_projection, target_projection, input_resolution, duration_seconds, quality_preset
        )

    def validate_conversion_feasibility(
        self,
        source_projection: ProjectionType,
        target_projection: ProjectionType,
    ) -> tuple[bool, str]:
        """
        Validate if a conversion between projections is feasible.

        Args:
            source_projection: Source projection type
            target_projection: Target projection type

        Returns:
            Tuple of (is_feasible, reason_if_not)
        """
        return self.utils.validate_conversion_feasibility(source_projection, target_projection)

    def get_recommended_resolution(
        self,
        source_projection: ProjectionType,
        target_projection: ProjectionType,
        source_resolution: tuple[int, int],
    ) -> tuple[int, int]:
        """
        Get recommended output resolution for conversion.

        Args:
            source_projection: Source projection type
            target_projection: Target projection type
            source_resolution: Source video resolution

        Returns:
            Recommended output resolution (width, height)
        """
        return self.utils.get_recommended_resolution(
            source_projection, target_projection, source_resolution
        )
