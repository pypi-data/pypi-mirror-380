"""Spatial audio format detection and analysis."""

import asyncio
import json
import logging
import subprocess
from pathlib import Path
from typing import Any

from .models import SpatialAudioType

logger = logging.getLogger(__name__)


class AudioDetector:
    """Detects and analyzes spatial audio formats in 360° video content."""

    def __init__(self):
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    async def detect_spatial_audio(self, video_path: Path) -> SpatialAudioType:
        """
        Detect spatial audio format in video file.

        Analyzes audio streams to identify ambisonic, object-based, binaural,
        or other spatial audio formats.
        """
        try:
            # Use ffprobe to analyze audio streams
            cmd = [
                "ffprobe",
                "-v", "quiet",
                "-print_format", "json",
                "-show_streams",
                "-select_streams", "a",
                str(video_path),
            ]

            result = await asyncio.to_thread(
                subprocess.run, cmd, capture_output=True, text=True
            )

            if result.returncode != 0:
                self.logger.warning(f"ffprobe failed: {result.stderr}")
                return SpatialAudioType.NONE

            probe_data = json.loads(result.stdout)
            audio_streams = probe_data.get("streams", [])

            if not audio_streams:
                return SpatialAudioType.NONE

            # Analyze each audio stream
            for stream in audio_streams:
                spatial_type = self._analyze_audio_stream(stream)
                if spatial_type != SpatialAudioType.NONE:
                    return spatial_type

            return SpatialAudioType.NONE

        except Exception as e:
            self.logger.error(f"Spatial audio detection failed: {e}")
            return SpatialAudioType.NONE

    def _analyze_audio_stream(self, stream: dict[str, Any]) -> SpatialAudioType:
        """Analyze individual audio stream for spatial characteristics."""
        channels = stream.get("channels", 0)
        channel_layout = stream.get("channel_layout", "")
        tags = stream.get("tags", {})

        # Check for ambisonic audio
        if self._has_ambisonic_metadata(tags):
            if channels == 4:
                return SpatialAudioType.AMBISONIC_BFORMAT
            elif channels > 4:
                return SpatialAudioType.AMBISONIC_HOA
            else:
                return SpatialAudioType.AMBISONIC_BFORMAT

        # Check for object-based audio
        if self._has_object_audio_metadata(tags):
            return SpatialAudioType.OBJECT_BASED

        # Check for binaural audio
        if self._has_binaural_metadata(tags):
            return SpatialAudioType.BINAURAL

        # Infer from channel count and layout
        if channels >= 4:
            # 4+ channels could be ambisonic B-format
            if "quad" in channel_layout.lower():
                return SpatialAudioType.AMBISONIC_BFORMAT
            elif channels >= 16:
                # 16+ channels likely higher-order ambisonics
                return SpatialAudioType.AMBISONIC_HOA
            elif channels > 8:
                # Many channels suggest object-based
                return SpatialAudioType.OBJECT_BASED

        return SpatialAudioType.NONE

    def _has_ambisonic_metadata(self, tags: dict[str, str]) -> bool:
        """Check for ambisonic audio metadata indicators."""
        ambisonic_indicators = [
            "ambisonic", "ambisonics", "b-format", "bformat",
            "spherical_audio", "360_audio"
        ]

        # Check tag values
        for tag_value in tags.values():
            if isinstance(tag_value, str):
                tag_lower = tag_value.lower()
                if any(indicator in tag_lower for indicator in ambisonic_indicators):
                    return True

        # Check specific ambisonic tags
        ambisonic_tags = [
            "ambisonic_type", "ambisonic_order", "ambisonics",
            "spherical-audio", "google_spherical_audio"
        ]

        return any(tag in tags for tag in ambisonic_tags)

    def _has_object_audio_metadata(self, tags: dict[str, str]) -> bool:
        """Check for object-based audio metadata."""
        object_indicators = [
            "object_audio", "objects", "dolby_atmos", "atmos",
            "object_based", "spatial_objects"
        ]

        # Check tag values
        for tag_value in tags.values():
            if isinstance(tag_value, str):
                tag_lower = tag_value.lower()
                if any(indicator in tag_lower for indicator in object_indicators):
                    return True

        # Check specific object audio tags
        object_tags = [
            "objects", "audio_objects", "dolby_atmos", "dts_x"
        ]

        return any(tag in tags for tag in object_tags)

    def _has_binaural_metadata(self, tags: dict[str, str]) -> bool:
        """Check for binaural audio metadata."""
        binaural_indicators = [
            "binaural", "hrtf", "head_related", "3d_audio", "immersive"
        ]

        # Check tag values
        for tag_value in tags.values():
            if isinstance(tag_value, str):
                tag_lower = tag_value.lower()
                if any(indicator in tag_lower for indicator in binaural_indicators):
                    return True

        # Check specific binaural tags
        binaural_tags = [
            "binaural", "hrtf", "head_related_transfer"
        ]

        return any(tag in tags for tag in binaural_tags)

    def get_audio_characteristics(self, video_path: Path) -> dict[str, Any]:
        """Get detailed audio stream characteristics."""
        try:
            cmd = [
                "ffprobe",
                "-v", "quiet",
                "-print_format", "json",
                "-show_streams",
                "-select_streams", "a:0",  # First audio stream
                str(video_path),
            ]

            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode != 0:
                return {}

            probe_data = json.loads(result.stdout)
            streams = probe_data.get("streams", [])

            if not streams:
                return {}

            stream = streams[0]
            return {
                "channels": stream.get("channels", 0),
                "channel_layout": stream.get("channel_layout", ""),
                "sample_rate": int(stream.get("sample_rate", 0)),
                "codec": stream.get("codec_name", ""),
                "bitrate": int(stream.get("bit_rate", 0)) if stream.get("bit_rate") else 0,
                "duration": float(stream.get("duration", 0)),
                "tags": stream.get("tags", {}),
            }

        except Exception as e:
            self.logger.error(f"Failed to get audio characteristics: {e}")
            return {}
