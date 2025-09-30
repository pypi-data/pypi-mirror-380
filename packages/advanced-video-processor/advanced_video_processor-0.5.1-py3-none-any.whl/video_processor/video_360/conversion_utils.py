"""Utility functions for 360° video conversions."""

import logging
from pathlib import Path

from ..constants import VIDEO_360
from .models import ProjectionType

logger = logging.getLogger(__name__)


class ConversionUtils:
    """Utility functions for 360° video conversion operations."""

    def __init__(self):
        # Mapping of projection types to FFmpeg v360 format codes
        self.projection_formats = {
            ProjectionType.EQUIRECTANGULAR: "e",
            ProjectionType.CUBEMAP: "c3x2",
            ProjectionType.EAC: "eac",
            ProjectionType.FISHEYE: "fisheye",
            ProjectionType.DUAL_FISHEYE: "dfisheye",
            ProjectionType.CYLINDRICAL: "cylindrical",
            ProjectionType.STEREOGRAPHIC: "sg",
            ProjectionType.PANNINI: "pannini",
            ProjectionType.MERCATOR: "mercator",
            ProjectionType.LITTLE_PLANET: "sg",  # Same as stereographic
            ProjectionType.FLAT: "flat",
            ProjectionType.HALF_EQUIRECTANGULAR: "hequirect",
        }

        # Quality presets for different conversion scenarios
        self.quality_presets = {
            "fast": {"preset": "fast", "crf": "26"},
            "balanced": {"preset": "medium", "crf": "23"},
            "quality": {"preset": "slow", "crf": "20"},
            "archive": {"preset": "veryslow", "crf": "18"},
        }

    def get_supported_projections(self) -> list[ProjectionType]:
        """Get list of supported projection types."""
        return list(self.projection_formats.keys())

    def get_conversion_matrix(self) -> dict[ProjectionType, list[ProjectionType]]:
        """Get matrix of supported conversions between projection types."""
        conversions = {}

        # Most projections can convert to most others
        all_projections = self.get_supported_projections()

        for source in all_projections:
            conversions[source] = [
                target for target in all_projections if target != source
            ]

        # Special restrictions for some projections
        # Dual fisheye typically only converts to equirectangular
        conversions[ProjectionType.DUAL_FISHEYE] = [
            ProjectionType.EQUIRECTANGULAR,
            ProjectionType.FLAT,
        ]

        return conversions

    def build_v360_filter(
        self,
        source_proj: ProjectionType,
        target_proj: ProjectionType,
        output_resolution: tuple[int, int] | None = None,
        custom_params: dict | None = None,
    ) -> str:
        """
        Build FFmpeg v360 filter string.

        Args:
            source_proj: Source projection type
            target_proj: Target projection type
            output_resolution: Optional (width, height) for output
            custom_params: Custom projection-specific parameters

        Returns:
            FFmpeg v360 filter string
        """
        source_format = self.projection_formats.get(source_proj, "e")
        target_format = self.projection_formats.get(target_proj, "e")

        filter_parts = [f"v360={source_format}:{target_format}"]

        # Add resolution if specified
        if output_resolution:
            filter_parts.append(f"w={output_resolution[0]}:h={output_resolution[1]}")

        # Add projection-specific parameters
        if target_proj == ProjectionType.STEREOGRAPHIC:
            # Little planet effect parameters
            filter_parts.extend([
                "pitch=-90",  # Look down for little planet
                "h_fov=360",
                "v_fov=180",
            ])

        elif target_proj == ProjectionType.FISHEYE:
            # Fisheye parameters
            filter_parts.extend(["h_fov=190", "v_fov=190"])

        elif target_proj == ProjectionType.PANNINI:
            # Pannini projection parameters
            filter_parts.extend(["h_fov=120", "v_fov=90"])

        elif source_proj == ProjectionType.DUAL_FISHEYE:
            # Dual fisheye specific handling
            filter_parts.extend([
                "ih_flip=1",  # Input horizontal flip
                "iv_flip=1",  # Input vertical flip
            ])

        # Apply custom parameters if provided
        if custom_params:
            for key, value in custom_params.items():
                filter_parts.append(f"{key}={value}")

        return ":".join(filter_parts)

    def build_conversion_command(
        self,
        ffmpeg_path: str,
        input_path: Path,
        output_path: Path,
        v360_filter: str,
        quality_preset: str = "balanced",
        preserve_metadata: bool = True,
        target_projection: ProjectionType | None = None,
        extra_args: list[str] | None = None,
    ) -> list[str]:
        """
        Build complete FFmpeg command for conversion.

        Args:
            ffmpeg_path: Path to ffmpeg executable
            input_path: Source video path
            output_path: Output video path
            v360_filter: Pre-built v360 filter string
            quality_preset: Quality preset name
            preserve_metadata: Whether to preserve spherical metadata
            target_projection: Target projection type for metadata
            extra_args: Additional FFmpeg arguments

        Returns:
            Complete FFmpeg command as list
        """
        # Get quality settings
        quality_settings = self.quality_presets.get(
            quality_preset, self.quality_presets["balanced"]
        )

        cmd = [
            ffmpeg_path,
            "-i",
            str(input_path),
            "-vf",
            v360_filter,
            "-c:v",
            "libx264",
            "-preset",
            quality_settings["preset"],
            "-crf",
            quality_settings["crf"],
            "-c:a",
            "copy",  # Copy audio unchanged
            "-movflags",
            "+faststart",  # Web-friendly
        ]

        # Add metadata preservation
        if preserve_metadata and target_projection and target_projection != ProjectionType.FLAT:
            cmd.extend([
                "-metadata",
                "spherical=1",
                "-metadata",
                f"projection={target_projection.value}",
                "-metadata",
                "stitched=1",
            ])

        # Add extra arguments if provided
        if extra_args:
            cmd.extend(extra_args)

        cmd.extend([str(output_path), "-y"])

        return cmd

    def estimate_conversion_time(
        self,
        source_projection: ProjectionType,
        target_projection: ProjectionType,
        input_resolution: tuple[int, int],
        duration_seconds: float,
        quality_preset: str = "balanced",
    ) -> dict:
        """
        Estimate conversion time and resource requirements.

        Args:
            source_projection: Source projection
            target_projection: Target projection
            input_resolution: Input video resolution (width, height)
            duration_seconds: Input video duration
            quality_preset: Quality preset used

        Returns:
            Dictionary with time and resource estimates
        """
        try:
            # Base processing rate (pixels per second, rough estimate)
            base_rates = {
                "fast": 3000000,     # 3M pixels per second
                "balanced": 2000000,  # 2M pixels per second
                "quality": 1200000,   # 1.2M pixels per second
                "archive": 800000,    # 800K pixels per second
            }

            base_rate = base_rates.get(quality_preset, base_rates["balanced"])

            # Complexity multipliers for different conversion pairs
            complexity_multipliers = {
                (ProjectionType.EQUIRECTANGULAR, ProjectionType.CUBEMAP): VIDEO_360["conversion"]["complexity_multipliers"]["equirectangular_to_cubemap"],
                (ProjectionType.EQUIRECTANGULAR, ProjectionType.STEREOGRAPHIC): VIDEO_360["conversion"]["complexity_multipliers"]["equirectangular_to_stereographic"],
                (ProjectionType.EQUIRECTANGULAR, ProjectionType.FISHEYE): VIDEO_360["conversion"]["complexity_multipliers"]["equirectangular_to_fisheye"],
                (ProjectionType.CUBEMAP, ProjectionType.EQUIRECTANGULAR): VIDEO_360["conversion"]["complexity_multipliers"]["cubemap_to_equirectangular"],
                (ProjectionType.FISHEYE, ProjectionType.EQUIRECTANGULAR): VIDEO_360["conversion"]["complexity_multipliers"]["fisheye_to_equirectangular"],
                (ProjectionType.DUAL_FISHEYE, ProjectionType.EQUIRECTANGULAR): VIDEO_360["conversion"]["complexity_multipliers"]["dual_fisheye_to_equirectangular"],
                (ProjectionType.EAC, ProjectionType.EQUIRECTANGULAR): VIDEO_360["conversion"]["complexity_multipliers"]["eac_to_equirectangular"],
                (ProjectionType.STEREOGRAPHIC, ProjectionType.EQUIRECTANGULAR): VIDEO_360["conversion"]["complexity_multipliers"]["stereographic_to_equirectangular"],
            }

            # Calculate total pixels to process
            width, height = input_resolution
            total_pixels = width * height * duration_seconds * 30  # Assume 30fps

            # Get complexity multiplier
            conversion_pair = (source_projection, target_projection)
            multiplier = complexity_multipliers.get(conversion_pair, VIDEO_360["conversion"]["complexity_multipliers"]["default"])

            # Estimate time
            estimated_time = (total_pixels / base_rate) * multiplier

            # Add overhead for I/O, initialization, etc.
            estimated_time *= VIDEO_360["conversion"]["processing_overhead"]

            # Calculate resource estimates
            file_size_mb = (width * height * duration_seconds * 30 * 3) / (1024 * 1024)  # Rough estimate

            return {
                "estimated_time_seconds": max(estimated_time, VIDEO_360["conversion"]["minimum_time_seconds"]),  # Minimum 1 second
                "estimated_time_minutes": max(estimated_time / 60, VIDEO_360["conversion"]["minimum_time_minutes"]),  # Minimum 1.2 seconds
                "complexity_multiplier": multiplier,
                "base_processing_rate": base_rate,
                "quality_preset": quality_preset,
                "estimated_cpu_usage_percent": min(70 + (multiplier * 15), 95),
                "estimated_memory_mb": min(VIDEO_360["conversion"]["memory_base_mb"] + (file_size_mb * VIDEO_360["conversion"]["memory_multiplier"]), VIDEO_360["conversion"]["memory_max_mb"]),
                "input_resolution": input_resolution,
                "total_pixels": total_pixels,
            }

        except Exception as e:
            logger.error(f"Estimation error: {e}")
            return {
                "estimated_time_seconds": "unknown",
                "error": str(e),
            }

    def validate_conversion_feasibility(
        self,
        source_projection: ProjectionType,
        target_projection: ProjectionType,
    ) -> tuple[bool, str]:
        """
        Validate if a conversion between projections is feasible.

        Args:
            source_projection: Source projection type
            target_projection: Target projection type

        Returns:
            Tuple of (is_feasible, reason_if_not)
        """
        # Check if projections are supported
        if source_projection not in self.projection_formats:
            return False, f"Unsupported source projection: {source_projection.value}"

        if target_projection not in self.projection_formats:
            return False, f"Unsupported target projection: {target_projection.value}"

        # Check conversion matrix
        conversion_matrix = self.get_conversion_matrix()
        supported_targets = conversion_matrix.get(source_projection, [])

        if target_projection not in supported_targets:
            return False, f"Conversion from {source_projection.value} to {target_projection.value} not supported"

        # Special validation for complex conversions
        if source_projection == ProjectionType.DUAL_FISHEYE and target_projection != ProjectionType.EQUIRECTANGULAR:
            return False, "Dual fisheye should first be converted to equirectangular"

        return True, "Conversion is feasible"

    def get_recommended_resolution(
        self,
        source_projection: ProjectionType,
        target_projection: ProjectionType,
        source_resolution: tuple[int, int],
    ) -> tuple[int, int]:
        """
        Get recommended output resolution for conversion.

        Args:
            source_projection: Source projection type
            target_projection: Target projection type
            source_resolution: Source video resolution

        Returns:
            Recommended output resolution (width, height)
        """
        width, height = source_resolution

        # Resolution adjustments for different projection types
        if target_projection == ProjectionType.CUBEMAP:
            # Cubemap typically needs different aspect ratio
            if source_projection == ProjectionType.EQUIRECTANGULAR:
                # 2:1 -> 3:2 aspect ratio
                return (width, int(width * 2 / 3))

        elif target_projection == ProjectionType.STEREOGRAPHIC:
            # Stereographic (little planet) works well as square
            size = min(width, height)
            return (size, size)

        elif target_projection == ProjectionType.FISHEYE:
            # Fisheye works well as square
            size = min(width, height)
            return (size, size)

        elif target_projection == ProjectionType.FLAT:
            # Flat viewport extraction - standard video aspect ratios
            return (1920, 1080)  # Default to 1080p

        # Default: maintain source resolution
        return source_resolution
