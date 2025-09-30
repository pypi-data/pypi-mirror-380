"""Constants for video processor to eliminate magic numbers."""

# Quality assessment thresholds
QUALITY_THRESHOLDS = {
    "sharpness_good": 0.7,
    "brightness_optimal": 0.5,
    "brightness_tolerance": 0.3,
    "contrast_good": 0.6,
    "noise_acceptable": 0.3,
}

# Motion detection constants
MOTION_DETECTION = {
    "threshold": 0.1,  # Minimum intensity to consider as "has motion"
    "sample_duration": 10,  # Seconds to sample for motion analysis
    "frame_batch_size": 100,  # Frames to process for intensity calculation
    # Scene detection thresholds for motion analysis
    "scene_threshold": 0.1,  # FFmpeg scene detection sensitivity
    "frame_change_threshold": 1.0,  # Full change threshold
    "minimal_change": 0.1,  # Minimal motion detection
    # Motion intensity classification
    "high_motion_threshold": 0.7,  # Above this is high motion
    "moderate_motion_threshold": 0.3,  # Above this is moderate motion
    "static_intensity": 0.0,  # No motion detected
    # Confidence levels
    "high_confidence": 0.85,  # High confidence in detection
    "low_confidence": 0.3,  # Low confidence fallback
    "fallback_intensity": 0.4,  # Conservative estimate when detection fails
}

# 360° video constants
VIDEO_360 = {
    # Aspect ratio detection for equirectangular
    "equirectangular_aspect_min": 1.9,
    "equirectangular_aspect_max": 2.1,
    "equirectangular_precise_min": 1.98,  # More precise detection
    "equirectangular_precise_max": 2.02,
    # Additional aspect ratio thresholds
    "square_aspect_ratio": 1.0,
    "panoramic_aspect_min": 2.5,
    "dual_fisheye_aspect_min": 0.9,
    "dual_fisheye_aspect_max": 1.5,
    # Regional motion intensity multipliers (based on typical content patterns)
    "regional_multipliers": {
        "front": 1.0,  # Primary viewing area
        "back": 0.6,  # Less activity typically
        "left": 0.8,  # Side regions
        "right": 0.8,  # Side regions
        "up": 0.4,  # Sky/ceiling often static
        "down": 0.3,  # Ground/floor often static
        # Additional multipliers for regional motion enhancement
        "front_enhancement": 1.1,
        "back_reduction": 0.9,
        "vertical_reduction": 0.8,
    },
    # Quality scores by projection type
    "projection_quality": {
        "equirectangular": 0.7,  # Pole distortion issues
        "cubemap": 0.85,  # Good quality
        "eac": 0.9,  # Excellent quality
        "fisheye": 0.75,  # Decent quality
        "stereographic": 0.6,  # Lower quality due to extreme distortion
        "flat": 1.0,  # Perfect for non-360 content
    },
    # Quality assessment thresholds
    "quality_thresholds": {
        "high_confidence": 0.8,
        "medium_confidence": 0.6,
        "low_confidence": 0.3,
        "excellent_seam": 0.95,
        "good_seam": 0.9,
        "acceptable_seam": 0.7,
        "low_pole_distortion": 0.1,
        "moderate_pole_distortion": 0.2,
        "high_pole_distortion": 0.3,
        "max_pole_distortion": 0.3,
        "high_viewport_quality": 0.9,
        "moderate_viewport_quality": 0.7,
        "low_viewport_quality": 0.5,
        "default_fallback_quality": 0.5,
        "default_good_quality": 0.8,
        "motion_suitable_threshold": 0.8,
        "high_motion_threshold": 0.6,
        "very_high_motion": 0.7,
    },
    # Distortion calculation constants
    "distortion": {
        "height_normalization": 2160,  # 4K height for normalization
        "max_height_multiplier": 1.5,
        "height_distortion_factor": 0.25,  # Max 25% distortion at very high res
        "moderate_distortion": 0.15,
        "pole_normalization": 2000,  # 2K height for pole distortion
        "pole_max_factor": 0.3,  # Max 30% distortion
    },
    # Bitrate multipliers for 360° content
    "bitrate_multipliers": {
        "equirectangular": 2.8,  # Higher due to pole distortion
        "cubemap": 2.3,  # More efficient
        "eac": 2.5,  # YouTube optimized
        "fisheye": 2.2,  # Dual fisheye
        "stereographic": 2.0,  # Little planet style
        "default": 2.5,  # Conservative default
        "projection_efficiency": {
            "equirectangular": 1.4,  # Higher bitrate needed for pole distortion
            "cubemap": 1.2,  # Good compression efficiency
            "eac": 1.1,  # Excellent compression efficiency
            "fisheye": 1.3,  # Moderate efficiency
            "stereographic": 1.5,  # Less efficient
            "default": 1.2,  # Default conservative multiplier
        },
    },
    # Processing and conversion multipliers
    "conversion": {
        "complexity_multipliers": {
            "equirectangular_to_cubemap": 1.2,
            "equirectangular_to_stereographic": 1.5,
            "equirectangular_to_fisheye": 1.3,
            "cubemap_to_equirectangular": 1.1,
            "fisheye_to_equirectangular": 1.8,
            "dual_fisheye_to_equirectangular": 2.0,
            "eac_to_equirectangular": 1.4,
            "stereographic_to_equirectangular": 1.6,
            "default": 1.0,
        },
        "processing_overhead": 1.2,  # 20% processing overhead
        "minimum_time_seconds": 1.0,
        "minimum_time_minutes": 0.02,  # 1.2 seconds
        "memory_base_mb": 256,
        "memory_multiplier": 0.2,
        "memory_max_mb": 1024,
    },
}

