"""Video codec capability detection and validation."""

import logging
import subprocess
from typing import Any

from ..config import ProcessorConfig


class CodecCapabilities:
    """Detects and validates available video codec capabilities."""

    def __init__(self, config: ProcessorConfig):
        self.config = config
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self._capabilities_cache: dict[str, Any] = {}

    def detect_all_capabilities(self) -> dict[str, Any]:
        """
        Detect all available codec capabilities.

        Returns:
            Dictionary with capability information
        """
        if self._capabilities_cache:
            return self._capabilities_cache

        capabilities = {
            "advanced_codecs": self._detect_advanced_codecs(),
            "hardware_encoders": self._detect_hardware_encoders(),
            "hdr_support": self._detect_hdr_support(),
            "container_formats": self._detect_container_formats(),
            "ffmpeg_version": self._get_ffmpeg_version(),
        }

        self._capabilities_cache = capabilities
        return capabilities

    def _detect_advanced_codecs(self) -> dict[str, bool]:
        """Detect support for advanced codecs."""
        codecs_to_check = {
            "av1": "libaom-av1",
            "hevc": "libx265",
            "vp9": "libvpx-vp9",
            "vp8": "libvpx",
        }

        capabilities = {}

        try:
            result = subprocess.run(
                [self.config.ffmpeg_path, "-encoders"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                encoders_output = result.stdout
                for codec_name, encoder_name in codecs_to_check.items():
                    capabilities[codec_name] = encoder_name in encoders_output
            else:
                self.logger.warning("Could not detect codec capabilities")
                capabilities = dict.fromkeys(codecs_to_check, False)

        except (subprocess.SubprocessError, FileNotFoundError):
            self.logger.error("FFmpeg not found or not working")
            capabilities = dict.fromkeys(codecs_to_check, False)

        return capabilities

    def _detect_hardware_encoders(self) -> dict[str, bool]:
        """Detect available hardware encoders."""
        hardware_encoders = {
            "hevc_nvenc": "NVIDIA HEVC",
            "hevc_qsv": "Intel HEVC",
            "hevc_amf": "AMD HEVC",
            "h264_nvenc": "NVIDIA H.264",
            "h264_qsv": "Intel H.264",
            "h264_amf": "AMD H.264",
            "av1_nvenc": "NVIDIA AV1",
            "av1_qsv": "Intel AV1",
        }

        capabilities = {}

        try:
            result = subprocess.run(
                [self.config.ffmpeg_path, "-encoders"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                encoders_output = result.stdout
                for encoder_name, description in hardware_encoders.items():
                    is_available = encoder_name in encoders_output

                    # Additional validation: test if encoder actually works
                    if is_available:
                        is_available = self._test_hardware_encoder(encoder_name)

                    capabilities[encoder_name] = is_available
                    if is_available:
                        self.logger.info(f"Hardware encoder available: {description}")
            else:
                capabilities = dict.fromkeys(hardware_encoders, False)

        except (subprocess.SubprocessError, FileNotFoundError):
            capabilities = dict.fromkeys(hardware_encoders, False)

        return capabilities

    def _detect_hdr_support(self) -> dict[str, bool]:
        """Detect HDR processing capabilities."""
        hdr_capabilities = {
            "hdr10_encoding": True,  # Basic HDR10 with x265
            "hdr10_analysis": True,  # ffprobe can analyze HDR metadata
            "tone_mapping": True,    # zscale filter for tone mapping
            "hdr10plus": False,      # Requires special builds
            "dolby_vision": False,   # Requires licensed tools
        }

        # Check for zscale filter (tone mapping)
        try:
            result = subprocess.run(
                [self.config.ffmpeg_path, "-filters"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                filters_output = result.stdout
                hdr_capabilities["tone_mapping"] = "zscale" in filters_output
            else:
                hdr_capabilities["tone_mapping"] = False

        except (subprocess.SubprocessError, FileNotFoundError):
            hdr_capabilities["tone_mapping"] = False

        return hdr_capabilities

    def _detect_container_formats(self) -> dict[str, bool]:
        """Detect supported container formats."""
        containers = ["mp4", "webm", "mkv", "avi", "mov"]
        capabilities = {}

        try:
            result = subprocess.run(
                [self.config.ffmpeg_path, "-formats"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                formats_output = result.stdout
                for container in containers:
                    # Look for muxer support (E flag)
                    capabilities[container] = f" E {container}" in formats_output or f"DE {container}" in formats_output
            else:
                capabilities = dict.fromkeys(containers, False)

        except (subprocess.SubprocessError, FileNotFoundError):
            capabilities = dict.fromkeys(containers, False)

        return capabilities

    def _get_ffmpeg_version(self) -> str:
        """Get FFmpeg version information."""
        try:
            result = subprocess.run(
                [self.config.ffmpeg_path, "-version"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode == 0:
                # Extract version from first line
                first_line = result.stdout.split('\n')[0]
                if 'ffmpeg version' in first_line:
                    return first_line.split('ffmpeg version ')[1].split(' ')[0]

            return "unknown"

        except (subprocess.SubprocessError, FileNotFoundError):
            return "not_found"

    def _test_hardware_encoder(self, encoder: str) -> bool:
        """Test if a hardware encoder actually works."""
        try:
            # Create a minimal test encode
            test_cmd = [
                self.config.ffmpeg_path,
                "-f", "lavfi",
                "-i", "testsrc=duration=1:size=320x240:rate=1",
                "-c:v", encoder,
                "-t", "0.1",
                "-f", "null",
                "-"
            ]

            result = subprocess.run(
                test_cmd,
                capture_output=True,
                text=True,
                timeout=30,
            )

            return result.returncode == 0

        except (subprocess.SubprocessError, subprocess.TimeoutExpired):
            return False

    def get_optimal_encoder_for_quality(self, quality_priority: str = "balanced") -> dict[str, str]:
        """
        Get optimal encoder recommendations based on quality priority.

        Args:
            quality_priority: "speed", "balanced", or "quality"

        Returns:
            Dictionary with encoder recommendations
        """
        capabilities = self.detect_all_capabilities()
        hardware_encoders = capabilities["hardware_encoders"]
        advanced_codecs = capabilities["advanced_codecs"]

        recommendations = {}

        # H.264 recommendations
        if quality_priority == "speed" and hardware_encoders.get("h264_nvenc"):
            recommendations["h264"] = "h264_nvenc"
        elif quality_priority == "speed" and hardware_encoders.get("h264_qsv"):
            recommendations["h264"] = "h264_qsv"
        else:
            recommendations["h264"] = "libx264"

        # HEVC recommendations
        if quality_priority == "speed" and hardware_encoders.get("hevc_nvenc"):
            recommendations["hevc"] = "hevc_nvenc"
        elif quality_priority == "speed" and hardware_encoders.get("hevc_qsv"):
            recommendations["hevc"] = "hevc_qsv"
        elif advanced_codecs.get("hevc"):
            recommendations["hevc"] = "libx265"
        else:
            recommendations["hevc"] = "not_available"

        # AV1 recommendations
        if advanced_codecs.get("av1"):
            if quality_priority == "speed":
                recommendations["av1"] = "libaom-av1_fast"
            else:
                recommendations["av1"] = "libaom-av1"
        else:
            recommendations["av1"] = "not_available"

        return recommendations

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
        capabilities = self.detect_all_capabilities()

        # Check container support
        if container not in capabilities["container_formats"]:
            return False, f"Container format {container} not supported"

        if not capabilities["container_formats"][container]:
            return False, f"Container format {container} not available"

        # Check codec support
        if codec == "av1":
            if not capabilities["advanced_codecs"]["av1"]:
                return False, "AV1 codec not available (requires libaom-av1)"
        elif codec == "hevc":
            if not capabilities["advanced_codecs"]["hevc"]:
                return False, "HEVC codec not available (requires libx265)"
        elif codec == "vp9":
            if not capabilities["advanced_codecs"]["vp9"]:
                return False, "VP9 codec not available (requires libvpx-vp9)"

        # Check hardware acceleration
        if use_hardware:
            hardware_key = f"{codec}_nvenc"
            if hardware_key not in capabilities["hardware_encoders"]:
                hardware_key = f"{codec}_qsv"
            if hardware_key not in capabilities["hardware_encoders"]:
                hardware_key = f"{codec}_amf"

            if hardware_key not in capabilities["hardware_encoders"] or \
               not capabilities["hardware_encoders"][hardware_key]:
                return False, f"Hardware acceleration for {codec} not available"

        return True, "All requirements can be met"

    def get_capability_report(self) -> str:
        """Generate a human-readable capability report."""
        capabilities = self.detect_all_capabilities()

        report = []
        report.append(f"FFmpeg Version: {capabilities['ffmpeg_version']}")
        report.append("")

        report.append("Advanced Codecs:")
        for codec, available in capabilities["advanced_codecs"].items():
            status = "✓" if available else "✗"
            report.append(f"  {status} {codec.upper()}")
        report.append("")

        report.append("Hardware Encoders:")
        for encoder, available in capabilities["hardware_encoders"].items():
            if available:
                report.append(f"  ✓ {encoder}")

        hw_available = any(capabilities["hardware_encoders"].values())
        if not hw_available:
            report.append("  ✗ No hardware encoders available")
        report.append("")

        report.append("HDR Support:")
        for feature, available in capabilities["hdr_support"].items():
            status = "✓" if available else "✗"
            report.append(f"  {status} {feature}")

        return "\n".join(report)
