"""360° video stream processing and rendition generation."""

import asyncio
import logging
import subprocess
from pathlib import Path
from typing import Any

from ..config import ProcessorConfig
from ..constants import ENCODING
from .models import BitrateLevel360

logger = logging.getLogger(__name__)


class StreamProcessor:
    """Handles 360° video stream processing and rendition generation."""

    def __init__(self, config: ProcessorConfig):
        self.config = config
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    async def generate_360_renditions(
        self,
        video_path: Path,
        bitrate_levels: list[BitrateLevel360],
        output_dir: Path,
        base_filename: str,
    ) -> list[Path]:
        """Generate video renditions for different bitrate levels."""
        try:
            tasks = []

            for level in bitrate_levels:
                task = self._create_rendition(
                    video_path, level, output_dir, base_filename
                )
                tasks.append(task)

            # Process renditions in parallel
            rendition_paths = await asyncio.gather(*tasks, return_exceptions=True)

            # Filter out exceptions and return successful renditions
            successful_paths = [
                path for path in rendition_paths
                if isinstance(path, Path)
            ]

            self.logger.info(f"Generated {len(successful_paths)} renditions")
            return successful_paths

        except Exception as e:
            self.logger.error(f"Failed to generate renditions: {e}")
            raise

    async def _create_rendition(
        self,
        video_path: Path,
        level: BitrateLevel360,
        output_dir: Path,
        base_filename: str,
    ) -> Path:
        """Create a single video rendition."""
        output_path = output_dir / f"{base_filename}_{level.quality}.mp4"

        # Build FFmpeg command for 360° video
        cmd = [
            self.config.ffmpeg_path,
            "-i", str(video_path),
            "-c:v", self._get_encoder_for_codec("h264"),
            "-b:v", str(level.bitrate),
            "-maxrate", str(int(level.bitrate * ENCODING["bitrate_control"]["maxrate_multiplier"])),
            "-bufsize", str(int(level.bitrate * ENCODING["bitrate_control"]["bufsize_multiplier"])),
            "-vf", f"scale={level.resolution[0]}:{level.resolution[1]}",
            "-r", str(level.fps),
            "-preset", "medium",
            "-c:a", "aac",
            "-b:a", "128k",
        ]

        # Add 360° metadata
        cmd.extend([
            "-metadata", "spherical=1",
            "-metadata", f"projection={level.projection.value}",
        ])

        # Add tiling if enabled
        if level.tiling_enabled:
            cmd.extend(["-tiles", "6x4"])

        cmd.extend([str(output_path), "-y"])

        # Execute FFmpeg
        result = await asyncio.to_thread(
            subprocess.run, cmd, capture_output=True, text=True
        )

        if result.returncode != 0:
            raise RuntimeError(f"FFmpeg failed for {level.quality}: {result.stderr}")

        self.logger.info(f"Created rendition: {output_path}")
        return output_path

    def _get_encoder_for_codec(self, codec: str) -> str:
        """Get appropriate encoder for codec."""
        encoders = {
            "h264": "libx264",
            "h265": "libx265",
            "hevc": "libx265",
            "vp9": "libvpx-vp9",
            "av1": "libaom-av1",
        }
        return encoders.get(codec, "libx264")

    async def generate_viewport_streams(
        self,
        video_path: Path,
        viewports: list[dict[str, Any]],
        output_dir: Path,
        base_filename: str,
    ) -> list[dict[str, Any]]:
        """Generate viewport-specific streams for adaptive viewing."""
        try:
            viewport_streams = []

            for i, viewport in enumerate(viewports):
                stream_info = await self._create_viewport_stream(
                    video_path, viewport, output_dir, f"{base_filename}_viewport_{i}"
                )
                viewport_streams.append(stream_info)

            self.logger.info(f"Generated {len(viewport_streams)} viewport streams")
            return viewport_streams

        except Exception as e:
            self.logger.error(f"Failed to generate viewport streams: {e}")
            raise

    async def _create_viewport_stream(
        self,
        video_path: Path,
        viewport: dict[str, Any],
        output_dir: Path,
        filename: str,
    ) -> dict[str, Any]:
        """Create a single viewport stream."""
        output_path = output_dir / f"{filename}.mp4"

        # Build viewport extraction command
        cmd = [
            self.config.ffmpeg_path,
            "-i", str(video_path),
            "-vf", f"v360=e:flat:"
                  f"yaw={viewport['yaw']}:"
                  f"pitch={viewport['pitch']}:"
                  f"fov={viewport['fov']}:"
                  f"w={viewport.get('width', 1920)}:"
                  f"h={viewport.get('height', 1080)}",
            "-c:v", "libx264",
            "-preset", "medium",
            "-crf", "23",
            "-c:a", "copy",
            str(output_path),
            "-y",
        ]

        result = await asyncio.to_thread(
            subprocess.run, cmd, capture_output=True, text=True
        )

        if result.returncode != 0:
            raise RuntimeError(f"Viewport stream creation failed: {result.stderr}")

        return {
            "filename": filename,
            "path": output_path,
            "viewport": f"yaw={viewport['yaw']},pitch={viewport['pitch']},fov={viewport['fov']}",
            "width": viewport.get('width', 1920),
            "height": viewport.get('height', 1080),
            "bitrate": viewport.get('bitrate', 2000000),
        }
