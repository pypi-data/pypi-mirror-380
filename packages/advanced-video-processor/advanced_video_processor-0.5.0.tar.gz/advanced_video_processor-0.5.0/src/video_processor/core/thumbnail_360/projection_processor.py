"""360° projection processing for various viewing angles."""

import logging
import math
from pathlib import Path
from typing import Literal

from ...config import ProcessorConfig
from ...constants import THUMBNAILS

# Optional dependency handling
try:
    import cv2
    import numpy as np

    HAS_OPENCV = True
except ImportError:
    HAS_OPENCV = False

ViewingAngle = Literal["front", "back", "left", "right", "up", "down", "stereographic"]

logger = logging.getLogger(__name__)


class ProjectionProcessor:
    """Handles 360° projections for different viewing angles."""

    def __init__(self, config: ProcessorConfig) -> None:
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.config = config

        if not HAS_OPENCV:
            raise ImportError(
                "Projection processing requires opencv-python. "
                "Install with: uv add opencv-python"
            )

    def generate_angle_thumbnail(
        self,
        equirect_img: "np.ndarray",
        viewing_angle: ViewingAngle,
        output_dir: Path,
        video_id: str,
        timestamp: int,
    ) -> Path:
        """Generate thumbnail for a specific viewing angle."""
        output_path = output_dir / f"{video_id}_360_{viewing_angle}_{timestamp}.jpg"

        if viewing_angle == "stereographic":
            # Generate "little planet" stereographic projection
            thumbnail = self.create_stereographic_projection(equirect_img)
        else:
            # Generate perspective projection for the viewing angle
            thumbnail = self.create_perspective_projection(equirect_img, viewing_angle)

        # Save thumbnail with high quality
        cv2.imwrite(
            str(output_path),
            thumbnail,
            [cv2.IMWRITE_JPEG_QUALITY, THUMBNAILS["quality"]]
        )

        return output_path

    def create_perspective_projection(
        self, equirect_img: "np.ndarray", viewing_angle: ViewingAngle
    ) -> "np.ndarray":
        """Create perspective projection for a viewing angle."""
        height, width = equirect_img.shape[:2]

        # Define viewing directions (yaw, pitch) in radians
        viewing_directions = {
            "front": (0, 0),
            "back": (math.pi, 0),
            "left": (-math.pi / 2, 0),
            "right": (math.pi / 2, 0),
            "up": (0, math.pi / 2),
            "down": (0, -math.pi / 2),
        }

        if viewing_angle not in viewing_directions:
            viewing_angle = "front"

        yaw, pitch = viewing_directions[viewing_angle]

        # Generate perspective view
        thumbnail_size = self.config.thumbnail_width
        fov = math.pi / 3  # 60 degrees field of view

        # Create coordinate maps for perspective projection
        u_map, v_map = self._create_perspective_maps(
            thumbnail_size, thumbnail_size, fov, yaw, pitch, width, height
        )

        # Apply remapping
        thumbnail = cv2.remap(equirect_img, u_map, v_map, cv2.INTER_LINEAR)

        return thumbnail

    def create_stereographic_projection(
        self, equirect_img: "np.ndarray"
    ) -> "np.ndarray":
        """Create stereographic 'little planet' projection."""
        height, width = equirect_img.shape[:2]

        # Output size for stereographic projection
        output_size = self.config.thumbnail_width

        # Create coordinate maps for stereographic projection
        y_coords, x_coords = np.mgrid[0:output_size, 0:output_size]

        # Convert to centered coordinates
        x_centered = (x_coords - output_size // 2) / (output_size // 2)
        y_centered = (y_coords - output_size // 2) / (output_size // 2)

        # Calculate distance from center
        r = np.sqrt(x_centered**2 + y_centered**2)

        # Create mask for circular boundary
        mask = r <= 1.0

        # Convert to spherical coordinates for stereographic projection
        theta = np.arctan2(y_centered, x_centered)
        phi = 2 * np.arctan(r)

        # Convert to equirectangular coordinates
        u = (theta + np.pi) / (2 * np.pi) * width
        v = (np.pi / 2 - phi) / np.pi * height

        # Clamp coordinates
        u = np.clip(u, 0, width - 1)
        v = np.clip(v, 0, height - 1)

        # Create maps for remapping
        u_map = u.astype(np.float32)
        v_map = v.astype(np.float32)

        # Apply remapping
        thumbnail = cv2.remap(equirect_img, u_map, v_map, cv2.INTER_LINEAR)

        # Apply circular mask
        thumbnail[~mask] = [0, 0, 0]  # Black background

        return thumbnail

    def _create_perspective_maps(
        self,
        out_width: int,
        out_height: int,
        fov: float,
        yaw: float,
        pitch: float,
        equirect_width: int,
        equirect_height: int,
    ) -> tuple["np.ndarray", "np.ndarray"]:
        """Create coordinate mapping for perspective projection."""
        # Create output coordinate grids
        y_coords, x_coords = np.mgrid[0:out_height, 0:out_width]

        # Convert to normalized device coordinates [-1, 1]
        x_ndc = (x_coords - out_width / 2) / (out_width / 2)
        y_ndc = (y_coords - out_height / 2) / (out_height / 2)

        # Apply perspective projection
        focal_length = 1.0 / math.tan(fov / 2)

        # Create 3D ray directions
        x_3d = x_ndc / focal_length
        y_3d = y_ndc / focal_length
        z_3d = np.ones_like(x_3d)

        # Normalize ray directions
        ray_length = np.sqrt(x_3d**2 + y_3d**2 + z_3d**2)
        x_3d /= ray_length
        y_3d /= ray_length
        z_3d /= ray_length

        # Apply rotation for viewing direction
        # Rotate by yaw (around Y axis)
        cos_yaw, sin_yaw = math.cos(yaw), math.sin(yaw)
        x_rot = x_3d * cos_yaw - z_3d * sin_yaw
        z_rot = x_3d * sin_yaw + z_3d * cos_yaw

        # Rotate by pitch (around X axis)
        cos_pitch, sin_pitch = math.cos(pitch), math.sin(pitch)
        y_rot = y_3d * cos_pitch - z_rot * sin_pitch
        z_final = y_3d * sin_pitch + z_rot * cos_pitch

        # Convert 3D coordinates to spherical
        theta = np.arctan2(x_rot, z_final)
        phi = np.arcsin(np.clip(y_rot, -1, 1))

        # Convert spherical to equirectangular coordinates
        u = (theta + np.pi) / (2 * np.pi) * equirect_width
        v = (np.pi / 2 - phi) / np.pi * equirect_height

        # Clamp to image boundaries
        u = np.clip(u, 0, equirect_width - 1)
        v = np.clip(v, 0, equirect_height - 1)

        return u.astype(np.float32), v.astype(np.float32)
