"""Preview generation utilities for 360° videos."""

import asyncio
import logging
import shutil
import subprocess
import time
from pathlib import Path

from ..config import ProcessorConfig
from .models import ProjectionType, Video360ProcessingResult
from .projection_converter import ProjectionConverter

logger = logging.getLogger(__name__)


class PreviewGenerator:
    """Generates preview content for 360° videos."""

    def __init__(self, config: ProcessorConfig):
        self.config = config
        self.projection_converter = ProjectionConverter(config)
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    async def create_projection_preview_grid(
        self,
        input_path: Path,
        output_path: Path,
        source_projection: ProjectionType = ProjectionType.EQUIRECTANGULAR,
        grid_size: tuple[int, int] = (2, 3),
        preview_duration: float = 10.0,
    ) -> Video360ProcessingResult:
        """
        Create a preview grid showing different projections.

        Args:
            input_path: Source video
            output_path: Output preview video
            source_projection: Source projection type
            grid_size: Grid dimensions (cols, rows)
            preview_duration: Duration of preview in seconds

        Returns:
            Video360ProcessingResult with preview creation details
        """
        start_time = time.time()
        result = Video360ProcessingResult(operation="projection_preview_grid")

        try:
            # Define projections to show in grid
            preview_projections = [
                ProjectionType.EQUIRECTANGULAR,
                ProjectionType.CUBEMAP,
                ProjectionType.STEREOGRAPHIC,
                ProjectionType.FISHEYE,
                ProjectionType.PANNINI,
                ProjectionType.MERCATOR,
            ]

            cols, rows = grid_size
            max_projections = cols * rows
            preview_projections = preview_projections[:max_projections]

            # Create temporary files for each projection
            temp_dir = output_path.parent / "temp_projections"
            temp_dir.mkdir(exist_ok=True)

            temp_files = []

            # Convert to each projection
            for i, proj in enumerate(preview_projections):
                temp_file = temp_dir / f"proj_{i}_{proj.value}.mp4"

                if proj == source_projection:
                    # Copy original
                    shutil.copy2(input_path, temp_file)
                else:
                    # Convert projection
                    conversion_result = await self.projection_converter.convert_projection(
                        input_path, temp_file, proj
                    )

                    if not conversion_result.success:
                        self.logger.warning(f"Failed to convert to {proj.value} for preview")
                        continue

                temp_files.append(temp_file)

            # Create grid layout using FFmpeg
            if len(temp_files) >= 4:  # Minimum for 2x2 grid
                filter_complex = self._build_grid_filter(temp_files, cols, rows)

                cmd = [self.config.ffmpeg_path]

                # Add all input files
                for temp_file in temp_files:
                    cmd.extend(["-i", str(temp_file)])

                cmd.extend(
                    [
                        "-filter_complex",
                        filter_complex,
                        "-c:v",
                        "libx264",
                        "-preset",
                        "medium",
                        "-crf",
                        "25",
                        "-t",
                        str(preview_duration),
                        str(output_path),
                        "-y",
                    ]
                )

                process_result = await asyncio.to_thread(
                    subprocess.run, cmd, capture_output=True, text=True
                )

                if process_result.returncode == 0:
                    result.success = True
                    result.output_path = output_path
                    result.file_size_after = output_path.stat().st_size
                    self.logger.info("Projection preview grid created successfully")
                else:
                    result.add_error(f"Grid creation failed: {process_result.stderr}")
            else:
                result.add_error("Insufficient projections for grid")

            # Cleanup temp files
            shutil.rmtree(temp_dir, ignore_errors=True)

        except Exception as e:
            result.add_error(f"Preview grid creation error: {e}")
            self.logger.error(f"Preview grid error: {e}")

        result.processing_time = time.time() - start_time
        return result

    def _build_grid_filter(self, input_files: list[Path], cols: int, rows: int) -> str:
        """Build FFmpeg filter for grid layout."""
        # Simple 2x2 grid filter (can be extended for other sizes)
        if cols == 2 and rows == 2 and len(input_files) >= 4:
            return (
                "[0:v]scale=iw/2:ih/2[v0];"
                "[1:v]scale=iw/2:ih/2[v1];"
                "[2:v]scale=iw/2:ih/2[v2];"
                "[3:v]scale=iw/2:ih/2[v3];"
                "[v0][v1]hstack[top];"
                "[v2][v3]hstack[bottom];"
                "[top][bottom]vstack[out]"
            )
        elif cols == 3 and rows == 2 and len(input_files) >= 6:
            return (
                "[0:v]scale=iw/3:ih/2[v0];"
                "[1:v]scale=iw/3:ih/2[v1];"
                "[2:v]scale=iw/3:ih/2[v2];"
                "[3:v]scale=iw/3:ih/2[v3];"
                "[4:v]scale=iw/3:ih/2[v4];"
                "[5:v]scale=iw/3:ih/2[v5];"
                "[v0][v1][v2]hstack=inputs=3[top];"
                "[v3][v4][v5]hstack=inputs=3[bottom];"
                "[top][bottom]vstack[out]"
            )
        else:
            # Fallback to simple 2x2
            return (
                "[0:v]scale=iw/2:ih/2[v0];[1:v]scale=iw/2:ih/2[v1];[v0][v1]hstack[out]"
            )

    async def create_viewport_sample_grid(
        self,
        input_path: Path,
        output_path: Path,
        viewport_configs: list[dict],
        grid_size: tuple[int, int] = (2, 2),
    ) -> Video360ProcessingResult:
        """
        Create a grid showing different viewport extractions.

        Args:
            input_path: Source 360° video
            output_path: Output preview video
            viewport_configs: List of viewport configurations
            grid_size: Grid dimensions (cols, rows)

        Returns:
            Video360ProcessingResult with viewport grid details
        """
        start_time = time.time()
        result = Video360ProcessingResult(operation="viewport_sample_grid")

        try:
            cols, rows = grid_size
            max_viewports = cols * rows
            viewport_configs = viewport_configs[:max_viewports]

            # Create temporary files for each viewport
            temp_dir = output_path.parent / "temp_viewports"
            temp_dir.mkdir(exist_ok=True)

            temp_files = []

            # Extract each viewport
            for i, viewport_config in enumerate(viewport_configs):
                temp_file = temp_dir / f"viewport_{i}.mp4"

                # Build viewport extraction command
                yaw = viewport_config.get("yaw", 0)
                pitch = viewport_config.get("pitch", 0)
                fov = viewport_config.get("fov", 90)

                v360_filter = f"v360=e:flat:yaw={yaw}:pitch={pitch}:fov={fov}:w=1280:h=720"

                cmd = [
                    self.config.ffmpeg_path,
                    "-i",
                    str(input_path),
                    "-vf",
                    v360_filter,
                    "-c:v",
                    "libx264",
                    "-preset",
                    "fast",
                    "-crf",
                    "26",
                    "-t",
                    "5",  # Short clip
                    str(temp_file),
                    "-y",
                ]

                process_result = await asyncio.to_thread(
                    subprocess.run, cmd, capture_output=True, text=True
                )

                if process_result.returncode == 0:
                    temp_files.append(temp_file)
                else:
                    self.logger.warning(f"Failed to extract viewport {i}: {process_result.stderr}")

            # Create grid layout
            if len(temp_files) >= 2:
                filter_complex = self._build_grid_filter(temp_files, cols, rows)

                cmd = [self.config.ffmpeg_path]

                # Add all input files
                for temp_file in temp_files:
                    cmd.extend(["-i", str(temp_file)])

                cmd.extend(
                    [
                        "-filter_complex",
                        filter_complex,
                        "-c:v",
                        "libx264",
                        "-preset",
                        "medium",
                        "-crf",
                        "25",
                        str(output_path),
                        "-y",
                    ]
                )

                process_result = await asyncio.to_thread(
                    subprocess.run, cmd, capture_output=True, text=True
                )

                if process_result.returncode == 0:
                    result.success = True
                    result.output_path = output_path
                    result.file_size_after = output_path.stat().st_size
                    self.logger.info("Viewport sample grid created successfully")
                else:
                    result.add_error(f"Viewport grid creation failed: {process_result.stderr}")
            else:
                result.add_error("Insufficient viewports for grid")

            # Cleanup temp files
            shutil.rmtree(temp_dir, ignore_errors=True)

        except Exception as e:
            result.add_error(f"Viewport grid creation error: {e}")
            self.logger.error(f"Viewport grid error: {e}")

        result.processing_time = time.time() - start_time
        return result

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
        start_time = time.time()
        result = Video360ProcessingResult(operation="motion_preview")

        try:
            # Create animated viewport extraction with smooth camera movement
            # Rotate 360 degrees horizontally over the duration
            v360_filter = (
                f"v360=e:flat:"
                f"yaw='360*t/{duration}':"
                f"pitch='30*sin(2*PI*t/{duration})':"
                f"fov=90:"
                f"w=1920:h=1080"
            )

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
                "-t",
                str(duration),
                str(output_path),
                "-y",
            ]

            process_result = await asyncio.to_thread(
                subprocess.run, cmd, capture_output=True, text=True
            )

            if process_result.returncode == 0:
                result.success = True
                result.output_path = output_path
                result.file_size_after = output_path.stat().st_size
                self.logger.info("Motion preview created successfully")
            else:
                result.add_error(f"Motion preview creation failed: {process_result.stderr}")

        except Exception as e:
            result.add_error(f"Motion preview creation error: {e}")
            self.logger.error(f"Motion preview error: {e}")

        result.processing_time = time.time() - start_time
        return result
