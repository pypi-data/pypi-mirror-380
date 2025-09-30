"""Video quality assessment using OpenCV computer vision algorithms."""

import logging
from dataclasses import dataclass
from pathlib import Path

from ..constants import QUALITY_THRESHOLDS

# Optional OpenCV dependency
try:
    import cv2
    import numpy as np
    HAS_OPENCV = True
except ImportError:
    HAS_OPENCV = False

logger = logging.getLogger(__name__)


@dataclass
class QualityMetrics:
    """Video quality assessment metrics."""

    sharpness_score: float  # 0-1, higher is sharper
    brightness_score: float  # 0-1, optimal around 0.5
    contrast_score: float  # 0-1, higher is more contrast
    noise_level: float  # 0-1, lower is better
    overall_quality: float  # 0-1, composite quality score


class QualityAssessor:
    """Assesses video quality using computer vision algorithms."""

    def __init__(self, enable_opencv: bool = True):
        self.enable_opencv = enable_opencv and HAS_OPENCV
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

        if not self.enable_opencv and HAS_OPENCV:
            self.logger.info("OpenCV available but disabled by configuration")
        elif not HAS_OPENCV:
            self.logger.warning("OpenCV not available, using fallback quality assessment")

    async def assess_quality(self, video_path: Path, sample_frames: int = 5) -> QualityMetrics:
        """
        Assess video quality using computer vision algorithms.

        Analyzes sample frames to determine sharpness, brightness, contrast, and noise levels.
        """
        if not self.enable_opencv:
            return self._fallback_quality_assessment()

        try:
            return await self._opencv_quality_analysis(video_path, sample_frames)
        except Exception as e:
            self.logger.error(f"OpenCV quality analysis failed: {e}")
            return self._fallback_quality_assessment()

    async def _opencv_quality_analysis(self, video_path: Path, sample_frames: int) -> QualityMetrics:
        """Perform actual computer vision quality analysis."""
        import asyncio

        def analyze_frames():
            cap = cv2.VideoCapture(str(video_path))

            if not cap.isOpened():
                raise ValueError(f"Cannot open video: {video_path}")

            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

            # Sample frames evenly throughout video
            frame_indices = np.linspace(0, total_frames - 1, sample_frames, dtype=int)

            sharpness_scores = []
            brightness_scores = []
            contrast_scores = []
            noise_scores = []

            for frame_idx in frame_indices:
                cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
                ret, frame = cap.read()

                if not ret:
                    continue

                # Convert to grayscale for analysis
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # 1. Sharpness: Laplacian variance
                laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
                sharpness = min(laplacian_var / 1000, 1.0)  # Normalize to 0-1
                sharpness_scores.append(sharpness)

                # 2. Brightness: Mean pixel intensity
                brightness = np.mean(gray) / 255.0
                brightness_scores.append(brightness)

                # 3. Contrast: Standard deviation of pixel intensities
                contrast = np.std(gray) / 128.0  # Normalize to 0-1 range
                contrast_scores.append(min(contrast, 1.0))

                # 4. Noise: High-frequency content using Sobel
                sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
                sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
                noise_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
                noise_level = min(np.mean(noise_magnitude) / 100, 1.0)
                noise_scores.append(noise_level)

            cap.release()

            # Calculate averages
            avg_sharpness = np.mean(sharpness_scores) if sharpness_scores else 0.0
            avg_brightness = np.mean(brightness_scores) if brightness_scores else 0.0
            avg_contrast = np.mean(contrast_scores) if contrast_scores else 0.0
            avg_noise = np.mean(noise_scores) if noise_scores else 1.0

            return avg_sharpness, avg_brightness, avg_contrast, avg_noise

        # Run OpenCV analysis in thread to avoid blocking
        sharpness, brightness, contrast, noise = await asyncio.to_thread(analyze_frames)

        # Calculate overall quality score
        overall_quality = self._calculate_overall_quality(sharpness, brightness, contrast, noise)

        return QualityMetrics(
            sharpness_score=sharpness,
            brightness_score=brightness,
            contrast_score=contrast,
            noise_level=noise,
            overall_quality=overall_quality,
        )

    def _calculate_overall_quality(self, sharpness: float, brightness: float, contrast: float, noise: float) -> float:
        """Calculate composite quality score using thresholds from constants."""
        # Sharpness contribution (30% weight)
        sharpness_weight = 0.3
        sharpness_contribution = sharpness * sharpness_weight

        # Brightness contribution (20% weight) - optimal around 0.5
        brightness_weight = 0.2
        brightness_optimal = QUALITY_THRESHOLDS["brightness_optimal"]
        brightness_tolerance = QUALITY_THRESHOLDS["brightness_tolerance"]
        brightness_distance = abs(brightness - brightness_optimal)
        brightness_score = max(0, 1 - (brightness_distance / brightness_tolerance))
        brightness_contribution = brightness_score * brightness_weight

        # Contrast contribution (30% weight)
        contrast_weight = 0.3
        contrast_contribution = contrast * contrast_weight

        # Noise contribution (20% weight) - lower is better
        noise_weight = 0.2
        noise_contribution = (1 - noise) * noise_weight

        overall = sharpness_contribution + brightness_contribution + contrast_contribution + noise_contribution
        return min(max(overall, 0.0), 1.0)  # Clamp to 0-1 range

    def _fallback_quality_assessment(self) -> QualityMetrics:
        """
        Fallback quality assessment when OpenCV is not available.

        Returns conservative estimates rather than fake random values.
        """
        self.logger.info("Using fallback quality assessment (no OpenCV)")

        return QualityMetrics(
            sharpness_score=0.6,  # Conservative estimate - moderate sharpness
            brightness_score=0.5,  # Assume optimal brightness
            contrast_score=0.6,   # Conservative estimate - moderate contrast
            noise_level=0.3,      # Assume acceptable noise level
            overall_quality=0.6,  # Conservative overall quality
        )

    @staticmethod
    def is_analysis_available() -> bool:
        """Check if full quality analysis is available."""
        return HAS_OPENCV

    @staticmethod
    def get_missing_dependencies() -> list[str]:
        """Get list of missing dependencies for quality analysis."""
        missing = []
        if not HAS_OPENCV:
            missing.append("opencv-python")
        return missing