# Scene detection constants
SCENE_DETECTION = {
    "scene_threshold": 0.3,  # FFmpeg scene detection threshold
    "max_key_moments": 5,  # Maximum key moments to extract
    "key_moment_offset": 0.3,  # Offset into scene for key moment
    "short_video_threshold": 30,  # Seconds - no scene breaks needed
    "medium_video_threshold": 120,  # Seconds - single scene break
    "max_scenes": 10,  # Maximum number of scenes to detect
    "fallback_confidence": 0.5,  # Confidence when using fallback detection
}

# Thumbnail generation constants
THUMBNAILS = {
    "max_recommendations": 5,  # Maximum thumbnail recommendations
    "minimum_timestamp": 5,  # Minimum seconds into video
    "quality_threshold": 0.5,  # Minimum quality for recommendations
    "long_video_threshold": 60,  # Seconds to add middle timestamp
    # Sprite sheet configuration
    "sprite_columns": 10,  # Thumbnails per row in sprite sheet
    "sprite_interval": 10,  # Seconds between sprite thumbnails
    "sprite_tile_size": "160:90",  # Size of individual sprite tiles
    "sprite_grid": "10x10",  # Grid layout for sprite sheet
    # Quality settings
    "quality": 85,  # JPEG quality for thumbnails
}

# File size limits and validation
VALIDATION = {
    "max_file_size_gb": 10,  # Maximum input file size
    "min_duration_seconds": 1,  # Minimum video duration
    "max_resolution_pixels": 8192,  # Maximum width/height
}

# Error handling
ERROR_HANDLING = {
    "max_retries": 3,  # Maximum retry attempts
    "retry_delay": 1.0,  # Seconds between retries
    "timeout_seconds": 300,  # FFmpeg operation timeout
}

# Audio processing constants
AUDIO = {
    # Ambisonic B-format coefficients for binaural conversion
    "ambisonic_bformat": {
        "w_coefficient": 0.707,  # W channel coefficient
        "xyz_coefficient": 0.5,  # X, Y, Z channel coefficients
        "z_pitch_coefficient": 0.25,  # Z channel pitch coefficient
    },
    # Higher Order Ambisonics coefficients
    "hoa": {
        "w_coefficient": 0.6,  # W channel coefficient
        "xyz_coefficient": 0.3,  # X, Y, Z channel coefficients
        "high_order_coefficient": 0.15,  # Higher order coefficient
    },
    # Generic spatial audio coefficients
    "generic_spatial": {
        "main_coefficient": 0.5,  # Main channel coefficient
        "cross_coefficient": 0.3,  # Cross-channel coefficient
        "center_coefficient": 0.2,  # Center channel coefficient
    },
    # Audio quality thresholds
    "quality_thresholds": {
        "rotation_left": 0.3,  # Left rotation audio coefficient
        "rotation_right": 0.7,  # Right rotation audio coefficient
        "balance_left": 0.1,  # Left balance coefficient
        "balance_right": 0.5,  # Right balance coefficient
    },
    # Audio rotation and positioning constants
    "rotation": {
        "pi_approximation": 3.14159,  # Pi approximation for angle conversion
        "front_facing_threshold": 15,  # Degrees - threshold for front-facing audio
        "behind_threshold": 90,  # Degrees - threshold for behind listener
        "center_threshold": 30,  # Degrees - threshold for centered audio
        "echo_gain": 0.8,  # Echo effect gain
        "echo_delay": 0.88,  # Echo delay factor
        "echo_decay_front": 0.4,  # Echo decay for front audio
        "echo_decay_side": 0.3,  # Echo decay for side audio
        "echo_time_multiplier": 10,  # Multiplier for yaw-based echo time
        "echo_time_multiplier_side": 5,  # Multiplier for side echo time
        "echo_base_time": 60,  # Base echo time for front-facing
    },
    # Pan coefficients for different positions
    "pan": {
        "centered": {
            "main": 0.5,  # Main channel mixing
            "cross": 0.3,  # Cross channel mixing
            "center": 0.2,  # Center channel mixing
        },
        "right_side": {
            "left_main": 0.3,  # Left channel from main
            "left_cross": 0.1,  # Left channel cross-mix
            "right_main": 0.7,  # Right channel from main
            "right_cross": 0.5,  # Right channel cross-mix
        },
        "left_side": {
            "left_main": 0.7,  # Left channel from main
            "left_cross": 0.5,  # Left channel cross-mix
            "right_main": 0.3,  # Right channel from main
            "right_cross": 0.1,  # Right channel cross-mix
        },
    },
}

