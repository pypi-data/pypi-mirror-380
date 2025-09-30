"""Spatial audio processing orchestrator for 360° videos."""

import logging
from pathlib import Path
from typing import Any

from .audio_converter import AudioConverter
from .audio_detector import AudioDetector
from .audio_rotator import AudioRotator
from .models import SpatialAudioType

logger = logging.getLogger(__name__)


class SpatialAudioProcessor:
    """
    Orchestrates spatial audio processing for 360° videos.

    Coordinates audio detection, rotation, and format conversion
    through specialized audio processing classes.
    """

    def __init__(self):
        # Initialize specialized processors
        self.audio_detector = AudioDetector()
        self.audio_rotator = AudioRotator()
        self.audio_converter = AudioConverter()

        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.logger.info("SpatialAudioProcessor initialized with specialized components")

    async def detect_spatial_audio(self, video_path: Path) -> SpatialAudioType:
        """Detect spatial audio format in video file."""
        return await self.audio_detector.detect_spatial_audio(video_path)

    async def rotate_spatial_audio(
        self,
        input_path: Path,
        output_path: Path,
        yaw: float = 0,
        pitch: float = 0,
        roll: float = 0,
        audio_format: SpatialAudioType = SpatialAudioType.AMBISONIC_BFORMAT,
    ) -> bool:
        """Rotate spatial audio to match video orientation."""
        return await self.audio_rotator.rotate_spatial_audio(
            input_path, output_path, yaw, pitch, roll, audio_format
        )

    async def convert_to_binaural(
        self,
        input_path: Path,
        output_path: Path,
        source_format: SpatialAudioType,
        head_rotation: tuple[float, float, float] = (0, 0, 0),
    ) -> bool:
        """Convert spatial audio to binaural format for headphone playback."""
        return await self.audio_converter.convert_to_binaural(
            input_path, output_path, source_format, head_rotation
        )

    async def extract_ambisonic_channels(
        self,
        input_path: Path,
        output_dir: Path,
        format_type: SpatialAudioType = SpatialAudioType.AMBISONIC_BFORMAT,
    ) -> list[Path]:
        """Extract individual channels from ambisonic audio."""
        return await self.audio_converter.extract_ambisonic_channels(
            input_path, output_dir, format_type
        )

    async def create_ambisonic_from_channels(
        self,
        channel_paths: list[Path],
        output_path: Path,
        format_type: SpatialAudioType = SpatialAudioType.AMBISONIC_BFORMAT,
    ) -> bool:
        """Create ambisonic audio from individual channel files."""
        return await self.audio_converter.create_ambisonic_from_channels(
            channel_paths, output_path, format_type
        )

    async def apply_head_tracking(
        self,
        input_path: Path,
        output_path: Path,
        tracking_data: list[dict],
        audio_format: SpatialAudioType,
    ) -> bool:
        """Apply head tracking data to spatial audio for dynamic positioning."""
        return await self.audio_rotator.apply_head_tracking(
            input_path, output_path, tracking_data, audio_format
        )

    def get_audio_characteristics(self, video_path: Path) -> dict[str, Any]:
        """Get detailed audio stream characteristics."""
        return self.audio_detector.get_audio_characteristics(video_path)

    def get_supported_formats(self) -> list[SpatialAudioType]:
        """Get list of supported spatial audio formats."""
        return [
            SpatialAudioType.AMBISONIC_BFORMAT,
            SpatialAudioType.AMBISONIC_HOA,
            SpatialAudioType.OBJECT_BASED,
            SpatialAudioType.BINAURAL,
            SpatialAudioType.HEAD_LOCKED,
        ]

    def get_format_info(self, audio_type: SpatialAudioType) -> dict[str, Any]:
        """Get information about a specific spatial audio format."""
        format_info = {
            SpatialAudioType.NONE: {
                "name": "No Spatial Audio",
                "channels": 2,
                "description": "Standard stereo audio without spatial information",
                "use_cases": ["Regular video content", "Music"],
            },
            SpatialAudioType.AMBISONIC_BFORMAT: {
                "name": "Ambisonic B-Format",
                "channels": 4,
                "description": "First-order ambisonic format with W, X, Y, Z channels",
                "use_cases": ["360° video", "VR content", "Live recordings"],
            },
            SpatialAudioType.AMBISONIC_HOA: {
                "name": "Higher Order Ambisonics",
                "channels": 16,  # Typical 3rd order
                "description": "Higher-order ambisonic format for improved spatial resolution",
                "use_cases": ["High-end VR", "Professional 360° production"],
            },
            SpatialAudioType.OBJECT_BASED: {
                "name": "Object-Based Audio",
                "channels": "Variable",
                "description": "Audio objects with position metadata (e.g., Dolby Atmos)",
                "use_cases": ["Cinema", "Interactive media", "Gaming"],
            },
            SpatialAudioType.BINAURAL: {
                "name": "Binaural Audio",
                "channels": 2,
                "description": "Stereo audio optimized for headphone playback with spatial cues",
                "use_cases": ["Headphone listening", "Mobile VR", "Podcasts"],
            },
            SpatialAudioType.HEAD_LOCKED: {
                "name": "Head-Locked Audio",
                "channels": 2,
                "description": "Audio that follows head movement in VR/AR",
                "use_cases": ["VR UI sounds", "Narration", "Interface audio"],
            },
        }

        return format_info.get(audio_type, {})

    def get_supported_conversions(self) -> dict[SpatialAudioType, list[SpatialAudioType]]:
        """Get supported audio format conversions."""
        return self.audio_converter.get_supported_conversions()

    def can_process_format(self, audio_type: SpatialAudioType) -> bool:
        """Check if a specific audio format can be processed."""
        supported = self.get_supported_formats()
        return audio_type in supported
