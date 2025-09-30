"""Advanced video encoding orchestrator for next-generation codecs."""

import logging
from pathlib import Path
from typing import Literal

from ..config import ProcessorConfig
from ..exceptions import EncodingError
from .av1_encoder import AV1Encoder
from .codec_capabilities import CodecCapabilities
from .hdr_processor import HDRProcessor
from .hevc_encoder import HEVCEncoder


class AdvancedEncodingOrchestrator:
    """
    Orchestrates advanced video encoding operations using next-generation codecs.

    This class coordinates between specialized encoding classes:
    - AV1Encoder: AV1 codec encoding with optimized settings
    - HEVCEncoder: HEVC/H.265 encoding with hardware acceleration
    - HDRProcessor: HDR video processing and conversion
    - CodecCapabilities: Capability detection and validation
    """

    def __init__(self, config: ProcessorConfig):
        self.config = config
        self.av1_encoder = AV1Encoder(config)
        self.hevc_encoder = HEVCEncoder(config)
        self.hdr_processor = HDRProcessor(config)
        self.capabilities = CodecCapabilities(config)
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    def get_capabilities_report(self) -> str:
        """Get a comprehensive report of available encoding capabilities."""
        return self.capabilities.get_capability_report()

    def encode_av1(
        self,
        input_path: Path,
        output_dir: Path,
        video_id: str,
        container: Literal["mp4", "webm"] = "mp4",
        use_two_pass: bool = True,
        quality_preset: str | None = None,
    ) -> Path:
        """
        Encode video to AV1 using the specialized AV1 encoder.

        Args:
            input_path: Input video file
            output_dir: Output directory
            video_id: Unique video identifier
            container: Output container (mp4 or webm)
            use_two_pass: Whether to use two-pass encoding for better quality
            quality_preset: Override default quality preset

        Returns:
            Path to encoded file
        """
        # Validate requirements
        valid, reason = self.capabilities.validate_encoding_requirements(
            "av1", container, use_hardware=False
        )
        if not valid:
            raise EncodingError(f"AV1 encoding requirements not met: {reason}")

        return self.av1_encoder.encode_av1(
            input_path, output_dir, video_id, container, use_two_pass, quality_preset
        )

    def estimate_av1_encoding_time(
        self,
        input_path: Path,
        quality_preset: str | None = None,
        use_two_pass: bool = True,
    ) -> dict:
        """
        Estimate AV1 encoding time using the specialized AV1 encoder.

        Args:
            input_path: Input video file
            quality_preset: Quality preset to use
            use_two_pass: Whether using two-pass encoding

        Returns:
            Dictionary with time estimates
        """
        return self.av1_encoder.estimate_av1_encoding_time(
            input_path, quality_preset, use_two_pass
        )

    def encode_hevc(
        self,
        input_path: Path,
        output_dir: Path,
        video_id: str,
        use_hardware: bool = False,
        quality_preset: str | None = None,
    ) -> Path:
        """
        Encode video to HEVC/H.265 using the specialized HEVC encoder.

        Args:
            input_path: Input video file
            output_dir: Output directory
            video_id: Unique video identifier
            use_hardware: Whether to attempt hardware acceleration
            quality_preset: Override default quality preset

        Returns:
            Path to encoded file
        """
        # Validate requirements
        valid, reason = self.capabilities.validate_encoding_requirements(
            "hevc", "mp4", use_hardware=use_hardware
        )
        if not valid:
            raise EncodingError(f"HEVC encoding requirements not met: {reason}")

        return self.hevc_encoder.encode_hevc(
            input_path, output_dir, video_id, use_hardware, quality_preset
        )

    def estimate_hevc_encoding_time(
        self,
        input_path: Path,
        use_hardware: bool = False,
        quality_preset: str | None = None,
    ) -> dict:
        """
        Estimate HEVC encoding time using the specialized HEVC encoder.

        Args:
            input_path: Input video file
            use_hardware: Whether using hardware acceleration
            quality_preset: Quality preset to use

        Returns:
            Dictionary with time estimates
        """
        return self.hevc_encoder.estimate_hevc_encoding_time(
            input_path, use_hardware, quality_preset
        )

    def get_av1_bitrate_multiplier(self, quality_preset: str | None = None) -> float:
        """
        Get bitrate multiplier for AV1 encoding.

        AV1 needs significantly less bitrate than H.264 for same quality.
        """
        return self.av1_encoder.get_bitrate_multiplier(quality_preset)

    def encode_hdr_hevc(
        self,
        input_path: Path,
        output_dir: Path,
        video_id: str,
        hdr_standard: Literal["hdr10", "hdr10plus", "dolby_vision"] = "hdr10",
        quality_preset: str = "high",
    ) -> Path:
        """
        Encode HDR video using the specialized HDR processor.

        Args:
            input_path: Input HDR video file
            output_dir: Output directory
            video_id: Unique video identifier
            hdr_standard: HDR standard to use
            quality_preset: Quality preset for encoding

        Returns:
            Path to encoded HDR file
        """
        return self.hdr_processor.encode_hdr_hevc(
            input_path, output_dir, video_id, hdr_standard, quality_preset
        )

    def analyze_hdr_content(self, video_path: Path) -> dict:
        """
        Analyze video for HDR characteristics using the specialized HDR processor.

        Args:
            video_path: Path to video file

        Returns:
            Dictionary with HDR analysis results
        """
        return self.hdr_processor.analyze_hdr_content(video_path)

    def convert_sdr_to_hdr(
        self,
        input_path: Path,
        output_path: Path,
        hdr_standard: str = "hdr10",
    ) -> Path:
        """
        Convert SDR content to HDR using the specialized HDR processor.

        Args:
            input_path: Input SDR video
            output_path: Output HDR video
            hdr_standard: Target HDR standard

        Returns:
            Path to converted HDR file
        """
        return self.hdr_processor.convert_sdr_to_hdr(
            input_path, output_path, hdr_standard
        )

    def get_optimal_encoder_recommendations(self, quality_priority: str = "balanced") -> dict[str, str]:
        """
        Get optimal encoder recommendations based on available capabilities.

        Args:
            quality_priority: "speed", "balanced", or "quality"

        Returns:
            Dictionary with encoder recommendations
        """
        return self.capabilities.get_optimal_encoder_for_quality(quality_priority)

    def validate_encoding_requirements(
        self,
        codec: str,
        container: str,
        use_hardware: bool = False,
    ) -> tuple[bool, str]:
        """
        Validate if encoding requirements can be met.

        Args:
            codec: Target codec (h264, hevc, av1, etc.)
            container: Target container (mp4, webm, etc.)
            use_hardware: Whether hardware acceleration is required

        Returns:
            Tuple of (is_valid, reason_if_invalid)
        """
        return self.capabilities.validate_encoding_requirements(
            codec, container, use_hardware
        )

    @staticmethod
    def get_supported_advanced_codecs() -> dict[str, bool]:
        """Get information about supported advanced codecs."""
        # Deprecated: Use capabilities.detect_all_capabilities() instead
        return {
            "av1": False,  # Will be detected at runtime
            "hevc": False,
            "vp9": True,  # Usually available
            "hardware_hevc": False,
            "hardware_av1": False,
        }

    @staticmethod
    def get_hdr_support() -> dict[str, bool]:
        """Check what HDR capabilities are available."""
        return HDRProcessor.get_hdr_support()


