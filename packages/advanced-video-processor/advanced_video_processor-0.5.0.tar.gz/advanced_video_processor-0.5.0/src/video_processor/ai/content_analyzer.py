"""Computer vision-enhanced video content analysis orchestrator."""

import asyncio
import json
import logging
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ..constants import THUMBNAILS
from .motion_detector import MotionDetector
from .quality_assessor import QualityAssessor, QualityMetrics
from .scene_analyzer import SceneAnalysis, SceneAnalyzer
from .video_360_analyzer import Video360Analysis, Video360Analyzer

logger = logging.getLogger(__name__)


@dataclass
class ContentAnalysis:
    """Complete video content analysis results."""

    # Video metadata
    duration: float
    width: int
    height: int
    fps: float
    codec: str

    # Scene analysis
    scene_analysis: SceneAnalysis

    # Quality metrics
    quality_metrics: QualityMetrics

    # Motion analysis
    has_motion: bool
    motion_intensity: float
    motion_patterns: str

    # 360° analysis (if applicable)
    video_360_analysis: Video360Analysis | None = None

    # Thumbnail recommendations
    recommended_timestamps: list[float] = None


class VideoContentAnalyzer:
    """
    Orchestrates video content analysis using specialized analyzers.

    Coordinates scene detection, quality assessment, motion analysis,
    and 360° video analysis through focused specialized classes.
    """

    def __init__(self, enable_opencv: bool = True) -> None:
        # Initialize specialized analyzers
        self.scene_analyzer = SceneAnalyzer()
        self.quality_assessor = QualityAssessor(enable_opencv)
        self.motion_detector = MotionDetector()
        self.video_360_analyzer = Video360Analyzer()

        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")
        self.logger.info(f"VideoContentAnalyzer initialized with OpenCV: {self.quality_assessor.enable_opencv}")

    async def analyze_content(self, video_path: Path) -> ContentAnalysis:
        """
        Perform comprehensive video content analysis.

        Orchestrates all specialized analyzers to provide complete analysis
        of video content, quality, motion, and 360° characteristics.
        """
        try:
            # Get basic video metadata
            metadata = await self._get_video_metadata(video_path)

            # Run analysis components in parallel for performance
            scene_task = self.scene_analyzer.analyze_scenes(video_path, metadata["duration"])
            quality_task = self.quality_assessor.assess_quality(video_path)
            motion_task = self.motion_detector.detect_motion(video_path, metadata["duration"])
            video_360_task = self.video_360_analyzer.analyze_360_content(video_path, metadata["probe_info"])

            # Wait for all analyses to complete
            scene_analysis, quality_metrics, motion_data, video_360_analysis = await asyncio.gather(
                scene_task, quality_task, motion_task, video_360_task
            )

            # Generate thumbnail recommendations
            recommended_timestamps = self._recommend_thumbnails(
                scene_analysis, motion_data, metadata["duration"]
            )

            return ContentAnalysis(
                # Basic metadata
                duration=metadata["duration"],
                width=metadata["width"],
                height=metadata["height"],
                fps=metadata["fps"],
                codec=metadata["codec"],

                # Analysis results
                scene_analysis=scene_analysis,
                quality_metrics=quality_metrics,
                has_motion=motion_data["has_motion"],
                motion_intensity=motion_data["motion_intensity"],
                motion_patterns=motion_data["motion_patterns"],
                video_360_analysis=video_360_analysis if video_360_analysis.is_360_video else None,
                recommended_timestamps=recommended_timestamps,
            )

        except Exception as e:
            self.logger.error(f"Content analysis failed for {video_path}: {e}")
            raise

    async def _get_video_metadata(self, video_path: Path) -> dict[str, Any]:
        """Extract basic video metadata using ffprobe."""
        cmd = [
            "ffprobe",
            "-v", "quiet",
            "-print_format", "json",
            "-show_format",
            "-show_streams",
            str(video_path),
        ]

        result = await asyncio.to_thread(
            subprocess.run, cmd, capture_output=True, text=True
        )

        if result.returncode != 0:
            raise RuntimeError(f"ffprobe failed: {result.stderr}")

        probe_info = json.loads(result.stdout)

        # Extract video stream info
        video_stream = next(
            (s for s in probe_info["streams"] if s["codec_type"] == "video"),
            None
        )

        if not video_stream:
            raise ValueError("No video stream found")

        return {
            "duration": float(probe_info["format"]["duration"]),
            "width": int(video_stream["width"]),
            "height": int(video_stream["height"]),
            "fps": eval(video_stream["r_frame_rate"]),  # Convert "30/1" to 30.0
            "codec": video_stream["codec_name"],
            "probe_info": probe_info,
        }

    def _recommend_thumbnails(
        self, scene_analysis: SceneAnalysis, motion_data: dict[str, Any], duration: float
    ) -> list[float]:
        """Generate thumbnail timestamp recommendations."""
        recommendations = []

        # Start with scene key moments
        recommendations.extend(scene_analysis.key_moments)

        # Add time-based recommendations for longer videos
        if duration > THUMBNAILS["long_video_threshold"]:
            # Add middle timestamp for longer videos
            middle_time = duration / 2
            if not any(abs(t - middle_time) < 5 for t in recommendations):
                recommendations.append(middle_time)

        # Ensure minimum timestamp
        recommendations = [
            max(t, THUMBNAILS["minimum_timestamp"]) for t in recommendations
        ]

        # Sort and limit recommendations
        recommendations = sorted(set(recommendations))
        return recommendations[:THUMBNAILS["max_recommendations"]]

    @staticmethod
    def is_analysis_available() -> bool:
        """Check if full content analysis is available."""
        return QualityAssessor.is_analysis_available()

    @staticmethod
    def get_missing_dependencies() -> list[str]:
        """Get list of missing dependencies for full analysis."""
        return QualityAssessor.get_missing_dependencies()
