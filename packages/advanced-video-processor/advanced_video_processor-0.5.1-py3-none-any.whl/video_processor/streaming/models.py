"""Data models for adaptive streaming."""

from dataclasses import dataclass
from pathlib import Path


@dataclass
class BitrateLevel:
    """Represents a single bitrate level in adaptive streaming."""

    name: str
    width: int
    height: int
    bitrate: int  # kbps
    max_bitrate: int  # kbps
    codec: str
    container: str


@dataclass
class StreamingPackage:
    """Complete adaptive streaming package."""

    video_id: str
    source_path: Path
    output_dir: Path
    hls_playlist: Path | None = None
    dash_manifest: Path | None = None
    bitrate_levels: list[BitrateLevel] = None
    segment_duration: int = 6  # seconds
    thumbnail_track: Path | None = None
    metadata: dict | None = None
