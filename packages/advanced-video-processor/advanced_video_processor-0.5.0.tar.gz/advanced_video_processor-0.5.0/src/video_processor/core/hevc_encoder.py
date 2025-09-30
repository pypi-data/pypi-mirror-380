"""HEVC/H.265 video encoder with hardware acceleration support."""

import logging
import subprocess
from pathlib import Path

from ..config import ProcessorConfig
from ..exceptions import EncodingError, FFmpegError


class HEVCEncoder:
    """Specialized HEVC/H.265 video encoder with hardware acceleration."""

    def __init__(self, config: ProcessorConfig):
        self.config = config
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

        # HEVC-specific quality presets
        self.quality_presets = {
            "low": {"crf": "30", "preset": "fast"},
            "medium": {"crf": "25", "preset": "medium"},
            "high": {"crf": "20", "preset": "slow"},
            "ultra": {"crf": "16", "preset": "veryslow"},
        }

    def encode_hevc(
        self,
        input_path: Path,
        output_dir: Path,
        video_id: str,
        use_hardware: bool = False,
        quality_preset: str | None = None,
    ) -> Path:
        """
        Encode video to HEVC/H.265 for better compression than H.264.

        HEVC provides ~25% better compression than H.264 with same quality.

        Args:
            input_path: Input video file
            output_dir: Output directory
            video_id: Unique video identifier
            use_hardware: Whether to attempt hardware acceleration
            quality_preset: Override default quality preset

        Returns:
            Path to encoded file
        """
        output_file = output_dir / f"{video_id}_hevc.mp4"
        preset = quality_preset or self.config.quality_preset
        quality = self.quality_presets[preset]

        # Choose encoder based on hardware availability
        encoder = "libx265"
        if use_hardware:
            hw_encoder = self._detect_hardware_hevc_encoder()
            if hw_encoder:
                encoder = hw_encoder
                self.logger.info(f"Using hardware HEVC encoder: {encoder}")
            else:
                self.logger.info("Hardware HEVC not available, using software encoder")

        try:
            cmd = self._build_hevc_command(
                input_path, output_file, encoder, quality
            )

            self.logger.info(f"Starting HEVC encoding with {encoder}...")
            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode != 0:
                # Fallback to software encoding if hardware fails
                if use_hardware and encoder != "libx265":
                    self.logger.warning("Hardware encoding failed, falling back to software")
                    return self.encode_hevc(
                        input_path, output_dir, video_id, use_hardware=False, quality_preset=quality_preset
                    )
                raise FFmpegError(f"HEVC encoding failed: {result.stderr}")

            if not output_file.exists():
                raise EncodingError("HEVC encoding failed - output file not created")

            self.logger.info(f"HEVC encoding completed: {output_file}")
            return output_file

        except Exception as e:
            if use_hardware and encoder != "libx265":
                # Fallback to software encoding
                self.logger.warning(f"Hardware encoding error, falling back to software: {e}")
                return self.encode_hevc(
                    input_path, output_dir, video_id, use_hardware=False, quality_preset=quality_preset
                )
            raise

    def _build_hevc_command(
        self,
        input_path: Path,
        output_file: Path,
        encoder: str,
        quality: dict[str, str],
    ) -> list[str]:
        """Build HEVC encoding command."""
        cmd = [
            self.config.ffmpeg_path,
            "-y",
            "-i", str(input_path),
            "-c:v", encoder,
        ]

        if encoder == "libx265":
            # Software encoding with x265
            cmd.extend([
                "-crf", quality["crf"],
                "-preset", quality["preset"],
                "-x265-params", "log-level=error",
            ])
        elif encoder == "hevc_nvenc":
            # NVIDIA hardware encoding
            cmd.extend([
                "-crf", quality["crf"],
                "-preset", "medium",
                "-profile:v", "main10",  # 10-bit support
            ])
        elif encoder == "hevc_qsv":
            # Intel Quick Sync Video
            cmd.extend([
                "-crf", quality["crf"],
                "-preset", "medium",
            ])
        elif encoder == "hevc_amf":
            # AMD hardware encoding
            cmd.extend([
                "-crf", quality["crf"],
                "-quality", "balanced",
            ])

        # Audio settings
        cmd.extend([
            "-c:a", "aac",
            "-b:a", "192k",
            str(output_file),
        ])

        return cmd

    def _detect_hardware_hevc_encoder(self) -> str | None:
        """Detect available hardware HEVC encoder."""
        encoders_to_check = ["hevc_nvenc", "hevc_qsv", "hevc_amf"]

        try:
            result = subprocess.run(
                [self.config.ffmpeg_path, "-encoders"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            for encoder in encoders_to_check:
                if encoder in result.stdout:
                    # Additional check to ensure encoder actually works
                    if self._test_hardware_encoder(encoder):
                        return encoder

        except (subprocess.SubprocessError, FileNotFoundError):
            pass

        return None

    def _test_hardware_encoder(self, encoder: str) -> bool:
        """Test if a hardware encoder actually works."""
        try:
            # Create a simple test encode
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

    def check_hevc_support(self) -> bool:
        """Check if FFmpeg has HEVC encoding support."""
        try:
            result = subprocess.run(
                [self.config.ffmpeg_path, "-encoders"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            return "libx265" in result.stdout
        except (subprocess.SubprocessError, FileNotFoundError):
            return False

    def check_hardware_hevc_support(self) -> dict[str, bool]:
        """Check what hardware HEVC encoders are available."""
        hardware_encoders = {
            "hevc_nvenc": False,  # NVIDIA
            "hevc_qsv": False,    # Intel
            "hevc_amf": False,    # AMD
        }

        try:
            result = subprocess.run(
                [self.config.ffmpeg_path, "-encoders"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            for encoder in hardware_encoders:
                if encoder in result.stdout:
                    hardware_encoders[encoder] = self._test_hardware_encoder(encoder)

        except (subprocess.SubprocessError, FileNotFoundError):
            pass

        return hardware_encoders

    def estimate_hevc_encoding_time(
        self,
        input_path: Path,
        use_hardware: bool = False,
        quality_preset: str | None = None,
    ) -> dict:
        """
        Estimate HEVC encoding time based on input characteristics.

        Args:
            input_path: Input video file
            use_hardware: Whether using hardware acceleration
            quality_preset: Quality preset to use

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

            # Estimation based on resolution, preset, and hardware
            pixels_per_second = width * height * 30  # Assume 30fps
            total_pixels = pixels_per_second * duration

            # HEVC encoding speeds (pixels per second)
            if use_hardware:
                # Hardware encoding is much faster
                encoding_speed = 8000000  # ~8M pixels/sec
            else:
                # Software encoding speeds vary by preset
                preset_speeds = {
                    "fast": 2000000,
                    "medium": 1500000,
                    "slow": 800000,
                    "veryslow": 400000,
                }
                encoding_speed = preset_speeds.get(quality["preset"], 1500000)

            estimated_seconds = total_pixels / encoding_speed

            return {
                "estimated_time_seconds": estimated_seconds,
                "estimated_time_minutes": estimated_seconds / 60,
                "resolution": f"{width}x{height}",
                "duration_seconds": duration,
                "quality_preset": preset,
                "use_hardware": use_hardware,
                "encoding_speed_mpps": encoding_speed / 1000000,  # Megapixels per second
            }

        except Exception as e:
            return {"error": str(e)}
