"""360° video viewport extraction operations."""

import asyncio
import logging
import subprocess
import time
from collections.abc import Callable
from pathlib import Path

from ..config import ProcessorConfig
from ..exceptions import VideoProcessorError
from .metadata_detector import MetadataDetector
from .models import (
    ProjectionType,
    SphericalMetadata,
    Video360ProcessingResult,
    ViewportConfig,
)

logger = logging.getLogger(__name__)


class ViewportExtractor:
    """Handles viewport extraction from 360° videos."""

    def __init__(self, config: ProcessorConfig):
        self.config = config
        self.metadata_detector = MetadataDetector(config)

    async def extract_viewport(
        self, input_path: Path, output_path: Path, viewport_config: ViewportConfig
    ) -> Video360ProcessingResult:
        """
        Extract flat viewport from 360° video.

        Args:
            input_path: Source 360° video
            output_path: Output flat video
            viewport_config: Viewport extraction settings

        Returns:
            Video360ProcessingResult with extraction details
        """
        if not viewport_config.validate():
            raise VideoProcessorError("Invalid viewport configuration")

        start_time = time.time()
        result = Video360ProcessingResult(operation="viewport_extraction")

        try:
            # Extract source metadata to determine projection
            source_metadata = await self.metadata_detector.extract_spherical_metadata(input_path)
            source_projection = source_metadata.projection
            if source_projection == ProjectionType.UNKNOWN:
                source_projection = ProjectionType.EQUIRECTANGULAR
                result.add_warning("Could not detect source projection, assuming equirectangular")

            if not source_metadata.is_spherical:
                result.add_warning("Source video may not be 360°")

            # Build v360 filter for viewport extraction
            v360_filter = (
                f"v360={source_projection.value}:flat:"
                f"yaw={viewport_config.yaw}:"
                f"pitch={viewport_config.pitch}:"
                f"roll={viewport_config.roll}:"
                f"fov={viewport_config.fov}:"
                f"w={viewport_config.width}:"
                f"h={viewport_config.height}"
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
                "copy",
                str(output_path),
                "-y",
            ]

            # Execute extraction
            process_result = await asyncio.to_thread(
                subprocess.run, cmd, capture_output=True, text=True
            )

            if process_result.returncode == 0:
                result.success = True
                result.output_path = output_path
                result.file_size_after = output_path.stat().st_size

                # Output is flat video (no spherical metadata)
                output_metadata = SphericalMetadata(
                    is_spherical=False,
                    projection=ProjectionType.FLAT,
                )
                result.output_metadata = output_metadata

                logger.info(
                    f"Viewport extraction successful: yaw={viewport_config.yaw}, pitch={viewport_config.pitch}"
                )

            else:
                result.add_error(f"FFmpeg failed: {process_result.stderr}")

        except Exception as e:
            result.add_error(f"Viewport extraction error: {e}")

        result.processing_time = time.time() - start_time
        return result

    async def extract_animated_viewport(
        self,
        input_path: Path,
        output_path: Path,
        viewport_function: Callable[[float], tuple],
    ) -> Video360ProcessingResult:
        """
        Extract animated viewport with camera movement.

        Args:
            input_path: Source 360° video
            output_path: Output flat video
            viewport_function: Function that takes time (seconds) and returns
                             (yaw, pitch, roll, fov) tuple

        Returns:
            Video360ProcessingResult with extraction details
        """
        start_time = time.time()
        result = Video360ProcessingResult(operation="animated_viewport_extraction")

        try:
            # Get video duration first
            duration = await self._get_video_duration(input_path)

            # Sample viewport function to create expression
            sample_times = [0, duration / 4, duration / 2, 3 * duration / 4, duration]
            sample_viewports = [viewport_function(t) for t in sample_times]

            # For now, use a simplified linear interpolation
            # In a full implementation, this would generate complex FFmpeg expressions
            start_yaw, start_pitch, start_roll, start_fov = sample_viewports[0]
            end_yaw, end_pitch, end_roll, end_fov = sample_viewports[-1]

            # Create animated v360 filter
            v360_filter = (
                f"v360=e:flat:"
                f"yaw='({start_yaw})+({end_yaw}-{start_yaw})*t/{duration}':"
                f"pitch='({start_pitch})+({end_pitch}-{start_pitch})*t/{duration}':"
                f"roll='({start_roll})+({end_roll}-{start_roll})*t/{duration}':"
                f"fov='({start_fov})+({end_fov}-{start_fov})*t/{duration}':"
                f"w=1920:h=1080"
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
                "copy",
                str(output_path),
                "-y",
            ]

            # Execute extraction
            process_result = await asyncio.to_thread(
                subprocess.run, cmd, capture_output=True, text=True
            )

            if process_result.returncode == 0:
                result.success = True
                result.output_path = output_path
                result.file_size_after = output_path.stat().st_size

                logger.info("Animated viewport extraction successful")
            else:
                result.add_error(f"FFmpeg failed: {process_result.stderr}")

        except Exception as e:
            result.add_error(f"Animated viewport extraction error: {e}")

        result.processing_time = time.time() - start_time
        return result

    async def _get_video_duration(self, video_path: Path) -> float:
        """Get video duration in seconds using ffprobe."""
        cmd = [
            self.config.ffmpeg_path.replace("ffmpeg", "ffprobe"),
            "-v", "quiet",
            "-print_format", "json",
            "-show_format",
            str(video_path),
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            import json
            metadata = json.loads(result.stdout)
            duration_str = metadata["format"]["duration"]
            return float(duration_str)
        except (subprocess.CalledProcessError, KeyError, ValueError) as e:
            logger.warning(f"Could not determine video duration: {e}")
            return 60.0  # Default fallback
