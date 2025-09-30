"""HDR (High Dynamic Range) video processing capabilities."""

import json
import logging
import subprocess
from pathlib import Path
from typing import Literal

from ..config import ProcessorConfig
from ..exceptions import EncodingError, FFmpegError


class HDRProcessor:
    """HDR (High Dynamic Range) video processing and analysis."""

    def __init__(self, config: ProcessorConfig):
        self.config = config
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

        # HDR encoding presets
        self.hdr_presets = {
            "hdr10": {
                "color_primaries": "bt2020",
                "color_trc": "smpte2084",
                "colorspace": "bt2020nc",
                "master_display": "G(13250,34500)B(7500,3000)R(34000,16000)WP(15635,16450)L(10000000,1)",
                "max_cll": "1000,400",
            },
            "hdr10plus": {
                "color_primaries": "bt2020",
                "color_trc": "smpte2084",
                "colorspace": "bt2020nc",
                # HDR10+ metadata would be handled differently
            },
            "dolby_vision": {
                "color_primaries": "bt2020",
                "color_trc": "smpte2084",
                "colorspace": "bt2020nc",
                # Dolby Vision requires special handling
            },
        }

    def encode_hdr_hevc(
        self,
        input_path: Path,
        output_dir: Path,
        video_id: str,
        hdr_standard: Literal["hdr10", "hdr10plus", "dolby_vision"] = "hdr10",
        quality_preset: str = "high",
    ) -> Path:
        """
        Encode HDR video using HEVC with HDR metadata preservation.

        Args:
            input_path: Input HDR video file
            output_dir: Output directory
            video_id: Unique video identifier
            hdr_standard: HDR standard to use
            quality_preset: Quality preset for encoding

        Returns:
            Path to encoded HDR file
        """
        output_file = output_dir / f"{video_id}_hdr_{hdr_standard}.mp4"

        # Verify HDR support
        if not self._check_hdr_support(hdr_standard):
            raise EncodingError(f"HDR standard {hdr_standard} not supported")

        cmd = self._build_hdr_command(
            input_path, output_file, hdr_standard, quality_preset
        )

        try:
            self.logger.info(f"Starting HDR encoding with {hdr_standard}...")
            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode != 0:
                raise FFmpegError(f"HDR encoding failed: {result.stderr}")

            if not output_file.exists():
                raise EncodingError("HDR encoding failed - output file not created")

            self.logger.info(f"HDR encoding completed: {output_file}")
            return output_file

        except Exception as e:
            self.logger.error(f"HDR encoding error: {e}")
            raise

    def _build_hdr_command(
        self,
        input_path: Path,
        output_file: Path,
        hdr_standard: str,
        quality_preset: str,
    ) -> list[str]:
        """Build HDR encoding command."""
        # Quality settings
        quality_settings = {
            "low": {"crf": "22", "preset": "fast"},
            "medium": {"crf": "20", "preset": "medium"},
            "high": {"crf": "18", "preset": "slow"},
            "ultra": {"crf": "16", "preset": "veryslow"},
        }

        quality = quality_settings.get(quality_preset, quality_settings["high"])
        hdr_params = self.hdr_presets[hdr_standard]

        cmd = [
            self.config.ffmpeg_path,
            "-y",
            "-i", str(input_path),
            "-c:v", "libx265",
            "-crf", quality["crf"],
            "-preset", quality["preset"],
            "-pix_fmt", "yuv420p10le",  # 10-bit encoding for HDR
        ]

        # Add HDR-specific parameters
        cmd.extend([
            "-color_primaries", hdr_params["color_primaries"],
            "-color_trc", hdr_params["color_trc"],
            "-colorspace", hdr_params["colorspace"],
        ])

        # Add standard-specific metadata
        if hdr_standard == "hdr10":
            cmd.extend([
                "-master-display", hdr_params["master_display"],
                "-max-cll", hdr_params["max_cll"],
            ])

        # Audio settings (higher quality for HDR content)
        cmd.extend([
            "-c:a", "aac",
            "-b:a", "256k",
            str(output_file),
        ])

        return cmd

    def analyze_hdr_content(self, video_path: Path) -> dict:
        """
        Analyze video for HDR characteristics.

        Args:
            video_path: Path to video file

        Returns:
            Dictionary with HDR analysis results
        """
        try:
            # Use ffprobe to analyze HDR metadata
            cmd = [
                self.config.ffmpeg_path.replace("ffmpeg", "ffprobe"),
                "-v", "quiet",
                "-select_streams", "v:0",
                "-show_entries",
                "stream=color_primaries,color_trc,color_space,pix_fmt",
                "-of", "json",
                str(video_path),
            ]

            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode == 0:
                data = json.loads(result.stdout)
                stream = data.get("streams", [{}])[0]

                color_primaries = stream.get("color_primaries", "unknown")
                color_trc = stream.get("color_trc", "unknown")
                color_space = stream.get("color_space", "unknown")
                pix_fmt = stream.get("pix_fmt", "unknown")

                # Determine HDR characteristics
                is_hdr = self._is_hdr_content(color_primaries, color_trc, color_space, pix_fmt)
                hdr_standard = self._detect_hdr_standard(color_primaries, color_trc, color_space)

                return {
                    "is_hdr": is_hdr,
                    "hdr_standard": hdr_standard,
                    "color_primaries": color_primaries,
                    "color_transfer": color_trc,
                    "color_space": color_space,
                    "pixel_format": pix_fmt,
                    "bit_depth": self._extract_bit_depth(pix_fmt),
                }

            return {"is_hdr": False, "error": result.stderr}

        except Exception as e:
            return {"is_hdr": False, "error": str(e)}

    def _is_hdr_content(self, primaries: str, trc: str, space: str, pix_fmt: str) -> bool:
        """Determine if content is HDR based on metadata."""
        hdr_indicators = {
            "color_primaries": ["bt2020"],
            "color_trc": ["smpte2084", "arib-std-b67"],
            "color_space": ["bt2020nc", "bt2020c"],
            "pix_fmt": ["yuv420p10le", "yuv422p10le", "yuv444p10le"],
        }

        return (
            primaries in hdr_indicators["color_primaries"] or
            trc in hdr_indicators["color_trc"] or
            space in hdr_indicators["color_space"] or
            pix_fmt in hdr_indicators["pix_fmt"]
        )

    def _detect_hdr_standard(self, primaries: str, trc: str, space: str) -> str:
        """Detect HDR standard based on metadata."""
        if trc == "smpte2084":  # PQ (Perceptual Quantizer)
            if primaries == "bt2020":
                return "hdr10"  # Could be HDR10 or HDR10+
        elif trc == "arib-std-b67":  # HLG (Hybrid Log-Gamma)
            return "hlg"

        return "unknown"

    def _extract_bit_depth(self, pix_fmt: str) -> int:
        """Extract bit depth from pixel format."""
        if "10" in pix_fmt:
            return 10
        elif "12" in pix_fmt:
            return 12
        elif "16" in pix_fmt:
            return 16
        else:
            return 8

    def convert_sdr_to_hdr(
        self,
        input_path: Path,
        output_path: Path,
        hdr_standard: str = "hdr10",
    ) -> Path:
        """
        Convert SDR content to HDR using tone mapping.

        Args:
            input_path: Input SDR video
            output_path: Output HDR video
            hdr_standard: Target HDR standard

        Returns:
            Path to converted HDR file
        """
        cmd = [
            self.config.ffmpeg_path,
            "-y",
            "-i", str(input_path),
            "-vf", "zscale=transfer=smpte2084:matrix=bt2020nc:primaries=bt2020",
            "-c:v", "libx265",
            "-crf", "18",
            "-preset", "slow",
            "-pix_fmt", "yuv420p10le",
        ]

        # Add HDR metadata
        if hdr_standard == "hdr10":
            hdr_params = self.hdr_presets["hdr10"]
            cmd.extend([
                "-color_primaries", hdr_params["color_primaries"],
                "-color_trc", hdr_params["color_trc"],
                "-colorspace", hdr_params["colorspace"],
                "-master-display", hdr_params["master_display"],
                "-max-cll", hdr_params["max_cll"],
            ])

        cmd.extend([
            "-c:a", "copy",
            str(output_path),
        ])

        try:
            self.logger.info("Converting SDR to HDR...")
            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode != 0:
                raise FFmpegError(f"SDR to HDR conversion failed: {result.stderr}")

            self.logger.info(f"SDR to HDR conversion completed: {output_path}")
            return output_path

        except Exception as e:
            self.logger.error(f"SDR to HDR conversion error: {e}")
            raise

    def _check_hdr_support(self, hdr_standard: str) -> bool:
        """Check if HDR standard is supported."""
        supported_standards = ["hdr10"]  # Basic HDR10 support

        # Additional checks could be done for HDR10+ and Dolby Vision
        return hdr_standard in supported_standards

    @staticmethod
    def get_hdr_support() -> dict[str, bool]:
        """Check what HDR capabilities are available."""
        return {
            "hdr10": True,        # Basic HDR10 support
            "hdr10plus": False,   # Requires special build
            "dolby_vision": False,  # Requires licensed encoder
            "hlg": True,          # HLG support usually available
            "sdr_to_hdr": True,   # Tone mapping available
        }
