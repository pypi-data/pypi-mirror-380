"""360° thumbnail generation components."""

from .frame_extractor import Frame360Extractor
from .projection_processor import ProjectionProcessor, ViewingAngle
from .sprite_generator import Sprite360Generator
from .thumbnail_orchestrator import Thumbnail360Orchestrator

# Re-export for backward compatibility
__all__ = [
    "Thumbnail360Orchestrator",
    "Frame360Extractor",
    "ProjectionProcessor",
    "Sprite360Generator",
    "ViewingAngle",
]
