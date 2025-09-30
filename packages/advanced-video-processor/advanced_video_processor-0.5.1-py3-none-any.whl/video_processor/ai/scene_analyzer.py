"""Scene detection and analysis for video content."""

import asyncio
import logging
import subprocess
from dataclasses import dataclass
from pathlib import Path

from ..constants import SCENE_DETECTION

logger = logging.getLogger(__name__)


@dataclass
class SceneAnalysis:
    """Scene detection analysis results."""

    scene_boundaries: list[float]  # Timestamps in seconds
    scene_count: int
    average_scene_length: float
    key_moments: list[float]  # Most important timestamps for thumbnails
    confidence_scores: list[float]  # Confidence for each scene boundary


class SceneAnalyzer:
    """Handles scene detection and temporal analysis of video content."""

    def __init__(self):
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    async def analyze_scenes(self, video_path: Path, duration: float) -> SceneAnalysis:
        """
        Detect scene boundaries and key moments in video.

        Uses FFmpeg's scene detection filter for accurate boundary detection.
        Falls back to time-based segmentation if FFmpeg analysis fails.
        """
        try:
            # Use FFmpeg scene detection
            scene_cmd = [
                "ffmpeg",
                "-i", str(video_path),
                "-vf", f"select='gt(scene,{SCENE_DETECTION['scene_threshold']}),"
                      f"showinfo'",
                "-f", "null",
                "-",
            ]

            result = await asyncio.to_thread(
                subprocess.run, scene_cmd, capture_output=True, text=True, timeout=60
            )

            if result.returncode == 0:
                boundaries = self._parse_scene_boundaries(result.stderr)
                if boundaries:
                    return self._create_scene_analysis(boundaries, duration)

            # Fallback to time-based analysis
            self.logger.warning("FFmpeg scene detection failed, using fallback")
            return self._fallback_scene_analysis(duration)

        except Exception as e:
            self.logger.error(f"Scene analysis error: {e}")
            return self._fallback_scene_analysis(duration)

    def _parse_scene_boundaries(self, ffmpeg_output: str) -> list[float]:
        """Parse scene boundaries from FFmpeg showinfo output."""
        boundaries = []

        for line in ffmpeg_output.split('\n'):
            if 'pts_time:' in line:
                try:
                    # Extract timestamp from showinfo output
                    time_part = line.split('pts_time:')[1].split()[0]
                    timestamp = float(time_part)
                    boundaries.append(timestamp)
                except (IndexError, ValueError):
                    continue

        return sorted(set(boundaries))  # Remove duplicates and sort

    def _generate_fallback_scenes(self, duration: float) -> list[float]:
        """Generate scene boundaries based on video duration when detection fails."""
        if duration <= SCENE_DETECTION["short_video_threshold"]:
            return []  # Short videos don't need scene breaks

        if duration <= SCENE_DETECTION["medium_video_threshold"]:
            return [duration / 2]  # Single scene break for medium videos

        # For long videos, create evenly spaced scenes
        max_scenes = SCENE_DETECTION["max_scenes"]
        scene_length = duration / min(max_scenes, int(duration / 30))  # ~30s per scene

        return [i * scene_length for i in range(1, int(duration / scene_length))]

    def _fallback_scene_analysis(self, duration: float) -> SceneAnalysis:
        """Create scene analysis using fallback time-based segmentation."""
        boundaries = self._generate_fallback_scenes(duration)
        return self._create_scene_analysis(boundaries, duration)

    def _create_scene_analysis(self, boundaries: list[float], duration: float) -> SceneAnalysis:
        """Create SceneAnalysis from detected boundaries."""
        scene_count = len(boundaries) + 1  # +1 because boundaries create N+1 scenes

        if scene_count > 1:
            scene_lengths = []
            prev_time = 0.0

            for boundary in boundaries:
                scene_lengths.append(boundary - prev_time)
                prev_time = boundary

            # Add final scene length
            scene_lengths.append(duration - prev_time)
            average_length = sum(scene_lengths) / len(scene_lengths)
        else:
            average_length = duration

        # Generate key moments for thumbnails
        key_moments = self._extract_key_moments(boundaries, duration)

        # Confidence scores (higher for FFmpeg detection, lower for fallback)
        confidence = SCENE_DETECTION["fallback_confidence"] if not boundaries else 0.9
        confidence_scores = [confidence] * len(boundaries)

        return SceneAnalysis(
            scene_boundaries=boundaries,
            scene_count=scene_count,
            average_scene_length=average_length,
            key_moments=key_moments,
            confidence_scores=confidence_scores,
        )

    def _extract_key_moments(self, boundaries: list[float], duration: float) -> list[float]:
        """Extract key timestamps for thumbnail generation."""
        if not boundaries:
            # For single scene, pick moments throughout the video
            if duration < 30:
                return [duration / 2]
            return [duration * 0.25, duration * 0.5, duration * 0.75]

        key_moments = []
        prev_time = 0.0

        for boundary in boundaries:
            # Pick a key moment within each scene
            scene_length = boundary - prev_time
            if scene_length > 5:  # Only add if scene is long enough
                key_moment = prev_time + (scene_length * SCENE_DETECTION["key_moment_offset"])
                key_moments.append(key_moment)
            prev_time = boundary

        # Add key moment for final scene
        final_scene_length = duration - prev_time
        if final_scene_length > 5:
            key_moment = prev_time + (final_scene_length * SCENE_DETECTION["key_moment_offset"])
            key_moments.append(key_moment)

        # Limit to max recommendations
        return key_moments[:SCENE_DETECTION["max_key_moments"]]
