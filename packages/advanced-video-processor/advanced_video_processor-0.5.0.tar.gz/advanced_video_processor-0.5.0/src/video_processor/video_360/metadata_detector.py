"""360° video metadata detection and parsing."""

import json
import logging
import subprocess
from pathlib import Path

from ..config import ProcessorConfig
from ..exceptions import VideoProcessorError
from .models import ProjectionType, SphericalMetadata, StereoMode

logger = logging.getLogger(__name__)


class MetadataDetector:
    """Detects and extracts 360° metadata from video files."""

    def __init__(self, config: ProcessorConfig):
        self.config = config

    async def extract_spherical_metadata(self, video_path: Path) -> SphericalMetadata:
        """
        Extract spherical metadata from video file.

        Analyzes video metadata to determine if it's a 360° video and extract
        projection information, stereoscopic mode, and other spatial properties.
        """
        try:
            # Use ffprobe to extract metadata
            cmd = [
                self.config.ffmpeg_path.replace("ffmpeg", "ffprobe"),
                "-v", "quiet",
                "-print_format", "json",
                "-show_format",
                "-show_streams",
                str(video_path),
            ]

            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            metadata = json.loads(result.stdout)

            return self._parse_spherical_tags(metadata, video_path)

        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to extract metadata from {video_path}: {e}")
            raise VideoProcessorError(f"Metadata extraction failed: {e}") from e
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse metadata JSON: {e}")
            raise VideoProcessorError(f"Invalid metadata format: {e}") from e

    def _parse_spherical_tags(
        self, metadata: dict, video_path: Path
    ) -> SphericalMetadata:
        """Parse spherical metadata from ffprobe output."""
        # Initialize with defaults
        is_360 = False
        projection = ProjectionType.EQUIRECTANGULAR
        stereo_mode = StereoMode.MONO

        # Look for spherical metadata in format tags
        format_tags = metadata.get("format", {}).get("tags", {})

        # Check for Google spherical metadata
        spherical_xml = format_tags.get("spherical-video") or format_tags.get("Spherical Video")
        if spherical_xml:
            is_360 = True
            # Parse XML for detailed parameters (simplified for now)
            if "equirectangular" in spherical_xml.lower():
                projection = ProjectionType.EQUIRECTANGULAR
            elif "cubemap" in spherical_xml.lower():
                projection = ProjectionType.CUBEMAP

        # Check for Samsung 360 metadata
        if format_tags.get("com.samsung.android.spherical"):
            is_360 = True

        # Check video streams for additional metadata
        for stream in metadata.get("streams", []):
            if stream.get("codec_type") == "video":
                stream_tags = stream.get("tags", {})

                # Check for projection metadata
                proj_mode = stream_tags.get("spherical_video_projection")
                if proj_mode:
                    is_360 = True
                    if proj_mode.lower() == "equirectangular":
                        projection = ProjectionType.EQUIRECTANGULAR
                    elif proj_mode.lower() == "cubemap":
                        projection = ProjectionType.CUBEMAP

                # Check for stereo mode
                stereo_tag = stream_tags.get("stereo_mode") or stream_tags.get("StereoMode")
                if stereo_tag:
                    if "top_bottom" in stereo_tag.lower():
                        stereo_mode = StereoMode.TOP_BOTTOM
                    elif "left_right" in stereo_tag.lower():
                        stereo_mode = StereoMode.LEFT_RIGHT

                # If no explicit 360 tags, infer from properties
                if not is_360:
                    is_360, projection = self._infer_360_properties(stream)

                break

        return SphericalMetadata(
            is_spherical=is_360,
            projection=projection,
            stereo_mode=stereo_mode,
        )

    def _infer_360_properties(
        self, stream: dict
    ) -> tuple[bool, ProjectionType]:
        """Infer 360° properties from video stream characteristics."""
        width = stream.get("width", 0)
        height = stream.get("height", 0)

        if width == 0 or height == 0:
            return False, ProjectionType.EQUIRECTANGULAR

        aspect_ratio = width / height

        # Equirectangular videos typically have 2:1 aspect ratio
        if 1.9 <= aspect_ratio <= 2.1:
            return True, ProjectionType.EQUIRECTANGULAR

        # Cubemap videos are typically square or 3:2/4:3
        if 0.9 <= aspect_ratio <= 1.5:
            return True, ProjectionType.CUBEMAP

        return False, ProjectionType.EQUIRECTANGULAR
