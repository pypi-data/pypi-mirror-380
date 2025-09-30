"""Playlist and manifest generation for adaptive streaming."""

import logging
from pathlib import Path

from ..config import ProcessorConfig

logger = logging.getLogger(__name__)


class PlaylistGenerator:
    """Handles HLS playlist and DASH manifest generation."""

    def __init__(self, config: ProcessorConfig) -> None:
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.config = config

    async def generate_hls_playlist(
        self, bitrate_levels: list, output_dir: Path, video_id: str
    ) -> Path:
        """Generate HLS master playlist."""
        playlist_path = output_dir / f"{video_id}_master.m3u8"

        try:
            with open(playlist_path, "w") as f:
                f.write("#EXTM3U\n")
                f.write("#EXT-X-VERSION:6\n\n")

                for level in bitrate_levels:
                    # Individual stream playlist
                    stream_playlist = f"{video_id}_{level.name}.m3u8"

                    f.write(
                        f'#EXT-X-STREAM-INF:BANDWIDTH={level.bitrate * 1000},'
                        f'RESOLUTION={level.width}x{level.height},'
                        f'CODECS="avc1.42e01e"\n'
                    )
                    f.write(f"{stream_playlist}\n")

            self.logger.info(f"Generated HLS master playlist: {playlist_path}")
            return playlist_path

        except Exception as e:
            self.logger.error(f"Failed to generate HLS playlist: {e}")
            raise

    async def generate_dash_manifest(
        self, bitrate_levels: list, output_dir: Path, video_id: str
    ) -> Path:
        """Generate DASH MPD manifest."""
        manifest_path = output_dir / f"{video_id}.mpd"

        try:
            with open(manifest_path, "w") as f:
                # Basic MPD structure
                f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
                f.write('<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" ')
                f.write('type="static" mediaPresentationDuration="PT0H0M30S" ')
                f.write('profiles="urn:mpeg:dash:profile:isoff-main:2011">\n')

                f.write("  <Period>\n")
                f.write("    <AdaptationSet mimeType=\"video/mp4\" ")
                f.write('codecs="avc1.42e01e">\n')

                for i, level in enumerate(bitrate_levels):
                    f.write(
                        f'      <Representation id="{i}" '
                        f'bandwidth="{level.bitrate * 1000}" '
                        f'width="{level.width}" height="{level.height}">\n'
                    )
                    f.write(f'        <BaseURL>{video_id}_{level.name}.mp4</BaseURL>\n')
                    f.write("      </Representation>\n")

                f.write("    </AdaptationSet>\n")
                f.write("  </Period>\n")
                f.write("</MPD>\n")

            self.logger.info(f"Generated DASH manifest: {manifest_path}")
            return manifest_path

        except Exception as e:
            self.logger.error(f"Failed to generate DASH manifest: {e}")
            raise

    async def generate_thumbnail_track(
        self, source_video: Path, output_dir: Path, video_id: str
    ) -> Path:
        """Generate thumbnail track for adaptive streaming."""
        import subprocess

        from ..constants import THUMBNAILS

        thumbnail_path = output_dir / f"{video_id}_thumbnails.jpg"

        try:
            # Generate thumbnail sprite using FFmpeg
            cmd = [
                self.config.ffmpeg_path,
                "-i",
                str(source_video),
                "-vf",
                f"fps=1/{THUMBNAILS['sprite_interval']},scale={THUMBNAILS['sprite_tile_size']},tile={THUMBNAILS['sprite_grid']}",
                "-y",
                str(thumbnail_path),
            ]

            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode != 0:
                raise RuntimeError(f"Thumbnail generation failed: {result.stderr}")

            self.logger.info(f"Generated thumbnail track: {thumbnail_path}")
            return thumbnail_path

        except Exception as e:
            self.logger.error(f"Failed to generate thumbnail track: {e}")
            raise
