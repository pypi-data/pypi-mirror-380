"""360° video projection conversion operations."""

import asyncio
import logging
import subprocess
import time
from pathlib import Path

from ..config import ProcessorConfig
from .metadata_detector import MetadataDetector
from .models import ProjectionType, Video360ProcessingResult

logger = logging.getLogger(__name__)


class ProjectionConverter:
    """Handles conversion between different 360° projection formats."""

    def __init__(self, config: ProcessorConfig):
        self.config = config
        self.metadata_detector = MetadataDetector(config)

    async def convert_projection(
        self,
        input_path: Path,
        output_path: Path,
        target_projection: ProjectionType,
        output_resolution: tuple | None = None,
        source_projection: ProjectionType | None = None,
    ) -> Video360ProcessingResult:
        """
        Convert between different 360° projections.

        Args:
            input_path: Source video path
            output_path: Output video path
            target_projection: Target projection type
            output_resolution: Optional (width, height) tuple
            source_projection: Source projection (auto-detect if None)

        Returns:
            Video360ProcessingResult with conversion details
        """
        start_time = time.time()
        result = Video360ProcessingResult(
            operation=f"projection_conversion_to_{target_projection.value}"
        )

        try:
            # Determine source projection if not provided
            if source_projection is None:
                # Use metadata detector to determine source projection
                source_metadata = await self.metadata_detector.extract_spherical_metadata(input_path)
                source_projection = source_metadata.projection
                if source_projection == ProjectionType.UNKNOWN:
                    source_projection = ProjectionType.EQUIRECTANGULAR
                    result.add_warning(
                        "Could not detect source projection, assuming equirectangular"
                    )

            # Build FFmpeg v360 filter command
            v360_filter = self._build_v360_filter(
                source_projection, target_projection, output_resolution
            )

            # Get file sizes
            result.file_size_before = input_path.stat().st_size

            # Build FFmpeg command
            cmd = [
                self.config.ffmpeg_path,
                "-i",
                str(input_path),
                "-vf",
                v360_filter,
                "-c:v",
                "libx264",
                "-preset",
                "medium",
                "-crf",
                "23",
                "-c:a",
                "copy",  # Copy audio unchanged
                str(output_path),
                "-y",
            ]

            # Add spherical metadata for output
            if target_projection != ProjectionType.FLAT:
                cmd.extend(
                    [
                        "-metadata",
                        "spherical=1",
                        "-metadata",
                        f"projection={target_projection.value}",
                    ]
                )

            # Execute conversion
            process_result = await asyncio.to_thread(
                subprocess.run, cmd, capture_output=True, text=True
            )

            if process_result.returncode == 0:
                result.success = True
                result.output_path = output_path
                result.file_size_after = output_path.stat().st_size

                logger.info(
                    f"Projection conversion successful: {source_projection.value} -> {target_projection.value}"
                )

            else:
                result.add_error(f"FFmpeg failed: {process_result.stderr}")
                logger.error(f"Projection conversion failed: {process_result.stderr}")

        except Exception as e:
            result.add_error(f"Conversion error: {e}")
            logger.error(f"Projection conversion error: {e}")

        result.processing_time = time.time() - start_time
        return result

    def _build_v360_filter(
        self,
        source_proj: ProjectionType,
        target_proj: ProjectionType,
        output_resolution: tuple | None = None,
    ) -> str:
        """Build FFmpeg v360 filter string."""
        # Map projection types to v360 format codes
        projection_map = {
            ProjectionType.EQUIRECTANGULAR: "e",
            ProjectionType.CUBEMAP: "c3x2",
            ProjectionType.EAC: "eac",
            ProjectionType.FISHEYE: "fisheye",
            ProjectionType.DUAL_FISHEYE: "dfisheye",
            ProjectionType.FLAT: "flat",
            ProjectionType.STEREOGRAPHIC: "sg",
            ProjectionType.MERCATOR: "mercator",
            ProjectionType.PANNINI: "pannini",
            ProjectionType.CYLINDRICAL: "cylindrical",
            ProjectionType.LITTLE_PLANET: "sg",  # Stereographic for little planet
        }

        source_format = projection_map.get(source_proj, "e")
        target_format = projection_map.get(target_proj, "e")

        filter_parts = [f"v360={source_format}:{target_format}"]

        # Add resolution if specified
        if output_resolution:
            filter_parts.append(f"w={output_resolution[0]}:h={output_resolution[1]}")

        return ":".join(filter_parts)
