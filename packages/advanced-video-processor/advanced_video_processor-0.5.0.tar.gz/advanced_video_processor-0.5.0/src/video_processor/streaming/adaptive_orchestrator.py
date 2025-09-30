"""Main orchestrator for adaptive streaming operations."""

import asyncio
import logging
from pathlib import Path
from typing import Literal

from ..config import ProcessorConfig
from ..core.processor import VideoProcessor
from ..exceptions import EncodingError
from .bitrate_manager import BitrateManager
from .models import StreamingPackage
from .playlist_generator import PlaylistGenerator

# Optional AI integration
try:
    from ..ai.content_analyzer import VideoContentAnalyzer

    HAS_AI_SUPPORT = True
except ImportError:
    HAS_AI_SUPPORT = False

logger = logging.getLogger(__name__)


class AdaptiveStreamOrchestrator:
    """
    Main orchestrator for adaptive streaming that coordinates bitrate management
    and playlist generation components.

    Creates HLS and DASH streams with multiple bitrate levels optimized using AI analysis.
    """

    def __init__(
        self, config: ProcessorConfig, enable_ai_optimization: bool = True
    ) -> None:
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.config = config
        self.enable_ai_optimization = enable_ai_optimization and HAS_AI_SUPPORT

        # Initialize component managers
        self.bitrate_manager = BitrateManager(config, enable_ai_optimization)
        self.playlist_generator = PlaylistGenerator(config)

        if self.enable_ai_optimization:
            self.content_analyzer = VideoContentAnalyzer()
        else:
            self.content_analyzer = None

        self.logger.info(
            f"Adaptive streaming orchestrator initialized with AI optimization: {self.enable_ai_optimization}"
        )

    async def create_adaptive_stream(
        self,
        video_path: Path,
        output_dir: Path,
        video_id: str | None = None,
        streaming_formats: list[Literal["hls", "dash"]] = None,
        custom_bitrate_ladder: list = None,
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
        if video_id is None:
            video_id = video_path.stem

        if streaming_formats is None:
            streaming_formats = ["hls", "dash"]

        self.logger.info(f"Creating adaptive stream for {video_path} -> {output_dir}")

        # Step 1: Generate optimal bitrate ladder
        bitrate_levels = custom_bitrate_ladder
        if bitrate_levels is None:
            bitrate_levels = await self.bitrate_manager.generate_optimal_bitrate_ladder(
                video_path
            )

        # Step 2: Create output directory structure
        stream_dir = output_dir / video_id
        stream_dir.mkdir(parents=True, exist_ok=True)

        # Step 3: Generate multiple bitrate renditions
        rendition_files = await self._generate_bitrate_renditions(
            video_path, stream_dir, video_id, bitrate_levels
        )

        # Step 4: Generate streaming manifests
        streaming_package = StreamingPackage(
            video_id=video_id,
            source_path=video_path,
            output_dir=stream_dir,
            bitrate_levels=bitrate_levels,
        )

        if "hls" in streaming_formats:
            streaming_package.hls_playlist = await self.playlist_generator.generate_hls_playlist(
                bitrate_levels, stream_dir, video_id
            )

        if "dash" in streaming_formats:
            streaming_package.dash_manifest = await self.playlist_generator.generate_dash_manifest(
                bitrate_levels, stream_dir, video_id
            )

        # Step 5: Generate thumbnail track for scrubbing
        streaming_package.thumbnail_track = await self.playlist_generator.generate_thumbnail_track(
            video_path, stream_dir, video_id
        )

        self.logger.info("Adaptive streaming package created successfully")
        return streaming_package

    async def _generate_bitrate_renditions(
        self,
        source_path: Path,
        output_dir: Path,
        video_id: str,
        bitrate_levels: list,
    ) -> dict[str, Path]:
        """
        Generate multiple bitrate renditions using existing VideoProcessor infrastructure.
        """
        self.logger.info(f"Generating {len(bitrate_levels)} bitrate renditions")
        rendition_files = {}

        for level in bitrate_levels:
            rendition_name = f"{video_id}_{level.name}"
            rendition_dir = output_dir / level.name
            rendition_dir.mkdir(exist_ok=True)

            # Create specialized config for this bitrate level
            rendition_config = ProcessorConfig(
                output_dir=rendition_dir,
                output_containers=[self._get_output_format(level.codec)],
                quality_preset=self._get_quality_preset_for_bitrate(level.bitrate),
                custom_ffmpeg_options=self.bitrate_manager._get_ffmpeg_options_for_level(level),
            )

            # Process video at this bitrate level
            try:
                processor = VideoProcessor(rendition_config)
                result = await asyncio.to_thread(
                    processor.process_video, source_path, rendition_name
                )

                # Get the generated file
                format_name = self._get_output_format(level.codec)
                if format_name in result.encoded_files:
                    rendition_files[level.name] = result.encoded_files[format_name]
                    self.logger.info(
                        f"Generated {level.name} rendition: {result.encoded_files[format_name]}"
                    )
                else:
                    self.logger.error(f"Failed to generate {level.name} rendition")

            except Exception as e:
                self.logger.error(f"Error generating {level.name} rendition: {e}")
                raise EncodingError(f"Failed to generate {level.name} rendition: {e}") from e

        return rendition_files

    def _get_output_format(self, codec: str) -> str:
        """Map codec to output format."""
        return self.bitrate_manager._get_output_format(codec)

    def _get_quality_preset_for_bitrate(self, bitrate: int) -> str:
        """Select quality preset based on target bitrate."""
        return self.bitrate_manager._get_quality_preset_for_bitrate(bitrate)

    def get_streaming_capabilities(self) -> dict[str, bool]:
        """Get information about available streaming capabilities."""
        return {
            "hls_streaming": True,
            "dash_streaming": True,
            "ai_optimization": self.enable_ai_optimization,
            "advanced_codecs": self.config.enable_hevc_encoding
            or self.config.enable_av1_encoding,
            "thumbnail_tracks": True,
            "multi_bitrate": True,
        }
