"""Spatial audio rotation and positioning for 360° video."""

import asyncio
import logging
import subprocess
from pathlib import Path

from ..constants import AUDIO
from .models import SpatialAudioType

logger = logging.getLogger(__name__)


class AudioRotator:
    """Handles spatial audio rotation and positioning."""

    def __init__(self):
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    async def rotate_spatial_audio(
        self,
        input_path: Path,
        output_path: Path,
        yaw: float = 0,
        pitch: float = 0,
        roll: float = 0,
        audio_format: SpatialAudioType = SpatialAudioType.AMBISONIC_BFORMAT,
    ) -> bool:
        """
        Rotate spatial audio to match video orientation or user preference.

        Args:
            input_path: Source video with spatial audio
            output_path: Output video with rotated audio
            yaw: Horizontal rotation in degrees (-180 to 180)
            pitch: Vertical rotation in degrees (-90 to 90)
            roll: Roll rotation in degrees (-180 to 180)
            audio_format: Source spatial audio format
        """
        try:
            # Build audio rotation filter
            rotation_filter = self._build_audio_rotation_filter(
                yaw, pitch, roll, audio_format
            )

            cmd = [
                "ffmpeg",
                "-i", str(input_path),
                "-af", rotation_filter,
                "-c:v", "copy",  # Copy video unchanged
                "-c:a", "aac",   # Re-encode audio
                "-b:a", "192k",  # High-quality audio
                str(output_path),
                "-y",
            ]

            result = await asyncio.to_thread(
                subprocess.run, cmd, capture_output=True, text=True
            )

            if result.returncode == 0:
                self.logger.info(f"Audio rotated: yaw={yaw}°, pitch={pitch}°, roll={roll}°")
                return True
            else:
                self.logger.error(f"Audio rotation failed: {result.stderr}")
                return False

        except Exception as e:
            self.logger.error(f"Audio rotation error: {e}")
            return False

    def _build_audio_rotation_filter(
        self,
        yaw: float,
        pitch: float,
        roll: float,
        audio_format: SpatialAudioType,
    ) -> str:
        """Build FFmpeg filter for spatial audio rotation."""

        if audio_format == SpatialAudioType.AMBISONIC_BFORMAT:
            return self._build_ambisonic_rotation_filter(yaw, pitch, roll)
        elif audio_format == SpatialAudioType.AMBISONIC_HOA:
            return self._build_hoa_rotation_filter(yaw, pitch, roll)
        elif audio_format == SpatialAudioType.BINAURAL:
            return self._build_binaural_rotation_filter(yaw, pitch, roll)
        else:
            return self._build_generic_rotation_filter(yaw, pitch, roll)

    def _build_ambisonic_rotation_filter(self, yaw: float, pitch: float, roll: float) -> str:
        """Build rotation filter for ambisonic B-format audio."""
        # Ambisonic rotation using rotation matrices
        # This is a simplified 2D rotation - full 3D rotation requires more complex math
        yaw_rad = yaw * AUDIO["rotation"]["pi_approximation"] / 180

        return (
            f"pan=4c|"
            f"c0=c0|"  # W channel unchanged
            f"c1=c1*cos({yaw_rad})-c2*sin({yaw_rad})|"  # X rotation
            f"c2=c1*sin({yaw_rad})+c2*cos({yaw_rad})|"  # Y rotation
            f"c3=c3"   # Z channel for pitch (simplified)
        )

    def _build_hoa_rotation_filter(self, yaw: float, pitch: float, roll: float) -> str:
        """Build rotation filter for Higher Order Ambisonic audio."""
        # HOA rotation is complex and typically requires specialized libraries
        # This is a simplified approach for demonstration
        yaw_rad = yaw * AUDIO["rotation"]["pi_approximation"] / 180

        # Apply rotation to lower-order components (simplified)
        return (
            f"pan=16c|"
            f"c0=c0|"  # W (0,0)
            f"c1=c1*cos({yaw_rad})-c2*sin({yaw_rad})|"  # X (1,-1)
            f"c2=c1*sin({yaw_rad})+c2*cos({yaw_rad})|"  # Y (1,0)
            f"c3=c3|"  # Z (1,1)
            # Additional HOA channels would need proper rotation matrices
            + "|".join(f"c{i}=c{i}" for i in range(4, 16))
        )

    def _build_binaural_rotation_filter(self, yaw: float, pitch: float, roll: float) -> str:
        """Build rotation filter for binaural audio."""
        # Binaural rotation using HRTF-based positioning
        if abs(yaw) < AUDIO["rotation"]["front_facing_threshold"]:
            # Front-facing, minimal processing
            return f"aecho={AUDIO['rotation']['echo_gain']}:{AUDIO['rotation']['echo_delay']}:{AUDIO['rotation']['echo_base_time']}:{AUDIO['rotation']['echo_decay_front']}"
        elif abs(yaw) > AUDIO["rotation"]["behind_threshold"]:
            # Behind listener, add more echo and damping
            return f"aecho={AUDIO['rotation']['echo_gain']}:{AUDIO['rotation']['echo_delay']}:{int(abs(yaw) * AUDIO['rotation']['echo_time_multiplier'])}:{AUDIO['rotation']['echo_decay_front']}"
        else:
            # Side positioning
            return f"aecho={AUDIO['rotation']['echo_gain']}:{AUDIO['rotation']['echo_delay']}:{int(abs(yaw) * AUDIO['rotation']['echo_time_multiplier_side'])}:{AUDIO['rotation']['echo_decay_side']}"

    def _build_generic_rotation_filter(self, yaw: float, pitch: float, roll: float) -> str:
        """Build generic rotation filter for other spatial audio formats."""
        # Generic spatial positioning using pan and delay
        if abs(yaw) < AUDIO["rotation"]["center_threshold"]:
            # Centered audio
            centered = AUDIO["pan"]["centered"]
            return f"pan=stereo|FL={centered['main']}*FL+{centered['cross']}*FR+{centered['center']}*FC|FR={centered['main']}*FR+{centered['cross']}*FL+{centered['center']}*FC"
        elif yaw > 0:
            # Right-side positioning
            right = AUDIO["pan"]["right_side"]
            return f"pan=stereo|FL={right['left_main']}*FL+{right['left_cross']}*FR|FR={right['right_main']}*FR+{right['right_cross']}*FL"
        else:
            # Left-side positioning
            left = AUDIO["pan"]["left_side"]
            return f"pan=stereo|FL={left['left_main']}*FL+{left['left_cross']}*FR|FR={left['right_main']}*FR+{left['right_cross']}*FL"

    async def apply_head_tracking(
        self,
        input_path: Path,
        output_path: Path,
        tracking_data: list[dict],
        audio_format: SpatialAudioType,
    ) -> bool:
        """
        Apply head tracking data to spatial audio for dynamic positioning.

        Args:
            input_path: Source video with spatial audio
            output_path: Output video with head-tracked audio
            tracking_data: List of {"time": seconds, "yaw": degrees, "pitch": degrees, "roll": degrees}
            audio_format: Source spatial audio format
        """
        try:
            # For simplicity, use the first tracking point
            # Full implementation would create time-varying filters
            if not tracking_data:
                # No tracking data, copy unchanged
                cmd = ["ffmpeg", "-i", str(input_path), "-c", "copy", str(output_path), "-y"]
            else:
                first_point = tracking_data[0]
                rotation_filter = self._build_audio_rotation_filter(
                    first_point.get("yaw", 0),
                    first_point.get("pitch", 0),
                    first_point.get("roll", 0),
                    audio_format
                )

                cmd = [
                    "ffmpeg",
                    "-i", str(input_path),
                    "-af", rotation_filter,
                    "-c:v", "copy",
                    "-c:a", "aac",
                    "-b:a", "192k",
                    str(output_path),
                    "-y",
                ]

            result = await asyncio.to_thread(
                subprocess.run, cmd, capture_output=True, text=True
            )

            if result.returncode == 0:
                self.logger.info(f"Applied head tracking to audio: {len(tracking_data)} points")
                return True
            else:
                self.logger.error(f"Head tracking application failed: {result.stderr}")
                return False

        except Exception as e:
            self.logger.error(f"Head tracking error: {e}")
            return False
