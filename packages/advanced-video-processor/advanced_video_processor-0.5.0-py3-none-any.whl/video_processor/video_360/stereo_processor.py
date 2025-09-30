"""360° video stereoscopic processing operations."""

import asyncio
import logging
import shutil
import subprocess
import time
from pathlib import Path

from ..config import ProcessorConfig
from ..exceptions import VideoProcessorError
from .metadata_detector import MetadataDetector
from .models import StereoMode, Video360ProcessingResult

logger = logging.getLogger(__name__)


class StereoProcessor:
    """Handles stereoscopic processing for 360° videos."""

    def __init__(self, config: ProcessorConfig):
        self.config = config
        self.metadata_detector = MetadataDetector(config)

    async def stereo_to_mono(
        self, input_path: Path, output_path: Path, eye: str = "left"
    ) -> Video360ProcessingResult:
        """
        Convert stereoscopic 360° video to monoscopic.

        Args:
            input_path: Source stereoscopic video
            output_path: Output monoscopic video
            eye: Which eye to extract ("left" or "right")

        Returns:
            Video360ProcessingResult with conversion details
        """
        start_time = time.time()
        result = Video360ProcessingResult(operation=f"stereo_to_mono_{eye}")

        try:
            # Extract metadata to determine stereo mode
            source_metadata = await self.metadata_detector.extract_spherical_metadata(input_path)
            source_stereo_mode = source_metadata.stereo_mode

            if source_stereo_mode == StereoMode.MONO:
                result.add_warning("Source video is already monoscopic")
                # Copy file instead of processing
                shutil.copy2(input_path, output_path)
                result.success = True
                result.output_path = output_path
                return result

            # Build crop filter based on stereo mode
            if source_stereo_mode == StereoMode.TOP_BOTTOM:
                if eye == "left":
                    crop_filter = "crop=iw:ih/2:0:0"  # Top half
                else:
                    crop_filter = "crop=iw:ih/2:0:ih/2"  # Bottom half
            elif source_stereo_mode == StereoMode.LEFT_RIGHT:
                if eye == "left":
                    crop_filter = "crop=iw/2:ih:0:0"  # Left half
                else:
                    crop_filter = "crop=iw/2:ih:iw/2:0"  # Right half
            else:
                raise VideoProcessorError(
                    f"Unsupported stereo mode: {source_stereo_mode}"
                )

            # Scale back to original resolution
            if source_stereo_mode == StereoMode.TOP_BOTTOM:
                scale_filter = "scale=iw:ih*2"
            else:  # LEFT_RIGHT
                scale_filter = "scale=iw*2:ih"

            # Combine filters
            video_filter = f"{crop_filter},{scale_filter}"

            # Get file sizes
            result.file_size_before = input_path.stat().st_size

            # Build FFmpeg command
            cmd = [
                self.config.ffmpeg_path,
                "-i",
                str(input_path),
                "-vf",
                video_filter,
                "-c:v",
                "libx264",
                "-preset",
                "medium",
                "-crf",
                "23",
                "-c:a",
                "copy",
                "-metadata",
                "spherical=1",
                "-metadata",
                "stereo_mode=mono",
                str(output_path),
                "-y",
            ]

            # Execute conversion
            process_result = await asyncio.to_thread(
                subprocess.run, cmd, capture_output=True, text=True
            )

            if process_result.returncode == 0:
                result.success = True
                result.output_path = output_path
                result.file_size_after = output_path.stat().st_size

                logger.info(
                    f"Stereo to mono conversion successful: {eye} eye extracted"
                )

            else:
                result.add_error(f"FFmpeg failed: {process_result.stderr}")

        except Exception as e:
            result.add_error(f"Stereo to mono conversion error: {e}")

        result.processing_time = time.time() - start_time
        return result

    async def convert_stereo_mode(
        self, input_path: Path, output_path: Path, target_mode: StereoMode
    ) -> Video360ProcessingResult:
        """
        Convert between stereoscopic modes (e.g., top-bottom to side-by-side).

        Args:
            input_path: Source stereoscopic video
            output_path: Output video with new stereo mode
            target_mode: Target stereoscopic mode

        Returns:
            Video360ProcessingResult with conversion details
        """
        start_time = time.time()
        result = Video360ProcessingResult(
            operation=f"stereo_mode_conversion_to_{target_mode.value}"
        )

        try:
            # Extract metadata to determine stereo mode
            source_metadata = await self.metadata_detector.extract_spherical_metadata(input_path)
            source_stereo_mode = source_metadata.stereo_mode

            if not self._is_stereoscopic(source_stereo_mode):
                raise VideoProcessorError("Source video is not stereoscopic")

            if source_stereo_mode == target_mode:
                result.add_warning("Source already in target stereo mode")
                shutil.copy2(input_path, output_path)
                result.success = True
                result.output_path = output_path
                return result

            # Build conversion filter
            conversion_filter = self._build_stereo_conversion_filter(
                source_stereo_mode, target_mode
            )

            # Get file sizes
            result.file_size_before = input_path.stat().st_size

            # Build FFmpeg command
            cmd = [
                self.config.ffmpeg_path,
                "-i",
                str(input_path),
                "-vf",
                conversion_filter,
                "-c:v",
                "libx264",
                "-preset",
                "medium",
                "-crf",
                "23",
                "-c:a",
                "copy",
                "-metadata",
                "spherical=1",
                "-metadata",
                f"stereo_mode={target_mode.value}",
                str(output_path),
                "-y",
            ]

            # Execute conversion
            process_result = await asyncio.to_thread(
                subprocess.run, cmd, capture_output=True, text=True
            )

            if process_result.returncode == 0:
                result.success = True
                result.output_path = output_path
                result.file_size_after = output_path.stat().st_size

                logger.info(
                    f"Stereo mode conversion successful: {source_stereo_mode.value} -> {target_mode.value}"
                )

            else:
                result.add_error(f"FFmpeg failed: {process_result.stderr}")

        except Exception as e:
            result.add_error(f"Stereo mode conversion error: {e}")

        result.processing_time = time.time() - start_time
        return result

    def _build_stereo_conversion_filter(
        self, source_mode: StereoMode, target_mode: StereoMode
    ) -> str:
        """Build FFmpeg filter for stereo mode conversion."""
        if (
            source_mode == StereoMode.TOP_BOTTOM
            and target_mode == StereoMode.LEFT_RIGHT
        ):
            # TB to SBS: split top/bottom, place side by side
            return (
                "[0:v]crop=iw:ih/2:0:0[left];"
                "[0:v]crop=iw:ih/2:0:ih/2[right];"
                "[left][right]hstack"
            )
        elif (
            source_mode == StereoMode.LEFT_RIGHT
            and target_mode == StereoMode.TOP_BOTTOM
        ):
            # SBS to TB: split left/right, stack vertically
            return (
                "[0:v]crop=iw/2:ih:0:0[left];"
                "[0:v]crop=iw/2:ih:iw/2:0[right];"
                "[left][right]vstack"
            )
        else:
            raise VideoProcessorError(
                f"Unsupported stereo conversion: {source_mode} -> {target_mode}"
            )

    def _is_stereoscopic(self, stereo_mode: StereoMode) -> bool:
        """Check if the stereo mode represents stereoscopic content."""
        return stereo_mode in [StereoMode.TOP_BOTTOM, StereoMode.LEFT_RIGHT]