# Legacy class alias for backward compatibility
class AdvancedVideoEncoder(AdvancedEncodingOrchestrator):
    """Legacy alias for AdvancedEncodingOrchestrator with backward compatibility methods."""

    @property
    def _quality_presets(self):
        """Legacy property for quality presets."""
        return {
            "ultrafast": {"crf": 28, "preset": "ultrafast"},
            "fast": {"crf": 23, "preset": "fast"},
            "medium": {"crf": 20, "preset": "medium"},
            "slow": {"crf": 18, "preset": "slow"},
            "veryslow": {"crf": 16, "preset": "veryslow"},
        }

    def _get_advanced_quality_presets(self):
        """Legacy method for getting quality presets."""
        return self._quality_presets

    def _check_av1_support(self):
        """Legacy method for checking AV1 support."""
        return self.capabilities.check_av1_support()


# Legacy class alias for backward compatibility
class HDRProcessor:
    """Legacy HDR processor class - use AdvancedEncodingOrchestrator instead."""

    def __init__(self, config: ProcessorConfig):
        import warnings
        warnings.warn(
            "HDRProcessor class is deprecated. Use AdvancedEncodingOrchestrator instead.",
            DeprecationWarning,
            stacklevel=2
        )
        from .hdr_processor import HDRProcessor as ActualHDRProcessor
        self._processor = ActualHDRProcessor(config)

    def __getattr__(self, name):
        return getattr(self._processor, name)