# Encoding quality multipliers
ENCODING = {
    # Quality preset multipliers for processing time
    "time_multipliers": {
        "fast": 0.5,  # Fastest encoding
        "balanced": 1.0,  # Balanced speed/quality
        "quality": 2.0,  # Better quality
        "archive": 4.0,  # Best quality, slowest
    },
    # Projection complexity multipliers
    "projection_complexity": {
        "flat": 0.3,  # Flat viewport (simplest)
        "equirectangular": 1.0,  # Standard complexity
        "cubemap": 1.5,  # Moderate complexity
        "eac": 1.8,  # Higher complexity
        "fisheye": 1.2,  # Moderate complexity
        "stereographic": 2.0,  # Most complex
    },
    # Motion intensity multipliers for bitrate
    "motion_multipliers": {
        "base": 1.0,  # Base multiplier
        "motion_factor": 0.5,  # Factor applied to motion intensity
    },
    # Encoding parameter multipliers
    "bitrate_control": {
        "maxrate_multiplier": 1.2,  # Maxrate = bitrate * 1.2
        "bufsize_multiplier": 2.0,  # Buffer size = bitrate * 2.0
    },
}

# Codec specification constants
CODECS = {
    # HEVC profile specifications
    "hevc_profile": "hev1.1.6.L93.B0",
    # AV1 codec specifications
    "av1_profile": "av01.0.05M.08",
    # Processing speeds for different presets (pixels per second)
    "processing_speeds": {
        "av1": {
            "8": 500000,  # cpu-used=8 (fastest)
            "6": 300000,  # cpu-used=6 (balanced)
            "4": 150000,  # cpu-used=4 (quality)
            "2": 75000,  # cpu-used=2 (best quality)
        },
        "hevc": {
            "hardware": 8000000,  # Hardware encoding speed
            "fast": 2000000,  # Software fast preset
            "medium": 1500000,  # Software medium preset
            "slow": 800000,  # Software slow preset
            "veryslow": 400000,  # Software veryslow preset
        },
    },
    # Encoding overhead factors
    "overhead_factor": 1.2,  # 20% overhead for encoding
    "two_pass_factor": 2.2,  # Two-pass encoding overhead
}

# Transcription and speech processing constants
TRANSCRIPTION = {
    # Whisper model configurations
    "whisper_models": {
        "tiny": {"size": "tiny", "vram_gb": 1, "speed": "fastest", "accuracy": "basic"},
        "base": {"size": "base", "vram_gb": 1, "speed": "fast", "accuracy": "good"},
        "small": {"size": "small", "vram_gb": 2, "speed": "medium", "accuracy": "better"},
        "medium": {"size": "medium", "vram_gb": 5, "speed": "slow", "accuracy": "high"},
        "large": {"size": "large", "vram_gb": 10, "speed": "slowest", "accuracy": "best"},
    },

    # Audio extraction settings for optimal speech recognition
    "audio_extraction": {
        "sample_rate": 16000,  # 16kHz optimal for speech recognition
        "channels": 1,  # Mono channel
        "format": "wav",  # PCM format for whisper compatibility
        "codec": "pcm_s16le",  # 16-bit PCM little-endian
        "timeout_seconds": 300,  # 5 minute timeout for FFmpeg
    },

    # Ollama integration settings
    "ollama": {
        "default_host": "localhost",
        "default_port": 11434,
        "timeout_seconds": 60,
        "connection_timeout": 10,
        "preferred_models": ["gemma2:2b", "llama3.1:8b", "phi3:medium"],
        "temperature": 0.3,  # Lower temperature for accurate cleanup
        "top_p": 0.9,
        "max_tokens": 2000,
        "enhancement_min_length": 50,  # Minimum length to consider enhancement successful
    },

    # Output format configurations
    "output": {
        "generate_json": True,  # Detailed JSON with timestamps
        "generate_text": True,  # Clean readable text
        "generate_srt": False,  # SRT subtitle format (future feature)
        "generate_vtt": False,  # WebVTT subtitle format (future feature)
        "text_encoding": "utf-8",
        "json_indent": 2,
    },

    # Processing timeouts and limits
    "processing": {
        "max_video_duration_hours": 4,  # Maximum video length to process
        "batch_size_limit": 50,  # Maximum videos in batch operation
        "temp_cleanup": True,  # Auto-cleanup temporary audio files
        "retry_attempts": 3,  # Number of retry attempts for failed operations
        "retry_delay_seconds": 2.0,  # Delay between retry attempts
    },
}
