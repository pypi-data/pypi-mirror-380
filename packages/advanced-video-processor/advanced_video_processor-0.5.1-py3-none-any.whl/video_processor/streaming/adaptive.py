"""Adaptive streaming processor - compatibility layer and public API."""

import logging
from pathlib import Path
from typing import Literal

from ..config import ProcessorConfig
from .adaptive_orchestrator import AdaptiveStreamOrchestrator
from .models import BitrateLevel, StreamingPackage

# Optional AI integration for test compatibility
try:
    from ..ai.content_analyzer import VideoContentAnalyzer
except ImportError:
    VideoContentAnalyzer = None

# Re-export data models for backward compatibility
__all__ = ["AdaptiveStreamProcessor", "BitrateLevel", "StreamingPackage"]

logger = logging.getLogger(__name__)


class AdaptiveStreamProcessor:
    """
    Adaptive streaming processor - compatibility wrapper around new orchestrator.

    Creates HLS and DASH streams with multiple bitrate levels optimized using AI analysis.
    """

    def __init__(
        self, config: ProcessorConfig, enable_ai_optimization: bool = True
    ) -> None:
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

        # Delegate to new orchestrator
        self._orchestrator = AdaptiveStreamOrchestrator(config, enable_ai_optimization)

        # Expose config and optimization setting for backward compatibility
        self.config = config
        self.enable_ai_optimization = enable_ai_optimization

        # Expose AI analyzer for test compatibility
        self.content_analyzer = self._orchestrator.content_analyzer if hasattr(self._orchestrator, 'content_analyzer') else None

        self.logger.info(
            "Adaptive streaming processor initialized (compatibility layer)"
        )

    async def create_adaptive_stream(
        self,
        video_path: Path,
        output_dir: Path,
        video_id: str | None = None,
        streaming_formats: list[Literal["hls", "dash"]] = None,
        custom_bitrate_ladder: list[BitrateLevel] | None = None,
    ) -> StreamingPackage:
        """
        Create adaptive streaming package from source video.

        Args:
            video_path: Source video file
            output_dir: Output directory for streaming files
            video_id: Optional video identifier
            streaming_formats: List of streaming formats to generate
            custom_bitrate_ladder: Custom bitrate levels (uses optimized defaults if None)

        Returns:
            Complete streaming package with manifests and segments
        """
        # Delegate to orchestrator
        return await self._orchestrator.create_adaptive_stream(
            video_path=video_path,
            output_dir=output_dir,
            video_id=video_id,
            streaming_formats=streaming_formats,
            custom_bitrate_ladder=custom_bitrate_ladder,
        )


    def get_streaming_capabilities(self) -> dict[str, bool]:
        """Get information about available streaming capabilities."""
        return self._orchestrator.get_streaming_capabilities()

    # Backward compatibility methods for tests
    def _get_output_format(self, codec: str) -> str:
        """Map codec to output format - compatibility method."""
        return self._orchestrator._get_output_format(codec)

    def _get_quality_preset_for_bitrate(self, bitrate: int) -> str:
        """Select quality preset based on target bitrate - compatibility method."""
        return self._orchestrator._get_quality_preset_for_bitrate(bitrate)

    def _get_ffmpeg_options_for_level(self, level) -> dict[str, str]:
        """Generate FFmpeg options for specific bitrate level - compatibility method."""
        return self._orchestrator.bitrate_manager._get_ffmpeg_options_for_level(level)

    async def _generate_optimal_bitrate_ladder(self, video_path: Path) -> list:
        """Generate optimal bitrate ladder - compatibility method."""
        return await self._orchestrator.bitrate_manager.generate_optimal_bitrate_ladder(video_path)

    async def _generate_bitrate_renditions(self, source_path: Path, output_dir: Path, video_id: str, bitrate_levels: list) -> dict[str, Path]:
        """Generate multiple bitrate renditions - compatibility method."""
        return await self._orchestrator._generate_bitrate_renditions(source_path, output_dir, video_id, bitrate_levels)

    async def _generate_thumbnail_track(self, source_path: Path, output_dir: Path, video_id: str) -> Path:
        """Generate thumbnail track - compatibility method."""
        return await self._orchestrator.playlist_generator.generate_thumbnail_track(source_path, output_dir, video_id)

    async def _generate_hls_playlist(self, output_dir: Path, video_id: str, bitrate_levels: list, rendition_files: dict[str, Path]) -> Path:
        """Generate HLS playlist - compatibility method."""
        return await self._orchestrator.playlist_generator.generate_hls_playlist(bitrate_levels, output_dir, video_id)

    async def _generate_dash_manifest(self, output_dir: Path, video_id: str, bitrate_levels: list, rendition_files: dict[str, Path]) -> Path:
        """Generate DASH manifest - compatibility method."""
        return await self._orchestrator.playlist_generator.generate_dash_manifest(bitrate_levels, output_dir, video_id)
