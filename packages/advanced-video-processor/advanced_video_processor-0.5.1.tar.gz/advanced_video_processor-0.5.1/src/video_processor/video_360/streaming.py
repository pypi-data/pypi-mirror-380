"""360° video streaming integration orchestrator."""

import logging
from pathlib import Path

from ..config import ProcessorConfig
from ..streaming.adaptive import AdaptiveStreamProcessor
from .bitrate_manager import BitrateManager
from .manifest_generator import ManifestGenerator
from .models import (
    ProjectionType,
    Video360StreamingPackage,
)
from .processor import Video360Processor
from .stream_processor import StreamProcessor

logger = logging.getLogger(__name__)


class Video360StreamProcessor:
    """
    Orchestrates adaptive streaming for 360° videos.

    Coordinates bitrate management, stream processing, and manifest generation
    for optimal 360° video streaming experiences.
    """

    def __init__(self, config: ProcessorConfig):
        self.config = config

        # Initialize specialized processors
        self.bitrate_manager = BitrateManager(config)
        self.stream_processor = StreamProcessor(config)
        self.manifest_generator = ManifestGenerator(config)

        # Integration with standard adaptive streaming
        self.adaptive_processor = AdaptiveStreamProcessor(config)
        self.video_360_processor = Video360Processor(config)

        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    async def create_360_adaptive_stream(
        self,
        video_path: Path,
        output_dir: Path,
        streaming_formats: list[str] | None = None,
        enable_viewport_adaptive: bool = False,
        enable_tiled_streaming: bool = False,
    ) -> Video360StreamingPackage:
        """
        Create complete adaptive streaming package for 360° video.

        Orchestrates all components to produce optimized streaming assets
        including multiple bitrate levels, manifests, and 360° metadata.
        """
        try:
            # Detect 360° video properties
            metadata = await self.video_360_processor.extract_spherical_metadata(video_path)

            if not metadata.is_spherical:
                # Fallback to standard adaptive streaming for non-360° content
                return await self._create_standard_adaptive_stream(
                    video_path, output_dir, streaming_formats
                )

            # Generate optimized bitrate ladder for 360° content
            bitrate_levels = await self.bitrate_manager.generate_360_bitrate_ladder(
                str(video_path), metadata.projection, streaming_formats
            )

            base_filename = video_path.stem

            # Generate video renditions
            await self.stream_processor.generate_360_renditions(
                video_path, bitrate_levels, output_dir, base_filename
            )

            # Create streaming manifests
            manifests = {}

            # Generate HLS manifest
            if not streaming_formats or "hls" in streaming_formats:
                hls_manifest = await self.manifest_generator.generate_360_hls_playlist(
                    bitrate_levels, output_dir, base_filename
                )
                manifests["hls"] = hls_manifest

            # Generate DASH manifest
            if not streaming_formats or "dash" in streaming_formats:
                dash_manifest = await self.manifest_generator.generate_360_dash_manifest(
                    bitrate_levels, output_dir, base_filename
                )
                manifests["dash"] = dash_manifest

            # Optional: viewport-adaptive streaming
            viewport_manifests = {}
            if enable_viewport_adaptive:
                viewport_manifests = await self._create_viewport_adaptive_streams(
                    video_path, output_dir, base_filename, metadata
                )

            # Optional: tiled streaming
            tiled_manifests = {}
            if enable_tiled_streaming:
                package_placeholder = Video360StreamingPackage(
                    base_filename=base_filename,
                    renditions=bitrate_levels,
                    manifests=manifests,
                    projection=metadata.projection,
                    supports_viewport_adaptive=enable_viewport_adaptive,
                    supports_tiled_streaming=enable_tiled_streaming,
                )
                tiled_manifests = await self.manifest_generator.create_tiled_manifests(
                    package_placeholder, output_dir
                )

            # Create final streaming package
            package = Video360StreamingPackage(
                base_filename=base_filename,
                renditions=bitrate_levels,
                manifests={**manifests, **viewport_manifests, **tiled_manifests},
                projection=metadata.projection,
                supports_viewport_adaptive=enable_viewport_adaptive,
                supports_tiled_streaming=enable_tiled_streaming,
                has_spatial_audio=metadata.has_spatial_audio,
                stereo_mode=metadata.stereo_mode,
            )

            self.logger.info(f"Created 360° streaming package: {len(bitrate_levels)} renditions, "
                           f"{len(package.manifests)} manifests")
            return package

        except Exception as e:
            self.logger.error(f"Failed to create 360° adaptive stream: {e}")
            raise

    async def _create_standard_adaptive_stream(
        self,
        video_path: Path,
        output_dir: Path,
        streaming_formats: list[str] | None = None,
    ) -> Video360StreamingPackage:
        """Fallback to standard adaptive streaming for non-360° content."""
        self.logger.info("Creating standard adaptive stream (non-360° content)")

        # Use standard adaptive streaming processor
        standard_package = await self.adaptive_processor.create_adaptive_stream(
            video_path, output_dir, streaming_formats or ["hls", "dash"]
        )

        # Convert to 360° package format for consistency
        return Video360StreamingPackage(
            base_filename=video_path.stem,
            renditions=[],  # Would need conversion from standard format
            manifests={"hls": standard_package.hls_manifest, "dash": standard_package.dash_manifest}
            if hasattr(standard_package, 'hls_manifest') else {},
            projection=ProjectionType.FLAT,
            supports_viewport_adaptive=False,
            supports_tiled_streaming=False,
        )

    async def _create_viewport_adaptive_streams(
        self,
        video_path: Path,
        output_dir: Path,
        base_filename: str,
        metadata,
    ) -> dict[str, Path]:
        """Create viewport-adaptive streaming assets."""
        try:
            # Generate optimal viewports based on content analysis
            analysis = await self.video_360_processor.analyze_360_content(video_path)
            viewports = analysis.recommended_viewports

            if not viewports:
                # Fallback to standard viewports
                viewports = [
                    {"yaw": 0, "pitch": 0, "fov": 90, "width": 1920, "height": 1080},
                    {"yaw": 90, "pitch": 0, "fov": 90, "width": 1280, "height": 720},
                ]

            # Generate viewport streams
            viewport_streams = await self.stream_processor.generate_viewport_streams(
                video_path, viewports, output_dir, base_filename
            )

            # Create viewport manifest
            viewport_manifest = await self.manifest_generator.generate_viewport_adaptive_manifest(
                viewport_streams, output_dir, base_filename
            )

            return {"viewport_hls": viewport_manifest}

        except Exception as e:
            self.logger.error(f"Failed to create viewport-adaptive streams: {e}")
            return {}
