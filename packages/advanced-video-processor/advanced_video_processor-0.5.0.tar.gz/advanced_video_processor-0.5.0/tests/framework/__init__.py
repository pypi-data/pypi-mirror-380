"""Video Processor Testing Framework

A comprehensive testing framework designed specifically for video processing applications,
featuring modern HTML reports with video themes, parallel execution, and quality metrics.
"""

__version__ = "1.0.0"
__author__ = "Video Processor Testing Framework"

from .config import TestingConfig
from .fixtures import VideoTestFixtures
from .quality import QualityMetricsCalculator
from .reporters import ConsoleReporter, HTMLReporter, JSONReporter

__all__ = [
    "HTMLReporter",
    "JSONReporter",
    "ConsoleReporter",
    "VideoTestFixtures",
    "QualityMetricsCalculator",
    "TestingConfig",
]
