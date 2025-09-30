"""Batch 360° video projection conversion operations."""

import asyncio
import logging
from pathlib import Path
from typing import Any

from ..config import ProcessorConfig
from ..constants import ENCODING
from .models import ProjectionType, Video360ProcessingResult
from .projection_converter import ProjectionConverter

logger = logging.getLogger(__name__)


class BatchConverter:
    """Handles batch conversion operations for multiple 360° videos."""

    def __init__(self, config: ProcessorConfig):
        self.config = config
        self.projection_converter = ProjectionConverter(config)
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    async def batch_convert_projections(
        self,
        input_files: list[Path],
        output_dir: Path,
        target_projection: ProjectionType,
        batch_size: int = 4,
        quality_preset: str = "balanced",
    ) -> list[Video360ProcessingResult]:
        """
        Convert multiple videos to specified projection format.

        Args:
            input_files: List of input video files
            output_dir: Output directory for converted files
            target_projection: Target projection format
            batch_size: Number of concurrent conversions
            quality_preset: Quality preset (fast, balanced, quality, archive)

        Returns:
            List of processing results for each file
        """
        try:
            output_dir.mkdir(parents=True, exist_ok=True)

            # Process files in batches to avoid overwhelming system
            results = []

            for i in range(0, len(input_files), batch_size):
                batch = input_files[i:i + batch_size]
                batch_tasks = []

                for input_file in batch:
                    output_file = output_dir / f"{input_file.stem}_{target_projection.value}.mp4"
                    task = self.projection_converter.convert_projection(
                        input_file, output_file, target_projection
                    )
                    batch_tasks.append(task)

                # Process batch concurrently
                batch_results = await asyncio.gather(*batch_tasks, return_exceptions=True)

                # Filter out exceptions and add successful results
                for result in batch_results:
                    if isinstance(result, Video360ProcessingResult):
                        results.append(result)
                    else:
                        # Create error result for failed conversions
                        error_result = Video360ProcessingResult(
                            operation=f"batch_conversion_to_{target_projection.value}"
                        )
                        error_result.add_error(f"Conversion failed: {result}")
                        results.append(error_result)

                self.logger.info(f"Completed batch {i//batch_size + 1}/{(len(input_files) + batch_size - 1)//batch_size}")

            successful = sum(1 for r in results if r.success)
            self.logger.info(f"Batch conversion complete: {successful}/{len(input_files)} successful")
            return results

        except Exception as e:
            self.logger.error(f"Batch conversion error: {e}")
            raise

    async def create_cubemap_layouts(
        self,
        input_path: Path,
        output_dir: Path,
        layouts: list[str] | None = None,
    ) -> list[Path]:
        """
        Create multiple cubemap layout variations from equirectangular video.

        Args:
            input_path: Source equirectangular video
            output_dir: Output directory for cubemap layouts
            layouts: List of layout types (3x2, 2x3, 1x6, etc.)

        Returns:
            List of created cubemap files
        """
        try:
            if layouts is None:
                layouts = ["c3x2", "c2x3", "c1x6"]  # Common cubemap layouts

            output_dir.mkdir(parents=True, exist_ok=True)
            created_files = []

            for layout in layouts:
                output_file = output_dir / f"{input_path.stem}_cubemap_{layout}.mp4"

                # Use the projection converter with specific cubemap layout
                result = await self.projection_converter.convert_projection(
                    input_path, output_file, ProjectionType.CUBEMAP
                )

                if result.success:
                    created_files.append(output_file)
                    self.logger.info(f"Created cubemap layout {layout}: {output_file}")
                else:
                    self.logger.error(f"Failed to create layout {layout}: {result.errors}")

            return created_files

        except Exception as e:
            self.logger.error(f"Cubemap layout creation error: {e}")
            raise

    def get_conversion_matrix(self) -> dict[ProjectionType, list[ProjectionType]]:
        """Get supported conversion matrix between projection types."""
        return {
            ProjectionType.EQUIRECTANGULAR: [
                ProjectionType.CUBEMAP,
                ProjectionType.EAC,
                ProjectionType.FISHEYE,
                ProjectionType.STEREOGRAPHIC,
                ProjectionType.FLAT,
            ],
            ProjectionType.CUBEMAP: [
                ProjectionType.EQUIRECTANGULAR,
                ProjectionType.EAC,
                ProjectionType.FLAT,
            ],
            ProjectionType.EAC: [
                ProjectionType.EQUIRECTANGULAR,
                ProjectionType.CUBEMAP,
                ProjectionType.FLAT,
            ],
            ProjectionType.FISHEYE: [
                ProjectionType.EQUIRECTANGULAR,
                ProjectionType.FLAT,
            ],
            ProjectionType.STEREOGRAPHIC: [
                ProjectionType.EQUIRECTANGULAR,
                ProjectionType.FLAT,
            ],
        }

    def estimate_conversion_time(
        self,
        input_path: Path,
        target_projection: ProjectionType,
        quality_preset: str = "balanced",
    ) -> dict[str, Any]:
        """
        Estimate conversion time and resource requirements.

        Returns:
            Dictionary with estimated time, CPU usage, and memory requirements
        """
        try:
            file_size_mb = input_path.stat().st_size / (1024 * 1024)

            # Get multipliers from constants
            preset_multipliers = ENCODING["time_multipliers"]
            complexity_multipliers = {
                ProjectionType.FLAT: ENCODING["projection_complexity"]["flat"],
                ProjectionType.EQUIRECTANGULAR: ENCODING["projection_complexity"]["equirectangular"],
                ProjectionType.CUBEMAP: ENCODING["projection_complexity"]["cubemap"],
                ProjectionType.EAC: ENCODING["projection_complexity"]["eac"],
                ProjectionType.FISHEYE: ENCODING["projection_complexity"]["fisheye"],
                ProjectionType.STEREOGRAPHIC: ENCODING["projection_complexity"]["stereographic"],
            }

            base_time = file_size_mb / 1024  # Base time in minutes per GB
            preset_factor = preset_multipliers.get(quality_preset, 1.0)
            complexity_factor = complexity_multipliers.get(target_projection, 1.0)

            estimated_minutes = base_time * preset_factor * complexity_factor

            return {
                "estimated_time_minutes": max(estimated_minutes, 0.5),  # Minimum 30 seconds
                "estimated_cpu_usage": f"{min(80 + (preset_factor * 10), 95)}%",
                "estimated_memory_mb": min(512 + (file_size_mb * 0.1), 2048),
                "file_size_mb": file_size_mb,
                "quality_preset": quality_preset,
                "complexity_factor": complexity_factor,
            }

        except Exception as e:
            self.logger.error(f"Estimation error: {e}")
            return {
                "estimated_time_minutes": "unknown",
                "error": str(e),
            }
