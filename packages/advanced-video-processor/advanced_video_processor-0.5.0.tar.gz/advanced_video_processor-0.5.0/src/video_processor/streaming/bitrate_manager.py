"""Bitrate ladder management for adaptive streaming."""

import logging

from ..config import ProcessorConfig
from ..constants import ENCODING

logger = logging.getLogger(__name__)

# Optional AI integration
try:
    from ..ai.content_analyzer import VideoContentAnalyzer

    HAS_AI_SUPPORT = True
except ImportError:
    HAS_AI_SUPPORT = False


class BitrateManager:
    """Manages bitrate ladder generation and optimization for adaptive streaming."""

    def __init__(self, config: ProcessorConfig, enable_ai_optimization: bool = True) -> None:
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.config = config
        self.enable_ai_optimization = enable_ai_optimization and HAS_AI_SUPPORT

        if self.enable_ai_optimization:
            self.content_analyzer = VideoContentAnalyzer()
        else:
            self.content_analyzer = None

    async def generate_optimal_bitrate_ladder(
        self, video_path, base_bitrate: int = 2500
    ) -> list:
        """Generate optimized bitrate ladder based on content analysis."""
        from .models import BitrateLevel

        try:
            # Analyze video content if AI is available
            content_analysis = None
            if self.content_analyzer:
                try:
                    content_analysis = await self.content_analyzer.analyze_video(
                        video_path
                    )
                    self.logger.info("Content analysis completed for bitrate optimization")
                except Exception as e:
                    self.logger.warning(f"Content analysis failed: {e}")

            # Generate base ladder
            bitrate_levels = []

            # Quality levels with standard resolutions
            quality_configs = [
                ("240p", 426, 240, 0.15),  # Low quality mobile
                ("360p", 640, 360, 0.25),  # Standard mobile
                ("480p", 854, 480, 0.4),   # Standard quality
                ("720p", 1280, 720, 0.7),  # HD quality
                ("1080p", 1920, 1080, 1.0), # Full HD (base)
            ]

            # Apply AI-based adjustments if available
            bitrate_multiplier = 1.0
            if content_analysis:
                motion_intensity = content_analysis.motion_analysis.get("motion_intensity", 0.5)
                # Higher motion = higher bitrate needed
                bitrate_multiplier = 1.0 + (motion_intensity * ENCODING["motion_multipliers"]["motion_factor"])

            for name, width, height, factor in quality_configs:
                adjusted_bitrate = int(base_bitrate * factor * bitrate_multiplier)
                max_bitrate = int(adjusted_bitrate * ENCODING["bitrate_control"]["maxrate_multiplier"])

                level = BitrateLevel(
                    name=name,
                    width=width,
                    height=height,
                    bitrate=adjusted_bitrate,
                    max_bitrate=max_bitrate,
                    codec=self._get_optimal_codec(),
                    container=self._get_output_format(self._get_optimal_codec()),
                )
                bitrate_levels.append(level)

            self.logger.info(f"Generated {len(bitrate_levels)} bitrate levels")
            return bitrate_levels

        except Exception as e:
            self.logger.error(f"Failed to generate bitrate ladder: {e}")
            raise

    def _get_optimal_codec(self) -> str:
        """Determine optimal codec based on configuration."""
        if "h264" in self.config.video_codecs:
            return "h264"
        elif "hevc" in self.config.video_codecs:
            return "hevc"
        elif "av1" in self.config.video_codecs:
            return "av1"
        else:
            return "h264"  # Fallback

    def _get_output_format(self, codec: str) -> str:
        """Get appropriate container format for codec."""
        format_mapping = {
            "h264": "mp4",
            "hevc": "mp4",
            "av1": "mp4",
            "vp9": "webm",
        }
        return format_mapping.get(codec, "mp4")

    def _get_quality_preset_for_bitrate(self, bitrate: int) -> str:
        """Map bitrate to ProcessorConfig quality preset."""
        if bitrate < 500:
            return "low"        # Fast encoding for low bitrates
        elif bitrate < 2000:
            return "medium"     # Balanced quality/speed
        elif bitrate < 5000:
            return "high"       # Higher quality for mid-range bitrates
        else:
            return "ultra"      # Maximum quality for high bitrates

    def _get_ffmpeg_preset_for_bitrate(self, bitrate: int) -> str:
        """Map bitrate to FFmpeg preset for encoding speed/quality tradeoff."""
        if bitrate < 500:
            return "fast"       # Fast encoding for low bitrates
        elif bitrate < 2000:
            return "medium"     # Balanced speed/quality
        elif bitrate < 5000:
            return "slow"       # Higher quality for mid-range bitrates
        else:
            return "veryslow"   # Maximum quality for high bitrates

    def _get_ffmpeg_options_for_level(self, level) -> dict[str, str]:
        """Generate FFmpeg options for specific bitrate level."""
        preset = self._get_ffmpeg_preset_for_bitrate(level.bitrate)

        return {
            "preset": preset,
            "profile": "high" if level.codec == "h264" else "main",
            "level": "4.0",
            "pix_fmt": "yuv420p",
        }
