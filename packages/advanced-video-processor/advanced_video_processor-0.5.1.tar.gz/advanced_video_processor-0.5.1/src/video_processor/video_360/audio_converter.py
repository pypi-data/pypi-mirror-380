"""Spatial audio format conversion and processing."""

import asyncio
import logging
import subprocess
from pathlib import Path

from ..constants import AUDIO
from .models import SpatialAudioType

logger = logging.getLogger(__name__)


class AudioConverter:
    """Handles conversion between spatial audio formats."""

    def __init__(self):
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    async def convert_to_binaural(
        self,
        input_path: Path,
        output_path: Path,
        source_format: SpatialAudioType,
        head_rotation: tuple[float, float, float] = (0, 0, 0),
    ) -> bool:
        """
        Convert spatial audio to binaural format for headphone playback.

        Args:
            input_path: Source video with spatial audio
            output_path: Output video with binaural audio
            source_format: Source spatial audio format
            head_rotation: Head rotation as (yaw, pitch, roll) in degrees
        """
        try:
            # Build conversion filter based on source format
            if source_format == SpatialAudioType.AMBISONIC_BFORMAT:
                audio_filter = self._build_ambisonic_to_binaural_filter(head_rotation)
            elif source_format == SpatialAudioType.AMBISONIC_HOA:
                audio_filter = self._build_hoa_to_binaural_filter(head_rotation)
            else:
                # For other formats, use generic spatial conversion
                audio_filter = self._build_generic_binaural_filter(head_rotation)

            # FFmpeg command for binaural conversion
            cmd = [
                "ffmpeg",
                "-i", str(input_path),
                "-af", audio_filter,
                "-c:v", "copy",  # Copy video unchanged
                "-c:a", "aac",   # Encode audio as AAC
                "-b:a", "192k",  # High-quality audio bitrate
                str(output_path),
                "-y",
            ]

            result = await asyncio.to_thread(
                subprocess.run, cmd, capture_output=True, text=True
            )

            if result.returncode == 0:
                self.logger.info(f"Converted to binaural: {output_path}")
                return True
            else:
                self.logger.error(f"Binaural conversion failed: {result.stderr}")
                return False

        except Exception as e:
            self.logger.error(f"Binaural conversion error: {e}")
            return False

    async def extract_ambisonic_channels(
        self,
        input_path: Path,
        output_dir: Path,
        format_type: SpatialAudioType = SpatialAudioType.AMBISONIC_BFORMAT,
    ) -> list[Path]:
        """Extract individual channels from ambisonic audio."""
        try:
            extracted_paths = []

            if format_type == SpatialAudioType.AMBISONIC_BFORMAT:
                # B-format has 4 channels: W, X, Y, Z
                channel_names = ["W", "X", "Y", "Z"]
                channel_count = 4
            else:
                # HOA formats have more channels
                channel_count = 16  # Common HOA configuration
                channel_names = [f"Ch{i:02d}" for i in range(channel_count)]

            # Extract each channel
            for i, name in enumerate(channel_names):
                output_path = output_dir / f"ambisonic_{name}.wav"

                cmd = [
                    "ffmpeg",
                    "-i", str(input_path),
                    "-af", f"pan=mono|c0=c{i}",  # Extract channel i
                    "-c:a", "pcm_s24le",        # High-quality PCM
                    str(output_path),
                    "-y",
                ]

                result = await asyncio.to_thread(
                    subprocess.run, cmd, capture_output=True, text=True
                )

                if result.returncode == 0:
                    extracted_paths.append(output_path)
                    self.logger.info(f"Extracted channel {name}: {output_path}")
                else:
                    self.logger.warning(f"Failed to extract channel {name}: {result.stderr}")

            return extracted_paths

        except Exception as e:
            self.logger.error(f"Channel extraction error: {e}")
            return []

    async def create_ambisonic_from_channels(
        self,
        channel_paths: list[Path],
        output_path: Path,
        format_type: SpatialAudioType = SpatialAudioType.AMBISONIC_BFORMAT,
    ) -> bool:
        """Create ambisonic audio from individual channel files."""
        try:
            if format_type == SpatialAudioType.AMBISONIC_BFORMAT and len(channel_paths) != 4:
                raise ValueError("B-format requires exactly 4 channels")

            # Build input arguments
            input_args = []
            for path in channel_paths:
                input_args.extend(["-i", str(path)])

            # Build channel mapping for ambisonic format
            if format_type == SpatialAudioType.AMBISONIC_BFORMAT:
                channel_layout = "quad"
            else:
                # HOA format - map all available channels
                "|".join(f"{i}:0" for i in range(len(channel_paths)))
                channel_layout = f"{len(channel_paths)}c"

            cmd = [
                "ffmpeg",
                *input_args,
                "-filter_complex", f"amerge=inputs={len(channel_paths)}",
                "-ac", str(len(channel_paths)),
                "-channel_layout", channel_layout,
                "-c:a", "pcm_s24le",
                str(output_path),
                "-y",
            ]

            result = await asyncio.to_thread(
                subprocess.run, cmd, capture_output=True, text=True
            )

            if result.returncode == 0:
                self.logger.info(f"Created ambisonic audio: {output_path}")
                return True
            else:
                self.logger.error(f"Ambisonic creation failed: {result.stderr}")
                return False

        except Exception as e:
            self.logger.error(f"Ambisonic creation error: {e}")
            return False

    def _build_ambisonic_to_binaural_filter(self, rotation: tuple[float, float, float]) -> str:
        """Build FFmpeg filter for ambisonic B-format to binaural conversion."""
        yaw, pitch, roll = rotation

        # Get coefficients from constants
        w_coeff = AUDIO["ambisonic_bformat"]["w_coefficient"]
        xyz_coeff = AUDIO["ambisonic_bformat"]["xyz_coefficient"]
        z_pitch_coeff = AUDIO["ambisonic_bformat"]["z_pitch_coefficient"]

        # Use FFmpeg's ambisonic decoder with HRTF
        # This is a simplified implementation - full implementation would use
        # proper HRTF databases and ambisonic decoding matrices
        return (
            f"pan=stereo|"
            f"FL={w_coeff}*c0+{xyz_coeff}*c1*cos({yaw}*PI/180)+{xyz_coeff}*c2*sin({yaw}*PI/180)+{z_pitch_coeff}*c3*sin({pitch}*PI/180)|"
            f"FR={w_coeff}*c0-{xyz_coeff}*c1*cos({yaw}*PI/180)-{xyz_coeff}*c2*sin({yaw}*PI/180)-{z_pitch_coeff}*c3*sin({pitch}*PI/180)"
        )

    def _build_hoa_to_binaural_filter(self, rotation: tuple[float, float, float]) -> str:
        """Build FFmpeg filter for HOA to binaural conversion."""
        # HOA binaural decoding is more complex and would typically require
        # specialized libraries. This is a simplified approach.
        yaw, pitch, roll = rotation

        # Get coefficients from constants
        w_coeff = AUDIO["hoa"]["w_coefficient"]
        xyz_coeff = AUDIO["hoa"]["xyz_coefficient"]
        ho_coeff = AUDIO["hoa"]["high_order_coefficient"]

        return (
            f"pan=stereo|"
            f"FL={w_coeff}*c0+{xyz_coeff}*c1*cos({yaw}*PI/180)+{xyz_coeff}*c2*sin({yaw}*PI/180)+{ho_coeff}*c3|"
            f"FR={w_coeff}*c0-{xyz_coeff}*c1*cos({yaw}*PI/180)-{xyz_coeff}*c2*sin({yaw}*PI/180)-{ho_coeff}*c3"
        )

    def _build_generic_binaural_filter(self, rotation: tuple[float, float, float]) -> str:
        """Build generic spatial to binaural conversion filter."""
        yaw, pitch, roll = rotation

        # Get coefficients from constants
        main_coeff = AUDIO["generic_spatial"]["main_coefficient"]
        cross_coeff = AUDIO["generic_spatial"]["cross_coefficient"]
        center_coeff = AUDIO["generic_spatial"]["center_coefficient"]

        # Generic spatial audio to stereo conversion with positioning
        return (
            f"pan=stereo|"
            f"FL={main_coeff}*FL+{cross_coeff}*FR+{center_coeff}*FC*cos({yaw}*PI/180)|"
            f"FR={main_coeff}*FR+{cross_coeff}*FL+{center_coeff}*FC*cos({yaw}*PI/180)"
        )

    def get_supported_conversions(self) -> dict[SpatialAudioType, list[SpatialAudioType]]:
        """Get supported audio format conversions."""
        return {
            SpatialAudioType.AMBISONIC_BFORMAT: [
                SpatialAudioType.BINAURAL,
                SpatialAudioType.AMBISONIC_HOA,
            ],
            SpatialAudioType.AMBISONIC_HOA: [
                SpatialAudioType.BINAURAL,
                SpatialAudioType.AMBISONIC_BFORMAT,
            ],
            SpatialAudioType.OBJECT_BASED: [
                SpatialAudioType.BINAURAL,
            ],
            SpatialAudioType.BINAURAL: [
                SpatialAudioType.HEAD_LOCKED,
            ],
        }
