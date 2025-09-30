"""AV1 video encoder with advanced optimization."""

import logging
import platform
import subprocess
from pathlib import Path
from typing import Literal

from ..config import ProcessorConfig
from ..exceptions import EncodingError, FFmpegError


class AV1Encoder:
    """Specialized AV1 video encoder with optimized settings."""

    def __init__(self, config: ProcessorConfig):
        self.config = config
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

        # AV1-specific quality presets
        self.quality_presets = {
            "low": {
                "crf": "35",
                "cpu_used": "8",  # Fastest encoding
                "bitrate_multiplier": "0.7",  # AV1 needs less bitrate
            },
            "medium": {
                "crf": "28",
                "cpu_used": "6",  # Balanced speed/quality
                "bitrate_multiplier": "0.8",
            },
            "high": {
                "crf": "22",
                "cpu_used": "4",  # Better quality
                "bitrate_multiplier": "0.9",
            },
            "ultra": {
                "crf": "18",
                "cpu_used": "2",  # Highest quality, slower encoding
                "bitrate_multiplier": "1.0",
            },
        }

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
        Encode video to AV1 using libaom-av1 encoder.

        AV1 provides ~30% better compression than H.264 with same quality.
        Uses CRF (Constant Rate Factor) for quality-based encoding.

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
        # Check AV1 support early
        if not self.check_av1_support():
            raise EncodingError("AV1 encoding requires libaom-av1 encoder in FFmpeg")

        extension = "mp4" if container == "mp4" else "webm"
        output_file = output_dir / f"{video_id}_av1.{extension}"
        passlog_file = output_dir / f"{video_id}.av1-pass"

        preset = quality_preset or self.config.quality_preset
        quality = self.quality_presets[preset]

        # Clean existing pass logs
        self._clean_av1_passlogs(passlog_file)

        try:
            if use_two_pass:
                self._encode_av1_two_pass(
                    input_path, output_file, passlog_file, quality, container
                )
            else:
                self._encode_av1_single_pass(
                    input_path, output_file, quality, container
                )

        finally:
            self._clean_av1_passlogs(passlog_file)

        if not output_file.exists():
            raise EncodingError("AV1 encoding failed - output file not created")

        self.logger.info(f"AV1 encoding completed: {output_file}")
        return output_file

    def _encode_av1_two_pass(
        self,
        input_path: Path,
        output_file: Path,
        passlog_file: Path,
        quality: dict[str, str],
        container: str,
    ) -> None:
        """Execute AV1 two-pass encoding."""
        # Pass 1 - Analysis pass
        pass1_cmd = [
            self.config.ffmpeg_path,
            "-y",
            "-i", str(input_path),
            "-c:v", "libaom-av1",
            "-crf", quality["crf"],
            "-cpu-used", quality["cpu_used"],
            "-row-mt", "1",  # Enable row-based multithreading
            "-tiles", "2x2",  # Tile-based encoding for parallelization
            "-pass", "1",
            "-passlogfile", str(passlog_file),
            "-an",  # No audio in pass 1
            "-f", container,
            self._get_null_output(container),
        ]

        self.logger.info("Starting AV1 pass 1...")
        result = subprocess.run(pass1_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise FFmpegError(f"AV1 Pass 1 failed: {result.stderr}")

        # Pass 2 - Final encoding
        pass2_cmd = [
            self.config.ffmpeg_path,
            "-y",
            "-i", str(input_path),
            "-c:v", "libaom-av1",
            "-crf", quality["crf"],
            "-cpu-used", quality["cpu_used"],
            "-row-mt", "1",
            "-tiles", "2x2",
            "-pass", "2",
            "-passlogfile", str(passlog_file),
        ]

        # Add audio encoding based on container
        pass2_cmd.extend(self._get_audio_settings(container))
        pass2_cmd.append(str(output_file))

        self.logger.info("Starting AV1 pass 2...")
        result = subprocess.run(pass2_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise FFmpegError(f"AV1 Pass 2 failed: {result.stderr}")

    def _encode_av1_single_pass(
        self,
        input_path: Path,
        output_file: Path,
        quality: dict[str, str],
        container: str,
    ) -> None:
        """Execute AV1 single-pass CRF encoding."""
        cmd = [
            self.config.ffmpeg_path,
            "-y",
            "-i", str(input_path),
            "-c:v", "libaom-av1",
            "-crf", quality["crf"],
            "-cpu-used", quality["cpu_used"],
            "-row-mt", "1",
            "-tiles", "2x2",
        ]

        # Add audio encoding based on container
        cmd.extend(self._get_audio_settings(container))
        cmd.append(str(output_file))

        self.logger.info("Starting AV1 single-pass encoding...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise FFmpegError(f"AV1 single-pass encoding failed: {result.stderr}")

    def _get_audio_settings(self, container: str) -> list[str]:
        """Get audio encoding settings based on container."""
        if container == "webm":
            return ["-c:a", "libopus", "-b:a", "128k"]
        else:  # mp4
            return ["-c:a", "aac", "-b:a", "128k"]

    def _get_null_output(self, container: str) -> str:
        """Get null output path for first pass."""
        if platform.system() == "Windows":
            return "NUL"
        return "/dev/null"

    def _clean_av1_passlogs(self, passlog_file: Path) -> None:
        """Clean up AV1 pass log files."""
        for suffix in ["-0.log", ".log"]:
            log_file = Path(f"{passlog_file}{suffix}")
            if log_file.exists():
                try:
                    log_file.unlink()
                except FileNotFoundError:
                    pass  # Already removed

    def get_bitrate_multiplier(self, quality_preset: str | None = None) -> float:
        """
        Get bitrate multiplier for AV1 encoding.

        AV1 needs significantly less bitrate than H.264 for same quality.
        """
        preset = quality_preset or self.config.quality_preset
        return float(self.quality_presets[preset]["bitrate_multiplier"])

    def check_av1_support(self) -> bool:
        """Check if FFmpeg has AV1 encoding support."""
        try:
            result = subprocess.run(
                [self.config.ffmpeg_path, "-encoders"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            return "libaom-av1" in result.stdout
        except (subprocess.SubprocessError, FileNotFoundError):
            return False

    def estimate_av1_encoding_time(
        self,
        input_path: Path,
        quality_preset: str | None = None,
        use_two_pass: bool = True,
    ) -> dict:
        """
        Estimate AV1 encoding time based on input characteristics.

        Args:
            input_path: Input video file
            quality_preset: Quality preset to use
            use_two_pass: Whether using two-pass encoding

        Returns:
            Dictionary with time estimates
        """
        try:
            # Get video info
            probe_cmd = [
                self.config.ffmpeg_path.replace("ffmpeg", "ffprobe"),
                "-v", "quiet",
                "-print_format", "json",
                "-show_format",
                "-show_streams",
                str(input_path),
            ]

            result = subprocess.run(probe_cmd, capture_output=True, text=True)
            if result.returncode != 0:
                return {"error": "Could not analyze input file"}

            import json
            data = json.loads(result.stdout)

            # Extract video stream info
            video_stream = next((s for s in data["streams"] if s["codec_type"] == "video"), None)
            if not video_stream:
                return {"error": "No video stream found"}

            width = int(video_stream.get("width", 1920))
            height = int(video_stream.get("height", 1080))
            duration = float(data["format"].get("duration", 60))

            preset = quality_preset or self.config.quality_preset
            quality = self.quality_presets[preset]

            # Rough estimation based on resolution and quality
            pixels_per_second = width * height * 30  # Assume 30fps
            total_pixels = pixels_per_second * duration

            # AV1 encoding is significantly slower than H.264
            base_speed = {
                "8": 500000,    # cpu-used=8 (fastest)
                "6": 300000,    # cpu-used=6 (balanced)
                "4": 150000,    # cpu-used=4 (quality)
                "2": 75000,     # cpu-used=2 (best quality)
            }

            cpu_used = quality["cpu_used"]
            encoding_speed = base_speed.get(cpu_used, 200000)

            estimated_seconds = total_pixels / encoding_speed
            if use_two_pass:
                estimated_seconds *= 2.2  # Two-pass overhead

            return {
                "estimated_time_seconds": estimated_seconds,
                "estimated_time_minutes": estimated_seconds / 60,
                "resolution": f"{width}x{height}",
                "duration_seconds": duration,
                "quality_preset": preset,
                "cpu_used": cpu_used,
                "two_pass": use_two_pass,
            }

        except Exception as e:
            return {"error": str(e)}
