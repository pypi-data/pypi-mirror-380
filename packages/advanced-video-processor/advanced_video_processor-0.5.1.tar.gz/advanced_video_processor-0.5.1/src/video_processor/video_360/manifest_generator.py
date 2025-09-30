"""360° video manifest generation for HLS and DASH streaming."""

import logging
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

from ..config import ProcessorConfig
from .models import BitrateLevel360, Video360StreamingPackage

logger = logging.getLogger(__name__)


class ManifestGenerator:
    """Generates streaming manifests (HLS/DASH) for 360° video content."""

    def __init__(self, config: ProcessorConfig):
        self.config = config
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    async def generate_360_hls_playlist(
        self,
        renditions: list[BitrateLevel360],
        output_dir: Path,
        base_filename: str,
    ) -> Path:
        """Generate HLS master playlist with 360° video metadata."""
        try:
            playlist_content = ["#EXTM3U", "#EXT-X-VERSION:6"]

            # Add 360° metadata
            playlist_content.extend([
                "#EXT-X-DEFINE:NAME=\"projection\",VALUE=\"equirectangular\"",
                "#EXT-X-DEFINE:NAME=\"stereo-mode\",VALUE=\"mono\"",
                "#EXT-X-DEFINE:NAME=\"spherical\",VALUE=\"1\"",
            ])

            # Add stream variants
            for rendition in renditions:
                playlist_content.append(
                    f"#EXT-X-STREAM-INF:BANDWIDTH={rendition.bitrate},"
                    f"RESOLUTION={rendition.resolution[0]}x{rendition.resolution[1]},"
                    f"FRAME-RATE={rendition.fps}"
                )
                playlist_content.append(f"{base_filename}_{rendition.quality}.m3u8")

            # Write playlist
            playlist_path = output_dir / f"{base_filename}_master.m3u8"
            playlist_path.write_text("\n".join(playlist_content))

            self.logger.info(f"Generated HLS playlist: {playlist_path}")
            return playlist_path

        except Exception as e:
            self.logger.error(f"Failed to generate HLS playlist: {e}")
            raise

    async def generate_360_dash_manifest(
        self,
        renditions: list[BitrateLevel360],
        output_dir: Path,
        base_filename: str,
    ) -> Path:
        """Generate DASH manifest with 360° video metadata."""
        try:
            # Create DASH MPD structure
            mpd = ET.Element("MPD")
            mpd.set("xmlns", "urn:mpeg:dash:schema:mpd:2011")
            mpd.set("type", "static")
            mpd.set("mediaPresentationDuration", "PT1H")  # Placeholder duration

            # Add 360° metadata
            self._add_360_metadata_to_dash_element(mpd)

            # Create period
            period = ET.SubElement(mpd, "Period")
            period.set("id", "0")

            # Create adaptation set for video
            video_as = ET.SubElement(period, "AdaptationSet")
            video_as.set("mimeType", "video/mp4")
            video_as.set("segmentAlignment", "true")

            # Add representations for each rendition
            for rendition in renditions:
                representation = ET.SubElement(video_as, "Representation")
                representation.set("id", rendition.quality)
                representation.set("bandwidth", str(rendition.bitrate))
                representation.set("width", str(rendition.resolution[0]))
                representation.set("height", str(rendition.resolution[1]))
                representation.set("frameRate", str(rendition.fps))

                # Add segment template
                segment_template = ET.SubElement(representation, "SegmentTemplate")
                segment_template.set("media", f"{base_filename}_{rendition.quality}_$Number$.mp4")
                segment_template.set("initialization", f"{base_filename}_{rendition.quality}_init.mp4")
                segment_template.set("startNumber", "1")

            # Write manifest
            manifest_path = output_dir / f"{base_filename}.mpd"
            tree = ET.ElementTree(mpd)
            ET.indent(tree, space="  ", level=0)
            tree.write(manifest_path, encoding="utf-8", xml_declaration=True)

            self.logger.info(f"Generated DASH manifest: {manifest_path}")
            return manifest_path

        except Exception as e:
            self.logger.error(f"Failed to generate DASH manifest: {e}")
            raise

    def _add_360_metadata_to_dash_element(self, mpd_element: ET.Element) -> None:
        """Add 360° metadata to DASH MPD element."""
        # Add spherical video descriptor
        descriptor = ET.SubElement(mpd_element, "Descriptor")
        descriptor.set("schemeIdUri", "http://dashif.org/guidelines/spherical-video")
        descriptor.set("value", "1")

        # Add projection descriptor
        proj_descriptor = ET.SubElement(mpd_element, "Descriptor")
        proj_descriptor.set("schemeIdUri", "http://dashif.org/guidelines/spherical-video/projection")
        proj_descriptor.set("value", "equirectangular")

    async def generate_viewport_adaptive_manifest(
        self,
        viewport_streams: list[dict[str, Any]],
        output_dir: Path,
        base_filename: str,
    ) -> Path:
        """Generate manifest for viewport-adaptive streaming."""
        try:
            # Create viewport-adaptive HLS playlist
            playlist_content = ["#EXTM3U", "#EXT-X-VERSION:7"]

            # Add viewport metadata
            playlist_content.extend([
                "#EXT-X-DEFINE:NAME=\"viewport-adaptive\",VALUE=\"1\"",
                "#EXT-X-DEFINE:NAME=\"projection\",VALUE=\"equirectangular\"",
            ])

            # Add viewport streams
            for viewport_stream in viewport_streams:
                playlist_content.append(
                    f"#EXT-X-STREAM-INF:BANDWIDTH={viewport_stream['bitrate']},"
                    f"RESOLUTION={viewport_stream['width']}x{viewport_stream['height']},"
                    f"VIEWPORT=\"{viewport_stream['viewport']}\""
                )
                playlist_content.append(f"{viewport_stream['filename']}.m3u8")

            # Write viewport manifest
            manifest_path = output_dir / f"{base_filename}_viewport.m3u8"
            manifest_path.write_text("\n".join(playlist_content))

            self.logger.info(f"Generated viewport-adaptive manifest: {manifest_path}")
            return manifest_path

        except Exception as e:
            self.logger.error(f"Failed to generate viewport-adaptive manifest: {e}")
            raise

    async def create_tiled_manifests(
        self,
        package: Video360StreamingPackage,
        output_dir: Path,
    ) -> dict[str, Path]:
        """Create tiled streaming manifests for bandwidth optimization."""
        try:
            manifests = {}

            # Create HLS tiled manifest
            hls_content = ["#EXTM3U", "#EXT-X-VERSION:7"]
            hls_content.extend([
                "#EXT-X-DEFINE:NAME=\"tiled\",VALUE=\"1\"",
                "#EXT-X-DEFINE:NAME=\"tile-format\",VALUE=\"6x4\"",  # 6x4 tiling
            ])

            hls_path = output_dir / f"{package.base_filename}_tiled.m3u8"
            hls_path.write_text("\n".join(hls_content))
            manifests["hls"] = hls_path

            # Create DASH tiled manifest
            mpd = ET.Element("MPD")
            mpd.set("xmlns", "urn:mpeg:dash:schema:mpd:2011")
            mpd.set("type", "static")

            # Add tiling metadata
            tiling_descriptor = ET.SubElement(mpd, "Descriptor")
            tiling_descriptor.set("schemeIdUri", "http://dashif.org/guidelines/tiled-streaming")
            tiling_descriptor.set("value", "6x4")

            dash_path = output_dir / f"{package.base_filename}_tiled.mpd"
            tree = ET.ElementTree(mpd)
            tree.write(dash_path, encoding="utf-8", xml_declaration=True)
            manifests["dash"] = dash_path

            self.logger.info(f"Generated tiled manifests: {list(manifests.keys())}")
            return manifests

        except Exception as e:
            self.logger.error(f"Failed to generate tiled manifests: {e}")
            raise
